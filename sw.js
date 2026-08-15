self.addEventListener("install", (e) => self.skipWaiting());
self.addEventListener("activate", (e) => e.waitUntil(self.clients.claim()));

self.addEventListener("message", (e) => {
  if (e.data?.type !== "schedule-reminder") return;
  const when = e.data.when;
  const delay = when - Date.now();
  if (delay <= 0 || delay > 86400000) return;

  const title = e.data.title || "Time to practice math! 🎮";
  const body = e.data.body || "Grab 15 minutes and play Multiply Quest!";
  const tag = e.data.tag || "mq-practice";
  const icon =
    e.data.icon ||
    "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🦄</text></svg>";
  const url = e.data.url || "./multiplication-quest.html";

  setTimeout(() => {
    self.registration.showNotification(title, {
      body,
      icon,
      tag,
      requireInteraction: true,
      data: { url }
    });
  }, delay);
});

self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const target = e.notification.data?.url || "./";
  e.waitUntil(
    self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if ("focus" in client && client.url.includes(target.replace("./", ""))) {
          return client.focus();
        }
      }
      if (self.clients.openWindow) return self.clients.openWindow(target);
    })
  );
});
