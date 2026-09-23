#!/usr/bin/env python3
"""Extracts a range of pages from a PDF.

Usage:
    python extract_pages.py file.pdf start_page end_page [output.pdf]

Pages are numbered starting from 1 and the range is inclusive.
Requirement: pip install pypdf
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) < 4:
        sys.exit("Usage: python extract_pages.py file.pdf start_page end_page [output.pdf]")

    path = Path(sys.argv[1])
    start, end = int(sys.argv[2]), int(sys.argv[3])
    output = Path(sys.argv[4]) if len(sys.argv) > 4 else path.with_name(f"{path.stem}_p{start}-{end}.pdf")

    reader = PdfReader(path)
    total = len(reader.pages)

    if not (1 <= start <= end <= total):
        sys.exit(f"Invalid range: the PDF has {total} pages (requested {start}-{end}).")

    writer = PdfWriter()
    for i in range(start - 1, end):
        writer.add_page(reader.pages[i])

    with open(output, "wb") as f:
        writer.write(f)

    print(f"Saved pages {start}-{end} to: {output}")


if __name__ == "__main__":
    main()
