import json 
from pathlib import Path 
from src.data import load_processed 
 
def recent_quality(): 
    data = load_processed() 
    recent = data.tail(30) 
    result = { 
        'rows': len(recent), 
        'missing_rate': float(recent.isna().mean().mean()), 
        'average_aqi': float(recent['AQI'].mean()), 
        'maximum_aqi': float(recent['AQI'].max()) 
    } 
    Path('reports/monitoring.json').write_text(json.dumps(result, indent=2)) 
    return result 
 
if __name__ == '__main__': 
    print(recent_quality())