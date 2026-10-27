/* Prudent Dental Clinic · site behaviour (no dependencies) */
(() => {
  document.documentElement.classList.add("js");
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const PHONE = "917028722200";

  /* ---------- clinic clock, always Pune time ---------- */
  const ist = (add = 0) => { const d = new Date(new Date().toLocaleString("en-US", { timeZone: "Asia/Kolkata" })); d.setDate(d.getDate() + add); return d; };
  const closeOf = d => (d.getDay() === 0 ? 17 : 21);
  const hr = h => (h === 12 ? "12 PM" : h > 12 ? `${h - 12} PM` : `${h} AM`);
  const now = ist(), hNow = now.getHours() + now.getMinutes() / 60;
  const isOpen = hNow >= 9 && hNow < closeOf(now);
  const statusText = isOpen ? `Open now · until ${hr(closeOf(now))}` : hNow < 9 ? "Opens at 9 AM today" : "Closed · opens 9 AM tomorrow";
  $$("[data-open-status]").forEach(el => { el.textContent = statusText; el.closest("[data-open-wrap]")?.classList.toggle("is-closed", !isOpen); });
  $$(".hours tr[data-day]").forEach(tr => tr.classList.toggle("is-today", +tr.dataset.day === now.getDay()));
  $$("[data-year]").forEach(el => (el.textContent = now.getFullYear()));

  /* ---------- smooth scroll (Lenis) ---------- */
  // Wheel and trackpad get eased scrolling; touch keeps the phone's native
  // momentum. Skipped entirely under reduced motion.
  let lenis = null;
  if (window.Lenis && !reduce) {
    lenis = new Lenis({ duration: 1.1, easing: t => 1 - Math.pow(1 - t, 4), smoothWheel: true, wheelMultiplier: 1, touchMultiplier: 1.2 });
    window.__lenis = lenis;
    const raf = t => { lenis.raf(t); requestAnimationFrame(raf); };
    requestAnimationFrame(raf);
  }
  const headOffset = () => -(($(".head")?.offsetHeight || 80) + 12);
  // In-page anchors glide to their target, clearing the sticky header.
  document.addEventListener("click", e => {
    const a = e.target.closest('a[href^="#"], a[href*=".html#"]');
    if (!a || !lenis) return;
    const url = new URL(a.href, location.href);
    if (url.pathname !== location.pathname || !url.hash) return;
    const el = document.querySelector(url.hash); if (!el) return;
    e.preventDefault(); lenis.scrollTo(el, { offset: headOffset() }); history.replaceState(null, "", url.hash);
  });
  if (lenis && location.hash) { const el = document.querySelector(location.hash); if (el) setTimeout(() => lenis.scrollTo(el, { offset: headOffset(), immediate: true }), 60); }
  const lockScroll = on => { if (lenis) on ? lenis.stop() : lenis.start(); document.body.style.overflow = on ? "hidden" : ""; };

  /* ---------- parallax: a few large images drift against the scroll ---------- */
  const PX = [[".hero__art > img", .05], [".why__img img", .07], [".how__img img", .06], [".cta__img img", .05], [".phead__art", .12], [".bento__ph img", .05]];
  const pxEls = reduce ? [] : PX.flatMap(([s, k]) => $$(s).map(el => (el.classList.add("px"), { el, k })));
  if (pxEls.length) {
    const wide = matchMedia("(min-width: 761px)");
    const tick = () => {
      const vh = innerHeight;
      for (const p of pxEls) {
        if (!wide.matches) { p.el.style.removeProperty("--py"); continue; }
        const r = p.el.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) continue;
        const d = (r.top + r.height / 2 - vh / 2) * -p.k;
        p.el.style.setProperty("--py", d.toFixed(1) + "px");
      }
    };
    if (lenis) lenis.on("scroll", tick); else addEventListener("scroll", () => requestAnimationFrame(tick), { passive: true });
    addEventListener("resize", tick); tick();
  }

  /* ---------- mobile menu ---------- */
  const menu = $(".menu"), burger = $(".burger");
  const openMenu = open => {
    if (!menu) return;
    menu.classList.toggle("is-open", open);
    burger?.setAttribute("aria-expanded", String(open));
    lockScroll(open);
    if (open) setTimeout(() => $("nav a", menu)?.focus(), 60); else burger?.focus();
  };
  burger?.addEventListener("click", () => openMenu(true));
  $$("[data-menu-close]").forEach(b => b.addEventListener("click", () => openMenu(false)));
  addEventListener("keydown", e => { if (e.key === "Escape" && menu?.classList.contains("is-open")) openMenu(false); });

  /* ---------- appear on entry (once): opacity + rise + blur, staggered ---------- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -4% 0px", threshold: 0 });
  $$("[data-stagger]").forEach(g => [...g.children].forEach((c, i) => { if (!c.hasAttribute("data-a")) c.setAttribute("data-a", ""); c.style.setProperty("--d", i); }));
  $$("[data-a]").forEach(el => io.observe(el));

  /* ---------- count up real figures ---------- */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; cio.unobserve(e.target);
    const el = e.target, raw = el.dataset.count, to = parseFloat(raw), dec = (raw.split(".")[1] || "").length, suf = el.dataset.suffix || "";
    if (reduce) { el.textContent = to.toFixed(dec) + suf; return; }
    const t0 = performance.now(), dur = 1500;
    const tick = t => { const k = Math.min(1, (t - t0) / dur), v = to * (1 - Math.pow(1 - k, 3)); el.textContent = v.toFixed(dec) + suf; if (k < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }), { threshold: 0.6 });
  $$("[data-count]").forEach(el => cio.observe(el));

  /* ---------- accordion ---------- */
  $$(".qa button").forEach(b => b.addEventListener("click", () => b.setAttribute("aria-expanded", String(b.getAttribute("aria-expanded") !== "true"))));

  /* ---------- tabs ---------- */
  $$("[data-tabs]").forEach(root => {
    const btns = $$("[role=tab]", root);
    const select = b => btns.forEach(x => { const on = x === b; x.setAttribute("aria-selected", String(on)); x.tabIndex = on ? 0 : -1; const p = document.getElementById(x.getAttribute("aria-controls")); if (p) p.hidden = !on; });
    btns.forEach(b => b.addEventListener("click", () => select(b)));
    root.addEventListener("keydown", e => {
      const i = btns.indexOf(document.activeElement); if (i < 0) return;
      const k = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key]; if (!k) return;
      e.preventDefault(); const n = btns[(i + k + btns.length) % btns.length]; n.focus(); select(n);
    });
  });

  /* ---------- pinned rails: scrolling down moves a row of cards sideways ---------- */
  // Any row that overflows (services everywhere, videos on phones) holds still
  // while the page scroll drives it. A sideways swipe on the row scrolls too.
  // Falls back to a plain swipe row if it would not fit on screen.
  const css = (el, p) => parseFloat(getComputedStyle(el)[p]) || 0;
  const actbar = $(".actbar");
  const pins = new Map();
  $$("[data-pin]").forEach(sec => {
    const sticky = $(".pin__sticky", sec), rail = $("[data-pin-rail]", sec);
    if (!sticky || !rail) return;
    let on = false;
    const max = () => Math.max(0, rail.scrollWidth - rail.clientWidth);
    const start = () => sec.getBoundingClientRect().top + scrollY + css(sec, "paddingTop") - css(sticky, "top");
    const drive = () => { if (on) rail.scrollLeft = Math.min(max(), Math.max(0, scrollY - start())); };
    const layout = () => {
      sec.classList.add("is-pinned");
      const room = innerHeight - css(sticky, "top") - (actbar && getComputedStyle(actbar).display !== "none" ? actbar.offsetHeight + 16 : 0);
      on = !reduce && max() > 0 && sticky.offsetHeight <= room;
      sec.classList.toggle("is-pinned", on);
      sec.style.height = on ? `${css(sec, "paddingTop") + sticky.offsetHeight + max()}px` : "";
      drive();
    };
    let x0 = 0, y0 = 0, side = null;
    rail.addEventListener("touchstart", e => { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; side = null; }, { passive: true });
    rail.addEventListener("touchmove", e => {
      if (!on) return;
      const x = e.touches[0].clientX, y = e.touches[0].clientY;
      if (side === null) { if (Math.hypot(x - x0, y - y0) < 6) return; side = Math.abs(x - x0) > Math.abs(y - y0); }
      if (!side) return;
      if (e.cancelable) e.preventDefault();
      scrollBy({ top: x0 - x, behavior: "instant" }); x0 = x;
    }, { passive: false });
    // a sliding row fetches all its photos as it approaches, so cards never slide in blank
    new IntersectionObserver((es, ob) => { if (es[0].isIntersecting) { $$("img[loading=lazy]", sec).forEach(i => (i.loading = "eager")); ob.disconnect(); } }, { rootMargin: "100% 0px" }).observe(sec);
    pins.set(sec, { on: () => on, start, layout, drive });
  });
  if (pins.size) {
    const driveAll = () => pins.forEach(p => p.drive());
    const layoutAll = () => pins.forEach(p => p.layout());
    if (lenis) lenis.on("scroll", driveAll); else addEventListener("scroll", () => requestAnimationFrame(driveAll), { passive: true });
    addEventListener("resize", layoutAll);
    addEventListener("load", layoutAll);
    layoutAll();
  }

  /* ---------- services carousel: counter + arrows ---------- */
  $$("[data-carousel]").forEach(root => {
    const rail = $(".rail", root), cards = [...rail.children], prev = $("[data-prev]", root), next = $("[data-next]", root), cur = $("[data-cur]", root);
    const pin = pins.get(root.closest("[data-pin]"));
    const step = () => cards[0].getBoundingClientRect().width + parseFloat(getComputedStyle(rail).columnGap || 14);
    const max = () => Math.max(0, rail.scrollWidth - rail.clientWidth);
    // Counter follows progress through the whole set, so the last position reads 09 / 09.
    const update = () => {
      const m = max(), p = m ? rail.scrollLeft / m : 0;
      if (cur) cur.textContent = String(1 + Math.round(p * (cards.length - 1))).padStart(2, "0");
      prev.disabled = rail.scrollLeft < 4;
      next.disabled = rail.scrollLeft >= m - 4;
    };
    // While pinned, the arrows scroll the page by one card so the rail follows.
    const go = dir => {
      if (pin?.on()) {
        const y = pin.start() + Math.min(max(), Math.max(0, rail.scrollLeft + dir * step()));
        lenis ? lenis.scrollTo(y, { duration: 0.9 }) : scrollTo({ top: y, behavior: "smooth" });
      } else rail.scrollBy({ left: dir * step(), behavior: reduce ? "auto" : "smooth" });
    };
    prev.addEventListener("click", () => go(-1));
    next.addEventListener("click", () => go(1));
    rail.addEventListener("scroll", () => requestAnimationFrame(update), { passive: true });
    addEventListener("resize", update);
    update();
  });

  /* ---------- video stories: custom player, one plays at a time ---------- */
  const ICON = {
    play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5.6v12.8c0 .8.9 1.3 1.6.9l10.2-6.4c.6-.4.6-1.4 0-1.8L9.6 4.7C8.9 4.3 8 4.8 8 5.6z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6.5" y="5" width="4" height="14" rx="1.4" fill="currentColor"/><rect x="13.5" y="5" width="4" height="14" rx="1.4" fill="currentColor"/></svg>',
    vol: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 9.5h3.2L12 5.6v12.8l-4.8-3.9H4z"/><path d="M15.5 9a4 4 0 0 1 0 6M18 6.5a7.5 7.5 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    mute: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 9.5h3.2L12 5.6v12.8l-4.8-3.9H4z"/><path d="m16 9.5 5 5m0-5-5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    full: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V5a1 1 0 0 1 1-1h4m6 0h4a1 1 0 0 1 1 1v4m0 6v4a1 1 0 0 1-1 1h-4m-6 0H5a1 1 0 0 1-1-1v-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
  };
  const fmt = t => (isFinite(t) ? `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, "0")}` : "0:00");
  const players = [];
  $$(".vid").forEach(fig => {
    const v = $("video", fig), frame = $(".vid__frame", fig);
    if (!v) return;
    v.removeAttribute("controls");
    const name = (v.getAttribute("aria-label") || "video").replace(/^Video: /, "").replace(/[<>"&]/g, "");
    frame.insertAdjacentHTML("beforeend", `
      <button class="vid__big" type="button" aria-label="Play ${name}"><span>${ICON.play}</span></button>
      <div class="vid__bar">
        <button class="vid__btn js-pp" type="button" aria-label="Play">${ICON.play}</button>
        <span class="vid__time nums"><span class="js-cur">0:00</span> / <span class="js-dur">0:00</span></span>
        <div class="vid__track" role="slider" tabindex="0" aria-label="Seek" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><i class="vid__buf"></i><i class="vid__fill"></i><i class="vid__knob"></i></div>
        <button class="vid__btn js-mute" type="button" aria-label="Mute">${ICON.vol}</button>
        <button class="vid__btn js-full" type="button" aria-label="Full screen">${ICON.full}</button>
      </div>`);
    const big = $(".vid__big", frame), pp = $(".js-pp", frame), mute = $(".js-mute", frame), full = $(".js-full", frame);
    const track = $(".vid__track", frame), fill = $(".vid__fill", frame), knob = $(".vid__knob", frame), buf = $(".vid__buf", frame);
    const cur = $(".js-cur", frame), dur = $(".js-dur", frame);
    let idle;
    const wake = () => { fig.classList.add("is-awake"); clearTimeout(idle); if (!v.paused) idle = setTimeout(() => fig.classList.remove("is-awake"), 2200); };
    const toggle = () => (v.paused ? v.play() : v.pause());
    const paint = () => {
      const k = v.duration ? v.currentTime / v.duration : 0;
      fill.style.transform = `scaleX(${k})`; knob.style.left = `${k * 100}%`;
      track.setAttribute("aria-valuenow", Math.round(k * 100)); cur.textContent = fmt(v.currentTime);
    };
    big.addEventListener("click", () => v.play());
    pp.addEventListener("click", toggle);
    v.addEventListener("click", toggle);
    mute.addEventListener("click", () => { v.muted = !v.muted; mute.innerHTML = v.muted ? ICON.mute : ICON.vol; mute.setAttribute("aria-label", v.muted ? "Unmute" : "Mute"); });
    full.addEventListener("click", () => {
      if (document.fullscreenElement) return document.exitFullscreen();
      if (frame.requestFullscreen) frame.requestFullscreen(); else if (v.webkitEnterFullscreen) v.webkitEnterFullscreen();
    });
    v.addEventListener("loadedmetadata", () => (dur.textContent = fmt(v.duration)));
    if (v.readyState >= 1) dur.textContent = fmt(v.duration);
    v.addEventListener("timeupdate", paint);
    v.addEventListener("progress", () => { try { buf.style.transform = `scaleX(${v.buffered.end(v.buffered.length - 1) / v.duration})`; } catch (e) {} });
    v.addEventListener("play", () => {
      fig.classList.add("is-playing", "has-started"); pp.innerHTML = ICON.pause; pp.setAttribute("aria-label", "Pause");
      players.forEach(o => o !== v && !o.paused && o.pause()); wake();
    });
    v.addEventListener("pause", () => { fig.classList.remove("is-playing"); fig.classList.add("is-awake"); pp.innerHTML = ICON.play; pp.setAttribute("aria-label", "Play"); clearTimeout(idle); });
    v.addEventListener("ended", () => { fig.classList.remove("has-started"); v.currentTime = 0; });
    ["pointermove", "touchstart"].forEach(ev => frame.addEventListener(ev, wake, { passive: true }));
    // seek by dragging or tapping the track; arrow keys skip 5 s
    const seekAt = x => { const r = track.getBoundingClientRect(); const k = Math.min(1, Math.max(0, (x - r.left) / r.width)); if (v.duration) { v.currentTime = k * v.duration; paint(); } };
    track.addEventListener("pointerdown", e => { track.setPointerCapture(e.pointerId); fig.classList.add("is-seeking"); seekAt(e.clientX); });
    track.addEventListener("pointermove", e => { if (track.hasPointerCapture(e.pointerId)) seekAt(e.clientX); });
    track.addEventListener("pointerup", () => fig.classList.remove("is-seeking"));
    track.addEventListener("keydown", e => { const d = { ArrowRight: 5, ArrowLeft: -5 }[e.key]; if (d && v.duration) { e.preventDefault(); v.currentTime = Math.min(v.duration, Math.max(0, v.currentTime + d)); } });
    frame.addEventListener("contextmenu", e => e.preventDefault());
    players.push(v);
  });
  const vio = new IntersectionObserver(es => es.forEach(e => { if (!e.isIntersecting && !e.target.paused) e.target.pause(); }), { threshold: 0.35 });
  players.forEach(v => vio.observe(v));

  /* ---------- sub-nav highlight ---------- */
  const sub = $$(".subnav a");
  if (sub.length) {
    const sio = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) sub.forEach(a => a.classList.toggle("is-on", a.getAttribute("href") === "#" + e.target.id));
    }), { rootMargin: "-45% 0px -50% 0px" });
    sub.map(a => document.querySelector(a.getAttribute("href"))).filter(Boolean).forEach(s => sio.observe(s));
  }

  /* ======================================================================
     Booking in three taps: day, time, then "Book on WhatsApp".
     WhatsApp already gives the clinic the sender's number, so there is
     nothing to type. Name is optional. Nothing is stored on this site.
     ====================================================================== */
  const REASONS = ["Check-up", "Cleaning", "Tooth pain", "Root canal", "Implants", "Braces / aligners", "Whitening", "Kids"];
  const dayLabel = d => d.toLocaleDateString("en-IN", { weekday: "short", day: "numeric", month: "short" });
  const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const SLOTS = { Morning: [9, 12], Afternoon: [12, 16], Evening: [16, 21] };
  const WA = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.7-.3-1.4-.7-2-1.2-.5-.5-.9-1-1.3-1.6-.1-.2 0-.4.1-.5l.4-.5.2-.4c.1-.1 0-.3 0-.4l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.3.3-1 .9-1 2.2s1 2.6 1.1 2.7c.1.2 2 3 4.8 4.2 1.8.8 2.5.8 3.4.7.6-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>';
  const CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5 10 17l9-10" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  let uid = 0;

  function mountBooker(host, preset = {}) {
    const id = "bk" + ++uid;
    const st = { reason: preset.reason || null, day: null, date: null, time: null };
    const todayOpen = hNow < closeOf(ist(0)) - 0.5;
    host.innerHTML = `
      <form class="booker" novalidate>
        <div class="booker__head"><b>Book your visit</b><span class="steps3" aria-hidden="true"><i></i><i></i><i></i></span></div>
        <div class="booker__body">
          <fieldset class="bq"><legend>Which day? <span>tap 1</span></legend>
            <div class="bchips">
              <button type="button" class="bchip" data-d="0" aria-pressed="false" ${todayOpen ? "" : "disabled"}>Today<small>${todayOpen ? dayLabel(ist(0)) : "Closed now"}</small></button>
              <button type="button" class="bchip" data-d="1" aria-pressed="false">Tomorrow<small>${dayLabel(ist(1))}</small></button>
              <button type="button" class="bchip" data-d="pick" aria-pressed="false">Later<small class="js-pick">Pick a date</small></button>
            </div>
            <div class="bdate"><label class="sr" for="${id}-date">Choose a date</label><input type="date" id="${id}-date" min="${iso(ist(0))}"></div>
          </fieldset>
          <fieldset class="bq"><legend>What time suits you? <span>tap 2</span></legend>
            <div class="bchips">
              <button type="button" class="bchip" data-t="Morning" aria-pressed="false">Morning<small>9 to 12</small></button>
              <button type="button" class="bchip" data-t="Afternoon" aria-pressed="false">Afternoon<small class="js-aft">12 to 4</small></button>
              <button type="button" class="bchip" data-t="Evening" aria-pressed="false">Evening<small class="js-eve">4 to 9</small></button>
            </div>
          </fieldset>
          <fieldset class="bq"><legend>What's it for? <span>optional</span></legend>
            <div class="bchips--r">${REASONS.map(r => `<button type="button" class="bchip" data-r="${esc(r)}" aria-pressed="false">${esc(r)}</button>`).join("")}</div>
          </fieldset>
          <div class="bq bname"><label for="${id}-n">Your name (optional)</label><input id="${id}-n" autocomplete="name" placeholder="So we can greet you"></div>
          <p class="bsum" aria-live="polite"></p>
          <a class="btn btn--wa bsend" href="#" target="_blank" rel="noopener" aria-disabled="true">${WA} Book on WhatsApp</a>
          <div class="balt"><span>Tap 3 opens WhatsApp with everything filled in.</span><span>Prefer a call? <a href="tel:+${PHONE}">+91 70287 22200</a></span></div>
        </div>
      </form>`;
    const form = $("form", host), body = $(".booker__body", form), dots = $$(".steps3 i", form), sum = $(".bsum", form), send = $(".bsend", form), dateIn = $(".bdate input", form), nameIn = $(`#${id}-n`);
    const press = (sel, b) => $$(sel, form).forEach(x => x.setAttribute("aria-pressed", String(x === b)));
    const message = () => {
      const day = st.day === "0" ? "today" : st.day === "1" ? "tomorrow" : dayLabel(st.date);
      const sun = st.date.getDay() === 0;
      const range = { Morning: "9 to 12", Afternoon: sun ? "12 to 5" : "12 to 4", Evening: "4 to 9" }[st.time];
      const nm = nameIn.value.trim();
      return `Hello Prudent Dental Clinic, I'd like to book a visit${st.reason ? " for " + st.reason.toLowerCase() : ""}.\nDay: ${day} (${dayLabel(st.date)})\nTime: ${st.time.toLowerCase()} (${range})${nm ? "\nName: " + nm : ""}`;
    };
    const sync = () => {
      const sun = st.date && st.date.getDay() === 0, today = st.date && iso(st.date) === iso(ist(0));
      $(".js-aft", form).textContent = sun ? "12 to 5" : "12 to 4";
      $(".js-eve", form).textContent = sun ? "Closed Sundays" : "4 to 9";
      $$("[data-t]", form).forEach(b => {
        let end = SLOTS[b.dataset.t][1]; if (sun && b.dataset.t === "Afternoon") end = 17;
        const off = (sun && b.dataset.t === "Evening") || (today && hNow > end - 0.5);
        b.disabled = off; if (off && st.time === b.dataset.t) { st.time = null; b.setAttribute("aria-pressed", "false"); }
      });
      const ready = !!(st.date && st.time);
      dots[0].classList.toggle("on", !!st.date); dots[1].classList.toggle("on", !!st.time); dots[2].classList.toggle("on", ready);
      send.setAttribute("aria-disabled", String(!ready));
      send.href = ready ? `https://wa.me/${PHONE}?text=${encodeURIComponent(message())}` : "#";
      sum.innerHTML = ready ? `Requesting <b>${esc(st.day === "0" ? "today" : st.day === "1" ? "tomorrow" : dayLabel(st.date))}</b>, <b>${esc(st.time.toLowerCase())}</b>${st.reason ? ` for <b>${esc(st.reason.toLowerCase())}</b>` : ""}.` : (st.date ? "Now pick a time of day." : "Pick a day to start.");
    };
    const setDay = d => {
      st.day = d; $(".bdate", form).classList.toggle("is-open", d === "pick");
      st.date = d === "pick" ? (dateIn.value ? new Date(dateIn.value + "T10:00") : null) : ist(+d);
      if (d === "pick" && !dateIn.value) dateIn.focus();
      sync();
    };
    $$("[data-d]", form).forEach(b => b.addEventListener("click", () => { press("[data-d]", b); setDay(b.dataset.d); }));
    dateIn.addEventListener("change", () => { st.date = dateIn.value ? new Date(dateIn.value + "T10:00") : null; $(".js-pick", form).textContent = st.date ? dayLabel(st.date) : "Pick a date"; sync(); });
    $$("[data-t]", form).forEach(b => b.addEventListener("click", () => { press("[data-t]", b); st.time = b.dataset.t; sync(); }));
    $$("[data-r]", form).forEach(b => b.addEventListener("click", () => { const on = b.getAttribute("aria-pressed") !== "true"; press("[data-r]", on ? b : null); st.reason = on ? b.dataset.r : null; sync(); }));
    nameIn.addEventListener("input", sync);
    if (st.reason) $$("[data-r]", form).find(x => x.dataset.r === st.reason)?.setAttribute("aria-pressed", "true");
    let pd = preset.day; if (pd === "0" && !todayOpen) pd = "1";
    if (pd != null) { const b = $(`[data-d="${pd}"]`, form); if (b && !b.disabled) { press("[data-d]", b); setDay(String(pd)); } }
    sync();

    send.addEventListener("click", e => {
      if (send.getAttribute("aria-disabled") === "true") { e.preventDefault(); sum.innerHTML = st.date ? "<b>Pick a time of day</b> to continue." : "<b>Pick a day</b> to continue."; return; }
      // Let the link open WhatsApp, then show what happens next.
      const href = send.href;
      setTimeout(() => {
        body.innerHTML = `<div class="bdone"><div class="bdone__ic">${CHECK}</div><h3>Almost done</h3><p>WhatsApp has your request ready. Tap send there, and the clinic replies with your exact time.</p>
          <a class="btn btn--wa btn--lg" href="${href}" target="_blank" rel="noopener">${WA} Open WhatsApp again</a>
          <div class="balt" style="justify-content:center"><button type="button" class="btn btn--line btn--sm js-edit">Change details</button></div></div>`;
        $(".js-edit", form).addEventListener("click", () => mountBooker(host, { reason: st.reason }));
      }, 120);
    });
  }

  $$("[data-booker]").forEach(h => { const q = new URLSearchParams(location.search); mountBooker(h, { reason: q.get("for") || null, day: q.get("day") }); });

  let dlg = null;
  const openBook = preset => {
    if (!dlg) {
      dlg = document.createElement("dialog");
      dlg.className = "bookdlg"; dlg.setAttribute("aria-label", "Book your visit");
      dlg.innerHTML = `<button class="dlg-x" type="button" aria-label="Close"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button><div class="dlg-host"></div>`;
      document.body.appendChild(dlg);
      $(".dlg-x", dlg).addEventListener("click", () => dlg.close());
      dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });
      dlg.addEventListener("close", () => lockScroll(false));
    }
    mountBooker($(".dlg-host", dlg), preset);
    lockScroll(true);
    dlg.showModal();
    setTimeout(() => $(".bchip:not(:disabled)", dlg)?.focus({ preventScroll: true }), 30);
  };
  document.addEventListener("click", e => {
    const t = e.target.closest("[data-book]");
    if (!t || !window.HTMLDialogElement) return;
    e.preventDefault();
    if (menu?.classList.contains("is-open")) openMenu(false);
    openBook({ reason: t.dataset.reason || null, day: t.dataset.day ?? null });
  });
})();
