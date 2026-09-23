#!/usr/bin/env python3
"""
extract_pdf_text.py

Extracts text from a PDF file and saves it to a .txt file.
The extracted text can then be used as a base for writing slides.

Command-line usage:
    python extract_pdf_text.py lecture.pdf
    python extract_pdf_text.py lecture.pdf -o extracted_text.txt
    python extract_pdf_text.py lecture.pdf --per-page

Requires the "pypdf" library:
    pip install pypdf
"""

import argparse
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: the 'pypdf' library is not installed.")
    print("Install it with:  pip install pypdf")
    sys.exit(1)


def extract_text(pdf_path: Path, per_page: bool = False) -> str:
    """
    Extracts text from all pages of a PDF.

    Args:
        pdf_path: path to the input PDF file.
        per_page: if True, inserts a separator with the page
                  number before the text of each page.

    Returns:
        The extracted text as a single string.
    """
    reader = PdfReader(str(pdf_path))
    text_parts = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        page_text = page_text.strip()

        if per_page:
            header = f"\n{'=' * 40}\nPAGE {page_number}\n{'=' * 40}\n"
            text_parts.append(header + page_text)
        else:
            text_parts.append(page_text)

    return "\n\n".join(text_parts)


def main():
    parser = argparse.ArgumentParser(
        description="Extracts text from a PDF and saves it to a .txt file"
    )
    parser.add_argument(
        "input_pdf",
        type=Path,
        help="Path to the PDF file to extract text from"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Path to the output .txt file (default: same name as the PDF)"
    )
    parser.add_argument(
        "--per-page",
        action="store_true",
        help="Adds a header with the page number before each text section"
    )

    args = parser.parse_args()

    if not args.input_pdf.exists():
        print(f"Error: the file '{args.input_pdf}' does not exist.")
        sys.exit(1)

    if args.input_pdf.suffix.lower() != ".pdf":
        print("Warning: the given file does not have a .pdf extension, proceeding anyway.")

    output_path = args.output or args.input_pdf.with_suffix(".txt")

    print(f"Extracting text from: {args.input_pdf}")
    text = extract_text(args.input_pdf, per_page=args.per_page)

    if not text.strip():
        print("Warning: no text was extracted. "
              "The PDF might contain only images (scans) "
              "and require OCR to extract text.")

    output_path.write_text(text, encoding="utf-8")
    print(f"Done! Text saved to: {output_path}")


if __name__ == "__main__":
    main()
