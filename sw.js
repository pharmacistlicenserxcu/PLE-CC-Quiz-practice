const CACHE_NAME = 'ple-cc-quiz-practice-v81';
const ASSETS = [
  './',
  './index.html',
  './quiz-data-offline.js',
  './manifest.json'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).catch((err) => {
      console.warn('[SW] Cache addAll warning:', err);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Network-First for HTML and JS to ensure fresh Google Sheet data
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  const isCodeOrData = url.pathname.endsWith('.html') || url.pathname.endsWith('.js') || url.pathname.endsWith('/') || url.pathname.endsWith('.json');

  if (isCodeOrData) {
    e.respondWith(
      fetch(e.request)
        .then((networkRes) => {
          if (networkRes && networkRes.status === 200) {
            try {
              const resClone = networkRes.clone();
              caches.open(CACHE_NAME).then((cache) => cache.put(e.request, resClone).catch(() => {}));
            } catch (_) {}
          }
          return networkRes;
        })
        .catch(() => caches.match(e.request, { ignoreSearch: true }))
    );
  } else {
    // Cache-First for static assets/images
    e.respondWith(
      caches.match(e.request, { ignoreSearch: true }).then((res) => {
        return res || fetch(e.request);
      })
    );
  }
});
