# Mini-Lesson 12.2: MongoDB: A Document Database

## Overview

MongoDB is a popular NoSQL database that stores data as documents instead of rows and columns. Unlike relational databases such as MySQL, MongoDB does not require a fixed schema and stores data using a JSON-like format called BSON.

MongoDB is designed to support:

- Flexible data models
- High-performance reads
- Horizontal scalability
- Fault tolerance
- Distributed storage

---

## What Is MongoDB?

MongoDB is a document-oriented NoSQL database.

Unlike relational databases that organize data into tables, MongoDB organizes data into:

```text
Database
    ↓
Collection
    ↓
Document
```

### Relational Database Equivalent

| Relational Database | MongoDB |
|---------------------|----------|
| Database | Database |
| Table | Collection |
| Record | Document |
| Row | Document |
| Column | Field |

---

## Documents

The fundamental unit of storage in MongoDB is a document.

Example:

```json
{
    "name": "John",
    "address": "Highway 37"
}
```

Documents are stored in BSON format.

### BSON

BSON stands for:

```text
Binary JSON
```

BSON:

- Supports JSON structures
- Adds binary data support
- Supports additional data types
- Improves storage efficiency

---

## Collections

A collection is a group of related documents.

Relational example:

```text
customers table
```

MongoDB equivalent:

```text
customers collection
```

Example:

```json
{
    "name": "John"
}
```

```json
{
    "name": "Mary"
}
```

Both documents belong to the same collection.

---

## Advantages of MongoDB

### Flexible Schema

Documents do not have to share the exact same structure.

Example:

```json
{
    "name": "John"
}
```

```json
{
    "name": "Mary",
    "address": "Highway 37"
}
```

Both documents can exist in the same collection.

---

### Fast Reads

MongoDB stores related information together.

Because data is stored within documents:

- Fewer joins are required
- Read performance is often faster

---

### Distributed Architecture

MongoDB can distribute data across multiple servers.

Benefits:

- High availability
- Fault tolerance
- Scalability

If one server fails, redundant copies on other servers remain available.

---

## Installing PyMongo

PyMongo is the official Python driver for MongoDB.

Install:

```bash
pip install pymongo
```

or

```bash
pip3 install pymongo
```

Import:

```python
import pymongo
```

---

## Connecting to MongoDB

Create a client connection:

```python
import pymongo

myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/"
)
```

### Connection String

```text
mongodb://localhost:27017/
```

Components:

- Protocol: mongodb
- Host: localhost
- Port: 27017

---

## Creating a Database

Create a database reference:

```python
mydb = myclient["mydatabase"]
```

Example:

```python
import pymongo

myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/"
)

mydb = myclient["mydatabase"]
```

MongoDB creates the database automatically when data is inserted.

---

## Listing Databases

Display available databases:

```python
print(myclient.list_database_names())
```

Example output:

```python
['admin', 'config', 'local', 'mydatabase']
```

---

## Creating a Collection

Create a collection reference:

```python
mycol = mydb["customers"]
```

Example:

```python
myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/"
)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]
```

---

## Listing Collections

Display collections:

```python
print(mydb.list_collection_names())
```

Example output:

```python
['customers']
```

---

## Inserting One Document

MongoDB stores documents using Python dictionaries.

Example:

```python
mydict = {
    "name": "John",
    "address": "Highway 37"
}

x = mycol.insert_one(mydict)
```

Document inserted:

```json
{
    "name": "John",
    "address": "Highway 37"
}
```

---

## Inserting Multiple Documents

Use:

```python
insert_many()
```

Example:

```python
mylist = [
    {
        "name": "Amy",
        "address": "Apple st 652"
    },
    {
        "name": "Hannah",
        "address": "Mountain 21"
    },
    {
        "name": "Michael",
        "address": "Valley 345"
    }
]

x = mycol.insert_many(mylist)
```

Display inserted IDs:

```python
print(x.inserted_ids)
```

---

## Module 12 Video Example

The MongoDB sandbox created from Video 12.7 uses:

### Database

```text
pluto
```

### Collection

```text
posts
```

### Connection

```python
client = MongoClient(
    "mongodb://localhost:27017"
)
```

### Example Document

```json
{
    "id": "3f014562-214f-4cc3-b354-8c1cf945d08b",
    "stamp": "2026-08-14 09:03:32"
}
```

### Insert Document

```python
db.posts.insert_one(item)
```

### Read Documents

```python
for doc in db.posts.find():
    print(doc)
```

---

## MongoDB and Docker

MongoDB is commonly run inside a Docker container.

Pull image:

```bash
docker pull mongo
```

Run container:

```bash
docker run --name mongodb \
-p 27017:27017 \
-d mongo
```

Verify:

```bash
docker ps
```

Expected output:

```text
mongodb
0.0.0.0:27017->27017/tcp
```

---

## MongoDB VS Code Extension

MongoDB can be managed directly from VS Code.

Connection string:

```text
mongodb://localhost:27017
```

After connecting:

```text
localhost:27017
├── admin
├── config
├── local
└── pluto
    └── posts
```

---

## MongoDB vs MySQL

| Feature | MySQL | MongoDB |
|----------|---------|---------|
| Database Type | Relational | Document |
| Storage Structure | Tables | Collections |
| Records | Rows | Documents |
| Schema | Fixed | Flexible |
| Query Language | SQL | MongoDB Query Language |
| Scaling | Vertical | Horizontal |
| Joins | Common | Less Common |

---

## Key Terms

### NoSQL

Databases that do not use the traditional relational model.

### Document

A JSON-like record stored in MongoDB.

### Collection

A group of related documents.

### BSON

Binary representation of JSON.

### MongoClient

The Python connection object used to communicate with MongoDB.

### PyMongo

Official Python driver for MongoDB.

---

## Key Takeaways

- MongoDB is a NoSQL document database.
- Documents are stored in BSON format.
- Collections are equivalent to relational tables.
- Documents are equivalent to records.
- MongoDB does not require a fixed schema.
- PyMongo enables Python applications to interact with MongoDB.
- MongoDB supports distributed storage and horizontal scaling.
- MongoDB is commonly deployed in Docker containers.
- VS Code and Studio 3T can be used to browse MongoDB databases visually.

### Quick Reference

```text
Database
    ↓
Collection
    ↓
Document
```

Common Operations:

```python
insert_one()
insert_many()
find()
list_database_names()
list_collection_names()
```

Module Example:

```text
Database: pluto
Collection: posts
```