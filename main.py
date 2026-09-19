
# # ============================================================
# # BLOC 1/3 - CONFIG, NORMALISATION & DICTIONNAIRE PERSONNAGES
# # ============================================================

# import json
# import re
# import unicodedata
# import inspect
# from typing import Dict, List, Optional, Any

# from recherche_hybride import rechercher
# from generateur_reponse import generer_reponse_biblique


# # ============================================================
# # CONSTANTES GLOBALES
# # ============================================================

# MAX_HISTORIQUE_ENTRIES = 6
# MAX_LONGUEUR_ENTREE_HISTORIQUE = 3000
# MAX_LONGUEUR_HISTORIQUE_TOTAL = 12000

# MAX_QUESTION_LEN = 5000
# MAX_RESULTATS_PERSONNAGES = 12


# # ============================================================
# # NIVEAUX UTILISATEUR
# # ============================================================

# NIVEAUX_AUTORISES = {
#     "8-11",
#     "12-15",
#     "16-17",
#     "18+",
#     "approfondi",
# }


# def normaliser_niveau_utilisateur(
#     niveau_utilisateur: Optional[str],
# ) -> str:
#     """
#     Vérifie et normalise le niveau choisi par l'utilisateur.
#     """

#     if not niveau_utilisateur:
#         return "18+"

#     niveau = str(niveau_utilisateur).strip().lower()

#     correspondances = {
#         "8": "8-11",
#         "8-11": "8-11",
#         "8–11": "8-11",
#         "8_11": "8-11",
#         "8 à 11": "8-11",
#         "8 a 11": "8-11",

#         "12": "12-15",
#         "12-15": "12-15",
#         "12–15": "12-15",
#         "12_15": "12-15",
#         "12 à 15": "12-15",
#         "12 a 15": "12-15",

#         "16": "16-17",
#         "16-17": "16-17",
#         "16–17": "16-17",
#         "16_17": "16-17",
#         "16 à 17": "16-17",
#         "16 a 17": "16-17",

#         "18": "18+",
#         "18+": "18+",
#         "18 et plus": "18+",
#         "18 ans et plus": "18+",
#         "adulte": "18+",

#         "approfondi": "approfondi",
#         "approfondie": "approfondi",
#         "expert": "approfondi",
#         "detaille": "approfondi",
#         "détaillé": "approfondi",
#     }

#     return correspondances.get(niveau, "18+")


# # ============================================================
# # NORMALISATION DU TEXTE
# # ============================================================

# def normaliser_texte(texte: Any) -> str:
#     """
#     Normalise un texte pour faciliter les comparaisons :

#     - conversion en chaîne
#     - minuscules
#     - suppression des accents
#     - espaces normalisés
#     """

#     if texte is None:
#         return ""

#     texte = str(texte).lower().strip()

#     texte = unicodedata.normalize("NFD", texte)

#     texte = "".join(
#         caractere
#         for caractere in texte
#         if unicodedata.category(caractere) != "Mn"
#     )

#     texte = re.sub(r"\s+", " ", texte)

#     return texte


# def contient_terme(
#     texte: Any,
#     terme: Any,
# ) -> bool:
#     """
#     Vérifie qu'un terme apparaît comme un mot ou une expression
#     complète afin d'éviter les faux positifs.

#     Exemple :
#     "dan" ne doit pas être détecté dans "Daniel".
#     """

#     texte_normalise = normaliser_texte(texte)
#     terme_normalise = normaliser_texte(terme)

#     if not texte_normalise or not terme_normalise:
#         return False

#     motif = (
#         r"(?<!\w)"
#         + re.escape(terme_normalise)
#         + r"(?!\w)"
#     )

#     return re.search(
#         motif,
#         texte_normalise,
#     ) is not None


# # ============================================================
# # DICTIONNAIRE DES PERSONNAGES - PARTIE 1
# # ============================================================

# DICTIONNAIRE_PERSONNAGES: Dict[str, Dict[str, Any]] = {

#     # ========================================================
#     # PAUL / SAÜL
#     # ========================================================

#     "paul": {
#         "aliases": [
#             "saul de tarse",
#             "saül de tarse",
#             "saul",
#             "saül",
#             "paul",
#         ],

#         "profils": [

#             {
#                 "nom": "Saül de Tarse (l'apôtre Paul)",

#                 "aliases_specifiques": [
#                     "saul de tarse",
#                     "saül de tarse",
#                     "paul",
#                 ],

#                 "aliases_generiques": [
#                     "saul",
#                     "saül",
#                 ],

#                 "mots_forts": [
#                     "tarse",
#                     "damas",
#                     "apotre",
#                     "gentils",
#                     "epitres",
#                     "lettres",
#                     "persecuteur",
#                     "conversion",
#                     "missionnaire",
#                     "chretiens",
#                 ],

#                 "mots_contexte": [
#                     "eglise",
#                     "evangile",
#                     "mission",
#                     "voyage",
#                     "rome",
#                     "corinthe",
#                     "jerusalem",
#                     "paul",
#                 ],

#                 "requetes": [
#                     "Saül de Tarse conversion Actes",
#                     "Paul apôtre des gentils lettres",
#                     "Saül Damas persécution chrétiens",
#                 ],
#             },

#             {
#                 "nom": "Saül, premier roi d'Israël",

#                 "aliases_specifiques": [
#                     "saul roi",
#                     "saül roi",
#                     "premier roi d israel",
#                     "premier roi d'israel",
#                     "roi saul",
#                     "roi saül",
#                 ],

#                 "aliases_generiques": [
#                     "saul",
#                     "saül",
#                 ],

#                 "mots_forts": [
#                     "roi",
#                     "israel",
#                     "philistins",
#                     "kis",
#                     "cisch",
#                     "samuel",
#                     "gilboa",
#                     "jonathan",
#                     "royaume",
#                 ],

#                 "mots_contexte": [
#                     "david",
#                     "goliath",
#                     "berger",
#                     "combat",
#                     "arme",
#                     "ennemi",
#                     "trone",
#                 ],

#                 "requetes": [
#                     "Saül roi d'Israël Samuel",
#                     "Saül et David roi d'Israël",
#                     "Saül Philistins Jonathan",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # SIMON
#     # ========================================================

#     "simon": {
#         "aliases": [
#             "simon",
#             "simeon pierre",
#             "siméon pierre",
#             "simon pierre",
#             "cephas",
#             "céphas",
#         ],

#         "profils": [

#             {
#                 "nom": "Simon Pierre (l'apôtre Pierre)",

#                 "aliases_specifiques": [
#                     "simon pierre",
#                     "siméon pierre",
#                     "simeon pierre",
#                     "cephas",
#                     "céphas",
#                 ],

#                 "aliases_generiques": [
#                     "simon",
#                 ],

#                 "mots_forts": [
#                     "pierre",
#                     "apotre",
#                     "reniement",
#                     "renie",
#                     "renie jesus",
#                     "pentecote",
#                     "cephas",
#                     "cles",
#                     "corneille",
#                     "filets",
#                     "pecheur",
#                     "galilee",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "douze",
#                     "disciple",
#                     "appel",
#                     "peche",
#                     "pecher",
#                     "frere",
#                     "andre",
#                 ],

#                 "requetes": [
#                     "Simon Pierre apôtre Jésus",
#                     "Pierre reniement Jésus",
#                     "Pierre renie Jésus trois fois",
#                     "Jean 18 Pierre reniement Jésus",
#                     "Pierre Pentecôte Actes",
#                 ],
#             },

#             {
#                 "nom": "Simon le Zélote",

#                 "aliases_specifiques": [
#                     "simon le zelote",
#                     "simon le zélote",
#                     "simon zelote",
#                     "simon zélote",
#                 ],

#                 "aliases_generiques": [
#                     "simon",
#                 ],

#                 "mots_forts": [
#                     "zelote",
#                     "zélote",
#                     "douze",
#                     "disciple",
#                     "apotre",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "disciples",
#                 ],

#                 "requetes": [
#                     "Simon le Zélote disciple de Jésus",
#                     "Simon le Zélote apôtre",
#                 ],
#             },

#             {
#                 "nom": "Simon père de Judas Iscariot",

#                 "aliases_specifiques": [
#                     "simon pere de judas",
#                     "simon père de judas",
#                     "simon pere de judas iscariot",
#                     "simon père de judas iscariot",
#                 ],

#                 "aliases_generiques": [
#                     "simon",
#                 ],

#                 "mots_forts": [
#                     "judas iscariot",
#                     "judas",
#                     "iscariot",
#                     "pere de judas",
#                 ],

#                 "mots_contexte": [
#                     "pere",
#                 ],

#                 "requetes": [
#                     "Simon père de Judas Iscariot",
#                 ],
#             },

#             {
#                 "nom": "Simon le Pharisien",

#                 "aliases_specifiques": [
#                     "simon le pharisien",
#                 ],

#                 "aliases_generiques": [
#                     "simon",
#                 ],

#                 "mots_forts": [
#                     "pharisien",
#                     "pecheresse",
#                     "parfum",
#                     "repas",
#                     "maison",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "repas",
#                 ],

#                 "requetes": [
#                     "Simon le Pharisien Jésus",
#                     "Simon le Pharisien femme pécheresse",
#                 ],
#             },

#             {
#                 "nom": "Simon le lépreux",

#                 "aliases_specifiques": [
#                     "simon le lepreux",
#                     "simon le lépreux",
#                 ],

#                 "aliases_generiques": [
#                     "simon",
#                 ],

#                 "mots_forts": [
#                     "lepreux",
#                     "lépreux",
#                     "bethanie",
#                     "parfum",
#                 ],

#                 "mots_contexte": [
#                     "repas",
#                     "jesus",
#                 ],

#                 "requetes": [
#                     "Simon le lépreux Bethanie Jésus",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # MARIE
#     # ========================================================

#     "marie": {
#         "aliases": [
#             "marie",
#         ],

#         "profils": [

#             {
#                 "nom": "Marie, mère de Jésus",

#                 "aliases_specifiques": [
#                     "marie mere de jesus",
#                     "marie mère de jesus",
#                     "marie mere de dieu",
#                 ],

#                 "aliases_generiques": [
#                     "marie",
#                 ],

#                 "mots_forts": [
#                     "mere de jesus",
#                     "mere",
#                     "nazareth",
#                     "gabriel",
#                     "ange",
#                     "annonciation",
#                     "naissance",
#                     "bethleem",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "joseph",
#                     "enfant",
#                     "fils",
#                 ],

#                 "requetes": [
#                     "Marie mère de Jésus naissance",
#                     "Marie Joseph Jésus",
#                     "Marie annonciation Gabriel",
#                 ],
#             },

#             {
#                 "nom": "Marie de Magdala",

#                 "aliases_specifiques": [
#                     "marie de magdala",
#                     "marie magdala",
#                     "marie madeleine",
#                 ],

#                 "aliases_generiques": [
#                     "marie",
#                 ],

#                 "mots_forts": [
#                     "magdala",
#                     "madeleine",
#                     "tombeau",
#                     "resurrection",
#                     "ressuscite",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "croix",
#                     "disciples",
#                 ],

#                 "requetes": [
#                     "Marie de Magdala Jésus",
#                     "Marie Madeleine tombeau Jésus",
#                     "Marie de Magdala résurrection",
#                 ],
#             },

#             {
#                 "nom": "Marie de Béthanie",

#                 "aliases_specifiques": [
#                     "marie de bethanie",
#                     "marie bethanie",
#                 ],

#                 "aliases_generiques": [
#                     "marie",
#                 ],

#                 "mots_forts": [
#                     "bethanie",
#                     "marthe",
#                     "lazare",
#                     "parfum",
#                     "pieds",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "soeur",
#                     "frere",
#                 ],

#                 "requetes": [
#                     "Marie Marthe Lazare Bethanie",
#                     "Marie de Béthanie Jésus parfum",
#                     "Jean 11 Marie Marthe Lazare",
#                 ],
#             },

#             {
#                 "nom": "Marie, mère de Jacques et de Joses",

#                 "aliases_specifiques": [
#                     "marie mere de jacques",
#                     "marie mère de jacques",
#                     "marie mere de joses",
#                     "marie mère de joses",
#                 ],

#                 "aliases_generiques": [
#                     "marie",
#                 ],

#                 "mots_forts": [
#                     "jacques",
#                     "joses",
#                     "sepulcre",
#                     "tombeau",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "femme",
#                 ],

#                 "requetes": [
#                     "Marie mère de Jacques Joses",
#                 ],
#             },

#             {
#                 "nom": "Marie, mère de Jean-Marc",

#                 "aliases_specifiques": [
#                     "marie mere de jean marc",
#                     "marie mère de jean marc",
#                     "marie mere de jean-marc",
#                     "marie mère de jean-marc",
#                 ],

#                 "aliases_generiques": [
#                     "marie",
#                 ],

#                 "mots_forts": [
#                     "jean marc",
#                     "jean-marc",
#                     "marc",
#                     "maison",
#                     "priere",
#                 ],

#                 "mots_contexte": [
#                     "jerusalem",
#                     "pierre",
#                 ],

#                 "requetes": [
#                     "Marie mère de Jean Marc Actes",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # JEAN
#     # ========================================================

#     "jean": {
#         "aliases": [
#             "jean",
#         ],

#         "profils": [

#             {
#                 "nom": "Jean-Baptiste",

#                 "aliases_specifiques": [
#                     "jean baptiste",
#                     "jean-baptiste",
#                 ],

#                 "aliases_generiques": [
#                     "jean",
#                 ],

#                 "mots_forts": [
#                     "baptiste",
#                     "baptiser",
#                     "bapteme",
#                     "désert",
#                     "desert",
#                     "herode",
#                     "jean baptiste",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "prophete",
#                     "jordan",
#                     "fleuve",
#                 ],

#                 "requetes": [
#                     "Jean Baptiste Jésus baptême",
#                     "Jean Baptiste Hérode",
#                 ],
#             },

#             {
#                 "nom": "Jean, fils de Zébédée",

#                 "aliases_specifiques": [
#                     "jean fils de zebedee",
#                     "jean fils de zébédée",
#                     "jean de zebedee",
#                     "jean de zébédée",
#                 ],

#                 "aliases_generiques": [
#                     "jean",
#                 ],

#                 "mots_forts": [
#                     "zebedee",
#                     "zébédée",
#                     "jacques",
#                     "apotre",
#                     "douze",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "pecheur",
#                     "galilee",
#                 ],

