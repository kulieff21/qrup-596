"""Build the qrup-596 site: content/ + src/ -> site/.

    python3 tools/build.py

Standard library only, so it runs the same on WSL and Windows.
"""
from __future__ import annotations

import html
import difflib
import json
import math
import re
import shutil
import sys
import tomllib
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md import ContentError, Context, render, inline, slugify  # noqa: E402
from bus import bus_big, bus_small  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SRC = ROOT / "src"
OUT = ROOT / "site"

SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MEDIA_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".avif"}
WORDS_PER_MIN = 180
LESSON_KINDS = {"story": "Hekayə", "bundle": "Toplu"}   # lesson shapes for unordered courses
COMPONENT_MIN = {"quiz": 2, "flashcards": 2, "match": 2, "steps": 1, "reveal": 1}

ICONS = {
    "coin": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5.5"/><path d="M12 9.5v5M10.5 11h3"/>',
    "chip": '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 7V3M14 7V3M10 21v-4M14 21v-4M7 10H3M7 14H3M21 10h-4M21 14h-4"/><rect x="10" y="10" width="4" height="4" rx=".5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>',
    "shield": '<path d="M12 3l7.5 3v5.5c0 4.6-3.1 8.4-7.5 9.5-4.4-1.1-7.5-4.9-7.5-9.5V6z"/><path d="M8.8 12.2l2.2 2.2 4.4-4.6"/>',
    "code": '<path d="M8.5 7L3.5 12l5 5M15.5 7l5 5-5 5M13.5 4.5l-3 15"/>',
    "network": '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M12 7.5v4.5M12 12l-5.5 5M12 12l5.5 5"/>',
    "book": '<path d="M4 5.5C4 4.7 4.7 4 5.5 4H11v16H5.5c-.8 0-1.5-.7-1.5-1.5zM20 5.5c0-.8-.7-1.5-1.5-1.5H13v16h5.5c.8 0 1.5-.7 1.5-1.5z"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "lines-short": '<path d="M5 9h14M5 14h8"/>',
    "lines-mid": '<path d="M5 7h14M5 12h14M5 17h9"/>',
    "lines-long": '<path d="M5 5h14M5 9.5h14M5 14h14M5 18.5h10"/>',
    "glossary": '<path d="M4 19.5l4.5-13 4.5 13M5.6 15h5.8"/><path d="M15 9h5M15 13h5M15 17h3"/>',
    "spark": '<path d="M12 3.5c.6 4.6 1.9 5.9 6.5 6.5-4.6.6-5.9 1.9-6.5 6.5-.6-4.6-1.9-5.9-6.5-6.5 4.6-.6 5.9-1.9 6.5-6.5z"/><path d="M18.5 15.5v4M16.5 17.5h4"/>',
}


class BuildError(Exception):
    pass


@dataclass
class Unit:
    id: str
    title: str
    summary: str
    plan: list = field(default_factory=list)      # [{"id", "title", "objectives", "kind"}] in teaching order
    lessons: list = field(default_factory=list)
    exam: dict | None = None                      # planned end-of-unit exam: {"title", "questions"}
    bank: dict | None = None
    icon: str = "book"                            # tracks layout: icon on the track card
    kicker: str = ""                              # tracks layout: small label above the track title

    @property
    def items(self) -> list:
        """Planned entries in order, each paired with its written Lesson or None."""
        if not self.plan:
            return [(None, l) for l in self.lessons]
        written = {l.slug: l for l in self.lessons}
        return [(p, written.get(p["id"])) for p in self.plan]


@dataclass
class Lesson:
    course: "Course"
    slug: str
    source: Path
    title: str
    unit: str
    order: int
    summary: str
    objectives: list
    sources: list
    updated: str
    body_md: str
    body_line: int
    html: str = ""
    headings: list = field(default_factory=list)
    minutes: int = 0
    components: dict = field(default_factory=dict)

    @property
    def key(self) -> str:
        return f"{self.course.slug}/{self.slug}"


@dataclass
class Course:
    slug: str
    dir: Path
    title: str
    kicker: str
    summary: str
    hue: int
    icon: str
    order: int
    tags: list
    hidden: bool
    sources: list
    units: list
    ordered: bool = True                          # False: no unit/lesson numbers, lessons show their kind
    layout: str = "units"                         # "tracks": units are parallel paths (e.g. short/long) shown as cards
    lessons: list = field(default_factory=list)

    @property
    def minutes(self) -> int:
        return sum(l.minutes for l in self.lessons)

    @property
    def planned_total(self) -> int:
        return sum(len(u.items) for u in self.units)


def fail(path: Path, message: str):
    try:
        label = path.relative_to(ROOT)
    except ValueError:
        label = path
    raise BuildError(f"{label}: {message}")


def check_keys(obj: dict, required: dict, optional: dict, path: Path, where: str):
    allowed = set(required) | set(optional)
    extra = set(obj) - allowed
    if extra:
        fail(path, f"{where}: unknown key(s) {sorted(extra)}; allowed {sorted(allowed)}")
    for key, typ in required.items():
        if key not in obj:
            fail(path, f"{where}: missing '{key}'")
    for key, typ in {**required, **optional}.items():
        if key in obj and not isinstance(obj[key], typ):
            fail(path, f"{where}: '{key}' has the wrong type")


def load_sources(items, path: Path, where: str) -> list:
    out = []
    for k, s in enumerate(items or [], 1):
        if not isinstance(s, dict):
            fail(path, f"{where}[{k}] must be a table")
        check_keys(s, {"title": str}, {"url": str, "note": str}, path, f"{where}[{k}]")
        if s.get("url") and not re.match(r"^https?://", s["url"]):
            fail(path, f"{where}[{k}]: url must start with http(s)://")
        out.append(s)
    return out


# ---------------------------------------------------------------- loading

