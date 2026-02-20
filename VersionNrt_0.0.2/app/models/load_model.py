# ============================================================
# Fichier de chargement du modèle ML
# Ce fichier charge le modèle sauvegardé (model.joblib) depuis
# le disque et le met à disposition pour les prédictions.
# ============================================================

import joblib

from app.config.config import MODEL_PATH

def get_model():
    """
    Fonction qui charge et retourne le modèle ML depuis le fichier .joblib.

    Le modèle est un Pipeline scikit-learn qui contient :
    - StandardScaler : pour normaliser les données (mise à l'échelle)
    - LogisticRegression : pour faire la classification binaire (0 ou 1)

    Returns:
        model: Le pipeline scikit-learn prêt à faire des prédictions
    """
    # joblib.load() lit le fichier .joblib et reconstruit l'objet Python (le pipeline)
    # MODEL_PATH est le chemin absolu vers le fichier model.joblib défini dans config.py
    model = joblib.load(MODEL_PATH)

    # On retourne le modèle chargé pour qu'il puisse être utilisé dans les routes
    return model