#                 "requetes": [
#                     "Jean fils de Zébédée apôtre",
#                     "Jean Jacques Zébédée Jésus",
#                 ],
#             },

#             {
#                 "nom": "Jean-Marc",

#                 "aliases_specifiques": [
#                     "jean marc",
#                     "jean-marc",
#                 ],

#                 "aliases_generiques": [
#                     "jean",
#                 ],

#                 "mots_forts": [
#                     "marc",
#                     "maison",
#                     "barnabas",
#                     "pierre",
#                 ],

#                 "mots_contexte": [
#                     "jerusalem",
#                     "eglise",
#                 ],

#                 "requetes": [
#                     "Jean Marc Actes Barnabas Pierre",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # JACQUES
#     # ========================================================

#     "jacques": {
#         "aliases": [
#             "jacques",
#         ],

#         "profils": [

#             {
#                 "nom": "Jacques, fils de Zébédée",

#                 "aliases_specifiques": [
#                     "jacques fils de zebedee",
#                     "jacques fils de zébédée",
#                 ],

#                 "aliases_generiques": [
#                     "jacques",
#                 ],

#                 "mots_forts": [
#                     "zebedee",
#                     "zébédée",
#                     "jean",
#                     "herode",
#                     "épée",
#                     "epee",
#                 ],

#                 "mots_contexte": [
#                     "apotre",
#                     "douze",
#                     "jesus",
#                     "galilee",
#                 ],

#                 "requetes": [
#                     "Jacques fils de Zébédée Jean",
#                     "Jacques tué par Hérode Actes 12",
#                 ],
#             },

#             {
#                 "nom": "Jacques, fils d'Alphée",

#                 "aliases_specifiques": [
#                     "jacques fils d alphee",
#                     "jacques fils d'alphée",
#                     "jacques fils d'alphee",
#                 ],

#                 "aliases_generiques": [
#                     "jacques",
#                 ],

#                 "mots_forts": [
#                     "alphee",
#                     "alphée",
#                 ],

#                 "mots_contexte": [
#                     "apotre",
#                     "douze",
#                     "disciple",
#                 ],

#                 "requetes": [
#                     "Jacques fils d'Alphée apôtre",
#                 ],
#             },

#             {
#                 "nom": "Jacques, frère de Jésus",

#                 "aliases_specifiques": [
#                     "jacques frere de jesus",
#                     "jacques frère de jesus",
#                 ],

#                 "aliases_generiques": [
#                     "jacques",
#                 ],

#                 "mots_forts": [
#                     "frere de jesus",
#                     "frère de jesus",
#                     "jerusalem",
#                     "eglise",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "apotre",
#                     "lettre",
#                 ],

#                 "requetes": [
#                     "Jacques frère de Jésus Jérusalem",
#                     "Jacques église de Jérusalem",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # HÉRODE
#     # ========================================================

#     "herode": {
#         "aliases": [
#             "herode",
#             "hérode",
#         ],

#         "profils": [

#             {
#                 "nom": "Hérode le Grand",

#                 "aliases_specifiques": [
#                     "herode le grand",
#                     "hérode le grand",
#                 ],

#                 "aliases_generiques": [
#                     "herode",
#                     "hérode",
#                 ],

#                 "mots_forts": [
#                     "enfant",
#                     "bethleem",
#                     "mages",
#                     "magiciens",
#                     "massacre",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "naissance",
#                     "judee",
#                     "jerusalem",
#                 ],

#                 "requetes": [
#                     "Hérode le Grand Jésus enfant",
#                     "Hérode Bethléem mages",
#                 ],
#             },

#             {
#                 "nom": "Hérode Antipas",

#                 "aliases_specifiques": [
#                     "herode antipas",
#                     "hérode antipas",
#                 ],

#                 "aliases_generiques": [
#                     "herode",
#                     "hérode",
#                 ],

#                 "mots_forts": [
#                     "jean baptiste",
#                     "jean-baptiste",
#                     "salome",
#                     "herodias",
#                     "galilee",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "pilate",
#                     "roi",
#                 ],

#                 "requetes": [
#                     "Hérode Antipas Jean Baptiste",
#                     "Hérode Antipas Jésus",
#                 ],
#             },

#             {
#                 "nom": "Hérode Agrippa I",

#                 "aliases_specifiques": [
#                     "herode agrippa",
#                     "hérode agrippa",
#                     "herode agrippa premier",
#                     "hérode agrippa premier",
#                 ],

#                 "aliases_generiques": [
#                     "herode",
#                     "hérode",
#                 ],

#                 "mots_forts": [
#                     "jacques",
#                     "pierre",
#                     "persecution",
#                     "actes",
#                 ],

#                 "mots_contexte": [
#                     "eglise",
#                     "juifs",
#                 ],

#                 "requetes": [
#                     "Hérode Agrippa Jacques Pierre Actes",
#                 ],
#             },

#             {
#                 "nom": "Hérode Agrippa II",

#                 "aliases_specifiques": [
#                     "herode agrippa ii",
#                     "hérode agrippa ii",
#                     "agrippa ii",
#                     "agrippa 2",
#                     "agrippa deux",
#                 ],

#                 "aliases_generiques": [
#                     "herode",
#                     "hérode",
#                 ],

#                 "mots_forts": [
#                     "paul",
#                     "bernice",
#                     "festus",
#                     "cesar",
#                     "procès",
#                     "proces",
#                 ],

#                 "mots_contexte": [
#                     "actes",
#                     "roi",
#                 ],

#                 "requetes": [
#                     "Agrippa II Paul Festus Actes",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # JOSEPH
#     # ========================================================

#     "joseph": {
#         "aliases": [
#             "joseph",
#         ],

#         "profils": [

#             {
#                 "nom": "Joseph, fils de Jacob",

#                 "aliases_specifiques": [
#                     "joseph fils de jacob",
#                     "joseph vendu par ses freres",
#                     "joseph vendu par ses frères",
#                 ],

#                 "aliases_generiques": [
#                     "joseph",
#                 ],

#                 "mots_forts": [
#                     "jacob",
#                     "freres",
#                     "frères",
#                     "egypte",
#                     "égypte",
#                     "songe",
#                     "pharaon",
#                     "prison",
#                 ],

#                 "mots_contexte": [
#                     "genese",
#                     "robe",
#                     "reve",
#                     "rêve",
#                 ],

#                 "requetes": [
#                     "Joseph fils de Jacob vendu par ses frères",
#                     "Joseph Égypte Pharaon",
#                     "Joseph frères Genèse",
#                 ],
#             },

#             {
#                 "nom": "Joseph, époux de Marie",

#                 "aliases_specifiques": [
#                     "joseph epoux de marie",
#                     "joseph époux de marie",
#                     "joseph mari de marie",
#                     "joseph pere adoptif de jesus",
#                     "joseph père adoptif de jesus",
#                 ],

#                 "aliases_generiques": [
#                     "joseph",
#                 ],

#                 "mots_forts": [
#                     "marie",
#                     "jesus",
#                     "ange",
#                     "songe",
#                     "bethleem",
#                     "nazareth",
#                 ],

#                 "mots_contexte": [
#                     "enfant",
#                     "naissance",
#                     "famille",
#                 ],

#                 "requetes": [
#                     "Joseph mari de Marie Jésus",
#                     "Joseph naissance Jésus",
#                     "Joseph Nazareth Marie",
#                 ],
#             },

#             {
#                 "nom": "Joseph d'Arimathée",

#                 "aliases_specifiques": [
#                     "joseph d arimathee",
#                     "joseph d'arimathee",
#                     "joseph d arimathée",
#                     "joseph d'arimathée",
#                 ],

#                 "aliases_generiques": [
#                     "joseph",
#                 ],

#                 "mots_forts": [
#                     "arimathee",
#                     "arimathée",
#                     "tombeau",
#                     "sepulcre",
#                     "sépulcre",
#                     "corps",
#                 ],

#                 "mots_contexte": [
#                     "jesus",
#                     "crucifixion",
#                     "pilate",
#                 ],

#                 "requetes": [
#                     "Joseph d'Arimathée tombeau Jésus",
#                     "Joseph d'Arimathée Pilate",
#                 ],
#             },
#         ],
#     },
# }

# # ============================================================
# # BLOC 2/3 - DICTIONNAIRE (P2), NLP & RÉFÉRENCES BIBLIQUES
# # ============================================================


# # ============================================================
# # SUITE DU DICTIONNAIRE DES PERSONNAGES
# # ============================================================

# DICTIONNAIRE_PERSONNAGES.update({

#     # ========================================================
#     # SIMÉON
#     # ========================================================

#     "simeon": {
#         "aliases": [
#             "simeon",
#             "siméon",
#         ],

#         "profils": [

#             {
#                 "nom": "Siméon, fils de Jacob",

#                 "aliases_specifiques": [
#                     "simeon fils de jacob",
#                     "siméon fils de jacob",
#                 ],

#                 "aliases_generiques": [
#                     "simeon",
#                     "siméon",
#                 ],

#                 "mots_forts": [
#                     "jacob",
#                     "tribu",
#                     "freres",
#                     "frères",
#                 ],

#                 "mots_contexte": [
#                     "israel",
#                     "fils",
#                 ],

#                 "requetes": [
#                     "Siméon fils de Jacob tribu",
#                 ],
#             },

#             {
#                 "nom": "Siméon au temple",

#                 "aliases_specifiques": [
#                     "simeon au temple",
#                     "siméon au temple",
#                     "simeon qui a vu jesus",
#                     "siméon qui a vu jesus",
#                 ],

#                 "aliases_generiques": [
#                     "simeon",
#                     "siméon",
#                 ],

#                 "mots_forts": [
#                     "temple",
#                     "jesus",
#                     "enfant",
#                     "esprit saint",
#                     "esprit",
#                     "jerusalem",
#                 ],

#                 "mots_contexte": [
#                     "marie",
#                     "joseph",
#                     "luc",
#                 ],

#                 "requetes": [
#                     "Siméon temple Jésus enfant Luc 2",
#                     "Siméon bénit Jésus temple",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # DAVID
#     # ========================================================

#     "david": {
#         "aliases": [
#             "david",
#         ],

#         "profils": [
#             {
#                 "nom": "David, roi d'Israël",

#                 "aliases_specifiques": [
#                     "roi david",
#                     "david roi",
#                 ],

#                 "aliases_generiques": [
#                     "david",
#                 ],

#                 "mots_forts": [
#                     "roi",
#                     "goliath",
#                     "bethleem",
#                     "jonathan",
#                     "saul",
#                     "saül",
#                     "jerusalem",
#                     "psaumes",
#                     "psaume",
#                 ],

#                 "mots_contexte": [
#                     "berger",
#                     "onction",
#                     "royaume",
#                     "israel",
#                     "israël",
#                 ],

#                 "requetes": [
#                     "David roi Israël Saül",
#                     "David Goliath",
#                     "David Jonathan",
#                 ],
#             },
#         ],
#     },


#     # ========================================================
#     # PERSONNAGES UNIQUES AVEC PROFIL
#     # ========================================================

#     "ruth": {
#         "aliases": ["ruth"],
#         "profils": [
#             {
#                 "nom": "Ruth",
#                 "aliases_specifiques": ["ruth"],
#                 "aliases_generiques": [],
#                 "mots_forts": ["boaz", "naomi", "moab"],
#                 "mots_contexte": ["bled", "moisson"],
#                 "requetes": ["Ruth Naomi Boaz"],
#             }
#         ],
#     },

#     "moise": {
#         "aliases": ["moise", "moïse"],
#         "profils": [
#             {
#                 "nom": "Moïse",
#                 "aliases_specifiques": ["moise", "moïse"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "egypte",
#                     "pharaon",
#                     "mer rouge",
#                     "buisson",
#                     "sinai",
#                     "loi",
#                 ],
#                 "mots_contexte": ["aaron", "israel"],
#                 "requetes": [
#                     "Moïse Exode Pharaon",
#                     "Moïse Sinaï loi",
#                 ],
#             }
#         ],
#     },

#     "abraham": {
#         "aliases": ["abraham"],
#         "profils": [
#             {
#                 "nom": "Abraham",
#                 "aliases_specifiques": ["abraham"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "isaac",
#                     "sarah",
#                     "lot",
#                     "alliance",
#                 ],
#                 "mots_contexte": [
#                     "promesse",
#                     "canan",
#                 ],
#                 "requetes": [
#                     "Abraham Isaac Sarah alliance",
#                 ],
#             }
#         ],
#     },

#     "nebucadnetsar": {
#         "aliases": [
#             "nebucadnetsar",
#             "nebuchadnezzar",
#             "nabuchodonosor",
#         ],

#         "profils": [
#             {
#                 "nom": "Nebucadnetsar",

#                 "aliases_specifiques": [
#                     "nebucadnetsar",
#                     "nebuchadnezzar",
#                     "nabuchodonosor",
#                 ],

#                 "aliases_generiques": [],

#                 "mots_forts": [
#                     "babylone",
#                     "roi",
#                     "songe",
#                     "daniel",
#                     "statue",
#                 ],

#                 "mots_contexte": [
#                     "royaume",
#                     "fournaise",
#                 ],

#                 "requetes": [
#                     "Nebucadnetsar Daniel Babylone",
#                     "Nebucadnetsar songe statue",
#                 ],
#             }
#         ],
#     },

#     "salomon": {
#         "aliases": ["salomon"],
#         "profils": [
#             {
#                 "nom": "Salomon",
#                 "aliases_specifiques": ["salomon"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "sagesse",
#                     "temple",
#                     "roi",
#                     "david",
#                 ],
#                 "mots_contexte": [
#                     "proverbes",
#                     "jerusalem",
#                 ],
#                 "requetes": [
#                     "Salomon sagesse temple David",
#                 ],
#             }
#         ],
#     },

#     "elie": {
#         "aliases": ["elie", "elijah"],
#         "profils": [
#             {
#                 "nom": "Élie",
#                 "aliases_specifiques": ["elie", "elijah"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "baal",
#                     "carmel",
#                     "ahab",
#                     "feu",
#                     "prophète",
#                     "prophete",
#                 ],
#                 "mots_contexte": [
#                     "veuve",
#                     "corbeaux",
#                 ],
#                 "requetes": [
#                     "Élie prophète Carmel Baal",
#                     "Élie Ahab",
#                 ],
#             }
#         ],
#     },

