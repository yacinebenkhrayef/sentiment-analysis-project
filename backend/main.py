# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import os

app = FastAPI(title="Sentiment API V0")

# Autoriser le front (port Vite / CRA)
origins = [
    "http://localhost:5173",  # Vite
    "http://localhost:3000",  # CRA
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "models/baseline.joblib"

class TextIn(BaseModel):
    text: str

# Try load model if present
model = None
tfidf = None
if os.path.exists(MODEL_PATH):
    try:
        saved = joblib.load(MODEL_PATH)
        tfidf = saved.get("tfidf")
        model = saved.get("model")
        print("Model loaded.")
    except Exception as e:
        print("Error loading model:", e)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: TextIn):
    text = data.text or ""
    # If model available use it
    if model is not None and tfidf is not None:
        X = tfidf.transform([text])
        pred = model.predict(X)[0]
        # Map numeric -> label if needed
        return {"sentiment": str(pred)}
    # Fallback rule-based simple
    t = text.lower()
    if any(w in t for w in ["love", "happy", "great", "good", "excellent"]):
        return {"sentiment": "positif"}
    if any(w in t for w in ["hate", "sad", "bad", "terrible", "awful"]):
        return {"sentiment": "negatif"}
    return {"sentiment": "neutre"}
