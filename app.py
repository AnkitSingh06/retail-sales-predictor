
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("lr_model.pkl")

st.title("Retail Sales Prediction App")

st.write("Enter store details to predict monthly sales:")

store_size = st.number_input("Store Size (sq ft)", min_value=500, max_value=5000, value=1500)
location_rating = st.slider("Location Rating (1-5)", 1, 5, 3)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=1000, max_value=100000, value=20000)

if st.button("Predict Sales"):
    input_df = pd.DataFrame([[store_size, location_rating, marketing_spend]],
                            columns=["Store_Size", "Location_Rating", "Marketing_Spend"])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Monthly Sales: ${prediction:,.2f}")
