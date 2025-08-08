
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv(r'C:\Users\Ankit Kumar Singh\Downloads\retail_sales_prediction_deployable\retail_sales_data.csv')
X = df[["Store_Size", "Location_Rating", "Marketing_Spend"]]
y = df["Monthly_Sales"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "lr_model.pkl")
print("Model saved as lr_model.pkl")
