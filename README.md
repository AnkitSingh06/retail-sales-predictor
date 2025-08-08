# 🛍️ Retail Sales Predictor – Business-Driven Sales Forecasting App

A **Streamlit-powered web application** designed for **retail managers, business analysts, and category heads** to forecast store-level sales using key business drivers such as store size, marketing spend, and location rating.

This tool enables faster decision-making in:
- Inventory planning  
- Campaign performance estimation  
- Regional sales performance benchmarking  

---

## 🧩 Business Context

Retail organizations often struggle with:
- Misaligned sales projections leading to over/understocking
- Non-quantified impact of marketing investments
- Poor visibility into store performance due to varying regional factors

**Solution**: A predictive model that forecasts monthly sales using core business variables, wrapped into an easy-to-use web interface.

---

## 🎯 Project Objective

Develop an interpretable and deployable machine learning solution that:
- Predicts store-level retail sales
- Helps regional managers forecast sales based on inputs they control
- Is accessible via a user-friendly web app (Streamlit)

---

## 🚀 Live Demo

👉 [Try the Live App](https://retail-sales-predictor-akfxck5hpg4wdpn3shexnn.streamlit.app/#retail-sales-prediction-app)

---

## 🧠 Model Overview

- **Algorithm**: Linear Regression (interpretable, fast)
- **Target Variable**: `Store_Sales`
- **Business Input Features**:
  - `Store_Size` (sq. ft.)
  - `Location_Rating` (footfall potential / catchment quality)
  - `Marketing_Spend` (monthly advertising budget)
  - `Monthly_Sales` (previous month's sales)

> A **Decision Tree Regressor** was also evaluated to benchmark performance.

---

## 📈 Model Performance

| Metric        | Linear Regression | Decision Tree |
|---------------|-------------------|----------------|
| MAE           | 8,762.76          | 11,732.30       |
| RMSE          | 10,646.98         | 15,046.47       |
| R² Score      | 0.15              | -0.70          |

📌 **Linear Regression** was selected due to better generalization and interpretability.

---

## 📊 Insights

- **Marketing Spend** is a strong driver of sales uplift, but shows diminishing returns.
- **Store Size** positively correlates with sales, up to an optimal range.
- **Location Rating** captures regional disparities in footfall and purchasing behavior.

---

## 📸 Visuals

### 📈 Predicted vs Actual Sales

![Predicted vs Actual](Predicted_vs_Actual.png)

Shows alignment of model predictions with real sales values.

### 🖥️ App Interface

![App Screenshot](retail_sales_prediction.png)

A clean, user-friendly interface for entering store-level parameters and getting instant sales forecasts.

---

## 💼 Business Impact (Hypothetical Scenario)

If deployed across a 500-store network:
- Forecast error (MAE) reduction: ~\$8.7K/store/month  
  → **Potential annual savings: $5M+**
- Streamlined campaign planning: Better ROI per dollar spent on marketing
- Location benchmarking: Easily identify underperforming stores

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/AnkitSingh06/retail-sales-predictor.git
cd retail-sales-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧰 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas / Numpy
- Matplotlib / Seaborn
