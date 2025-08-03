# 🩺 Diabetes Prediction App

This is a simple **Machine Learning web app** built using **FastAPI (backend)** and **Streamlit (frontend)** that predicts the likelihood of diabetes in a patient based on medical parameters.

## 🚀 Tech Stack

- 🐍 Python 3.11
- ⚡ FastAPI (ML model API)
- 📊 Streamlit (frontend UI)
- 🤖 Scikit-learn (trained ML model)
- 📦 Pydantic, Uvicorn, Requests, Pandas, etc.

---

## 📦 Project Structure

📁 diabetes_prediction_app/
│
├── main.py # FastAPI backend
├── frontend.py # Streamlit frontend UI
├── model.pkl # Trained ML model (pickle file)
├── requirements.txt # Python dependencies
├── Untitled8.ipynb # Jupyter notebook (optional dev notes)
└── pycache/ # Auto-generated Python cache

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/ayushhhh2999/diabetes_prediction_app.git
cd diabetes_prediction_app
2. Create a virtual environment and activate
bash
Copy
Edit
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run FastAPI backend
bash
Copy
Edit
uvicorn main:app --reload
Open browser and visit: http://localhost:8000/docs

5. Run Streamlit frontend (new terminal)
bash
Copy
Edit
streamlit run frontend.py
🧠 Model Info
The model was trained on the popular PIMA Indians Diabetes Dataset with features such as:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age
<img width="1919" height="959" alt="image" src="https://github.com/user-attachments/assets/66af844f-a212-44a4-9ff5-3fb4c9d213cb" />
<img width="1912" height="918" alt="image" src="https://github.com/user-attachments/assets/9ba492d3-265f-47cf-a4db-e75ab91da4cb" />

📤 API Endpoint
POST /predict

Request JSON:

json
Copy
Edit
{
  "pregnancies": 2,
  "glucose": 120,
  "bloodPressure": 70,
  "skinThickness": 20,
  "insulin": 80,
  "diabetespedigreeFunction": 0.3,
  "Age": 30,
  "bmi": 25.5
}
Response JSON:

json
Copy
Edit
{
  "predicted_category": 1
}
