from __future__ import annotations

import json
from typing import Any, Optional

import redis


class RedisManager:
    _client: Optional[redis.Redis] = None

    def __init__(self, url: str):
        if not RedisManager._client:
            RedisManager._client = redis.from_url(
                url,
                decode_responses=True,  # returns str instead of bytes
            )
        self.client = RedisManager._client

    # ------------------------
    # Basic Operations
    # ------------------------

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        try:
            return self.client.set(name=key, value=json.dumps(value), ex=ttl)
        except Exception as e:
            raise RuntimeError(f"Redis SET failed: {e}") from e

    def get(self, key: str) -> Any:
        try:
            value = self.client.get(name=key)
            return json.loads(value) if value is not None else None
        except Exception as e:
            raise RuntimeError(f"Redis GET failed: {e}") from e

    def delete(self, key: str) -> int:
        try:
            return self.client.delete(key)
        except Exception as e:
            raise RuntimeError(f"Redis DELETE failed: {e}") from e

    def exists(self, key: str) -> bool:
        return self.client.exists(key) == 1

    def expire(self, key: str, ttl: int) -> bool:
        return self.client.expire(key, ttl)


__all__ = ["RedisManager"]
