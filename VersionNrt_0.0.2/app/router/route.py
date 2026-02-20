from fastapi import APIRouter
import numpy as np
from app.schemas.schema import InputData
from app.schemas.schema import PredictionResponse # Importation du schéma de sortie (la réponse que l'API retourne)
from app.models.load_model import get_model # Importation de la fonction qui charge le modèle ML 

router = APIRouter(
    prefix="/ml",
    tags=["Prediction"]
)

model = get_model()

@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Prédire si une personne va acheter",
    description="Envoyer les données (gender, age, estimated_salary) pour obtenir une prédiction d'achat."
)
def predict(data: InputData):
    """
    Endpoint de prédiction.

    Reçoit les données d'un utilisateur (genre, âge, salaire estimé)
    et retourne si la personne est susceptible d'acheter (0 ou 1)
    avec la probabilité associée.

    Args:
        data (InputData): Les données d'entrée validées par Pydantic

    Returns:
        PredictionResponse: La prédiction (0 ou 1) et la probabilité d'achat
    """
    
    input_array = np.array([[data.gender, data.age, data.estimated_salary]])

    prediction = int(model.predict(input_array)[0])

    # model.predict_proba() retourne un tableau de probabilités pour chaque classe
    # La forme du résultat est [[proba_classe_0, proba_classe_1]]
    # [0] accède à la première observation
    # [1] accède à la probabilité de la classe 1 (achat = OUI)
    # round(..., 4) arrondit à 4 décimales pour une meilleure lisibilité
    probability = round(float(model.predict_proba(input_array)[0][1]), 4)

    # On retourne un dictionnaire qui sera automatiquement converti en JSON par FastAPI
    # Ce dictionnaire correspond au schéma PredictionResponse (prediction + probability)
    return {
        "prediction": prediction,       # Le résultat : 0 (n'achète pas) ou 1 (achète)
        "probability": probability       # La probabilité d'achat (entre 0.0 et 1.0)
    }
