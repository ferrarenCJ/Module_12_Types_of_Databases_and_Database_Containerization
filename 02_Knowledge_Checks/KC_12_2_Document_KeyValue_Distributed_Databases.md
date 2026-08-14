# Knowledge Check 12.2: Document, Key-Value, and Distributed Scalable Databases

## Overview

This knowledge check covered the three major NoSQL database types introduced in Module 12:

- MongoDB (Document Database)
- Redis (Key-Value Database)
- Cassandra (Distributed Scalable Database)

The assessment focused on database architecture, terminology, scalability, fault tolerance, and common operations.

---

## Learning Outcome

**Identify key concepts related to different types of databases.**

---

# Question 1

## Which of the following are advantages of document stores?

### Correct Answer

✅ **All of the answer options are correct.**

### Explanation

Document databases provide several advantages:

- Documents are independent units.
- Application logic is easier to write.
- Unstructured data can be stored easily.
- Flexible schemas allow different document structures.

### Example

```json
{
    "FirstName": "John",
    "Age": 25
}
```

```json
{
    "FirstName": "Mary",
    "Age": 28,
    "Department": "Engineering"
}
```

Both documents can exist within the same collection.

---

# Question 2

## What kind of database is MongoDB?

### Correct Answer

✅ **Document-based database**

### Explanation

MongoDB stores data as documents rather than rows and columns.

Structure:

```text
Database
    ↓
Collection
    ↓
Document
```

MongoDB is a NoSQL document-oriented database.

---

# Question 3

## What document format is used internally in MongoDB?

### Correct Answer

✅ **BSON**

### Explanation

MongoDB stores data as:

```text
BSON
```

which stands for:

```text
Binary JSON
```

BSON extends JSON with:

- Binary data support
- Date types
- Additional data types
- Improved storage efficiency

---

# Question 4

## How does MongoDB provide fault tolerance?

### Correct Answer

✅ **MongoDB keeps multiple copies of the same data on different servers so that a single server failure does not bring the whole system down.**

### Explanation

MongoDB uses:

```text
Replication
```

to store copies of data across multiple servers.

Benefits:

- High availability
- Fault tolerance
- Disaster recovery

---

# Question 5

## What are tables called in MongoDB?

### Correct Answer

✅ **Collections**

### Explanation

MongoDB terminology:

| Relational Database | MongoDB |
|---------------------|----------|
| Database | Database |
| Table | Collection |
| Record | Document |
| Row | Document |

Example:

```text
EmployeeDB
    ↓
employees
    ↓
documents
```

---

# Question 6

## What is Redis?

### Correct Answer

✅ **Redis is an in-memory, key-value data store.**

### Explanation

Redis is a NoSQL database that stores information as:

```text
Key → Value
```

Example:

```text
Italy → Rome
France → Paris
```

Redis stores data primarily in memory (RAM), providing extremely fast performance.

---

# Question 7

## What is the difference between keys in Redis and keys in Python dictionaries?

### Correct Answer

✅ **In Redis, keys are always strings, but in Python dictionaries, keys can be of any datatype.**

### Explanation

Redis:

```text
Keys are always strings.
```

Examples:

```text
"Italy"
"EmployeeID"
"Name"
```

Python dictionary example:

```python
my_dict = {
    "name": "John",
    1001: "Employee",
    True: "Active"
}
```

Python allows multiple key data types.

---

# Question 8

## What does the DEL method do in Redis?

### Correct Answer

✅ **It removes the specified key.**

### Explanation

Redis command:

```python
delete()
```

Example:

```python
r.delete("Italy")
```

Before:

```text
Italy → Rome
```

After:

```text
Key removed
```

---

# Question 9

## Which of the following is an advantage of the Cassandra database?

### Correct Answer

✅ **It is highly scalable.**

### Explanation

Cassandra is designed for:

- Massive datasets
- Horizontal scaling
- Distributed storage

Example:

```text
3 Nodes
    ↓
10 Nodes
    ↓
100 Nodes
```

Performance and storage increase as additional nodes are added.

---

# Question 10

## What are keyspaces in Cassandra?

### Correct Answer

✅ **A keyspace is like an RDBMS database that contains column families, indexes, etc.**

### Explanation

A keyspace is the highest-level container in Cassandra.

Equivalent:

| Relational Database | Cassandra |
|---------------------|------------|
| Database | Keyspace |
| Table | Table |
| Row | Row |

Example:

```text
employees
    ├── employee
    ├── department
    └── payroll
```

The keyspace contains tables, indexes, replication settings, and schema information.

---

# MongoDB Summary

### Database Structure

```text
Database
    ↓
Collection
    ↓
Document
```

### Key Concepts

- Document Database
- BSON
- Collections
- Replication
- Fault Tolerance
- Flexible Schema

---

# Redis Summary

### Database Structure

```text
Key
    ↓
Value
```

### Key Concepts

- In-Memory Database
- Key-Value Store
- GET
- SET
- DEL
- Fast Data Retrieval

---

# Cassandra Summary

### Database Structure

```text
Cluster
    ↓
Node
    ↓
Keyspace
    ↓
Table
```

### Key Concepts

- Distributed Database
- Fault Tolerance
- High Availability
- Horizontal Scaling
- Replication
- Keyspaces

---

# Knowledge Check Results

### Final Score

```text
10 / 10 Correct
```

### Topics Mastered

✅ MongoDB Fundamentals

✅ MongoDB Collections and BSON

✅ MongoDB Replication and Fault Tolerance

✅ Redis Architecture

✅ Redis Commands and Data Types

✅ Cassandra Keyspaces

✅ Cassandra Scalability

✅ Cassandra Distributed Architecture

✅ Cassandra Fault Tolerance

✅ NoSQL Database Concepts

---

# Key Takeaways

### MongoDB

```text
Collection = Table
Document = Record
BSON = Storage Format
```

### Redis

```text
SET = Create/Update
GET = Read
DEL = Delete
```

### Cassandra

```text
Keyspace = Database
Node = Server
Cluster = Collection of Nodes
```

Module Theme:

> MongoDB, Redis, and Cassandra are NoSQL databases designed to solve different data management challenges through document storage, key-value storage, and distributed scalable architectures.