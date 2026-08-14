# Mini-Lesson 12.3: Redis: A Key-Value Database

## Overview

Redis is an in-memory NoSQL database that stores information using key-value pairs. Redis is designed for extremely fast data access and is commonly used for caching, session storage, real-time analytics, and messaging systems.

Unlike relational databases and document databases, Redis uses a simple structure:

```text
Key → Value
```

This design enables Redis to achieve very high performance and low latency.

---

## What Is Redis?

Redis stands for:

```text
REmote DIctionary Server
```

Redis is:

- An in-memory database
- A key-value data store
- A NoSQL database
- A high-performance caching platform

The key serves as a unique identifier used to retrieve the associated value.

Example:

```text
Name → John
```

```text
City → Anaheim
```

```text
EmployeeID → 1001
```

---

## Key-Value Databases

A key-value database stores data as:

```text
Key → Value
```

Example:

```text
username → ferrarenCJ
```

```text
department → Data Engineering
```

Unlike relational databases:

- No tables
- No rows
- No joins

Data is retrieved directly from its key.

---

## Redis Installation

Install the Redis Python library:

```bash
pip install redis
```

or

```bash
pip3 install redis
```

Import:

```python
import redis
```

---

## Running Redis in Docker

The module uses Redis running inside a Docker container.

### Create Redis Container

```bash
docker run -p 6379:6379 --name redis-server -d redis
```

### Parameter Breakdown

```text
-p 6379:6379
```

Maps the local Redis port to the container port.

```text
--name redis-server
```

Assigns a container name.

```text
-d
```

Runs Redis in detached mode.

```text
redis
```

Uses the official Redis image.

---

## Verify Container

```bash
docker ps
```

Expected:

```text
redis-server
0.0.0.0:6379->6379/tcp
```

---

## Connecting to Redis

Example connection:

```python
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)
```

Parameters:

### host

```text
localhost
```

Local Redis server.

### port

```text
6379
```

Default Redis port.

### db

```text
0
```

Database number.

---

## Redis Databases

Redis provides multiple logical databases.

Default configuration:

```text
0
1
2
...
15
```

Total:

```text
16 databases
```

Database numbers range from:

```text
0 to 15
```

Example:

```python
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)
```

connects to Redis Database 0.

---

## Redis and Python Dictionaries

Redis is often compared to Python dictionaries because both store information using key-value pairs.

Example Dictionary:

```python
employee = {
    "name": "John",
    "age": 25
}
```

Redis follows a similar pattern:

```text
name → John
age → 25
```

### Differences

#### Methods

Redis supports:

```text
GET
SET
DEL
```

Python dictionaries support:

```python
copy()
clear()
pop()
```

---

#### Key Types

Redis:

```text
Keys are always strings.
```

Python:

```text
Keys can be any hashable datatype.
```

---

#### Data Storage

Redis stores data outside the application.

Python dictionaries exist only in memory during program execution.

---

## Writing Data to Redis

Example:

```python
r.set(
    "name",
    "John"
)
```

Redis stores:

```text
name → John
```

---

## Reading Data from Redis

Retrieve a value:

```python
print(
    r.get("name")
)
```

Output:

```text
John
```

---

## Working with Lists

The lesson demonstrates using:

```python
rpush()
```

Example:

```python
r.rpush(
    "entries",
    "Record 1"
)
```

This pushes a value to the end of a Redis list.

---

## Reading Lists

Example:

```python
for item in r.lrange(
    "entries",
    0,
    -1
):
    print(item)
```

Output:

```text
Record 1
Record 2
Record 3
```

---

## Important Redis Methods

### GET

Retrieve the value associated with a key.

Example:

```python
r.get("name")
```

Result:

```text
John
```

If the key does not exist:

```text
nil
```

is returned by Redis.

---

### SET

Assign a value to a key.

Example:

```python
r.set(
    "name",
    "John"
)
```

If the key already exists:

```text
The value is overwritten.
```

---

### DEL

Delete a key.

Example:

```python
r.delete("name")
```

The key-value pair is removed.

---

## CRUD Operations in Redis

### Create

```python
r.set()
```

### Read

```python
r.get()
```

```python
r.lrange()
```

### Update

```python
r.set()
```

(overwrites existing value)

### Delete

```python
r.delete()
```

---

## Example Workflow

### Connect

```python
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    db=0
)
```

### Create

```python
r.set(
    "city",
    "Anaheim"
)
```

### Read

```python
print(
    r.get("city")
)
```

Output:

```text
Anaheim
```

### Update

```python
r.set(
    "city",
    "Los Angeles"
)
```

### Delete

```python
r.delete("city")
```

---

## Redis vs Python Dictionaries

| Feature | Redis | Python Dictionary |
|----------|--------|------------------|
| Storage | Database | Application Memory |
| Shared Access | Yes | No |
| Persistence | Optional | No |
| Data Access | Network | Local Memory |
| Supports GET/SET/DEL | Yes | No |

---

## Redis Use Cases

### Caching

Store frequently used data.

Examples:

- Product information
- API responses
- Customer profiles

---

### Session Storage

Store web application sessions.

Examples:

- Login tokens
- User settings
- Authentication data

---

### Real-Time Applications

Examples:

- Chat systems
- Gaming leaderboards
- Event processing

---

### Queue Processing

Redis lists are commonly used for:

- Job queues
- Message queues
- Event streaming

---

## Key Terms

### Redis

An in-memory NoSQL key-value database.

### Key

Unique identifier.

### Value

Information associated with a key.

### GET

Retrieve a value.

### SET

Store a value.

### DEL

Delete a value.

### RPUSH

Append an item to a Redis list.

### LRANGE

Read items from a Redis list.

---

## Docker Commands

Create Redis container:

```bash
docker run -p 6379:6379 --name redis-server -d redis
```

Verify container:

```bash
docker ps
```

Stop Redis:

```bash
docker stop redis-server
```

Start Redis:

```bash
docker start redis-server
```

---

## Key Takeaways

- Redis is a NoSQL key-value database.
- Data is stored as key-value pairs.
- Redis operates primarily in memory for extremely fast performance.
- Redis commonly supports caching, sessions, and real-time applications.
- Redis is frequently deployed using Docker containers.
- Redis databases are numbered from 0 through 15 by default.
- Common Redis operations include GET, SET, and DEL.
- Python applications connect using