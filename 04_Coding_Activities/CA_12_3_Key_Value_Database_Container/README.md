# Coding Activity 12.3: Modify a Key-Value Database in a Container

## Objective

The objective of this activity is to create and interact with a Redis key-value database running inside a Docker container. The activity demonstrates how to create key-value pairs, retrieve stored values, and use Python to communicate with a Redis database.

---

## Learning Outcome

**Update and delete data in different types of containerized databases.**

---

## Technologies Used

- Python
- Redis
- Redis Python Client
- Docker
- Docker Desktop
- Visual Studio Code

---

## Overview

Redis is a NoSQL key-value database that stores information using a simple structure:

```text
Key → Value
```

For this activity, Redis stores the following entries:

```text
Italy  → Rome
France → Paris
```

---

## Docker Container Setup

### Pull Redis Image

```bash
docker pull redis
```

### Create Redis 