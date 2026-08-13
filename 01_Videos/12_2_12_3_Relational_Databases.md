# Videos 12.2 & 12.3: Relational Databases

## Overview

Relational databases are one of the most widely used database technologies in business and data engineering. In this lesson, Dr. Sanchez introduces relational database concepts, relational database design, and demonstrates how to interact with a MySQL database using Python.

The videos also cover CRUD operations, which are the foundational operations performed on data stored in a relational database.

---

# Video 12.2: Relational Databases - Part 1

**Duration:** 4:46

## What Is a Relational Database?

A relational database stores data in tables consisting of rows and columns. Relationships between tables are established using keys, allowing data to be organized efficiently while reducing redundancy.

Common relational database systems include:

- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server

MySQL is one of the most widely used relational database management systems (RDBMS) in industry.

---

## Characteristics of Relational Databases

### Structured Data

Data is stored in predefined schemas consisting of:

- Tables
- Columns
- Rows
- Constraints

Example:

| EmployeeID | Name | Department |
|------------|--------|------------|
| 1001 | Alice | Engineering |
| 1002 | Bob | Finance |

---

### Relationships

Tables can be connected through:

- Primary Keys
- Foreign Keys

Example:

**Employees Table**

| EmployeeID | Name |
|------------|------|
| 1001 | Alice |

**Departments Table**

| DepartmentID | Department |
|-------------|------------|
| 10 | Engineering |

Relationships allow data normalization and consistency.

---

## Relational Database Design

Good database design helps:

- Reduce redundancy
- Improve consistency
- Improve query performance
- Maintain data integrity

Key concepts include:

- Entities
- Attributes
- Primary Keys
- Foreign Keys
- Normalization

---

## Python Client Application

Dr. Sanchez demonstrates how to create a Python client program that communicates with MySQL.

Components include:

### Python Client

Python acts as the client application that sends commands to the database.

### Database Driver

A driver allows Python to communicate with MySQL.

Example libraries include:

```python
mysql.connector
pymysql
```

The database driver serves as an interface between:

```text
Python Application
        ↓
 MySQL Driver
        ↓
 MySQL Database
```

---

## Key Takeaways from Video 12.2

- MySQL is a relational database management system.
- Relational databases store data in tables.
- Database relationships are created using keys.
- Proper database design reduces redundancy and improves consistency.
- Python applications use drivers to connect to databases.

---

# Video 12.3: Relational Databases - Part 2

**Duration:** 8:32

## CRUD Operations

CRUD represents the four fundamental database operations:

| Operation | Purpose |
|------------|-----------|
| Create | Insert new data |
| Read | Retrieve data |
| Update | Modify existing data |
| Delete | Remove data |

These operations form the foundation of nearly all database applications.

---

## CREATE

Adds new records to the database.

Example SQL:

```sql
INSERT INTO employees
(
    employee_id,
    employee_name
)
VALUES
(
    1001,
    'Alice'
);
```

Purpose:

- Add customers
- Add products
- Add transactions
- Add employee records

---

## READ

Retrieves records from the database