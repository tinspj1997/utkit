import re


# ------------------------
# Core Mask Functions
# ------------------------

def mask_email(email: str) -> str:
    if not email or "@" not in email:
        return email

    name, domain = email.split("@")

    if len(name) <= 2:
        masked_name = name[0] + "*"
    else:
        masked_name = name[:2] + "*" * (len(name) - 2)

    return f"{masked_name}@{domain}"


def mask_phone(phone: str) -> str:
    if not phone:
        return phone

    digits = re.sub(r"\D", "", phone)

    if len(digits) <= 4:
        return "*" * len(digits)

    return "*" * (len(digits) - 4) + digits[-4:]


def mask_card(card: str) -> str:
    if not card:
        return card

    digits = re.sub(r"\D", "", card)

    if len(digits) < 8:
        return "*" * len(digits)

    return digits[:4] + "*" * (len(digits) - 8) + digits[-4:]


def mask_string(value: str, visible_start: int = 2, visible_end: int = 2) -> str:
    if not value:
        return value

    if len(value) <= visible_start + visible_end:
        return "*" * len(value)

    return (
        value[:visible_start]
        + "*" * (len(value) - visible_start - visible_end)
        + value[-visible_end:]
    )