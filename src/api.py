from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("fraud_model.pkl")

@app.get("/")
def home():
    return {"message": "AI Fraud Detection API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/predict/{amount}")
def predict(amount: int):
    prediction = model.predict([[amount]])[0]

    return {
        "amount": amount,
        "fraud": bool(prediction)
    }
