# backend/notifications.py
from pywebpush import webpush, WebPushException
import json, os, logging

VAPID_PRIVATE_KEY = os.environ["VAPID_PRIVATE_KEY"]
VAPID_CLAIMS = {"sub": "mailto:your‑address@example.com"}

def send_push(subscription: dict, payload: dict) -> None:
    """
    subscription: Service Worker 側で取得した JSON をそのまま dict 化したもの
    payload: {"title": "...", "body": "..."} など
    """
    try:
        webpush(
            subscription_info=subscription,
            data=json.dumps(payload),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS,
        )
    except WebPushException as exc:
        logging.warning(f"Push failed: {exc}")