def load_course(d: Path) -> Course:
    path = d / "course.toml"
    if not SLUG.match(d.name):
        fail(d, "course folder name must be a lowercase slug like 'risk-management'")
    if not path.exists():
        fail(d, "missing course.toml")
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as e:
        fail(path, f"invalid TOML: {e}")
    check_keys(data, {"title": str, "kicker": str, "summary": str},
               {"hue": int, "icon": str, "order": int, "tags": list, "hidden": bool,
                "unit": list, "source": list, "ordered": bool, "layout": str}, path, "course")
    layout = data.get("layout", "units")
    if layout not in ("units", "tracks"):
        fail(path, f"layout '{layout}' is unknown; use 'units' or 'tracks'")
    ordered = data.get("ordered", True)
    icon = data.get("icon", "book")
    if icon not in ICONS:
        fail(path, f"icon '{icon}' is unknown; use one of {sorted(ICONS)}")
    units = []
    seen = set()
    planned_ids = set()
    for k, u in enumerate(data.get("unit", []), 1):
        check_keys(u, {"id": str, "title": str}, {"summary": str, "lesson": list, "exam": dict, "icon": str, "kicker": str}, path, f"unit[{k}]")
        if u.get("icon", "book") not in ICONS:
            fail(path, f"unit[{k}]: icon '{u['icon']}' is unknown; use one of {sorted(ICONS)}")
        if not SLUG.match(u["id"]) or u["id"] in seen:
            fail(path, f"unit[{k}]: id '{u['id']}' must be a unique slug")
        seen.add(u["id"])
        plan = []
        for j, pl in enumerate(u.get("lesson", []), 1):
            where = f"unit '{u['id']}' lesson[{j}]"
            check_keys(pl, {"id": str, "title": str}, {"objectives": list, "kind": str}, path, where)
            kind = pl.get("kind")
            if kind is not None and kind not in LESSON_KINDS:
                fail(path, f"{where}: kind '{kind}' is unknown; use one of {sorted(LESSON_KINDS)}")
            if not ordered and kind is None:
                fail(path, f"{where}: an unordered course (ordered = false) needs a 'kind' on every planned lesson")
            if not SLUG.match(pl["id"]) or pl["id"] in planned_ids:
                fail(path, f"{where}: id '{pl['id']}' must be a slug unique in the course")
            planned_ids.add(pl["id"])
            plan.append({"id": pl["id"], "title": pl["title"], "objectives": [str(o) for o in pl.get("objectives", [])], "kind": kind})
        exam = None
        if "exam" in u:
            check_keys(u["exam"], {}, {"title": str, "questions": str}, path, f"unit '{u['id']}' exam")
            exam = {"title": u["exam"].get("title", "Bölmə imtahanı"), "questions": u["exam"].get("questions", "")}
        units.append(Unit(u["id"], u["title"], u.get("summary", ""), plan, exam=exam,
                          icon=u.get("icon", "book"), kicker=u.get("kicker", "")))
    return Course(
        slug=d.name, dir=d, title=data["title"], kicker=data["kicker"], summary=data["summary"],
        hue=data.get("hue", 250) % 360, icon=icon, order=data.get("order", 100),
        tags=[str(t) for t in data.get("tags", [])], hidden=data.get("hidden", False),
        sources=load_sources(data.get("source"), path, "source"), units=units, ordered=ordered,
        layout=layout,
    )


def load_lesson(course: Course, path: Path) -> Lesson:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.match(r"^\+\+\+\n(.*?)\n\+\+\+\n", text, re.S)
    if not m:
        fail(path, "lesson must start with TOML frontmatter between '+++' lines")
    try:
        meta = tomllib.loads(m.group(1))
    except tomllib.TOMLDecodeError as e:
        fail(path, f"invalid frontmatter TOML: {e}")
    check_keys(meta, {"title": str, "unit": str, "order": int, "summary": str, "source": list},
               {"objectives": list, "updated": (date, str)}, path, "frontmatter")
    slug = re.sub(r"^\d+-", "", path.stem)
    if not SLUG.match(slug):
        fail(path, "file name must be a slug, optionally prefixed with a number: '03-cpu-sockets.md'")
    units = {u.id for u in course.units}
    if meta["unit"] not in units:
        fail(path, f"unit '{meta['unit']}' is not declared in course.toml (known: {sorted(units) or 'none'})")
    sources = load_sources(meta["source"], path, "source")
    if not sources:
        fail(path, "a lesson needs at least one [[source]]")
    return Lesson(
        course=course, slug=slug, source=path, title=meta["title"], unit=meta["unit"],
        order=meta["order"], summary=meta["summary"],
        objectives=[str(o) for o in meta.get("objectives", [])], sources=sources,
        updated=str(meta.get("updated", "")), body_md=text[m.end():],
        body_line=m.group(0).count("\n") + 1,
    )


def load_all() -> list[Course]:
    courses = []
    base = CONTENT / "courses"
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        course = load_course(d)
        lessons_dir = d / "lessons"
        if lessons_dir.exists():
            for f in sorted(lessons_dir.glob("*")):
                if f.suffix != ".md":
                    fail(f, "only .md files belong in lessons/ (images go in media/)")
                course.lessons.append(load_lesson(course, f))
        slugs = [l.slug for l in course.lessons]
        dup = {s for s in slugs if slugs.count(s) > 1}
        if dup:
            fail(lessons_dir, f"duplicate lesson slugs {sorted(dup)}")
        by_unit = {u.id: u for u in course.units}
        for l in course.lessons:
            by_unit[l.unit].lessons.append(l)
        for u in course.units:
            if u.plan:
                positions = {p["id"]: k for k, p in enumerate(u.plan, 1)}
                for l in u.lessons:
                    if l.slug not in positions:
                        fail(l.source, f"unit '{u.id}' has a lesson plan in course.toml; add '{l.slug}' to it or rename the file to a planned id ({', '.join(positions)})")
                    if l.order != positions[l.slug]:
                        fail(l.source, f"'order' must be {positions[l.slug]}, the position of '{l.slug}' in the unit plan")
            orders = [l.order for l in u.lessons]
            if len(orders) != len(set(orders)):
                fail(d, f"unit '{u.id}' has lessons with the same 'order'")
            u.lessons.sort(key=lambda l: l.order)
        course.lessons = [l for u in course.units for l in u.lessons]
        if course.layout == "tracks":
            clash = {u.id for u in course.units} & {l.slug for l in course.lessons} | ({u.id for u in course.units} & {"exams", "media"})
            if clash:
                fail(d / "course.toml", f"tracks layout: unit id(s) {sorted(clash)} collide with a lesson slug or a reserved folder")
        exams_dir = d / "exams"
        if exams_dir.exists():
            for path in sorted(exams_dir.iterdir()):
                if not path.is_file() or path.suffix != ".toml":
                    fail(path, "only .toml question banks belong in exams/")
                unit = by_unit.get(path.stem)
                if unit is None or unit.exam is None:
                    fail(path, f"unit '{path.stem}' is not in course.toml or has no exam key")
                unit.bank = load_exam(course, unit, path)
        courses.append(course)
    courses.sort(key=lambda c: (c.order, c.title))
    return courses