#     "elisee": {
#         "aliases": ["elisee", "elisée"],
#         "profils": [
#             {
#                 "nom": "Élisée",
#                 "aliases_specifiques": ["elisee", "elisée"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "elie",
#                     "naaman",
#                     "elisée",
#                     "elisee",
#                 ],
#                 "mots_contexte": [
#                     "prophète",
#                     "prophete",
#                     "miracle",
#                 ],
#                 "requetes": [
#                     "Élisée Élie Naaman",
#                 ],
#             }
#         ],
#     },

#     "esther": {
#         "aliases": ["esther"],
#         "profils": [
#             {
#                 "nom": "Esther",
#                 "aliases_specifiques": ["esther"],
#                 "aliases_generiques": [],
#                 "mots_forts": [
#                     "mardochee",
#                     "aman",
#                     "perse",
#                     "reine",
#                 ],
#                 "mots_contexte": [
#                     "roi",
#                     "jeune fille",
#                 ],
#                 "requetes": [
#                     "Esther Mardochée Aman",
#                 ],
#             }
#         ],
#     },

#     "melchizedek": {
#         "aliases": [
#             "melchizedek",
#             "melchisédek",
#         ],

#         "profils": [
#             {
#                 "nom": "Melchisédek",

#                 "aliases_specifiques": [
#                     "melchizedek",
#                     "melchisédek",
#                 ],

#                 "aliases_generiques": [],

#                 "mots_forts": [
#                     "salem",
#                     "sacrificateur",
#                     "abraham",
#                 ],

#                 "mots_contexte": [
#                     "roi",
#                 ],

#                 "requetes": [
#                     "Melchisédek Abraham Salem",
#                 ],
#             }
#         ],
#     },

#     "methuselah": {
#         "aliases": [
#             "methuselah",
#             "mathusalem",
#             "mathusala",
#         ],

#         "profils": [
#             {
#                 "nom": "Mathusalem",

#                 "aliases_specifiques": [
#                     "methuselah",
#                     "mathusalem",
#                     "mathusala",
#                 ],

#                 "aliases_generiques": [],

#                 "mots_forts": [
#                     "noe",
#                     "enoch",
#                     "969",
#                 ],

#                 "mots_contexte": [
#                     "annees",
#                     "âge",
#                     "age",
#                 ],

#                 "requetes": [
#                     "Mathusalem Noé Enoch",
#                 ],
#             }
#         ],
#     },

#     "nehemie": {
#         "aliases": [
#             "nehemie",
#             "néhémie",
#         ],

#         "profils": [
#             {
#                 "nom": "Néhémie",

#                 "aliases_specifiques": [
#                     "nehemie",
#                     "néhémie",
#                 ],

#                 "aliases_generiques": [],

#                 "mots_forts": [
#                     "mur",
#                     "jerusalem",
#                     "perse",
#                 ],

#                 "mots_contexte": [
#                     "reconstruction",
#                     "roi",
#                 ],

#                 "requetes": [
#                     "Néhémie mur Jérusalem",
#                 ],
#             }
#         ],
#     },

#     "zerubbabel": {
#         "aliases": [
#             "zerubbabel",
#             "zorobabel",
#         ],

#         "profils": [
#             {
#                 "nom": "Zorobabel",

#                 "aliases_specifiques": [
#                     "zerubbabel",
#                     "zorobabel",
#                 ],

#                 "aliases_generiques": [],

#                 "mots_forts": [
#                     "temple",
#                     "babylone",
#                     "judee",
#                 ],

#                 "mots_contexte": [
#                     "reconstruction",
#                 ],

#                 "requetes": [
#                     "Zorobabel temple Jérusalem",
#                 ],
#             }
#         ],
#     },
# })


# # ============================================================
# # PERSONNAGES UNIQUES
# # ============================================================

# PERSONNAGES_UNIQUES = {
#     "noe", "noé",
#     "isaac",
#     "jacob",
#     "israel", "israël",
#     "lot",
#     "sara", "sarah",
#     "hagar",
#     "ishmael",
#     "ezekias",
#     "ezechias",
#     "josias",
#     "ozias",
#     "jeroboam",
#     "rehoboam",
#     "samuel",
#     "jonathan",
#     "jeremie", "jérémie",
#     "isaie", "isaïe",
#     "ezechiel",
#     "daniel",
#     "osée", "osee",
#     "joel",
#     "amos",
#     "abdias",
#     "jonas",
#     "michee", "michée",
#     "nahum",
#     "habacuc",
#     "sophonie",
#     "aggée", "aggee",
#     "zacharie",
#     "malachie",
#     "job",
#     "esdras",
#     "mardochee", "mardochée",
#     "gideon", "gédéon",
#     "samson",
#     "delila", "delilah",
#     "debora", "déborah",
#     "barak",
#     "jephte",
#     "caleb",
#     "josue", "josué",
#     "aaron",
#     "levi", "lévi",
#     "benjamin",
#     "reuben",
#     "juda", "judah",
#     "issacar",
#     "zebulon", "zabulon",
#     "dan",
#     "nephthali",
#     "gad",
#     "aser",
#     "ephraim", "éphraïm",
#     "manasse",
#     "barnabas",
#     "timothee", "timothée",
#     "tite",
#     "silas",
#     "etienne", "étienne",
#     "philippe",
#     "matthias",
#     "matthieu", "mathieu",
#     "marc",
#     "luc",
#     "marthe",
#     "lazare",
#     "nicodeme", "nicodème",
#     "zachee", "zachée",
#     "bartimee", "bartimée",
#     "jairus", "jaïrus",
#     "corneille",
#     "lydie",
#     "priscille",
#     "aquilas",
#     "pharaon",
#     "pilate",
#     "herodias", "hérodiade",
#     "barabbas",
#     "judas",
#     "thomas",
#     "andre", "andré",
# }


# # ============================================================
# # HORS SUJETS STRICTS
# # ============================================================

# HORS_SUJETS_STRICTS = [
#     "messi",
#     "ronaldo",
#     "football",
#     "meteo",
#     "météo",
#     "python",
#     "javascript",
#     "programme",
#     "programming",
#     "capitale",
#     "president",
#     "président",
#     "recette de cuisine",
#     "formule 1",
# ]


# # ============================================================
# # TERMES BIBLIQUES
# # ============================================================

# TERMES_BIBLIQUES = [
#     "bible",
#     "biblique",
#     "jesus",
#     "jésus",
#     "dieu",
#     "seigneur",
#     "christ",
#     "evangile",
#     "évangile",
#     "ancien testament",
#     "nouveau testament",
#     "apotre",
#     "apôtre",
#     "disciple",
#     "prophete",
#     "prophète",
#     "psaume",
#     "verset",
#     "chapitre",
#     "eglise",
#     "église",
#     "priere",
#     "prière",
#     "peche",
#     "péché",
#     "foi",
#     "amour",
#     "salut",
#     "grace",
#     "grâce",
# ]


# def est_hors_sujet_absolu(question: str) -> bool:
#     """
#     Bloque uniquement certains sujets explicitement étrangers
#     au domaine de BIBLE-IA.
#     """

#     question_normalisee = normaliser_texte(question)

#     return any(
#         contient_terme(question_normalisee, terme)
#         for terme in HORS_SUJETS_STRICTS
#     )


# # ============================================================
# # DÉTECTION DES ALIAS
# # ============================================================

# def detecter_alias_explicite(
#     question: str,
#     alias: str,
# ) -> bool:
#     return contient_terme(question, alias)


# def trouver_mentions_personnages(
#     question: str,
# ) -> List[Dict[str, Any]]:

#     mentions = []

#     for cle_famille, famille in DICTIONNAIRE_PERSONNAGES.items():

#         aliases_trouves = [
#             alias
#             for alias in famille["aliases"]
#             if detecter_alias_explicite(question, alias)
#         ]

#         if aliases_trouves:
#             mentions.append({
#                 "famille": cle_famille,
#                 "aliases": aliases_trouves,
#             })

#     return mentions


# # ============================================================
# # SCORE D'UN PROFIL
# # ============================================================

# def calculer_score_profil(
#     question: str,
#     profil: Dict[str, Any],
# ) -> Dict[str, Any]:

#     score = 0

#     aliases_specifiques_trouves = []
#     aliases_generiques_trouves = []

#     for alias in profil.get("aliases_specifiques", []):

#         if contient_terme(question, alias):
#             score += 100
#             aliases_specifiques_trouves.append(alias)

#     for alias in profil.get("aliases_generiques", []):

#         if contient_terme(question, alias):
#             score += 15
#             aliases_generiques_trouves.append(alias)

#     for mot in profil.get("mots_forts", []):

#         if contient_terme(question, mot):
#             score += 12

#     for mot in profil.get("mots_contexte", []):

#         if contient_terme(question, mot):
#             score += 4

#     return {
#         "score": score,
#         "aliases_specifiques": aliases_specifiques_trouves,
#         "aliases_generiques": aliases_generiques_trouves,
#     }


# # ============================================================
# # ANALYSE D'UNE FAMILLE DE PERSONNAGE
# # ============================================================

# def analyser_famille_personnage(
#     question: str,
#     famille: Dict[str, Any],
# ) -> Dict[str, Any]:

#     resultats = []

#     for profil in famille["profils"]:

#         analyse = calculer_score_profil(
#             question,
#             profil,
#         )

#         resultats.append({
#             "profil": profil,
#             "score": analyse["score"],
#             "aliases_specifiques": analyse["aliases_specifiques"],
#             "aliases_generiques": analyse["aliases_generiques"],
#         })

#     resultats.sort(
#         key=lambda resultat: resultat["score"],
#         reverse=True,
#     )

#     if not resultats:
#         return {
#             "statut": "ambigu",
#             "profil": None,
#             "score": 0,
#             "possibilites": [],
#         }

#     meilleur = resultats[0]

#     # Une seule possibilité.
#     if len(resultats) == 1:
#         return {
#             "statut": "identifie",
#             "profil": meilleur["profil"],
#             "score": meilleur["score"],
#             "possibilites": resultats,
#         }

#     # Un alias explicitement spécifique est prioritaire.
#     if meilleur["aliases_specifiques"]:
#         return {
#             "statut": "identifie",
#             "profil": meilleur["profil"],
#             "score": meilleur["score"],
#             "possibilites": resultats,
#         }

#     deuxieme = resultats[1]

#     ecart = (
#         meilleur["score"]
#         - deuxieme["score"]
#     )

#     # On exige à la fois un score suffisant et un écart
#     # significatif afin d'éviter une identification arbitraire.
#     if meilleur["score"] >= 35 and ecart >= 10:
#         return {
#             "statut": "identifie",
#             "profil": meilleur["profil"],
#             "score": meilleur["score"],
#             "possibilites": resultats,
#         }

#     return {
#         "statut": "ambigu",
#         "profil": None,
#         "score": meilleur["score"],
#         "possibilites": resultats,
#     }


# # ============================================================
# # ANALYSE GLOBALE DES PERSONNAGES
# # ============================================================

# def analyser_personnage_question(
#     question: str,
# ) -> Dict[str, Any]:

#     personnages_identifies = []
#     ambiguities = []
#     familles_detectees = []

#     mentions = trouver_mentions_personnages(question)

#     for mention in mentions:

#         cle_famille = mention["famille"]
#         famille = DICTIONNAIRE_PERSONNAGES[cle_famille]

#         familles_detectees.append(cle_famille)

#         analyse = analyser_famille_personnage(
#             question,
#             famille,
#         )

#         if analyse["statut"] == "identifie":

#             personnages_identifies.append({
#                 "famille": cle_famille,
#                 "profil": analyse["profil"],
#                 "score": analyse["score"],
#                 "aliases": mention["aliases"],
#             })

#         else:

#             ambiguities.append({
#                 "famille": cle_famille,
#                 "possibilites": analyse["possibilites"],
#                 "aliases": mention["aliases"],
#             })


#     # ========================================================
#     # PERSONNAGES UNIQUES
#     # ========================================================

#     question_normalisee = normaliser_texte(question)

#     for nom in PERSONNAGES_UNIQUES:

#         if not contient_terme(
#             question_normalisee,
#             nom,
#         ):
#             continue

#         deja_detecte = any(
#             contient_terme(
#                 personnage["profil"]["nom"],
#                 nom,
#             )
#             for personnage in personnages_identifies
#         )

#         if deja_detecte:
#             continue

#         personnages_identifies.append({
#             "famille": nom,

#             "profil": {
#                 "nom": nom.capitalize(),
#                 "aliases_specifiques": [nom],
#                 "aliases_generiques": [],
#                 "mots_forts": [],
#                 "mots_contexte": [],
#                 "requetes": [nom],
#             },

#             "score": 100,
#             "aliases": [nom],
#         })


#     # ========================================================
#     # CAS PARTICULIER : SIMON + INDICES FORTS DE PIERRE
#     # ========================================================

#     if any(
#         ambiguite["famille"] == "simon"
#         for ambiguite in ambiguities
#     ):

#         indices_pierre = [
#             "reniement",
#             "renie jesus",
#             "renie",
#             "pentecote",
#             "cephas",
#             "cles",
#             "corneille",
#             "filets",
#             "pecheur",
#             "trois fois",
#         ]

#         if any(
#             contient_terme(
#                 question_normalisee,
#                 indice,
#             )
#             for indice in indices_pierre
#         ):

#             nouvelles_ambiguities = []

#             for ambiguite in ambiguities:

#                 if ambiguite["famille"] != "simon":
#                     nouvelles_ambiguities.append(ambiguite)
#                     continue

#                 profil_pierre = next(
#                     (
#                         profil
#                         for profil
#                         in DICTIONNAIRE_PERSONNAGES["simon"]["profils"]
#                         if profil["nom"]
#                         == "Simon Pierre (l'apôtre Pierre)"
#                     ),
#                     None,
#                 )

#                 if profil_pierre:

#                     personnages_identifies.append({
#                         "famille": "simon",
#                         "profil": profil_pierre,
#                         "score": 100,
#                         "aliases": ["simon"],
#                     })

#             ambiguities = nouvelles_ambiguities


#     # ========================================================
#     # DÉDOUBLONNAGE FINAL
#     # ========================================================

#     uniques = []
#     noms_vus = set()

#     for personnage in personnages_identifies:

#         nom = personnage["profil"]["nom"]

#         if nom in noms_vus:
#             continue

