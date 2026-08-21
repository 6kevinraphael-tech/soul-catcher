# Verse Keepers — Gmail login setup

The app uses the same Firebase project as United to Serve. Do this once so Kevin and Rachel can sign in with Gmail.

## 1. Enable Google sign-in

1. Open [Firebase Console](https://console.firebase.google.com) → project **united-to-serve-prayer**
2. **Build → Authentication → Get started** (if needed)
3. **Sign-in method → Google → Enable → Save**
4. **Authentication → Settings → Authorized domains**
   - Add `localhost`
   - Add `6kevinraphael-tech.github.io` (for GitHub Pages)

## 2. Firestore rules

**Firestore Database → Rules** — merge so prayer chains still work and Verse Keepers accounts are protected:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /prayerChains/{groupId} {
      allow read, write: if true;
    }

    match /verseKeepersUsers/{uid} {
      allow read: if request.auth != null;
      allow create, update: if request.auth != null && request.auth.uid == uid;
      allow delete: if request.auth != null && request.auth.uid == uid;
    }

    match /verseKeepersEmails/{emailId} {
      allow read: if request.auth != null;
      allow write: if request.auth != null
        && request.resource.data.uid == request.auth.uid;
    }
  }
}
```

Click **Publish**.

## 3. Play

Open `verse-keepers.html` (or the live Pages URL), tap **Continue with Google**, then create your account with a display name. Link your sister’s Gmail under **Practice partner** so week scores show side by side.
