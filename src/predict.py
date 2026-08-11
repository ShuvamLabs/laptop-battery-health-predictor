import joblib
import pandas as pd
from pathlib import Path

def loadmodel():
    path = Path(__file__).resolve().parent.parent/ "model" / "best-model.pkl"
    return joblib.load(path)

def predict(new_data):
    model = loadmodel()
    data = pd.DataFrame([new_data])
    prediction = model.predict(data)
    return prediction[0]
