---
icon: lucide/check-circle
---

# Validators

The `utkit.validators.data` module provides lightweight string validation and transformation helpers. No external dependencies are required.

---

## Quick start

```python
from utkit.validators import remove_whitespace, is_numeric, slugify

clean = remove_whitespace("  hello world  ")
print(clean)  # "hello world"

is_numeric("12345")  # True
slug = slugify("Hello World!")
print(slug)  # "hello-world"
```

---

## Validation Functions

### `is_alphanumeric`

Check if string contains only alphanumeric characters (letters and digits).

```python
def is_alphanumeric(value: str) -> bool
```

**Returns:** `bool` — True if all characters are alphanumeric, False otherwise.

```python
from utkit.validators import is_alphanumeric

is_alphanumeric("abc123")      # True
is_alphanumeric("hello world") # False (contains space)
is_alphanumeric("hello-123")   # False (contains hyphen)
```

---

### `is_numeric`

Check if string contains only numeric characters (digits).

```python
def is_numeric(value: str) -> bool
```

**Returns:** `bool` — True if all characters are digits, False otherwise.

```python
from utkit.validators import is_numeric

is_numeric("12345")   # True
is_numeric("123.45")  # False (contains decimal point)
is_numeric("abc123")  # False (contains letters)
```

---

### `is_alpha`

Check if string contains only alphabetic characters.

```python
def is_alpha(value: str) -> bool
```

**Returns:** `bool` — True if all characters are alphabetic, False otherwise.

```python
from utkit.validators import is_alpha

is_alpha("hello")     # True
is_alpha("hello123")  # False (contains digits)
is_alpha("hello-world") # False (contains hyphen)
```

---

### `is_empty`

Check if string is empty or contains only whitespace.

```python
def is_empty(value: str) -> bool
```

**Returns:** `bool` — True if empty or only whitespace, False otherwise.

```python
from utkit.validators import is_empty

is_empty("")          # True
is_empty("   ")       # True
is_empty("\t\n")      # True
is_empty("hello")     # False
```

---

### `is_palindrome`

Check if string is a palindrome (ignoring spaces and case).

```python
def is_palindrome(value: str) -> bool
```

**Returns:** `bool` — True if the string reads the same forwards and backwards, False otherwise.

```python
from utkit.validators import is_palindrome

is_palindrome("racecar")           # True
is_palindrome("A man a plan a canal Panama") # True
is_palindrome("hello")             # False
```

---

### `is_title_case`

Check if string is in title case format.

```python
def is_title_case(value: str) -> bool
```

**Returns:** `bool` — True if string is in title case, False otherwise.

```python
from utkit.validators import is_title_case

is_title_case("Hello World")  # True
is_title_case("hello world")  # False
is_title_case("HELLO WORLD")  # False
```

---

## Transformation Functions

### `remove_whitespace`

Remove leading and trailing whitespace from a string.

```python
def remove_whitespace(value: str) -> str
```

**Returns:** `str` — the string with leading and trailing whitespace removed.

```python
from utkit.validators import remove_whitespace

remove_whitespace("  hello world  ")  # "hello world"
remove_whitespace("\tvalue\n")        # "value"
```

---

### `normalize_string`

Normalize string by converting to lowercase and removing extra whitespace.

```python
def normalize_string(value: str) -> str
```

**Returns:** `str` — the normalized string.

```python
from utkit.validators import normalize_string

normalize_string("  HELLO   WORLD  ")  # "hello world"
normalize_string("HeLLo  WoRLd")       # "hello world"
```

---

### `to_lowercase`

Convert string to lowercase.

```python
def to_lowercase(value: str) -> str
```

**Returns:** `str` — the lowercase string.

```python
from utkit.validators import to_lowercase

to_lowercase("HELLO")          # "hello"
to_lowercase("HeLLo WoRLd")    # "hello world"
```

---

### `to_uppercase`

Convert string to uppercase.

```python
def to_uppercase(value: str) -> str
```

**Returns:** `str` — the uppercase string.

```python
from utkit.validators import to_uppercase

to_uppercase("hello")          # "HELLO"
to_uppercase("hello world")    # "HELLO WORLD"
```

---

### `capitalize_string`

Capitalize the first letter of string.

```python
def capitalize_string(value: str) -> str
```

**Returns:** `str` — the string with first letter capitalized.

```python
from utkit.validators import capitalize_string

capitalize_string("hello world")   # "Hello world"
capitalize_string("HELLO")         # "Hello"
```

---

### `slugify`

Convert string to URL-safe slug format.

```python
def slugify(value: str) -> str
```

**Returns:** `str` — the slugified string.

```python
from utkit.validators import slugify

slugify("Hello World!")          # "hello-world"
slugify("Product Name & Price")  # "product-name-price"
slugify("Multiple   Spaces")     # "multiple-spaces"
```

---

### `reverse_string`

Reverse the string.

```python
def reverse_string(value: str) -> str
```

**Returns:** `str` — the reversed string.

```python
from utkit.validators import reverse_string

reverse_string("hello")     # "olleh"
reverse_string("12345")     # "54321"
```

---

### `remove_duplicates`

Remove duplicate characters while preserving order.

```python
def remove_duplicates(value: str) -> str
```

**Returns:** `str` — the string with duplicate characters removed.

```python
from utkit.validators import remove_duplicates

remove_duplicates("aabbcc")     # "abc"
remove_duplicates("hello")      # "helo"
remove_duplicates("mississippi") # "misp"
```

---

### `remove_numbers`

Remove all numeric digits from string.

```python
def remove_numbers(value: str) -> str
```

**Returns:** `str` — the string with all digits removed.

```python
from utkit.validators import remove_numbers

remove_numbers("abc123def456")  # "abcdef"
remove_numbers("test123")       # "test"
remove_numbers("12345")         # ""
```

---

### `remove_vowels`

Remove all vowels from string.

```python
def remove_vowels(value: str) -> str
```

**Returns:** `str` — the string with vowels removed.

```python
from utkit.validators import remove_vowels

remove_vowels("hello")     # "hll"
remove_vowels("programming") # "prgrmmng"
```

---

### `extract_numbers`

Extract all numeric digits from string.

```python
def extract_numbers(value: str) -> str
```

**Returns:** `str` — a string containing only the extracted digits.

```python
from utkit.validators import extract_numbers

extract_numbers("abc123def456")  # "123456"
extract_numbers("test123")       # "123"
extract_numbers("no digits")     # ""
```

---

### `count_words`

Count the number of words in string.

```python
def count_words(value: str) -> int
```

**Returns:** `int` — the number of words.

```python
from utkit.validators import count_words

count_words("hello world")       # 2
count_words("one")               # 1
count_words("multiple  spaces")  # 2
```
