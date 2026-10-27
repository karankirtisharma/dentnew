"""Builds the Prudent Dental Clinic site (v2 layout). Content lives in content_data.py.
Run:  python build.py"""
import html, pathlib
from content_data import AREAS, QUOTES, FAQS, SPECIALISTS, MAP_IFRAME, initials, SERVICES9, VIDEOS

ROOT = pathlib.Path(__file__).parent
E = html.escape
PHONE, PHONE_D = "+917028722200", "+91 70287 22200"
WA = "https://wa.me/917028722200?text=Hello%20Prudent%20Dental%20Clinic%2C%20I%27d%20like%20to%20book%20a%20visit."
MAPS = "https://share.google/ShzOUFCvSZfTAajnL"

def ic(d, fill=False, cls="ico"):
    a = 'fill="currentColor"' if fill else 'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><path {a} d="{d}"/></svg>'
ARR = ic("M5 12h14m-5-5 5 5-5 5", cls="ico arr")
LEFT = ic("M19 12H5m5 5-5-5 5-5")
RIGHT = ic("M5 12h14m-5-5 5 5-5 5")
PHONE_I = ic("M5 4h3l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z")
WA_I = ic("M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1-.7-.3-1.4-.7-2-1.2-.5-.5-.9-1-1.3-1.6-.1-.2 0-.4.1-.5l.4-.5.2-.4c.1-.1 0-.3 0-.4l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.3.3-1 .9-1 2.2s1 2.6 1.1 2.7c.1.2 2 3 4.8 4.2 1.8.8 2.5.8 3.4.7.6-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z", fill=True)
CAL = ic("M7 3v3m10-3v3M4 9h16M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z")
PIN = ic("M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21zm0-9a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z")
CAR = ic("M5 16h14M6 16l1.5-5h9L18 16M7 16v2m10-2v2")
MAIL = ic("M4 6h16v12H4zM4 7l8 6 8-6")
TICK = ic("M5 12.5 10 17l9-10")
SHIELD = ic("M12 3 5 6v6c0 4.4 3 7.8 7 9 4-1.2 7-4.6 7-9V6l-7-3zm-3 9 2 2 4-4")
TOOTH = ic("M8 3c-2.8 0-4.5 2.4-4 5.5.4 2.4 1.5 3.6 2 6 .5 2.6.8 6.5 2.4 6.5 1.8 0 1.4-5 3.6-5s1.8 5 3.6 5c1.6 0 1.9-3.9 2.4-6.5.5-2.4 1.6-3.6 2-6C20.5 5.4 18.8 3 16 3c-1.6 0-2.6 1-4 1S9.6 3 8 3z")
SUN = ic("M12 4V2m0 20v-2m8-8h2M2 12h2m13.7-5.7 1.4-1.4M4.9 19.1l1.4-1.4m0-11.4L4.9 4.9m14.2 14.2-1.4-1.4M12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8z")
CAM = ic("M4 8h3l2-2h6l2 2h3v11H4zm8 9a4 4 0 1 0 0-8 4 4 0 0 0 0 8z")
RUPEE = ic("M7 5h10M7 9h10M7 5c5 0 6 2 6 4s-1 4-6 4l7 6")
USERS = ic("M16 19v-1a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v1m6.5-9a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM21 19v-1a4 4 0 0 0-3-3.9M16 3.1a3.5 3.5 0 0 1 0 6.8")
DOOR = ic("M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17M4 21h16M14 12h.01")
SMILE = ic("M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zm-4-7a5 5 0 0 0 8 0M9 9.5h.01M15 9.5h.01")
STAR = ic("m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z", fill=True)
MENU = ic("M4 8h16M4 16h16")
X = ic("M6 6l12 12M18 6 6 18")

NAV = [("index.html", "Home"), ("services.html", "Services"), ("dentists.html", "Dentists"), ("about.html", "About"), ("stories.html", "Reviews"), ("faq.html", "FAQ"), ("contact.html", "Contact")]
HOURS = "".join(f'<tr data-day="{d}"><td>{n}</td><td>{h}</td></tr>' for d, n, h in [(1, "Monday", "9 AM – 9 PM"), (2, "Tuesday", "9 AM – 9 PM"), (3, "Wednesday", "9 AM – 9 PM"), (4, "Thursday", "9 AM – 9 PM"), (5, "Friday", "9 AM – 9 PM"), (6, "Saturday", "9 AM – 9 PM"), (0, "Sunday", "9 AM – 5 PM")])

def page(file, title, desc, body, active=None):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV)
    mnav = "".join(f'<a href="{h}"{cur if h == active else ""}>{t}</a>' for h, t in NAV)
    doc = f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#F3F8F6">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='16' fill='%231D6A56'/><path d='M10 8.5c2-1.6 4.2-.4 6 .4 1.8-.8 4-2 6-.4 2.2 1.8 1.4 6-.4 9.4-.9 1.8-1.2 6-2.6 6-1.6 0-1.3-4.8-3-4.8s-1.4 4.8-3 4.8c-1.4 0-1.7-4.2-2.6-6C8.6 14.5 7.8 10.3 10 8.5z' fill='%23F3F8F6'/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@200..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
