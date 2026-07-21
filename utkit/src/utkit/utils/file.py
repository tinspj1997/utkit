from collections import defaultdict
import hashlib
import magic
import base64
import mimetypes
from pathlib import Path

def get_file_checksum(file_path, algorithm="sha256", chunk_size=8192):
    """
    Calculate a file checksum by reading the file in chunks.

    Args:
        file_path: Path to the file to checksum
        algorithm: Hash algorithm supported by hashlib (default: "sha256")
        chunk_size: Number of bytes to read at a time

    Returns:
        str: Hex digest of the file checksum
    """
    hasher = hashlib.new(algorithm)

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_file_type(file_path):
    """
    Identify file type based on content using magic numbers.

    Args:
        file_path: Path to the file to identify

    Returns:
        str: File type identifier ("pdf", "docx", "csv", "xlsx", "xls", "png", "jpeg", "jpg", "unknown")
    """
    
    # Read file content
    with open(file_path, "rb") as f:
        data = f.read()

    # Use python-magic to identify file type from content
    mime = magic.Magic(mime=True)
    mime_type = mime.from_buffer(data)

    # Map MIME types to file type identifiers
    mime_to_type = defaultdict(
        lambda: "unknown",
        {
            "application/pdf": "pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
            "text/csv": "csv",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
            "application/vnd.ms-excel": "xls",
            "image/png": "png",
            "image/jpeg": "jpeg",
            "image/jpg": "jpg",
        },
    )

    return mime_to_type[mime_type]


def encode_file(file_path: str | Path) -> dict[str, str]:
    """
    Encode a file as Base64.

    Returns:
    {
        "mime_type": "application/pdf",
        "data": "...",
        "url": "data:application/pdf;base64,..."
    }
    """
    path = Path(file_path)
    mime_type, _ = mimetypes.guess_type(path)
    mime_type = mime_type or "application/octet-stream"
    with path.open("rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return {
        "mime_type": mime_type,
        "data": encoded,
        "url": f"data:{mime_type};base64,{encoded}",
    }