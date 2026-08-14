# Video 12.7: MongoDB: A Document Database

## Overview

This lesson introduces MongoDB, one of the most popular NoSQL databases. Unlike relational databases that store data in tables, MongoDB stores information in collections of documents. These documents are formatted using JSON-like structures, making MongoDB highly flexible for applications with changing data requirements.

Dr. Sanchez demonstrates:

- MongoDB fundamentals
- Document-oriented data storage
- MongoDB collections
- Running MongoDB inside a Docker container
- Accessing MongoDB from Python
- Reading and writing data to MongoDB

---

## Video Information

**Video 12.7: MongoDB: A Document Database**

**Duration:** 09:24

---

## What Is MongoDB?

MongoDB is a NoSQL document database designed to store and manage semi-structured data.

Instead of organizing data into rows and columns, MongoDB stores data as documents.

### Relational Database Example

```text
Employees Table

| EmployeeID | Name  | Department |
|------------|--------|------------|
| 1001       | Alice | Engineering |
```

### MongoDB Example

```json
{
  "employee_id": 1001,
  "name": "Alice",
  "department": "Engineering"
}
```

Each record is stored as a document.

---

## Documents

A document is the basic unit of data storage in MongoDB.

Documents are stored using BSON (Binary JSON), which is a binary representation of JSON.

Example:

```json
{
  "restaurant_id": 1,
  "name": "Pizza House",
  "city": "Anaheim",
  "rating": 5
}
```

Benefits:

- Human-readable structure
- Flexible format
- Easy application integration

---

## Collections

Collections are groups of related documents.

Relational Database Equivalent:

```text
Table
```

MongoDB Equivalent:

```text
Collection
```

Example:

```text
restaurants
```

Collection:

```json
{
  "restaurant_id": 1,
  "name": "Pizza House"
}
```

```json
{
  "restaurant_id": 2,
  "name": "Taco Corner"
}
```

Both documents belong to the same collection.

---

## Flexible Schema

One of MongoDB's biggest advantages is its flexible schema.

Documents within the same collection do not need identical structures.

Example:

```json
{
  "name": "Pizza House",
  "rating": 5
}
```

```json
{
  "name": "Taco Corner",
  "city": "Anaheim",
  "hours": "9 AM - 9 PM"
}
```

Both documents can coexist in the same collection.

---

## MongoDB Architecture

```text
Database
    ↓
Collection
    ↓
Document
```

Example:

```text
restaurants_db
    ↓
restaurants
    ↓
restaurant documents
```

---

## Running MongoDB in Docker

Similar to MySQL, MongoDB can run inside a Docker container.

### Pull MongoDB Image

```bash
docker pull mongo
```

### Run MongoDB Container

```bash
docker run --name mongodb -d mongo
```

Benefits:

- Easy deployment
- Consistent environments
- Fast setup
- Simplified testing

---

## Accessing MongoDB

Applications connect to MongoDB through drivers.

### Python Driver

MongoDB commonly uses:

```python
pymongo
```

Installation:

```bash
pip install pymongo
```

Import:

```python
from pymongo import MongoClient
```

---

## Connecting to MongoDB with Python

Example:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
```

The client object creates a connection to the database server.

---

## Creating a Database

```python
db = client["restaurants"]
```

MongoDB creates databases automatically when data is inserted.

---

## Creating a Collection

```python
collection = db["restaurants"]
```

Equivalent to creating a table in a relational database.

---

## Inserting Documents

Example:

```python
restaurant = {
    "id": 1,
    "name": "Pizza House"
}

collection.insert_one(restaurant)
```

This inserts a document into the collection.

---

## Reading Documents

Retrieve documents:

```python
for doc in collection.find():
    print(doc)
```

Output:

```json
{
    "id": 1,
    "name": "Pizza House"
}
```

---

## CRUD Operations in MongoDB

### Create

```python
insert_one()
```

### Read

```python
find()
find_one()
```

### Update

```python
update_one()
```

### Delete

```python
delete_one()
```

MongoDB supports the same CRUD concepts found in relational databases, but uses documents instead of rows.

---

## Studio 3T

The lesson introduces **Studio 3T**, a graphical user interface for MongoDB.

Studio 3T allows users to:

- Browse databases
- Browse collections
- View documents
- Execute queries
- Manage MongoDB visually

Advantages:

- User-friendly interface
- Easier document management
- Database visualization

This tool provides functionality similar to what MySQL Workbench provides for MySQL databases.

---

## MongoDB vs MySQL

| Feature | MySQL | MongoDB |
|----------|---------|---------|
| Database Type | Relational | Document |
| Storage | Tables | Documents |
| Schema | Fixed | Flexible |
| Query Language | SQL | MongoDB Query Language |
| Scalability | Vertical | Horizontal |
| Data Format | Rows and Columns | JSON/BSON Documents |

---

## Common MongoDB Use Cases

MongoDB is commonly used for:

### Content Management

- Articles
- Blogs
- Web content

### Product Catalogs

- E-commerce applications
- Inventory management

### User Profiles

- Social media applications
- Customer information systems

### Mobile Applications

- Dynamic application data

### IoT Applications

- Semi-structured sensor data

---

## Advantages of MongoDB

### Flexible Schema

No need to define every field in advance.

### Easy Scaling

Supports horizontal scaling.

### JSON-Based Structure

Matches modern application development patterns.

### Fast Development

Allows rapid changes to application data models.

---

## Limitations of MongoDB

### Less Structured

Data consistency must be managed carefully.

### Complex Joins

Joins are not as straightforward as relational databases.

### Not Always Ideal for Transactions

Relational databases remain stronger for highly transactional workloads.

---

## Key Terms

### Document

A JSON-like record stored in MongoDB.

### Collection

A group of related documents.

### BSON

Binary representation of JSON.

### MongoClient

Python object used to connect to MongoDB.

### NoSQL

A category of databases that do not follow the traditional relational model.

---

## Key Takeaways

- MongoDB is a document-oriented NoSQL database.
- Data is stored as JSON-like documents.
- Collections are similar to tables in relational databases.
- MongoDB provides a flexible schema.
- MongoDB can be deployed using Docker containers.
- Python applications typically connect using the `pymongo` library.
- CRUD operations are supported through document manipulation methods.
- MongoDB is well suited for applications with rapidly changing data structures.

---

## Quick Reference

### MongoDB Hierarchy

```text
Database
    ↓
Collection
    ↓
Document
```

### Common Commands

Insert:

```python
insert_one()
```

Read:

```python
find()
```

Update:

```python
update_one()
```

Delete:

```python
delete_one()
```

### Module Theme

**MongoDB provides a flexible, document-based alternative to relational databases and is commonly used when application data structures evolve frequently or contain semi-structured information.**