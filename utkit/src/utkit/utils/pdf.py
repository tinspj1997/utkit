import fitz
import os

def analyze_pdf_pages(pdf_path: str) -> dict[str, list[int]]:
    """
    Detect different page types in a PDF.

    Returns:
    {
        "image_pages": [...],
        "vector_pages": [...],
        "table_pages": [...],
        "vision_pages": [...]
    }
    """

    image_pages = set()
    vector_pages = set()
    table_pages = set()

    with fitz.open(pdf_path) as doc:
        for page_number, page in enumerate(doc, start=1):
            # Embedded images
            if page.get_images(full=True):
                image_pages.add(page_number)

            # Vector graphics
            if page.get_drawings():
                vector_pages.add(page_number)

            # Tables
            if page.find_tables().tables:
                table_pages.add(page_number)

    vision_pages = sorted(
        image_pages | vector_pages | table_pages
    )

    return {
        "image_pages": sorted(image_pages),
        "vector_pages": sorted(vector_pages),
        "table_pages": sorted(table_pages),
        "vision_pages": vision_pages,
    }


def pdf_to_images(pdf_path, output_dir="pages", dpi=300):
    os.makedirs(output_dir, exist_ok=True)
    paths = []
    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=dpi)
            path = f"{output_dir}/page_{i+1}.png"
            pix.save(path)
            paths.append(path)

    return paths