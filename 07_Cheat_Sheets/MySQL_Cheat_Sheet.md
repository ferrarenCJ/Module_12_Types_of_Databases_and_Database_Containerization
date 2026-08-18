# MySQL Cheat Sheet

## Connect

```bash
mysql -u root -p
```

## Show Databases

```sql
SHOW DATABASES;
```

## Create Database

```sql
CREATE DATABASE gas_utility_assets;
```

## Use Database

```sql
USE gas_utility_assets;
```

## Create Table

```sql
CREATE TABLE assets (
    asset_id INT PRIMARY KEY,
    asset_type VARCHAR(50),
    location VARCHAR(50)
);
```

## Insert Records

```sql
INSERT INTO assets
VALUES
(1,'Regulator','Anaheim');
```

## Query Data

```sql
SELECT *
FROM assets;
```

## Update Data

```sql
UPDATE assets
SET location='Long Beach'
WHERE asset_id=1;
```

## Delete Data

```sql
DELETE
FROM assets
WHERE asset_id=1;
```
