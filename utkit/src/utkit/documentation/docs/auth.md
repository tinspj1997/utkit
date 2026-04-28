---
icon: lucide/key-round
---

# Auth

The `utkit.auth` module provides password hashing and verification utilities using [pwdlib](https://frankie567.github.io/pwdlib/).

## Installation

`pwdlib` is bundled as a core dependency — no extra installation is required beyond `utkit` itself:

```bash
pip install utkit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add utkit
```

---

## Quick start

```python
from utkit.auth import create_password_hash, verify_password

hashed = create_password_hash("my-secret-password")
is_valid = verify_password("my-secret-password", hashed)

print(is_valid)  # True
```

---

## `create_password_hash`

Hashes a plain-text password using the recommended algorithm from `pwdlib`.

```python
def create_password_hash(password: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `password` | `str` | The plain-text password to hash |

**Returns:** `str` — the hashed password string (includes algorithm metadata).

```python
hashed = create_password_hash("hunter2")
```

---

## `verify_password`

Verifies a plain-text password against a stored hash.

```python
def verify_password(plain_password: str, hashed_password: str) -> bool
```

| Parameter | Type | Description |
|---|---|---|
| `plain_password` | `str` | The plain-text password to check |
| `hashed_password` | `str` | The stored hash to verify against |

**Returns:** `bool` — `True` if the password matches, `False` otherwise.

```python
is_valid = verify_password("hunter2", hashed)
```

---

## FastAPI example

```python
from fastapi import FastAPI, HTTPException
from utkit.auth import create_password_hash, verify_password

app = FastAPI()

# Simulate a stored user
db_user = {"username": "alice", "hashed_password": create_password_hash("secret")}


@app.post("/login")
async def login(username: str, password: str):
    if username != db_user["username"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
```
