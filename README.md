# pdf-utils

Small collection of command-line tools for working with PDF files: extracting a range of pages, and extracting text content.

## Features

- **Extract pages** — pull a range of pages (1-indexed, inclusive) from a PDF into a new PDF file.
- **Extract text** — extract the text content of a PDF into a `.txt` file, optionally with a page-number header before each page's text.
- **Unified CLI** — a single entry point (`pdf_cli.py`) exposes both features as subcommands, while the individual scripts remain usable standalone.
- **Standalone executable** — build a single-file executable with PyInstaller to run the tool without a Python interpreter installed.

## Requirements

- Python 3.9+
- [pypdf](https://pypi.org/project/pypdf/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Unified CLI

```bash
python pdf_cli.py pages file.pdf start_page end_page [output.pdf]
python pdf_cli.py text file.pdf [-o output.txt] [--per-page]
```

### Individual scripts

Extract a page range:

```bash
python extract_pages.py file.pdf start_page end_page [output.pdf]
```

If `output.pdf` is omitted, the result is saved as `file_pSTART-END.pdf` next to the input file.

Extract text:

```bash
python extract_pdf_text.py file.pdf
python extract_pdf_text.py file.pdf -o extracted_text.txt
python extract_pdf_text.py file.pdf --per-page
```

If `-o/--output` is omitted, the result is saved with the same name as the input file, with a `.txt` extension.

## Building a standalone executable

A standalone, single-file executable can be built with [PyInstaller](https://pyinstaller.org/), bundling the Python interpreter and all dependencies so it can run without Python installed.

```bash
pip install -r requirements-dev.txt
python build.py
```

The executable is created at `dist/pdf-cli` (`dist/pdf-cli.exe` on Windows) and supports the same subcommands as the unified CLI:

```bash
dist/pdf-cli pages file.pdf 1 5
dist/pdf-cli text file.pdf --per-page
```

PyInstaller does not cross-compile: run `build.py` on each target operating system (Windows, Linux, macOS) to produce a native executable for it.

## License

MIT — see [LICENSE](LICENSE).