<header class="head"><div class="wrap"><div class="head__bar">
  <a class="head__logo" href="index.html" aria-label="Prudent Dental Clinic, home"><img src="assets/img/logo.webp" width="900" height="335" alt="Prudent Dental"></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
  <div class="head__end"><span class="status" data-open-wrap><span class="dot" aria-hidden="true"></span><span data-open-status>Open 7 days</span></span>
    <a class="btn btn--dark btn--sm" href="book.html" data-book>Book a visit</a></div>
  <button class="burger" type="button" aria-label="Open menu" aria-expanded="false">{MENU}</button>
</div></div></header>
<div class="menu"><div class="menu__scrim" data-menu-close></div>
  <div class="menu__panel" role="dialog" aria-label="Menu">
    <div class="menu__top"><img src="assets/img/logo.webp" width="900" height="335" alt="Prudent Dental"><button class="dlg-x" style="position:static" type="button" aria-label="Close menu" data-menu-close>{X}</button></div>
    <nav aria-label="Mobile">{mnav}</nav>
    <p class="status" data-open-wrap><span class="dot" aria-hidden="true"></span><span data-open-status>Open 7 days</span></p>
    <div class="menu__actions"><a class="btn btn--dark btn--lg" href="book.html" data-book>Book a visit</a><a class="btn btn--line" href="tel:{PHONE}">{PHONE_I} {PHONE_D}</a></div>
  </div></div>
<main id="main">
{body}
</main>
<footer class="foot"><div class="foot__in">
  <div class="foot__top"><p class="foot__big">A calmer visit to the dentist starts here.</p><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn--white btn--lg" href="book.html" data-book>Book a visit {ARR}</a><a class="btn btn--wa btn--lg" href="{WA}" target="_blank" rel="noopener">{WA_I} WhatsApp</a></div></div>
  <div class="foot__grid">
    <div><span class="foot__logo"><img src="assets/img/logo-light.webp" width="900" height="335" alt="Prudent Dental"></span><p style="margin-top:16px;max-width:30ch">Gentle, patient-first dentistry in Viman Nagar, Pune, led by Dr. Puja Bansal since 2005.</p></div>
    <div><h4>Visit</h4><ul><li>Office 503, 5th Floor, DNK Square, New Airport Road, Viman Nagar, Pune 411014</li><li><a href="{MAPS}" target="_blank" rel="noopener">Get directions</a></li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:{PHONE}">{PHONE_D}</a></li><li><a href="tel:+919850847079">+91 98508 47079</a></li><li><a href="mailto:prudenthealthclinic@gmail.com">prudenthealthclinic@gmail.com</a></li><li>Mon–Sat 9 AM–9 PM · Sun 9 AM–5 PM</li></ul></div>
    <div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="dentists.html">Dentists</a></li><li><a href="about.html">About &amp; safety</a></li><li><a href="stories.html">Reviews</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div>
  </div>
  <div class="foot__base"><span>© 2005–<span data-year>2026</span> Prudent Dental Clinic · Dr. Puja Bansal, BDS, MSDC Reg. No. A8860</span><span><a href="{MAPS}" target="_blank" rel="noopener">Google reviews</a> · <a href="https://www.instagram.com/clinicprudent/" target="_blank" rel="noopener">Instagram</a></span></div>
</div></footer>
<nav class="actbar" aria-label="Quick actions"><a href="tel:{PHONE}">{PHONE_I}Call</a><a class="a-wa" href="{WA}" target="_blank" rel="noopener">{WA_I}WhatsApp</a><a class="a-book" href="book.html" data-book>{CAL}Book a visit</a></nav>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="assets/site.js" defer></script>
</body>
</html>"""
    (ROOT / file).write_text(doc, encoding="utf-8")
    print("wrote", file)

def shead(tag, title, note):
    return f'<div class="shead"><div><span class="tag" data-a>{tag}</span><h2 class="h" data-a style="--d:1">{title}</h2></div><p data-a style="--d:2">{note}</p></div>'

def phead(crumb, title, lead, art=None):
    pic = f'<img class="phead__art" src="assets/img/art/{art}.webp" alt="" aria-hidden="true" data-a="scale" style="--d:2">' if art else ""
    return f'<section class="phead"><div class="wrap"><div class="phead__panel{" has-art" if art else ""}">{pic}<div class="crumbs" data-a><a href="index.html">Home</a><span>/</span><span>{crumb}</span></div><h1 class="h" data-a style="--d:1">{title}</h1><p data-a style="--d:2">{lead}</p></div></div></section>'

def cta(title="Ready for a calmer dental visit?", text="Three taps on WhatsApp. Same-week appointments are usually available, evenings and Sundays included."):
    return f"""<section class="section"><div class="wrap"><div class="cta" data-a="scale">
  <div class="cta__txt"><h2 class="h">{title}</h2><p>{text}</p><div class="cta__btns"><a class="btn btn--dark btn--lg" href="book.html" data-book>Book a visit {ARR}</a><a class="btn btn--glass btn--lg" href="tel:{PHONE}">{PHONE_I} Call us</a></div></div>
  <div class="cta__img"><img src="assets/img/dr-bansal.webp" width="800" height="1139" alt="Dr. Puja Bansal" loading="lazy"></div>
