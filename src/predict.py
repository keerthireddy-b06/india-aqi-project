import json 
from pathlib import Path 
import joblib 
import pandas as pd 
from src.data import load_processed 
from src.features import create_features, aqi_category 
 
MODEL = joblib.load('models/aqi_model.joblib') 
COLUMNS = json.loads(Path('models/feature_columns.json').read_text()) 
 
def predict_latest() -> dict: 
    features = create_features(load_processed()) 
    row = features.iloc[[-1]][COLUMNS] 
    value = max(0.0, float(MODEL.predict(row)[0])) 
    return { 
        'prediction': round(value, 1), 
        'category': aqi_category(value), 
        'feature_date': str(row.index[0].date()), 
        'model_version': 'v1' 
    } 
 
if __name__ == '__main__': 
    print(predict_latest()) 