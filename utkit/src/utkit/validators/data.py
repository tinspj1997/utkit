def remove_whitespace(value: str) -> str:
    """Remove leading and trailing whitespace from a string."""
    return value.strip()


def normalize_string(value: str) -> str:
    """Normalize string by converting to lowercase and removing extra whitespace."""
    return " ".join(value.lower().split())



def to_lowercase(value: str) -> str:
    """Convert string to lowercase."""
    return value.lower()


def to_uppercase(value: str) -> str:
    """Convert string to uppercase."""
    return value.upper()


def slugify(value: str) -> str:
    """Convert string to URL-safe slug format."""
    import re
    value = value.lower().strip()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[\s-]+', '-', value)
    return value.strip('-')


def is_alphanumeric(value: str) -> bool:
    """Check if string contains only alphanumeric characters."""
    return value.isalnum()





