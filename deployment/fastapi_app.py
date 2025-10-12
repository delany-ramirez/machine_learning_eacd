from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="HELOC Risk Scoring API")

MODEL_PATH = Path("models/model.joblib")
SCALER_PATH = Path("models/scaler.joblib")

class HelocInput(BaseModel):
    # Define aquí un subconjunto de features del HELOC
    ExternalRiskEstimate: float | None = None
    MSinceOldestTradeOpen: float | None = None
    MSinceMostRecentTradeOpen: float | None = None
    NumSatisfactoryTrades: float | None = None
    NumTrades60Ever2DerogPubRec: float | None = None
    NumTrades90Ever2DerogPubRec: float | None = None
    PercentTradesNeverDelq: float | None = None
    MaxDelq2PublicRecLast12M: float | None = None
    MaxDelqEver: float | None = None

@app.on_event("startup")
def load_artifacts():
    global model, scaler
    model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None
    scaler = joblib.load(SCALER_PATH) if SCALER_PATH.exists() else None

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": MODEL_PATH.exists()}

@app.post("/predict")
def predict(payload: HelocInput):
    if MODEL_PATH.exists() is False:
        return {"error": "Model not found. Train and export to models/model.joblib"}
    df = pd.DataFrame([payload.dict()])
    if scaler is not None:
        df = scaler.transform(df)
    yhat = model.predict_proba(df)[:,1] if hasattr(model, "predict_proba") else model.predict(df)
    return {"score": float(yhat[0])}
