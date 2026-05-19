---
icon: lucide/database
---

# Redis

The `utkit.store.redis` module provides a singleton-backed Redis client with a simple interface for common cache and store operations, built on top of [redis-py](https://github.com/redis/redis-py).

## Installation

`redis` is part of the optional `store` extras. Install `utkit` with the `store` extra:

```bash
pip install "utkit[store]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[store]"
```

---

## Quick start

```python
from utkit.store.redis import RedisManager

redis = RedisManager(url="redis://localhost:6379/0")

redis.set("user:1", {"name": "Alice", "role": "admin"}, ttl=3600)

user = redis.get("user:1")
print(user)  # {'name': 'Alice', 'role': 'admin'}
```

---

## `RedisManager`

A class that wraps a shared `redis.Redis` client instance. The underlying connection is created once per process (singleton pattern) and reused across all `RedisManager` instances.

Values are automatically serialised to JSON on write and deserialised on read, so you can store any JSON-compatible Python object.

### Constructor

```python
RedisManager(url: str)
```

| Parameter | Type | Description |
|---|---|---|
| `url` | `str` | Redis connection URL, e.g. `redis://localhost:6379/0` or `rediss://user:pass@host:6380/0` for TLS |

```python
redis = RedisManager(url="redis://localhost:6379/0")
```

---

### `set`

Stores a value under the given key, serialised as JSON.

```python
def set(self, key: str, value: Any, ttl: int | None = None) -> bool
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `key` | `str` | — | The Redis key |
| `value` | `Any` | — | Any JSON-serialisable value |
| `ttl` | `int \| None` | `None` | Expiry in seconds. `None` means no expiry. |

**Returns:** `bool` — `True` if the key was set successfully.

**Raises:** `RuntimeError` — if the Redis operation fails.

```python
redis.set("session:abc", {"user_id": 42}, ttl=1800)
```

---

### `get`

Retrieves and deserialises the value stored at a key.

```python
def get(self, key: str) -> Any
```

| Parameter | Type | Description |
|---|---|---|
| `key` | `str` | The Redis key to retrieve |

**Returns:** The deserialised Python value, or `None` if the key does not exist.

**Raises:** `RuntimeError` — if the Redis operation fails.

```python
session = redis.get("session:abc")
```

---

### `delete`

Deletes a key from Redis.

```python
def delete(self, key: str) -> int
```

| Parameter | Type | Description |
|---|---|---|
| `key` | `str` | The Redis key to delete |

**Returns:** `int` — the number of keys deleted (`1` if found and deleted, `0` if the key did not exist).

**Raises:** `RuntimeError` — if the Redis operation fails.

```python
redis.delete("session:abc")
```

---

### `exists`

```python
def exists(self, key: str) -> bool
```

Checks if a key exists in the Redis store.

- **Parameters**:
  - `key` (str): The key to check.
- **Returns**: `True` if the key exists, `False` otherwise.

---

### `expire`

```python
def expire(self, key: str, ttl: int) -> bool
```

Sets a time-to-live (TTL) for a key in the Redis store.

- **Parameters**:
  - `key` (str): The key to set the TTL for.
  - `ttl` (int): Time-to-live in seconds.
- **Returns**: `True` if the TTL was set successfully, `False` otherwise.

**Returns:** `bool` — `True` if the TTL was set, `False` if the key does not exist.

```python
redis.expire("session:abc", 600)
```

---

## Connection URLs

| Scheme | Description |
|---|---|
| `redis://host:port/db` | Standard unencrypted connection |
| `rediss://host:port/db` | TLS-encrypted connection |
| `redis://:password@host:port/db` | Password-authenticated connection |
| `unix:///path/to/socket.sock` | Unix domain socket |

```python
# With password
redis = RedisManager(url="redis://:mypassword@localhost:6379/0")

# With TLS
redis = RedisManager(url="rediss://localhost:6380/0")
```
