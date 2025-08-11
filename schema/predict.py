from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd
from fastapi.responses import JSONResponse
import numpy as np
from typing import List
def make_predict(input1: List[int]):
    input2 = np.asarray(input1)
    input = input2.reshape(1, -1)  # Reshape input to match model's expected input shape
    with open("scaler.pkl", "rb") as f_scaler:
        scalar = pickle.load(f_scaler)
    std_data = scalar.transform(input)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        prediction = model.predict(std_data)
        ans = "He has diabetes" if prediction[0] == 1 else "He does not have diabetes"
        return ans 