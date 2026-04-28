---
icon: lucide/gauge
---

# Rate Limiting

The `utkit.api.rate_limit` module provides rate limiting utilities for [FastAPI](https://fastapi.tiangolo.com/) applications, built on top of [SlowAPI](https://github.com/laurentS/slowapi).

## Installation

`slowapi` is part of the optional `api` extras. Install `utkit` with the `api` extra:

```bash
pip install "utkit[api]"
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[api]"
```

---

## Quick start

```python
from fastapi import FastAPI, Request
from utkit.api.rate_limit import initialize_rate_limiter, rate_limit_exceeded_handler
from utkit.api.rate_limit.middleware import RateLimitMiddleware
from utkit.api.rate_limit.error import RateLimitExceededError

limiter = initialize_rate_limiter("60/minute")

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceededError, rate_limit_exceeded_handler)
app.add_middleware(RateLimitMiddleware)


@app.get("/ping")
@limiter.limit("10/minute")
async def ping(request: Request):
    return {"message": "pong"}
```

---

## `initialize_rate_limiter`

Creates a `Limiter` instance configured to use the client's remote IP address as the rate limit key.

```python
def initialize_rate_limiter(rate_limit_default: str = "100/minute") -> Limiter
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `rate_limit_default` | `str` | `"100/minute"` | The default rate limit applied to all routes. Accepts SlowAPI limit strings such as `"100/minute"`, `"1000/hour"`, `"10/second"` |

**Returns:** `Limiter` — a configured SlowAPI `Limiter` instance.

```python
limiter = initialize_rate_limiter("200/minute")
```

---

## `rate_limit_exceeded_handler`

A pre-built exception handler that returns a `429 Too Many Requests` response when a rate limit is exceeded. Import it and register it directly on your FastAPI app.

```python
app.add_exception_handler(RateLimitExceededError, rate_limit_exceeded_handler)
```

---

## `RateLimitMiddleware`

ASGI middleware that intercepts rate-limit exceptions raised during request processing. Add it to your FastAPI app via `add_middleware`.

```python
from utkit.api.rate_limit.middleware import RateLimitMiddleware

app.add_middleware(RateLimitMiddleware)
```

This is a re-export of `slowapi.middleware.SlowAPIMiddleware`.

---

## `RateLimitExceededError`

Exception raised when a request exceeds the configured rate limit.

```python
from utkit.api.rate_limit.error import RateLimitExceededError
```

Use this as the exception type when registering the error handler:

```python
app.add_exception_handler(RateLimitExceededError, rate_limit_exceeded_handler)
```

This is a re-export of `slowapi.errors.RateLimitExceeded`.

---

## Rate limit string format

SlowAPI accepts human-readable limit strings:

| String | Meaning |
|---|---|
| `"10/second"` | 10 requests per second |
| `"100/minute"` | 100 requests per minute |
| `"1000/hour"` | 1 000 requests per hour |
| `"10000/day"` | 10 000 requests per day |
