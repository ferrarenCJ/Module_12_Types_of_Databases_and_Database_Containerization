# Cassandra Cheat Sheet

## Start cqlsh

```bash
cqlsh
```

## Show Keyspaces

```sql
DESCRIBE KEYSPACES;
```

## Create Keyspace

```sql
CREATE KEYSPACE company
WITH replication =
{
  'class':'SimpleStrategy',
  'replication_factor':1
};
```

## Use Keyspace

```sql
USE company;
```

## Create Table

```sql
CREATE TABLE employees
(
    employee_id INT PRIMARY KEY,
    name TEXT
);
```

## Insert Data

```sql
INSERT INTO employees
(employee_id,name)
VALUES
(1,'John Smith');
```

## Query Data

```sql
SELECT *
FROM employees;
```