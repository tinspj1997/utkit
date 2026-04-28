from __future__ import annotations
from slowapi import Limiter, _rate_limit_exceeded_handler as rate_limit_exceeded_handler
from slowapi.util import get_remote_address

__all__ = ["initialize_rate_limiter", "rate_limit_exceeded_handler"]


def initialize_rate_limiter(rate_limit_default: str = "100/minute") -> Limiter:
    return Limiter(key_func=get_remote_address, default_limits=[rate_limit_default])
