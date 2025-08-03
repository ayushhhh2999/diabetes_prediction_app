from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import pickle
import pandas as pd
from fastapi.responses import JSONResponse

app = FastAPI()

# Loading my model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Input schema
class Patient(BaseModel):
    pregnancies: int = Field(..., ge=0, description="Number of pregnancies (non-negative integer).")
    glucose: int = Field(..., ge=0, le=300, description="Plasma glucose concentration (0-300).")
    blood_pressure: int = Field(..., alias="bloodPressure", ge=0, le=200, description="Diastolic blood pressure in mm Hg (0-200).")
    skin_thickness: int = Field(..., alias="skinThickness", ge=0, le=100, description="Triceps skinfold thickness in mm (0-100).")
    insulin: int = Field(..., ge=0, le=1000, description="2-Hour serum insulin in mu U/ml (0-1000).")
    diabetes_pedigree_function: float = Field(..., alias="diabetespedigreeFunction", ge=0, le=3.0, description="Genetic diabetes influence factor (0.0–3.0).")
    age: int = Field(..., alias="Age", ge=1, le=120, description="Patient's age in years (1–120).")
    bmi: Optional[float] = Field(None, ge=10, le=60, description="Body Mass Index (optional)")

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
        prediction = model.predict(input_df)[0]
        ans = "He has diabetes" if bool(prediction) == True else "He does not have diabetes"
        return JSONResponse(status_code=200, content={"predicted_category": ans})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
