# backend/main.py
from fastapi import FastAPI
from your_scheduler import schedule_reviews

app = FastAPI()

@app.post("/api/review")
async def api_review(history: list[dict]):
    return schedule_reviews(history)
