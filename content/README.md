# Writing content for qrup-596

This is the contract for every agent that adds courses or lessons. Follow it exactly; the build
enforces it and stops with `file:line: reason` when something is off.

**You never touch `src/`, `tools/` or `site/` to add content.** Only files under `content/`.

After every change:

```bash
python3 tools/check.py        # Windows: py tools\check.py
```

It must end with `check: N pages, M references, all resolve`. Then open `site/index.html`.

Requires Python 3.12+ (standard library only).

---

## 1. Layout

```
content/courses/<course-slug>/
  course.toml          course card, units, course-level sources
  lessons/             one Markdown file per lesson (nothing else in here)
    01-some-topic.md
  media/               images used by lessons (svg, png, jpg, webp, gif, avif)
```

- Folder and file names are lowercase slugs: `risk-management`, `03-risk-matrix.md`.
- The number prefix on a lesson file only sorts files on disk; the page URL drops it
  (`03-risk-matrix.md` → `courses/risk-management/risk-matrix/`). Lesson order on the site comes
  from `unit` + `order` in the frontmatter.
- `content/courses/guide/` is a hidden course that demonstrates every component. Read its
  lesson source next to its rendered page before writing your first lesson.

## 2. `course.toml`

```toml
title = "Risklərin idarə edilməsi"
kicker = "Magistratura · 1-ci semestr"           # small label above the title
summary = "One or two sentences."
hue = 192                                  # accent colour, 0-359 (OKLCH hue)
icon = "chip"                              # chip, globe, shield, code, network, book, compass, coin, spark
order = 1                                  # position on the home page
tags = ["Aralıq imtahanı"]
hidden = false                             # true keeps it off the home page and stats
ordered = true                             # false: no unit/lesson numbers; every planned lesson needs kind = "story" | "bundle"

[[unit]]                                   # units appear in this order
id = "basics"                            # slug, referenced by lessons
title = "Əsas anlayışlar"
summary = "Optional one-liner."

[[source]]                                 # optional, shown on the course page
title = "Course syllabus"
url = "https://..."
note = "Optional note"
```

A course with no `[[unit]]` shows the "curriculum not prepared yet" state. Add units when the
curriculum is decided, not before.

### Lesson plan inside a unit

A unit can list its planned lessons before they are written. Planned lessons appear greyed out
("yakında") on the course page and in the lesson sidebar, and course progress counts them.

```toml
[[unit]]
id = "inside-the-pc"
title = "Bilgisayarın içi"

  [[unit.lesson]]
  id = "motherboards"              # the lesson file must be named after this id
  title = "Anakartlar: form factor, slotlar, konnektörler"
  objectives = ["3.5"]
```

### Planned unit exam

A unit can announce an end-of-unit exam. It appears after the unit's lessons as a highlighted
"İmtahan · tezliklə" row on the course page and in the lesson sidebar. It does not count toward
course progress. The key goes right under the unit's `title`/`summary`, before its lessons:

```toml
[[unit]]
id = "inside-the-pc"
title = "Bilgisayarın içi"
exam = { questions = "50–70" }     # optional keys: title (default "Bölmə imtahanı"), questions
```

When a question bank exists at `exams/<unit-id>.toml`, the placeholder becomes a link to the exam
page. Banks must follow the approved exam format and pass `tools/check.py`. Do not write exam
questions unless the maintainer asks (rules in `AGENTS.md`, "Unit exams").

When a unit has a plan, the build enforces it: a lesson file in that unit must be named after a
planned id (`lessons/01-motherboards.md`), and its `order` must equal the id's position in the
plan (1-based). Planned ids are unique across the whole course.

## 3. Lesson file

```markdown
+++
title = "Risk matrisi"
unit = "basics"                  # must exist in course.toml
order = 3                          # unique inside the unit
summary = "One or two sentences shown under the title."
objectives = ["1.2", "1.3"]        # optional; syllabus topic numbers this lesson covers
updated = 2026-09-17               # optional

[[source]]                         # at least one, required
title = "Lecture 3 slides"
url = "https://..."
note = "Section 3.4"
+++

Lesson body in Markdown…
```

### Truth rules

- Every fact must come from a listed source. No source, no lesson.
- Topic and objective numbers come from the course syllabus or the lecturer's materials, never from memory.
- If sources disagree, say so in a `:::note` and name both.

### Reading a source PDF

Lecture slides and course PDFs are read through `tools/pdfpages.py`, a page range at a time,
never the whole file at once:

```bash
python3 tools/pdfpages.py path/to/lecture.pdf 12-30 --out pages.txt
```

