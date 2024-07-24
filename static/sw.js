const CACHE_NAME = 'flask-pwa-cache';
const urlsToCache = [
    '/',
    '/manifest.json',
    '/icon-192x192.png',
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
           .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.open(CACHE_NAME)
           .then(cache => {
                return cache.match(event.request)
                   .then(response => {
                        return response || fetch(event.request);
                    })
            })
    );
});