def normalized_prompt(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return " ".join("".join(c if c.isalnum() else " " for c in value).split())


def load_exam(course: Course, unit: Unit, path: Path) -> dict:
    if unit.exam is None:
        fail(path, f"unit '{unit.id}' has no exam key")
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as err:
        fail(path, f"invalid TOML: {err}")
    check_keys(data, {"unit": str, "updated": date, "source": list, "question": list}, {}, path, "exam")
    if data["unit"] != unit.id:
        fail(path, f"unit '{data['unit']}' does not match filename/unit '{unit.id}'")
    sources = load_sources(data["source"], path, "source")
    if not sources or not any(s.get("url") for s in sources):
        fail(path, "exam needs at least one [[source]] with a url")
    match = re.fullmatch(r"\s*(\d+)\s*(?:–\s*(\d+))?\s*", unit.exam["questions"])
    if not match:
        fail(course.dir / "course.toml", f"unit '{unit.id}' exam.questions must be a number or an en-dash range")
    low, high = int(match[1]), int(match[2] or match[1])
    questions = data["question"]
    if not low <= len(questions) <= high:
        fail(path, f"question count {len(questions)} is outside unit exam.questions range {low}–{high}")
    lessons = {lesson.slug: lesson for lesson in unit.lessons}
    counts = {slug: 0 for slug in lessons}
    previous = []
    for lesson in unit.lessons:
        for block in re.findall(r"^:::quiz(?:[^\n]*)\n(.*?)^:::\s*$", lesson.body_md, re.M | re.S):
            try:
                quiz = tomllib.loads(block)
            except tomllib.TOMLDecodeError as err:
                fail(lesson.source, f"invalid quiz TOML: {err}")
            for item in quiz.get("question", []):
                if isinstance(item, dict) and isinstance(item.get("prompt"), str):
                    previous.append((normalized_prompt(item["prompt"]), f"lesson '{lesson.slug}' quiz"))
    for number, q in enumerate(questions, 1):
        where = f"question[{number}]"
        if not isinstance(q, dict):
            fail(path, f"{where} must be a table")
        check_keys(q, {"lesson": str, "objective": str, "prompt": str, "choices": list,
                       "answer": (int, list), "explain": str}, {}, path, where)
        lesson = lessons.get(q["lesson"])
        if lesson is None:
            fail(path, f"{where}: lesson '{q['lesson']}' is not published in unit '{unit.id}'")
        if q["objective"] not in lesson.objectives:
            fail(path, f"{where}: objective '{q['objective']}' is not in lesson '{lesson.slug}' objectives")
        counts[lesson.slug] += 1
        if not q["prompt"].strip() or not q["explain"].strip():
            fail(path, f"{where}: prompt and explain must not be empty")
        choices = q["choices"]
        if len(choices) < 2 or not all(isinstance(c, str) and c.strip() for c in choices):
            fail(path, f"{where}: choices must contain at least two nonempty strings")
        answers = q["answer"] if isinstance(q["answer"], list) else [q["answer"]]
        if not answers or any(type(a) is not int or not 1 <= a <= len(choices) for a in answers) or len(set(answers)) != len(answers):
            fail(path, f"{where}: answer must contain unique 1-based choice indexes")
        prompt = normalized_prompt(q["prompt"])
        if not prompt:
            fail(path, f"{where}: prompt needs readable text")
        for earlier, origin in previous:
            if difflib.SequenceMatcher(None, prompt, earlier).ratio() >= 0.85:
                fail(path, f"{where}: duplicate or near-duplicate prompt of {origin}")
        previous.append((prompt, where))
        ctx = Context(path=str(path))
        for key in ("prompt", "explain", "*choices"):
            values = choices if key == "*choices" else [q[key]]
            for value in values:
                inline(value, ctx, number)
    missing = [slug for slug, count in counts.items() if count == 0]
    if missing:
        fail(path, f"published lesson(s) with zero questions: {', '.join(missing)}")
    return {"questions": questions, "sources": sources, "updated": str(data["updated"])}


# ---------------------------------------------------------------- rendering helpers

def e(s) -> str:
    return html.escape(str(s))


def icon(name: str, cls: str = "icon") -> str:
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def logo_mark(cls: str = "logo-mark", eyes: bool = False) -> str:
    """The 596 bus, flat front view (header, footer, empty states). The hero uses bus_big()."""
    return bus_small(cls, eyes)


def fmt_minutes(m: int) -> str:
    if m < 60:
        return f"{m} dəq"
    h, r = divmod(m, 60)
    return f"{h} saat {r} dəq" if r else f"{h} saat"


def page(title: str, body: str, depth: int, page_class: str, description: str = "",
         extra_head: str = "") -> str:
    root = "../" * depth
    layout = (SRC / "templates" / "layout.html").read_text(encoding="utf-8")
    values = {
        "title": e(title),
        "description": e(description or "Qrup 596 — magistr qrupunun birgə öyrənmə məkanı."),
        "root": root,
        "page_class": page_class,
        "header": header(root),
        "body": body,
        "footer": footer(root),
        "extra_head": extra_head,
        "logo": logo_mark(),
    }
    out = re.sub(r"\{\{\s*(\w+)\s*\}\}", lambda m: values[m.group(1)], layout)
    return out


def header(root: str) -> str:
    return f'''<header class="site-header" data-header>
  <div class="wrap header-inner">
    <a class="brand" href="{root}index.html" aria-label="Qrup 596 ana səhifə">{logo_mark()}<span class="brand-word">Qrup 596</span></a>
    <nav class="header-nav" aria-label="Əsas menyu">
      <a href="{root}index.html#courses">Fənlər</a>
      <a href="{root}index.html#method">Metod</a>
    </nav>
    <button class="search-trigger" type="button" data-search-open aria-label="Axtar">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>
      <span>Axtar</span><span class="keys"><kbd>Ctrl</kbd><kbd>K</kbd></span>
    </button>
  </div>
  <div class="read-progress" aria-hidden="true"><span></span></div>
</header>'''


def footer(root: str) -> str:
    return f'''<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-brand">{logo_mark()}<span>Qrup 596</span></div>
    <p class="footer-note">Qaranlıqda da görmək üçün. 596-cı qrupun imtahanlara birlikdə hazırlaşdığı açıq öyrənmə məkanı.</p>
    <div class="footer-links"><a href="{root}courses/guide/components/index.html">Komponent bələdçisi</a><button type="button" class="linklike" data-motion-toggle>Animasiya: <span>açıq</span></button></div>
  </div>
</footer>'''


# ---------------------------------------------------------------- pages

def build_lesson_html(lesson: Lesson, depth_root: str):
    media_dir = lesson.course.dir / "media"

    def media(name: str, line: int) -> str:
        p = (media_dir / name).resolve()
        if media_dir.resolve() not in p.parents or not p.is_file():
            raise ContentError(str(lesson.source.relative_to(ROOT)), line,
                               f"media file '{name}' not found in {media_dir.relative_to(ROOT)}")
        if p.suffix.lower() not in MEDIA_EXT:
            raise ContentError(str(lesson.source.relative_to(ROOT)), line, f"unsupported media type '{p.suffix}'")
        return f"{depth_root}courses/{lesson.course.slug}/media/{name}"

    ctx = Context(path=str(lesson.source.relative_to(ROOT)), media=media)
    lesson.html = render(lesson.body_md, ctx, lesson.body_line)
    lesson.headings = ctx.headings
    lesson.components = dict(ctx.counts)
    words = len(re.findall(r"\w+", lesson.body_md))
    extra = sum(COMPONENT_MIN.get(k, 0) * v for k, v in ctx.counts.items())
    lesson.minutes = max(1, math.ceil(words / WORDS_PER_MIN) + extra)


def course_card(c: Course, root: str, index: int) -> str:
    n = len(c.lessons)
    total = c.planned_total
    status = (f'<span class="chip chip-live">{n} / {total} dərs</span>' if n
              else '<span class="chip chip-soon"><span class="pulse"></span>Hazırlanır</span>')
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in c.tags)
    units = f"{len(c.units)} bölmə · {total} dərs" if c.units else "Proqram gözlənilir"
    return f'''<a class="course-card" href="{root}courses/{c.slug}/index.html" style="--hue:{c.hue}; --i:{index}" data-course="{c.slug}" data-tilt>
  <span class="card-glow" aria-hidden="true"></span>
  <span class="card-grid" aria-hidden="true"></span>
  <div class="cc-visual" aria-hidden="true"><span class="cv-ring"></span><span class="cv-ring"></span><span class="cv-ring"></span><span class="cv-orbit"></span><span class="cv-orbit o2"></span><span class="cv-scan"></span><span class="cv-icon">{icon(c.icon)}</span></div>
  <div class="cc-top">
    <span class="cc-icon">{icon(c.icon)}</span>
    {status}
  </div>
  <div class="cc-body">
    <span class="cc-kicker">{e(c.kicker)}</span>
    <h3 class="cc-title">{e(c.title)}</h3>
    <p class="cc-summary">{e(c.summary)}</p>
  </div>
  <div class="cc-tags">{tags}</div>
  <div class="cc-foot">
    <div class="cc-meta"><span>{units}</span>{f'<span>{fmt_minutes(c.minutes)}</span>' if n else ''}</div>
    <div class="cc-progress" data-progress-course="{c.slug}" data-total="{total}"><span class="bar"><span></span></span><span class="pct">0%</span></div>
    <span class="cc-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
  </div>
</a>'''


