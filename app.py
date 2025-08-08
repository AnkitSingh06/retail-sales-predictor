import streamlit as st  # type: ignore
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("lr_model.pkl")

# ----------------------------
# Streamlit App Interface
# ----------------------------
st.title("🛍️ Retail Sales Prediction App")

# Manual input
st.subheader("🧾 Enter Store Details")
store_size = st.number_input("Store Size (sq ft)", min_value=500, max_value=5000, value=1500)
location_rating = st.slider("Location Rating (1-5)", 1, 5, 3)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=1000, max_value=100000, value=20000)

# Only runs when button is clicked
if st.button("Predict Sales"):
    # ✅ Define input_df safely inside this block
    input_df = pd.DataFrame([[store_size, location_rating, marketing_spend]],
                            columns=["Store_Size", "Location_Rating", "Marketing_Spend"])
    
    # ✅ Now input_df is defined, and we can inspect the model's expected features
    st.write("Model was trained on features:", model.feature_names_in_)
    st.write("Input DataFrame:", input_df)

    # Make prediction
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Monthly Sales: ${prediction:,.2f}")
