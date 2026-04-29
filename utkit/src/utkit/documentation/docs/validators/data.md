---
icon: lucide/check-circle
---

# Validators

The `utkit.validators.data` module provides lightweight string validation and sanitization helpers. No external dependencies are required.

---

## Quick start

```python
from utkit.validators import remove_whitespace

clean = remove_whitespace("  hello world  ")
print(clean)  # "hello world"
```

---

## `remove_whitespace`

Removes leading and trailing whitespace from a string.

```python
def remove_whitespace(value: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `value` | `str` | The input string to sanitize. |

**Returns:** `str` — the input string with leading and trailing whitespace removed.

| Input | Output |
|---|---|
| `"  hello  "` | `"hello"` |
| `"\t data\n"` | `"data"` |
| `"no change"` | `"no change"` |
| `"   "` | `""` |

```python
from utkit.validators import remove_whitespace

remove_whitespace("  Jane Doe  ")   # "Jane Doe"
remove_whitespace("\tvalue\n")       # "value"
```
