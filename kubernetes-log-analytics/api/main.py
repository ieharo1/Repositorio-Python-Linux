import json
import os
from fastapi import FastAPI, HTTPException

RESULT_PATH = os.getenv("RESULT_PATH", "/data/results/summary.json")

app = FastAPI(title="Log Analytics API", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/results")
def results():
    if not os.path.exists(RESULT_PATH):
        raise HTTPException(status_code=404, detail="Resultados no generados")
    with open(RESULT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

