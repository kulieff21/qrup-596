"""Print the text of selected pages of a source PDF, and nothing else.

    python3 tools/pdfpages.py <lecture.pdf> <pages> [--out file.txt]

<pages> are PDF page numbers as a PDF viewer shows them (1 = first page): "12-30" or
"1-5,40-44". At most MAX_PAGES pages per call, so a lesson reads its own range, not the file.

Research helper only, not part of the build: needs PyMuPDF (`pymupdf`) or `pypdf`.
Text only; figures are not extracted and tables lose their layout.
"""
import argparse
import sys

MAX_PAGES = 60


def parse_pages(spec: str, total: int) -> list[int]:
    pages: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        lo, sep, hi = part.partition("-")
        if not lo.isdigit() or (sep and not hi.isdigit()):
            raise ValueError(f"bad page range '{part}' (use 240-272 or 131-160,308-311)")
        a, b = int(lo), int(hi) if sep else int(lo)
        if a > b:
            raise ValueError(f"page range '{part}' runs backwards")
        if a < 1 or b > total:
            raise ValueError(f"page range '{part}' is outside 1-{total}")
        pages.extend(range(a, b + 1))
    if len(set(pages)) != len(pages):
        raise ValueError("page ranges overlap")
    if len(pages) > MAX_PAGES:
        raise ValueError(f"{len(pages)} pages requested; limit is {MAX_PAGES} per call")
    return pages


def open_book(path: str):
    """Return (page_count, text_of(n), label_of(n)) with n as 1-based viewer page numbers."""
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    if pymupdf:
        doc = pymupdf.open(path)
        return len(doc), lambda n: doc[n - 1].get_text(), lambda n: doc[n - 1].get_label()
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("pdfpages: install PyMuPDF or pypdf (py -m pip install pymupdf)")
    reader = PdfReader(path)
    labels = reader.page_labels
    return (len(reader.pages), lambda n: reader.pages[n - 1].extract_text() or "",
            lambda n: labels[n - 1] if labels else "")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("pages")
    ap.add_argument("--out", help="write to this file instead of stdout")
    args = ap.parse_args()

    total, text_of, label_of = open_book(args.pdf)
    try:
        pages = parse_pages(args.pages, total)
    except ValueError as e:
        sys.exit(f"pdfpages: {e}")

    chunks = []
    for n in pages:
        label = label_of(n)
        printed = f" (printed page {label})" if label and label != str(n) else ""
        chunks.append(f"===== PDF page {n}{printed} =====\n{text_of(n).strip()}\n")
    result = "\n".join(chunks)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"pdfpages: wrote {len(pages)} pages to {args.out}")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