def home_page(courses: list[Course]) -> str:
    root = ""
    visible = [c for c in courses if not c.hidden]
    lessons = sum(len(c.lessons) for c in visible)
    cards = "\n".join(course_card(c, root, k) for k, c in enumerate(visible))
    if not visible:
        cards = '<p class="section-lede">Fənlər tezliklə əlavə olunacaq.</p>'
    featured = " is-featured" if len(visible) <= 2 else ""
    body = f'''
<section class="hero" data-hero>
  <canvas class="hero-sky" data-sky aria-hidden="true"></canvas>
  <div class="hero-moon" aria-hidden="true"></div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <p class="eyebrow" data-rise style="--d:0">Qrup 596 · birgə öyrənmə məkanı</p>
      <h1 class="hero-title">
        <span class="line" data-rise style="--d:1"><span class="word">Oxu.</span></span>
        <span class="line" data-rise style="--d:2"><span class="word">Sına.</span></span>
        <span class="line" data-rise style="--d:3"><span class="word accent-word">Xatırla.</span></span>
      </h1>
      <p class="hero-lede" data-rise style="--d:4">Mühazirə materiallarından və etibarlı mənbələrdən mövzu-mövzu yazılmış dərslər; yanında sxemlər, addım-addım proseslər, təkrar kartları və qısa testlər. PDF-in bacarmadığını bacaran bir iş masası.</p>
      <div class="hero-actions" data-rise style="--d:5">
        <a class="btn btn-lg" href="#courses">Fənlərə bax</a>
        <a class="btn btn-lg btn-ghost" href="#" data-resume hidden>Qaldığın yerdən davam et <span class="resume-title"></span></a>
      </div>
    </div>
    <div class="hero-owl" data-rise style="--d:2">
      <div class="owl-halo" aria-hidden="true"></div>
      {bus_big()}
      <div class="orbit orbit-1" aria-hidden="true"><span></span></div>
      <div class="orbit orbit-2" aria-hidden="true"><span></span></div>
    </div>
  </div>
  <a class="scroll-cue" href="#courses" aria-label="Aşağı sürüşdür"><span></span></a>
</section>

<section class="stats wrap" aria-label="Xülasə">
  <div class="stat" data-reveal><span class="stat-n" data-count="{len(visible)}">0</span><span class="stat-l">fənn</span></div>
  <div class="stat" data-reveal><span class="stat-n" data-count="{lessons}">0</span><span class="stat-l">dərs</span></div>
  <div class="stat" data-reveal><span class="stat-n" data-stat="done">0</span><span class="stat-l">tamamlanmış dərs</span></div>
  <div class="stat" data-reveal><span class="stat-n" data-stat="answered">0</span><span class="stat-l">həll olunmuş sual</span></div>
</section>

<section class="section wrap" id="courses">
  <div class="section-head" data-reveal>
    <span class="section-index">01</span>
    <div><h2 class="section-title">Fənlər</h2>
    <p class="section-lede">Hər blok bir fəndir. İçinə girəndə bölmələri və dərsləri görürsən.</p></div>
  </div>
  <div class="course-grid{featured}">
    {cards}
  </div>
</section>

<section class="section wrap" id="method">
  <div class="section-head" data-reveal>
    <span class="section-index">02</span>
    <div><h2 class="section-title">Bir dərs necə yaranır</h2>
    <p class="section-lede">Məzmunu süni intellekt yazır, amma təxminlə yox: əvvəl mənbə, sonra proqram, sonra dərs.</p></div>
  </div>
  <ol class="method" data-method>
    <li class="method-step" data-reveal style="--i:0"><span class="ms-n">01</span><h3>Araşdırma</h3><p>Fənnin proqramı, mühazirə materialları və etibarlı mənbələr toplanır.</p></li>
    <li class="method-step" data-reveal style="--i:1"><span class="ms-n">02</span><h3>Proqram</h3><p>Mövzular bölmələrə ayrılır; hər dərs hansı hədəfi qarşıladığını göstərir.</p></li>
    <li class="method-step" data-reveal style="--i:2"><span class="ms-n">03</span><h3>Dərs</h3><p>İzah, sxem, addım-addım proses və uyğunlaşdırma kimi interaktiv hissələr.</p></li>
    <li class="method-step" data-reveal style="--i:3"><span class="ms-n">04</span><h3>Möhkəmləndirmə</h3><p>Təkrar kartları və izahlı suallar; nəyi bilmədiyin görünür olur.</p></li>
  </ol>
</section>
'''
    return page("Qrup 596", body, 0, "page-home", extra_head="")


def track_target(u: Unit) -> str:
    """Where a track card points, relative to the course folder: a one-lesson track opens it directly."""
    items = u.items
    if len(items) == 1 and items[0][1]:
        return f"{items[0][1].slug}/index.html"
    return f"{u.id}/index.html"


def track_minutes(u: Unit) -> int:
    return sum(l.minutes for l in u.lessons)


