---
icon: lucide/scroll-text
---

# Logging

The `utkit.core.logging` module provides structured, file-based logging built on top of [Loguru](https://github.com/Delgan/loguru). It supports daily log rotation, compression, separate application and metering log streams, and automatic class-name injection into log records.

## Installation

`loguru` is bundled as a core dependency — no extra installation is required beyond `utkit` itself:

```bash
pip install utkit
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add utkit
```

---

## Quick start

```python
from utkit.core.logging import setup_logging
from loguru import logger

setup_logging(log_base_path="logs")

logger.bind(type="app").info("Application started")
logger.bind(type="meter").info("Metering event recorded")
```

Log files are written to the `logs/` directory:

```
logs/
  application_2026-04-28.log
  metering_2026-04-28.log
```

---

## `setup_logging`

Configures Loguru sinks for console output, application logs, and metering logs.

```python
def setup_logging(
    log_base_path: str = "logs",
    patchers: list[Callable] = [],
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
| `log_base_path` | `str` | `"logs"` | Base directory where log files are created |
| `patchers` | `list[Callable]` | `[]` | Additional patcher functions applied to each log record |
| `rotation` | `str` | `"1 day"` | Loguru rotation interval (e.g. `"500 MB"`, `"1 week"`) |
| `compression` | `str` | `"zip"` | Compression format for rotated files (`"zip"`, `"gz"`, etc.) |
| `level` | `str` | `"INFO"` | Minimum log level for file sinks |
| `app_retention` | `str` | `"7 days"` | Retention period for `application_*.log` files |
| `meter_retention` | `str` | `"30 days"` | Retention period for `metering_*.log` files |
| `**kwargs` | | | Extra keyword arguments forwarded to each Loguru file sink |

**Returns:** `None`

---

## Log streams

`setup_logging` creates three sinks:

| Sink | Filter | Retention |
|---|---|---|
| **Console** (`stderr`) | All records at `INFO` and above | — |
| **Application log** (`application_YYYY-MM-DD.log`) | Records where `extra["type"] == "app"` | `app_retention` |
| **Metering log** (`metering_YYYY-MM-DD.log`) | Records where `extra["type"] == "meter"` | `meter_retention` |

Use `logger.bind(type="app")` or `logger.bind(type="meter")` to route records to the correct file sink:

```python
logger.bind(type="app").info("User logged in", user_id=42)
logger.bind(type="meter").info("API call", endpoint="/users")
```

---

## Log format

Each log line follows this structured format:

```
YYYY-MM-DD HH:mm:ss | LEVEL    | module:ClassName:function:line | message | Context: {...}
```

Example:

```
2026-04-28 12:00:00 | INFO     | myapp.service:UserService:login:45 | User logged in | Context: {'type': 'app', 'user_id': 42}
```

---

## Custom patchers

You can inject additional fields into log records by passing patcher functions:

```python
def add_request_id(record):
    record["extra"].setdefault("request_id", "n/a")

setup_logging(patchers=[add_request_id])
```

The built-in `_add_class_name` patcher runs automatically and populates `extra["classname"]` from the calling class (or `"Global"` for module-level calls).
