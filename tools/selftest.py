"""Self-test for the lesson parser: every rule the build promises must actually fire.

    python3 tools/selftest.py
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md import ContentError, Context, render  # noqa: E402
import build as site_build  # noqa: E402


def ctx() -> Context:
    def media(name, line):
        if name != "ok.svg":
            raise ContentError("t.md", line, f"media file '{name}' not found")
        return "media/ok.svg"
    return Context(path="t.md", media=media)


MUST_FAIL = {
    "raw html": ("Metin <b>kalın</b>", "raw HTML"),
    "raw html block": ("<div>x</div>", "raw HTML"),
    "h1 in body": ("# Başlık", "only ##"),
    "h4 in body": ("#### Başlık", "only ##"),
    "unknown directive": (":::diagram\nx\n:::", "unknown directive"),
    "unclosed directive": (":::note\nmetin", "not closed"),
    "unclosed fence": ("```\ncode", "unclosed code fence"),
    "nested directive": (":::note\n:::tip\nx\n:::\n:::", "not closed before"),
    "relative link": ("[bak](../x.html)", "link must be"),
    "javascript link": ("[bak](javascript:alert(1))", "link must be"),
    "bad toml": (":::quiz\n[[question]\n:::", "invalid TOML"),
    "quiz no answer": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y"]\nexplain="e"\n:::', "missing 'answer'"),
    "quiz answer out of range": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y"]\nanswer=3\nexplain="e"\n:::', "1-based"),
    "quiz answer zero": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y"]\nanswer=0\nexplain="e"\n:::', "1-based"),
    "quiz one choice": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x"]\nanswer=1\nexplain="e"\n:::', "at least two strings"),
    "quiz unknown key": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y"]\nanswer=1\nexplain="e"\nhint="h"\n:::', "unknown key"),
    "quiz empty": (":::quiz\n:::", "at least one [[question]]"),
    "steps single": (':::steps\n[[step]]\ntitle="a"\nbody="b"\n:::', "at least two [[step]]"),
    "flashcard no back": (':::flashcards\n[[card]]\nfront="a"\n:::', "missing 'back'"),
    "match single pair": (':::match\n[[pair]]\nleft="a"\nright="b"\n:::', "at least two [[pair]]"),
    "figure missing file": (':::figure\nsrc="nope.png"\nalt="x"\n:::', "not found"),
    "figure empty alt": (':::figure\nsrc="ok.svg"\nalt=" "\n:::', "'alt' must"),
    "heading in callout": (":::note\n## x\n:::", "headings are not allowed"),
    "table column mismatch": ("| a | b |\n| --- | --- |\n| 1 |", "cells, header has"),
    "quiz answer boolean": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y"]\nanswer=true\nexplain="e"\n:::', "1-based"),
    "html inside quiz prompt": (':::quiz\n[[question]]\nprompt="<i>a</i>"\nchoices=["x","y"]\nanswer=1\nexplain="e"\n:::', "raw HTML"),
}

MUST_PASS = {
    "code span with angle brackets": ("`content/<kurs>/lessons`", "<code>content/&lt;kurs&gt;/lessons</code>"),
    "comparison text": ("RAM < 8 GB ise yavaşlar", "RAM &lt; 8 GB"),
    "kbd combo": ("++Ctrl+Alt+Del++", "<kbd>Del</kbd>"),
    "bold": ("**kalın**", "<strong>kalın</strong>"),
    "mark": ("==önemli==", "<mark>önemli</mark>"),
    "external link": ("[CompTIA](https://www.comptia.org)", 'target="_blank"'),
    "turkish heading id": ("## Şema ve Çıktı", 'id="sema-ve-cikti"'),
    "multi answer quiz": (':::quiz\n[[question]]\nprompt="a"\nchoices=["x","y","z"]\nanswer=[1,3]\nexplain="e"\n:::', 'data-multi="1"'),
    "figure": (':::figure\nsrc="ok.svg"\nalt="şema"\n:::', 'src="media/ok.svg"'),
    "ul then ol stay separate": ("- a\n- b\n\n1. c\n2. d", "</ul>\n<ol>"),
    "nested list": ("- a\n  - b\n- c", "<li>a<ul><li>b</li></ul></li>"),
    "fence inside callout": (":::example\n```\n:::\n```\n:::", "<pre><code>:::</code></pre>"),
    "table alignment": ("| a | b |\n| --- | :---: |\n| 1 | 2 |", 'class="al-center"'),
}


def exam_mutations() -> tuple[int, list[str]]:
    failures = []
    course_text = '''title="Test"
kicker="Test"
summary="Test"
[[unit]]
id="unit-one"
title="Test unit"
exam={questions="2–3"}
'''
    source = '[[source]]\ntitle="Official"\nurl="https://example.test/objectives"\n'
    question = '''[[question]]
lesson="{lesson}"
objective="3.5"
prompt="{prompt}"
choices=["A", "B"]
answer=1
explain="A doğru çünkü test; B yanlış çünkü test."
'''
    base = ('unit="unit-one"\nupdated=2026-09-27\n' + source +
            question.format(lesson="first", prompt="Hangi anakart bağlantısı kullanılmalı?") +
            question.format(lesson="second", prompt="İkinci işlem için doğru adım hangisi?"))
    cases = {
        "valid": (base, course_text, None),
        "unknown exam key": (base.replace('[[source]]', 'surprise="x"\n[[source]]', 1), course_text, "unknown key"),
        "unknown source key": (base.replace('url="https://example.test/objectives"', 'url="https://example.test/objectives"\nextra="x"'), course_text, "unknown key"),
        "unknown question key": (base.replace('answer=1', 'answer=1\nextra="x"', 1), course_text, "unknown key"),
        "unknown unit": (base, course_text.replace('id="unit-one"', 'id="other-unit"'), "not declared in course.toml"),
        "unit without exam": (base, course_text.replace('exam={questions="2–3"}', ''), "no exam key"),
        "bad lesson": (base.replace('lesson="second"', 'lesson="absent"'), course_text, "not published"),
        "bad objective": (base.replace('objective="3.5"', 'objective="9.9"', 1), course_text, "not in lesson"),
        "bad answer": (base.replace('answer=1', 'answer=3', 1), course_text, "1-based"),
        "boolean answer": (base.replace('answer=1', 'answer=true', 1), course_text, "1-based"),
        "duplicate answer": (base.replace('answer=1', 'answer=[1,1]', 1), course_text, "unique 1-based"),
        "too few": (base[:base.index('[[question]]', base.index('[[question]]') + 1)], course_text, "outside"),
        "too many": (base + question.format(lesson="first", prompt="Üçüncü farklı senaryo nasıl çözülür?") + question.format(lesson="second", prompt="Dördüncü farklı senaryo nasıl çözülür?"), course_text, "outside"),
        "uncovered lesson": (base.replace('lesson="second"', 'lesson="first"'), course_text, "zero questions"),
        "quiz duplicate": (base.replace('Hangi anakart bağlantısı kullanılmalı?', 'Ders quiz sorusu tam olarak nedir?'), course_text, "near-duplicate"),
        "exam near duplicate": (base.replace('İkinci işlem için doğru adım hangisi?', 'Hangi anakart bağlantısı kullanılmalı'), course_text, "near-duplicate"),
    }
    old_content = site_build.CONTENT
    try:
        with tempfile.TemporaryDirectory(prefix="qrup596-exam-selftest-") as directory:
            root = Path(directory) / "courses" / "test-course"
            (root / "lessons").mkdir(parents=True)
            (root / "exams").mkdir()
            for order, slug in enumerate(("first", "second"), 1):
                (root / "lessons" / f"0{order}-{slug}.md").write_text(
                    f'+++\ntitle="{slug}"\nunit="unit-one"\norder={order}\nsummary="Test"\nobjectives=["3.5"]\n{source}+++\n'
                    + (':::quiz\n[[question]]\nprompt="Ders quiz sorusu tam olarak nedir?"\nchoices=["A","B"]\nanswer=1\nexplain="A"\n:::\n' if order == 1 else 'Lesson body.\n'), encoding="utf-8")
            site_build.CONTENT = Path(directory)
            for name, (bank, course, reason) in cases.items():
                (root / "course.toml").write_text(course, encoding="utf-8")
                (root / "exams" / "unit-one.toml").write_text(bank, encoding="utf-8")
                try:
                    loaded = site_build.load_all()
                    if reason or not loaded[0].units[0].bank:
                        failures.append(f"exam {name}: expected {reason or 'bank'}")
                except site_build.BuildError as err:
                    if reason is None or reason not in str(err):
                        failures.append(f"exam {name}: wrong error: {err}")
    finally:
        site_build.CONTENT = old_content
    return len(cases), failures


def main() -> int:
    failures = []
    for name, (src, reason) in MUST_FAIL.items():
        try:
            render(src, ctx())
        except ContentError as e:
            if reason not in e.message:
                failures.append(f"'{name}' failed for the wrong reason: {e.message}")
            continue
        failures.append(f"expected an error: {name}")
    for name, (src, needle) in MUST_PASS.items():
        try:
            out = render(src, ctx())
        except ContentError as e:
            failures.append(f"unexpected error in '{name}': {e}")
            continue
        if needle not in out:
            failures.append(f"'{name}': expected {needle!r} in output:\n    {out[:300]}")
    exam_total, exam_failures = exam_mutations()
    failures.extend(exam_failures)
    total = len(MUST_FAIL) + len(MUST_PASS) + exam_total
    if failures:
        print("SELFTEST FAILED\n  " + "\n  ".join(failures))
        return 1
    print(f"selftest: {total}/{total} cases pass ({len(MUST_FAIL)} parser must-fail, {len(MUST_PASS)} parser must-pass, {exam_total} exam mutations)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
