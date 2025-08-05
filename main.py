from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import pickle
import pandas as pd
from fastapi.responses import JSONResponse
from schema.schema import Patient
from schema.predict import make_predict
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction APP"}
@app.get("/health")
def health_check():
    return {"statuscode": "200", "message": "The API is running smoothly."}
@app.post("/predict")
def predict(patient: Patient):
    # converting input in the same format as training data
    input_df = pd.DataFrame([{
        "Pregnancies": patient.pregnancies,
        "Glucose": patient.glucose,
        "BloodPressure": patient.blood_pressure,
        "SkinThickness": patient.skin_thickness,
        "Insulin": patient.insulin,
        "BMI": patient.bmi,
        "DiabetesPedigreeFunction": patient.diabetes_pedigree_function,
        "Age": patient.age
    }])

    # Run prediction
    try:
        ans = make_predict(input_df)
        return JSONResponse(status_code=200, content={"predicted_category": ans})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))