</div></div></section>"""

def qa(q, a, open_=False):
    return f'<div class="qa"><button type="button" aria-expanded="{"true" if open_ else "false"}">{E(q)}<i aria-hidden="true"></i></button><div class="qa__a"><div><p>{E(a)}</p></div></div></div>'

def visit():
    return f"""<div class="visit">
  <div class="vcard" data-a><p class="status" data-open-wrap style="color:var(--ink)"><span class="dot"></span><span data-open-status>Open 7 days</span></p>
    <table class="hours">{HOURS}</table>
    <div class="addr"><div>{PIN}<span>Office 503, 5th Floor, DNK Square, New Airport Road, Sakore Nagar, Viman Nagar, Pune 411014</span></div><div>{CAR}<span>Parking near the building. Take the lift to the 5th floor.</span></div></div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:20px"><a class="btn btn--dark" href="{MAPS}" target="_blank" rel="noopener">{PIN} Directions</a><a class="btn btn--line" href="tel:{PHONE}">{PHONE_I} Call</a></div></div>
  <div class="map" data-a style="--d:1">{MAP_IFRAME}</div>
</div>"""

# ---------------------------------------------------------------- HOME --
scards = "".join(f"""<a class="scard" href="services.html#{a[3]}"><span class="scard__img"><img src="assets/img/{a[0]}.webp" alt="{E(a[1])} at Prudent Dental Clinic" loading="lazy"></span><span class="scard__panel"><h3>{E(a[1])}</h3><p>{E(a[2])}</p><span class="scard__go" aria-hidden="true">{ARR}</span></span></a>""" for a in SERVICES9)
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5.5v13a1 1 0 0 0 1.5.86l10.6-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg>'
videos = "".join(f"""<figure class="vid" data-a style="--d:{i}"><div class="vid__frame"><video src="assets/video/{v[0]}.mp4" poster="assets/video/{v[0]}.jpg" preload="metadata" playsinline controlslist="nodownload noplaybackrate noremoteplayback" disablepictureinpicture disableremoteplayback oncontextmenu="return false" aria-label="Video: {E(v[1])}"></video></div><figcaption><b>{E(v[1])}</b><span>{E(v[2])}</span></figcaption></figure>""" for i, v in enumerate(VIDEOS))
team_cards = f"""<div class="tcard"><p class="tcard__n">01</p><div class="tcard__ph"><img src="assets/img/dr-bansal-ai.webp" alt="Dr. Puja Bansal" loading="lazy"></div><h3>Dr. Puja Bansal</h3><p>Lead Dentist &amp; Founder, BDS</p><small>· 27 years experience ·</small></div>""" + "".join(
    f"""<div class="tcard"><p class="tcard__n">0{i+2}</p><div class="tcard__ph"><img src="assets/img/{s[0]}.webp" alt="{E(s[1])}" loading="lazy"></div><h3>{E(s[1])}</h3><p>{E(s[3])}</p><small>· {E(s[4].split(',')[0])} ·</small></div>""" for i, s in enumerate(SPECIALISTS))

TABS = [
    ("room", "The treatment room", "A calm room with natural light", "Unhurried appointments in a clean, bright space. Dr. Bansal examines every patient herself and explains what she finds in plain language.",
     ["Every visit starts with a thorough examination", "X-rays only when they are needed", "We aim to see every patient on schedule"], DOOR),
    ("chair", "Sterilisation", "Clean for every single patient", "Infection control shapes how we work, with a documented routine reviewed by Dr. Bansal.",
     ["Autoclaved instruments, sealed and stored in a UV chamber", "Single-use needles, tips, cups and napkins, never reused", "Chair and surfaces disinfected between patients"], SHIELD),
    ("tech", "Technology", "See what the dentist sees", "Everyday clinical technology that makes diagnosis clearer and treatment more precise and comfortable.",
     ["Digital X-rays, generally a lower dose than film", "Intra-oral camera, so you decide together", "Magnification and an apex locator for root canals"], CAM),
]
tab_btns = "".join(f'<button role="tab" id="tb{i}" aria-controls="tp{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{t[5]}{t[1]}</button>' for i, t in enumerate(TABS))
tab_panels = "".join(f"""<div class="icard" id="tp{i}" role="tabpanel" aria-labelledby="tb{i}"{"" if i == 0 else " hidden"}><img src="assets/img/{t[0]}.webp" alt="" loading="lazy"><div class="icard__txt"><h3>{t[2]}</h3><p>{t[3]}</p><ul>{"".join(f"<li>{TICK}<span>{E(x)}</span></li>" for x in t[4])}</ul><a class="btn btn--dark" href="about.html#safety">Learn more {ARR}</a></div></div>""" for i, t in enumerate(TABS))

def q_card(q, n, o, tags=()):
    tg = f'<div class="qcard__tags">{"".join(f"<span>{E(t)}</span>" for t in tags)}</div>' if tags else ""
    return f'<figure class="qcard" style="margin:0">{tg}<q>{E(q)}</q><footer><span><b>{E(n)}</b>{E(o)}</span><span class="stars" aria-label="Five stars">★★★★★</span></footer></figure>'
bento = f"""<div class="bento" data-stagger>
  <div class="bento__ph"><img src="assets/img/c16.webp" alt="Dr. Bansal with a patient" loading="lazy"></div>
  {q_card(*QUOTES[0], tags=("First visits",))}
  {q_card(*QUOTES[1], tags=("Root canal", "Crowns"))}
  <div class="bento__ph"><img src="assets/img/team-care.webp" alt="Treatment in progress" loading="lazy"></div>
  <div class="bento__ph"><img src="assets/img/c03.webp" alt="Dr. Bansal at the chair" loading="lazy"></div>
  {q_card(*QUOTES[2])}
