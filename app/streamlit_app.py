import sys 
from pathlib import Path 
sys.path.append(str(Path(__file__).resolve().parents[1])) 
 
import streamlit as st 
from src.data import load_processed 
from src.predict import predict_latest 
 
st.set_page_config(page_title='India AQI Predictor', layout='wide') 
st.title('Hyderabad AQI Predictor') 
st.caption('Learning prototype using historical Indian air-quality data') 
 
result = predict_latest() 
col1, col2 = st.columns(2) 
col1.metric('Tomorrows predicted AQI', result['prediction'])
col2.metric('Predicted category', result['category']) 
 
history = load_processed() 
st.subheader('Recent AQI history') 
st.line_chart(history[['AQI']].tail(90)) 
 
with st.expander('Model details and limitations'): 
    st.write('Model version:', result['model_version']) 
    st.write('Latest feature date:', result['feature_date']) 
    st.write('This is an educational forecast, not medical advice.')