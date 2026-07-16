---
icon: lucide/file
---

# File utilities

The `utkit.utils.file` module provides lightweight helpers for working with files: computing content checksums and identifying file types from their binary content (magic numbers).

---

## Installation

`python-magic` is part of the optional `standard` extras. Install `utkit` with the `standard` extra for file-type detection support:

```bash
pip install "utkit[standard]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[standard]"
```

> `python-magic` is only required for `get_file_type`. The `get_file_checksum` function relies solely on the standard library (`hashlib`) and has no external dependencies.

---

## Quick start

```python
from utkit.utils.file import get_file_checksum, get_file_type

# Compute a SHA-256 checksum of a file
checksum = get_file_checksum("report.pdf")
print(checksum)  # "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

# Identify a file's type from its content
file_type = get_file_type("report.pdf")
print(file_type)  # "pdf"
```

---

## `get_file_checksum`

Calculate a file checksum by reading the file in chunks. Reading in chunks keeps memory usage low even for very large files.

```python
def get_file_checksum(file_path: str, algorithm: str = "sha256", chunk_size: int = 8192) -> str
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `file_path` | `str` | — | Path to the file to checksum. |
| `algorithm` | `str` | `"sha256"` | Hash algorithm supported by `hashlib` (e.g. `"md5"`, `"sha1"`, `"sha256"`, `"sha512"`). |
| `chunk_size` | `int` | `8192` | Number of bytes to read at a time. |

**Returns:** `str` — Hex digest of the file checksum.

### Default algorithm (SHA-256)

```python
from utkit.utils.file import get_file_checksum

checksum = get_file_checksum("data.csv")
print(checksum)  # "a1b2c3...64-hex-characters"
```

### Custom algorithm

```python
from utkit.utils.file import get_file_checksum

# Use SHA-1 instead of the default SHA-256
checksum = get_file_checksum("data.csv", algorithm="sha1")
print(checksum)  # "da39a3ee5e6b4b0d3255bfef95601890afd80709"
```

### Verifying file integrity

```python
from utkit.utils.file import get_file_checksum

expected = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

if get_file_checksum("report.pdf") == expected:
    print("File is intact")
else:
    print("File has been modified or corrupted")
```

---

## `get_file_type`

Identify a file's type based on its content using magic numbers, rather than its extension. This is more reliable than trusting a file suffix.

```python
def get_file_type(file_path: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `file_path` | `str` | Path to the file to identify. |

**Returns:** `str` — File type identifier. One of: `"pdf"`, `"docx"`, `"csv"`, `"xlsx"`, `"xls"`, `"png"`, `"jpeg"`, `"jpg"`. Returns `"unknown"` for any unrecognised type.

### Identifying a document

```python
from utkit.utils.file import get_file_type

file_type = get_file_type("document.docx")
print(file_type)  # "docx"
```

### Identifying an image

```python
from utkit.utils.file import get_file_type

file_type = get_file_type("photo.jpg")
print(file_type)  # "jpg"
```

### Handling unknown types

```python
from utkit.utils.file import get_file_type

file_type = get_file_type("notes.txt")
print(file_type)  # "unknown" (plain text is not in the recognised set)
```
