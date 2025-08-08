# 🛍️ Retail Sales Predictor

A Streamlit-powered web app that predicts retail sales using a trained machine learning model based on store attributes. It allows business users and analysts to quickly estimate sales with intuitive inputs.

---

## 📺 Demo

👉 [Live App on Streamlit](https://retail-sales-predictor-akfxck5hpg4wdpn3shexnn.streamlit.app/#retail-sales-prediction-app)  

---

## 🧠 Model Overview

- **Type**: Linear Regression
- **Target Variable**: `Store_Sales`
- **Input Features**:
  - `Store_Area`
  - `Items_Available`
  - `Daily_Customer_Count`
  - `Store_Location_Type`
  - `Holiday_Flag`, etc.

---

## 📊 Model Evaluation

The model was evaluated using the following metrics on a hold-out test set:

| Metric              | Value        |
|---------------------|--------------|
| R² Score            | 0.85         |
| Mean Absolute Error | 1265.32      |
| RMSE                | 1624.87      |

### 📈 Predicted vs Actual Plot

![Predicted vs Actual](Predicted_vs_Actual.png)

*This plot shows how well the model predictions align with actual sales values.*

---

## 🖼️ App Preview

Below is a preview of the deployed Streamlit web app:

![App Screenshot](retail_sales_prediction.png)

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/AnkitSingh06/retail-sales-predictor.git
cd retail-sales-predictor
pip install -r requirements.txt
streamlit run app.py

