# Validation functions
def is_alphanumeric(value: str) -> bool:
    """Check if string contains only alphanumeric characters."""
    return value.isalnum()


def is_numeric(value: str) -> bool:
    """Check if string contains only numeric characters."""
    return value.isdigit()


def is_alpha(value: str) -> bool:
    """Check if string contains only alphabetic characters."""
    return value.isalpha()


def is_empty(value: str) -> bool:
    """Check if string is empty or contains only whitespace."""
    return not value or value.isspace()


def is_palindrome(value: str) -> bool:
    """Check if string is a palindrome (ignoring spaces and case)."""
    cleaned = value.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def is_title_case(value: str) -> bool:
    """Check if string is in title case."""
    return value == value.title()


# Transformation functions
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


def capitalize_string(value: str) -> str:
    """Capitalize first letter of string."""
    return value.capitalize()


def slugify(value: str) -> str:
    """Convert string to URL-safe slug format."""
    import re
    value = value.lower().strip()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[\s-]+', '-', value)
    return value.strip('-')


def reverse_string(value: str) -> str:
    """Reverse the string."""
    return value[::-1]


def remove_duplicates(value: str) -> str:
    """Remove duplicate characters while preserving order."""
    seen = set()
    return "".join(char for char in value if not (char in seen or seen.add(char)))


def remove_numbers(value: str) -> str:
    """Remove all numeric digits from string."""
    return "".join(char for char in value if not char.isdigit())


def remove_vowels(value: str) -> str:
    """Remove all vowels from string."""
    vowels = "aeiouAEIOU"
    return "".join(char for char in value if char not in vowels)


def extract_numbers(value: str) -> str:
    """Extract all numeric digits from string."""
    return "".join(char for char in value if char.isdigit())


def count_words(value: str) -> int:
    """Count number of words in string."""
    return len(value.split())

