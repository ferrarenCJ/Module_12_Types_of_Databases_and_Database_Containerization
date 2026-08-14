# Mini-Lesson 12.4: Cassandra: A Distributed Scalable Database

## Overview

Apache Cassandra is a distributed NoSQL database originally developed by Facebook. It is designed to store and manage very large datasets across multiple servers while providing high availability, scalability, and fault tolerance.

Unlike traditional relational databases, Cassandra distributes data across multiple nodes and eliminates single points of failure.

---

## What Is Cassandra?

Cassandra is a:

- NoSQL database
- Distributed database
- Highly scalable database
- Fault-tolerant system
- High-availability platform

Cassandra is commonly used by organizations that process massive volumes of data and require continuous system availability.

---

## Key Features of Cassandra

### Highly Scalable

Cassandra can expand easily by adding additional servers (nodes).

Benefits:

- Supports growing datasets
- Supports increasing workloads
- No major redesign required

Example:

```text
3 Nodes
    ↓
10 Nodes
    ↓
100 Nodes
```

As storage and performance requirements increase, more nodes can be added to the cluster.

---

### Fault Tolerant

Cassandra stores copies of the same data across multiple nodes.

Example:

```text
Node 1
Node 2
Node 3
```

If one node fails, the remaining nodes still provide access to the data.

Benefits:

- Reduced downtime
- Increased reliability
- Improved disaster recovery

---

### High Availability (HA)

High Availability means authorized users can continuously access data and applications.

HA protects against failures involving:

- Hard drives
- CPUs
- Servers
- Data centers
- Regional outages

Goal:

```text
Maximum uptime
```

---

### Decentralized Architecture

Cassandra has no central server.

Every node in the cluster operates independently while working together.

Benefits:

- No bottlenecks
- No master server dependency
- No single point of failure

---

### Cluster-Based Design

Cassandra uses clusters composed of multiple nodes.

#### Node

A node is a server that contains data.

Example:

```text
Node 1
```

#### Cluster

A cluster is a collection of nodes functioning as a single database system.

Example:

```text
Cluster
├── Node 1
├── Node 2
└── Node 3
```

Every node is independent and participates equally.

---

## Cassandra Data Model

### Keyspace

In Cassandra, a database is called a:

```text
Keyspace
```

A keyspace contains:

- Tables
- Replication settings
- Cluster configuration

Equivalent:

| Relational Database | Cassandra |
|---------------------|------------|
| Database | Keyspace |
| Table | Table |
| Row | Row |
| Column | Column |

---

### Apache Cassandra Definition

According to PhoenixNAP:

> In a Cassandra cluster, a keyspace is an outermost object that determines how data replicates on nodes. Keyspaces consist of core objects called column families (tables), rows indexed by keys, datatypes, data center awareness, replication factor, and keyspace strategy.

---

## Running Cassandra in Docker

### Create a Cassandra Container

```bash
docker run -p 9042:9042 --name some-cassandra -d cassandra
```

### Parameter Breakdown

```text
-p 9042:9042
```

Maps local port 9042 to Cassandra's internal port.

```text
--name some-cassandra
```

Assigns a container name.

```text
-d
```

Runs the container in detached mode.

---

## Verify Cassandra Is Running

```bash
docker ps
```

Expected:

```text
some-cassandra
0.0.0.0:9042->9042/tcp
```

---

## Install Cassandra Python Driver

Install the driver:

```bash
pip install cassandra-driver
```

Import:

```python
from cassandra.cluster import Cluster
```

---

## Creating a Keyspace with Python

### Connect

```python
from cassandra.cluster import Cluster

cluster = Cluster(
    ['localhost'],
    port=9042
)

session = cluster.connect()
```

### Create Keyspace

```python
session.execute("""
CREATE KEYSPACE IF NOT EXISTS employees
WITH REPLICATION = {
    'class':'SimpleStrategy',
    'replication_factor':1
};
""")
```

---

## Using a Keyspace

Equivalent to:

```sql
USE employees;
```

Python:

```python
session.set_keyspace(
    'employees'
)
```

---

## Creating a Table

