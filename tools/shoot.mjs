// Screenshot a page through Chrome DevTools Protocol, reporting console errors.
// Runs under Windows node.exe driving Windows Chrome (the WSL side has neither).
//
//   node shoot.mjs <url> <out.(png|webp|jpeg)> [width=1440] [height=900]
//        [--full] [--scheme=dark|light] [--scroll=px] [--wait=ms] [--quality=82]
//        [--eval=js]   run JS in the page before the capture
import { spawn } from "node:child_process";
import { writeFileSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";

const args = process.argv.slice(2);
const flags = Object.fromEntries(
  args.filter((a) => a.startsWith("--")).map((a) => {
    const [k, ...v] = a.slice(2).split("=");
    return [k, v.length ? v.join("=") : true];
  })
);
const [url, out, w = "1440", h = "900"] = args.filter((a) => !a.startsWith("--"));
if (!url || !out) {
  console.error("usage: node shoot.mjs <url> <out> [width] [height] [--full] ...");
  process.exit(2);
}

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const PORT = 9300 + Math.floor(Math.random() * 500);
// Throwaway Chrome profile; set SHOOT_PROFILE_DIR to keep it off a full system drive.
const PROFILE = `${process.env.SHOOT_PROFILE_DIR || tmpdir()}\\qrup596-chrome-${PORT}`;
mkdirSync(PROFILE, { recursive: true });

const chrome = spawn(CHROME, [
  "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars",
  `--remote-debugging-port=${PORT}`, `--user-data-dir=${PROFILE}`, "about:blank",
], { stdio: "ignore" });

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function pageSocket() {
  for (let i = 0; i < 60; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
      const page = list.find((t) => t.type === "page");
      if (page) return page.webSocketDebuggerUrl;
    } catch {}
    await sleep(250);
  }
  throw new Error("Chrome did not expose a page target");
}

let seq = 0;
const pending = new Map();
const listeners = [];
function connect(wsUrl) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(wsUrl);
    ws.onopen = () => resolve(ws);
    ws.onerror = reject;
    ws.onmessage = (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && pending.has(msg.id)) {
        const { res, rej } = pending.get(msg.id);
        pending.delete(msg.id);
        msg.error ? rej(new Error(msg.error.message)) : res(msg.result);
      } else if (msg.method) listeners.forEach((fn) => fn(msg));
    };
  });
}
const send = (ws, method, params = {}) =>
  new Promise((res, rej) => {
    const id = ++seq;
    pending.set(id, { res, rej });
    ws.send(JSON.stringify({ id, method, params }));
  });

const errors = [];
try {
  const ws = await connect(await pageSocket());
  listeners.push((m) => {
    if (m.method === "Runtime.exceptionThrown")
      errors.push("exception: " + (m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text));
    if (m.method === "Runtime.consoleAPICalled" && m.params.type === "error")
      errors.push("console.error: " + m.params.args.map((a) => a.value ?? a.description).join(" "));
    if (m.method === "Log.entryAdded" && m.params.entry.level === "error")
      errors.push("log: " + m.params.entry.text + " " + (m.params.entry.url || ""));
  });
  await send(ws, "Page.enable");
  await send(ws, "Runtime.enable");
  await send(ws, "Log.enable");
  const width = +w, height = +h;
  await send(ws, "Emulation.setDeviceMetricsOverride", {
    width, height, deviceScaleFactor: 1, mobile: width < 700,
  });
  const features = [];
  if (flags.scheme) features.push({ name: "prefers-color-scheme", value: flags.scheme });
  if (flags.reduced) features.push({ name: "prefers-reduced-motion", value: "reduce" });
  if (features.length) await send(ws, "Emulation.setEmulatedMedia", { features });

  const loaded = new Promise((r) => listeners.push((m) => m.method === "Page.loadEventFired" && r()));
  await send(ws, "Page.navigate", { url });
  await Promise.race([loaded, sleep(15000)]);
  await sleep(+(flags.wait || 1200));
  // Instant scrolling: the site sets scroll-behavior: smooth, which would otherwise
  // leave the page mid-animation when the capture happens.
  if (flags.scroll) {
    await send(ws, "Runtime.evaluate", { expression: `window.scrollTo({ top: ${+flags.scroll}, behavior: "instant" })` });
    await sleep(+(flags.wait || 1200));
  }
  if (flags.at) {
    const sel = JSON.stringify(flags.at);
    const off = +(flags.offset || 0);
    await send(ws, "Runtime.evaluate", {
      expression: `(() => { const el = document.querySelector(${sel}); if (!el) return; const y = el.getBoundingClientRect().top + scrollY + ${off}; window.scrollTo({ top: y, behavior: "instant" }); })()`,
    });
    await sleep(+(flags.wait || 1200));
  }
  if (flags.eval) {
    const r = await send(ws, "Runtime.evaluate", { expression: flags.eval, awaitPromise: true, returnByValue: true });
    if (r.result?.value !== undefined) console.log("eval:", JSON.stringify(r.result.value));
    await sleep(600);
  }
  const format = out.endsWith(".webp") ? "webp" : out.endsWith(".jpg") || out.endsWith(".jpeg") ? "jpeg" : "png";
  const params = { format, captureBeyondViewport: !!flags.full };
  if (format !== "png") params.quality = +(flags.quality || 82);
  if (flags.full) {
    const m = await send(ws, "Page.getLayoutMetrics");
    params.clip = { x: 0, y: 0, width, height: Math.ceil(m.cssContentSize.height), scale: 1 };
  }
  const shot = await send(ws, "Page.captureScreenshot", params);
  writeFileSync(out, Buffer.from(shot.data, "base64"));
  console.log(`saved ${out}`);
  if (errors.length) console.log("PAGE ERRORS:\n" + errors.join("\n"));
  else console.log("no page errors");
  ws.close();
} catch (e) {
  console.error("shoot failed:", e.message);
  process.exitCode = 1;
} finally {
  chrome.kill();
  await sleep(500);
  try { (await import("node:fs")).rmSync(PROFILE, { recursive: true, force: true }); } catch {}
}
