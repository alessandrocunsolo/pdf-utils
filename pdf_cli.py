#!/usr/bin/env python3
"""
pdf_cli.py

Unified command-line entry point for the pdf-utils scripts.
Dispatches to the individual scripts (extract_pages.py, extract_pdf_text.py)
which remain usable on their own.

Usage:
    python pdf_cli.py pages file.pdf start_page end_page [output.pdf]
    python pdf_cli.py text file.pdf [-o output.txt] [--per-page]
"""

import sys

import extract_pages
import extract_pdf_text


def run_pages(args):
    sys.argv = ["extract_pages.py", *args]
    extract_pages.main()


def run_text(args):
    sys.argv = ["extract_pdf_text.py", *args]
    extract_pdf_text.main()


COMMANDS = {
    "pages": run_pages,
    "text": run_text,
}


def print_usage():
    print(__doc__)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print_usage()
        sys.exit(0 if len(sys.argv) >= 2 else 1)

    command, *rest = sys.argv[1:]

    handler = COMMANDS.get(command)
    if handler is None:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)

    handler(rest)


if __name__ == "__main__":
    main()
