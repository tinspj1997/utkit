from collections import defaultdict

import magic


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