#         noms_vus.add(nom)
#         uniques.append(personnage)

#     return {
#         "personnages": uniques,
#         "ambiguities": ambiguities,
#         "familles_detectees": familles_detectees,
#         "plusieurs_personnages": len(uniques) > 1,
#     }


# # ============================================================
# # DÉTECTION ACTION / RELATION
# # ============================================================

# def est_question_action_ou_relation(
#     question: str,
# ) -> bool:

#     texte = normaliser_texte(question)

#     # Formes interrogatives avec inversion.
#     motifs_verification = [

#         # a-t-il / a t il / a-t-il...
#         r"\ba\s*t\s*il\b",
#         r"\ba\s*t\s*elle\b",

#         # est-il / est il
#         r"\best\s*[-]?\s*il\b",
#         r"\best\s*[-]?\s*elle\b",

#         # était-il / etait il
#         r"\betait\s*[-]?\s*il\b",
#         r"\betait\s*[-]?\s*elle\b",

#         # avait-il / avait il
#         r"\bavait\s*[-]?\s*il\b",
#         r"\bavait\s*[-]?\s*elle\b",

#         # pouvait-il / pouvait il
#         r"\bpouvait\s*[-]?\s*il\b",
#         r"\bpouvait\s*[-]?\s*elle\b",

#         # devait-il / devait il
#         r"\bdevait\s*[-]?\s*il\b",
#         r"\bdevait\s*[-]?\s*elle\b",

#         # allait-il / allait il
#         r"\ballait\s*[-]?\s*il\b",
#         r"\ballait\s*[-]?\s*elle\b",

#         # sait-il / sait il
#         r"\bsait\s*[-]?\s*il\b",
#         r"\bsait\s*[-]?\s*elle\b",

#         # peut-il / peut il
#         r"\bpeut\s*[-]?\s*il\b",
#         r"\bpeut\s*[-]?\s*elle\b",

#         # doit-il / doit il
#         r"\bdoit\s*[-]?\s*il\b",
#         r"\bdoit\s*[-]?\s*elle\b",
#     ]

#     if any(
#         re.search(motif, texte)
#         for motif in motifs_verification
#     ):
#         return True


#     # Relations humaines ou familiales.
#     termes_relations = [
#         "connaissait",
#         "connu",
#         "connaissance",
#         "relation",
#         "entre",
#         "frere",
#         "soeur",
#         "pere",
#         "mere",
#         "fils",
#         "fille",
#         "epoux",
#         "mari",
#         "femme",
#         "epouse",
#         "parent",
#         "enfant",
#         "oncle",
#         "cousin",
#         "ami",
#         "amie",
#     ]

#     if any(
#         contient_terme(texte, terme)
#         for terme in termes_relations
#     ):
#         return True


#     # Actions courantes.
#     termes_actions = [
#         "vendu",
#         "vendre",
#         "vendait",

#         "livre",
#         "livrer",
#         "livrait",

#         "renie",
#         "renier",
#         "reniait",

#         "suivi",
#         "suivre",
#         "suivait",

#         "tue",
#         "tuer",
#         "tuait",

#         "parle",
#         "parler",
#         "parlait",

#         "vu",
#         "voir",
#         "voyait",

#         "rencontre",
#         "rencontrer",
#         "rencontrait",

#         "connaitre",
#         "connaître",

#         "aime",
#         "aimer",
#         "aimait",

#         "prie",
#         "prier",
#         "priait",

#         "appele",
#         "appeler",
#         "appelait",

#         "combattu",
#         "combattre",
#         "combattait",

#         "pardonne",
#         "pardonner",
#         "pardonnait",

#         "benit",
#         "benir",
#         "bénit",

#         "guerit",
#         "guerir",

#         "trahi",
#         "trahir",

#         "abandonne",
#         "abandonner",

#         "choisi",
#         "choisir",

#         "envoye",
#         "envoyer",

#         "rejete",
#         "rejeter",

#         "enseigne",
#         "enseigner",

#         "baptise",
#         "baptiser",

#         "ressuscite",
#         "ressusciter",
#     ]

#     return any(
#         contient_terme(texte, terme)
#         for terme in termes_actions
#     )


# # ============================================================
# # AFFICHAGE DES AMBIGUÏTÉS
# # ============================================================

# def afficher_ambiguite_personnage(
#     ambiguite: Dict[str, Any],
# ):

#     print(
#         "\n🤔 Plusieurs personnages peuvent correspondre "
#         "à ta question.\n"
#     )

#     print("Voici les possibilités :")

#     for index, resultat in enumerate(
#         ambiguite.get("possibilites", []),
#         start=1,
#     ):

#         profil = resultat.get("profil", {})

#         print(
#             f" {index}. {profil.get('nom', 'Personnage inconnu')}"
#         )

#     print(
#         "\n👉 Précise simplement lequel tu veux."
#     )


# # ============================================================
# # RÉFÉRENCES BIBLIQUES
# # ============================================================

# def _normaliser_separateurs_reference(
#     texte: str,
# ) -> str:

#     texte = normaliser_texte(texte)

#     texte = texte.replace("’", "'")

#     texte = re.sub(
#         r"\bchapitre\s+",
#         " ",
#         texte,
#     )

#     texte = re.sub(
#         r"\bversets?\s+",
#         " ",
#         texte,
#     )

#     # "à" devient "-" après suppression des accents.
#     texte = re.sub(
#         r"\s+a\s+",
#         " - ",
#         texte,
#     )

#     texte = re.sub(
#         r"\s*:\s*",
#         " ",
#         texte,
#     )

#     texte = re.sub(
#         r"\s*-\s*",
#         " - ",
#         texte,
#     )

#     texte = re.sub(
#         r"\s+",
#         " ",
#         texte,
#     )

#     return texte.strip()


# def trouver_reference_biblique(
#     question: str,
# ) -> Optional[Dict[str, str]]:

#     question_normalisee = _normaliser_separateurs_reference(
#         str(question)
#     )

#     livres = [
#         "genese",
#         "exode",
#         "levitique",
#         "nombres",
#         "deuteronome",
#         "josue",
#         "juges",
#         "ruth",

#         "1 samuel",
#         "2 samuel",
#         "1 rois",
#         "2 rois",
#         "1 chroniques",
#         "2 chroniques",

#         "esdras",
#         "nehemie",
#         "esther",
#         "job",
#         "psaumes",
#         "proverbes",
#         "ecclesiaste",
#         "cantique des cantiques",

#         "esaie",
#         "jeremie",
#         "lamentations",
#         "ezechiel",
#         "daniel",
#         "osee",
#         "joel",
#         "amos",
#         "abdias",
#         "jonas",
#         "michee",
#         "nahum",
#         "habacuc",
#         "sophonie",
#         "aggee",
#         "zacharie",
#         "malachie",

#         "matthieu",
#         "marc",
#         "luc",
#         "jean",
#         "actes",
#         "romains",

#         "1 corinthiens",
#         "2 corinthiens",

#         "galates",
#         "ephesiens",
#         "philippiens",
#         "colossiens",

#         "1 thessaloniciens",
#         "2 thessaloniciens",

#         "1 timothee",
#         "2 timothee",

#         "tite",
#         "philemon",
#         "hebreux",
#         "jacques",

#         "1 pierre",
#         "2 pierre",

#         "1 jean",
#         "2 jean",
#         "3 jean",

#         "jude",
#         "apocalypse",
#     ]

#     livres_tries = sorted(
#         livres,
#         key=len,
#         reverse=True,
#     )

#     livre_pattern = "|".join(
#         re.escape(livre)
#         for livre in livres_tries
#     )

#     motif = (
#         rf"""
#         \b
#         (
#             {livre_pattern}
#         )
#         \s+
#         (\d+)
#         (?:
#             \s+
#             (\d+)
#         )?
#         (?:
#             \s*
#             -
#             \s*
#             (\d+)
#         )?
#         \b
#         """
#     )

#     resultat = re.search(
#         motif,
#         question_normalisee,
#         flags=re.IGNORECASE | re.VERBOSE,
#     )

#     # Une référence doit comporter au minimum chapitre + verset.
#     if not resultat or not resultat.group(3):
#         return None

#     livre = resultat.group(1).strip()
#     chapitre = resultat.group(2)
#     verset = resultat.group(3)
#     verset_fin = resultat.group(4)

#     reference_complete = (
#         f"{livre} {chapitre}:{verset}"
#     )

#     if verset_fin:
#         reference_complete += f"-{verset_fin}"

#     return {
#         "livre": livre,
#         "chapitre": chapitre,
#         "verset": verset,
#         "verset_fin": verset_fin,
#         "reference_complete": reference_complete,
#     }

# # ============================================================
# # BLOC 3/3 - RECHERCHE, MÉMOIRE & APPLICATION CLI
# # ============================================================


# # ============================================================
# # CONSTRUCTION DES REQUÊTES DE RÉFÉRENCE
# # ============================================================

# def construire_requetes_reference(
#     question: str,
#     reference: Dict[str, Any],
# ) -> List[str]:

#     requetes = [question]

#     reference_complete = reference.get(
#         "reference_complete",
#         "",
#     )

#     livre = reference.get(
#         "livre",
#         "",
#     )

#     chapitre = reference.get(
#         "chapitre",
#         "",
#     )

#     verset = reference.get(
#         "verset",
#         "",
#     )

#     verset_fin = reference.get(
#         "verset_fin",
#     )

#     if reference_complete:
#         requetes.append(reference_complete)

#     if livre and chapitre and verset:

#         requetes.extend([
#             f"{livre} {chapitre}:{verset}",
#             f"{livre} {chapitre} {verset}",
#         ])

#     if verset_fin:

#         requetes.extend([
#             f"{livre} {chapitre}:{verset}-{verset_fin}",
#             f"{livre} {chapitre} {verset} {verset_fin}",
#         ])

#     resultat_final = []
#     vus = set()

#     for requete in requetes:

#         cle = normaliser_texte(requete)

#         if cle in vus:
#             continue

#         vus.add(cle)
#         resultat_final.append(requete)

#     return resultat_final


# # ============================================================
# # CONSTRUCTION DU CONTEXTE BIBLIQUE
# # ============================================================

# def construire_contexte(
#     versets: List[Any],
# ) -> str:

#     lignes = []

#     for verset in versets:

#         if not isinstance(verset, dict):
#             continue

#         reference = verset.get(
#             "reference",
#             verset.get("ref", ""),
#         )

#         texte = verset.get(
#             "texte",
#             verset.get("text", ""),
#         )

#         if reference and texte:

#             lignes.append(
#                 f"- {reference} : {texte}"
#             )

#     return "\n".join(lignes)


# # ============================================================
# # RECHERCHE CIBLÉE PERSONNAGES
# # ============================================================

# def rechercher_contexte_personnages(
#     question: str,
#     analyse_personnages: Dict[str, Any],
#     nombre_resultats: int = 5,
# ) -> List[Dict[str, Any]]:

#     recherches = [question]

#     personnages = analyse_personnages.get(
#         "personnages",
#         [],
#     )

#     ambiguities = analyse_personnages.get(
#         "ambiguities",
#         [],
#     )

#     noms_personnages = []


#     # ========================================================
#     # PERSONNAGES IDENTIFIÉS
#     # ========================================================

#     for personnage in personnages:

#         profil = personnage.get(
#             "profil",
#             {},
#         )

#         nom = profil.get(
#             "nom",
#             "",
#         )

#         if nom:
#             noms_personnages.append(nom)

#         recherches.extend(
#             profil.get(
#                 "requetes",
#                 [],
#             )
#         )


#     # ========================================================
#     # PERSONNAGES AMBIGUS
#     #
#     # IMPORTANT :
#     # On utilise leurs informations uniquement pour élargir
#     # la recherche.
#     #
#     # On ne transforme PAS une possibilité en identification.
#     # ========================================================

#     if ambiguities and est_question_action_ou_relation(question):

#         for ambiguite in ambiguities:

#             for possibilite in ambiguite.get(
#                 "possibilites",
#                 [],
#             ):

#                 profil = possibilite.get(
#                     "profil",
#                     {},
#                 )

#                 nom = profil.get(
#                     "nom",
#                     "",
#                 )

#                 if nom:
#                     noms_personnages.append(nom)

#                 for requete in profil.get(
#                     "requetes",
#                     [],
#                 ):

#                     recherches.append(
#                         f"{requete} {question}"
#                     )

#                 if nom:

#                     recherches.append(
#                         f"{nom} {question}"
#                     )


#     # ========================================================
#     # DÉDOUBLONNAGE DES NOMS
#     # ========================================================

#     noms_uniques = []

#     for nom in noms_personnages:

#         if not nom:
#             continue

#         if nom not in noms_uniques:
#             noms_uniques.append(nom)


#     # Recherche relationnelle seulement lorsqu'au moins
#     # deux personnages sont réellement concernés.
#     if len(noms_uniques) >= 2:

#         recherches.append(
#             " ".join(noms_uniques)
#             + " "
#             + question
#         )


#     # ========================================================
#     # EXÉCUTION DES RECHERCHES
#     # ========================================================

#     resultats_final = []
#     references_vues = set()

#     for requete in recherches:

#         if not isinstance(requete, str):
#             continue

#         requete = requete.strip()

#         if not requete:
#             continue

#         try:

#             resultats = rechercher(
#                 requete,
#                 nombre_resultats=nombre_resultats,
#             )

#         except Exception:
#             # Ne jamais exposer l'erreur interne à l'utilisateur.
#             continue

#         if not resultats:
#             continue

#         for verset in resultats:

#             if not isinstance(verset, dict):
#                 continue

#             reference = verset.get(
#                 "reference",
#                 verset.get("ref", ""),
#             )

#             texte = verset.get(
#                 "texte",
#                 verset.get("text", ""),
#             )

#             if reference:

#                 cle = (
#                     "reference:"
#                     + normaliser_texte(reference)
#                 )

#             else:

#                 cle = (
#                     "texte:"
#                     + normaliser_texte(texte)
#                 )

#             if cle in references_vues:
#                 continue

#             references_vues.add(cle)
#             resultats_final.append(verset)

#             if (
#                 len(resultats_final)
#                 >= MAX_RESULTATS_PERSONNAGES
#             ):
#                 return resultats_final

#     return resultats_final


# # ============================================================
# # RECHERCHE PAR RÉFÉRENCE
# # ============================================================