</div>"""

home = f"""
<section class="hero"><div class="wrap"><div class="hero__panel" data-a="scale">
  <div class="hero__copy">
    <span class="tag tag--white" data-a style="--d:1"><span class="dot"></span>Viman Nagar, Pune · since 2005</span>
    <h1 class="h" data-a style="--d:2;margin-top:18px">Gentle dentistry for the whole family, <b>open every day.</b></h1>
    <p class="hero__sub" data-a style="--d:3">From routine check-ups to implants and aligners, Dr. Puja Bansal and her specialist team care for you in a calm, welcoming clinic.</p>
    <div class="hero__ctas" data-a style="--d:4"><a class="btn btn--white btn--lg" href="book.html" data-book>Book a visit {ARR}</a><a class="btn btn--glass btn--lg" href="services.html">Explore services</a></div>
    <div class="hero__meta" data-a style="--d:5"><span>{SUN}Open 7 days</span><span>{USERS}MDS specialists</span><span>{RUPEE}Written estimate first</span></div>
  </div>
  <div class="hero__art"><img src="assets/img/dr-bansal.webp" width="800" height="1139" alt="Dr. Puja Bansal, lead dentist" fetchpriority="high">
    <div class="rating" data-a style="--d:5"><img src="assets/img/team-care.webp" alt=""><span><b>4.5 {STAR}</b><small>from 88 patient reviews<br>27 years of care</small></span></div></div>
</div></div></section>

<section class="section"><div class="wrap">
  {shead("About", "Patient-first dentistry, <b>since 2005</b>", "Trusted by Pune families, professionals and visitors from abroad, all returning for the same honest, gentle care.")}
  <div class="arc">
    <svg class="arc__svg" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true"><path d="M40 20 C 120 290, 880 290, 960 20"/></svg>
    <figure data-a style="--d:0"><img src="assets/img/c03.webp" alt="Dr. Bansal treating a patient" loading="lazy"><div class="arc__stat"><b><span data-count="27">27</span>+ years</b><span>of hands-on experience</span></div></figure>
    <figure data-a style="--d:1"><img src="assets/img/room.webp" alt="The treatment room at Prudent Dental Clinic" loading="lazy"></figure>
    <figure data-a style="--d:2"><img src="assets/img/c18.webp" alt="Treatment with full protection" loading="lazy"><div class="arc__stat"><b><span data-count="88">88</span> reviews</b><span>averaging 4.5 stars</span></div></figure>
  </div>
</div></section>

<section class="section pin" data-pin><div class="pin__sticky"><div class="wrap">
  {shead("Services", "Everything your smile needs, <b>under one roof</b>", "Whatever brings you in, we keep it simple, comfortable and clear, with a written estimate before anything starts.")}
  <div class="svc" data-carousel>
    <div class="svc__ctl"><p class="svc__count nums"><span data-cur>01</span> <small>/ 09</small></p><div class="svc__btns"><button class="circ" type="button" data-prev aria-label="Previous service">{LEFT}</button><button class="circ" type="button" data-next aria-label="Next service">{RIGHT}</button></div></div>
    <div class="rail" data-a data-pin-rail>{scards}</div>
  </div>
</div></div></section>

<section class="section"><div class="wrap">
  {shead("Why choose us", "Care that feels different <b>from the moment you walk in</b>", "No rushed appointments, no jargon, no pressure. Just honest care from a team that genuinely wants to see you smile.")}
  <div class="why">
    <div class="why__img" data-a><img src="assets/img/hero.webp" alt="Dr. Bansal with a patient in the treatment room" loading="lazy"></div>
    <div class="why__list" data-stagger>
      <div class="why__i"><em>01</em><div><h3>Gentle, unhurried treatment</h3><p>Nervous? Tell us when you book, and we'll pace the appointment around you.</p></div></div>
      <div class="why__i"><em>02</em><div><h3>A written estimate first</h3><p>You see the full plan and cost before anything begins. Never committed to work you haven't agreed to.</p></div></div>
      <div class="why__i"><em>03</em><div><h3>Open seven days a week</h3><p>9 AM to 9 PM, and 9 to 5 on Sundays. Evening and weekend visits without taking time off.</p></div></div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {shead("Our team", "Meet the people <b>behind your smile</b>", "Dr. Bansal leads every plan. MDS specialists join her here, in the same clinic, when your case needs them.")}
  <div class="team" data-stagger>{team_cards}</div>
