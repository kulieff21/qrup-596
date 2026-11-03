"""Strict Markdown subset + qrup-596 directives -> HTML.

Lessons never carry raw HTML. Everything the page shows is produced here, so a lesson
written by any agent renders with the same markup the stylesheet and scripts expect.
Anything the parser does not understand is an error, not a silent pass-through.
"""
from __future__ import annotations

import html
import json
import re
import tomllib
from dataclasses import dataclass, field


class ContentError(Exception):
    def __init__(self, path: str, line: int, message: str):
        super().__init__(f"{path}:{line}: {message}")
        self.path, self.line, self.message = path, line, message


@dataclass
class Context:
    path: str                      # source file, for error messages
    media: callable = None         # media(name, line) -> relative URL, raises if missing
    headings: list = field(default_factory=list)
    counts: dict = field(default_factory=dict)
    ids: set = field(default_factory=set)

    def fail(self, line: int, message: str):
        raise ContentError(self.path, line, message)

    def uid(self, kind: str) -> str:
        n = self.counts.get(kind, 0) + 1
        self.counts[kind] = n
        return f"{kind}-{n}"


# ---------------------------------------------------------------- inline

_TR = str.maketrans("çğıöşüÇĞİÖŞÜâîûÂÎÛəƏ", "cgiosucgiosuaiuaiuee")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).translate(_TR).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "section"


_INLINE = re.compile(
    r"(?P<code>`+)(?P<code_body>.+?)(?P=code)"
    r"|\+\+(?P<kbd>[^\s+]\S*?)\+\+"
    r"|\*\*(?P<bold>.+?)\*\*"
    r"|==(?P<mark>.+?)=="
    r"|(?<![\w*])\*(?P<em>[^*\s][^*]*?)\*(?![\w*])"
    r"|\[(?P<link_text>[^\]]+)\]\((?P<link_url>[^)\s]+)\)"
)


