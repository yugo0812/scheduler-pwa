# backend/app.py
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from datetime import datetime, timedelta
+ from .your_scheduler import schedule_reviews as next_reviews, send_push


app = FastAPI()

class Item(BaseModel):
    title: str
    last_review: str          # ISO8601
    interval: int             # days already waited

@app.post("/api/review")
def review(items: list[Item]):
    """次の復習タイミングを計算して返す"""
    return [next_reviews(i) for i in items]

@app.post("/api/subscribe")
def subscribe(sub: dict, tasks: BackgroundTasks):
    """ブラウザの Push 購読情報を登録 & 即時テスト送信"""
    tasks.add_task(send_push, sub, "登録ありがとう！")
    return {"status": "ok"}
