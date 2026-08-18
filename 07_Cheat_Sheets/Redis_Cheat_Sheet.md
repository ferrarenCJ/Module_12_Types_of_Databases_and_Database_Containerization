# Redis Cheat Sheet

## Connect

```bash
redis-cli
```

## Set Value

```bash
SET Milk Lactose
```

## Get Value

```bash
GET Milk
```

## Delete Key

```bash
DEL Milk
```

## Python Example

```python
r.mset({
    "Milk": "Lactose",
    "Bread": "Gluten"
})
```

## Read Values

```python
print(r.get("Milk"))
print(r.get("Bread"))
```