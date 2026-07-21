#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "weasyprint",
# ]
# ///
"""
Convert resume.html to resume.pdf using WeasyPrint.

Usage:
    uv run html_to_pdf.py resume.html resume.pdf
    uv run html_to_pdf.py                 # defaults to resume.html -> resume.pdf
"""

import sys
from pathlib import Path

from weasyprint import HTML


def convert(html_path: str, pdf_path: str) -> None:
    src = Path(html_path)
    if not src.exists():
        raise FileNotFoundError(f"HTML file not found: {src}")
    HTML(filename=str(src)).write_pdf(pdf_path)
    print(f"Wrote {pdf_path}")


def main() -> None:
    html_path = sys.argv[1] if len(sys.argv) > 1 else "resume.html"
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else "resume.pdf"
    convert(html_path, pdf_path)


if __name__ == "__main__":
    main()
