self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('v1').then(c =>
      c.addAll(['/', '/index.html', '/app.js', '/offline.html'])
    )
  );
});
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
      .catch(() => caches.match('/offline.html'))
  );
});
self.addEventListener('push', e => {
  const data = e.data?.json() || {};
  e.waitUntil(
    self.registration.showNotification(data.title || '復習ですよ', {
      body: data.body || 'そろそろ次のカードを開きましょう。',
      icon: '/icons/icon-192.png',
    })
  );
});
