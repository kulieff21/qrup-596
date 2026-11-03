/* qrup-596 — page behaviour. No dependencies; works from file:// and http. */
(() => {
  "use strict";

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => Array.from(el.querySelectorAll(s));
  const root = window.Q596_ROOT || "";
  const data = window.Q596_DATA || { courses: [] };
  const html = document.documentElement;
  const reducedQuery = matchMedia("(prefers-reduced-motion: reduce)");
  const motionOn = () => html.dataset.motion !== "off" && !(reducedQuery.matches && html.dataset.motion !== "on");
  const finePointer = matchMedia("(pointer: fine)").matches;

  /* ---------------------------------------------------------------- storage */

  const KEY = "qrup596:v1";
  const store = {
    read() {
      try {
        const s = JSON.parse(localStorage.getItem(KEY) || "{}");
        return { done: s.done || {}, answers: s.answers || {}, last: s.last || null };
      } catch (e) {
        return { done: {}, answers: {}, last: null };
      }
    },
    write(s) {
      try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* private mode: keep going */ }
    },
    update(fn) {
      const s = this.read();
      fn(s);
      this.write(s);
      return s;
    },
  };

  let toastTimer;
  function toast(msg) {
    const t = $("[data-toast]");
    if (!t) return;
    t.textContent = msg;
    t.classList.add("is-on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove("is-on"), 2200);
  }

  /* ---------------------------------------------------------------- ready + reveal */

  function ready() {
    requestAnimationFrame(() => html.classList.add("is-ready"));
  }
  if (document.fonts && document.fonts.ready) {
    Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 700))]).then(ready);
  } else {
    ready();
  }

  const revealIO = "IntersectionObserver" in window
    ? new IntersectionObserver((entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            en.target.classList.add("is-in");
            revealIO.unobserve(en.target);
          }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 })
    : null;
  $$("[data-reveal]").forEach((el) => (revealIO ? revealIO.observe(el) : el.classList.add("is-in")));

  /* ---------------------------------------------------------------- header */

  const header = $("[data-header]");
  const bar = $(".read-progress span");
  const prose = $("[data-prose]");
  function onScroll() {
    const y = window.scrollY;
    header && header.classList.toggle("is-scrolled", y > 10);
    if (bar && prose) {
      const r = prose.getBoundingClientRect();
      const total = r.height - window.innerHeight * 0.6;
      const p = Math.min(1, Math.max(0, (-r.top + window.innerHeight * 0.25) / Math.max(1, total)));
      bar.style.setProperty("--p", p.toFixed(4));
    }
    method();
  }
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------------------------------------------------------------- method line */

  const methodEl = $("[data-method]");
  function method() {
    if (!methodEl) return;
    const r = methodEl.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (window.innerHeight * 0.85 - r.top) / (window.innerHeight * 0.5)));
    methodEl.style.setProperty("--m", p.toFixed(3));
    $$(".method-step", methodEl).forEach((s, i, all) => s.classList.toggle("is-lit", p >= i / (all.length - 1) - 0.02));
  }

  /* ---------------------------------------------------------------- night sky (home hero) */

  function sky(canvas) {
    const ctx = canvas.getContext("2d");
    let w = 0, h = 0, dpr = 1, stars = [], shooting = null, raf = 0, visible = true;
    const pointer = { x: -9999, y: -9999, tx: 0, ty: 0, px: 0, py: 0 };

    function resize() {
      dpr = Math.min(2, window.devicePixelRatio || 1);
      const r = canvas.getBoundingClientRect();
      w = r.width; h = r.height;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const count = Math.round((w * h) / 5200);
      stars = Array.from({ length: count }, () => {
        const z = Math.random();
        return {
          x: Math.random() * w,
          y: Math.random() * h,
          z,
          r: 0.35 + z * 1.25,
          tw: Math.random() * Math.PI * 2,
          sp: 0.4 + Math.random() * 1.6,
          warm: Math.random() < 0.12,
        };
      });
    }

    function frame(t) {
      ctx.clearRect(0, 0, w, h);
      pointer.px += (pointer.tx - pointer.px) * 0.04;
      pointer.py += (pointer.ty - pointer.py) * 0.04;
      const time = t / 1000;
      const near = [];
      for (const s of stars) {
        s.x -= 0.02 + s.z * 0.06;
        if (s.x < -4) s.x = w + 4;
        const ox = s.x + pointer.px * s.z * 18;
        const oy = s.y + pointer.py * s.z * 12;
        const a = 0.25 + s.z * 0.55 + Math.sin(time * s.sp + s.tw) * 0.2;
        ctx.beginPath();
        ctx.arc(ox, oy, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.warm ? `rgba(255, 208, 138, ${a})` : `rgba(226, 232, 255, ${a})`;
        ctx.fill();
        if (s.z > 0.45) {
          const dx = ox - pointer.x, dy = oy - pointer.y;
          if (dx * dx + dy * dy < 170 * 170) near.push([ox, oy]);
        }
      }
      // constellation lines around the pointer
      ctx.lineWidth = 0.6;
      for (let i = 0; i < near.length; i++) {
        for (let j = i + 1; j < near.length; j++) {
          const dx = near[i][0] - near[j][0], dy = near[i][1] - near[j][1];
          const d = Math.sqrt(dx * dx + dy * dy);
          if (d < 95) {
            ctx.strokeStyle = `rgba(242, 179, 91, ${0.28 * (1 - d / 95)})`;
            ctx.beginPath();
            ctx.moveTo(near[i][0], near[i][1]);
            ctx.lineTo(near[j][0], near[j][1]);
            ctx.stroke();
          }
        }
      }
      // an occasional shooting star
      if (!shooting && Math.random() < 0.0025) {
        shooting = { x: Math.random() * w * 0.8 + w * 0.2, y: Math.random() * h * 0.4, life: 0 };
      }
      if (shooting) {
        shooting.life += 1;
        const L = shooting.life;
        const x = shooting.x - L * 9, y = shooting.y + L * 4;
        const g = ctx.createLinearGradient(x, y, x + 90, y - 40);
        const fade = Math.max(0, 1 - L / 50);
        g.addColorStop(0, `rgba(255, 236, 200, ${0.9 * fade})`);
        g.addColorStop(1, "rgba(255, 236, 200, 0)");
        ctx.strokeStyle = g;
        ctx.lineWidth = 1.4;
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + 90, y - 40);
        ctx.stroke();
        if (L > 50) shooting = null;
      }
      if (motionOn() && visible) raf = requestAnimationFrame(frame);
    }

    function start() {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(frame);
    }

    resize();
    start();
    window.addEventListener("resize", () => { resize(); start(); });
    const hero = canvas.parentElement;
    hero.addEventListener("pointermove", (e) => {
      const r = canvas.getBoundingClientRect();
      pointer.x = e.clientX - r.left;
      pointer.y = e.clientY - r.top;
      pointer.tx = (pointer.x / w - 0.5) * 2;
      pointer.ty = (pointer.y / h - 0.5) * 2;
    });
    hero.addEventListener("pointerleave", () => { pointer.x = pointer.y = -9999; });
    new IntersectionObserver(([en]) => {
      visible = en.isIntersecting;
      if (visible) start();
    }).observe(canvas);
    document.addEventListener("visibilitychange", () => { if (!document.hidden) start(); });
    return start;
  }

  /* ---------------------------------------------------------------- owl eyes */

  function owls() {
    const list = $$("[data-owl]");
    if (!list.length) return;
    document.addEventListener("pointermove", (e) => {
      if (!motionOn()) return;
      list.forEach((svg) => {
        const r = svg.getBoundingClientRect();
        const cx = r.left + r.width / 2, cy = r.top + r.height * 0.53;
        const dx = e.clientX - cx, dy = e.clientY - cy;
        const d = Math.hypot(dx, dy) || 1;
        const k = Math.min(1, d / 260) * 4.6;
        const p = $(".owl-pupils", svg);
        p.style.transform = `translate(${(dx / d) * k}px, ${(dy / d) * k}px)`;
      });
    });
    const blink = () => {
      if (motionOn()) {
        list.forEach((svg) => {
          svg.classList.remove("owl-blink");
          void svg.getBoundingClientRect();
          svg.classList.add("owl-blink");
        });
      }
      setTimeout(blink, 2600 + Math.random() * 4200);
    };
    setTimeout(blink, 3200);
  }

  /* ---------------------------------------------------------------- count up */

  function countUp(el, to) {
    if (!motionOn() || to === 0) { el.textContent = to; return; }
    const t0 = performance.now(), dur = 1400;
    const step = (t) => {
      const p = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 4)));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  /* ---------------------------------------------------------------- course cards */

  function cards() {
    $$("[data-tilt]").forEach((card) => {
      card.addEventListener("pointermove", (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        card.style.setProperty("--mx", `${x * 100}%`);
        card.style.setProperty("--my", `${y * 100}%`);
        if (motionOn() && finePointer) {
          card.style.setProperty("--rx", `${(0.5 - y) * 7}deg`);
          card.style.setProperty("--ry", `${(x - 0.5) * 9}deg`);
        }
      });
      card.addEventListener("pointerleave", () => {
        card.style.setProperty("--rx", "0deg");
        card.style.setProperty("--ry", "0deg");
      });
    });
  }

  /* ---------------------------------------------------------------- circuit (course hero) */

  function circuit(canvas) {
    const ctx = canvas.getContext("2d");
    const hue = getComputedStyle(canvas.closest("[style]")).getPropertyValue("--hue").trim() || "200";
    let w, h, dpr, traces = [], pulses = [], raf = 0, visible = true;
    const G = 44;

    function resize() {
      dpr = Math.min(2, window.devicePixelRatio || 1);
      const r = canvas.getBoundingClientRect();
      w = r.width; h = r.height;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      traces = [];
      const n = Math.round(w / 90);
      for (let i = 0; i < n; i++) {
        let x = Math.round((w * 0.35 + Math.random() * w * 0.65) / G) * G;
        let y = Math.round((Math.random() * h) / G) * G;
        const pts = [[x, y]];
        let dir = Math.random() < 0.5 ? 0 : 1;
        for (let k = 0; k < 4 + Math.random() * 4; k++) {
          const len = G * (1 + Math.floor(Math.random() * 4));
          if (dir === 0) x += Math.random() < 0.5 ? len : -len; else y += Math.random() < 0.5 ? len : -len;
          pts.push([x, y]);
          dir = 1 - dir;
        }
        let total = 0;
        for (let k = 1; k < pts.length; k++) total += Math.abs(pts[k][0] - pts[k - 1][0]) + Math.abs(pts[k][1] - pts[k - 1][1]);
        traces.push({ pts, total });
      }
      pulses = traces.map((t) => ({ t, pos: Math.random() * t.total, sp: 0.6 + Math.random() * 1.2 }));
    }

    function at(tr, dist) {
      let d = dist;
      for (let k = 1; k < tr.pts.length; k++) {
        const [x0, y0] = tr.pts[k - 1], [x1, y1] = tr.pts[k];
        const seg = Math.abs(x1 - x0) + Math.abs(y1 - y0);
        if (d <= seg) {
          const f = d / seg;
          return [x0 + (x1 - x0) * f, y0 + (y1 - y0) * f];
        }
        d -= seg;
      }
      return tr.pts[tr.pts.length - 1];
    }

    function frame() {
      ctx.clearRect(0, 0, w, h);
      ctx.lineWidth = 1;
      for (const tr of traces) {
        ctx.strokeStyle = `oklch(0.8 0.1 ${hue} / 0.10)`;
        ctx.beginPath();
        tr.pts.forEach(([x, y], k) => (k ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
        ctx.stroke();
        const [ex, ey] = tr.pts[tr.pts.length - 1];
        ctx.fillStyle = `oklch(0.8 0.1 ${hue} / 0.25)`;
        ctx.beginPath();
        ctx.arc(ex, ey, 2.2, 0, Math.PI * 2);
        ctx.fill();
      }
      for (const p of pulses) {
        p.pos += p.sp;
        if (p.pos > p.t.total) p.pos = 0;
        for (let k = 0; k < 14; k++) {
          const [x, y] = at(p.t, Math.max(0, p.pos - k * 3));
          ctx.fillStyle = `oklch(0.85 0.13 ${hue} / ${0.75 * (1 - k / 14)})`;
          ctx.beginPath();
          ctx.arc(x, y, 1.6 - k * 0.07, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      if (motionOn() && visible) raf = requestAnimationFrame(frame);
    }
    const start = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(frame); };
    resize();
    start();
    window.addEventListener("resize", () => { resize(); start(); });
    new IntersectionObserver(([en]) => { visible = en.isIntersecting; if (visible) start(); }).observe(canvas);
  }

  /* ---------------------------------------------------------------- progress */

  function lessonsOf(courseId) {
    const c = data.courses.find((x) => x.id === courseId);
    return c ? c.lessons : [];
  }

  function paintProgress() {
    const s = store.read();
    $$("[data-progress-course]").forEach((el) => {
      const lessons = lessonsOf(el.dataset.progressCourse);
      const done = lessons.filter((l) => s.done[l.key]).length;
      const total = +el.dataset.total || lessons.length;
      const p = total ? Math.min(1, done / total) : 0;
      el.style.setProperty("--p", p);
      $$(".bar > span", el).forEach((b) => b.style.setProperty("--p", p));
      const pct = $(".pct", el);
      if (pct) pct.textContent = `${Math.round(p * 100)}%`;
    });
    $$("[data-lesson]").forEach((el) => el.classList.toggle("is-done", !!s.done[el.dataset.lesson]));
    const doneStat = $('[data-stat="done"]');
    if (doneStat) {
      const visibleKeys = new Set(data.courses.filter((c) => !c.hidden).flatMap((c) => c.lessons.map((l) => l.key)));
      countUp(doneStat, Object.keys(s.done).filter((k) => visibleKeys.has(k)).length);
    }
    const answered = $('[data-stat="answered"]');
    if (answered) countUp(answered, Object.keys(s.answers).length);
    const resume = $("[data-resume]");
    if (resume && s.last) {
      resume.hidden = false;
      resume.href = root + s.last.url;
      $(".resume-title", resume).textContent = `· ${s.last.title}`;
    }
  }

  /* ---------------------------------------------------------------- lesson page */

  function lessonPage(shell) {
    const key = shell.dataset.lessonPage;
    const course = key.split("/")[0];
    const lesson = lessonsOf(course).find((l) => l.key === key);
    if (lesson) {
      store.update((s) => { s.last = { key, title: lesson.title, url: lesson.url }; });
    }

    const btn = $("[data-complete]");
    const badge = $("[data-done-badge]");
    const sync = () => {
      const done = !!store.read().done[key];
      btn.classList.toggle("is-done", done);
      badge.hidden = !done;
    };
    btn.addEventListener("click", () => {
      const s = store.update((st) => {
        if (st.done[key]) delete st.done[key];
        else st.done[key] = Date.now();
      });
      sync();
      paintProgress();
      toast(s.done[key] ? "Dərs tamamlanmış kimi qeyd olundu" : "Qeyd götürüldü");
    });
    sync();

    // table of contents scrollspy
    const toc = $("[data-toc]");
    if (toc) {
      const links = $$("a", toc);
      const heads = links.map((a) => document.getElementById(a.hash.slice(1))).filter(Boolean);
      const setActive = () => {
        let cur = heads[0];
        for (const h of heads) if (h.getBoundingClientRect().top < window.innerHeight * 0.3) cur = h;
        links.forEach((a) => a.classList.toggle("is-active", cur && a.hash === "#" + cur.id));
        const act = links.find((a) => a.classList.contains("is-active"));
        if (act) {
          toc.style.setProperty("--t", `${act.offsetTop}px`);
          toc.style.setProperty("--h", `${act.offsetHeight}px`);
        }
      };
      window.addEventListener("scroll", setActive, { passive: true });
      setActive();
    }

    // copy buttons
    $$(".code-copy").forEach((b) => b.addEventListener("click", async () => {
      const text = b.parentElement.querySelector("code").textContent;
      try {
        await navigator.clipboard.writeText(text);
      } catch (e) {
        const ta = document.createElement("textarea");
        ta.value = text; document.body.append(ta); ta.select(); document.execCommand("copy"); ta.remove();
      }
      b.textContent = "Kopyalandı";
      setTimeout(() => (b.textContent = "Kopyala"), 1600);
    }));

    // lightbox
    const lb = $("[data-lightbox]");
    $$(".figure-zoom").forEach((f) => f.addEventListener("click", () => {
      const img = $("img", f);
      $("img", lb).src = img.src;
      $("img", lb).alt = img.alt;
      lb.hidden = false;
    }));
    lb && lb.addEventListener("click", () => (lb.hidden = true));

    $$('[data-component="steps"]').forEach(stepsC);
    $$('[data-component="flashcards"]').forEach(flashC);
    $$('[data-component="quiz"]').forEach((q) => quizC(q, key));
    $$('[data-component="match"]').forEach(matchC);
    $$('[data-component="reveal"]').forEach((r) => $(".reveal-btn", r).addEventListener("click", () => {
      r.classList.add("is-open");
      $(".reveal-a", r).hidden = false;
    }));
  }

  function stepsC(el) {
    const steps = $$(".step", el);
    const fill = $(".steps-fill", el);
    const count = $(".steps-count", el);
    const prev = $("[data-prev]", el), next = $("[data-next]", el);
    let cur = 0;
    const go = (i) => {
      cur = Math.max(0, Math.min(steps.length - 1, i));
      steps.forEach((s, k) => {
        s.classList.toggle("is-active", k === cur);
        s.classList.toggle("is-done", k < cur);
      });
      fill.style.setProperty("--p", (cur + 1) / steps.length);
      count.textContent = `${cur + 1} / ${steps.length}`;
      prev.disabled = cur === 0;
      next.textContent = cur === steps.length - 1 ? "Yenidən" : "Növbəti";
    };
    steps.forEach((s, k) => $(".step-tab", s).addEventListener("click", () => go(k)));
    prev.addEventListener("click", () => go(cur - 1));
    next.addEventListener("click", () => go(cur === steps.length - 1 ? 0 : cur + 1));
    go(0);
  }

  function flashC(el) {
    const cards = $$(".card", el);
    const count = $(".fc-count", el);
    let order = cards.map((_, i) => i), cur = 0;
    const paint = () => {
      cards.forEach((c) => c.classList.remove("is-current", "is-next", "is-next2"));
      const c0 = cards[order[cur]];
      c0.classList.add("is-current");
      if (order.length > 1) cards[order[(cur + 1) % order.length]].classList.add("is-next");
      if (order.length > 2) cards[order[(cur + 2) % order.length]].classList.add("is-next2");
      count.textContent = `${cur + 1} / ${order.length}`;
    };
    const move = (d) => {
      const leaving = cards[order[cur]];
      leaving.classList.add("is-leaving");
      setTimeout(() => leaving.classList.remove("is-leaving", "is-flipped"), 450);
      cur = (cur + d + order.length) % order.length;
      paint();
    };
    const flip = () => cards[order[cur]].classList.toggle("is-flipped");
    cards.forEach((c) => c.addEventListener("click", flip));
    $("[data-flip]", el).addEventListener("click", flip);
    $("[data-next]", el).addEventListener("click", () => move(1));
    $("[data-prev]", el).addEventListener("click", () => move(-1));
    el.tabIndex = 0;
    el.addEventListener("keydown", (e) => {
      if (e.target !== el) return;
      if (e.key === " ") { e.preventDefault(); flip(); }
      if (e.key === "ArrowRight") move(1);
      if (e.key === "ArrowLeft") move(-1);
    });
    paint();
  }

  function quizC(el, lessonKey) {
    const qs = $$(".q", el);
    const score = $(".quiz-score", el);
    const result = $(".quiz-result", el);
    const answered = () => qs.filter((q) => q.classList.contains("is-checked"));
    const paint = () => {
      const a = answered();
      const right = a.filter((q) => q.classList.contains("is-correct")).length;
      score.textContent = a.length ? `${right} / ${a.length} düzgün` : `${qs.length} sual`;
      if (a.length === qs.length) {
        const pct = Math.round((right / qs.length) * 100);
        const note = pct === 100 ? "Qüsursuz." : pct >= 70 ? "Yaxşı gedir; səhvlərinin izahlarına bir də bax." : "Dərsin uyğun hissəsinə qayıdıb yenidən cəhd et.";
        $(".quiz-result-score", el).innerHTML = `${right} / ${qs.length} <small>%${pct} · ${note}</small>`;
        result.hidden = false;
      } else {
        result.hidden = true;
      }
    };
    qs.forEach((q, qi) => {
      const answer = JSON.parse(q.dataset.answer);
      const multi = q.dataset.multi === "1";
      const check = $("[data-check]", q);
      const choices = $$(".choice", q);
      choices.forEach((c) => c.addEventListener("click", () => {
        if (!multi) choices.forEach((o) => o !== c && o.classList.remove("is-picked"));
        if (multi) c.classList.toggle("is-picked"); else c.classList.add("is-picked");
        check.disabled = !choices.some((o) => o.classList.contains("is-picked"));
      }));
      check.addEventListener("click", () => {
        const picked = choices.filter((c) => c.classList.contains("is-picked")).map((c) => +c.dataset.i);
        const ok = picked.length === answer.length && picked.every((i) => answer.includes(i));
        choices.forEach((c) => {
          const i = +c.dataset.i;
          const isAns = answer.includes(i), isPicked = picked.includes(i);
          c.classList.toggle("is-right", isAns && isPicked);
          c.classList.toggle("is-wrong", !isAns && isPicked);
          c.classList.toggle("is-missed", isAns && !isPicked);
          if (isAns && !isPicked && !multi) c.classList.add("is-right");
        });
        q.classList.add("is-checked", ok ? "is-correct" : "is-incorrect");
        $(".q-explain", q).hidden = false;
        store.update((s) => { s.answers[`${lessonKey}#${el.id}#${qi}`] = ok ? 1 : 0; });
        paint();
        const nextQ = qs[qi + 1];
        if (nextQ && !nextQ.classList.contains("is-checked")) {
          setTimeout(() => {
            const r = nextQ.getBoundingClientRect();
            if (r.top > window.innerHeight * 0.85) window.scrollBy({ top: r.top - window.innerHeight * 0.35, behavior: "smooth" });
          }, 600);
        }
      });
    });
    $("[data-retry]", el).addEventListener("click", () => {
      qs.forEach((q) => {
        q.classList.remove("is-checked", "is-correct", "is-incorrect");
        $$(".choice", q).forEach((c) => c.classList.remove("is-picked", "is-right", "is-wrong", "is-missed"));
        $("[data-check]", q).disabled = true;
        $(".q-explain", q).hidden = true;
      });
      paint();
      el.scrollIntoView({ behavior: motionOn() ? "smooth" : "auto", block: "start" });
    });
    paint();
  }

  function matchC(el) {
    const leftCol = $(".m-left", el), rightCol = $(".m-right", el);
    const score = $(".match-score", el);
    const done = $(".match-done", el);
    let pick = null, matched = 0, n = $$(".m-item", leftCol).length;
    const shuffle = (col) => {
      const items = $$(".m-item", col);
      for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
      }
      items.forEach((it) => col.append(it));
    };
    const paint = () => { score.textContent = `${matched} / ${n}`; done.hidden = matched < n; };
    const wrong = (a, b) => {
      [a, b].forEach((x) => { x.classList.remove("is-wrong"); void x.offsetWidth; x.classList.add("is-wrong"); });
      setTimeout(() => [a, b].forEach((x) => x.classList.remove("is-wrong", "is-picked")), 500);
    };
    $$(".m-item", el).forEach((it) => it.addEventListener("click", () => {
      if (it.classList.contains("is-matched")) return;
      if (!pick) { pick = it; it.classList.add("is-picked"); return; }
      if (pick === it) { it.classList.remove("is-picked"); pick = null; return; }
      if (pick.parentElement === it.parentElement) {
        pick.classList.remove("is-picked");
        pick = it; it.classList.add("is-picked");
        return;
      }
      if (pick.dataset.k === it.dataset.k) {
        matched += 1;
        [pick, it].forEach((x) => { x.classList.remove("is-picked"); x.classList.add("is-matched"); x.dataset.pair = matched; });
      } else {
        wrong(pick, it);
      }
      pick = null;
      paint();
    }));
    $("[data-retry]", el).addEventListener("click", () => {
      $$(".m-item", el).forEach((x) => { x.classList.remove("is-matched", "is-picked"); delete x.dataset.pair; });
      matched = 0; pick = null;
      shuffle(rightCol);
      paint();
    });
    shuffle(rightCol);
    paint();
  }

  /* ---------------------------------------------------------------- search palette */

  function norm(s) {
    return s.toLocaleLowerCase("az").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ı/g, "i").replace(/ə/g, "e");
  }

  function searchPalette() {
    const box = $("[data-search]");
    if (!box) return;
    const input = $("[data-search-input]", box);
    const list = $("[data-search-results]", box);
    const items = [];
    data.courses.forEach((c) => {
      if (!c.hidden) items.push({ kind: "Fənn", title: c.title, sub: c.kicker, url: c.url, hay: norm(`${c.title} ${c.kicker}`) });
      c.lessons.forEach((l) => items.push({
        kind: c.hidden ? "Bələdçi" : `Dərs · ${c.title}`, title: l.title, sub: l.unit, url: l.url,
        hay: norm(`${l.title} ${l.summary} ${l.unit} ${l.headings.join(" ")}`),
      }));
    });
    let active = 0, results = [];
    const escape = (s) => s.replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
    const render = () => {
      const q = norm(input.value.trim());
      const words = q.split(/\s+/).filter(Boolean);
      results = words.length ? items.filter((it) => words.every((w) => it.hay.includes(w))) : items.slice(0, 8);
      active = 0;
      if (!results.length) {
        list.innerHTML = `<li class="search-empty">"${escape(input.value)}" üçün nəticə yoxdur.</li>`;
        return;
      }
      list.innerHTML = results.slice(0, 20).map((r, i) =>
        `<li><a href="${root}${r.url}" class="${i === 0 ? "is-active" : ""}"><span class="sr-kind">${escape(r.kind)}</span>` +
        `<span class="sr-title">${escape(r.title)}</span><span class="sr-sub">${escape(r.sub)}</span></a></li>`).join("");
    };
    const setActive = (i) => {
      const links = $$("a", list);
      if (!links.length) return;
      active = (i + links.length) % links.length;
      links.forEach((a, k) => a.classList.toggle("is-active", k === active));
      links[active].scrollIntoView({ block: "nearest" });
    };
    const open = () => { box.hidden = false; input.value = ""; render(); setTimeout(() => input.focus(), 10); };
    const close = () => { box.hidden = true; };
    $$("[data-search-open]").forEach((b) => b.addEventListener("click", open));
    $$("[data-search-close]").forEach((b) => b.addEventListener("click", close));
    input.addEventListener("input", render);
    document.addEventListener("keydown", (e) => {
      const typing = /INPUT|TEXTAREA/.test(document.activeElement.tagName);
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); box.hidden ? open() : close(); return; }
      if (e.key === "/" && !typing && box.hidden) { e.preventDefault(); open(); return; }
      if (box.hidden) {
        if (e.key === "Escape") { const lb = $("[data-lightbox]"); if (lb) lb.hidden = true; }
        return;
      }
      if (e.key === "Escape") close();
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(active + 1); }
      if (e.key === "ArrowUp") { e.preventDefault(); setActive(active - 1); }
      if (e.key === "Enter") { const a = $$("a", list)[active]; if (a) location.href = a.href; }
    });
  }

  /* ---------------------------------------------------------------- motion toggle */

  function motionToggle() {
    $$("[data-motion-toggle]").forEach((b) => {
      const label = $("span", b);
      const paint = () => (label.textContent = motionOn() ? "açıq" : "bağlı");
      b.addEventListener("click", () => {
        const next = motionOn() ? "off" : "on";
        html.dataset.motion = next;
        try { localStorage.setItem("qrup596:motion", next); } catch (e) {}
        paint();
        restartSky && restartSky();
        toast(next === "off" ? "Animasiyalar söndürüldü" : "Animasiyalar yandırıldı");
      });
      paint();
    });
  }

  /* ---------------------------------------------------------------- page transitions */

  function transitions() {
    document.addEventListener("click", (e) => {
      const a = e.target.closest("a[href]");
      if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      if (a.target === "_blank" || a.hasAttribute("download") || !motionOn()) return;
      const url = new URL(a.href, location.href);
      const here = new URL(location.href);
      if (url.protocol !== here.protocol || url.host !== here.host) return;
      if (url.pathname === here.pathname && url.hash) return;
      e.preventDefault();
      html.classList.add("is-leaving");
      setTimeout(() => (location.href = url.href), 200);
    });
    // coming back through the history cache must not leave the page faded out
    window.addEventListener("pageshow", (e) => { if (e.persisted) html.classList.remove("is-leaving"); });
  }

  /* ---------------------------------------------------------------- boot */

  let restartSky = null;
  const skyCanvas = $("[data-sky]");
  if (skyCanvas) restartSky = sky(skyCanvas);
  const circuitCanvas = $("[data-circuit]");
  if (circuitCanvas) circuit(circuitCanvas);
  owls();
  cards();
  $$("[data-count]").forEach((el) => {
    const io = new IntersectionObserver(([en]) => {
      if (en.isIntersecting) { countUp(el, +el.dataset.count); io.disconnect(); }
    });
    io.observe(el);
  });
  const shell = $("[data-lesson-page]");
  if (shell) lessonPage(shell);
  paintProgress();
  searchPalette();
  motionToggle();
  transitions();
  onScroll();
})();
