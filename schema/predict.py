
import pickle
import pandas as pd
from fastapi.responses import JSONResponse
def make_predict(input: pd.DataFrame):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
        prediction = model.predict(input)[0]
        ans = "He has diabetes" if bool(prediction) == True else "He does not have diabetes"
        return ans 