def tracks_course_page(c: Course) -> str:
    """Course page for layout = "tracks": one card per track (unit) instead of the unit list."""
    root = "../../"
    n = len(c.lessons)
    total = c.planned_total
    cards = []
    for k, u in enumerate(c.units):
        written, planned = len(u.lessons), len(u.items)
        chip = (f'<span class="chip chip-live">{written} / {planned}</span>' if written
                else '<span class="chip chip-soon"><span class="pulse"></span>Hazırlanır</span>')
        meta = f"<span>{planned} dərs</span>" if planned > 1 else "<span>Bir səhifə</span>"
        if written:
            meta += f"<span>{fmt_minutes(track_minutes(u))}</span>"
        cards.append(f'''<a class="course-card track-card" href="{track_target(u)}" style="--hue:{c.hue}; --i:{k}" data-tilt>
  <span class="card-glow" aria-hidden="true"></span>
  <span class="card-grid" aria-hidden="true"></span>
  <div class="cc-top"><span class="cc-icon">{icon(u.icon)}</span>{chip}</div>
  <div class="cc-body">
    {f'<span class="cc-kicker">{e(u.kicker)}</span>' if u.kicker else ''}
    <h3 class="cc-title">{e(u.title)}</h3>
    <p class="cc-summary">{e(u.summary)}</p>
  </div>
  <div class="cc-foot">
    <div class="cc-meta">{meta}</div>
    <span class="cc-arrow" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
  </div>
</a>''')
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in c.tags)
    sources = ""
    if c.sources:
        items = "".join(
            f'<li>{f"<a href={chr(34)}{e(s["url"])}{chr(34)} target={chr(34)}_blank{chr(34)} rel={chr(34)}noopener{chr(34)}>{e(s["title"])}</a>" if s.get("url") else e(s["title"])}'
            f'{f"<span>{e(s["note"])}</span>" if s.get("note") else ""}</li>' for s in c.sources)
        sources = f'<div class="side-card track-sources" data-reveal><h3>Mənbələr</h3><ul class="source-list">{items}</ul></div>'
    body = f'''
<section class="course-hero" style="--hue:{c.hue}">
  <div class="course-hero-bg" aria-hidden="true"><span class="ch-grid"></span><span class="ch-glow"></span><canvas data-circuit></canvas></div>
  <div class="wrap course-hero-inner">
    <nav class="crumbs" data-rise style="--d:0" aria-label="Yer"><a href="{root}index.html">Ana səhifə</a><span>/</span><a href="{root}index.html#courses">Fənlər</a><span>/</span><span aria-current="page">{e(c.title)}</span></nav>
    <div class="ch-main">
      <div class="ch-icon" data-rise style="--d:1">{icon(c.icon)}</div>
      <div class="ch-copy">
        <span class="eyebrow" data-rise style="--d:1">{e(c.kicker)}</span>
        <h1 class="ch-title" data-rise style="--d:2">{e(c.title)}</h1>
        <p class="ch-summary" data-rise style="--d:3">{e(c.summary)}</p>
        <div class="cc-tags" data-rise style="--d:4">{tags}</div>
      </div>
      <div class="ch-progress" data-rise style="--d:3" data-progress-course="{c.slug}" data-total="{total}">
        <svg viewBox="0 0 120 120" class="ring" aria-hidden="true"><circle class="ring-bg" cx="60" cy="60" r="52"/><circle class="ring-fg" cx="60" cy="60" r="52" pathLength="100"/></svg>
        <div class="ring-label"><span class="pct">0%</span><span>tamamlandı</span></div>
      </div>
    </div>
  </div>
</section>
<section class="wrap course-body is-tracks" style="--hue:{c.hue}" id="tracks">
  <div class="section-head compact" data-reveal><span class="section-index">01</span><div><h2 class="section-title">Necə oxumaq istəyirsən?</h2>
  <p class="section-lede">Hər seçimdə eyni mühazirələr var, fərq həcmdədir. İstədiyin vaxt bir mühazirənin başqa səviyyəsinə keçə bilərsən.</p></div></div>
  <div class="track-grid">
    {"".join(cards)}
  </div>
  {sources}
</section>'''
    return page(f"{c.title} · Qrup 596", body, 2, "page-course", c.summary)


def track_page(c: Course, u: Unit) -> str:
    """List page of one track: its lessons in order, plus links to the sibling tracks."""
    root = "../../../"
    rows = []
    for j, (plan, l) in enumerate(u.items, 1):
        if l:
            rows.append(f'<li><a class="lesson-row" href="../{l.slug}/index.html" data-lesson="{l.key}">'
                        f'<span class="lr-n">{j}</span><span class="lr-t">{e(l.title)}</span>'
                        f'<span class="lr-m">{fmt_minutes(l.minutes)}</span><span class="lr-check" aria-hidden="true"></span></a></li>')
        else:
            rows.append(f'<li><div class="lesson-row is-planned"><span class="lr-n">{j}</span>'
                        f'<span class="lr-t">{e(plan["title"])}</span>'
                        f'<span class="lr-m">tezliklə</span><span class="lr-lock" aria-hidden="true"></span></div></li>')
    switch = "".join(
        f'<a class="level-pill{" is-current" if x is u else ""}" href="../{track_target(x)}"'
        f'{" aria-current=" + chr(34) + "page" + chr(34) if x is u else ""}>{e(x.title)}</a>'
        for x in c.units)
    body = f'''
<section class="course-hero track-hero" style="--hue:{c.hue}">
  <div class="course-hero-bg" aria-hidden="true"><span class="ch-grid"></span><span class="ch-glow"></span></div>
  <div class="wrap course-hero-inner">
    <nav class="crumbs" data-rise style="--d:0" aria-label="Yer"><a href="{root}index.html">Ana səhifə</a><span>/</span><a href="../index.html">{e(c.title)}</a><span>/</span><span aria-current="page">{e(u.title)}</span></nav>
    <div class="ch-main">
      <div class="ch-icon" data-rise style="--d:1">{icon(u.icon)}</div>
      <div class="ch-copy">
        <span class="eyebrow" data-rise style="--d:1">{e(c.title)}{" · " + e(u.kicker) if u.kicker else ""}</span>
        <h1 class="ch-title" data-rise style="--d:2">{e(u.title)}</h1>
        <p class="ch-summary" data-rise style="--d:3">{e(u.summary)}</p>
        <nav class="level-switch" data-rise style="--d:4" aria-label="Səviyyə">{switch}</nav>
      </div>
    </div>
  </div>
</section>
<section class="wrap course-body is-tracks" style="--hue:{c.hue}">
  <div class="unit track-unit" data-reveal><ol class="lesson-list">{"".join(rows) or '<li class="lesson-empty">Bu bölmənin dərsləri hələ yazılmayıb.</li>'}</ol></div>
</section>'''
    return page(f"{u.title} · {c.title}", body, 3, "page-course", u.summary)


