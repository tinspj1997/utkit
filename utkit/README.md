# utkit

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="https://res.cloudinary.com/daft06bly/image/upload/v1777439163/logo_wussdc.png" alt="utkit" style="height: 100px; width: auto;" />
</div>

**utkit** is a collection of core libraries for Python development, providing ready-to-use utilities for common tasks such as authentication, email, encryption, caching, rate limiting, and more.

- **Version:** `0.4.0`
- **Author:** TINS PJ
- **Requires:** Python `>=3.12`
- **License:** MIT
- **PyPI:** [pypi.org/project/utkit](https://pypi.org/project/utkit/)

---

## Installation

```bash
pip install utkit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add utkit
```

### Optional extras

| Extra | Included dependencies | Use for |
|---|---|---|
| `api` | `slowapi`, `pydantic` | Rate limiting and API schema for FastAPI |
| `standard` | `psutil`, `jinja2` | Performance monitoring and HTML template rendering |
| `store` | `redis` | Redis cache and key-value store |
| `all` | all of the above | Install every optional dependency at once |

```bash
pip install "utkit[api]"
pip install "utkit[standard]"
pip install "utkit[store]"

# All optional dependencies at once
pip install "utkit[all]"
```

---

## Modules

### Core

| Module | Description |
|---|---|
| `auth` | Password hashing and verification |
| `communication.mail` | Send HTML emails via SMTP |
| `privacy.mask` | Mask sensitive data (email, phone, card, string) |
| `privacy.security` | Fernet & RSA encryption, secret key generation, JWT |

### Optional

| Module | Extra | Description |
|---|---|---|
| `api.rate_limit` | `api` | Rate limiting for FastAPI via SlowAPI |
| `api.schema` | `api` | Reusable Pydantic query models (pagination) |
| `utils.performance` | `standard` | Execution time decorator and memory usage |
| `template.render` | `standard` | HTML rendering from Jinja2 files and strings |
| `store.redis` | `store` | Singleton Redis client with JSON serialisation |

---

## CLI

```bash
utkit --version
utkit docs
```
