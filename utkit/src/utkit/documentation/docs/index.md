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

Use `uv version` to increment the package version. For a minor release (e.g. `0.2.0` → `0.3.0`):

```bash
uv version --bump minor
```

Other bump options:

| Command | Example result |
|---|---|
| `uv version --bump patch` | `0.2.0` → `0.2.1` |
| `uv version --bump minor` | `0.2.0` → `0.3.0` |
| `uv version --bump major` | `0.2.0` → `1.0.0` |

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
  utkit-0.3.0-py3-none-any.whl
  utkit-0.3.0.tar.gz
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

