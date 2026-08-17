# Coding Activity 12.5: Modify a Serverless Cloud Database

## Objective

Create and configure a Firebase Realtime Database, connect to it using Python, and write data to a Firebase serverless cloud database using the Firebase Admin SDK.

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

## Folder Structure

```text
CA_12_5_Serverless_Cloud_Database_Container
│
├── Documentation
│   ├── Activity 12.5_Modify a Serverless Cloud Database.docx
│   └── Supporting screenshots and submission materials
│
├── Solution_Files
│   └── fire.py
│
├── Source_Files
│   ├── fire.py
│   └── README.md
│
└── README.md
```

---

## Folder Descriptions

### Documentation

Contains the final assignment submission and supporting deliverables.

Examples:

- Word document submitted to Canvas
- Assignment screenshots
- Supporting documentation

---

### Source_Files

Contains the original working files used during development.

Files:

```text
fire.py
README.md
```

---

### Solution_Files

Contains the finalized solution files for the activity.

Files:

```text
fire.py
```

---

## Firebase Project

Project Name:

```text
Activity12-5
```

Database Type:

```text
Firebase Realtime Database
```

---

## Python Package Installation

Install the Firebase Admin SDK:

```bash
pip install firebase-admin
```

Verify installation:

```bash
pip show firebase-admin
```

---

## Source Code Overview

The Python script performs the following tasks:

1. Authenticates with Firebase using a service account.
2. Connects to a Firebase Realtime Database.
3. Writes custom JSON data to the database.
4. Verifies successful communication with Firebase.

---

## Security Note

The Firebase service account key should never be committed to GitHub.

Add the following to `.gitignore`:

```gitignore
serviceAccountKey.json
*-firebase-adminsdk-*.json
```

---

## Key Takeaways

- Firebase is a serverless cloud database platform.
- Firebase Realtime Database stores information as JSON.
- Python applications can interact with Firebase using the Firebase Admin SDK.
- Serverless services remove the need to manage servers and infrastructure.
- Google automatically handles scaling, availability, and maintenance.

---

## Conclusion

This activity demonstrated how to create a Firebase project, configure a Realtime Database