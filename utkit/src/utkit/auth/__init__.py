from __future__ import annotations

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

__all__ = [
    "verify_password","create_password_hash"
]

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def create_password_hash(password):
    return password_hash.hash(password)