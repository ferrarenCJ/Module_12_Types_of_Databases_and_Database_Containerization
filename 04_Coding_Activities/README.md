# Coding Activity 12.2: Modify a Document Database in a Container

## Objective

The objective of this activity is to learn how to perform CRUD (Create, Read, Update, and Delete) operations on a MongoDB document database running inside a Docker container. The activity demonstrates how to connect Python to MongoDB using PyMongo, create and query collections, update documents, and delete documents.

---

## Learning Outcome

**Update and delete data in different types of containerized databases.**

---

## Technologies Used

- Python
- MongoDB
- PyMongo
- Docker
- Visual Studio Code
- MongoDB VS Code Extension

---

## Environment Setup

### Install PyMongo

```bash
pip install pymongo
```

### Create MongoDB Container

```bash
docker run -p 27017:27017 --name mongodb -d mongo
```

Verify container status:

```bash
docker ps
```

Expected output:

```text
mongodb
0.0.0.0:27017->27017/tcp
```

### MongoDB Connection String

```text
mongodb://localhost:27017
```

---

## Database Design

### Database

```text
EmployeeDB
```

### Collection

```text
employees
```

### Employee Documents

```json
{
    "FirstName": "John",
    "LastName": "Smith",
    "Age": 25
}
```

```json
{
    "FirstName": "Peter",
    "LastName": "Smith",
    "Age": 26
}
```

```json
{
    "FirstName": "Gabriel",
    "LastName": "Smith",
    "Age": 28
}
```

```json
{
   