# def rechercher_par_reference(
#     question: str,
#     reference: Dict[str, Any],
#     nombre_resultats: int = 5,
# ) -> List[Dict[str, Any]]:

#     requetes = construire_requetes_reference(
#         question,
#         reference,
#     )

#     resultats_final = []
#     references_vues = set()

#     for requete in requetes:

#         try:

#             resultats = rechercher(
#                 requete,
#                 nombre_resultats=nombre_resultats,
#             )

#         except Exception:
#             continue

#         if not resultats:
#             continue

#         for verset in resultats:

#             if not isinstance(verset, dict):
#                 continue

#             reference_verset = verset.get(
#                 "reference",
#                 verset.get("ref", ""),
#             )

#             texte = verset.get(
#                 "texte",
#                 verset.get("text", ""),
#             )

#             if reference_verset:

#                 cle = (
#                     "reference:"
#                     + normaliser_texte(reference_verset)
#                 )

#             else:

#                 cle = (
#                     "texte:"
#                     + normaliser_texte(texte)
#                 )

#             if cle in references_vues:
#                 continue

#             references_vues.add(cle)
#             resultats_final.append(verset)

#     return resultats_final


# # ============================================================
# # PRÉPARATION SÉCURISÉE DE L'HISTORIQUE
# # ============================================================

# def preparer_historique_pour_modele(
#     historique: List[Any],
# ) -> List[Dict[str, str]]:

#     if not isinstance(historique, list):
#         return []

#     historique_propre = []

#     for element in historique[
#         -MAX_HISTORIQUE_ENTRIES:
#     ]:

#         if not isinstance(element, dict):
#             continue

#         role = element.get("role")

#         if role not in {
#             "user",
#             "assistant",
#         }:
#             continue

#         contenu = str(
#             element.get(
#                 "content",
#                 "",
#             )
#             or ""
#         ).strip()

#         if not contenu:
#             continue

#         historique_propre.append({
#             "role": role,
#             "content": contenu[
#                 :MAX_LONGUEUR_ENTREE_HISTORIQUE
#             ],
#         })


#     # ========================================================
#     # LIMITE TOTALE
#     # ========================================================

#     historique_final = []
#     longueur_totale = 0

#     for element in reversed(
#         historique_propre
#     ):

#         longueur_element = len(
#             element["content"]
#         )

#         if (
#             longueur_totale
#             + longueur_element
#             > MAX_LONGUEUR_HISTORIQUE_TOTAL
#         ):
#             break

#         historique_final.append(element)
#         longueur_totale += longueur_element

#     historique_final.reverse()

#     return historique_final


# # ============================================================
# # VÉRIFICATION COMPATIBILITÉ GÉNÉRATEUR
# # ============================================================

# def generateur_accepte_historique() -> bool:
#     """
#     Vérifie si generer_reponse_biblique accepte le paramètre
#     historique.

#     Cela évite l'ancien système :
#         try -> TypeError -> second appel

#     qui pouvait masquer un véritable TypeError interne.
#     """

#     try:

#         signature = inspect.signature(
#             generer_reponse_biblique
#         )

#         parametres = signature.parameters

#         if "historique" in parametres:
#             return True

#         return any(
#             parametre.kind
#             == inspect.Parameter.VAR_KEYWORD
#             for parametre
#             in parametres.values()
#         )

#     except Exception:
#         return False


# # ============================================================
# # APPEL CENTRALISÉ DU GÉNÉRATEUR
# # ============================================================

# def appeler_generateur(
#     question: str,
#     versets_contexte: str,
#     niveau_utilisateur: str,
#     historique: List[Any],
# ) -> str:

#     historique_propre = (
#         preparer_historique_pour_modele(
#             historique
#         )
#     )

#     if generateur_accepte_historique():

#         return generer_reponse_biblique(
#             question,
#             versets_contexte,
#             niveau_utilisateur,
#             historique=historique_propre,
#         )

#     return generer_reponse_biblique(
#         question,
#         versets_contexte,
#         niveau_utilisateur,
#     )


# # ============================================================
# # APPLICATION PRINCIPALE
# # ============================================================

# def demarrer_application(
#     niveau_utilisateur: str = "18+",
# ):

#     niveau_utilisateur = (
#         normaliser_niveau_utilisateur(
#             niveau_utilisateur
#         )
#     )


#     # ========================================================
#     # VÉRIFICATION DES DONNÉES BIBLIQUES
#     # ========================================================

#     try:

#         with open(
#             "bible.json",
#             "r",
#             encoding="utf-8",
#         ) as fichier:

#             bible = json.load(fichier)

#         if bible is None:
#             print(
#                 "\n❌ Les données bibliques sont indisponibles."
#             )
#             return

#     except Exception:

#         print(
#             "\n❌ Impossible de charger les données bibliques."
#         )

#         return


#     # ========================================================
#     # INTERFACE CLI
#     # ========================================================

#     print(
#         "\n"
#         + "=" * 60
#     )

#     print(
#         "📖 BIBLE-IA (Jack + Mémoire Ben)"
#     )

#     print(
#         "=" * 60
#     )

#     print(
#         f"\n🎓 Niveau utilisateur : "
#         f"{niveau_utilisateur}"
#     )

#     print(
#         "💡 Tape /exit pour quitter, "
#         "/clear pour effacer la mémoire"
#     )


#     # ========================================================
#     # MÉMOIRE DE CONVERSATION
#     # ========================================================

#     historique_conversation: List[
#         Dict[str, str]
#     ] = []


#     # ========================================================
#     # BOUCLE PRINCIPALE
#     # ========================================================

#     while True:

#         try:

#             question = input(
#                 "\n❓ Ta question : "
#             )

#         except (
#             EOFError,
#             KeyboardInterrupt,
#         ):

#             print(
#                 "\n👋 A bientôt!"
#             )

#             break


#         # ====================================================
#         # NETTOYAGE DE LA QUESTION
#         # ====================================================

#         question = str(
#             question or ""
#         ).strip()

#         if not question:

#             print(
#                 "\n💬 Pose ta question biblique, "
#                 "je suis là."
#             )

#             continue


#         # ====================================================
#         # COMMANDES
#         # ====================================================

#         commande = question.lower()

#         if commande in {
#             "/exit",
#             "/quit",
#             "exit",
#             "quit",
#         }:

#             print(
#                 "\n👋 A bientôt!"
#             )

#             break


#         if commande in {
#             "/clear",
#             "clear",
#         }:

#             historique_conversation = []

#             print(
#                 "\n🧹 Mémoire effacée."
#             )

#             continue


#         # ====================================================
#         # LIMITE DE LONGUEUR
#         # ====================================================

#         if len(question) > MAX_QUESTION_LEN:

#             print(
#                 "\n⚠️ Ta question est trop longue. "
#                 "Essaie de la raccourcir."
#             )

#             continue


#         # ====================================================
#         # FILTRE HORS SUJET
#         # ====================================================

#         if est_hors_sujet_absolu(question):

#             print(
#                 "\n🚫 Cette question sort du domaine "
#                 "de BIBLE-IA."
#             )

#             continue


#         # ====================================================
#         # DÉTECTION DE RÉFÉRENCE
#         # ====================================================

#         reference = trouver_reference_biblique(
#             question
#         )

#         resultats = None

#         if reference:

#             print(
#                 "\n📖 Référence biblique détectée : "
#                 f"{reference['reference_complete']}"
#             )

#             resultats = rechercher_par_reference(
#                 question,
#                 reference,
#                 nombre_resultats=5,
#             )


#         # ====================================================
#         # ANALYSE DES PERSONNAGES
#         # ====================================================

#         analyse_personnages = (
#             analyser_personnage_question(
#                 question
#             )
#         )

#         personnages = (
#             analyse_personnages["personnages"]
#         )

#         ambiguities = (
#             analyse_personnages["ambiguities"]
#         )


#         # ====================================================
#         # AFFICHAGE DES PERSONNAGES IDENTIFIÉS
#         # ====================================================

#         if personnages:

#             print(
#                 "\n👤 Personnage(s) identifié(s) :"
#             )

#             for personnage in personnages:

#                 nom = personnage[
#                     "profil"
#                 ].get(
#                     "nom",
#                     "Personnage inconnu",
#                 )

#                 print(
#                     f" • {nom}"
#                 )


#         # ====================================================
#         # GESTION DES AMBIGUÏTÉS
#         # ====================================================

#         if ambiguities:

#             if not personnages:

#                 if est_question_action_ou_relation(
#                     question
#                 ):

#                     nom_famille = (
#                         ambiguities[0][
#                             "famille"
#                         ].capitalize()
#                     )

#                     print(
#                         f"\n🔎 Plusieurs « "
#                         f"{nom_famille} » existent "
#                         "dans la Bible, mais la question "
#                         "cible une action précise."
#                     )

#                     print(
#                         "🧭 Recherche élargie aux "
#                         "différents profils concernés "
#                         "pour vérifier..."
#                     )

#                 else:

#                     afficher_ambiguite_personnage(
#                         ambiguities[0]
#                     )

#                     continue

#             else:

#                 print(
#                     "\nℹ️ Un des personnages mentionnés "
#                     "reste ambigu. BIBLE-IA va poursuivre "
#                     "avec les personnages déjà identifiés."
#                 )


#         # ====================================================
#         # RECHERCHE DES PASSAGES
#         # ====================================================

#         if resultats is None:

#             if personnages:

#                 resultats = (
#                     rechercher_contexte_personnages(
#                         question,
#                         analyse_personnages,
#                         nombre_resultats=5,
#                     )
#                 )

#             elif (
#                 ambiguities
#                 and est_question_action_ou_relation(
#                     question
#                 )
#             ):

#                 # Recherche élargie mais neutre.
#                 # Aucun personnage ambigu n'est forcé.
#                 resultats = (
#                     rechercher_contexte_personnages(
#                         question,
#                         analyse_personnages,
#                         nombre_resultats=5,
#                     )
#                 )

#             else:

#                 resultats = rechercher(
#                     question,
#                     nombre_resultats=8,
#                 )


#         # ====================================================
#         # AUCUN RÉSULTAT
#         # ====================================================

#         if not resultats:

#             if ambiguities and not personnages:

#                 print(
#                     "\n⚠️ Les passages retrouvés "
#                     "ne permettent pas de déterminer "
#                     "quel personnage tu veux."
#                 )

#                 afficher_ambiguite_personnage(
#                     ambiguities[0]
#                 )

#                 continue

#             print(
#                 "\n⚠️ Aucun passage biblique pertinent "
#                 "n'a été retrouvé."
#             )

#             continue


#         # ====================================================
#         # CONSTRUCTION DU CONTEXTE
#         # ====================================================

#         versets_contexte = (
#             construire_contexte(
#                 resultats
#             )
#         )

#         if not versets_contexte.strip():

#             print(
#                 "\n⚠️ Les passages trouvés ne contiennent "
#                 "pas de texte exploitable."
#             )

#             continue


#         # ====================================================
#         # GÉNÉRATION
#         # ====================================================

#         print(
#             "\n🧠 Analyse des passages bibliques..."
#         )

#         try:

#             reponse = appeler_generateur(
#                 question,
#                 versets_contexte,
#                 niveau_utilisateur,
#                 historique_conversation,
#             )

#         except Exception:

#             # Sécurité :
#             # aucune exception technique brute n'est
#             # transmise à l'utilisateur.
#             print(
#                 "\n❌ Désolé, une erreur technique "
#                 "momentanée empêche la génération "
#                 "de la réponse."
#             )

#             print(
#                 "Veuillez réessayer dans quelques instants."
#             )

#             continue


#         # ====================================================
#         # VALIDATION DE LA RÉPONSE
#         # ====================================================

#         if not isinstance(
#             reponse,
#             str,
#         ):

#             reponse = str(
#                 reponse
#             )

#         reponse = reponse.strip()

#         if not reponse:

#             print(
#                 "\n⚠️ BIBLE-IA n'a pas pu générer "
#                 "une réponse exploitable."
#             )

#             continue


#         # ====================================================
#         # AFFICHAGE
#         # ====================================================

#         print(
#             "\n"
#             + "=" * 60
#         )

#         print(
#             "📖 RÉPONSE DE BIBLE-IA"
#         )

#         print(
#             "=" * 60
#         )

#         print(
#             f"\n{reponse}"
#         )


#         # ====================================================
#         # MÉMOIRE
#         # ====================================================

#         historique_conversation.append({
#             "role": "user",
#             "content": question,
#         })

#         historique_conversation.append({
#             "role": "assistant",
#             "content": reponse,
#         })

#         historique_conversation = (
#             historique_conversation[
#                 -MAX_HISTORIQUE_ENTRIES:
#             ]
#         )


# # ============================================================
# # LANCEMENT
# # ============================================================

# if __name__ == "__main__":
#     demarrer_application()
    

import json
import re
import unicodedata
import inspect
import logging
import threading
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# ================= IMPORTS MOTEURS PROD - fallback compatible =================
try:
    from moteur_biblique_optimise import MoteurBibliquePROD
    MOTEUR_PROD_DISPO = True
except ImportError:
    MoteurBibliquePROD = None
    MOTEUR_PROD_DISPO = False

try:
    from recherche_hybride import rechercher as fallback_rechercher
except ImportError:
    fallback_rechercher = None

try:
    from generateur_reponse import generer_reponse_biblique
except ImportError:
    generer_reponse_biblique = None

logger = logging.getLogger(__name__)

# ================= CONFIG PROD CORRIGÉE =================
MAX_HISTORIQUE_ENTRIES = 6
MAX_LONGUEUR_ENTREE_HISTORIQUE = 1500
MAX_LONGUEUR_HISTORIQUE_TOTAL = 8000
MAX_QUESTION_LEN = 500
MAX_QUESTION_MOTS = 100
MAX_RESULTATS_PERSONNAGES = 12
MAX_VERSETS_RAG = 5
MAX_TOKENS_CONTEXT = 3500
NOMBRE_VERSETS_DEFAUT = 5

_lock = threading.Lock()
_orchestrator_singleton = None

RE_ESPACES = re.compile(r"\s+")
RE_CHAPITRE = re.compile(r"\bchapitre\s+")
RE_VERSET = re.compile(r"\bversets?\s+")

