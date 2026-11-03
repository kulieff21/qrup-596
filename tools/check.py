"""Run before every commit: parser self-test, build, then verify the generated site.

    python3 tools/check.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])


def run(step: str, args: list[str]) -> None:
    r = subprocess.run([sys.executable, *args], cwd=ROOT)
    if r.returncode:
        print(f"CHECK FAILED at {step}")
        sys.exit(1)


def main() -> int:
    run("selftest", ["tools/selftest.py"])
    run("build", ["tools/build.py"])
    problems = []
    parsed = {}
    pages = sorted(SITE.rglob("*.html"))
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if "{{" in text:
            problems.append(f"{page.relative_to(ROOT)}: unreplaced template placeholder")
        p = Refs()
        p.feed(text)
        parsed[page.resolve()] = p
    for page, p in parsed.items():
        rel = page.relative_to(ROOT.resolve())
        for ref in p.refs:
            if re.match(r"^(https?:|mailto:|data:)", ref):
                continue
            parts = urlsplit(ref)
            target = page if not parts.path else (page.parent / unquote(parts.path)).resolve()
            if parts.path and parts.path.endswith("/"):
                problems.append(f"{rel}: directory link '{ref}' breaks under file:// (link to index.html)")
                continue
            if not target.exists():
                problems.append(f"{rel}: broken reference '{ref}'")
                continue
            if parts.fragment and target.suffix == ".html":
                ids = parsed[target].ids if target in parsed else set()
                if parts.fragment not in ids:
                    problems.append(f"{rel}: missing anchor '{ref}'")
    if problems:
        print("CHECK FAILED\n  " + "\n  ".join(problems))
        return 1
    refs = sum(len(p.refs) for p in parsed.values())
    print(f"check: {len(pages)} pages, {refs} references, all resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
