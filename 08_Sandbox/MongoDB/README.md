# MongoDB Sandbox
## Module 12: Types of Databases and Database Containerization

This sandbox contains practice exercises, test scripts, notes, and experiments related to MongoDB concepts covered in Module 12.

MongoDB was introduced as a NoSQL, document-oriented database that stores data in flexible JSON-like documents rather than traditional relational tables.

---

# Purpose

The MongoDB sandbox was used to:

- Practice MongoDB commands
- Explore document-oriented database concepts
- Create and query collections
- Insert and retrieve documents
- Test MongoDB Docker containers
- Compare MongoDB with relational databases

---

# MongoDB Overview

MongoDB is a NoSQL database designed to store information as documents organized into collections.

### Key Concepts

#### Database

Container that holds collections.

#### Collection

Equivalent to a table in a relational database.

#### Document

Equivalent to a row or record in a relational database.

Example document:

```json
{
    "employee_id": 101,
    "name": "John Smith",
    "department": "Engineering"
}
```

---

# MongoDB Architecture

```text
Database
│
├── Collection
│   ├── Document
│   ├── Document
│   └── Document
│
└── Collection
    ├── Document
    └── Document
```

---

# Common MongoDB Commands

## Show Databases

```javascript
show dbs
```

---

## Create or Use a Database

```javascript
use company
```

---

## Show Collections

```javascript
show collections
```

---

## Create Collection

```javascript
db.createCollection("employees")
```

---

## Insert a Document

```javascript
db.employees.insertOne({
    employee_id: 101,
    name: "John Smith",
    department: "Engineering"
})
```

---

## Insert Multiple Documents

```javascript
db.employees.insertMany([
{
    employee_id: 101,
    name: "John Smith"
},
{
    employee_id: 102,
    name: "Jane Doe"
}
])
```

---

## Query Documents

```javascript
db.employees.find()
```

---

## Query Specific Document

```javascript
db.employees.find({
    employee_id: 101
})
```

---

## Update Document

```javascript
db.employees.updateOne(
    { employee_id: 101 },
    {
        $set: {
            department: "Operations"
        }
    }
)
```

---

## Delete Document

```javascript
db.employees.deleteOne(
    { employee_id: 101 }
)
```

---

# Docker Commands

## Pull MongoDB Image

```bash
docker pull mongo
```

---

## Create MongoDB Container

```bash
docker run -d \
--name mongodb-sandbox \
-p 27017:27017 \
mongo
```

---

## Verify Container

```bash
docker ps
```

---

## Access Mongo Shell

```bash
docker exec -it mongodb-sandbox mongosh
```

---

# Example Sandbox Dataset

## Employees Collection

```json
{
    "employee_id": 101,
    "name": "John Smith",
    "department": "Engineering"
}
```

```json
{
    "employee_id": 102,
    "name": "Jane Doe",
    "department": "Operations"
}
```

---

# Relational vs MongoDB

## Relational Database

```text
Table: Employees

employee_id | name       | department
------------|------------|------------
101         | John Smith | Engineering
```

---

## MongoDB

```json
{
    "employee_id": 101,
    "name": "John Smith",
    "department": "Engineering"
}
```

---

# Learning Outcomes

Through this sandbox, the following concepts were practiced:

✅ Document-oriented databases

✅ Collections and documents

✅ NoSQL architecture

✅ MongoDB CRUD operations

✅ MongoDB Docker deployment

✅ JSON document storage

✅ Querying and updating documents

---

# Useful References

## MongoDB Documentation

```text
https://www.mongodb.com/docs/
```

## MongoDB Manual

```text
https://www.mongodb.com/docs/manual/
```

## MongoDB Docker Image

```text
https://hub.docker.com/_/mongo
```

---

# Key Takeaways

- MongoDB stores data as documents instead of rows and columns.
- Collections are equivalent to relational database tables.
- Documents use JSON-like structures.
- MongoDB provides flexible schemas compared to relational databases.
- Docker makes it easy to deploy and test MongoDB environments.
- MongoDB is well suited for applications with evolving data structures and large volumes of semi-structured information.

---

## Sandbox Summary

```text
MongoDB
    ↓
Document-Oriented Database

Collection
    ↓
Table Equivalent

Document
    ↓
Row Equivalent

JSON
    ↓
Flexible Data Structure
```

The MongoDB sandbox provided a safe environment for experimenting with NoSQL concepts and understanding how document-oriented databases differ from traditional relational database systems.