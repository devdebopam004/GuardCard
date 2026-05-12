import streamlit as st
import joblib
import pandas as pd
import lightgbm as lgb
from geopy.distance import geodesic

model = joblib.load('Fraud_detection_model.jb')
encoders = joblib.load('label_encoders.jb')

def haversine(lat1, lon1, lat2, lon2):
    return geodesic((lat1,lon1),(lat2,lon2)).km 

st.title('GuardCard')
st.write('AI Powered Credit Card Fraud Detection')

merchant= st.text_input('Merchant Name')
category = st.text_input('Category')
amt = st.number_input('Transaction Amount', min_value=0.0, format="%.2f")
lat = st.number_input('Latitude', format="%.6f")
long = st.number_input('Longitude', format="%.6f")
merch_lat = st.number_input('Merchant Latitude', format="%.6f")
merch_long = st.number_input('Merchant Longitude', format="%.6f")
hour = st.slider('Transaction Hour', 0, 23, 12)
day = st.slider('Transaction Day', 1, 31, 15)
month = st.slider('Transaction Month', 1, 12, 6)
gender = st.selectbox("Gender",["Male","Female"])
cc_num = st.text_input('Credit Card Number')

distance = haversine(lat, long, merch_lat, merch_long)

if st.button('Check for Fraud'):
    if merchant and category and cc_num:
        input_data = pd.DataFrame([[merchant, category, amt, distance, hour, day, month, gender, cc_num]],
                                  columns=['merchant', 'category', 'amt', 'distance', 'hour', 'day', 'month', 'gender', 'cc_num'])
        categorical_col = ['merchant', 'category', 'gender']
        for col in categorical_col:
            try:
                input_data[col] = encoders[col].transform(input_data[col])
            except ValueError:
                input_data[col] = -1
    input_data['cc_num'] = input_data['cc_num'].apply(lambda x: hash(x) % (10 ** 2))
    prediction = model.predict(input_data)[0]
    result= 'Fraudulent' if prediction == 1 else 'Legitimate'
    st.subheader(f'The transaction is predicted to be: {result}')
else:
    st.error('Please fill in all the required fields and click the button to check for fraud.')