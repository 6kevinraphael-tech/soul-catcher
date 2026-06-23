# United to Serve — Prayer Chain

A simple shared prayer chain for your group:

- **Left side:** add and remove prayer requests  
- **Right side:** week chart (Mon–Sun) — tap ☆ to mark ★ when you prayed  
- **Same link on every device** — changes sync for the whole group (with Firebase)

## Try it locally

```bash
cd united-to-serve
python3 -m http.server 8766
```

Open http://localhost:8766/

---

## Share with your prayer group

Send everyone the **same link**, for example:

```
https://YOUR-SITE.com/united-to-serve/?group=our-prayer-group
```

The `group=` name keeps your list private from other groups. Use one name for your whole church/prayer group (e.g. `group=st-marys-chain`).

---

## Sync across phones & computers (Firebase — free)

Without Firebase, the app works on **one device only** (saved in the browser).  
To sync for everyone, set up Firebase once (~5 minutes):

### 1. Create a Firebase project

1. Go to [console.firebase.google.com](https://console.firebase.google.com)
2. **Add project** → name it (e.g. `united-to-serve-prayer`)
3. Disable Google Analytics if you want (optional)

### 2. Create a Firestore database

1. In the left menu: **Build → Firestore Database**
2. **Create database** → **Start in test mode** (for a small trusted prayer group)
3. Pick a region close to you → **Enable**

### 3. Register a web app

1. Project **Settings** (gear icon) → **General**
2. Under **Your apps**, click **Web** `</>`
3. App nickname: `Prayer Chain` → **Register app**
4. Copy the `firebaseConfig` values

### 4. Paste config into this project

Open `firebase-config.js` and replace the placeholder values:

```javascript
window.FIREBASE_CONFIG = {
  apiKey: '...',
  authDomain: '...',
  projectId: '...',
  storageBucket: '...',
  messagingSenderId: '...',
  appId: '...',
};
```

### 5. Firestore security rules (important)

In Firebase → **Firestore → Rules**, paste:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /prayerChains/{groupId} {
      allow read, write: if true;
    }
  }
}
```

Click **Publish**.

> For a small private prayer group this is fine. For public internet exposure, add a shared group password later.

### 6. Deploy the folder

Upload the `united-to-serve` folder to:

- **GitHub Pages** (subfolder on your site)
- **Netlify / Vercel** (drag & drop)
- **itch.io** (zip `index.html`, `firebase-config.js`)

After deploy, open the site — the top badge should say **Live — synced with group**.

---

## How to use

1. Open the link on your phone or computer  
2. **Add** a prayer request (name, need, situation)  
3. Tap **☆** on the days you pray — your ★ shows only for you; everyone else sees counts only (anonymous)  
4. Each request shows **“X people prayed”** — no names are shared  
5. **All prayer marks reset every Monday at midnight Pacific Time**  
6. **Copy link** and send to your prayer group  

Made by Kevin Raphael.

---

## Files

| File | Purpose |
|------|---------|
| `index.html` | The app |
| `firebase-config.js` | Your Firebase keys (for sync) |
| `firebase-config.example.js` | Template |