def course_page(c: Course) -> str:
    if c.layout == "tracks":
        return tracks_course_page(c)
    root = "../../"
    n = len(c.lessons)
    total = c.planned_total
    if c.units:
        units_html = []
        for k, u in enumerate(c.units, 1):
            rows = []
            for j, (plan, l) in enumerate(u.items, 1):
                num = f"{k}.{j}" if c.ordered or not plan else LESSON_KINDS[plan["kind"]]
                if l:
                    rows.append(
                        f'<li><a class="lesson-row" href="{l.slug}/index.html" data-lesson="{l.key}">'
                        f'<span class="lr-n">{num}</span><span class="lr-t">{e(l.title)}</span>'
                        f'<span class="lr-m">{fmt_minutes(l.minutes)}</span><span class="lr-check" aria-hidden="true"></span></a></li>')
                else:
                    objs = "".join(f'<span class="lr-obj">{e(o)}</span>' for o in plan["objectives"])
                    rows.append(
                        f'<li><div class="lesson-row is-planned"><span class="lr-n">{num}</span>'
                        f'<span class="lr-t">{e(plan["title"])}<span class="lr-objs">{objs}</span></span>'
                        f'<span class="lr-m">tezliklə</span><span class="lr-lock" aria-hidden="true"></span></div></li>')
            rows = "".join(rows) or '<li class="lesson-empty">Bu bölmənin dərsləri hələ yazılmayıb.</li>'
            if u.exam is not None:
                count = len(u.bank["questions"]) if u.bank else 0
                amount = str(count) if u.bank else e(u.exam["questions"])
                q = f'<span class="lr-exam-q">{amount} sual · bölmənin bütün mövzuları</span>' if amount else ""
                if u.bank:
                    rows += (f'<li><a class="lesson-row is-exam" href="exams/{u.id}/index.html">'
                             f'<span class="lr-n">İmtahan</span><span class="lr-t">{e(u.exam["title"])}{q}</span>'
                             f'<span class="lr-m">{count} sual</span></a></li>')
                else:
                    rows += (f'<li><div class="lesson-row is-planned is-exam"><span class="lr-n">İmtahan</span>'
                             f'<span class="lr-t">{e(u.exam["title"])}{q}</span>'
                             f'<span class="lr-m">tezliklə</span><span class="lr-lock" aria-hidden="true"></span></div></li>')
            written = len(u.lessons)
            meta = f"{written} / {len(u.items)} dərs" if u.plan else f"{written} dərs"
            if u.exam is not None:
                meta += " · imtahan"
            units_html.append(f'''<details class="unit" data-reveal style="--i:{k}" {"open" if k == 1 else ""}>
  <summary><span class="unit-n">{f"{k:02d}" if c.ordered else ""}</span><span class="unit-text"><span class="unit-title">{e(u.title)}</span>
  {f'<span class="unit-summary">{e(u.summary)}</span>' if u.summary else ''}</span>
  <span class="unit-meta">{meta}</span><span class="unit-chev" aria-hidden="true"></span></summary>
  <ol class="lesson-list{"" if c.ordered else " is-unordered"}">{rows}</ol>
</details>''')
        curriculum = "\n".join(units_html)
    else:
        curriculum = f'''<div class="empty" data-reveal>
  <div class="empty-art" aria-hidden="true">{logo_mark("empty-owl", eyes=True)}<span class="empty-ring"></span><span class="empty-ring r2"></span></div>
  <h3>Proqram hələ hazırlanmayıb</h3>
  <p>Bu fənnin mövzuları araşdırma bitəndən sonra bura bölmə-bölmə əlavə olunacaq. Səhifə hazırdır; çatışmayan yalnız məzmundur.</p>
  <ol class="pipeline">
    <li class="pl-step is-current"><span class="pl-dot"></span><span class="pl-t">Araşdırma</span><span class="pl-s">gözləyir</span></li>
    <li class="pl-step"><span class="pl-dot"></span><span class="pl-t">Proqram</span><span class="pl-s">—</span></li>
    <li class="pl-step"><span class="pl-dot"></span><span class="pl-t">Dərslər</span><span class="pl-s">—</span></li>
  </ol>
</div>'''
    sources = ""
    if c.sources:
        items = "".join(
            f'<li>{f"<a href={chr(34)}{e(s["url"])}{chr(34)} target={chr(34)}_blank{chr(34)} rel={chr(34)}noopener{chr(34)}>{e(s["title"])}</a>" if s.get("url") else e(s["title"])}'
            f'{f"<span>{e(s["note"])}</span>" if s.get("note") else ""}</li>' for s in c.sources)
        sources = f'<div class="side-card" data-reveal><h3>Mənbələr</h3><ul class="source-list">{items}</ul></div>'
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in c.tags)
    first = c.lessons[0] if c.lessons else None
    cta = (f'<a class="btn btn-lg" href="{first.slug}/index.html" data-course-cta="{c.slug}">Başla</a>' if first
           else '<span class="btn btn-lg btn-disabled" aria-disabled="true">Dərslər tezliklə</span>')
    body = f'''
<section class="course-hero" style="--hue:{c.hue}">
  <div class="course-hero-bg" aria-hidden="true"><span class="ch-grid"></span><span class="ch-glow"></span><canvas data-circuit></canvas></div>
  <div class="wrap course-hero-inner">
    <nav class="crumbs" data-rise style="--d:0" aria-label="Yer"><a href="{root}index.html">Ana səhifə</a><span>/</span><a href="{root}index.html#courses">Fənlər</a><span>/</span><span aria-current="page">{e(c.title)}</span></nav>
    <div class="ch-main">
      <div class="ch-icon" data-rise style="--d:1">{icon(c.icon)}</div>
      <div class="ch-copy">
        <span class="eyebrow" data-rise style="--d:1">{e(c.kicker)}</span>
        <h1 class="ch-title" data-rise style="--d:2">{e(c.title)}</h1>
        <p class="ch-summary" data-rise style="--d:3">{e(c.summary)}</p>
        <div class="cc-tags" data-rise style="--d:4">{tags}</div>
      </div>
      <div class="ch-progress" data-rise style="--d:3" data-progress-course="{c.slug}" data-total="{total}">
        <svg viewBox="0 0 120 120" class="ring" aria-hidden="true"><circle class="ring-bg" cx="60" cy="60" r="52"/><circle class="ring-fg" cx="60" cy="60" r="52" pathLength="100"/></svg>
        <div class="ring-label"><span class="pct">0%</span><span>tamamlandı</span></div>
      </div>
    </div>
    <dl class="ch-facts" data-rise style="--d:5">
      <div><dt>Bölmə</dt><dd>{len(c.units)}</dd></div>
      <div><dt>Dərs</dt><dd>{f"{n} / {total}" if total != n else n}</dd></div>
      <div><dt>Müddət</dt><dd>{fmt_minutes(c.minutes) if n else "—"}</dd></div>
      <div class="ch-cta">{cta}</div>
    </dl>
  </div>
</section>
<section class="wrap course-body" style="--hue:{c.hue}">
  <div class="curriculum">
    <div class="section-head compact" data-reveal><span class="section-index">01</span><div><h2 class="section-title">Proqram</h2></div></div>
    {curriculum}
  </div>
  <aside class="course-side">
    <div class="side-card" data-reveal>
      <h3>Bu fəndə</h3>
      <ul class="feature-list">
        <li><span class="fl-dot"></span>Mövzu izahı və sxemlər</li>
        <li><span class="fl-dot"></span>Addım-addım proseslər</li>
        <li><span class="fl-dot"></span>Təkrar kartları və uyğunlaşdırma</li>
        <li><span class="fl-dot"></span>İzahlı qısa testlər</li>
      </ul>
    </div>
    {sources}
  </aside>
</section>'''
    return page(f"{c.title} · Qrup 596", body, 2, "page-course", c.summary)