</div></section>

<section class="section"><div class="wrap">
  {shead("Inside the clinic", "Real rooms, <b>real routines</b>", "Every photo here was taken at our Viman Nagar clinic. We don't publish before-and-after photos; ask at your consultation to see cases like yours.")}
  <div class="inside" data-tabs><div class="inside__tabs" role="tablist" aria-label="Inside the clinic" data-a>{tab_btns}</div><div data-a style="--d:1">{tab_panels}</div></div>
</div></section>

<section class="section"><div class="gpanel" data-a="scale">
  {shead('<span class="stars">★★★★★</span> Reviews', "Loved by patients <b>across Pune</b>", "From families in Viman Nagar to visitors from Europe, here is what genuine, unhurried care feels like.")}
  {bento}
  <div style="display:flex;justify-content:center;margin-top:26px"><a class="btn btn--white" href="stories.html">Read all reviews {ARR}</a></div>
</div></section>

<section class="section pin" data-pin><div class="pin__sticky"><div class="wrap">
  {shead("Video stories", "Real patients, <b>in their own words</b>", "Filmed at our Viman Nagar clinic with Dr. Bansal. Tap to play with sound.")}
  <div class="vids" data-pin-rail>{videos}</div>
</div></div></section>

<section class="section"><div class="wrap">
  {shead("How it works", "Booking takes <b>three taps</b>", "No forms, no accounts. Pick a time that suits you and confirm on WhatsApp.")}
  <div class="how">
    <div class="how__img" data-a><img src="assets/img/c14.webp" alt="Dr. Bansal at work" loading="lazy"></div>
    <div class="how__steps" data-stagger>
      <div class="hstep"><i>{CAL}</i><div><h3>Pick a day and time</h3><p>Today, tomorrow or later, morning, afternoon or evening.</p></div></div>
      <div class="hstep"><i>{WA_I}</i><div><h3>Send it on WhatsApp</h3><p>Your request is written for you. The clinic replies with your exact slot.</p></div></div>
      <div class="hstep"><i>{SMILE}</i><div><h3>Visit us, calmly</h3><p>A conversation and an examination first, with a written estimate before any treatment.</p></div></div>
    </div>
  </div>
  <div class="how__cta" data-a><a class="btn btn--dark btn--lg" href="book.html" data-book>Book a visit {ARR}</a></div>
</div></section>

<section class="section"><div class="wrap">
  {shead("Costs", "Clear costs that <b>fit your budget</b>", "No fixed online prices, because every mouth is different. You always get a written, itemised estimate first.")}
  <div class="costs" data-stagger>
    <div class="cost"><div class="cost__txt"><small>New patient</small><h3>Examination &amp; written plan</h3><p>A thorough check-up, X-rays only if needed, and a clear plan with costs before anything starts.</p><a class="btn btn--dark btn--sm" href="book.html?for=Check-up" data-book data-reason="Check-up">Book a check-up</a></div><div class="cost__img"><img src="assets/img/c15.webp" alt="" loading="lazy"></div></div>
    <div class="cost cost--g"><div class="cost__txt"><small>Larger treatments</small><h3>EMI, including no-cost plans</h3><p>Implants, braces and smile makeovers can be paid monthly. Payment options sit on top of your estimate, never instead of it.</p><a class="btn btn--dark btn--sm" href="faq.html#costs">How costs work</a></div><div class="cost__img"><img src="assets/img/c19.webp" alt="" loading="lazy"></div></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {shead("FAQs", "Questions? <b>We've got answers</b>", "Everything you wanted to ask before your first visit, answered simply and honestly.")}
  <div class="faq">
    <div class="collage" data-a><img src="assets/img/c12.webp" alt="" loading="lazy"><img src="assets/img/svc-gum.webp" alt="" loading="lazy"><img src="assets/img/c08.webp" alt="" loading="lazy"><img src="assets/img/c17.webp" alt="" loading="lazy"></div>
    <div data-a style="--d:1">{qa(*FAQS["visiting"][1][0], True)}{qa(*FAQS["visiting"][1][1])}{qa(*FAQS["costs"][1][0])}{qa(*FAQS["costs"][1][1])}{qa(*FAQS["treatments"][1][1])}{qa(*FAQS["visiting"][1][3])}{qa(*FAQS["emergency"][1][0])}</div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  {shead("Visit", "Find us in <b>Viman Nagar</b>", "On New Airport Road, with parking near the building.")}
  {visit()}
