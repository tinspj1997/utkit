---
icon: lucide/eye-off
---

# Masking

The `utkit.core.mask` module provides utilities for masking sensitive data such as email addresses, phone numbers, payment card numbers, and arbitrary strings before displaying or logging them.

No external dependencies are required — the module uses Python's built-in `re` library.

---

## Quick start

```python
from utkit.core.mask import mask_email, mask_phone, mask_card, mask_string

mask_email("john.doe@example.com")   # "jo******@example.com"
mask_phone("+1 (555) 123-4567")      # "*******4567"
mask_card("4111 1111 1111 1111")     # "4111********1111"
mask_string("Hello, World!")         # "He*********d!"
```

---

## `mask_email`

Masks the local part of an email address, keeping the first two characters visible.

```python
def mask_email(email: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `email` | `str` | The email address to mask |

**Returns:** `str` — the masked email address. Returns the original value unchanged if it is empty or does not contain `@`.

| Input | Output |
|---|---|
| `"john.doe@example.com"` | `"jo******@example.com"` |
| `"ab@example.com"` | `"a*@example.com"` |
| `"a@example.com"` | `"a*@example.com"` |

```python
mask_email("john.doe@example.com")  # "jo******@example.com"
```

---

## `mask_phone`

Masks a phone number, keeping only the last 4 digits visible. Non-digit characters are stripped before masking.

```python
def mask_phone(phone: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `phone` | `str` | The phone number to mask (any format) |

**Returns:** `str` — the masked phone number. Returns the original value unchanged if it is empty.

| Input | Output |
|---|---|
| `"+1 (555) 123-4567"` | `"*******4567"` |
| `"07911123456"` | `"*******3456"` |
| `"1234"` | `"****"` |

```python
mask_phone("+1 (555) 123-4567")  # "*******4567"
```

---

## `mask_card`

Masks a payment card number, keeping the first 4 and last 4 digits visible. Non-digit characters are stripped before masking.

```python
def mask_card(card: str) -> str
```

| Parameter | Type | Description |
|---|---|---|
| `card` | `str` | The card number to mask (any format) |

**Returns:** `str` — the masked card number. Returns the original value unchanged if it is empty.

| Input | Output |
|---|---|
| `"4111 1111 1111 1111"` | `"4111********1111"` |
| `"378282246310005"` | `"3782*******0005"` |

```python
mask_card("4111 1111 1111 1111")  # "4111********1111"
```

---

## `mask_string`

Masks an arbitrary string, keeping a configurable number of characters visible at the start and end.

```python
def mask_string(value: str, visible_start: int = 2, visible_end: int = 2) -> str
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `value` | `str` | — | The string to mask |
| `visible_start` | `int` | `2` | Number of characters to keep visible at the start |
| `visible_end` | `int` | `2` | Number of characters to keep visible at the end |

**Returns:** `str` — the masked string. If the value is shorter than or equal to `visible_start + visible_end`, the entire string is masked with `*`. Returns the original value unchanged if it is empty.

| Input | `visible_start` | `visible_end` | Output |
|---|---|---|---|
| `"Hello, World!"` | `2` | `2` | `"He*********d!"` |
| `"API-KEY-12345"` | `3` | `3` | `"API*******345"` |
| `"abc"` | `2` | `2` | `"***"` |

```python
mask_string("Hello, World!")            # "He*********d!"
mask_string("API-KEY-12345", 3, 3)      # "API*******345"
```
