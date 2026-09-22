from src.predict import predict_latest 
 
def test_prediction_contract(): 
    result = predict_latest() 
    assert result['prediction'] >= 0 
    assert result['category'] in { 
        'Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe' 
    } 
    assert result['model_version'] == 'v1' 