---
icon: lucide/timer
---

# Performance

The `utkit.utils.performance` module provides lightweight utilities for measuring function execution time and monitoring memory usage.

## Installation

`psutil` is part of the optional `standard` extras. Install `utkit` with the `standard` extra for memory tracking support:

```bash
pip install "utkit[standard]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[standard]"
```

> `psutil` is only required for `get_memory_usage_mb`. The `time_checker` decorator has no external dependencies.

---

## Quick start

```python
from utkit.utils.performance import time_checker, get_memory_usage_mb

@time_checker
def compute(n: int) -> int:
    return sum(range(n))

result = compute(1_000_000)
# [compute] executed in 0.0321 seconds

mem = get_memory_usage_mb()
print(f"Memory usage: {mem:.2f} MB")
```

---

## `time_checker`

A decorator that prints the wall-clock execution time of a function after each call. Works with both regular and `async` functions.

```python
def time_checker(func: Callable) -> Callable
```

| Parameter | Type | Description |
|---|---|---|
| `func` | `Callable` | The function to wrap. Can be synchronous or asynchronous. |

**Returns:** The wrapped function with the same signature.

**Output format:**

```
[<function_name>] executed in <seconds> seconds
```

### Synchronous usage

```python
from utkit.utils.performance import time_checker

@time_checker
def slow_task():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

slow_task()
# [slow_task] executed in 0.5123 seconds
```

### Async usage

```python
import asyncio
from utkit.utils.performance import time_checker

@time_checker
async def async_task():
    await asyncio.sleep(0.1)

asyncio.run(async_task())
# [async_task] executed in 0.1003 seconds
```

---

## `get_memory_usage_mb`

Returns the current resident set size (RSS) memory usage of the running process in megabytes.

```python
def get_memory_usage_mb() -> float
```

**Returns:** `float` — current memory usage in MB.

**Requires:** `psutil`

```python
from utkit.utils.performance import get_memory_usage_mb

before = get_memory_usage_mb()
data = [i for i in range(1_000_000)]
after = get_memory_usage_mb()

print(f"Memory delta: {after - before:.2f} MB")
```
