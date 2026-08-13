# Knowledge Check 12.1: Containers

## Learning Outcome

Identify key concepts related to database containerization.

---

## Score

**5 / 5 Correct**

Completed: August 13, 2026

---

## Question Review

### Question 1

**Which of the following has its own operating system?**

✅ Correct Answer:

**Virtual machines**

#### Explanation

Virtual machines include a complete guest operating system.

Containers share the host operating system kernel and do not contain their own operating system.

---

### Question 2

**Which of the following options lists the correct order of steps required to run a MySQL database using containers on your machine?**

✅ Correct Answer:

1. Install Docker on your machine.
2. Download the MySQL Docker image from the Docker registry.
3. Execute the `docker run` command to start the container using the MySQL image.

#### Explanation

The standard workflow for running MySQL in Docker is:

```bash
docker pull mysql
docker run mysql
```

Docker provides the container platform while Docker Hub provides downloadable images.

---

### Question 3

**What is a container?**

✅ Correct Answer:

**Containers provide an isolated environment with a shared operating system and come with executables and libraries, as required.**

#### Explanation

Containers package:

- Application code
- Dependencies
- Libraries
- Configuration files

into isolated environments while sharing the host operating system kernel.

---

### Question 4

**Which functions can you perform on a running container?**

✅ Correct Answer:

**All the answer options are correct.**

#### Explanation

Docker containers can be:

- Started
- Stopped
- Restarted
- Deleted

Examples:

```bash
docker stop container_name
docker restart container_name
docker rm container_name
```

---

### Question 5

**What is the basic syntax to define a cursor in Python?**

✅ Correct Answer:

```python
cursor.execute(query)
```

#### Explanation

The cursor object executes SQL commands against a database.

Example:

```python
query = "SELECT * FROM fruit"

cursor.execute(query)
```

The cursor acts as the interface between Python and the database.

---

## Key Concepts Learned

### Virtual Machine

- Has its own operating system
- Higher resource usage
- Provides complete OS isolation

### Container

- Shares host operating system
- Lightweight
- Portable
- Fast startup

### Docker Image

- Blueprint for creating containers
- Stored in Docker Hub

### Docker Container

- Running instance of an image

### Cursor

Python object used to:

- Execute SQL statements
- Retrieve data
- Insert records
- Update records
- Delete records

---

## Key Takeaways

- Virtual machines contain their own operating systems.
- Containers share the host operating system.
- Docker images are used to create containers.
- MySQL can run inside a Docker container.
- Python uses `cursor.execute()` to communicate with databases.
- Containers simplify database deployment and improve portability across environments.