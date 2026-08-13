# Mini-Lesson 12.1: Cursors

## Overview

A cursor is a database object that allows a program to process the results of a query one row at a time. Cursors are commonly used when applications need to retrieve, iterate through, or manipulate records returned from a database query.

In Python, cursors provide the interface between an application and the database, allowing SQL statements to be executed and results to be retrieved.

---

## What Is a Cursor?

A cursor is used to execute SQL statements and process the results returned by the database.

Think of a cursor as a pointer that moves through the rows returned by a query.

```text
Python Application
        ↓
      Cursor
        ↓
     Query
        ↓
    Database
```

The cursor acts as an intermediary between the application and the database.

---

## Basic Cursor Syntax

A cursor executes a query using:

```python
cursor.execute(query)
```

Where:

- `cursor` is the cursor object
- `query` is a SQL command written in MySQL syntax

Example:

```python
query = "SELECT * FROM fruit"

cursor.execute(query)
```

---

## Creating a Cursor in Python

After establishing a database connection, a cursor object can be created.

Example:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="fruit"
)

cursor = connection.cursor()
```

The cursor can now be used to execute SQL statements.

---

## Using a Cursor to Insert Data

The lesson provides the following example:

```python
query = (
    "INSERT INTO fruit (name, average_weight) "
    "VALUES (%s, %s)"
)

data = ("Apple", 200)

cursor.execute(query, data)
```

### Explanation

SQL Statement:

```sql
INSERT INTO fruit
(
    name,
    average_weight
)
VALUES
(
    'Apple',
    200
);
```

The values are supplied separately through the `data` variable.

Benefits:

- Improves security
- Reduces SQL injection risk
- Makes code easier to maintain

---

## Retrieving Data with a Cursor

Example:

```python
cursor.execute("SELECT * FROM fruit")
```

Retrieve records:

```python
for row in cursor:
    print(row)
```

Output:

```text
('Apple', 200)
('Orange', 180)
('Banana', 120)
```

The cursor iterates through each row returned by the query.

---

## Common Cursor Operations

### Execute Query

```python
cursor.execute(query)
```

Runs a SQL statement.

---

### Fetch One Record

```python
row = cursor.fetchone()
```

Returns:

```text
One row
```

Useful when expecting a single result.

---

### Fetch Multiple Records

```python
rows = cursor.fetchmany(5)
```

Returns:

```text
Five rows
```

Useful when working