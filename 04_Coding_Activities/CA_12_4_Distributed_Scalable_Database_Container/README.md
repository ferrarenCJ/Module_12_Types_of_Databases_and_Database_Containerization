# Coding Activity 12.4: Modify a Distributed Scalable Database in a Container

## Objective

The objective of this activity is to deploy a Cassandra database in a Docker container, create and populate a database using Python, retrieve data using a Python client, and perform additional database operations using the Cassandra Query Language Shell (cqlsh).

---

## Learning Outcome

**Update and delete data in different types of containerized databases.**

---

## Technologies Used

- Python 3.11
- Apache Cassandra
- Cassandra Python Driver
- Docker
- Docker Desktop
- Visual Studio Code
- cqlsh

---

## Environment Setup

### Cassandra Docker Container

Container Name:

```text
cassandra-server
```

Port:

```text
9042
```

Verify the container is running:

```bash
docker ps
```

Expected output:

```text
cassandra-server
0.0.0.0:9042->9042/tcp
```

---

## Python Driver Installation

Install the Cassandra driver:

```bash
pip install cassandra-driver
```

Verify installation:

```bash
pip show cassandra-driver
```

---

# Task 1: Create the Books Keyspace

A Cassandra keyspace functions similarly to a database in a relational database management system.

Keyspace:

```text
books
```

---

# Task 2: Create the Book Table

Table Name:

```text
book
```

### Table Structure

| Column Name | Data Type |
|------------|------------|
| Book_ID | int |
| Name | text |
| Author | text |
| Year_Published | int |
| Number_of_Pages | int |

### Primary Key

```text
Book_ID
```

---

# Task 3: Populate the Table

### Initial Books

| Book_ID | Name | Author | Year_Published | Number_Of_Pages |
|----------|----------|----------|----------|----------|
| 1 | The Mystery of Capital | Hernando de Soto | 1970 | 209 |
| 2 | Fairy Tales | Hans Christian Andersen | 1836 | 784 |
| 3 | The Divine Comedy | Dante Alighieri | 1315 | 928 |
| 4 | Romeo and Juliet | William Shakespeare | 1597 | 100 |

---

# write.py

## Purpose

The script performs the following actions:

1. Connects to Cassandra.
2. Creates the books keyspace.
3. Creates the book table.
4. Inserts four book records.

### Expected Output

```text
Books loaded successfully.
```

---

# Task 4: Read Data Using Python

## File

```text
read.py
```

### Purpose

Connect to the books keyspace and retrieve all records from the book table.

### Query

```sql
SELECT * FROM book;
```

### Expected Output

```text
Row(book_id=1, ...)
Row(book_id=2, ...)
Row(book_id=3, ...)
Row(book_id=4, ...)
```

---

# Task 5: Connect Using cqlsh

Open the Cassandra shell:

```bash
docker exec -it cassandra-server cqlsh
```

Connect to the books keyspace:

```sql
USE books;
```

---

# Task 6: Insert the Fifth Book

Run:

```sql
INSERT INTO book
(
    Book_ID,
    Name,
    Author,
    Year_Published,
    Number_of_Pages
)
VALUES
(
    5,
    'Hamlet',
    'William Shakespeare',
    1603,
    100
);
```

### Book Added

| Book_ID | Name | Author | Year_Published | Number_Of_Pages |
|----------|----------|----------|----------|----------|
| 5 | Hamlet | William Shakespeare | 1603 | 100 |

---

# Task 7: Verify All Books

Run:

```sql
SELECT * FROM book;
```

Expected results:

```text
 book_id | author                  | name                     | number_of_pages | year_published
---------+-------------------------+--------------------------+-----------------+---------------
       1 | Hernando de Soto        | The Mystery of Capital   |             209 |          1970
       2 | Hans Christian Andersen | Fairy Tales              |             784 |          1836
       3 | Dante Alighieri         | The Divine Comedy        |             928 |          1315
       4 | William Shakespeare     | Romeo and Juliet         |             100 |          1597
       5 | William Shakespeare     | Hamlet                   |             100 |          1603
```

---

## Source Files

### write.py

Creates:

- books keyspace
- book table
- four initial book records

### read.py

Reads and displays all books stored in the book table.

---

## Cassandra Concepts Demonstrated

### Keyspace

Equivalent to a relational database.

Example:

```text
books
```

### Table

Stores related data records.

Example:

```text
book
```

### Cluster

A collection of Cassandra nodes.

### Node

A server that stores Cassandra data.

### Replication

Copies data across nodes to support fault tolerance.

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

## Screenshots Required

### Step 1

Docker Desktop showing:

```text
cassandra-server
```

running on port:

```text
9042
```

### Step 2

`write.py` showing:

- books keyspace
- book table
- four insert statements

### Step 3

Terminal showing successful execution of:

```bash
python write.py
```

### Step 4

`read.py` code

### Step 5

Terminal output showing all four books

### Step 6

cqlsh window showing:

```sql
INSERT INTO book ...
```

for Hamlet

### Step 7

cqlsh window showing:

```sql
SELECT * FROM book;
```

with all five books displayed

---

## Key Takeaways

- Cassandra is a distributed NoSQL database.
- Keyspaces serve the same purpose as databases in relational systems.
- Cassandra provides high availability and fault tolerance.
- Docker simplifies Cassandra deployment.
- Python can connect to Cassandra using the Cassandra Driver.
- cqlsh provides direct access to Cassandra without using Python.
- Data can be created and queried using both Python and CQL.

---

## Conclusion

This activity demonstrated how to deploy and interact with a Cassandra database running in a Docker container. Using both Python and cqlsh, a books keyspace and book table were created, records were inserted and queried, and Cassandra's distributed database architecture was explored through hands-on practice.