```python
session.execute("""
CREATE TABLE IF NOT EXISTS employee (
    EMPLOYEE_ID int PRIMARY KEY,
    FIRST_NAME text,
    LAST_NAME text,
    AGE int
);
""")
```

Table structure:

| Column | Type |
|----------|----------|
| EMPLOYEE_ID | int |
| FIRST_NAME | text |
| LAST_NAME | text |
| AGE | int |

---

## Inserting Data

Example employee:

```python
session.execute("""
INSERT INTO employee (
    EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    AGE
)
VALUES (
    123450,
    'John',
    'Doe',
    33
);
""")
```

Additional employees:

```text
Mary Jane
Peter Gabriel
```

---

## Reading Data Using Python

### Query

```python
rows = session.execute(
    'SELECT * FROM EMPLOYEE'
)
```

### Display Results

```python
for row in rows:
    print(row)
```

Expected output:

```text
Row(
    employee_id=123450,
    first_name='John',
    last_name='Doe',
    age=33
)
```

---

## Using CQLSH

Cassandra provides:

```text
cqlsh
```

which allows direct interaction with the database.

### Open the Shell

```bash
docker exec -it some-cassandra cqlsh
```

Example prompt:

```text
cqlsh>
```

---

## View Keyspaces

```sql
DESCRIBE KEYSPACES;
```

Example:

```text
employees
system
system_auth
system_schema
```

---

## Select a Keyspace

```sql
USE employees;
```

Output:

```text
employees>
```

---

## Query Data

```sql
SELECT * FROM employee;
```

Expected:

```text
 employee_id | first_name | last_name | age
-------------+------------+-----------+-----
      123450 | John       | Doe       |  33
      123678 | Mary       | Jane      |  21
      678123 | Peter      | Gabriel   |  65
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

## Cassandra Architecture

```text
Cluster
    ↓
Node
    ↓
Keyspace
    ↓
Table
    ↓
Row
```

---

## Cassandra vs Other Databases

| Feature | Cassandra | MongoDB | Redis |
|----------|------------|----------|--------|
| Type | Distributed NoSQL | Document DB | Key-Value DB |
| Storage Model | Tables | Documents | Keys |
| Availability | Very High | High | High |
| Scalability | Excellent | Excellent | Good |
| Fault Tolerance | Excellent | Good | Moderate |
| Typical Use | Large Enterprise Systems | Web Applications | Caching |

---

## Common Cassandra Use Cases

### Social Media

- Activity feeds
- Messaging systems

### Telecommunications

- Call records
- Usage tracking

### Financial Services

- Transaction logs
- Market data

### Internet of Things (IoT)

- Sensor data
- Device telemetry

### Streaming Platforms

- Event storage
- Real-time analytics

---

## Key Terms

### Keyspace

Equivalent to a database.

### Node

An individual Cassandra server.

### Cluster

A collection of nodes.

### Replication

Storing copies of data across multiple nodes.

### High Availability

Continuous access to data and applications.

### Fault Tolerance

Operation continues despite failures.

---

## Docker Commands

Create container:

```bash
docker run -p 9042:9042 --name some-cassandra -d cassandra
```

Start:

```bash
docker start some-cassandra
```

Stop:

```bash
docker stop some-cassandra
```

Open cqlsh:

```bash
docker exec -it some-cassandra cqlsh
```

---

## Key Takeaways

- Cassandra is a distributed NoSQL database.
- Cassandra stores data in keyspaces and tables.
- Data is replicated across multiple nodes.
- Cassandra eliminates single points of failure.
- Cassandra provides high availability and fault tolerance.
- Cassandra scales horizontally by adding nodes.
- Python applications connect using the Cassandra Driver.
- Docker provides an easy way to deploy Cassandra locally.
- cqlsh allows direct interaction with Cassandra without Python.

### Quick Reference

```text
Keyspace
    ↓
Table
    ↓
Row
```

Connect:

```python
Cluster(['localhost'], port=9042)
```

Open Shell:

```bash
docker exec -it some-cassandra cqlsh
```

Module Example:

```text
Keyspace: employees
Table: employee
```

### Module Theme

**Cassandra is a distributed, fault-tolerant, highly available database designed to manage massive datasets across clusters of independent nodes without a single point of failure.**