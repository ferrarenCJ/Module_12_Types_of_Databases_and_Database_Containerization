# Coding Activity 12.5: Modify a Serverless Cloud Database

## Objective

The purpose of this activity is to create a serverless cloud database using Google Firebase, connect to it using Python, and write data to a Firebase Realtime Database using the Firebase Admin SDK.

---

## Learning Outcome

**Update and delete data in different types of containerized and cloud-hosted databases.**

---

## Technologies Used

- Google Firebase
- Firebase Realtime Database
- Firebase Admin SDK
- Python 3
- Visual Studio Code

---

## Project Information

### Firebase Project

```text
Activity12-5
```

### Database Type

```text
Firebase Realtime Database
```

### Architecture

```text
Python Application
        ↓
Firebase Admin SDK
        ↓
Firebase API
        ↓
Realtime Database
```

---

## Folder Structure

```text
CA_12_5_Serverless_Cloud_Database
│
├── fire.py
├── serviceAccountKey.json
├── README.md
└── Screenshots
```

> Note: `serviceAccountKey.json` should never be committed to GitHub.

---

## Firebase Setup

### Create Project

Navigate to:

```text
https://console.firebase.google.com
```

Create a project named:

```text
Activity12-5
```

---

## Generate Service Account Credentials

Navigate to:

```text
Project Settings
    ↓
Service Accounts
```

Generate a new private key.

Save the downloaded file as:

```text
serviceAccountKey.json
```

Place it in the same folder as:

```text
fire.py
```

---

## Create Realtime Database

Navigate to:

```text
Build
    ↓
Realtime Database
```