NIVEAUX_AUTORISES = {"8-11", "12-15", "16-17", "18+", "approfondi"}
CORRESPONDANCES_NIVEAUX = {
    "8": "8-11", "8-11": "8-11", "8–11": "8-11", "8_11": "8-11", "8 à 11": "8-11", "8 a 11": "8-11",
    "12": "12-15", "12-15": "12-15", "12–15": "12-15", "12_15": "12-15", "12 à 15": "12-15", "12 a 15": "12-15",
    "16": "16-17", "16-17": "16-17", "16–17": "16-17", "16_17": "16-17", "16 à 17": "16-17", "16 a 17": "16-17",
    "18": "18+", "18+": "18+", "18 et plus": "18+", "18 ans et plus": "18+", "adulte": "18+",
    "approfondi": "approfondi", "approfondie": "approfondi", "expert": "approfondi", "detaille": "approfondi", "détaillé": "approfondi",
}

def normaliser_niveau_utilisateur(niveau_utilisateur: Optional[str]) -> str:
    if not niveau_utilisateur: return "18+"
    niveau = str(niveau_utilisateur).strip().lower()
    return CORRESPONDANCES_NIVEAUX.get(niveau, "18+")

@lru_cache(maxsize=5000)
def normaliser_texte(texte: Any) -> str:
    if texte is None: return ""
    texte = str(texte).lower().strip()
    texte = unicodedata.normalize("NFD", texte)
    texte = "".join(c for c in texte if unicodedata.category(c)!= "Mn")
    texte = RE_ESPACES.sub(" ", texte)
    return texte

def contient_terme(texte: Any, terme: Any) -> bool:
    texte_normalise = normaliser_texte(texte)
    terme_normalise = normaliser_texte(terme)
    if not texte_normalise or not terme_normalise: return False
    motif = r"(?<!\w)" + re.escape(terme_normalise) + r"(?!\w)"
    return re.search(motif, texte_normalise) is not None

def _texte_securise(t: Any, max_len: int = MAX_QUESTION_LEN) -> str:
    if t is None: return ""
    try: t = str(t)
    except: return ""
    t = t.replace("\x00"," ").strip()
    return t[:max_len]

def valider_question(question: Any) -> Tuple[bool, str]:
    q = _texte_securise(question)
    if not q: return False, "Pose ta question biblique."
    if len(q) < 2: return False, "Question trop courte."
    if len(q) > MAX_QUESTION_LEN: return False, f"Question trop longue (max {MAX_QUESTION_LEN})."
    if len(q.split()) > MAX_QUESTION_MOTS: return False, "Question trop longue."
    return True, q

DICTIONNAIRE_PERSONNAGES: Dict[str, Dict[str, Any]] = {
    "paul": {"aliases": ["saul de tarse", "saül de tarse", "saul", "saül", "paul"], "profils": [{"nom": "Saül de Tarse (l'apôtre Paul)", "aliases_specifiques": ["saul de tarse", "saül de tarse", "paul"], "aliases_generiques": ["saul", "saül"], "mots_forts": ["tarse", "damas", "apotre", "gentils", "epitres", "lettres", "persecuteur", "conversion", "missionnaire", "chretiens"], "mots_contexte": ["eglise", "evangile", "mission", "voyage", "rome", "corinthe", "jerusalem", "paul"], "requetes": ["Saül de Tarse conversion Actes", "Paul apôtre des gentils lettres", "Saül Damas persécution chrétiens"]}, {"nom": "Saül, premier roi d'Israël", "aliases_specifiques": ["saul roi", "saül roi", "premier roi d israel", "premier roi d'israel", "roi saul", "roi saül"], "aliases_generiques": ["saul", "saül"], "mots_forts": ["roi", "israel", "philistins", "kis", "cisch", "samuel", "gilboa", "jonathan", "royaume"], "mots_contexte": ["david", "goliath", "berger", "combat", "arme", "ennemi", "trone"], "requetes": ["Saül roi d'Israël Samuel", "Saül et David roi d'Israël", "Saül Philistins Jonathan"]}]},
    "simon": {"aliases": ["simon", "simeon pierre", "siméon pierre", "simon pierre", "cephas", "céphas"], "profils": [{"nom": "Simon Pierre (l'apôtre Pierre)", "aliases_specifiques": ["simon pierre", "siméon pierre", "simeon pierre", "cephas", "céphas"], "aliases_generiques": ["simon"], "mots_forts": ["pierre", "apotre", "reniement", "renie", "renie jesus", "pentecote", "cephas", "cles", "corneille", "filets", "pecheur", "galilee"], "mots_contexte": ["jesus", "douze", "disciple", "appel", "peche", "pecher", "frere", "andre"], "requetes": ["Simon Pierre apôtre Jésus", "Pierre reniement Jésus", "Pierre renie Jésus trois fois", "Jean 18 Pierre reniement Jésus", "Pierre Pentecôte Actes"]}, {"nom": "Simon le Zélote", "aliases_specifiques": ["simon le zelote", "simon le zélote", "simon zelote", "simon zélote"], "aliases_generiques": ["simon"], "mots_forts": ["zelote", "zélote", "douze", "disciple", "apotre"], "mots_contexte": ["jesus", "disciples"], "requetes": ["Simon le Zélote disciple de Jésus", "Simon le Zélote apôtre"]}, {"nom": "Simon père de Judas Iscariot", "aliases_specifiques": ["simon pere de judas", "simon père de judas", "simon pere de judas iscariot", "simon père de judas iscariot"], "aliases_generiques": ["simon"], "mots_forts": ["judas iscariot", "judas", "iscariot", "pere de judas"], "mots_contexte": ["pere"], "requetes": ["Simon père de Judas Iscariot"]}, {"nom": "Simon le Pharisien", "aliases_specifiques": ["simon le pharisien"], "aliases_generiques": ["simon"], "mots_forts": ["pharisien", "pecheresse", "parfum", "repas", "maison"], "mots_contexte": ["jesus", "repas"], "requetes": ["Simon le Pharisien Jésus", "Simon le Pharisien femme pécheresse"]}, {"nom": "Simon le lépreux", "aliases_specifiques": ["simon le lepreux", "simon le lépreux"], "aliases_generiques": ["simon"], "mots_forts": ["lepreux", "lépreux", "bethanie", "parfum"], "mots_contexte": ["repas", "jesus"], "requetes": ["Simon le lépreux Bethanie Jésus"]}]},
    "marie": {"aliases": ["marie"], "profils": [{"nom": "Marie, mère de Jésus", "aliases_specifiques": ["marie mere de jesus", "marie mère de jesus", "marie mere de dieu"], "aliases_generiques": ["marie"], "mots_forts": ["mere de jesus", "mere", "nazareth", "gabriel", "ange", "annonciation", "naissance", "bethleem"], "mots_contexte": ["jesus", "joseph", "enfant", "fils"], "requetes": ["Marie mère de Jésus naissance", "Marie Joseph Jésus", "Marie annonciation Gabriel"]}, {"nom": "Marie de Magdala", "aliases_specifiques": ["marie de magdala", "marie magdala", "marie madeleine"], "aliases_generiques": ["marie"], "mots_forts": ["magdala", "madeleine", "tombeau", "resurrection", "ressuscite"], "mots_contexte": ["jesus", "croix", "disciples"], "requetes": ["Marie de Magdala Jésus", "Marie Madeleine tombeau Jésus", "Marie de Magdala résurrection"]}, {"nom": "Marie de Béthanie", "aliases_specifiques": ["marie de bethanie", "marie bethanie"], "aliases_generiques": ["marie"], "mots_forts": ["bethanie", "marthe", "lazare", "parfum", "pieds"], "mots_contexte": ["jesus", "soeur", "frere"], "requetes": ["Marie Marthe Lazare Bethanie", "Marie de Béthanie Jésus parfum", "Jean 11 Marie Marthe Lazare"]}, {"nom": "Marie, mère de Jacques et de Joses", "aliases_specifiques": ["marie mere de jacques", "marie mère de jacques", "marie mere de joses", "marie mère de joses"], "aliases_generiques": ["marie"], "mots_forts": ["jacques", "joses", "sepulcre", "tombeau"], "mots_contexte": ["jesus", "femme"], "requetes": ["Marie mère de Jacques Joses"]}, {"nom": "Marie, mère de Jean-Marc", "aliases_specifiques": ["marie mere de jean marc", "marie mère de jean marc", "marie mere de jean-marc", "marie mère de jean-marc"], "aliases_generiques": ["marie"], "mots_forts": ["jean marc", "jean-marc", "marc", "maison", "priere"], "mots_contexte": ["jerusalem", "pierre"], "requetes": ["Marie mère de Jean Marc Actes"]}]},
    "jean": {"aliases": ["jean"], "profils": [{"nom": "Jean-Baptiste", "aliases_specifiques": ["jean baptiste", "jean-baptiste"], "aliases_generiques": ["jean"], "mots_forts": ["baptiste", "baptiser", "bapteme", "désert", "desert", "herode", "jean baptiste"], "mots_contexte": ["jesus", "prophete", "jordan", "fleuve"], "requetes": ["Jean Baptiste Jésus baptême", "Jean Baptiste Hérode"]}, {"nom": "Jean, fils de Zébédée", "aliases_specifiques": ["jean fils de zebedee", "jean fils de zébédée", "jean de zebedee", "jean de zébédée"], "aliases_generiques": ["jean"], "mots_forts": ["zebedee", "zébédée", "jacques", "apotre", "douze"], "mots_contexte": ["jesus", "pecheur", "galilee"], "requetes": ["Jean fils de Zébédée apôtre", "Jean Jacques Zébédée Jésus"]}, {"nom": "Jean-Marc", "aliases_specifiques": ["jean marc", "jean-marc"], "aliases_generiques": ["jean"], "mots_forts": ["marc", "maison", "barnabas", "pierre"], "mots_contexte": ["jerusalem", "eglise"], "requetes": ["Jean Marc Actes Barnabas Pierre"]}]},
    "jacques": {"aliases": ["jacques"], "profils": [{"nom": "Jacques, fils de Zébédée", "aliases_specifiques": ["jacques fils de zebedee", "jacques fils de zébédée"], "aliases_generiques": ["jacques"], "mots_forts": ["zebedee", "zébédée", "jean", "herode", "épée", "epee"], "mots_contexte": ["apotre", "douze", "jesus", "galilee"], "requetes": ["Jacques fils de Zébédée Jean", "Jacques tué par Hérode Actes 12"]}, {"nom": "Jacques, fils d'Alphée", "aliases_specifiques": ["jacques fils d alphee", "jacques fils d'alphée", "jacques fils d'alphee"], "aliases_generiques": ["jacques"], "mots_forts": ["alphee", "alphée"], "mots_contexte": ["apotre", "douze", "disciple"], "requetes": ["Jacques fils d'Alphée apôtre"]}, {"nom": "Jacques, frère de Jésus", "aliases_specifiques": ["jacques frere de jesus", "jacques frère de jesus"], "aliases_generiques": ["jacques"], "mots_forts": ["frere de jesus", "frère de jesus", "jerusalem", "eglise"], "mots_contexte": ["jesus", "apotre", "lettre"], "requetes": ["Jacques frère de Jésus Jérusalem", "Jacques église de Jérusalem"]}]},
    "herode": {"aliases": ["herode", "hérode"], "profils": [{"nom": "Hérode le Grand", "aliases_specifiques": ["herode le grand", "hérode le grand"], "aliases_generiques": ["herode", "hérode"], "mots_forts": ["enfant", "bethleem", "mages", "magiciens", "massacre"], "mots_contexte": ["jesus", "naissance", "judee", "jerusalem"], "requetes": ["Hérode le Grand Jésus enfant", "Hérode Bethléem mages"]}, {"nom": "Hérode Antipas", "aliases_specifiques": ["herode antipas", "hérode antipas"], "aliases_generiques": ["herode", "hérode"], "mots_forts": ["jean baptiste", "jean-baptiste", "salome", "herodias", "galilee"], "mots_contexte": ["jesus", "pilate", "roi"], "requetes": ["Hérode Antipas Jean Baptiste", "Hérode Antipas Jésus"]}, {"nom": "Hérode Agrippa I", "aliases_specifiques": ["herode agrippa", "hérode agrippa", "herode agrippa premier", "hérode agrippa premier"], "aliases_generiques": ["herode", "hérode"], "mots_forts": ["jacques", "pierre", "persecution", "actes"], "mots_contexte": ["eglise", "juifs"], "requetes": ["Hérode Agrippa Jacques Pierre Actes"]}, {"nom": "Hérode Agrippa II", "aliases_specifiques": ["herode agrippa ii", "hérode agrippa ii", "agrippa ii", "agrippa 2", "agrippa deux"], "aliases_generiques": ["herode", "hérode"], "mots_forts": ["paul", "bernice", "festus", "cesar", "procès", "proces"], "mots_contexte": ["actes", "roi"], "requetes": ["Agrippa II Paul Festus Actes"]}]},
    "joseph": {"aliases": ["joseph"], "profils": [{"nom": "Joseph, fils de Jacob", "aliases_specifiques": ["joseph fils de jacob", "joseph vendu par ses freres", "joseph vendu par ses frères"], "aliases_generiques": ["joseph"], "mots_forts": ["jacob", "freres", "frères", "egypte", "égypte", "songe", "pharaon", "prison"], "mots_contexte": ["genese", "robe", "reve", "rêve"], "requetes": ["Joseph fils de Jacob vendu par ses frères", "Joseph Égypte Pharaon", "Joseph frères Genèse"]}, {"nom": "Joseph, époux de Marie", "aliases_specifiques": ["joseph epoux de marie", "joseph époux de marie", "joseph mari de marie", "joseph pere adoptif de jesus", "joseph père adoptif de jesus"], "aliases_generiques": ["joseph"], "mots_forts": ["marie", "jesus", "ange", "songe", "bethleem", "nazareth"], "mots_contexte": ["enfant", "naissance", "famille"], "requetes": ["Joseph mari de Marie Jésus", "Joseph naissance Jésus", "Joseph Nazareth Marie"]}, {"nom": "Joseph d'Arimathée", "aliases_specifiques": ["joseph d arimathee", "joseph d'arimathee", "joseph d arimathée", "joseph d'arimathée"], "aliases_generiques": ["joseph"], "mots_forts": ["arimathee", "arimathée", "tombeau", "sepulcre", "sépulcre", "corps"], "mots_contexte": ["jesus", "crucifixion", "pilate"], "requetes": ["Joseph d'Arimathée tombeau Jésus", "Joseph d'Arimathée Pilate"]}]},
}

