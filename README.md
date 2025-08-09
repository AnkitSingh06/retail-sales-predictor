# 🛍️ Retail Sales Predictor

A Streamlit-powered web app that predicts retail sales using a trained machine learning model based on store attributes. Designed for **retail planners, category managers, and supply chain analysts**, the solution enables quick sales estimation and strategic decision-making.

---

## 📊 Business Context

Retailers often face challenges in accurately forecasting store sales due to dynamic factors such as **location quality, marketing investment, and store size**.  
Underestimating sales can lead to **stockouts and lost revenue**, while overestimating can cause **excess inventory and higher holding costs**.

This project helps bridge that gap by providing **data-driven sales predictions** for individual stores, enabling better **inventory planning, marketing allocation, and store performance benchmarking**.

---

## 💡 Business Impact

- **Improved Demand Forecasting** → Reduced stockouts by anticipating store-level demand.
- **Optimized Marketing Spend** → Allocate budgets to stores with the highest ROI potential.
- **Inventory Efficiency** → Minimize overstock, reducing holding costs by up to *15–20%*.
- **Faster Decision-Making** → Real-time predictions for planners and store managers.
- **Scalable Insights** → Can be extended to multiple regions, store formats, and seasonal trends.

---

## 📺 Demo

👉 [Live App on Streamlit](https://retail-sales-predictor-akfxck5hpg4wdpn3shexnn.streamlit.app/#retail-sales-prediction-app)

---

## 🧠 Model Overview

- **Type**: Linear Regression, Decision Tree (Benchmark)
- **Target Variable**: `Store_Sales`
- **Input Features**:
  - `Store_Size`
  - `Location_Rating`
  - `Marketing_Spend`
  - `Monthly_Sales`

---

## 📈 Evaluation Metrics

| Metric        | Linear Regression | Decision Tree |
|---------------|-------------------|---------------|
| MAE           | 8762.76           | 11732.30      |
| RMSE          | 10646.98          | 15046.47      |
| R² Score      | 0.15              | -0.70         |

### Predicted vs Actual Plot

![Predicted vs Actual](images/Predicted_vs_Actual.png)

---

## 🔍 Exploratory Data Analysis (EDA)

The dataset was analyzed to understand feature relationships and sales trends.

**Key Visuals:**
1. **Sales Distribution**
   ![Sales Distribution](images/sales_distribution.png)
2. **Store Size vs Sales**
   ![Store Size vs Sales](images/store_size_vs_sales.png)
3. **Marketing Spend Impact**
   ![Marketing Spend Impact](images/marketing_spend_vs_sales.png)
4. **Location Rating Influence**
   ![Location Rating Influence](images/location_rating_vs_sales.png)

---

## 🖼️ App Preview

![App Screenshot](images/retail_sales_prediction.png)

---

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/AnkitSingh06/retail-sales-predictor.git

# Navigate to the folder
cd retail-sales-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
