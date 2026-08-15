# Knowledge Check 12.3: Serverless Cloud Databases

## Overview

This knowledge check focused on serverless cloud databases, Firebase, and the differences between serverless and managed cloud services.

**Score:** 6/6 Correct

---

# Question 1

## What are serverless services?

### Correct Answer

✅ Serverless services are a cloud offering where developers can build and run applications without managing the underlying infrastructure.

### Explanation

Serverless services allow developers to focus on application development while the cloud provider manages:

- Servers
- Operating systems
- Scaling
- Maintenance
- Infrastructure

---

# Question 2

## What is Firebase?

### Correct Answer

✅ Firebase is a cloud-based database.

### Explanation

Firebase is Google's serverless cloud platform that provides database services including:

- Realtime Database
- Cloud Firestore

Firebase allows applications to store and retrieve data without managing servers.

---

# Question 3

## What is the difference between serverless and managed cloud services?

### Correct Answer

✅ In managed cloud services, you can manually configure the servers. In serverless services, you can just use the servers without the possibility of configuring them.

### Explanation

| Managed Cloud | Serverless |
|---------------|------------|
| Server configuration available | No server configuration |
| More infrastructure control | Infrastructure hidden |
| User manages some settings | Provider manages everything |

---

# Question 4

## Firebase is an example of which kind of service?

### Correct Answer

✅ Serverless service

### Explanation

Firebase is a serverless platform because developers interact with services and APIs while Google manages the underlying infrastructure.

---

# Question 5

## Which command can be used to install the Firebase libraries for Python?

### Correct Answer

✅ `pip3 install firebase_admin`

### Explanation

Install the Firebase Admin SDK:

```bash
pip3 install firebase_admin
```

This library enables Python applications to connect to Firebase services.

---

# Question 6

## Firebase was developed by which organization?

### Correct Answer

✅ Google

### Explanation

Firebase was acquired by Google in 2014 and is now integrated into the Google Cloud ecosystem.

---

# Firebase Summary

## What Is Firebase?

Firebase is a serverless cloud platform that provides:

- Realtime Database
- Cloud Firestore
- Authentication
- Hosting
- Analytics
- Cloud Functions

---

## Serverless Architecture

Traditional:

```text
Application
    ↓
Server
    ↓
Database
```

Serverless:

```text
Application
    ↓
API
    ↓
Firebase
```

Google manages:

- Servers
- Updates
- Scaling
- Security
- Availability

---

## Firebase Workflow

```text
Create Project
      ↓
Create Database
      ↓
Generate Service Account Key
      ↓
Install SDK
      ↓
Connect Python
      ↓
Read / Write Data
```

---

## Important Command

Install Firebase SDK:

```bash
pip3 install firebase_admin
```

---

## Key Terms

### Serverless

Cloud service where infrastructure is managed by the provider.

### Firebase

Google's serverless application development platform.

### Realtime Database

JSON-based cloud-hosted database.

### Cloud Firestore

Document-oriented cloud database.

### Service Account

Credential used by applications to access Firebase services.

---

# Knowledge Check Results

## Final Score

```text
6 / 6 Correct
```

## Topics Mastered

✅ Serverless Services

✅ Firebase Fundamentals

✅ Managed Cloud vs Serverless

✅ Firebase Architecture

✅ Firebase Installation

✅ Google Cloud Services

---

# Key Takeaways

- Firebase is a serverless cloud database platform.
- Developers do not manage servers or infrastructure.
- Google handles scaling, security, and maintenance.
- Firebase can be accessed using Python and the Firebase Admin SDK.
- Cloud Firestore and Realtime Database are Firebase database offerings.
- Serverless architectures significantly reduce deployment complexity.

## Module Theme

> Serverless cloud databases allow developers to focus on application development while the cloud provider manages infrastructure, scalability, security, and availability.