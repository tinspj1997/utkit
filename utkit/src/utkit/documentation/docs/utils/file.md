---
icon: lucide/file
---

# File utilities

The `utkit.utils.file` module provides lightweight helpers for working with files: computing content checksums, identifying file types from binary content, getting file sizes in human-readable units, and encoding files for transfer or display.

---

## Installation

`python-magic` is required for content-based file type detection. Install the `standard` extra:

```bash
pip install "utkit[standard]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[standard]"
```

> `get_file_checksum`, `get_file_size` and `encode_file` use only the Python standard library. `get_file_type` requires `python-magic`.

---

## Quick start

```python
from utkit.utils.file import encode_file, get_file_checksum, get_file_size, get_file_type

# Compute a SHA-256 checksum
checksum = get_file_checksum("report.pdf")
print(checksum)  # "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

# Identify a file type from its content
file_type = get_file_type("report.pdf")
print(file_type)  # "pdf"

# Get the file size in kilobytes
size_kb = get_file_size("report.pdf", unit="KB")
print(size_kb)  # 245.83

# Encode a file as Base64 with MIME type detection
encoded = encode_file("report.pdf")
print(encoded["mime_type"])  # "application/pdf"
print(encoded["url"])        # "data:application/pdf;base64,..."
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

---

## `encode_file`

Encode a file as Base64 and return a dictionary containing the MIME type, encoded content, and a data URL.

```python
def encode_file(file_path: str | Path) -> dict[str, str]
```

| Parameter | Type | Description |
|---|---|---|
| `file_path` | `str \| Path` | Path to the file to encode. |

**Returns:** `dict[str, str]` — A dictionary with three keys:

| Key | Description |
|---|---|
| `mime_type` | MIME type detected from the file extension |
| `data` | Base64-encoded file content |
| `url` | Data URL combining MIME type and encoded content |

### Basic encoding

```python
from utkit.utils.file import encode_file

result = encode_file("document.pdf")
print(result)
# {
#     "mime_type": "application/pdf",
#     "data": "...base64-encoded-content...",
#     "url": "data:application/pdf;base64,..."
# }
```

### Using the data URL

```python
from utkit.utils.file import encode_file

result = encode_file("image.png")
print(f"Data URL: {result['url']}")
# Data URL can be used directly in HTML img tags or other applications
```

---

## `get_file_size`

Return the size of a file in the requested unit. Supports bytes (B), kilobytes (KB), megabytes (MB), gigabytes (GB), and terabytes (TB).

```python
def get_file_size(path: str | Path, unit: SizeUnit = "B", precision: int = 2) -> float
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `path` | `str \| Path` | — | Path to the file. |
| `unit` | `SizeUnit` | `"B"` | Unit of measurement: `"B"`, `"KB"`, `"MB"`, `"GB"`, or `"TB"`. |
| `precision` | `int` | `2` | Number of decimal places to round to. |

**Returns:** `float` — File size in the requested unit.

### Default unit (B)

```python
from utkit.utils.file import get_file_size

size = get_file_size("chart.png")
print(size)  # 145062.83
```

### Custom unit

```python
from utkit.utils.file import get_file_size

size = get_file_size("chart.png", unit="KB")
print(size)  # 1450.63
```

### Custom precision

```python
from utkit.utils.file import get_file_size

size = get_file_size("chart.png", unit="KB", precision=0)
print(size)  # 1451.0
```
