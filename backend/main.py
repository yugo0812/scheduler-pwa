# backend/main.py
from fastapi import FastAPI
from typing import List, Dict            # ← こちらを使う

from .your_scheduler import schedule_reviews

app = FastAPI()

@app.post("/api/review")
async def api_review(history: List[Dict]):   # ← List[Dict] に変更
    return schedule_reviews(history)
