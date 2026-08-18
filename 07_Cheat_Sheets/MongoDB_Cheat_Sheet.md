# MongoDB Cheat Sheet

## Show Databases

```javascript
show dbs
```

## Create / Use Database

```javascript
use company
```

## Create Collection

```javascript
db.createCollection("employees")
```

## Insert Document

```javascript
db.employees.insertOne({
    employee_id: 1,
    name: "John Smith"
});
```

## Find Documents

```javascript
db.employees.find()
```

## Update Document

```javascript
db.employees.updateOne(
    { employee_id: 1 },
    { $set: { name: "Jane Smith" } }
)
```

## Delete Document

```javascript
db.employees.deleteOne(
    { employee_id: 1 }
)
```
