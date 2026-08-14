# Video 12.9: Cassandra: A Distributed Scalable Database

## Overview

This lesson introduces Apache Cassandra, a distributed NoSQL database designed to store massive amounts of data while maintaining high availability and fault tolerance.

Unlike relational databases that rely on a single server, Cassandra distributes data across multiple nodes, eliminating single points of failure and enabling horizontal scalability.

Dr. Sanchez demonstrates:

- What Cassandra is
- Distributed database concepts
- Running Cassandra in a Docker container
- Connecting to Cassandra from Python
- Reading and writing data using Python

---

## Video Information

**Video 12.9: Cassandra: A Distributed Scalable Database**

**Duration:** 09:43

---

## What Is Cassandra?

Apache Cassandra is a:

- NoSQL database
- Distributed database
- Highly scalable database
- Fault-tolerant system

Cassandra was designed to handle:

- Massive datasets
- High transaction volumes
- Continuous availability

Even when individual servers fail.

---

## Why Cassandra Exists

Traditional databases often rely on a single database server.

Example:

```text
Application
     ↓
Database Server
```

Problems:

- Single point of failure
- Limited scalability
- Performance bottlenecks

Cassandra solves these issues by distributing data across multiple servers.

---

## Distributed Database Architecture

Instead of a single server:

```text
Application
     ↓
 ┌───────┐
 │ Node1 │
 ├───────┤
 │ Node2 │
 ├───────┤
 │ Node3 │
 └───────┘
```

Benefits:

- Data replication
- Load balancing
- Fault tolerance
- Horizontal scalability

---

## No Single Point of Failure

One of Cassandra's most important features is:

```text
No Single Point of Failure
```

If a server fails:

```text
Node 1 → Failed
```

Remaining nodes continue servicing requests.

Example:

```text
Node 2 → Active
Node 3 → Active
```

Application remains available.

---

## Horizontal Scaling

Relational databases often scale vertically:

```text
More CPU
More Memory
Better Hardware
```

Cassandra scales horizontally:

```text
Add More Servers
```

Example:

```text
3 Nodes
     ↓
10 Nodes
     ↓
100 Nodes
```

Storage and performance grow with the cluster.

---

## Cassandra Data Model

Cassandra organizes data using:

```text
Keyspace
     ↓
Table
     ↓
Row
```

Equivalent to:

| Relational Database | Cassandra |
|---------------------|------------|
| Database | Keyspace |
| Table | Table |
| Row | Row |
| Column | Column |

---

## Keyspace

A keyspace is similar to a database.

Example:

```sql
CREATE KEYSPACE employee_db;
```

Keyspaces contain tables and replication settings.

---

## Tables

Within a keyspace:

```sql
CREATE TABLE employees(
    id UUID,
    firstname TEXT,
    lastname TEXT
);
```

Tables store data similar to relational databases.

---

## Cassandra Replication

Cassandra automatically stores copies of data.

Example:

```text
Node1
Node2
Node3
```

The same record may exist on multiple nodes.

Advantages:

- Redundancy
- Reliability
- Disaster recovery

---

## Running Cassandra in Docker

Cassandra can run inside a Docker container.

### Pull Cassandra Image

```bash
docker pull cassandra
```

### Run Cassandra Container

```bash
docker run --name cassandra-server -p 9042:9042 -d cassandra
```

---

## Verify Container

```bash
docker ps
```

Expected:

```text
cassandra-server
0.0.0.0:9042->9042/tcp
```

---

## Cassandra Python Driver

Python applications communicate with Cassandra through the DataStax Cassandra Driver.

Install:

```bash
pip install cassandra-driver
```

Import:

```python
from cassandra.cluster import Cluster
```

---

## Connecting to Cassandra

Example:

```python
from cassandra.cluster import Cluster

cluster = Cluster(["127.0.0.1"])

session = cluster.connect()
```

Connection workflow:

```text
Python
    ↓
Cluster
    ↓
Session
    ↓
Cassandra
```

---

## Creating a Keyspace

Example:

```python
session.execute("""
CREATE KEYSPACE IF NOT EXISTS employee_db
WITH replication =
{
    'class':'SimpleStrategy',
    'replication_factor':1
}
""")
```

---

## Using a Keyspace

```python
session.set_keyspace(
    "employee_db"
)
```

---

## Creating a Table

```python
session.execute("""
CREATE TABLE employees(
    id UUID PRIMARY KEY,
    firstname TEXT,
    lastname TEXT
)
""")
```

---

## Inserting Data

Example:

```python
session.execute("""
INSERT INTO employees(
    id,
    firstname,
    lastname
)
VALUES(
    uuid(),
    'John',
    'Smith'
)
""")
```

---

## Reading Data

```python
rows = session.execute(
    "SELECT * FROM employees"
)

for row in rows:
    print(row)
```

---

## Updating Data

```python
session.execute("""
UPDATE employees
SET lastname='Jones'
WHERE id=...
""")
```

---

## Deleting Data

```python
session.execute("""
DELETE FROM employees
WHERE id=...
""")
```

---

## CRUD Operations

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

## Cassandra vs MongoDB vs Redis

| Feature | Cassandra | MongoDB | Redis |
|----------|------------|----------|--------|
| Database Type | Distributed NoSQL | Document | Key-Value |
| Scaling | Horizontal | Horizontal | Limited |
| Data Structure | Tables | Documents | Keys |
| Availability | Extremely High | High | High |
| Fault Tolerance | Excellent | Good | Good |
| Primary Use | Large Scale Systems | Flexible Applications | Caching |

---

## Advantages of Cassandra

### High Availability

System remains operational during failures.

### Horizontal Scaling

Add more servers as needed.

### Fault Tolerance

Data replicated across nodes.

### Massive Storage Capacity

Designed for large-scale workloads.

### No Single Point of Failure

Cluster continues operating even when nodes fail.

---

## Common Cassandra Use Cases

### IoT Platforms

Millions of sensor readings.

### Telecommunications

Call detail records.

### Financial Services

Large transaction workloads.

### Streaming Platforms

Large-scale event storage.

### Social Media

User activity and messaging.

---

## Key Terms

### Node

An individual Cassandra server.

### Cluster

A collection of Cassandra nodes.

### Keyspace

Equivalent to a database.

### Replication

Storing copies of data across nodes.

### Partition Key

Field used to determine where