# Module 12 Sandbox
## Types of Databases and Database Containerization

The Sandbox folder is used for experimentation, testing, troubleshooting, and practice activities completed during Module 12.

Unlike graded activities and assignments, the sandbox environment provides a safe place to test code, database connections, Docker containers, and configuration changes without affecting official submissions.

---

# Purpose

The sandbox serves as a development and learning environment where concepts can be explored before being implemented in graded activities.

### Common Uses

- Testing Python code
- Exploring database connections
- Practicing SQL queries
- Experimenting with Docker commands
- Testing Firebase configurations
- Troubleshooting errors
- Validating assignment solutions

---

# Technologies Tested

## MySQL

### Activities

- Database creation
- Table creation
- CRUD operations
- Python database connections

### Example

```sql
SELECT *
FROM assets;
```

---

## Docker

### Activities

- Pulling images
- Creating containers
- Managing container lifecycles
- Port mapping

### Example

```bash
docker ps
docker images
docker run
```

---

## MongoDB

### Activities

- Document creation
- Collection management
- Query testing

### Example

```javascript
db.employees.find()
```

---

## Redis

### Activities

- Key-value operations
- Redis client testing
- Python Redis integration

### Example

```python
r.mset({
    "Milk": "Lactose",
    "Bread": "Gluten"
})
```

---

## Cassandra

### Activities

- Keyspace creation
- Table creation
- cqlsh practice

### Example

```sql
DESCRIBE KEYSPACES;
```

---

## Firebase

### Activities

- Firebase Admin SDK testing
- Realtime Database operations
- Data validation
- Authentication testing

### Example

```python
print(ref.get())
```

---

# Troubleshooting Log

## Firebase SSL Certificate Verification Issue

### Error

```text
SSL: CERTIFICATE_VERIFY_FAILED
certificate verify failed:
self-signed certificate in certificate chain
```

### Cause

Corporate SSL inspection and certificate management policies.

### Resolution

Executed Firebase activities using a non-corporate computer where the Firebase connection completed successfully.

### Lesson Learned

When troubleshooting Firebase connection issues:

- Verify the Firebase configuration.
- Verify service account credentials.
- Check local SSL certificates.
- Consider VPN and corporate proxy configurations.

---

# Sandbox Best Practices

### Before Running Tests

✅ Create copies of production files.

✅ Use test databases when possible.

✅ Verify Docker container names and ports.

✅ Keep sensitive credentials out of GitHub.

---

### After Running Tests

✅ Remove unnecessary test files.

✅ Document successful solutions.

✅ Capture useful commands for future reference.

✅ Add important findings to cheat sheets or notes.

---

# Suggested Sandbox Contents

```text
test_mysql.py
test_redis.py
test_firebase.py

docker_notes.md
sql_examples.sql

temporary_screenshots/
practice_queries.sql
```

---

# Key Takeaways

- Sandbox environments reduce the risk of damaging production code.
- Experimentation improves understanding of database technologies.
- Troubleshooting skills are developed through testing and validation.
- Documenting successful solutions saves time in future projects.
- Sandbox environments are valuable tools for learning and problem solving.

---

# Module 12 Technologies Practiced

```text
MySQL
    ↓
Relational Database

Docker
    ↓
Containerization

MongoDB
    ↓
Document-Oriented Database

Redis
    ↓
Key-Value Database

Cassandra
    ↓
Distributed Database

Firebase
    ↓
Serverless Cloud Database
```

---

## Folder Purpose Summary

The Sandbox folder serves as a personal laboratory for testing, learning, troubleshooting, and validating concepts covered throughout Module 12 before applying them to discussions, coding activities, and assignments.