def lesson_page(l: Lesson) -> str:
    c = l.course
    root = "../../../"
    lessons = c.lessons
    idx = lessons.index(l)
    prev_l = lessons[idx - 1] if idx > 0 else None
    next_l = lessons[idx + 1] if idx + 1 < len(lessons) else None
    unit_no = [u.id for u in c.units].index(l.unit) + 1
    unit = c.units[unit_no - 1]
    plan_kind = next((p["kind"] for p in unit.plan if p["id"] == l.slug), None)
    unit_label = f"Bölmə {unit_no}" if c.ordered else e(unit.title)
    eyebrow = (f"Bölmə {unit_no} · {e(unit.title)}" if c.ordered or not plan_kind
               else f"{LESSON_KINDS[plan_kind]} · {e(unit.title)}")
    level_switch = ""
    if c.layout == "tracks":
        # prev/next and the sidebar stay inside the track; siblings at the same position form the level switch
        lessons = unit.lessons
        idx = lessons.index(l)
        prev_l = lessons[idx - 1] if idx > 0 else None
        next_l = lessons[idx + 1] if idx + 1 < len(lessons) else None
        pos = next((j for j, (_, x) in enumerate(unit.items) if x is l), 0)
        many = len(unit.items) > 1
        unit_label = f'<a href="../{unit.id}/index.html">{e(unit.title)}</a>' if many else e(unit.title)
        eyebrow = f"{e(unit.title)} · {pos + 1} / {len(unit.items)}" if many else e(unit.title)
        pills = []
        for x in c.units:
            if x is unit:
                pills.append(f'<span class="level-pill is-current" aria-current="page">{e(x.title)}</span>')
            elif len(x.items) > 1 and pos < len(x.items) and x.items[pos][1] and many:
                pills.append(f'<a class="level-pill" href="../{x.items[pos][1].slug}/index.html">{e(x.title)}</a>')
            elif len(x.items) == 1 and x.items[0][1]:
                pills.append(f'<a class="level-pill" href="../{x.items[0][1].slug}/index.html">{e(x.title)}</a>')
        if len(pills) > 1:
            level_switch = f'<nav class="level-switch" aria-label="Səviyyə"><span class="level-label">Səviyyə</span>{"".join(pills)}</nav>'

    nav_units = []
    for k, u in enumerate(c.units, 1):
        if not u.items or (c.layout == "tracks" and u is not unit):
            continue
        items = "".join(
            (f'<li><a href="../{x.slug}/index.html" data-lesson="{x.key}"{" aria-current=\"page\"" if x is l else ""}>'
             f'<span class="ln-check" aria-hidden="true"></span><span>{e(x.title)}</span></a></li>') if x else
            (f'<li><span class="ln-planned"><span class="ln-check" aria-hidden="true"></span><span>{e(plan["title"])}</span></span></li>')
            for plan, x in u.items)
        if u.exam is not None:
            if u.bank:
                items += (f'<li><a class="ln-exam" href="../exams/{u.id}/index.html"><span class="ln-check" aria-hidden="true"></span>'
                          f'<span>{e(u.exam["title"])} · {len(u.bank["questions"])} sual</span></a></li>')
            else:
                items += (f'<li><span class="ln-planned ln-exam"><span class="ln-check" aria-hidden="true"></span>'
                          f'<span>{e(u.exam["title"])}</span></span></li>')
        nav_units.append(f'<div class="ln-unit"><span class="ln-unit-t"><span>{f"{k:02d}" if c.ordered and c.layout != "tracks" else ""}</span>{e(u.title)}</span><ol>{items}</ol></div>')

    toc = "".join(
        f'<li class="toc-l{h["level"]}"><a href="#{h["id"]}">{re.sub(r"<[^>]+>", "", h["html"])}</a></li>'
        for h in l.headings)
    objectives = "".join(f'<span class="tag tag-obj">Hədəf {e(o)}</span>' for o in l.objectives)
    sources = "".join(
        f'<li>{f"<a href={chr(34)}{e(s["url"])}{chr(34)} target={chr(34)}_blank{chr(34)} rel={chr(34)}noopener{chr(34)}>{e(s["title"])}</a>" if s.get("url") else e(s["title"])}'
        f'{f"<span>{e(s["note"])}</span>" if s.get("note") else ""}</li>' for s in l.sources)

    def pn(x, label, cls):
        if not x:
            return f'<span class="pn {cls} pn-empty"></span>'
        return (f'<a class="pn {cls}" href="../{x.slug}/index.html"><span class="pn-l">{label}</span>'
                f'<span class="pn-t">{e(x.title)}</span></a>')

    body = f'''
<div class="lesson-shell" style="--hue:{c.hue}" data-lesson-page="{l.key}" data-lesson-title="{e(l.title)}">
  <aside class="lesson-nav" aria-label="Dərslər">
    <a class="ln-course" href="../index.html"><span class="ln-icon">{icon(c.icon)}</span><span><span class="ln-kicker">Fənn</span>{e(c.title)}</span></a>
    <div class="ln-progress" data-progress-course="{c.slug}" data-total="{c.planned_total}"><span class="bar"><span></span></span><span class="pct">0%</span></div>
    {"".join(nav_units)}
  </aside>
  <article class="lesson">
    <header class="lesson-head">
      <nav class="crumbs" aria-label="Yer"><a href="{root}index.html">Ana səhifə</a><span>/</span><a href="../index.html">{e(c.title)}</a><span>/</span><span>{unit_label}</span></nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1 class="lesson-title">{e(l.title)}</h1>
      <p class="lesson-summary">{e(l.summary)}</p>
      <div class="lesson-meta">
        <span class="lm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>{fmt_minutes(l.minutes)}</span>
        {objectives}
        <span class="lm lm-done" data-done-badge hidden>Tamamlandı</span>
      </div>
      {level_switch}
    </header>
    <div class="prose" data-prose>
{l.html}
    </div>
    <footer class="lesson-foot">
      <button class="complete-btn" type="button" data-complete>
        <span class="cb-box" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
        <span class="cb-text"><span class="cb-a">Dərsi bitirdim</span><span class="cb-b">Tamamlandı · geri al</span></span>
      </button>
      <div class="sources"><h2 class="sources-title">Mənbələr</h2><ol class="source-list">{sources}</ol>
      {f'<p class="updated">Son yenilənmə: {e(l.updated)}</p>' if l.updated else ''}</div>
      <nav class="prevnext" aria-label="Dərs naviqasiyası">{pn(prev_l, "Əvvəlki dərs", "pn-prev")}{pn(next_l, "Növbəti dərs", "pn-next")}</nav>
    </footer>
  </article>
  <aside class="lesson-toc" aria-label="Bu səhifədə">
    <div class="toc-inner"><span class="toc-title">Bu dərsdə</span><ol class="toc" data-toc>{toc}</ol></div>
  </aside>
</div>
<div class="lightbox" data-lightbox hidden><img alt=""><button type="button" class="lb-close" aria-label="Bağla">×</button></div>'''
    return page(f"{l.title} · {c.title}", body, 3, "page-lesson", l.summary)


