---
icon: lucide/rocket
---

# Get started

<div style="text-align: center; margin: 1.5rem 0;">
  <img src="images/logo.png" alt="utkit" style="height: 100px; width: auto;" />
</div>

**utkit** is a collection of core libraries for Python development, providing ready-to-use utilities for common tasks such as authentication, email, encryption, caching, rate limiting, and more.

- **Version:** `0.4.0`
- **Author:** TINS PJ
- **Requires:** Python `>=3.12`
- **License:** MIT
- **PyPI:** [pypi.org/project/utkit](https://pypi.org/project/utkit/)

---

## Installation

Install the base package from PyPI:

```bash
pip install utkit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add utkit
```

### Optional extras

utkit ships optional extras for additional functionality. Install only the extras you need:

| Extra | Included dependencies | Use for |
|---|---|---|
| `api` | `slowapi`, `pydantic` | Rate limiting and API schema for FastAPI |
| `standard` | `psutil`, `jinja2` | Performance monitoring and HTML template rendering |
| `store` | `redis` | Redis cache and key-value store |
| `all` | all of the above | Install every optional dependency at once |

**pip:**

```bash
pip install "utkit[api]"
pip install "utkit[standard]"
pip install "utkit[store]"

# All optional dependencies at once
pip install "utkit[all]"
```

**uv:**

```bash
uv add "utkit[api]"
uv add "utkit[standard]"
uv add "utkit[store]"

# All optional dependencies at once
uv add "utkit[all]"
```

Verify the installed version:

```bash
utkit --version
```

---

## Requirements

### Core dependencies

| Dependency | Version | Purpose |
|---|---|---|
| Python | `>=3.12` | Runtime |
| typer | `>=0.20.0` | CLI framework |
| cryptography | `>=47.0.0` | Fernet & RSA encryption |
| loguru | `>=0.7.3` | Logging |
| pwdlib\[argon2\] | `>=0.3.0` | Password hashing |
| pyjwt | `>=2.12.1` | JWT token creation & verification |
| zensical | `>=0.0.37` | Documentation server |

### Optional dependencies

| Extra | Dependency | Version |
|---|---|---|
| `api` | slowapi | `>=0.1.9` |
| `api` | pydantic | `>=2.13.3` |
| `standard` | psutil | `>=7.2.2` |
| `standard` | jinja2 | `>=3.1.6` |
| `standard` | python-magic | `>=0.4.27` |
| `store` | redis | `>=7.4.0` |
| `all` | all of the above | — |

---

## CLI

utkit ships with a command-line interface.

```bash
# Show version
utkit --version
utkit version

# Serve documentation locally on port 8005
utkit docs
```

---

## Modules

### Core modules

| Module | Description |
|---|---|
| [`auth`](auth.md) | Password hashing and verification |
| [`communication.mail`](communication/mail.md) | Send HTML emails via SMTP |
| [`privacy.mask`](privacy/mask.md) | Mask sensitive data (email, phone, card, string) |
| [`privacy.security`](privacy/security.md) | Fernet & RSA encryption, secret key generation, JWT |

### Optional modules

| Module | Extra | Description |
|---|---|---|
| [`api.rate_limit`](api/rate-limit.md) | `api` | Rate limiting for FastAPI via SlowAPI |
| [`api.schema`](api/schema.md) | `api` | Reusable Pydantic query models (pagination) |
| [`utils.performance`](utils/performance.md) | `standard` | Execution time decorator and memory usage || [`utils.file`](utils/file.md) | `standard` | File checksum and content-based type detection || [`template.render`](template/render.md) | `standard` | HTML rendering from Jinja2 files and strings |
| [`store.redis`](store/redis.md) | `store` | Singleton Redis client with JSON serialisation |

---

## Package Development Guide

This section covers the workflow for developing and publishing utkit using [uv](https://docs.astral.sh/uv/).

### Upgrade the package in a project

To pull the latest published version of utkit into a project:

```bash
uv add utkit --upgrade
```

This updates `utkit` to the newest available version on PyPI and syncs the lockfile.

---

### Bump the version

Use `uv version` to increment the package version. For a minor release (e.g. `0.3.0` → `0.4.0`):

```bash
uv version --bump minor
```

Other bump options:

| Command | Example result |
|---|---|
| `uv version --bump patch` | `0.4.0` → `0.4.1` |
| `uv version --bump minor` | `0.4.0` → `0.5.0` |
| `uv version --bump major` | `0.4.0` → `1.0.0` |

This updates the `version` field in `pyproject.toml` automatically.

---

### Build the package

Compile the distribution artifacts (wheel + sdist):

```bash
uv build
```

Output is placed in the `dist/` folder:

```
dist/
  utkit-0.4.0-py3-none-any.whl
  utkit-0.4.0.tar.gz
```

---

### Full release workflow

```bash
# 1. Bump version
uv version --bump minor

# 2. Build distribution
uv build

# 3. Publish to PyPI
uv publish
```

