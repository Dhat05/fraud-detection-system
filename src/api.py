
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Fraud Detection API is running",
        "developer": "Spark"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
@app.get("/check/{amount}")
def check_fraud(amount: int):
    if amount > 50000:
        return {"amount": amount, "risk": "HIGH"}

    return {"amount": amount, "risk": "LOW"}
