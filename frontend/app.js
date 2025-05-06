// Service Worker を登録
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}

// バックエンド API のベース URL
const API = 'https://scheduler-api.onrender.com';

// 復習データを取りに行く関数
async function fetchReviews() {
  const items = JSON.parse(localStorage.getItem('schedule') || '[]');

  const res = await fetch(`${API}/api/review`, {      // ← ここを絶対 URL に
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(items),
  });

  const data = await res.json();
  render(data);
}

// ページ読み込み時に呼び出す例
window.addEventListener('DOMContentLoaded', fetchReviews);
