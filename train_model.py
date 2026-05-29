import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample training data
data = {
    "amount": [100, 500, 1000, 5000, 10000, 50000, 75000, 100000],
    "fraud":  [0,   0,   0,    0,    0,     1,     1,      1]
}

df = pd.DataFrame(data)

X = df[["amount"]]
y = df["fraud"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "fraud_model.pkl")

print("Model trained and saved as fraud_model.pkl")
