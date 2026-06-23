# Firebase setup (5 minutes — you do this once in your browser)

The app is already online. Follow these steps to **sync prayers across all phones**.

## Step 1 — Create project

1. Open **https://console.firebase.google.com**
2. Sign in with Google
3. Click **Add project**
4. Name: `united-to-serve-prayer` → Continue → Create project

## Step 2 — Turn on Firestore

1. Left menu: **Build → Firestore Database**
2. **Create database**
3. Choose **Start in test mode** → Next
4. Pick a region (e.g. `us-west1`) → **Enable**

## Step 3 — Copy your web app keys

1. Click the **gear icon** → **Project settings**
2. Scroll to **Your apps** → click the **Web** icon `</>`
3. Nickname: `Prayer Chain` → **Register app**
4. You’ll see something like:

```javascript
const firebaseConfig = {
  apiKey: "AIza...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  ...
};
```

5. Copy those values into `firebase-config.js` in this folder (or send them to Kevin to paste in)

## Step 4 — Security rules

1. **Firestore Database → Rules**
2. Replace everything with:

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

3. Click **Publish**

## Step 5 — Push updated config (if you edited locally)

After saving `firebase-config.js` with your real keys, commit and push to GitHub — or edit the file on github.com directly.

## Done

Open your prayer chain link. The badge should say **Live — synced with group**.

**Live link:**
https://6kevinraphael-tech.github.io/soul-catcher/united-to-serve/?group=united-to-serve
