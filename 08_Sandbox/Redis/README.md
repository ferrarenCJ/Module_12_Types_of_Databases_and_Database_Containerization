# Redis Sandbox

## Purpose

This folder contains the Redis examples from Module 12 Video 12.8.

## Environment

### Docker Container

```bash
docker run --name redis-server -p 6379:6379 -d redis
```

### Connection Settings

```text
Host: localhost
Port: 6379
```

## Python Driver

Install:

```bash
pip install redis
```

Import:

```python
import redis
```

## Connect to Redis

```python
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)
```

## Common Operations

### Create / Update

```python
r.set("name", "John")
```

### Read

```python
r.get("name")
```

### Delete

```python
r.delete("name")
```

## Key Concepts

- NoSQL Database
- Key-Value Storage
- In-Memory Database
- Caching
- Session Management
- Docker Containers
- Redis

## Status

- Redis Docker container running
- Python Redis library installed
- Read operations verified
- Write operations verified