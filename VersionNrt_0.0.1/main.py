import pandas as pd
import joblib
import numpy as np
from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

model = joblib.load('Nirintsoa0.0.1/model.joblib')
scaler = joblib.load('Nirintsoa0.0.1/scaler.joblib')

class Irisinput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "Bienvenue dans mon API"}

@app.get('/predict')
def predict_iris(
    sepal_length: float = Query(..., description="Longueur du sépale"),
    sepal_width: float = Query(..., description="Largeur du sépale"),
    petal_length: float = Query(..., description="Longueur du pétale"),
    petal_width: float = Query(..., description="Largeur du pétale"),
):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    new_data = scaler.transform(input_data)
    prediction = model.predict(new_data)[0]
    return {'prediction': int(prediction)}


if __name__ == "__main__":
    uvicorn.run(app)
