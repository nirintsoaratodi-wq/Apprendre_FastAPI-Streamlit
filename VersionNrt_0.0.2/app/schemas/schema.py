# ============================================================
# Fichier des schémas de données (Pydantic)
# Ces schémas définissent la structure des données que l'API
# attend en entrée et retourne en sortie.
# Pydantic valide automatiquement les données reçues.
# ============================================================

# Importation de BaseModel depuis pydantic : c'est la classe de base pour créer des schémas de validation
from pydantic import BaseModel
from pydantic import Field

class InputData(BaseModel):
    """
    Schéma des données d'entrée pour la prédiction.

    Ce schéma correspond aux features utilisées par le modèle ML :
    - gender : Le genre de la personne (0 = Male/Homme, 1 = Female/Femme)
    - age : L'âge de la personne (entre 18 et 100 ans)
    - estimated_salary : Le salaire estimé de la personne (entre 0 et 1 000 000)
    """
    gender: int = Field(..., ge=0, le=1, description="Genre de la personne : 0 = Male (Homme), 1 = Female (Femme)")
    age: int = Field(
        ...,  # Champ obligatoire (le client doit fournir cette valeur)
        ge=18,
        le=60,
        description="Âge de la personne (entre 18 et 60 ans)"
    )
    estimated_salary: int = Field(
        ...,  
        ge=0,  
        le=150000.0,
        description="Salaire estimé de la personne (entre 0 et 150 000)"
    )

    # La classe Config interne permet de configurer le comportement du schéma Pydantic
    class Config:
        # json_schema_extra ajoute un exemple dans la documentation Swagger de l'API
        # Cet exemple aide les utilisateurs à comprendre le format attendu
        json_schema_extra = {
            "example": {
                "gender": 0,       # Exemple : Homme
                "age": 30,         # Exemple : 30 ans
                "estimated_salary": 50000  # Exemple : salaire de 50 000
            }
        }


class PredictionResponse(BaseModel):
    """
    Schéma de la réponse retournée par l'API après une prédiction.

    - prediction : Le résultat de la prédiction (0 = N'achète pas, 1 = Achète)
    - probability : La probabilité (entre 0 et 1) que la personne achète le produit
    """

    # Champ prediction : le résultat binaire du modèle (0 ou 1)
    # 0 signifie que le modèle prédit que la personne n'achètera PAS
    # 1 signifie que le modèle prédit que la personne VA acheter
    prediction: int = Field(
        ...,  # Champ obligatoire
        description="Résultat de la prédiction : 0 = N'achète pas, 1 = Achète"
    )

    # Champ probability : la probabilité calculée par le modèle (entre 0.0 et 1.0)
    # C'est le niveau de confiance du modèle dans sa prédiction
    probability: float = Field(
        ...,  # Champ obligatoire
        description="Probabilité (entre 0 et 1) que la personne achète le produit"
    )
