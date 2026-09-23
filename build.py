#!/usr/bin/env python3
"""
build.py

Builds a standalone, single-file executable of pdf_cli.py using PyInstaller.
The resulting binary bundles the Python interpreter and all dependencies,
so it can be run directly without having Python installed.

This must be run separately on each target OS (Windows, Linux, macOS):
PyInstaller does not cross-compile, it only builds for the platform it runs on.

Usage:
    python build.py

Requirement:
    pip install -r requirements-dev.txt

Output:
    dist/pdf-cli(.exe)
"""
import subprocess
import sys

APP_NAME = "pdf-cli"
ENTRY_POINT = "pdf_cli.py"


def main():
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        sys.exit(
            "Error: PyInstaller is not installed.\n"
            "Install it with:  pip install -r requirements-dev.txt"
        )

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--name", APP_NAME,
        "--clean",
        ENTRY_POINT,
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    print(f"\nDone! Executable created in dist/{APP_NAME}")


if __name__ == "__main__":
    main()