DICTIONNAIRE_PERSONNAGES.update({
    "simeon": {"aliases": ["simeon", "siméon"], "profils": [{"nom": "Siméon, fils de Jacob", "aliases_specifiques": ["simeon fils de jacob", "siméon fils de jacob"], "aliases_generiques": ["simeon", "siméon"], "mots_forts": ["jacob", "tribu", "freres", "frères"], "mots_contexte": ["israel", "fils"], "requetes": ["Siméon fils de Jacob tribu"]}, {"nom": "Siméon au temple", "aliases_specifiques": ["simeon au temple", "siméon au temple", "simeon qui a vu jesus", "siméon qui a vu jesus"], "aliases_generiques": ["simeon", "siméon"], "mots_forts": ["temple", "jesus", "enfant", "esprit saint", "esprit", "jerusalem"], "mots_contexte": ["marie", "joseph", "luc"], "requetes": ["Siméon temple Jésus enfant Luc 2", "Siméon bénit Jésus temple"]}]},
    "david": {"aliases": ["david"], "profils": [{"nom": "David, roi d'Israël", "aliases_specifiques": ["roi david", "david roi"], "aliases_generiques": ["david"], "mots_forts": ["roi", "goliath", "bethleem", "jonathan", "saul", "saül", "jerusalem", "psaumes", "psaume"], "mots_contexte": ["berger", "onction", "royaume", "israel", "israël"], "requetes": ["David roi Israël Saül", "David Goliath", "David Jonathan"]}]},
    "ruth": {"aliases": ["ruth"], "profils": [{"nom": "Ruth", "aliases_specifiques": ["ruth"], "aliases_generiques": [], "mots_forts": ["boaz", "naomi", "moab"], "mots_contexte": ["bled", "moisson"], "requetes": ["Ruth Naomi Boaz"]}]},
    "moise": {"aliases": ["moise", "moïse"], "profils": [{"nom": "Moïse", "aliases_specifiques": ["moise", "moïse"], "aliases_generiques": [], "mots_forts": ["egypte", "pharaon", "mer rouge", "buisson", "sinai", "loi"], "mots_contexte": ["aaron", "israel"], "requetes": ["Moïse Exode Pharaon", "Moïse Sinaï loi"]}]},
    "abraham": {"aliases": ["abraham"], "profils": [{"nom": "Abraham", "aliases_specifiques": ["abraham"], "aliases_generiques": [], "mots_forts": ["isaac", "sarah", "lot", "alliance"], "mots_contexte": ["promesse", "canan"], "requetes": ["Abraham Isaac Sarah alliance"]}]},
    "nebucadnetsar": {"aliases": ["nebucadnetsar", "nebuchadnezzar", "nabuchodonosor"], "profils": [{"nom": "Nebucadnetsar", "aliases_specifiques": ["nebucadnetsar", "nebuchadnezzar", "nabuchodonosor"], "aliases_generiques": [], "mots_forts": ["babylone", "roi", "songe", "daniel", "statue"], "mots_contexte": ["royaume", "fournaise"], "requetes": ["Nebucadnetsar Daniel Babylone", "Nebucadnetsar songe statue"]}]},
    "salomon": {"aliases": ["salomon"], "profils": [{"nom": "Salomon", "aliases_specifiques": ["salomon"], "aliases_generiques": [], "mots_forts": ["sagesse", "temple", "roi", "david"], "mots_contexte": ["proverbes", "jerusalem"], "requetes": ["Salomon sagesse temple David"]}]},
    "elie": {"aliases": ["elie", "elijah"], "profils": [{"nom": "Élie", "aliases_specifiques": ["elie", "elijah"], "aliases_generiques": [], "mots_forts": ["baal", "carmel", "ahab", "feu", "prophète", "prophete"], "mots_contexte": ["veuve", "corbeaux"], "requetes": ["Élie prophète Carmel Baal", "Élie Ahab"]}]},
    "elisee": {"aliases": ["elisee", "elisée"], "profils": [{"nom": "Élisée", "aliases_specifiques": ["elisee", "elisée"], "aliases_generiques": [], "mots_forts": ["elie", "naaman", "elisée", "elisee"], "mots_contexte": ["prophète", "prophete", "miracle"], "requetes": ["Élisée Élie Naaman"]}]},
    "esther": {"aliases": ["esther"], "profils": [{"nom": "Esther", "aliases_specifiques": ["esther"], "aliases_generiques": [], "mots_forts": ["mardochee", "aman", "perse", "reine"], "mots_contexte": ["roi", "jeune fille"], "requetes": ["Esther Mardochée Aman"]}]},
    "melchizedek": {"aliases": ["melchizedek", "melchisédek"], "profils": [{"nom": "Melchisédek", "aliases_specifiques": ["melchizedek", "melchisédek"], "aliases_generiques": [], "mots_forts": ["salem", "sacrificateur", "abraham"], "mots_contexte": ["roi"], "requetes": ["Melchisédek Abraham Salem"]}]},
    "methuselah": {"aliases": ["methuselah", "mathusalem", "mathusala"], "profils": [{"nom": "Mathusalem", "aliases_specifiques": ["methuselah", "mathusalem", "mathusala"], "aliases_generiques": [], "mots_forts": ["noe", "enoch", "969"], "mots_contexte": ["annees", "âge", "age"], "requetes": ["Mathusalem Noé Enoch"]}]},
    "nehemie": {"aliases": ["nehemie", "néhémie"], "profils": [{"nom": "Néhémie", "aliases_specifiques": ["nehemie", "néhémie"], "aliases_generiques": [], "mots_forts": ["mur", "jerusalem", "perse"], "mots_contexte": ["reconstruction", "roi"], "requetes": ["Néhémie mur Jérusalem"]}]},
    "zerubbabel": {"aliases": ["zerubbabel", "zorobabel"], "profils": [{"nom": "Zorobabel", "aliases_specifiques": ["zerubbabel", "zorobabel"], "aliases_generiques": [], "mots_forts": ["temple", "babylone", "judee"], "mots_contexte": ["reconstruction"], "requetes": ["Zorobabel temple Jérusalem"]}]},
})

PERSONNAGES_UNIQUES = {"noe", "noé", "isaac", "jacob", "israel", "israël", "lot", "sara", "sarah", "hagar", "ishmael", "ezekias", "ezechias", "josias", "ozias", "jeroboam", "rehoboam", "samuel", "jonathan", "jeremie", "jérémie", "isaie", "isaïe", "ezechiel", "daniel", "osée", "osee", "joel", "amos", "abdias", "jonas", "michee", "michée", "nahum", "habacuc", "sophonie", "aggée", "aggee", "zacharie", "malachie", "job", "esdras", "mardochee", "mardochée", "gideon", "gédéon", "samson", "delila", "delilah", "debora", "déborah", "barak", "jephte", "caleb", "josue", "josué", "aaron", "levi", "lévi", "benjamin", "reuben", "juda", "judah", "issacar", "zebulon", "zabulon", "dan", "nephthali", "gad", "aser", "ephraim", "éphraïm", "manasse", "barnabas", "timothee", "timothée", "tite", "silas", "etienne", "étienne", "philippe", "matthias", "matthieu", "mathieu", "marc", "luc", "marthe", "lazare", "nicodeme", "nicodème", "zachee", "zachée", "bartimee", "bartimée", "jairus", "jaïrus", "corneille", "lydie", "priscille", "aquilas", "pharaon", "pilate", "herodias", "hérodiade", "barabbas", "judas", "thomas", "andre", "andré"}
HORS_SUJETS_STRICTS = ["messi", "ronaldo", "football", "meteo", "météo", "python", "javascript", "programme", "programming", "capitale", "president", "président", "recette de cuisine", "formule 1"]
TERMES_BIBLIQUES = ["bible", "biblique", "jesus", "jésus", "dieu", "seigneur", "christ", "evangile", "évangile", "ancien testament", "nouveau testament", "apotre", "apôtre", "disciple", "prophete", "prophète", "psaume", "verset", "chapitre", "eglise", "église", "priere", "prière", "peche", "péché", "foi", "amour", "salut", "grace", "grâce"]

@lru_cache(maxsize=1000)
def est_hors_sujet_absolu(question: str) -> bool:
    q = normaliser_texte(question)
    # PROD FIX: whitelist biblique -> ne bloque pas si termes bibliques présents
    if any(contient_terme(q, t) for t in TERMES_BIBLIQUES):
        return False
    return any(contient_terme(q, t) for t in HORS_SUJETS_STRICTS)

def detecter_alias_explicite(question: str, alias: str) -> bool: return contient_terme(question, alias)
def trouver_mentions_personnages(question: str) -> List[Dict[str, Any]]:
    mentions = []
    for cle_famille, famille in DICTIONNAIRE_PERSONNAGES.items():
        aliases_trouves = [a for a in famille["aliases"] if detecter_alias_explicite(question, a)]
        if aliases_trouves: mentions.append({"famille": cle_famille, "aliases": aliases_trouves})
    return mentions

def calculer_score_profil(question: str, profil: Dict[str, Any]) -> Dict[str, Any]:
    score = 0; spec=[]; gener=[]
    for alias in profil.get("aliases_specifiques", []):
        if contient_terme(question, alias): score+=100; spec.append(alias)
    for alias in profil.get("aliases_generiques", []):
        if contient_terme(question, alias): score+=15; gener.append(alias)
    for mot in profil.get("mots_forts", []):
        if contient_terme(question, mot): score+=12
    for mot in profil.get("mots_contexte", []):
        if contient_terme(question, mot): score+=4
    return {"score": score, "aliases_specifiques": spec, "aliases_generiques": gener}

def analyser_famille_personnage(question: str, famille: Dict[str, Any]) -> Dict[str, Any]:
    resultats = []
    for profil in famille["profils"]:
        analyse = calculer_score_profil(question, profil)
        resultats.append({"profil": profil, "score": analyse["score"], "aliases_specifiques": analyse["aliases_specifiques"], "aliases_generiques": analyse["aliases_generiques"]})
    resultats.sort(key=lambda r: r["score"], reverse=True)
    if not resultats: return {"statut": "ambigu", "profil": None, "score": 0, "possibilites": []}
    meilleur = resultats[0]
    if len(resultats)==1 or meilleur["aliases_specifiques"]: return {"statut": "identifie", "profil": meilleur["profil"], "score": meilleur["score"], "possibilites": resultats}
    ecart = meilleur["score"] - resultats[1]["score"]
    if meilleur["score"]>=35 and ecart>=10: return {"statut": "identifie", "profil": meilleur["profil"], "score": meilleur["score"], "possibilites": resultats}
    return {"statut": "ambigu", "profil": None, "score": meilleur["score"], "possibilites": resultats}

def analyser_personnage_question(question: str) -> Dict[str, Any]:
    personnages_identifies=[]; ambiguities=[]; familles_detectees=[]
    for mention in trouver_mentions_personnages(question):
        cle_famille=mention["famille"]; famille=DICTIONNAIRE_PERSONNAGES[cle_famille]; familles_detectees.append(cle_famille)
        analyse=analyser_famille_personnage(question, famille)
        if analyse["statut"]=="identifie": personnages_identifies.append({"famille": cle_famille, "profil": analyse["profil"], "score": analyse["score"], "aliases": mention["aliases"]})
        else: ambiguities.append({"famille": cle_famille, "possibilites": analyse["possibilites"], "aliases": mention["aliases"]})
    qn=normaliser_texte(question)
    for nom in PERSONNAGES_UNIQUES:
        if not contient_terme(qn, nom): continue
        if any(contient_terme(p["profil"]["nom"], nom) for p in personnages_identifies): continue
        personnages_identifies.append({"famille": nom, "profil": {"nom": nom.capitalize(), "aliases_specifiques": [nom], "aliases_generiques": [], "mots_forts": [], "mots_contexte": [], "requetes": [nom]}, "score": 100, "aliases": [nom]})
    if any(a["famille"]=="simon" for a in ambiguities):
        indices_pierre=["reniement","renie jesus","renie","pentecote","cephas","cles","corneille","filets","pecheur","trois fois"]
        if any(contient_terme(qn, i) for i in indices_pierre):
            nouv=[];
            for amb in ambiguities:
                if amb["famille"]!="simon": nouv.append(amb); continue
                pp=next((p for p in DICTIONNAIRE_PERSONNAGES["simon"]["profils"] if p["nom"]=="Simon Pierre (l'apôtre Pierre)"), None)
                if pp: personnages_identifies.append({"famille": "simon","profil": pp,"score": 100,"aliases": ["simon"]})
            ambiguities=nouv
    uniques=[]; noms_vus=set()
    for p in personnages_identifies:
        nom=p["profil"]["nom"]
        if nom in noms_vus: continue
        noms_vus.add(nom); uniques.append(p)
    return {"personnages": uniques, "ambiguities": ambiguities, "familles_detectees": familles_detectees, "plusieurs_personnages": len(uniques)>1}

def afficher_ambiguite_personnage(ambiguite: Dict[str, Any]) -> Dict[str, Any]:
    poss=[r.get("profil", {}).get("nom","Inconnu") for r in ambiguite.get("possibilites", [])]
    return {"type":"ambiguite","possibilites":poss}

def est_question_action_ou_relation(question: str) -> bool:
    texte=normaliser_texte(question)
    motifs=[r"\ba\s*t\s*il\b", r"\best\s*[-]?\s*il\b", r"\bavait\s*[-]?\s*il\b", r"\bpeut\s*[-]?\s*il\b"]
    if any(re.search(m, texte) for m in motifs): return True
    termes_relations=["connaissait","connu","relation","entre","frere","soeur","pere","mere","fils","fille","epoux","mari","femme","parent","ami"]
    if any(contient_terme(texte,t) for t in termes_relations): return True
    termes_actions=["vendu","vendre","renie","suivi","tue","parle","vu","rencontre","aime","prie","appele","pardonne","benit","guerit","trahi","choisi","envoye","enseigne","baptise","ressuscite"]
    return any(contient_terme(texte,t) for t in termes_actions)

@lru_cache(maxsize=2000)
def _normaliser_separateurs_reference(texte: str) -> str:
    texte=normaliser_texte(texte); texte=texte.replace("’","'"); texte=RE_CHAPITRE.sub(" ", texte); texte=RE_VERSET.sub(" ", texte)
    texte=re.sub(r"\s+a\s+", " - ", texte); texte=re.sub(r"\s*:\s*", " ", texte); texte=re.sub(r"\s*-\s*", " - ", texte); texte=RE_ESPACES.sub(" ", texte)
    return texte.strip()

