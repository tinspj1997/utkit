---
icon: lucide/scroll-text
---

# Logging

The `utkit.core.logging` module provides a structured, opinionated logging setup built on top of [Loguru](https://github.com/Delgan/loguru). It configures console output, rotating application logs, and metering logs — all with a consistent format that includes timestamps, log levels, class/function context, and structured extras.

No external dependencies beyond `loguru` are required.

---

## Quick start

```python
from utkit.core.logging import setup_logging
from loguru import logger

setup_logging(log_base_path="logs")

logger.bind(type="app").info("Server started")
logger.bind(type="meter").info("Request count: 42")
```

---

## `setup_logging`

Configures Loguru with console, application, and metering log sinks.

```python
def setup_logging(
    log_base_path: str = "logs",
    patchers: List[Callable] = [],
    rotation: str = "1 day",
    compression: str = "zip",
    level: str = "INFO",
    app_retention: str = "7 days",
    meter_retention: str = "30 days",
    **kwargs,
) -> None
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `log_base_path` | `str` | `"logs"` | Directory where log files are written. Created automatically if it does not exist. |
| `patchers` | `List[Callable]` | `[]` | Additional patcher callables applied to every log record before formatting. Each callable receives the `record` dict and may mutate it in place. |
| `rotation` | `str` | `"1 day"` | Loguru rotation policy for file sinks (e.g. `"500 MB"`, `"1 week"`). |
| `compression` | `str` | `"zip"` | Compression format applied to rotated log files (e.g. `"gz"`, `"bz2"`). |
| `level` | `str` | `"INFO"` | Minimum log level written to file sinks. |
| `app_retention` | `str` | `"7 days"` | Retention period for application log files. |
| `meter_retention` | `str` | `"30 days"` | Retention period for metering log files. |
| `**kwargs` | | | Any additional keyword arguments are forwarded to all file sinks (e.g. `enqueue=True` for thread-safe async logging). |

**Returns:** `None`

### Log sinks

| Sink | Filter | Files |
|---|---|---|
| Console (`stderr`) | All records at `INFO` and above | — |
| Application | `record["extra"]["type"] == "app"` | `logs/application_YYYY-MM-DD.log` |
| Metering | `record["extra"]["type"] == "meter"` | `logs/metering_YYYY-MM-DD.log` |

Route a record to a specific sink by binding the `type` key:

```python
logger.bind(type="app").info("User signed in", user_id=42)
logger.bind(type="meter").info("API call", endpoint="/health")
```

Records without a `type` binding appear only in the console sink.

### Log format

All sinks share a consistent format:

```
YYYY-MM-DD HH:mm:ss | LEVEL    | module:ClassName:function:line | message | Context: {extra}
```

### Example

```python
from utkit.core.logging import setup_logging
from loguru import logger

setup_logging(
    log_base_path="var/logs",
    rotation="500 MB",
    compression="gz",
    level="DEBUG",
    app_retention="14 days",
    meter_retention="60 days",
    enqueue=True,   # thread-safe async logging
)

logger.bind(type="app").info("Application boot complete")
logger.bind(type="meter").debug("Cache hit", key="user:123")
```

---

## Custom patchers

Pass a list of callables to `patchers` to enrich every log record with additional context. Each callable receives the mutable `record` dict.

```python
def add_request_id(record):
    record["extra"]["request_id"] = get_current_request_id()

setup_logging(patchers=[add_request_id])
```

The built-in `_add_class_name` patcher is always appended last. It walks the call stack to detect the calling class and stores its name in `record["extra"]["classname"]`, which is rendered as part of the log format.

```python
class MyService:
    def process(self):
        logger.bind(type="app").info("Processing")
        # → ... | MyService:process:42 | Processing | ...
```

---

## Thread safety

Pass `enqueue=True` as a keyword argument to make all file sinks non-blocking and safe for multi-threaded or multi-process applications:

```python
setup_logging(enqueue=True)
```
