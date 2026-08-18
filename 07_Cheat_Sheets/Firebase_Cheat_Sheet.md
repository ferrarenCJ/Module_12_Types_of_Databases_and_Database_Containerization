# Firebase Cheat Sheet

## Install SDK

```bash
pip install firebase-admin
```

## Import

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
```

## Initialize

```python
cred = credentials.Certificate(
    "serviceAccountKey.json"
)

firebase_admin.initialize_app(
    cred,
    {
        'databaseURL':
        'https://project-default-rtdb.firebaseio.com/'
    }
)
```

## Create Reference

```python
ref = db.reference('py/')
```

## Write Data

```python
ref.set({
    'asset1': {
        'asset_type': 'Regulator'
    }
})
```

## Update Data

```python
ref.update({
    'status': 'Active'
})
```

## Read Data

```python
print(ref.get())
```