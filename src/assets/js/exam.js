(() => {
  const shell = document.querySelector("[data-exam]");
  if (!shell) return;
  const start = shell.querySelector("[data-exam-start]");
  const run = shell.querySelector("[data-exam-run]");
  const result = shell.querySelector("[data-exam-result]");
  const form = shell.querySelector("[data-exam-form]");
  const cards = [...shell.querySelectorAll(".exam-question")];
  const warning = shell.querySelector("[data-exam-warning]");
  const submit = shell.querySelector("[data-exam-submit]");
  const progress = shell.querySelector("[data-exam-progress]");
  const key = `qrup596:exam:${shell.dataset.exam}`;
  const lessons = window.Q596_EXAM_LESSONS || {};
  const storage = {
    read() { try { return JSON.parse(localStorage.getItem(key)); } catch (_) { return null; } },
    write(value) { try { localStorage.setItem(key, JSON.stringify(value)); } catch (_) {} },
  };
  const last = storage.read();
  if (last && Number.isInteger(last.score) && Number.isInteger(last.total) && last.total > 0 && last.score >= 0 && last.score <= last.total) {
    const el = shell.querySelector("[data-exam-last]");
    el.textContent = `Son cəhd: ${last.score} / ${last.total} düzgün · %${Math.round(last.score / last.total * 100)}`;
    el.hidden = false;
  }
  const picked = (card) => [...card.querySelectorAll("input:checked")].map((input) => Number(input.value)).sort((a, b) => a - b);
  const answers = (card) => JSON.parse(card.dataset.answer);
  const equal = (a, b) => a.length === b.length && a.every((v, i) => v === b[i]);
  const refresh = () => {
    const count = cards.filter((card) => picked(card).length).length;
    progress.textContent = `${count} / ${cards.length} cavablandı`;
    if (!warning.hidden) {
      warning.hidden = true;
      submit.textContent = "İmtahanı bitir";
    }
  };
  form.addEventListener("change", (event) => {
    if (event.target.matches("input")) {
      const card = event.target.closest(".exam-question");
      card.querySelectorAll(".choice").forEach((choice) => choice.classList.toggle("is-picked", choice.querySelector("input").checked));
      refresh();
    }
  });
  function begin() {
    run.append(form);
    form.querySelector(".exam-submit").hidden = false;
    cards.forEach((card) => {
      card.querySelectorAll("input").forEach((input) => { input.checked = false; input.disabled = false; });
      card.querySelectorAll(".choice").forEach((choice) => choice.classList.remove("is-picked", "is-right", "is-wrong", "is-missed"));
      card.classList.remove("is-checked", "is-correct", "is-incorrect");
      card.querySelector(".exam-feedback").hidden = true;
    });
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    cards.forEach((card, i) => {
      card.querySelector("[data-number]").textContent = `${i + 1}/${cards.length}`;
      form.insertBefore(card, form.querySelector(".exam-submit"));
    });
    warning.hidden = true;
    submit.textContent = "İmtahanı bitir";
    start.hidden = true;
    result.hidden = true;
    run.hidden = false;
    refresh();
    shell.querySelector("#exam-run-title").scrollIntoView();
  }
  shell.querySelector("[data-exam-begin]").addEventListener("click", begin);
  shell.querySelector("[data-exam-retry]").addEventListener("click", begin);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const unanswered = cards.filter((card) => !picked(card).length).length;
    if (unanswered && warning.hidden) {
      warning.textContent = `${unanswered} sual cavabsızdır. Bitirsən, səhv sayılacaq.`;
      warning.hidden = false;
      submit.textContent = "Yenə də bitir";
      warning.scrollIntoView({ block: "center" });
      return;
    }
    let score = 0;
    const breakdown = new Map();
    cards.forEach((card) => {
      const choice = picked(card), correct = answers(card);
      const right = equal(choice, correct);
      if (right) score++;
      const row = breakdown.get(card.dataset.lesson) || { right: 0, total: 0 };
      row.total++;
      if (right) row.right++;
      breakdown.set(card.dataset.lesson, row);
      card.classList.add("is-checked", right ? "is-correct" : "is-incorrect");
      card.querySelectorAll("input").forEach((input) => {
        input.disabled = true;
        const n = Number(input.value);
        const label = input.closest(".choice");
        label.classList.toggle("is-right", correct.includes(n));
        label.classList.toggle("is-wrong", choice.includes(n) && !correct.includes(n));
        label.classList.toggle("is-missed", correct.includes(n) && !choice.includes(n));
      });
      const text = (indexes) => indexes.map((n) => card.querySelectorAll(".choice-t")[n - 1].textContent.trim()).join("; ");
      card.querySelector(".exam-choice-summary").textContent = `Seçimin: ${choice.length ? text(choice) : "Cavab yoxdur"} · Düzgün: ${text(correct)}`;
      card.querySelector(".exam-feedback").hidden = false;
    });
    shell.querySelector("[data-exam-score]").textContent = `${score} / ${cards.length} düzgün · %${Math.round(score / cards.length * 100)}`;
    const list = shell.querySelector("[data-exam-breakdown]");
    list.replaceChildren();
    Object.entries(lessons).forEach(([slug, lesson]) => {
      const row = breakdown.get(slug);
      if (!row) return;
      const link = document.createElement("a");
      link.href = lesson.url;
      const name = document.createElement("span");
      name.textContent = lesson.title;
      const count = document.createElement("strong");
      count.textContent = `${row.right} / ${row.total}`;
      link.append(name, count);
      list.append(link);
    });
    storage.write({ score, total: cards.length });
    run.hidden = true;
    result.hidden = false;
    result.append(form);
    form.querySelector(".exam-submit").hidden = true;
    result.querySelector("#exam-result-title").focus();
    result.scrollIntoView();
  });
})();
