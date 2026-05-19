---
icon: lucide/database
---

# MongoDB

The `utkit.store.mongo` module provides an asynchronous MongoDB client for interacting with MongoDB databases.

## Installation

Install the required dependencies:

```bash
pip install "utkit[store]"
# or
pip install pymongo[srv]
```

---

## Quick start

```python
from utkit.store.mongo import MongoClient

mongo = MongoClient(uri="mongodb://localhost:27017")

db = await mongo.get_database("my_database")
collection = db["my_collection"]

# Perform operations
await collection.insert_one({"name": "Alice", "age": 30})
user = await collection.find_one({"name": "Alice"})
print(user)  # {'_id': ObjectId(...), 'name': 'Alice', 'age': 30}
```

---

## `MongoClient`

A class that provides an asynchronous MongoDB client for database operations.

### Constructor

```python
MongoClient(uri: str)
```

- **Parameters**:
  - `uri` (str): The MongoDB connection URI.

---

### Methods

#### `get_database`

```python
async def get_database(self, name: str)
```

Retrieves a database by name.

- **Parameters**:
  - `name` (str): The name of the database to retrieve.
- **Returns**: An asynchronous MongoDB database object.