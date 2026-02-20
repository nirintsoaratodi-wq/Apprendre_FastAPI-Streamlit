# ============================================================
# Fichier de configuration de l'application
# Ce fichier contient les paramètres globaux utilisés
# dans toute l'application, notamment le chemin du modèle ML.
# ============================================================

from pathlib import Path
# BASE_DIR est le répertoire de base de l'application (le dossier app)
BASE_DIR = Path(__file__).resolve().parent.parent
# MODEL_PATH construit le chemin complet vers le fichier model.joblib
MODEL_PATH = BASE_DIR / "models" / "model.joblib"