</div></section>
{cta()}
"""
page("index.html", "Prudent Dental Clinic · Gentle dentistry in Viman Nagar, Pune, open every day",
     "Dr. Puja Bansal and MDS specialists in Viman Nagar, Pune. Open 7 days. Book in three taps on WhatsApp.", home)

# ------------------------------------------------------------ SERVICES --
subn = "".join(f'<a href="#{a["id"]}">{E(a["short"])}</a>' for a in AREAS)
areas = "".join(f"""<article class="area" id="{a['id']}" data-a><img src="assets/img/{a['img']}.webp" alt="" loading="lazy"><div class="area__txt"><span class="area__n">0{i+1} / 06</span><h2 class="h">{E(a['name'])}</h2><p>{E(a['desc'])}</p><div class="chipsl">{"".join(f"<span>{E(t)}</span>" for t in a['list'])}</div><div class="area__ctas"><a class="btn btn--dark" href="book.html?for={E(a['reason'])}" data-book data-reason="{E(a['reason'])}">Book for {E(a['short'].lower())} {ARR}</a><a class="btn btn--line" href="{WA}" target="_blank" rel="noopener">{WA_I} Ask a question</a></div></div></article>""" for i, a in enumerate(AREAS))
services = phead("Services", "Everything your smile needs, <b>under one roof</b>", "Six areas of care. Every plan starts with an examination, and every treatment comes with a written estimate first.", "services") + \
    f'<nav class="subnav" aria-label="Areas of care"><div class="wrap"><div>{subn}</div></div></nav><section class="section" style="padding-top:20px"><div class="wrap">{areas}</div></section>' + \
    f"""<section class="section"><div class="wrap">{shead("Costs", "How costs <b>work</b>", "Straight answers, the same ones we give across the table.")}
<div class="cards" data-stagger><div class="card"><div class="ci">{TOOTH}</div><h3>Examination first</h3><p>Cost depends on your diagnosis and materials, so there is no fixed online price.</p></div><div class="card"><div class="ci">{RUPEE}</div><h3>Written, itemised estimate</h3><p>The full plan and cost before anything starts. Never committed to work you haven't agreed to.</p></div><div class="card"><div class="ci">{CAL}</div><h3>EMI on larger plans</h3><p>Implants, smile makeovers and braces can be paid monthly, including no-cost EMI on eligible plans.</p></div></div></div></section>""" + cta("Not sure which treatment you need?", "Book a check-up. Dr. Bansal will examine, explain and give you a written plan, with no obligation to start.")
page("services.html", "Dental services · Prudent Dental Clinic, Viman Nagar, Pune", "General, preventive, restorative, cosmetic, orthodontic and children's dentistry in Viman Nagar, Pune.", services, "services.html")

# ------------------------------------------------------------ DENTISTS --
spec = "".join(f"""<div class="card" style="display:grid;grid-template-columns:110px 1fr;gap:20px;align-items:start"><div class="tcard__ph" style="width:110px;margin:0"><img src="assets/img/{s[0]}.webp" alt="{E(s[1])}" loading="lazy"></div><div><h3>{E(s[1])}</h3><p style="margin-top:4px">{E(s[2])}</p><div class="chipsl" style="margin-top:12px"><span>{E(s[3])}</span><span>{E(s[4])}</span></div><p>{E(s[5])}</p></div></div>""" for s in SPECIALISTS)
dentists = phead("Dentists", "Meet the people <b>behind your smile</b>", "Led by Dr. Puja Bansal, with MDS specialist consultants for advanced care, all in the same clinic.", "dentists") + f"""
<section class="section"><div class="wrap split" style="align-items:center">
  <div class="why__img" data-a style="border-radius:var(--r)"><img src="assets/img/dr-bansal.webp" alt="Dr. Puja Bansal" style="aspect-ratio:4/4.6;-webkit-mask-image:none;mask-image:none;object-position:50% 15%"></div>
  <div><span class="tag" data-a>Lead dentist &amp; founder</span><h2 class="h" data-a style="font-size:var(--t-2xl);margin-top:14px">Dr. Puja Bansal, <b>BDS</b></h2>
    <p class="lead" data-a style="margin-top:16px">Dr. Bansal personally examines every patient and leads every treatment plan, with a special interest in cosmetic and aesthetic dentistry and dental implants. She holds a certificate in oral implantology and is registered with the Maharashtra State Dental Council (A8860).</p>
    <div class="chipsl" data-a><span>27 years experience</span><span>General dentist</span><span>Cosmetic &amp; aesthetic</span><span>Implantologist</span></div>
    <p class="bigq" data-a style="margin-top:28px">“Dr. Puja is the best dentist, I'm not scared when I need to visit her!”</p><p class="muted" data-a style="margin-top:8px;font-size:14px">Jana Kucekova, patient</p>
    <div data-a style="margin-top:24px"><a class="btn btn--dark btn--lg" href="book.html" data-book>Book with Dr. Bansal {ARR}</a></div></div>
</div></section>
<section class="section"><div class="wrap">{shead("Specialists", "MDS specialists, <b>in the same clinic</b>", "For advanced root canals, children's dentistry, gum treatment and implants, the right specialist joins your treatment here.")}
  <div class="cards" style="grid-template-columns:1fr" data-stagger>{spec}</div></div></section>
<section class="section"><div class="wrap split"><h2 class="h" data-a style="font-size:var(--t-2xl)">You are <b>never handed off.</b></h2><div><p class="lead" data-a>Your care starts and ends with the same person. Dr. Bansal examines you, plans your treatment and follows your case through.</p><p class="muted" data-a style="margin-top:14px">Some situations, such as complex maxillofacial surgery, belong in a hospital. When that is the case we say so plainly, guide you to the right place, and continue your general dental care here.</p></div></div></section>""" + cta()
page("dentists.html", "Our dentists · Prudent Dental Clinic, Viman Nagar", "Dr. Puja Bansal (BDS, 27 years) with MDS specialists in endodontics, pediatric dentistry, periodontics and implants.", dentists, "dentists.html")

