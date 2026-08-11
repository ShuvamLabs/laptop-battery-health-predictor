import pandas as pd
import joblib

def loadmodel():
    path = r"C:\Users\HP\Documents\PycharmProjects\laptop-battery-health-predictor\model\best-model.pkl"
    return joblib.load(path)

def predict(new_data):
    model = loadmodel()
    data = pd.DataFrame(new_data)
    prediction = model.predict(data)
    return prediction
