---
icon: lucide/rocket
---

# Get started

**utkit** is a collection of core libraries for Python development, providing ready-to-use utilities for common tasks such as sending email, and more.

- **Version:** `0.2.0`
- **Author:** TINS PJ
- **Requires:** Python `>=3.12`
- **License:** MIT
- **PyPI:** [pypi.org/project/utkit](https://pypi.org/project/utkit/)

---

## Installation

Install utkit from PyPI using pip:

```bash
pip install utkit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add utkit
```

Verify the installed version:

```bash
utkit --version
```

---

## Requirements

| Dependency | Version |
|---|---|
| Python | `>=3.12` |
| typer | `>=0.20.0` |

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

| Module | Description |
|---|---|
| [`communication.mail`](communication/mail.md) | Send HTML emails via SMTP |

