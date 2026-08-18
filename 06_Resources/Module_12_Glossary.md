# Module 12: Glossary

## Cassandra

Cassandra is a NoSQL database that was originally developed by Facebook. It is a distributed scalable database designed for high availability, scalability, and fault tolerance.

### Features

- Highly scalable
- Fault tolerant
- High availability (HA)
- Decentralized architecture
- Uses clusters and nodes

---

## cqlsh Terminal Command Line

The Cassandra Query Language Shell (**cqlsh**) is a command-line tool used to communicate with Cassandra databases. It can be accessed through a Docker container's command-line interface (CLI).

---

## Cluster

A cluster is a collection of Cassandra nodes that work together as a single system.

---

## Collection

In MongoDB, a collection is equivalent to a table in a relational database. Collections store groups of documents.

---

## Containerization

Containerization refers to deploying applications and databases within isolated containers that can run consistently across different environments.

---

## Cursor

A cursor is used to process the result set returned from a database query. It allows a program to access and manipulate rows returned from a database operation one at a time.

---

## Distributed Scalable Database

A distributed scalable database stores data across multiple servers and can scale horizontally by adding additional servers as data volume and workload increase.

### Example

```text
Cassandra
```

---

## Document

A document is MongoDB's equivalent of a database record. Documents are stored in JSON-like format and can contain flexible, schema-less data structures.

---

## Document Collection

A document collection in MongoDB is equivalent to a table in a relational database.

---

## Document-Oriented Database

A document-oriented database stores data as documents rather than rows and columns.

### Example

```text
MongoDB
```

---

## Firebase

Firebase is a serverless cloud database platform provided by Google. It supports real-time data synchronization and allows applications to interact with databases using multiple programming languages, including Python.

---

## Keyspace

A keyspace is Cassandra's equivalent of a database. It defines data storage, replication settings, and other database-level configurations.

---

## Key-Value Database

A key-value database stores information using pairs consisting of a unique key and an associated value.

### Example

```text
Redis
```

### Benefits

- Simple structure
- High performance
- Fast retrieval of data

---

## MongoDB

MongoDB is a NoSQL document-oriented database that stores data in JSON-like documents organized into collections.

### Features

- Flexible schema
- Horizontal scalability
- Fault tolerance
- Distributed architecture

---

## Node

A node in Cassandra is an individual server that stores actual data. Multiple nodes work together within a cluster.

---

## Redis

Redis is an in-memory key-value database optimized for extremely fast data access and retrieval.

### Typical Uses

- Caching
- Session management
- Real-time applications
- Message queues

---

## Redis Dictionary

Redis stands for **Remote Dictionary Service**.

Redis databases use key-value pairs similarly to Python dictionaries, but there are differences:

### Redis

- Supports commands such as:
  - GET
  - SET
  - DEL
- Keys are always strings.
- Values may contain different data types.

### Python Dictionaries

- Use methods such as:
  - copy()
  - clear()
  - pop()
- Keys can be any data type.
- Values are managed differently than Redis storage.

---

## Relational Database

A relational database stores data in tables consisting of rows and columns.

### Features

- Primary Keys
- Foreign Keys
- Structured schemas
- SQL support

### Example

```text
MySQL
```

---

## Serverless Cloud Database

A serverless cloud database is a database service where the cloud provider manages the infrastructure, scaling, and maintenance.

### Example

```text
Firebase
```

### Benefits

- No server management
- Automatic scaling
- Reduced operational overhead
- Cloud-hosted infrastructure

---

# Database Types Covered in Module 12

| Database | Type |
|-----------|-----------|
| MySQL | Relational Database |
| MongoDB | Document-Oriented Database |
| Redis | Key-Value Database |
| Cassandra | Distributed Scalable Database |
| Firebase | Serverless Cloud Database |

---

# Quick Review

### MySQL

```text
Relational Database
```

### MongoDB

```text
Document-Oriented Database
```

### Redis

```text
Key-Value Database
```

### Cassandra

```text
Distributed Scalable Database
```

### Firebase

```text
Serverless Cloud Database
```

---

# Key Terms to Remember

- CRUD
- Containerization
- Cursor
- Collection
- Document
- Node
- Cluster
- Keyspace
- Relational Database
- Document-Oriented Database
- Key-Value Database
- Distributed Scalable Database
- Serverless Cloud Database

---

## Module 12 Summary

```text
MySQL
    ↓
Relational Database

MongoDB
    ↓
Document-Oriented Database

Redis
    ↓
Key-Value Database

Cassandra
    ↓
Distributed Scalable Database

Firebase
    ↓
Serverless Cloud Database
```