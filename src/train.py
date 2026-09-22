import json 
from pathlib import Path 
import joblib 
from sklearn.ensemble import HistGradientBoostingRegressor 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from src.data import load_processed 
from src.features import create_features 
 
data = create_features(load_processed()) 
target = 'tomorrow_aqi' 
columns = [c for c in data.columns if c != target] 
split = int(len(data) * 0.85) 
train, test = data.iloc[:split], data.iloc[split:] 
model = HistGradientBoostingRegressor(max_iter=200, learning_rate=.05, random_state=42) 
model.fit(train[columns], train[target]) 
pred = model.predict(test[columns]) 
metrics = {'mae': mean_absolute_error(test[target], pred), 
           'rmse': mean_squared_error(test[target], pred) ** .5, 
           'r2': r2_score(test[target], pred)} 
Path('models').mkdir(exist_ok=True); Path('reports').mkdir(exist_ok=True) 
joblib.dump(model, 'models/aqi_model.joblib') 
Path('models/feature_columns.json').write_text(json.dumps(columns, indent=2)) 
Path('reports/metrics.json').write_text(json.dumps(metrics, indent=2)) 
print(metrics) 