def exam_page(c: Course, u: Unit) -> str:
    bank = u.bank
    questions = bank["questions"]
    lessons = {lesson.slug: lesson for lesson in u.lessons}
    ctx = Context(path=str((c.dir / "exams" / f"{u.id}.toml").relative_to(ROOT)))
    cards = []
    for number, q in enumerate(questions, 1):
        answers = q["answer"] if isinstance(q["answer"], list) else [q["answer"]]
        multiple = len(answers) > 1
        options = ''.join(
            f'<label class="choice"><input type="{"checkbox" if multiple else "radio"}" name="exam-q{number}" value="{j}">'
            f'<span class="choice-key">{chr(64 + j)}</span><span class="choice-t">{inline(value, ctx, number)}</span></label>'
            for j, value in enumerate(q["choices"], 1))
        cards.append(f'''<fieldset class="exam-question q" data-lesson="{e(q['lesson'])}" data-answer="{e(json.dumps(sorted(answers)))}">
  <legend class="q-prompt"><span class="q-n" data-number>{number}/{len(questions)}</span>{inline(q['prompt'], ctx, number)}{'<span class="q-multi">Birdən çox düzgün cavab</span>' if multiple else ''}</legend>
  <div class="choices">{options}</div>
  <div class="exam-feedback" hidden><p class="exam-choice-summary"></p><div class="q-explain">{inline(q['explain'], ctx, number)}</div></div>
</fieldset>''')
    lesson_links = ''.join(f'<li><a href="../../{lesson.slug}/index.html">{e(lesson.title)}</a></li>' for lesson in u.lessons)
    source_items = ''.join(
        f'<li>{f"<a href={chr(34)}{e(s["url"])}{chr(34)} target={chr(34)}_blank{chr(34)} rel={chr(34)}noopener{chr(34)}>{e(s["title"])}</a>" if s.get("url") else e(s["title"])}'
        f'{f"<span>{e(s["note"])}</span>" if s.get("note") else ""}</li>' for s in bank["sources"])
    body = f'''
<div class="exam-shell" style="--hue:{c.hue}" data-exam="{c.slug}/{u.id}">
  <nav class="crumbs" aria-label="Yer"><a href="../../../../index.html">Ana səhifə</a><span>/</span><a href="../../index.html">{e(c.title)}</a><span>/</span><span aria-current="page">{e(u.exam['title'])}</span></nav>
  <header class="lesson-head"><span class="eyebrow">{e(u.title)} · Bölmə imtahanı</span><h1 class="lesson-title">{e(u.exam['title'])}</h1><p class="lesson-summary">Bölmənin hamısını əhatə edən ümumi imtahan.</p></header>
  <section class="exam-start" data-exam-start aria-labelledby="exam-start-title"><h2 id="exam-start-title">Başlamazdan əvvəl</h2>
    <div class="exam-facts"><div><strong>{len(questions)}</strong><span>sual</span></div><div><strong>{len(u.lessons)}</strong><span>dərs</span></div><div><strong>~{math.ceil(len(questions) * 1.5)}</strong><span>dəqiqə</span></div></div>
    <p>Suallar hər cəhddə qarışdırılır. Cavab variantlarının sırası sabit qalır. Nəticə və izahlar bitirəndə açılır.</p>
    <p class="exam-last" data-exam-last hidden></p><button class="btn btn-lg" type="button" data-exam-begin>İmtahana başla</button>
  </section>
  <section class="exam-run" data-exam-run hidden aria-labelledby="exam-run-title"><div class="exam-run-head"><h2 id="exam-run-title">Suallar</h2><span data-exam-progress aria-live="polite">0 / {len(questions)} cavablandı</span></div>
    <form data-exam-form>{''.join(cards)}<div class="exam-submit"><p class="exam-warning" data-exam-warning role="status" hidden></p><button class="btn btn-lg" type="submit" data-exam-submit>İmtahanı bitir</button></div></form>
  </section>
  <section class="exam-result" data-exam-result hidden aria-labelledby="exam-result-title"><div class="exam-result-top"><span class="eyebrow">Nəticə</span><h2 id="exam-result-title" tabindex="-1">İmtahan bitdi</h2><p class="exam-score" data-exam-score></p><button class="btn btn-ghost" type="button" data-exam-retry>Yenidən cəhd et</button></div>
    <h3>Dərslərə görə nəticə</h3><div class="exam-breakdown" data-exam-breakdown></div><h3>Cavablara bax</h3><p>Aşağıdakı suallarda seçdiklərin, düzgün cavablar və izahlar göstərilir.</p></section>
  <aside class="exam-lessons"><h2>Bu bölmənin dərsləri</h2><ol>{lesson_links}</ol></aside>
  <section class="sources exam-sources"><h2 class="sources-title">Mənbələr</h2><ol class="source-list">{source_items}</ol><p class="updated">Son yenilənmə: {e(bank['updated'])}</p></section>
</div>'''
    data = {slug: {"title": lesson.title, "url": f"../../{slug}/index.html"} for slug, lesson in lessons.items()}
    head = (f'<script>window.Q596_EXAM_LESSONS = {json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")};</script>'
            f'<script defer src="../../../../assets/js/exam.js"></script>')
    return page(f"{u.exam['title']} · {c.title}", body, 4, "page-exam", extra_head=head)


def data_js(courses: list[Course]) -> str:
    data = {"courses": [
        {"id": c.slug, "title": c.title, "kicker": c.kicker, "hidden": c.hidden, "url": f"courses/{c.slug}/index.html",
         "lessons": [{"key": l.key, "title": l.title, "summary": l.summary,
                      "unit": next(u.title for u in c.units if u.id == l.unit),
                      "url": f"courses/{c.slug}/{l.slug}/index.html",
                      "headings": [re.sub(r"<[^>]+>", "", h["html"]) for h in l.headings]}
                     for l in c.lessons]}
        for c in courses]}
    return "window.Q596_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"


# ---------------------------------------------------------------- main

def build() -> dict:
    courses = load_all()
    for c in courses:
        for l in c.lessons:
            build_lesson_html(l, "../../../")

    tmp = ROOT / "site.tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    shutil.copytree(SRC / "assets", tmp / "assets")

    def write(rel: str, content: str):
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    write("index.html", home_page(courses))
    write("assets/js/data.js", data_js(courses))
    pages = 1
    for c in courses:
        write(f"courses/{c.slug}/index.html", course_page(c))
        pages += 1
        if (c.dir / "media").exists():
            shutil.copytree(c.dir / "media", tmp / "courses" / c.slug / "media")
        for l in c.lessons:
            write(f"courses/{c.slug}/{l.slug}/index.html", lesson_page(l))
            pages += 1
        for u in c.units:
            if c.layout == "tracks" and track_target(u) == f"{u.id}/index.html":
                write(f"courses/{c.slug}/{u.id}/index.html", track_page(c, u))
                pages += 1
            if u.bank:
                write(f"courses/{c.slug}/exams/{u.id}/index.html", exam_page(c, u))
                pages += 1

    if OUT.exists():
        shutil.rmtree(OUT)
    tmp.rename(OUT)
    return {"courses": len(courses), "lessons": sum(len(c.lessons) for c in courses), "pages": pages}


def main():
    try:
        stats = build()
    except (BuildError, ContentError) as err:
        print(f"BUILD FAILED\n  {err}", file=sys.stderr)
        sys.exit(1)
    print(f"built site/: {stats['courses']} courses, {stats['lessons']} lessons, {stats['pages']} pages")


if __name__ == "__main__":
    main()
