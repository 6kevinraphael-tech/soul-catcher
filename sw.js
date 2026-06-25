self.addEventListener("install", e => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));

self.addEventListener("message", e => {
  if (e.data?.type !== "schedule-reminder") return;
  const when = e.data.when;
  const delay = when - Date.now();
  if (delay <= 0 || delay > 86400000) return;
  setTimeout(() => {
    self.registration.showNotification("Time to practice math! 🎮", {
      body: "Grab 15 minutes and play Multiply Quest!",
      icon: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🦄</text></svg>",
      tag: "mq-practice",
      requireInteraction: true
    });
  }, delay);
});
