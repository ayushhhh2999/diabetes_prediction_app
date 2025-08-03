import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"  # Changing my server IP/port if deployed

st.title("Diabetes Prediction App")
st.markdown("Enter patient details below:")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin (mu U/ml)", min_value=0, max_value=1000, value=80)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI (optional)", min_value=10.0, max_value=60.0, value=25.0)

# Predict button
if st.button("Predict Diabetes"):
    input_data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "bloodPressure": blood_pressure,
        "skinThickness": skin_thickness,
        "insulin": insulin,
        "diabetespedigreeFunction": diabetes_pedigree_function,
        "Age": age,
        "bmi": bmi
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "predicted_category" in result:
            prediction = result["predicted_category"]
            st.success(f"🩺 Predicted Diabetes Category: **{prediction}**")
        else:
            st.error(f"❌ API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.RequestException as e:
        st.error("🚫 Failed to connect to FastAPI server.")
        st.exception(e)
