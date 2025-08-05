# Input schema
from pydantic import BaseModel, Field
from typing import Optional
class Patient(BaseModel):
    pregnancies: int = Field(..., ge=0, description="Number of pregnancies (non-negative integer).")
    glucose: int = Field(..., ge=0, le=300, description="Plasma glucose concentration (0-300).")
    blood_pressure: int = Field(..., alias="bloodPressure", ge=0, le=200, description="Diastolic blood pressure in mm Hg (0-200).")
    skin_thickness: int = Field(..., alias="skinThickness", ge=0, le=100, description="Triceps skinfold thickness in mm (0-100).")
    insulin: int = Field(..., ge=0, le=1000, description="2-Hour serum insulin in mu U/ml (0-1000).")
    diabetes_pedigree_function: float = Field(..., alias="diabetespedigreeFunction", ge=0, le=3.0, description="Genetic diabetes influence factor (0.0–3.0).")
    age: int = Field(..., alias="Age", ge=1, le=120, description="Patient's age in years (1–120).")
    bmi: Optional[float] = Field(None, ge=10, le=60, description="Body Mass Index (optional)")
