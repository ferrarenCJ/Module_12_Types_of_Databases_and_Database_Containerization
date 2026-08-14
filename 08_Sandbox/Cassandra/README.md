# Cassandra Sandbox

## Purpose

This folder contains the examples, code, and notes developed while following **Module 12 Video 12.9: Cassandra - A Distributed Scalable Database**.

The goal of this sandbox is to explore how Cassandra stores and retrieves data in a distributed environment and how Python applications can communicate with Cassandra using the Cassandra Driver.

---

## Overview

Apache Cassandra is a distributed NoSQL database designed to handle large amounts of data while providing:

- High availability
- Fault tolerance
- Horizontal scalability
- No single point of failure

Unlike traditional relational databases, Cassandra distributes data across multiple nodes and replicates data to ensure reliability.

---

## Environment Setup

### Pull Cassandra Image

```bash
docker pull cassandra
```

### Create Cassandra Container

```bash
docker run --name cassandra-server -p 9042:9042 -d cassandra
```

### Verify Container

```bash
docker ps
```

Expected output:

```text
CONTAINER ID   IMAGE       PORTS
xxxxxxxxxxxx   cassandra   0.0.0.0:9042->9042/tcp
```

---

## Python Driver Installation

Install the Cassandra Python Driver:

```bash
pip install cassandra-driver
```

Import the driver:

```python
from cassandra.cluster import Cluster
```

---

## Connecting to Cassandra

```python
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()
```

Connection flow:

```text
Python Application
        ↓
Cassandra Driver
        ↓
Cluster
        ↓
Session
        ↓
Cassandra Database
```

---

## Cassandra Data Model

### Cassandra Hierarchy

```text
Keyspace
    ↓
Table
    ↓
Row
```

### Relational Database Comparison

| Relational Database | Cassandra |
|---------------------|------------|
| Database | Keyspace |
| Table | Table |
| Row | Row |
| Column | Column |

---

## Keyspace Example

```sql
CREATE KEYSPACE employee_db
WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};
```

Use keyspace:

```sql
USE employee_db;
```

---

## Table Example

```sql
CREATE TABLE employees (
    id UUID PRIMARY KEY,
    firstname TEXT,
    lastname TEXT
);
```

---

## Insert Example

```sql
INSERT INTO employees (
    id,
    firstname,
    lastname
)
VALUES (
    uuid(),
    'John',
    'Smith'
);
```

---

## Read Example

```sql
SELECT * FROM employees;
```

Python example:

```python
rows = session.execute(
    "SELECT * FROM employees"
)

for row in rows:
    print(row)
```

---

## Update Example

```sql
UPDATE employees
SET lastname = 'Jones'
WHERE id = ?;
```

---

## Delete Example

```sql
DELETE FROM employees
WHERE id = ?;
```

---

## Video Files

### write.py

Purpose:

- Connect to Cassandra
- Create records
- Insert data into tables

### read.py

Purpose:

- Query records
- Display data from Cassandra tables

---

## CRUD Operations Demonstrated

### Create

```sql
INSERT
```

### Read

```sql
SELECT
```

### Update

```sql
UPDATE
```

### Delete

```sql
DELETE
```

---

## Distributed Database Concepts

### Node

An individual Cassandra server.

```text
Node 1
Node 2
Node 3
```

### Cluster

A collection of nodes working together.

```text
Cluster
├── Node 1
├── Node 2
└── Node 3
```

### Replication

Copies of data are stored across multiple nodes.

Benefits:

- High availability
- Fault tolerance
- Disaster recovery

---

## Advantages of Cassandra

### High Availability

Applications remain available even when individual nodes fail.

### Fault Tolerance

Data is replicated across multiple servers.

### Horizontal Scaling

Additional nodes can be added as data volume grows.

### No Single Point of Failure

Failure of a single node does not impact overall cluster availability.

### Massive Data Storage

Designed for enterprise-scale workloads.

---

## Common Use Cases

### Internet of Things (IoT)

- Sensor readings
- Smart devices

### Telecommunications

- Call detail records
- Event processing

### Financial Services

- High-volume transactions
- Fraud detection

### Social Media Platforms

- User activity tracking
- Messaging systems

### Streaming Platforms

- Event ingestion
- Activity logging

---

## Docker Commands

### Start Container

```bash
docker start cassandra-server
```

### Stop Container

```bash
docker stop cassandra-server
```

### View Running Containers

```bash
docker ps
```

### View All Containers

```bash
docker ps -a
```

---

## Key Concepts Learned

- Cassandra
- Distributed Databases
- Clusters
- Nodes
- Replication
- High Availability
- Fault Tolerance
- Horizontal Scaling
- Keyspaces
- Tables
- Cassandra Driver
- Docker Containers

---

## Status

✅ Cassandra Docker container created

✅ Cassandra Python driver installed

✅ Cassandra container accessible through port 9042

✅ Python connection established

✅ Write operations tested

✅ Read operations tested

✅ Video 12.9 examples completed

---

## Key Takeaways

- Cassandra is a distributed NoSQL database.
- Cassandra is designed for massive data volumes.
- Data is distributed across multiple nodes.
- Cassandra eliminates single points of failure.
- Data replication provides fault tolerance.
- Cassandra scales horizontally by adding servers.
- Python applications connect using the Cassandra Driver.
- Cassandra is commonly deployed using Docker containers.
- Cassandra is ideal for highly available, enterprise-scale systems.

---

## Conclusion

This sandbox provided hands-on experience with Apache Cassandra, a distributed scalable database designed for high availability and fault tolerance. Through Docker-based deployment and Python integration, it demonstrated how Cassandra differs from relational, document, and key-value databases while supporting large-scale data storage and processing requirements.