# --------------------------------------------------------------- ABOUT --
gal = "".join(f'<img src="assets/img/{n}.webp" alt="{E(a)}" loading="lazy" data-a>' for n, a in [("room", "Treatment room"), ("c03", "Dr. Bansal treating a patient"), ("c14", "Treatment in progress"), ("team-care", "Dr. Bansal at the chair"), ("c15", "Examination"), ("chair", "Precise treatment"), ("c19", "Dentist at work"), ("c17", "Treatment room"), ("hero", "Dr. Bansal with a patient")])
about = phead("About", "Patient-first dentistry, <b>since 2005</b>", "The dental practice of the Prudent International Health Clinic group: one dedicated dental home in Viman Nagar, caring for patients from across Pune.", "about") + f"""
<section class="section"><div class="wrap split"><div><span class="tag" data-a>Our story</span><h2 class="h" data-a style="font-size:var(--t-2xl);margin-top:14px">Prevention and plain-language explanations <b>are the base of everything.</b></h2></div>
  <div><p class="lead" data-a>Every visit starts with a thorough examination. We check the health of your teeth and gums, take X-rays only when needed, and focus on cleanings, sealants and fluoride that prevent disease.</p><p class="muted" data-a style="margin-top:14px">We care about the comfort of your treatment as much as the look of your smile. Dr. Bansal and the team are friendly and gentle, and that personal approach is what makes the practice feel like family.</p></div></div></section>
<section class="section"><div class="gpanel" data-a="scale" style="text-align:center"><span class="tag tag--white">Our mission</span><p class="bigq" style="max-width:34ch;margin:22px auto 0">“To provide the best and most exceptional dental health care to our patients with genuine personal attention and care, while observing every necessary medical and sterilisation precaution.”</p></div></section>
<section class="section" id="safety"><div class="wrap">{shead("Sterilisation &amp; safety", "Infection control <b>shapes how we work</b>", "One staff member handles general cleaning, kept separate from anyone working with clinical instruments. Standards are reviewed by Dr. Bansal.")}
  <div class="cards" data-stagger>
    <div class="card"><div class="ci">{SHIELD}</div><h3>Fresh protection, every patient</h3><p>Gloves, mask, eye protection and a head cap for each appointment.</p></div>
    <div class="card"><div class="ci">{TICK}</div><h3>Autoclaved instruments</h3><p>Cleaned, sealed in pouches, sterilised and stored in a UV chamber until use.</p></div>
    <div class="card"><div class="ci">{SUN}</div><h3>Deep-cleaned twice daily</h3><p>Chair and surfaces disinfected and barrier-covered between patients; single-use items never reused.</p></div>
  </div></div></section>
<section class="section"><div class="wrap">{shead("Technology", "See what <b>the dentist sees</b>", "Everyday clinical technology for clearer diagnosis and more comfortable treatment.")}
  <div class="cards" data-stagger>
    <div class="card"><div class="ci">{CAM}</div><h3>Intra-oral camera</h3><p>See your teeth on screen and decide on treatment together.</p></div>
    <div class="card"><div class="ci">{TOOTH}</div><h3>Digital X-rays</h3><p>Generally a lower radiation dose than older film, with lead aprons every time.</p></div>
    <div class="card"><div class="ci">{TICK}</div><h3>Magnification &amp; apex locator</h3><p>Precise fillings and root canal treatment.</p></div>
  </div></div></section>
<section class="section"><div class="wrap">{shead("Gallery", "Inside <b>our clinic</b>", "Every photo here was taken at Prudent Dental Clinic, DNK Square.")}<div class="masonry">{gal}</div></div></section>""" + cta()
page("about.html", "About Prudent Dental Clinic · Viman Nagar, Pune · since 2005", "Patient-first dentistry since 2005, with a documented sterilisation routine and modern technology.", about, "about.html")

