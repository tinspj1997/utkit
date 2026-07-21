---
icon: lucide/file-text
---

# PDF utilities

The `utkit.utils.pdf` module provides utilities for analyzing and converting PDF documents: detecting page types (images, vector graphics, tables) and rendering pages as images.

---

## Installation

`PyMuPDF` (`fitz`) is required for all PDF operations. Install it with pip:

```bash
pip install utkit[pdf]
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add "utkit[pdf]"
```

> `PyMuPDF` is **not** included in any of the existing extras (`standard`, `store`, `api`). You need to install it separately.

---

## Quick start

```python
from utkit.utils.pdf import analyze_pdf_pages, pdf_to_images

# Analyze a PDF to find pages with images, vectors, or tables
result = analyze_pdf_pages("document.pdf")
print(result)
# {
#     "image_pages": [1, 3],
#     "vector_pages": [2],
#     "table_pages": [4, 5],
#     "vision_pages": [1, 2, 3, 4, 5]
# }

# Convert all pages to PNG images
paths = pdf_to_images("document.pdf", output_dir="pages", dpi=200)
print(paths)  # ["pages/page_1.png", "pages/page_2.png", ...]
```

---

## `analyze_pdf_pages`

Detect different page types in a PDF by scanning each page for embedded images, vector drawings, and tables.

```python
def analyze_pdf_pages(pdf_path: str) -> dict[str, list[int]]
```

| Parameter | Type | Description |
|---|---|---|
| `pdf_path` | `str` | Path to the PDF file to analyze. |

**Returns:** `dict[str, list[int]]` — A dictionary with four keys, each containing a sorted list of 1-based page numbers:

| Key | Description |
|---|---|
| `image_pages` | Pages that contain embedded raster images. |
| `vector_pages` | Pages that contain vector graphics (drawings, shapes). |
| `table_pages` | Pages that contain tabular data detected by PyMuPDF. |
| `vision_pages` | Union of all the above — pages that likely need visual inspection. |

### Basic analysis

```python
from utkit.utils.pdf import analyze_pdf_pages

result = analyze_pdf_pages("report.pdf")
print(result)
# {
#     "image_pages": [1, 3, 7],
#     "vector_pages": [2, 8],
#     "table_pages": [4, 5, 6],
#     "vision_pages": [1, 2, 3, 4, 5, 6, 7, 8]
# }
```

### Filtering pages that need visual processing

```python
from utkit.utils.pdf import analyze_pdf_pages

result = analyze_pdf_pages("document.pdf")

# Pages that contain tables — may need structured extraction
table_pages = result["table_pages"]

# Pages with images or vector graphics — may need OCR
vision_pages = result["vision_pages"]

print(f"Tables found on pages: {table_pages}")
print(f"Vision processing needed for pages: {vision_pages}")
```

---

## `pdf_to_images`

Convert every page of a PDF to a PNG image at the specified DPI. Useful for OCR pipelines, preview generation, or archival purposes.

```python
def pdf_to_images(pdf_path: str, output_dir: str = "pages", dpi: int = 300) -> list[str]
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `pdf_path` | `str` | — | Path to the PDF file to convert. |
| `output_dir` | `str` | `"pages"` | Directory where the PNG images will be saved. Created automatically if it doesn't exist. |
| `dpi` | `int` | `300` | Output resolution in dots per inch. Higher values produce larger, sharper images. |

**Returns:** `list[str]` — List of absolute or relative paths to the generated PNG files, one per page.

### Default conversion (300 DPI)

```python
from utkit.utils.pdf import pdf_to_images

paths = pdf_to_images("document.pdf")
print(paths)
# ["pages/page_1.png", "pages/page_2.png", ...]
```

### Custom output directory and DPI

```python
from utkit.utils.pdf import pdf_to_images

paths = pdf_to_images("scan.pdf", output_dir="output", dpi=150)
print(paths)
# ["output/page_1.png", "output/page_2.png", ...]
```

### Using with `analyze_pdf_pages` for selective conversion

```python
from utkit.utils.pdf import analyze_pdf_pages, pdf_to_images

# First, find which pages need visual processing
result = analyze_pdf_pages("document.pdf")

# Convert only the vision-relevant pages
all_images = pdf_to_images("document.pdf", output_dir="vision_pages")
vision_images = [all_images[i - 1] for i in result["vision_pages"]]

print(f"Converting {len(vision_images)} vision-relevant pages")
for path in vision_images:
    print(path)
```