@lru_cache(maxsize=2000)
def trouver_reference_biblique(question: str) -> Optional[Dict[str, str]]:
    qn=_normaliser_separateurs_reference(str(question))
    livres=["genese","exode","levitique","nombres","deuteronome","josue","juges","ruth","1 samuel","2 samuel","1 rois","2 rois","1 chroniques","2 chroniques","esdras","nehemie","esther","job","psaumes","proverbes","ecclesiaste","cantique des cantiques","esaie","jeremie","lamentations","ezechiel","daniel","osee","joel","amos","abdias","jonas","michee","nahum","habacuc","sophonie","aggee","zacharie","malachie","matthieu","marc","luc","jean","actes","romains","1 corinthiens","2 corinthiens","galates","ephesiens","philippiens","colossiens","1 thessaloniciens","2 thessaloniciens","1 timothee","2 timothee","tite","philemon","hebreux","jacques","1 pierre","2 pierre","1 jean","2 jean","3 jean","jude","apocalypse"]
    livres_tries=sorted(livres, key=len, reverse=True); pattern="|".join(re.escape(l) for l in livres_tries)
    m=re.search(rf"""\b({pattern})\s+(\d+)(?:\s+(\d+))?(?:\s*-\s*(\d+))?\b""", qn, flags=re.IGNORECASE|re.VERBOSE)
    if not m or not m.group(3): return None
    livre, chapitre, verset, verset_fin=m.group(1).strip(), m.group(2), m.group(3), m.group(4)
    ref=f"{livre} {chapitre}:{verset}" + (f"-{verset_fin}" if verset_fin else "")
    return {"livre": livre, "chapitre": chapitre, "verset": verset, "verset_fin": verset_fin, "reference_complete": ref}

def construire_requetes_reference(question: str, reference: Dict[str, Any]) -> List[str]:
    requetes=[question]
    rc=reference.get("reference_complete",""); livre=reference.get("livre",""); chapitre=reference.get("chapitre",""); verset=reference.get("verset",""); verset_fin=reference.get("verset_fin")
    if rc: requetes.append(rc)
    if livre and chapitre and verset: requetes.extend([f"{livre} {chapitre}:{verset}", f"{livre} {chapitre} {verset}"])
    if verset_fin: requetes.extend([f"{livre} {chapitre}:{verset}-{verset_fin}", f"{livre} {chapitre} {verset} {verset_fin}"])
    final=[]; vus=set()
    for r in requetes:
        cle=normaliser_texte(r)
        if cle in vus: continue
        vus.add(cle); final.append(r)
    return final

def construire_contexte(versets: List[Any]) -> str:
    # PROD FIX: ne coupe jamais un verset au milieu + limite tokens
    lignes=[]; tokens=0
    for v in versets[:MAX_VERSETS_RAG]:
        if not isinstance(v, dict): continue
        ref=v.get("reference", v.get("ref","")); txt=v.get("texte", v.get("text",""))
        if not ref or not txt: continue
        bloc=f"- {ref} : {txt}"
        tok=len(bloc)//4
        if tokens+tok>MAX_TOKENS_CONTEXT and lignes: break
        lignes.append(bloc); tokens+=tok
    return "\n".join(lignes)

def rechercher_contexte_personnages(question: str, analyse_personnages: Dict[str, Any], nombre_resultats: int = 5) -> List[Dict[str, Any]]:
    recherches=[question]; noms=[]
    for p in analyse_personnages.get("personnages", []):
        profil=p.get("profil", {}); nom=profil.get("nom","")
        if nom: noms.append(nom)
        recherches.extend(profil.get("requetes", []))
    if analyse_personnages.get("ambiguities") and est_question_action_ou_relation(question):
        for amb in analyse_personnages.get("ambiguities", []):
            for poss in amb.get("possibilites", []):
                profil=poss.get("profil", {}); nom=profil.get("nom","")
                if nom: noms.append(nom)
                for rq in profil.get("requetes", []): recherches.append(f"{rq} {question}")
                if nom: recherches.append(f"{nom} {question}")
    noms_uniques=[]
    for n in noms:
        if n and n not in noms_uniques: noms_uniques.append(n)
    if len(noms_uniques)>=2: recherches.append(" ".join(noms_uniques)+" "+question)
    final=[]; vues=set()
    for rq in recherches:
        if not isinstance(rq, str) or not rq.strip(): continue
        try:
            orch=_get_orchestrator()
            if MOTEUR_PROD_DISPO and orch.moteur:
                resultats=orch.moteur.rechercher(rq.strip(), nombre_resultats=nombre_resultats)
            elif fallback_rechercher:
                resultats=fallback_rechercher(rq.strip(), nombre_resultats=nombre_resultats)
            else: resultats=[]
        except Exception: continue
        if not resultats: continue
        for verset in resultats:
            if not isinstance(verset, dict): continue
            ref=verset.get("reference", verset.get("ref","")); txt=verset.get("texte", verset.get("text",""))
            cle=("reference:"+normaliser_texte(ref)) if ref else ("texte:"+normaliser_texte(txt))
            if cle in vues: continue
            vues.add(cle); final.append(verset)
            if len(final)>=MAX_RESULTATS_PERSONNAGES: return final
    return final

def rechercher_par_reference(question: str, reference: Dict[str, Any], nombre_resultats: int = 5) -> List[Dict[str, Any]]:
    requetes=construire_requetes_reference(question, reference)
    final=[]; vues=set()
    for rq in requetes:
        try:
            orch=_get_orchestrator()
            if MOTEUR_PROD_DISPO and orch.moteur:
                resultats=orch.moteur.rechercher(rq, nombre_resultats=nombre_resultats)
            elif fallback_rechercher:
                resultats=fallback_rechercher(rq, nombre_resultats=nombre_resultats)
            else: resultats=[]
        except Exception: continue
        if not resultats: continue
        for v in resultats:
            if not isinstance(v, dict): continue
            ref=v.get("reference", v.get("ref","")); txt=v.get("texte", v.get("text",""))
            cle=("reference:"+normaliser_texte(ref)) if ref else ("texte:"+normaliser_texte(txt))
            if cle in vues: continue
            vues.add(cle); final.append(v)
    return final

def preparer_historique_pour_modele(historique: List[Any]) -> List[Dict[str, str]]:
    if not isinstance(historique, list): return []
    propre=[]
    for el in historique[-MAX_HISTORIQUE_ENTRIES:]:
        if not isinstance(el, dict): continue
        if el.get("role") not in {"user","assistant"}: continue
        contenu=str(el.get("content","") or "").strip()
        if not contenu: continue
        propre.append({"role": el.get("role"), "content": contenu[:MAX_LONGUEUR_ENTREE_HISTORIQUE]})
    final=[]; total=0
    for el in reversed(propre):
        if total+len(el["content"])>MAX_LONGUEUR_HISTORIQUE_TOTAL: break
        final.append(el); total+=len(el["content"])
    final.reverse(); return final

def generateur_accepte_historique() -> bool:
    if generer_reponse_biblique is None: return False
    try:
        sig=inspect.signature(generer_reponse_biblique); params=sig.parameters
        if "historique" in params: return True
        return any(p.kind==inspect.Parameter.VAR_KEYWORD for p in params.values())
    except Exception: return False

def appeler_generateur(question: str, versets_contexte: Any, niveau_utilisateur: str, historique: List[Any]) -> str:
    historique_propre=preparer_historique_pour_modele(historique)
    if generer_reponse_biblique is None:
        return construire_contexte(versets_contexte if isinstance(versets_contexte, list) else [])
    if generateur_accepte_historique():
        return generer_reponse_biblique(question, versets_contexte, niveau_utilisateur, historique=historique_propre)
    return generer_reponse_biblique(question, versets_contexte, niveau_utilisateur)

# ============================================================
# ORCHESTRATOR PROD - Singleton thread-safe pour 100 users
# ============================================================
class BibleOrchestratorPROD:
    def __init__(self):
        self._loaded=False
        self._load_lock=threading.Lock()
        self.moteur=None
    def _ensure_loaded(self):
        if self._loaded: return
        with self._load_lock:
            if self._loaded: return
            if MOTEUR_PROD_DISPO and MoteurBibliquePROD:
                try:
                    self.moteur=MoteurBibliquePROD()
                    logger.info("Orchestrator PROD: moteur chargé")
                except Exception:
                    logger.exception("Echec init moteur PROD")
                    self.moteur=None
            self._loaded=True

def _get_orchestrator():
    global _orchestrator_singleton
    if _orchestrator_singleton is None:
        with _lock:
            if _orchestrator_singleton is None:
                _orchestrator_singleton=BibleOrchestratorPROD()
    return _orchestrator_singleton

# ============================================================
# API PROD - Fonction principale - NE CASSE RIEN
# ============================================================
def traiter_question_bible(question: str, niveau_utilisateur: str = "18+", historique: List[Any] = None) -> Dict[str, Any]:
    if historique is None: historique=[]
    ok, q_or_msg = valider_question(question)
    if not ok:
        return {"erreur": "validation", "reponse": q_or_msg, "versets": [], "sources": []}
    question = q_or_msg
    if est_hors_sujet_absolu(question):
        return {"erreur": "Hors sujet", "reponse": "Cette question sort du domaine de BIBLE-IA, dédié à la Bible.", "versets": [], "sources": []}

    orch = _get_orchestrator()
    orch._ensure_loaded()

    reference=trouver_reference_biblique(question)
    analyse=analyser_personnage_question(question)

    resultats=None
    if reference:
        resultats=rechercher_par_reference(question, reference, nombre_resultats=NOMBRE_VERSETS_DEFAUT)
    if resultats is None or not resultats:
        if analyse["personnages"]:
            resultats=rechercher_contexte_personnages(question, analyse, nombre_resultats=NOMBRE_VERSETS_DEFAUT)
        elif analyse.get("ambiguities") and est_question_action_ou_relation(question):
            resultats=rechercher_contexte_personnages(question, analyse, nombre_resultats=NOMBRE_VERSETS_DEFAUT)
        else:
            try:
                if orch.moteur:
                    resultats=orch.moteur.rechercher(question, nombre_resultats=20)
                elif fallback_rechercher:
                    resultats=fallback_rechercher(question, nombre_resultats=20)
                else: resultats=[]
            except Exception:
                logger.exception("Erreur recherche orchestrator")
                resultats=[]

    if not resultats:
        amb = analyse["ambiguities"][0] if analyse.get("ambiguities") else None
        if amb:
            return {"erreur": "ambiguite", "ambiguite": afficher_ambiguite_personnage(amb), "reponse": f"Plusieurs {amb['famille']} existent. Peux-tu préciser? Options: {', '.join([p.get('profil',{}).get('nom','') for p in amb.get('possibilites',[])[:3]])}", "versets": [], "sources": []}
        return {"erreur": "Aucun passage", "reponse": "Je n'ai trouvé aucun passage suffisamment pertinent. Peux-tu reformuler?", "versets": [], "sources": []}

    # Filtrage PROD: exclure faible/hors_sujet, garder max 5, priorité référence
    filtres = [r for r in resultats if r.get("niveau_pertinence") in ("directe","forte","moderee") or r.get("est_reference_demandee")]
    if not filtres:
        filtres = [r for r in resultats if r.get("score_final",0) > 0.12] or resultats[:1]
    refs_demandees = [r for r in filtres if r.get("est_reference_demandee")]
    if refs_demandees:
        autres = [r for r in filtres if not r.get("est_reference_demandee")]
        filtres = refs_demandees + autres
    sources_finales = filtres[:MAX_VERSETS_RAG]

    contexte_str = construire_contexte(sources_finales)
    if not contexte_str.strip():
        return {"erreur": "Contexte vide", "reponse": "Contexte vide après filtrage.", "versets": [], "sources": []}

    try:
        reponse=appeler_generateur(question, sources_finales, normaliser_niveau_utilisateur(niveau_utilisateur), historique)
    except Exception:
        logger.exception("Erreur generateur")
        return {"erreur": "Erreur technique", "reponse": "Désolé, erreur technique temporaire. Réessaye.", "versets": sources_finales, "sources": sources_finales}

    if not isinstance(reponse, str): reponse=str(reponse)

    return {
        "reponse": reponse.strip(),
        "versets": sources_finales,
        "sources": sources_finales,
        "references": [r.get("reference") for r in sources_finales],
        "personnages": analyse["personnages"],
        "niveau_pertinence_top": sources_finales[0].get("niveau_pertinence") if sources_finales else "inconnu"
    }

def demarrer_application(niveau_utilisateur: str = "18+"):
    niveau_utilisateur=normaliser_niveau_utilisateur(niveau_utilisateur)
    logging.basicConfig(level=logging.INFO)
    print("\n"+"="*60); print("📖 BIBLE-IA (Jack + Mémoire Ben) - PROD"); print("="*60); print(f"\n🎓 Niveau: {niveau_utilisateur}"); print("💡 /exit pour quitter, /clear pour effacer")
    hist=[]
    while True:
        try: question=input("\n❓ Ta question : ")
        except (EOFError, KeyboardInterrupt): print("\n👋 A bientôt!"); break
        question=str(question or "").strip()
        if not question: continue
        cmd=question.lower()
        if cmd in {"/exit","/quit","exit","quit"}: print("\n👋 A bientôt!"); break
        if cmd in {"/clear","clear"}: hist=[]; print("\n🧹 Mémoire effacée."); continue
        res=traiter_question_bible(question, niveau_utilisateur, hist)
        if "erreur" in res and "reponse" not in res:
            if res.get("ambiguite"): print("\n🤔 Ambiguïté:", afficher_ambiguite_personnage(res["ambiguite"]))
            else: print(f"\n⚠️ {res['erreur']}")
            continue
        print("\n"+"="*60); print("📖 RÉPONSE DE BIBLE-IA"); print("="*60); print(f"\n{res['reponse']}")
        print(f"\n📚 Sources: {[r.get('reference') for r in res.get('versets',[])]} | Pertinence: {res.get('niveau_pertinence_top')}")
        hist.append({"role":"user","content":question}); hist.append({"role":"assistant","content":res["reponse"]}); hist=hist[-MAX_HISTORIQUE_ENTRIES:]

if __name__ == "__main__":
    demarrer_application()
    