# ------------------------------------------------------------- REVIEWS --
stories = phead("Reviews", "Loved by patients <b>across Pune</b>", "Real experiences shared by patients of Dr. Puja Bansal. Rated 4.5 from 88 reviews.", "reviews") + \
    f'<section class="section pin" data-pin><div class="pin__sticky"><div class="wrap"><div class="vids" data-pin-rail>{videos}</div></div></div></section>' +     f'<section class="section"><div class="wrap"><div class="masonry" data-stagger>{"".join(q_card(*q) for q in QUOTES)}</div><div style="display:flex;justify-content:center;margin-top:24px"><a class="btn btn--line" href="{MAPS}" target="_blank" rel="noopener">See our Google reviews {ARR}</a></div></div></section>' + cta("Join them.", "Book a calm first visit. Tell us if you're nervous, and we'll pace everything around you.")
page("stories.html", "Patient reviews · Prudent Dental Clinic, Viman Nagar", "What patients say about Dr. Puja Bansal and Prudent Dental Clinic.", stories, "stories.html")

# ----------------------------------------------------------------- FAQ --
fsub = "".join(f'<a href="#{k}">{E(v[0])}</a>' for k, v in FAQS.items())
fsec = "".join(f'<section id="{k}" class="section" style="padding-top:clamp(2.5rem,5vw,4rem);scroll-margin-top:calc(var(--head-h) + 70px)"><div class="wrap split"><h2 class="h" data-a style="font-size:var(--t-xl)">{E(v[0])}</h2><div data-a>{"".join(qa(q, a, i == 0) for i, (q, a) in enumerate(v[1]))}</div></div></section>' for k, v in FAQS.items())
faq = phead("FAQ", "Questions? <b>We've got answers</b>", "Visiting us, treatments, costs and emergencies. Can't find yours? Ask us on WhatsApp.", "faq") + f'<nav class="subnav" aria-label="FAQ topics"><div class="wrap"><div>{fsub}</div></div></nav>{fsec}' + cta("Still have a question?", "Message us on WhatsApp and a real person from the clinic replies.")
page("faq.html", "Dental FAQ · Prudent Dental Clinic, Viman Nagar", "Answers about first visits, implants, braces, costs, EMI, insurance, safety and emergencies.", faq, "faq.html")

# ------------------------------------------------------------- CONTACT --
contact = phead("Contact", "We're here <b>seven days a week</b>", "Call, WhatsApp or visit. For a dental emergency, please call so we can prioritise you.", "contact") + f"""
<section class="section"><div class="wrap"><div class="ccards" data-stagger>
  <a class="ccard" href="tel:{PHONE}">{PHONE_I}<b>{PHONE_D}</b><span>Call · also +91 98508 47079</span></a>
  <a class="ccard" href="{WA}" target="_blank" rel="noopener">{WA_I}<b>WhatsApp</b><span>Book, reschedule or ask a question</span></a>
  <a class="ccard" href="mailto:prudenthealthclinic@gmail.com">{MAIL}<b>Email</b><span>prudenthealthclinic@gmail.com</span></a></div></div></section>
<section class="section"><div class="wrap">{visit()}</div></section>
<section class="section"><div class="wrap"><div class="note" data-a><b>In an emergency, call first.</b> For a knocked-out adult tooth, keep it moist in milk and get to a dentist within about an hour. For uncontrolled bleeding, spreading facial swelling, or trouble breathing or swallowing, go to a hospital emergency department. We are not a 24-hour clinic.</div></div></section>""" + cta()
page("contact.html", "Contact & directions · Prudent Dental Clinic, DNK Square, Viman Nagar", "Office 503, DNK Square, New Airport Road, Viman Nagar, Pune 411014. Call or WhatsApp +91 70287 22200.", contact, "contact.html")

# ---------------------------------------------------------------- BOOK --
book = f"""<section class="phead"><div class="wrap"><div class="phead__panel" style="display:grid;grid-template-columns:1fr minmax(18rem,30rem);gap:clamp(1.5rem,4vw,3.5rem);align-items:start">
  <div><div class="crumbs"><a href="index.html">Home</a><span>/</span><span>Book a visit</span></div>
    <h1 class="h" data-a>Book your visit <b>in three taps.</b></h1>
    <p data-a style="--d:1">Pick a day, pick a time, and send it on WhatsApp. No forms, no accounts, nothing to type.</p>
    <ul class="ticks" data-stagger style="margin-top:28px">
      <li>{TICK}<span>Your first visit is a conversation and an examination with Dr. Bansal.</span></li>
      <li>{TICK}<span>A written estimate before any treatment begins.</span></li>
      <li>{TICK}<span>Evenings and Sundays are usually available.</span></li>
      <li>{TICK}<span>Bring any previous X-rays and a list of medicines you take.</span></li></ul>
    <div class="note" data-a style="margin-top:26px;background:rgba(255,255,255,.6)"><b>Pain, swelling or a broken tooth?</b> Please call <a href="tel:{PHONE}">{PHONE_D}</a> so we can see you sooner.</div></div>
  <div data-booker data-a="scale" style="--d:1"></div>
</div></div></section>
<style>@media (max-width: 900px) {{ .phead__panel[style*="grid-template-columns"] {{ grid-template-columns: 1fr !important; }} }}</style>"""
page("book.html", "Book a visit · Prudent Dental Clinic, Viman Nagar", "Book a dental visit in three taps on WhatsApp. Open 7 days.", book, "book.html")
