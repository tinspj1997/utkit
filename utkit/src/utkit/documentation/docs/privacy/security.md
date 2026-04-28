---
icon: lucide/lock
---

# Security

The `utkit.privacy.security` module provides cryptographic utilities for symmetric encryption (Fernet), asymmetric encryption (RSA), secure key generation, and JWT token creation and verification.

## Installation

`cryptography` is bundled as a core dependency — no extra installation is required beyond `utkit` itself:

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
import asyncio
from utkit.privacy.security import (
    generate_fernet_key,
    encrypt,
    decrypt,
    generate_secret_key,
)

async def main():
    key = await generate_fernet_key()
    token = await encrypt("hello world", key)
    plain = decrypt(token, key)
    print(plain)  # hello world

asyncio.run(main())
```

---

## Fernet (symmetric)

### `generate_fernet_key`

Generates a new Fernet symmetric encryption key.

```python
async def generate_fernet_key() -> FernetKey
```

**Returns:** `FernetKey` (`bytes`) — a URL-safe base64-encoded 32-byte key.

```python
key = await generate_fernet_key()
```

---

### `encrypt`

Encrypts a plain-text string using a Fernet key.

```python
async def encrypt(content: str, fernet_key: FernetKey) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `content` | `str` | The plain-text string to encrypt |
| `fernet_key` | `FernetKey` | The Fernet key used for encryption |

**Returns:** `str` — the encrypted ciphertext as a UTF-8 string.

**Raises:** `ValueError` — if `content` is not a `str`, or if encryption fails.

```python
cipher = await encrypt("secret data", key)
```

---

### `decrypt`

Decrypts a Fernet-encrypted string.

```python
def decrypt(content: str, fernet_key: FernetKey) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `content` | `str` | The encrypted ciphertext string |
| `fernet_key` | `FernetKey` | The Fernet key used for decryption |

**Returns:** `str` — the original plain-text string.

**Raises:** `ValueError` — if `content` is not a `str`, or if the key is invalid / data is corrupted.

```python
plain = decrypt(cipher, key)
```

---

## RSA (asymmetric)

### `generate_rsa_keys`

Generates an RSA private/public key pair and saves both to PEM files on disk.

```python
def generate_rsa_keys(
    key_size: int = 2048,
    private_key_path: str = "private_key.pem",
    public_key_path: str = "public_key.pem",
) -> tuple[str, str]
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `key_size` | `int` | `2048` | RSA key size in bits |
| `private_key_path` | `str` | `"private_key.pem"` | Output path for the private key PEM file |
| `public_key_path` | `str` | `"public_key.pem"` | Output path for the public key PEM file |

**Returns:** `tuple[str, str]` — `(private_key_path, public_key_path)`.

```python
priv, pub = generate_rsa_keys(key_size=4096)
```

---

### `load_rsa_public_key`

Loads an RSA public key from a PEM file.

```python
def load_rsa_public_key(public_key_path: str)
```

**Returns:** An RSA public key object from `cryptography`.

---

### `load_rsa_private_key`

Loads an RSA private key from a PEM file (no passphrase).

```python
def load_rsa_private_key(private_key_path: str)
```

**Returns:** An RSA private key object from `cryptography`.

---

### `encrypt_rsa_content`

Encrypts content using RSA-OAEP with SHA-256.

```python
def encrypt_rsa_content(content: str | bytes, public_key_path: str) -> bytes
```

| Parameter | Type | Description |
|---|---|---|
| `content` | `str \| bytes` | The data to encrypt |
| `public_key_path` | `str` | Path to the PEM public key file |

**Returns:** `bytes` — RSA-encrypted ciphertext.

```python
encrypted = encrypt_rsa_content("top secret", "public_key.pem")
```

---

### `decrypt_rsa_content`

Decrypts RSA-OAEP-encrypted bytes using a private key.

```python
def decrypt_rsa_content(encrypted_content: bytes, private_key_path: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `encrypted_content` | `bytes` | The RSA-encrypted ciphertext |
| `private_key_path` | `str` | Path to the PEM private key file |

**Returns:** `str` — the decrypted plain-text string.

```python
plain = decrypt_rsa_content(encrypted, "private_key.pem")
```

---

## Secret key generation

### `generate_secret_key`

Generates a cryptographically secure random hex string.

```python
def generate_secret_key(byte_length: int = 32) -> str
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `byte_length` | `int` | `32` | Number of random bytes — the resulting hex string is twice this length |

**Returns:** `str` — a hex-encoded random string (e.g., 64 characters for the default 32 bytes).

```python
secret = generate_secret_key()       # 64-char hex string
short  = generate_secret_key(16)     # 32-char hex string
```

---

## JWT

`pyjwt` is a core dependency — no extra installation required.

### `create_access_token`

Creates a signed JWT access token with an expiry claim.

```python
def create_access_token(
    data: dict,
    secret_key: str,
    algorithm: str = "HS256",
    expires_delta: timedelta | None = None,
) -> str
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `data` | `dict` | — | Payload claims to encode (e.g. `{"sub": "user_id"}`) |
| `secret_key` | `str` | — | Secret used to sign the token |
| `algorithm` | `str` | `"HS256"` | JWT signing algorithm |
| `expires_delta` | `timedelta \| None` | `None` | Token lifetime. Defaults to 15 minutes if not provided. |

**Returns:** `str` — the signed JWT string.

```python
from datetime import timedelta
from utkit.privacy.security import create_access_token, generate_secret_key

secret = generate_secret_key()
token = create_access_token(
    data={"sub": "user_123", "role": "admin"},
    secret_key=secret,
    expires_delta=timedelta(hours=1),
)
```

---

### `decode_token`

Decodes and verifies a JWT token, returning the payload.

```python
def decode_token(
    token: str,
    secret_key: str,
    algorithm: str = "HS256",
) -> dict
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `token` | `str` | — | The JWT string to decode |
| `secret_key` | `str` | — | Secret used to verify the token signature |
| `algorithm` | `str` | `"HS256"` | JWT signing algorithm |

**Returns:** `dict` — the decoded payload claims.

**Raises:**
- `ValueError("Token has expired.")` — if the token's `exp` claim is in the past
- `ValueError("Invalid token: ...")` — if the signature is invalid or the token is malformed

```python
from utkit.privacy.security import decode_token

payload = decode_token(token, secret_key=secret)
print(payload["sub"])   # "user_123"
print(payload["role"])  # "admin"
```