- Page numbers are **PDF page numbers** as a PDF viewer shows them (1 = first page). Each page
  in the output is headed `===== PDF page 12 (printed page 10) =====`; cite the page in `note`.
- At most 60 pages per call.
- Output is text only: figures are missing and tables lose their layout. Do not describe a
  figure you have not seen.
- Needs `pymupdf` or `pypdf`. Not part of the build; `check.py` does not need it.
- Do not commit lecture PDFs unless the lecturer allows sharing them; the repo is public.

### Language

Visible text is Azerbaijani (Latin script: ə, ğ, ı, ö, ş, ü, ç). A technical term may keep its
English form in brackets the first time, e.g. *risk iştahı (risk appetite)*. Write for master's
students: no padding, no over-simplification.

## 4. Markdown that works

| Write | Result |
| --- | --- |
| `## Heading`, `### Sub-heading` | Section headings (they build the "Bu dərsdə" map). `#` and `####` are rejected. |
| `**bold**`, `*italic*`, `==highlight==` | Emphasis |
| `` `code` `` | Inline code |
| `++Ctrl+Shift+Esc++` | Keyboard keys |
| `[text](https://...)` | External link (only `http(s)://`, `#anchor`, `mailto:`) |
| `- item`, `1. item`, two-space indent for nesting | Lists |
| `> quote` | Quote |
| ```` ```powershell ```` … ```` ``` ```` | Code block with copy button |
| GFM pipe tables, `:---:` / `---:` for alignment | Table |
| `![alt](file.svg)` on its own line | Figure from `media/` |
| `---` | Divider |

**No raw HTML**, not even `<br>`. Angle brackets are fine inside backticks.

## 5. Components (directives)

A directive opens with `:::name optional title` on its own line and closes with `:::`.
Directives cannot be nested. Text-type directives take Markdown; data-type directives take TOML.
All string values inside TOML accept inline Markdown (bold, code, keys, links).

### Callouts (Markdown body)

```
:::note            general side note
:::tip             memory aid, practical advice
:::warning         common mistake, easily confused pair
:::exam            how the exam asks it, traps
:::example         concrete scenario
```

Give a custom title after the name: `:::tip Hatırlama tekniği`.

### `reveal` (Markdown body) — think first, then show

```
:::reveal Question the reader should answer in their head
The answer, in Markdown.
:::
```

### `figure`

```
:::figure
src = "raid-levels.svg"            # file in the course's media/ folder
alt = "What the image shows"       # required, describe it
caption = "Optional caption"
wide = true                        # optional, breaks out of the text column
:::
```

Prefer SVG you draw yourself for diagrams: dark background `#0d1118`, text `#e9e3d6`,
muted `#8f8a80`, lines `#262d3b`, amber `#f2b35b`. Never hotlink images from the web; download
only when the licence allows and note the origin in the lesson's sources.

### `steps` — ordered process (2+ steps)

```
:::steps Laser printing process
[[step]]
title = "Processing"
body = "Markdown text for this step."

[[step]]
title = "Charging"
body = "…"
:::
```

### `terms` — glossary

```
:::terms Kısaltmalar
[[term]]
name = "POST"
full = "Power-On Self-Test"        # optional
def = "What it is, one or two sentences."
:::
```

### `flashcards` — active recall

```
:::flashcards
[[card]]
front = "Question"
back = "Answer in **Markdown**"
:::
```

### `match` — pair two lists (2+ pairs; right side is shuffled on the page)

```
:::match Port numaralarını eşleştir
[[pair]]
left = "22"
right = "SSH"

[[pair]]
left = "443"
right = "HTTPS"
:::
```

### `quiz` — explained multiple choice

```
:::quiz
[[question]]
prompt = "Question text"
choices = ["A", "B", "C", "D"]
answer = 2                         # 1-based; use a list for multiple answers: [1, 3] (the "Birdən çox düzgün cavab" badge is added automatically; do not repeat it in the prompt)
explain = "Why the answer is right **and** why the tempting wrong one is wrong."
:::
```

Allowed keys are exactly the ones shown for each component; any other key is an error.

## 6. A good lesson

1. Opening paragraph: what this topic is and why it matters (2-4 sentences).
2. `##` sections of explanation, each with at least one table, figure, steps or terms block
   where it helps. Plain walls of text are the thing this site exists to avoid.
3. `:::exam` callouts where the exam has known traps.
4. A `:::reveal` or `:::flashcards` block mid-lesson for recall.
5. End with `:::quiz` (4-8 questions). Every `explain` teaches, it does not just repeat the
   answer.

Keep a lesson to roughly 10-25 minutes of reading. Split bigger topics into several lessons.
