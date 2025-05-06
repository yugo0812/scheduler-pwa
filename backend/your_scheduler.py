from datetime import datetime, timedelta

# item = {"title": str, "last_review": "YYYY-MM-DD", "interval": int}
def next_reviews(item: dict) -> dict:
    last = datetime.fromisoformat(item["last_review"])
    interval = item.get("interval", 1)
    next_date = last + timedelta(days=interval)
    return {
        "title": item["title"],
        "next_review": next_date.date().isoformat()
    }

# Push 通知のダミー
def send_push(subscription: dict, message: str):
    # 実装するまでは何もしない
    return
