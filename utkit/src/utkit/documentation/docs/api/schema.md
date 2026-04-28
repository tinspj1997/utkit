---
icon: lucide/database
---

# Schema

The `utkit.api.schema` module provides reusable [Pydantic](https://docs.pydantic.dev/) models for common API query patterns.

## Installation

`pydantic` is part of the optional `api` extras. Install `utkit` with the `api` extra:

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
from fastapi import FastAPI, Depends
from utkit.api.schema.query import PaginationParams

app = FastAPI()


@app.get("/items")
async def list_items(pagination: PaginationParams = Depends()):
    return {
        "page": pagination.page,
        "page_size": pagination.page_size,
    }
```

Calling `GET /items?page=2&page_size=20` returns:

```json
{ "page": 2, "page_size": 20 }
```

---

## `PaginationParams`

A Pydantic model for standard page-based pagination query parameters.

```python
class PaginationParams(BaseModel):
    page: int = Field(1, gt=0, description="Page number, starting from 1")
    page_size: int = Field(10, ge=0, description="Number of items per page")
```

| Field | Type | Default | Validation | Description |
|---|---|---|---|---|
| `page` | `int` | `1` | `> 0` | The page number to retrieve, starting from `1` |
| `page_size` | `int` | `10` | `>= 0` | The number of items returned per page |

### Usage with an ORM

```python
from utkit.api.schema.query import PaginationParams

def paginate(query, pagination: PaginationParams):
    offset = (pagination.page - 1) * pagination.page_size
    return query.offset(offset).limit(pagination.page_size)
```
