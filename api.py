import os
import logging
import threading
import time
from typing import List, Dict, Any, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import uvicorn

from main import traiter_question_bible, normaliser_niveau_utilisateur, MAX_QUESTION_LEN, MAX_QUESTION_MOTS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="BIBLE-IA PROD", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mémoire isolée par user
_memoire_users: Dict[str, List[Dict]] = {}
_lock_memoire = threading.Lock()
MAX_HIST_PER_USER = 6

def _get_historique(user_id: str):
    with _lock_memoire:
        return list(_memoire_users.get(user_id, []))

def _add_historique(user_id: str, q: str, r: str):
    with _lock_memoire:
        hist = _memoire_users.get(user_id, [])
        hist.append({"role": "user", "content": q[:1000]})
        hist.append({"role": "assistant", "content": r[:1500]})
        _memoire_users[user_id] = hist[-MAX_HIST_PER_USER:]

def _clear_historique(user_id: str):
    with _lock_memoire:
        _memoire_users.pop(user_id, None)

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)
    niveau: Optional[str] = "18+"
    user_id: Optional[str] = "default"
    historique: Optional[List[Dict[str, str]]] = None

@app.get("/health")
async def health():
    return {"status": "ok", "version": "2.0.0"}

@app.post("/clear")
async def clear(req: Request):
    body = await req.json()
    _clear_historique(body.get("user_id", "default"))
    return {"status": "cleared"}

@app.post("/ask")
async def ask(req: AskRequest):
    start = time.time()

    if len(req.question.split()) > MAX_QUESTION_MOTS:
        raise HTTPException(status_code=400, detail="Question trop longue")

    niveau = normaliser_niveau_utilisateur(req.niveau)
    historique = req.historique if req.historique is not None else _get_historique(req.user_id)

    resultat = traiter_question_bible(
        question=req.question,
        niveau_utilisateur=niveau,
        historique=historique
    )

    if resultat.get("erreur") == "validation":
        raise HTTPException(status_code=400, detail=resultat.get("reponse"))

    if resultat.get("erreur") == "Hors sujet":
        return {
            "reponse": resultat["reponse"],
            "references": [],
            "sources": [],
            "niveau_pertinence_top": "hors_sujet",
            "duree_ms": int((time.time()-start)*1000)
        }

    reponse = resultat.get("reponse", "")
    sources = resultat.get("sources", [])

    if reponse and not resultat.get("erreur"):
        _add_historique(req.user_id, req.question, reponse)

    return {
        "reponse": reponse,
        "references": resultat.get("references", [])[:5],
        "sources": [
            {
                "reference": s.get("reference"),
                "texte": s.get("texte", "")[:500],
                "niveau_pertinence": s.get("niveau_pertinence"),
                "est_reference_demandee": s.get("est_reference_demandee", False)
            } for s in sources[:5]
        ],
        "personnages": resultat.get("personnages", []),
        "niveau_pertinence_top": resultat.get("niveau_pertinence_top"),
        "duree_ms": int((time.time()-start)*1000)
    }

@app.exception_handler(Exception)
async def global_handler(request: Request, exc: Exception):
    logger.exception("Erreur globale")
    return JSONResponse(status_code=500, content={"detail": "Erreur interne, réessaye"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("api:app", host="0.0.0.0", port=port)
    