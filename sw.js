const CACHE_NAME = 'pipe-counter-cache-v1';
const urlsToCache = [
  '/',
  '/static/styles.css',
  '/static/script.js',
  '/static/LnT.png',
  '/manifest.json',
  '/sw.js'
];
self.addEventListener('install', function(event) {
  console.log('[Service Worker] Installing Service Worker ...', event);
});

self.addEventListener('activate', function(event) {
  console.log('[Service Worker] Activating Service Worker ...', event);
});

self.addEventListener('fetch', function(event) {
  console.log('[Service Worker] Fetching something ...', event);
});