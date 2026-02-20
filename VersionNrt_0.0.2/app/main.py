# ============================================================
# Fichier principal de l'application FastAPI (Point d'entrée)
# Ce fichier crée l'application FastAPI, inclut les routes,
# et définit l'endpoint racine ("/") de bienvenue.
# C'est ce fichier qu'on lance avec uvicorn pour démarrer le serveur.
# ============================================================

# Importation de sys et os pour configurer le chemin Python
import sys
import os

# On ajoute le dossier parent (VersionNrt_0.0.2/) au sys.path
# Cela permet à Python de trouver le package "app" quand on lance "py main.py" depuis app/
# os.path.dirname(__file__) = le dossier où se trouve main.py (app/)
# os.path.abspath(..., "..") = le dossier parent (VersionNrt_0.0.2/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importation de uvicorn : le serveur ASGI qui fait tourner notre application FastAPI
import uvicorn

# Importation de la classe FastAPI : c'est le cœur du framework, elle crée l'application web
from fastapi import FastAPI

# Importation du routeur qui contient nos endpoints de prédiction (POST /ml/predict)
from app.router.route import router

# Création de l'instance de l'application FastAPI
# title : le nom de l'API affiché dans la documentation Swagger
# description : la description détaillée de l'API affichée dans Swagger
# version : le numéro de version de l'API (utile pour le suivi des modifications)
app = FastAPI(
    title="API de Prédiction d'Achat",
    description="API de Machine Learning pour prédire si un utilisateur va acheter un produit. "
                "Le modèle utilise le genre, l'âge et le salaire estimé comme features.",
    version="0.0.2"
)

# Inclusion du routeur dans l'application principale
# Cela ajoute toutes les routes définies dans route.py à notre application
# Les routes du routeur auront le préfixe /ml (défini dans le routeur)
# Exemple : POST /ml/predict
app.include_router(router)


# Décorateur @app.get("/") : définit une route HTTP GET sur le chemin racine "/"
# C'est la page d'accueil de l'API, accessible via http://localhost:8000/
@app.get(
    "/",
    summary="Page d'accueil",
    description="Endpoint de bienvenue qui confirme que l'API fonctionne correctement."
)
def root():
    """
    Endpoint racine de l'API.

    Retourne un message de bienvenue pour confirmer que le serveur est en marche.
    Utile pour vérifier rapidement que l'API est accessible.

    Returns:
        dict: Un dictionnaire avec un message de bienvenue
    """
    # Retourne un dictionnaire Python qui sera automatiquement converti en JSON par FastAPI
    # {"message": "..."} est la convention standard pour les réponses simples d'API
    return {
        "message": "Bienvenue sur l'API de Prédiction d'Achat - VersionNrt 0.0.2 🚀"
    }

if __name__ == "__main__":
    uvicorn.run(app)