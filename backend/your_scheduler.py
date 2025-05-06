from datetime import datetime, date, timedelta
from typing import List, Dict, Any

# ────────────────────────────────────────────────
# 外部 API
# ────────────────────────────────────────────────
def schedule_reviews(history: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    フロントまたは DB から受け取った履歴を走査し、
    今日復習すべきアイテムを返します。
    """
    today = date.today()
    due_items: List[Dict[str, Any]] = []

    for item in history:
        next_date = _next_review_date(item)
        if next_date <= today:
            # フロント側で表示しやすいよう文字列に変換
            due_items.append({**item, "due": next_date.isoformat()})

    return {"today": today.isoformat(), "due_items": due_items}


# ────────────────────────────────────────────────
# 内部計算ロジック
# ────────────────────────────────────────────────
def _next_review_date(item: Dict[str, Any]) -> date:
    """
    送ってもらった既存スクリプトをほぼそのまま関数化。
    last_review: "YYYY-MM-DD"
    interval: 次回までの間隔（デフォルト 1 日）
    """
    last = datetime.fromisoformat(item["last_review"]).date()
    interval = int(item.get("interval", 1))
    return last + timedelta(days=interval)