def inline(text: str, ctx: Context, line: int) -> str:
    if "<" in text and re.search(r"</?[a-zA-Z][\w-]*(\s[^>]*)?/?>", re.sub(r"(`+).+?\1", "", text)):
        ctx.fail(line, "raw HTML is not allowed in lessons; use Markdown or a directive")
    out, pos = [], 0
    for m in _INLINE.finditer(text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        pos = m.end()
        if m.group("code"):
            out.append(f"<code>{html.escape(m.group('code_body').strip(), quote=False)}</code>")
        elif m.group("kbd"):
            keys = [html.escape(k.strip(), quote=False) for k in m.group("kbd").split("+")]
            out.append('<span class="keys">' + '<span class="plus">+</span>'.join(f"<kbd>{k}</kbd>" for k in keys) + "</span>")
        elif m.group("bold"):
            out.append(f"<strong>{inline(m.group('bold'), ctx, line)}</strong>")
        elif m.group("mark"):
            out.append(f"<mark>{inline(m.group('mark'), ctx, line)}</mark>")
        elif m.group("em"):
            out.append(f"<em>{inline(m.group('em'), ctx, line)}</em>")
        else:
            url = m.group("link_url")
            if not re.match(r"^(https?://|#|mailto:)", url):
                ctx.fail(line, f"link must be absolute http(s), #anchor or mailto: {url}")
            label = inline(m.group("link_text"), ctx, line)
            ext = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
            out.append(f'<a href="{html.escape(url)}"{ext}>{label}</a>')
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


# ---------------------------------------------------------------- blocks

_LIST_ITEM = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")
_TABLE_SEP = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
_DIRECTIVE = re.compile(r"^:::([a-z]+)(?:\s+(.*))?$")

CALLOUTS = {
    "note": "Qeyd",
    "tip": "Məsləhət",
    "warning": "Diqqət",
    "exam": "İmtahanda",
    "example": "Nümunə",
}


def render(text: str, ctx: Context, first_line: int = 1, allow_directives: bool = True,
           allow_headings: bool = True) -> str:
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    def ln(k: int) -> int:
        return first_line + k

    while i < n:
        raw = lines[i]
        s = raw.strip()

        if not s:
            i += 1
            continue

        # fenced code
        if s.startswith("```"):
            lang = s[3:].strip()
            start = i
            i += 1
            body = []
            while i < n and lines[i].strip() != "```":
                body.append(lines[i])
                i += 1
            if i >= n:
                ctx.fail(ln(start), "unclosed code fence")
            i += 1
            label = f'<span class="code-lang">{html.escape(lang)}</span>' if lang else ""
            out.append(
                f'<div class="codeblock">{label}<button class="code-copy" type="button" aria-label="Kopyala">Kopyala</button>'
                f'<pre><code>{html.escape(chr(10).join(body), quote=False)}</code></pre></div>'
            )
            continue

        # directive
        m = _DIRECTIVE.match(s)
        if m:
            if not allow_directives:
                ctx.fail(ln(i), "directives cannot be nested")
            name, arg = m.group(1), (m.group(2) or "").strip()
            start = i
            i += 1
            body = []
            in_fence = False
            while i < n:
                t = lines[i].strip()
                if t.startswith("```"):
                    in_fence = not in_fence
                if not in_fence and t == ":::":
                    break
                if not in_fence and _DIRECTIVE.match(t):
                    ctx.fail(ln(i), f"directive '{name}' opened on line {ln(start)} is not closed before a new one")
                body.append(lines[i])
                i += 1
            if i >= n:
                ctx.fail(ln(start), f"directive '{name}' is not closed with ':::'")
            i += 1
            out.append(directive(name, arg, "\n".join(body), ctx, ln(start) + 1))
            continue

        # headings
        hm = re.match(r"^(#{1,6})\s+(.*)$", s)
        if hm:
            level = len(hm.group(1))
            if not allow_headings:
                ctx.fail(ln(i), "headings are not allowed inside a component")
            if level not in (2, 3):
                ctx.fail(ln(i), "only ## and ### headings are allowed (the title comes from frontmatter)")
            title_html = inline(hm.group(2).strip(), ctx, ln(i))
            hid = slugify(title_html)
            base, k = hid, 2
            while hid in ctx.ids:
                hid = f"{base}-{k}"
                k += 1
            ctx.ids.add(hid)
            ctx.headings.append({"level": level, "id": hid, "html": title_html})
            anchor = f'<a class="h-anchor" href="#{hid}" aria-hidden="true" tabindex="-1">#</a>'
            out.append(f'<h{level} id="{hid}">{title_html}{anchor}</h{level}>')
            i += 1
            continue

        # rule
        if re.match(r"^(-{3,}|\*{3,})$", s):
            out.append('<hr>')
            i += 1
            continue

        # blockquote
        if s.startswith(">"):
            start = i
            body = []
            while i < n and lines[i].strip().startswith(">"):
                body.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{render(chr(10).join(body), ctx, ln(start), False, False)}</blockquote>")
            continue

        # table
        if s.startswith("|") and i + 1 < n and _TABLE_SEP.match(lines[i + 1].strip()):
            start = i
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append((i, lines[i].strip()))
                i += 1
            out.append(table(rows, ctx, first_line))
            continue

        # list
        if _LIST_ITEM.match(raw) and not re.match(r"^\s{4,}", raw):
            start = i
            block = []
            ordered = bool(re.match(r"\s*\d", raw))
            while i < n:
                t = lines[i]
                if not t.strip():
                    # a blank line ends the list unless the same kind of list continues right after
                    nxt = lines[i + 1] if i + 1 < n else ""
                    same = _LIST_ITEM.match(nxt) and bool(re.match(r"\s*\d", nxt)) == ordered
                    if same or (nxt.startswith("  ") and nxt.strip()):
                        i += 1
                        continue
                    break
                if _LIST_ITEM.match(t) or t.startswith("  "):
                    block.append((i, t))
                    i += 1
                    continue
                break
            out.append(list_block(block, ctx, first_line))
            continue

        # standalone image -> figure
        im = re.match(r"^!\[([^\]]*)\]\(([^)\s]+)\)$", s)
        if im:
            out.append(figure({"src": im.group(2), "alt": im.group(1)}, ctx, ln(i)))
            i += 1
            continue

        # paragraph
        start = i
        para = []
        while i < n:
            t = lines[i].strip()
            if (not t or t.startswith(("```", "#", ">", ":::", "|")) or _LIST_ITEM.match(lines[i])
                    or re.match(r"^(-{3,}|\*{3,})$", t)):
                break
            para.append(t)
            i += 1
        out.append(f"<p>{inline(' '.join(para), ctx, ln(start))}</p>")

    return "\n".join(out)


def list_block(items: list, ctx: Context, first_line: int) -> str:
    base_indent = len(items[0][1]) - len(items[0][1].lstrip())
    ordered = bool(re.match(r"\d", items[0][1].strip()))
    tag = "ol" if ordered else "ul"
    parts: list[str] = []
    current: list | None = None
    children: list = []

    def flush():
        if current is None:
            return
        idx, text = current
        inner = inline(text, ctx, first_line + idx)
        if children:
            inner += list_block(children, ctx, first_line)
        parts.append(f"<li>{inner}</li>")

    for idx, t in items:
        m = _LIST_ITEM.match(t)
        indent = len(t) - len(t.lstrip())
        if m and indent <= base_indent + 1:
            flush()
            current = [idx, m.group(3).strip()]
            children = []
        elif m:
            children.append((idx, t))
        else:
            if children:
                ctx.fail(first_line + idx, "continuation lines inside nested lists are not supported")
            if current is None:
                ctx.fail(first_line + idx, "list continuation without an item")
            current[1] += " " + t.strip()
    flush()
    return f"<{tag}>{''.join(parts)}</{tag}>"


def table(rows: list, ctx: Context, first_line: int) -> str:
    def cells(s: str) -> list[str]:
        s = s.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        return [c.strip() for c in re.split(r"(?<!\\)\|", s)]

    head_idx, head = rows[0]
    aligns = []
    for c in cells(rows[1][1]):
        aligns.append("center" if c.startswith(":") and c.endswith(":") else "right" if c.endswith(":") else "")
    header = cells(head)
    if len(header) != len(aligns):
        ctx.fail(first_line + head_idx, "table header and separator have different column counts")

    def cell(tag, content, k, idx):
        a = f' class="al-{aligns[k]}"' if k < len(aligns) and aligns[k] else ""
        return f"<{tag}{a}>{inline(content.replace(chr(92) + '|', '|'), ctx, first_line + idx)}</{tag}>"

    thead = "".join(cell("th", c, k, head_idx) for k, c in enumerate(header))
    body = []
    for idx, r in rows[2:]:
        cs = cells(r)
        if len(cs) != len(header):
            ctx.fail(first_line + idx, f"table row has {len(cs)} cells, header has {len(header)}")
        body.append("<tr>" + "".join(cell("td", c, k, idx) for k, c in enumerate(cs)) + "</tr>")
    return (f'<div class="table-wrap"><table><thead><tr>{thead}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


# ---------------------------------------------------------------- directives

def _toml(body: str, ctx: Context, line: int, name: str) -> dict:
    try:
        return tomllib.loads(body)
    except tomllib.TOMLDecodeError as e:
        ctx.fail(line, f"invalid TOML in '{name}': {e}")


def _require(obj: dict, keys: dict, ctx: Context, line: int, where: str):
    for key, typ in keys.items():
        if key not in obj:
            ctx.fail(line, f"{where}: missing '{key}'")
        if not isinstance(obj[key], typ):
            ctx.fail(line, f"{where}: '{key}' must be {typ.__name__ if isinstance(typ, type) else typ}")


def _only(obj: dict, allowed: set, ctx: Context, line: int, where: str):
    extra = set(obj) - allowed
    if extra:
        ctx.fail(line, f"{where}: unknown key(s) {sorted(extra)}; allowed {sorted(allowed)}")


def _md(text: str, ctx: Context, line: int) -> str:
    return render(text.strip(), ctx, line, allow_directives=False, allow_headings=False)


DATA_DIRECTIVES = ["figure", "steps", "flashcards", "quiz", "match", "terms"]


def directive(name: str, arg: str, body: str, ctx: Context, line: int) -> str:
    if name in CALLOUTS:
        title = inline(arg, ctx, line - 1) if arg else CALLOUTS[name]
        return (f'<aside class="callout callout-{name}" data-reveal>'
                f'<div class="callout-head"><span class="callout-icon" aria-hidden="true"></span>'
                f'<span class="callout-title">{title}</span></div>'
                f'<div class="callout-body">{_md(body, ctx, line)}</div></aside>')

    if name == "reveal":
        uid = ctx.uid("reveal")
        title = inline(arg, ctx, line - 1) if arg else "Əvvəlcə özün düşün"
        return (f'<div class="reveal" data-component="reveal" id="{uid}">'
                f'<div class="reveal-q">{title}</div>'
                f'<button type="button" class="btn btn-ghost reveal-btn">Cavabı göstər</button>'
                f'<div class="reveal-a" hidden>{_md(body, ctx, line)}</div></div>')

    if name not in DATA_DIRECTIVES:
        ctx.fail(line - 1, f"unknown directive ':::{name}'. Known: {', '.join(sorted(list(CALLOUTS) + ['reveal'] + DATA_DIRECTIVES))}")
    data = _toml(body, ctx, line, name)
    title = inline(arg, ctx, line - 1) if arg else ""

    if name == "figure":
        _only(data, {"src", "alt", "caption", "wide"}, ctx, line, "figure")
        return figure(data, ctx, line)

    if name == "steps":
        _only(data, {"step"}, ctx, line, "steps")
        steps = data.get("step")
        if not isinstance(steps, list) or len(steps) < 2:
            ctx.fail(line, "steps: needs at least two [[step]] tables")
        items = []
        for k, st in enumerate(steps, 1):
            _only(st, {"title", "body"}, ctx, line, f"steps[{k}]")
            _require(st, {"title": str, "body": str}, ctx, line, f"steps[{k}]")
            items.append(
                f'<li class="step" data-step="{k}"><button type="button" class="step-tab">'
                f'<span class="step-n">{k:02d}</span><span class="step-t">{inline(st["title"], ctx, line)}</span></button>'
                f'<div class="step-body">{_md(st["body"], ctx, line)}</div></li>'
            )
        head = f'<div class="comp-title">{title}</div>' if title else ""
        return (f'<div class="steps" data-component="steps" id="{ctx.uid("steps")}">{head}'
                f'<div class="steps-track"><span class="steps-fill"></span></div>'
                f'<ol class="steps-list">{"".join(items)}</ol>'
                f'<div class="steps-nav"><button type="button" class="btn btn-ghost" data-prev>Əvvəlki</button>'
                f'<span class="steps-count"></span><button type="button" class="btn" data-next>Növbəti</button></div></div>')

    if name == "flashcards":
        _only(data, {"card"}, ctx, line, "flashcards")
        cards = data.get("card")
        if not isinstance(cards, list) or not cards:
            ctx.fail(line, "flashcards: needs at least one [[card]]")
        items = []
        for k, c in enumerate(cards, 1):
            _only(c, {"front", "back"}, ctx, line, f"flashcards[{k}]")
            _require(c, {"front": str, "back": str}, ctx, line, f"flashcards[{k}]")
            items.append(
                f'<div class="card" data-card="{k}"><div class="card-inner">'
                f'<div class="card-face card-front"><span class="card-label">Sual</span><div>{inline(c["front"], ctx, line)}</div></div>'
                f'<div class="card-face card-back"><span class="card-label">Cavab</span><div>{_md(c["back"], ctx, line)}</div></div>'
                f'</div></div>'
            )
        head = title or "Təkrar kartları"
        return (f'<div class="flashcards" data-component="flashcards" id="{ctx.uid("flashcards")}">'
                f'<div class="comp-head"><div class="comp-title">{head}</div><div class="fc-count"></div></div>'
                f'<div class="fc-stage">{"".join(items)}</div>'
                f'<div class="fc-nav"><button type="button" class="btn btn-ghost" data-prev>Əvvəlki</button>'
                f'<button type="button" class="btn btn-ghost" data-flip>Çevir <span class="keys"><kbd>Space</kbd></span></button>'
                f'<button type="button" class="btn" data-next>Növbəti</button></div></div>')

    if name == "quiz":
        _only(data, {"question"}, ctx, line, "quiz")
        qs = data.get("question")
        if not isinstance(qs, list) or not qs:
            ctx.fail(line, "quiz: needs at least one [[question]]")
        items = []
        for k, q in enumerate(qs, 1):
            where = f"quiz question {k}"
            _only(q, {"prompt", "choices", "answer", "explain"}, ctx, line, where)
            _require(q, {"prompt": str, "choices": list, "explain": str}, ctx, line, where)
            if "answer" not in q:
                ctx.fail(line, f"{where}: missing 'answer'")
            choices = q["choices"]
            if len(choices) < 2 or not all(isinstance(c, str) for c in choices):
                ctx.fail(line, f"{where}: 'choices' must be at least two strings")
            answer = q["answer"] if isinstance(q["answer"], list) else [q["answer"]]
            if not answer or not all(type(a) is int and 1 <= a <= len(choices) for a in answer):
                ctx.fail(line, f"{where}: 'answer' must be a 1-based choice number or a list of them")
            multi = len(answer) > 1
            opts = "".join(
                f'<li><button type="button" class="choice" data-i="{j}">'
                f'<span class="choice-key">{chr(64 + j)}</span><span class="choice-t">{inline(c, ctx, line)}</span></button></li>'
                for j, c in enumerate(choices, 1)
            )
            hint = '<span class="q-multi">Birdən çox düzgün cavab</span>' if multi else ""
            items.append(
                f'<div class="q" data-answer="{html.escape(json.dumps(sorted(answer)))}" data-multi="{int(multi)}">'
                f'<div class="q-prompt"><span class="q-n">{k}/{len(qs)}</span>{inline(q["prompt"], ctx, line)}{hint}</div>'
                f'<ol class="choices">{opts}</ol>'
                f'<div class="q-actions"><button type="button" class="btn" data-check disabled>Yoxla</button></div>'
                f'<div class="q-explain" hidden>{_md(q["explain"], ctx, line)}</div></div>'
            )
        head = title or "Özünü yoxla"
        return (f'<div class="quiz" data-component="quiz" id="{ctx.uid("quiz")}">'
                f'<div class="comp-head"><div class="comp-title">{head}</div><div class="quiz-score" aria-live="polite"></div></div>'
                f'{"".join(items)}'
                f'<div class="quiz-result" hidden><div class="quiz-result-score"></div>'
                f'<button type="button" class="btn btn-ghost" data-retry>Yenidən həll et</button></div></div>')

    if name == "match":
        _only(data, {"pair"}, ctx, line, "match")
        pairs = data.get("pair")
        if not isinstance(pairs, list) or len(pairs) < 2:
            ctx.fail(line, "match: needs at least two [[pair]] tables")
        for k, p in enumerate(pairs, 1):
            _only(p, {"left", "right"}, ctx, line, f"match[{k}]")
            _require(p, {"left": str, "right": str}, ctx, line, f"match[{k}]")
        rights = sorted(range(len(pairs)), key=lambda k: slugify(pairs[k]["right"])[::-1])
        if rights == list(range(len(pairs))):
            rights = rights[1:] + rights[:1]
        left = "".join(f'<button type="button" class="m-item" data-k="{k}">{inline(p["left"], ctx, line)}</button>'
                       for k, p in enumerate(pairs))
        right = "".join(f'<button type="button" class="m-item" data-k="{k}">{inline(pairs[k]["right"], ctx, line)}</button>'
                        for k in rights)
        head = title or "Uyğunlaşdır"
        return (f'<div class="match" data-component="match" id="{ctx.uid("match")}">'
                f'<div class="comp-head"><div class="comp-title">{head}</div><div class="match-score" aria-live="polite"></div></div>'
                f'<p class="comp-hint">Soldan birini, sonra sağdan qarşılığını seç.</p>'
                f'<div class="match-grid"><div class="m-col m-left">{left}</div><div class="m-col m-right">{right}</div></div>'
                f'<div class="match-done" hidden><span>Hamısı uyğunlaşdı.</span><button type="button" class="btn btn-ghost" data-retry>Qarışdır və təkrarla</button></div></div>')

    if name == "terms":
        _only(data, {"term"}, ctx, line, "terms")
        terms = data.get("term")
        if not isinstance(terms, list) or not terms:
            ctx.fail(line, "terms: needs at least one [[term]]")
        items = []
        for k, t in enumerate(terms, 1):
            _only(t, {"name", "def", "full"}, ctx, line, f"terms[{k}]")
            _require(t, {"name": str, "def": str}, ctx, line, f"terms[{k}]")
            full = f'<span class="term-full">{inline(t["full"], ctx, line)}</span>' if t.get("full") else ""
            items.append(f'<div class="term" data-reveal><dt><span class="term-name">{inline(t["name"], ctx, line)}</span>{full}</dt>'
                         f'<dd>{inline(t["def"], ctx, line)}</dd></div>')
        head = f'<div class="comp-title">{title}</div>' if title else ""
        return f'<div class="terms">{head}<dl class="terms-grid">{"".join(items)}</dl></div>'

    ctx.fail(line - 1, f"unknown directive ':::{name}'. Known: {', '.join(sorted(list(CALLOUTS) + ['reveal', 'figure', 'steps', 'flashcards', 'quiz', 'match', 'terms']))}")


def figure(data: dict, ctx: Context, line: int) -> str:
    _require(data, {"src": str, "alt": str}, ctx, line, "figure")
    if not data["alt"].strip():
        ctx.fail(line, "figure: 'alt' must describe the image")
    if ctx.media is None:
        ctx.fail(line, "figures are not available here")
    url = ctx.media(data["src"], line)
    cap = data.get("caption")
    wide = " figure-wide" if data.get("wide") else ""
    caption = f"<figcaption>{inline(cap, ctx, line)}</figcaption>" if cap else ""
    return (f'<figure class="figure{wide}" data-reveal><button type="button" class="figure-zoom" aria-label="Böyüt">'
            f'<img src="{html.escape(url)}" alt="{html.escape(data["alt"])}" loading="lazy" decoding="async"></button>{caption}</figure>')
