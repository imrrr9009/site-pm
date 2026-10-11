#!/usr/bin/env python3
"""Genereert de statische HTML-pagina's van Made for More."""
import json
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
SITE = "https://www.madeformore.nl"
EMAIL = "info@madeformore.nl"
TODAY = "2026-10-11"
NAME = "Made for More"

# ---------------------------------------------------------------- iconen (Lucide-stijl)
def ic(paths, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{paths}</svg>')

I = {
    "arrow": ic('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'),
    "check": ic('<path d="M20 6 9 17l-5-5"/>'),
    "checkc": ic('<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'),
    "x": ic('<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'),
    "menu": ic('<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>', "icon-open"),
    "close": ic('<path d="M18 6 6 18"/><path d="m6 6 12 12"/>', "icon-close"),
    "layout": ic('<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/>'),
    "palette": ic('<circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/>'),
    "search": ic('<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>'),
    "sparkles": ic('<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/>'),
    "pen": ic('<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
    "shield": ic('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>'),
    "gauge": ic('<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>'),
    "mail": ic('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'),
    "clock": ic('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    "map": ic('<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>'),
    "chat": ic('<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>'),
    "trend": ic('<path d="M22 7 13.5 15.5 8.5 10.5 2 17"/><path d="M16 7h6v6"/>'),
    "users": ic('<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'),
    "book": ic('<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/>'),
}

MARK = ('<svg class="brand__mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<rect width="64" height="64" rx="16" fill="#0F1115"/>'
        '<path d="M12 50V33.5a7.5 7.5 0 0 1 15 0V50M27 33.5a7.5 7.5 0 0 1 15 0V50" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M50 8.5v13M43.5 15h13" stroke="#FF5A36" stroke-width="5.5" stroke-linecap="round"/></svg>')
MARK_LIGHT = MARK.replace('fill="#0F1115"', 'fill="#FFFFFF"').replace('stroke="#fff"', 'stroke="#0F1115"')

NAV = [
    ("/diensten/", "Diensten"),
    ("/werkwijze/", "Werkwijze"),
    ("/prijzen/", "Prijzen"),
    ("/kennisbank/", "Kennisbank"),
    ("/over-ons/", "Over ons"),
]

# ---------------------------------------------------------------- schema.org
ORG_ID = f"{SITE}/#organisatie"
WEBSITE_ID = f"{SITE}/#website"

ORG = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": ORG_ID,
    "name": NAME,
    "alternateName": "Made for More webdesign",
    "url": f"{SITE}/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/img/icon-512.png", "width": 512, "height": 512},
    "image": f"{SITE}/assets/img/og-image.png",
    "description": "Made for More is een Nederlands webdesignbureau dat professionele, snelle en vindbare websites bouwt voor ondernemers en mkb-bedrijven, inclusief merkidentiteit, SEO en GEO (vindbaarheid in AI-zoekmachines).",
    "slogan": "Gemaakt voor meer.",
    "email": EMAIL,
    "areaServed": [{"@type": "Country", "name": "Nederland"}, {"@type": "Country", "name": "België"}],
    "knowsLanguage": ["nl", "en"],
    "priceRange": "€€",
    "knowsAbout": ["Webdesign", "Websiteontwikkeling", "Merkidentiteit", "Logo-ontwerp",
                   "Zoekmachineoptimalisatie (SEO)", "Generative Engine Optimization (GEO)",
                   "Copywriting", "Core Web Vitals", "Toegankelijkheid (WCAG)"],
    "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL,
                     "availableLanguage": ["Dutch", "English"], "areaServed": "NL"},
    # Vul aan zodra beschikbaar: "telephone", "address", "sameAs" (LinkedIn, Instagram, Google Bedrijfsprofiel), "vatID"
}
WEBSITE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": f"{SITE}/",
    "name": NAME,
    "inLanguage": "nl-NL",
    "publisher": {"@id": ORG_ID},
}


def breadcrumb_ld(crumbs):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}{u}"}
            for i, (u, n) in enumerate(crumbs)
        ],
    }


def faq_ld(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faqs
        ],
    }


def strip_tags(s):
    import re
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def webpage_ld(path, title, desc, ptype="WebPage"):
    return {
        "@type": ptype,
        "@id": f"{SITE}{path}#webpagina",
        "url": f"{SITE}{path}",
        "name": title,
        "description": desc,
        "inLanguage": "nl-NL",
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": ORG_ID},
        "dateModified": TODAY,
    }

# ---------------------------------------------------------------- bouwstenen
def header(active):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a class="nav__link" href="{u}"{cur if u == active else ""}>{n}</a></li>'
        for u, n in NAV
    )
    return f'''<a class="skip-link" href="#main">Naar de inhoud</a>
<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="/" aria-label="{NAME} — naar de homepage">{MARK}<span>made for more<span class="brand__plus">+</span></span></a>
    <nav class="nav" aria-label="Hoofdmenu">
      <div class="nav__panel" id="nav-panel">
        <ul class="nav__list">{items}</ul>
        <a class="btn btn--accent nav__panel-cta" href="/contact/">Plan een gratis kennismaking {I["arrow"]}</a>
      </div>
      <a class="btn btn--sm nav__cta" href="/contact/">Gratis kennismaking</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-panel" aria-label="Menu openen">{I["menu"]}{I["close"]}</button>
    </nav>
  </div>
</header>'''


def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="brand" href="/" aria-label="{NAME} — naar de homepage">{MARK_LIGHT}<span>made for more<span class="brand__plus">+</span></span></a>
        <p class="footer__tagline">Websites, merkidentiteit en vindbaarheid voor ondernemers die meer willen dan een visitekaartje online.</p>
      </div>
      <div>
        <p class="footer__title">Diensten</p>
        <ul class="footer__list">
          <li><a href="/diensten/#webdesign">Webdesign &amp; development</a></li>
          <li><a href="/diensten/#merkidentiteit">Logo &amp; merkidentiteit</a></li>
          <li><a href="/diensten/#seo">SEO</a></li>
          <li><a href="/diensten/#geo">GEO &amp; AI-vindbaarheid</a></li>
          <li><a href="/diensten/#onderhoud">Hosting &amp; onderhoud</a></li>
        </ul>
      </div>
      <div>
        <p class="footer__title">Made for More</p>
        <ul class="footer__list">
          <li><a href="/werkwijze/">Werkwijze</a></li>
          <li><a href="/prijzen/">Prijzen</a></li>
          <li><a href="/kennisbank/">Kennisbank</a></li>
          <li><a href="/over-ons/">Over ons</a></li>
        </ul>
      </div>
      <div>
        <p class="footer__title">Contact</p>
        <ul class="footer__list">
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="/contact/">Plan een kennismaking</a></li>
          <li>Werkgebied: Nederland &amp; België</li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p class="mb-0">© <span data-year>2026</span> {NAME}. Alle rechten voorbehouden.</p>
      <p class="mb-0"><a href="/privacy/">Privacyverklaring</a></p>
    </div>
  </div>
</footer>'''


def cta_band(title='Klaar voor een website die <span>meer</span> doet?',
             text="Plan een vrijblijvende kennismaking van 30 minuten. Je krijgt direct eerlijk advies over je huidige website — ook als je niet met ons verder gaat."):
    return f'''<section class="section section--dark cta-band" aria-labelledby="cta-titel">
  <div class="container">
    <h2 id="cta-titel" class="reveal">{title}</h2>
    <p class="reveal">{text}</p>
    <div class="btn-row reveal">
      <a class="btn btn--accent" href="/contact/">Plan een gratis kennismaking {I["arrow"]}</a>
      <a class="btn btn--ghost" href="/prijzen/">Bekijk de pakketten</a>
    </div>
  </div>
</section>'''


def crumbs_html(crumbs):
    lis = []
    for i, (u, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            lis.append(f'<li><span aria-current="page">{n}</span></li>')
        else:
            lis.append(f'<li><a href="{u}">{n}</a></li>')
    return f'<nav class="breadcrumbs" aria-label="Kruimelpad"><ol>{"".join(lis)}</ol></nav>'


def page_hero(crumbs, eyebrow, h1, lead, extra=""):
    return f'''<section class="page-hero">
  <div class="container">
    {crumbs_html(crumbs)}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{lead}</p>
    {extra}
  </div>
</section>'''


def faq_html(faqs):
    out = []
    for q, a in faqs:
        out.append(f'<details><summary>{q}</summary><div class="faq__answer"><p>{a}</p></div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def render(path, title, desc, body, active=None, ld=None, robots="index, follow, max-image-preview:large, max-snippet:-1",
           og_type="website", outfile=None):
    url = f"{SITE}{path}"
    graph = [ORG, WEBSITE] + (ld or [])
    ld_json = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    html = f'''<!doctype html>
<html lang="nl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="nl-NL" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#0F1115">
<meta name="author" content="{NAME}">

<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Made for More — websites die laten zien wie je bent">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&amp;family=Inter:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
<script src="/assets/js/main.js" defer></script>

<script type="application/ld+json">
{ld_json}
</script>
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    target = outfile or os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(html)


# ================================================================ inhoud
FAQ_HOME = [
    ("Wat kost een website bij Made for More?",
     "Een professionele bedrijfswebsite begint bij €1.495 (excl. btw) voor het Start-pakket tot 5 pagina's. Het populaire Groei-pakket met teksten, uitgebreide SEO en GEO kost €2.950. Voor maatwerk, webshops of een complete merkidentiteit maken we een offerte vanaf €5.500. Je krijgt altijd vooraf een vaste prijs."),
    ("Hoe lang duurt het voordat mijn website live staat?",
     "Een Start-website staat gemiddeld binnen 3 weken live, een Groei-website binnen 4 tot 6 weken. De planning hangt vooral af van hoe snel teksten, beeld en feedback beschikbaar zijn. Je krijgt bij de start een planning met vaste momenten."),
    ("Wat is het verschil tussen SEO en GEO?",
     "SEO (zoekmachineoptimalisatie) zorgt dat je hoog in de gewone zoekresultaten van Google en Bing verschijnt. GEO (Generative Engine Optimization) zorgt dat AI-zoekmachines zoals ChatGPT, Perplexity, Gemini en Google AI Overviews je bedrijf begrijpen, vertrouwen en noemen in hun antwoorden. Wij bouwen elke website voor allebei."),
    ("Ik heb nog geen logo of huisstijl. Kunnen jullie daarbij helpen?",
     "Ja. Veel ondernemers starten bij ons zonder logo. In het traject Logo &amp; merkidentiteit ontwikkelen we je logo, kleuren, lettertypes en tone of voice, zodat je website, social media en drukwerk één herkenbaar geheel vormen."),
    ("Kan ik de website daarna zelf aanpassen?",
     "Ja. Vanaf het Groei-pakket krijg je een gebruiksvriendelijk beheersysteem waarmee je zelf teksten, foto's en blogartikelen aanpast. Liever niets zelf doen? Dan regelen wij het via een onderhoudsabonnement."),
    ("Is de website na oplevering van mij?",
     "Ja. Na betaling ben jij eigenaar van je website, je domeinnaam en je content. Je zit nergens aan vast: je kunt altijd overstappen naar een andere partij."),
]

ARROW = I["arrow"]


def build_home():
    services = [
        ("layout", "Webdesign op maat", "Een website die past bij jouw bedrijf, niet bij een template. Strak ontworpen, supersnel en gebouwd om bezoekers klant te maken.", "/diensten/#webdesign"),
        ("palette", "Logo &amp; merkidentiteit", "Nog geen logo? Wij ontwikkelen je visuele identiteit: logo, kleuren, typografie en tone of voice.", "/diensten/#merkidentiteit"),
        ("search", "SEO", "Gevonden worden door klanten die nú zoeken. Technische SEO, zoekwoordenonderzoek en lokale vindbaarheid.", "/diensten/#seo"),
        ("sparkles", "GEO &amp; AI-vindbaarheid", "Genoemd worden in ChatGPT, Perplexity en Google AI Overviews. Wij structureren je site zodat AI je begrijpt én citeert.", "/diensten/#geo"),
        ("pen", "Teksten die verkopen", "Heldere, overtuigende webteksten in jouw tone of voice — geschreven voor mensen én zoekmachines.", "/diensten/#teksten"),
        ("shield", "Hosting &amp; onderhoud", "Veilig, snel en altijd up-to-date. Wij houden je site in topconditie, jij focust op je bedrijf.", "/diensten/#onderhoud"),
    ]
    svc = "".join(
        f'<article class="card card--link reveal" data-delay="{i*60}"><div class="card__icon">{I[k]}</div>'
        f'<h3>{t}</h3><p>{d}</p><div class="card__meta"><a class="link-arrow" href="{u}">Meer over deze dienst<span class="visually-hidden">: {strip_tags(t)}</span> {ARROW}</a></div></article>'
        for i, (k, t, d, u) in enumerate(services)
    )

    body = f'''
<section class="hero" aria-labelledby="hero-titel">
  <div class="container hero__grid">
    <div>
      <p class="eyebrow">Webdesign &amp; vindbaarheid voor ondernemers</p>
      <h1 id="hero-titel">Een website die laat zien wie je bent. <em>En klanten oplevert.</em></h1>
      <p class="hero__lead">Made for More bouwt professionele websites voor ondernemers en mkb-bedrijven. Mooi ontworpen, razendsnel en vindbaar in Google én in AI-zoekmachines zoals ChatGPT — zodat jouw bedrijf online net zo sterk overkomt als in het echt.</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="/contact/">Plan een gratis kennismaking {ARROW}</a>
        <a class="btn btn--ghost" href="/prijzen/">Bekijk prijzen</a>
      </div>
      <ul class="hero__proof">
        <li>{I["checkc"]} Vaste prijs, geen verrassingen</li>
        <li>{I["checkc"]} Binnen 3–6 weken live</li>
        <li>{I["checkc"]} Je bent zelf eigenaar</li>
      </ul>
    </div>
    <div class="mockup" aria-hidden="true">
      <span class="mockup__plus mockup__plus--1"></span>
      <span class="mockup__plus mockup__plus--2"></span>
      <div class="browser">
        <div class="browser__bar"><div class="browser__dots"><span></span><span></span><span></span></div><div class="browser__url">jouwbedrijf.nl</div></div>
        <div class="browser__body">
          <div class="sk sk--nav"></div>
          <div class="sk sk--h"></div>
          <div class="sk sk--h2"></div>
          <div class="sk sk--p"></div>
          <div class="sk sk--p2"></div>
          <div class="sk-row"><div class="sk sk--btn"></div><div class="sk sk--btn2"></div></div>
          <div class="sk-cards"><div class="sk-card"></div><div class="sk-card"></div><div class="sk-card"></div></div>
        </div>
      </div>
      <div class="float-card float-card--search"><div class="float-card__icon">{I["sparkles"]}</div><div><strong>Genoemd door AI</strong><span>ChatGPT · Perplexity · Gemini</span></div></div>
      <div class="float-card float-card--speed"><div class="float-card__score">90+</div><div><strong>Snel &amp; vindbaar</strong><span>Gebouwd op Core Web Vitals</span></div></div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker__track">
    <span>Meer vindbaarheid</span><span>Meer vertrouwen</span><span>Meer aanvragen</span><span>Meer herkenning</span><span>Meer rust</span><span>Meer groei</span>
    <span>Meer vindbaarheid</span><span>Meer vertrouwen</span><span>Meer aanvragen</span><span>Meer herkenning</span><span>Meer rust</span><span>Meer groei</span>
  </div>
</div>

<section class="section" aria-labelledby="probleem-titel">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Herkenbaar?</p>
      <h2 id="probleem-titel">Je bedrijf is beter dan je website laat zien.</h2>
      <p class="lead">Je website is vaak het eerste contact met een nieuwe klant. Binnen een paar seconden besluit een bezoeker of je betrouwbaar en professioneel overkomt. Een verouderde of onduidelijke site kost je dus elke dag klanten — zonder dat je het merkt.</p>
      <p>Made for More maakt van je website je beste verkoper: een plek die je identiteit professioneel laat zien en die bezoekers stap voor stap richting een aanvraag leidt.</p>
    </div>
    <ul class="problem-list">
      <li class="reveal"><span class="problem-list__x">{I["x"]}</span><div><strong>Verouderd of niet van jou</strong><p>Een template die op die van de concurrent lijkt, of een site die al jaren niet is bijgewerkt.</p></div></li>
      <li class="reveal" data-delay="80"><span class="problem-list__x">{I["x"]}</span><div><strong>Onvindbaar</strong><p>Niet zichtbaar in Google en niet genoemd wanneer klanten ChatGPT om een aanbeveling vragen.</p></div></li>
      <li class="reveal" data-delay="160"><span class="problem-list__x">{I["x"]}</span><div><strong>Levert niets op</strong><p>Bezoekers komen binnen, maar haken af. Geen duidelijke boodschap, geen heldere volgende stap.</p></div></li>
    </ul>
  </div>
</section>

<section class="section section--white" aria-labelledby="diensten-titel">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Diensten</p>
      <h2 id="diensten-titel">Alles voor een sterke online identiteit — onder één dak.</h2>
      <p>Van eerste schets tot een website die maandelijks nieuwe klanten oplevert. Je hebt één aanspreekpunt en één plan.</p>
    </div>
    <div class="grid grid--3">{svc}</div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="meer-titel">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Waarom “Made for More”</p>
      <h2 id="meer-titel">Een website is geen visitekaartje. Het is je beste verkoper.</h2>
      <p>Daarom bouwen we elke site rond drie doelen. Geen losse pagina's, maar een systeem dat werkt.</p>
    </div>
    <div class="grid grid--3">
      <div class="pillar reveal"><div class="pillar__num">+01</div><h3>Meer vertrouwen</h3><p>Een professioneel ontwerp dat jouw identiteit uitstraalt. Bezoekers zien direct wie je bent, wat je doet en waarom ze voor jou moeten kiezen.</p></div>
      <div class="pillar reveal" data-delay="80"><div class="pillar__num">+02</div><h3>Meer vindbaarheid</h3><p>Technisch perfect, razendsnel en inhoudelijk sterk. Zo vinden klanten je in Google, Google Maps én in de antwoorden van AI-assistenten.</p></div>
      <div class="pillar reveal" data-delay="160"><div class="pillar__num">+03</div><h3>Meer aanvragen</h3><p>Heldere teksten, duidelijke knoppen en een slimme opbouw. Elke pagina heeft één doel: van bezoeker naar klant.</p></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="werkwijze-titel">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Werkwijze</p>
      <h2 id="werkwijze-titel">In 4 stappen naar een website waar je trots op bent.</h2>
      <p>Duidelijk, persoonlijk en zonder vakjargon. Je weet altijd waar je aan toe bent.</p>
    </div>
    <ol class="steps">
      <li class="reveal"><span class="steps__time">Week 1</span><h3>Kennismaken &amp; strategie</h3><p>We leren je bedrijf, klanten en concurrenten kennen en bepalen samen de doelen en zoekwoorden.</p></li>
      <li class="reveal" data-delay="80"><span class="steps__time">Week 1–2</span><h3>Identiteit &amp; ontwerp</h3><p>We vertalen je merk naar een ontwerp. Je ziet het eerst, geeft feedback en keurt goed.</p></li>
      <li class="reveal" data-delay="160"><span class="steps__time">Week 2–5</span><h3>Bouwen &amp; schrijven</h3><p>We bouwen je site, schrijven de teksten en richten SEO, GEO en statistieken in.</p></li>
      <li class="reveal" data-delay="240"><span class="steps__time">Lancering</span><h3>Live &amp; groeien</h3><p>Na een uitgebreide check gaat je site live. Daarna meten, verbeteren en groeien we door.</p></li>
    </ol>
    <p class="mt-7 reveal"><a class="link-arrow" href="/werkwijze/">Bekijk de volledige werkwijze {ARROW}</a></p>
  </div>
</section>

<section class="section section--alt" aria-labelledby="geo-titel">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">SEO &amp; GEO</p>
      <h2 id="geo-titel">Gevonden worden in Google én in ChatGPT.</h2>
      <p class="lead">Steeds meer mensen stellen hun vraag niet meer aan Google, maar aan een AI-assistent. Die noemt maar een handvol bedrijven. Wij zorgen dat jij daar bij hoort.</p>
      <ul class="checklist">
        <li>{I["check"]}<span><strong>Gestructureerde data (schema.org)</strong> zodat zoekmachines en AI precies begrijpen wie je bent, wat je aanbiedt en waar.</span></li>
        <li>{I["check"]}<span><strong>Citeerbare content</strong>: heldere definities, concrete antwoorden en FAQ's die AI-modellen graag overnemen.</span></li>
        <li>{I["check"]}<span><strong>Technische basis</strong>: snelle laadtijden, schone code, toegankelijkheid, sitemap en een AI-vriendelijke robots.txt en llms.txt.</span></li>
        <li>{I["check"]}<span><strong>Autoriteit &amp; vertrouwen</strong>: Google Bedrijfsprofiel, reviews en vermeldingen die je geloofwaardigheid versterken.</span></li>
      </ul>
      <a class="link-arrow" href="/kennisbank/wat-is-geo/">Lees: wat is GEO precies? {ARROW}</a>
    </div>
    <div class="reveal" data-delay="100">
      <dl class="definition"><dt>SEO — Search Engine Optimization</dt><dd>Je website zo inrichten dat hij hoog verschijnt in de klassieke zoekresultaten van Google en Bing, voor de zoekwoorden die jouw klanten gebruiken.</dd></dl>
      <dl class="definition"><dt>GEO — Generative Engine Optimization</dt><dd>Je website en online aanwezigheid zo inrichten dat AI-zoekmachines zoals ChatGPT, Perplexity, Gemini en Google AI Overviews jouw bedrijf begrijpen, vertrouwen en noemen in hun antwoorden.</dd></dl>
      <dl class="definition"><dt>Wat wij doen</dt><dd>Elke Made for More-website wordt standaard gebouwd voor allebei. Zo ben je vindbaar op de manier waarop mensen vandaag zoeken — en morgen.</dd></dl>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="pakketten-titel">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Pakketten</p>
      <h2 id="pakketten-titel">Heldere prijzen. Geen kleine lettertjes.</h2>
      <p>Alle prijzen zijn eenmalig en exclusief btw. Je kiest zelf of je daarna een onderhoudsabonnement wilt.</p>
    </div>
    {pricing_cards()}
    <p class="text-center mt-6 reveal"><a class="link-arrow" href="/prijzen/">Alle pakketten, extra's en onderhoud vergelijken {ARROW}</a></p>
  </div>
</section>

<section class="section section--tight" aria-labelledby="aanbod-titel">
  <div class="container">
    <div class="offer reveal">
      <div>
        <p class="eyebrow">Lanceringsaanbod</p>
        <h2 id="aanbod-titel">Word één van onze eerste 5 partners.</h2>
        <p>Made for More is nieuw — en dat is jouw voordeel. Je krijgt onze volledige aandacht, en wij bouwen samen met jou aan ons portfolio.</p>
        <a class="btn" href="/contact/?aanbod=partner">Ik wil partner worden {ARROW}</a>
      </div>
      <ul>
        <li>{I["check"]} 20% korting op elk websitepakket</li>
        <li>{I["check"]} Gratis logo-opfrissing of merkscan</li>
        <li>{I["check"]} 3 maanden gratis onderhoud</li>
        <li>{I["check"]} In ruil voor een eerlijke review en een case op onze site</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="faq-titel">
  <div class="container container--narrow">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Veelgestelde vragen</p>
      <h2 id="faq-titel">Goed om te weten.</h2>
    </div>
    {faq_html(FAQ_HOME)}
  </div>
</section>

{cta_band()}
'''
    title = "Made for More | Professionele websites voor ondernemers"
    desc = "Professionele websites voor ondernemers en mkb: op maat ontworpen, snel en vindbaar in Google én AI-zoekmachines. Vaste prijs vanaf €1.495."
    render("/", title, desc, body, active=None,
           ld=[webpage_ld("/", title, desc), faq_ld(FAQ_HOME)])


PACKAGES = [
    {
        "name": "Start", "price": "€1.495", "unit": "eenmalig", "note": "Excl. btw · live in ±3 weken",
        "desc": "Voor zzp'ers en starters die professioneel online willen staan.",
        "features": ["Tot 5 pagina's, uniek ontwerp", "Perfect op mobiel, tablet en desktop", "Technische SEO + GEO-basis", "Schema.org-gegevens voor Google &amp; AI", "Contactformulier met spambeveiliging", "Google Bedrijfsprofiel ingericht", "Privacyvriendelijke statistieken"],
        "cta": "Start-pakket aanvragen", "featured": False,
    },
    {
        "name": "Groei", "price": "€2.950", "unit": "eenmalig", "note": "Excl. btw · live in 4–6 weken",
        "desc": "Voor ondernemers die serieus willen groeien met hun website.",
        "features": ["Alles uit Start, plus:", "Tot 10 pagina's", "Teksten geschreven door ons", "Zoekwoorden- en concurrentieonderzoek", "Uitgebreide GEO: FAQ's, kennisbank &amp; llms.txt", "2 SEO-blogartikelen bij de lancering", "Zelf aanpassen via beheersysteem", "Training van 1 uur"],
        "cta": "Groei-pakket aanvragen", "featured": True,
    },
    {
        "name": "Op maat", "price": "vanaf €5.500", "unit": "", "note": "Excl. btw · planning in overleg",
        "desc": "Voor bedrijven met grotere ambities of specifieke wensen.",
        "features": ["Alles uit Groei, plus:", "Volledige merkidentiteit &amp; logo", "Onbeperkt aantal pagina's", "Webshop, boekingen of koppelingen", "Meertalige website", "Conversie-optimalisatie &amp; A/B-tests", "Persoonlijke strategiesessies"],
        "cta": "Offerte op maat", "featured": False,
    },
]


def pricing_cards():
    cards = []
    for i, p in enumerate(PACKAGES):
        cls = "card price-card reveal" + (" price-card--featured" if p["featured"] else "")
        badge = '<span class="price-card__badge">Meest gekozen</span>' if p["featured"] else ""
        feats = "".join(f"<li>{I['check']}<span>{f}</span></li>" for f in p["features"])
        unit = f" <small>{p['unit']}</small>" if p["unit"] else ""
        price_html = p["price"].replace("vanaf ", '<span class="from">vanaf</span>')
        btn = "btn btn--accent btn--block" if p["featured"] else "btn btn--ghost btn--block"
        cards.append(f'''<article class="{cls}" data-delay="{i*80}">{badge}
  <h3 class="price-card__name">{p["name"]}</h3><p>{p["desc"]}</p>
  <p class="price-card__price">{price_html}{unit}</p><p class="price-card__note">{p["note"]}</p>
  <ul class="price-card__features">{feats}</ul>
  <a class="{btn}" href="/contact/?pakket={p["name"].lower().replace(" ", "-")}">{p["cta"]}</a>
</article>''')
    return '<div class="grid grid--3 pricing">' + "".join(cards) + "</div>"


def build_diensten():
    blocks = [
        ("webdesign", "layout", "Webdesign &amp; development",
         "Een website die volledig is afgestemd op jouw bedrijf, je klanten en je doelen. Geen standaardtemplate, maar een uniek ontwerp dat jouw identiteit professioneel neerzet en bezoekers omzet in aanvragen.",
         ["Uniek ontwerp op basis van jouw merk", "Mobile-first: perfect op elk scherm", "Snelle laadtijden en sterke Core Web Vitals", "Toegankelijk volgens WCAG-richtlijnen", "Duidelijke call-to-actions en conversiegerichte opbouw", "Veilig: HTTPS, spambeveiliging en AVG-proof"],
         "Voor wie: zzp'ers, dienstverleners, lokale bedrijven en mkb."),
        ("merkidentiteit", "palette", "Logo &amp; merkidentiteit",
         "Je identiteit is meer dan een logo. Het is hoe mensen je zien, herkennen en onthouden. We ontwikkelen een merk dat klopt met wie je bent — en dat overal consistent terugkomt: op je website, social media, offertes en bedrijfskleding.",
         ["Merkscan: waar sta je voor en voor wie?", "Logo-ontwerp in meerdere varianten", "Kleurenpalet en typografie", "Tone of voice: hoe je klinkt", "Compacte brandguide (PDF)", "Social media-templates en visitekaartje"],
         "Ideaal als je nog geen logo hebt of je huidige uitstraling niet meer past."),
        ("seo", "search", "SEO — vindbaar in Google",
         "Wij zorgen dat je gevonden wordt door mensen die op dit moment zoeken naar wat jij aanbiedt. Dat begint bij een technisch perfecte website en eindigt bij content die écht antwoord geeft op de vragen van je klanten.",
         ["Zoekwoorden- en concurrentieonderzoek", "Technische SEO: snelheid, structuur, indexatie", "Sterke titels, meta-beschrijvingen en koppen", "Lokale SEO en Google Bedrijfsprofiel", "Interne links en een logische sitestructuur", "Maandelijkse rapportage (bij abonnement)"],
         "Resultaat: meer relevante bezoekers die klaar zijn om contact op te nemen."),
        ("geo", "sparkles", "GEO — vindbaar in AI-zoekmachines",
         "ChatGPT, Perplexity, Gemini, Copilot en Google AI Overviews geven steeds vaker direct antwoord — en noemen daarbij een paar bedrijven. Generative Engine Optimization zorgt dat jouw bedrijf er één van is.",
         ["Uitgebreide schema.org-gegevens (organisatie, diensten, FAQ)", "Citeerbare content: definities, feiten en duidelijke antwoorden", "Een vaste, consistente bedrijfsomschrijving op het hele web", "AI-crawlers toegestaan via robots.txt en llms.txt", "Kennisbank met expertartikelen (E-E-A-T)", "Vermeldingen op betrouwbare externe platformen"],
         "Klaar voor de manier waarop mensen vandaag én morgen zoeken."),
        ("teksten", "pen", "Teksten &amp; content",
         "Goede teksten maken het verschil tussen ‘mooi’ en ‘ik wil contact’. We schrijven heldere, overtuigende webteksten in jouw tone of voice, die prettig lezen én scoren in zoekmachines.",
         ["Interview om jouw verhaal scherp te krijgen", "Webteksten per pagina", "SEO- en GEO-geoptimaliseerde blogartikelen", "Veelgestelde vragen die echt helpen"],
         "Je hoeft zelf niets te schrijven — alleen feedback te geven."),
        ("onderhoud", "shield", "Hosting &amp; onderhoud",
         "Na de lancering begint het pas. Wij zorgen dat je website veilig, snel en up-to-date blijft, en helpen je verder te groeien.",
         ["Snelle, veilige hosting in Europa", "Dagelijkse back-ups en monitoring", "Updates en beveiliging", "Kleine aanpassingen inbegrepen", "Vaste contactpersoon"],
         "Abonnementen vanaf €39 per maand."),
    ]
    out = []
    for bid, icon, title, intro, items, note in blocks:
        lis = "".join(f"<li>{I['check']}<span>{x}</span></li>" for x in items)
        out.append(f'''<section class="service-block" id="{bid}" aria-labelledby="{bid}-titel">
  <div class="reveal"><h2 id="{bid}-titel"><span class="card__icon">{I[icon]}</span>{title}</h2><p class="lead">{intro}</p></div>
  <div class="reveal" data-delay="80"><ul class="checklist">{lis}</ul><p class="text-muted mb-0"><strong>{note}</strong></p></div>
</section>''')

    crumbs = [("/", "Home"), ("/diensten/", "Diensten")]
    body = page_hero(crumbs, "Diensten", "Alles voor een professionele online identiteit.",
                     "Van logo tot vindbaarheid in AI-zoekmachines: Made for More regelt je complete online aanwezigheid. Kies één dienst of combineer ze in een pakket.",
                     f'<div class="btn-row"><a class="btn btn--accent" href="/contact/">Bespreek je project {ARROW}</a><a class="btn btn--ghost" href="/prijzen/">Bekijk prijzen</a></div>')
    body += f'<div class="container">{"".join(out)}</div>' + cta_band()

    services_ld = [{
        "@type": "Service",
        "@id": f"{SITE}/diensten/#{bid}",
        "name": strip_tags(title),
        "description": strip_tags(intro),
        "provider": {"@id": ORG_ID},
        "areaServed": {"@type": "Country", "name": "Nederland"},
        "serviceType": strip_tags(title),
    } for bid, icon, title, intro, items, note in blocks]
    title = "Diensten: webdesign, logo, SEO & GEO | Made for More"
    desc = "Webdesign op maat, logo en merkidentiteit, SEO, GEO (vindbaarheid in ChatGPT en AI), webteksten en onderhoud. Alles voor een professionele online identiteit."
    render("/diensten/", title, desc, body, active="/diensten/",
           ld=[webpage_ld("/diensten/", title, desc, "CollectionPage"), breadcrumb_ld(crumbs)] + services_ld)


def build_werkwijze():
    steps = [
        ("Kennismaking", "Gratis · 30 minuten", "We bespreken je bedrijf, je doelen en je huidige website. Je krijgt direct eerlijk advies, ook als je niet met ons verder gaat. Binnen 2 werkdagen ontvang je een helder voorstel met een vaste prijs."),
        ("Strategie &amp; merk", "Week 1", "Een strategiesessie waarin we je doelgroep, propositie, concurrenten en zoekwoorden scherp krijgen. Heb je nog geen logo of huisstijl? Dan ontwikkelen we die in deze fase."),
        ("Structuur &amp; ontwerp", "Week 1–2", "We maken de sitestructuur en het ontwerp van de belangrijkste pagina's. Je ziet precies hoe je website eruit komt te zien en hebt twee feedbackrondes."),
        ("Teksten &amp; bouw", "Week 2–5", "We schrijven de teksten (Groei en Op maat) en bouwen de website. SEO, GEO, schema.org, snelheid en toegankelijkheid zitten er vanaf de eerste regel code in."),
        ("Testen &amp; lancering", "Week 4–6", "We testen op alle apparaten en browsers, controleren snelheid en vindbaarheid, en zetten de site live. We melden je aan bij Google Search Console en Bing."),
        ("Meten &amp; groeien", "Na de lancering", "Na 30 dagen bespreken we de eerste resultaten. Met een onderhoudsabonnement blijven we je site verbeteren, beveiligen en uitbreiden."),
    ]
    lis = "".join(
        f'<li class="card reveal" data-delay="{(i%3)*80}"><span class="steps__time">Stap {i+1} · {t}</span><h3 class="mt-0" style="margin-top:var(--space-3)">{n}</h3><p>{d}</p></li>'
        for i, (n, t, d) in enumerate(steps))
    crumbs = [("/", "Home"), ("/werkwijze/", "Werkwijze")]
    faqs = [
        ("Wat moet ik zelf aanleveren?", "Bij voorkeur je logo (als je dat hebt), eigen foto's en input over je bedrijf. Teksten schrijven wij in het Groei- en Op maat-pakket. Geen goede foto's? Dan adviseren we een fotograaf of gebruiken we passend beeld."),
        ("Hoeveel tijd kost het mij?", "Reken op ongeveer 4 tot 6 uur verspreid over het hele traject: de kennismaking, een strategiesessie, feedback op het ontwerp en een eindcontrole."),
        ("Hoe verloopt de betaling?", "Je betaalt 50% bij de start en 50% bij de oplevering. Voor het Op maat-traject spreken we betaling in termijnen af."),
    ]
    body = page_hero(crumbs, "Werkwijze", "Helder proces. Geen verrassingen.",
                     "Van eerste gesprek tot een website die klanten oplevert, in gemiddeld 3 tot 6 weken. Je weet altijd wat er gebeurt, wat het kost en wat we van je nodig hebben.")
    body += f'''<section class="section"><div class="container"><ol class="grid grid--3" style="list-style:none;padding:0;margin:0">{lis}</ol></div></section>
<section class="section section--white" aria-labelledby="ww-faq"><div class="container container--narrow"><div class="section-head section-head--center"><p class="eyebrow">Vragen over het proces</p><h2 id="ww-faq">Wat kun je verwachten?</h2></div>{faq_html(faqs)}</div></section>
{cta_band()}'''
    howto = {
        "@type": "HowTo",
        "name": "Zo maakt Made for More jouw website",
        "description": "Het stappenplan van kennismaking tot lancering en groei.",
        "totalTime": "P6W",
        "step": [{"@type": "HowToStep", "position": i + 1, "name": strip_tags(n), "text": d} for i, (n, t, d) in enumerate(steps)],
    }
    title = "Werkwijze: in 6 stappen naar je website | Made for More"
    desc = "Zo werkt Made for More: kennismaking, strategie, ontwerp, bouw, lancering en groei. Binnen 3 tot 6 weken live, met een vaste prijs."
    render("/werkwijze/", title, desc, body, active="/werkwijze/",
           ld=[webpage_ld("/werkwijze/", title, desc), breadcrumb_ld(crumbs), howto, faq_ld(faqs)])


def build_prijzen():
    crumbs = [("/", "Home"), ("/prijzen/", "Prijzen")]
    addons = [
        ("Logo &amp; merkidentiteit", "Logo, kleuren, typografie, tone of voice en een compacte brandguide.", "vanaf €750"),
        ("Extra pagina", "Ontwerp en bouw van een extra pagina in je bestaande stijl.", "€150"),
        ("Webteksten (Start-pakket)", "Wij schrijven de teksten voor maximaal 5 pagina's.", "€395"),
        ("SEO/GEO-blogartikel", "Een expertartikel van 800–1.200 woorden, geoptimaliseerd voor Google en AI.", "€175"),
        ("Meertaligheid", "Een extra taalversie, inclusief juiste hreflang-instellingen.", "vanaf €495"),
    ]
    rows = "".join(f"<tr><td><strong>{n}</strong><span>{d}</span></td><td>{p}</td></tr>" for n, d, p in addons)
    plans = [
        ("Basis", "€39", "Hosting in Europa, SSL, dagelijkse back-ups, updates en beveiligingsmonitoring."),
        ("Zorgeloos", "€89", "Alles uit Basis + 1 uur aanpassingen per maand, maandelijkse snelheids- en SEO-check en een rapport."),
        ("Groei", "€249", "Alles uit Zorgeloos + 2 SEO/GEO-artikelen per maand, doorlopende optimalisatie en een kwartaalgesprek."),
    ]
    plan_html = "".join(
        f'<article class="card reveal" data-delay="{i*80}"><h3>{n}</h3><p class="price-card__price">{p} <small>per maand</small></p><p class="price-card__note">Excl. btw · maandelijks opzegbaar</p><p>{d}</p></article>'
        for i, (n, p, d) in enumerate(plans))
    faqs = [
        ("Zijn er verborgen kosten?", "Nee. Je krijgt vooraf een vaste prijs. Alleen je domeinnaam (meestal €10–15 per jaar) en eventuele betaalde licenties of stockfoto's komen erbij — dat weet je altijd vooraf."),
        ("Moet ik een onderhoudsabonnement nemen?", "Nee, het is niet verplicht. Wel raden we het aan: een website die veilig, snel en actueel blijft, scoort beter in Google en AI-zoekmachines. Abonnementen zijn maandelijks opzegbaar."),
        ("Kan ik later upgraden van Start naar Groei?", "Ja. Je betaalt dan alleen het verschil voor de onderdelen die je erbij wilt. Zo kun je klein beginnen en meegroeien."),
    ]
    body = page_hero(crumbs, "Prijzen", "Investeer in een website die zichzelf terugverdient.",
                     "Heldere pakketten met een vaste prijs. Alle bedragen zijn eenmalig en exclusief 21% btw, tenzij anders vermeld.")
    body += f'''<section class="section"><div class="container">{pricing_cards()}</div></section>
<section class="section section--tight" aria-labelledby="abon-titel"><div class="container">
  <div class="section-head reveal"><p class="eyebrow">Na de lancering</p><h2 id="abon-titel">Onderhoud &amp; groei-abonnementen</h2><p>Maandelijks opzegbaar. Voor ondernemers die zich willen focussen op hun bedrijf.</p></div>
  <div class="grid grid--3">{plan_html}</div>
</div></section>
<section class="section section--white" aria-labelledby="extra-titel"><div class="container">
  <div class="section-head reveal"><p class="eyebrow">Extra's</p><h2 id="extra-titel">Losse diensten en uitbreidingen</h2></div>
  <div class="table-wrap reveal"><table class="addon-table"><thead><tr><th scope="col">Dienst</th><th scope="col">Prijs (excl. btw)</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="section" aria-labelledby="prijs-faq"><div class="container container--narrow"><div class="section-head section-head--center"><p class="eyebrow">Vragen over prijzen</p><h2 id="prijs-faq">Eerlijk en transparant.</h2></div>{faq_html(faqs)}</div></section>
{cta_band()}'''
    offers = {
        "@type": "OfferCatalog",
        "name": "Websitepakketten Made for More",
        "url": f"{SITE}/prijzen/",
        "itemListElement": [{
            "@type": "Offer",
            "name": f"Website {p['name']}",
            "description": p["desc"],
            "price": p["price"].replace("vanaf ", "").replace("€", "").replace(".", ""),
            "priceCurrency": "EUR",
            "priceSpecification": {"@type": "PriceSpecification", "price": p["price"].replace("vanaf ", "").replace("€", "").replace(".", ""), "priceCurrency": "EUR", "valueAddedTaxIncluded": False,
                                   **({"minPrice": p["price"].replace("vanaf ", "").replace("€", "").replace(".", "")} if "vanaf" in p["price"] else {})},
            "seller": {"@id": ORG_ID},
        } for p in PACKAGES],
    }
    title = "Prijzen: wat kost een website? Vanaf €1.495 | Made for More"
    desc = "Transparante websiteprijzen: Start €1.495, Groei €2.950, Op maat vanaf €5.500. Onderhoud vanaf €39 per maand. Vaste prijs, geen verrassingen."
    render("/prijzen/", title, desc, body, active="/prijzen/",
           ld=[webpage_ld("/prijzen/", title, desc), breadcrumb_ld(crumbs), offers, faq_ld(faqs)])


def build_over():
    crumbs = [("/", "Home"), ("/over-ons/", "Over ons")]
    values = [
        ("Eerlijk", "We zeggen wat we denken en beloven alleen wat we waarmaken. Ook als dat betekent dat je iets niet nodig hebt."),
        ("Functioneel mooi", "Design is geen versiering. Elk detail heeft een doel: vertrouwen wekken, informeren of overtuigen."),
        ("Meetbaar", "We bouwen voor resultaat: meer bezoekers, meer aanvragen, meer klanten. En dat maken we zichtbaar."),
        ("Persoonlijk", "Eén vast aanspreekpunt dat jouw bedrijf kent. Geen tickets, geen wachtrijen."),
    ]
    vh = "".join(f'<div class="card reveal" data-delay="{i*60}"><div class="pillar__num" style="color:var(--accent-ink)">+0{i+1}</div><h3>{n}</h3><p>{d}</p></div>' for i, (n, d) in enumerate(values))
    body = page_hero(crumbs, "Over ons", "Elk bedrijf is gemaakt voor meer.",
                     "Made for More helpt ondernemers hun identiteit online professioneel en functioneel neer te zetten. Want je website is vaak de eerste indruk — en die moet kloppen.")
    body += f'''<section class="section"><div class="container split">
  <div class="reveal">
    <p class="eyebrow">Ons verhaal</p>
    <h2>Waarom Made for More?</h2>
    <p class="lead">Te veel goede bedrijven worden online onderschat. Ze leveren topwerk, maar hun website vertelt dat verhaal niet. Dat is zonde — en onnodig.</p>
    <p>Made for More is opgericht met één overtuiging: elke ondernemer verdient een website die net zo professioneel is als het werk dat hij of zij levert. Een website die laat zien wie je bent, waar je voor staat en waarom klanten voor jou moeten kiezen.</p>
    <p>We combineren strategie, design, techniek en vindbaarheid. Zo krijg je niet alleen een mooie site, maar een website die werkt: in Google, in AI-zoekmachines en bij je klanten.</p>
  </div>
  <!-- TODO: vervang dit blok door een persoonlijke foto en introductie van de oprichter (naam, achtergrond, expertise). Dit versterkt vertrouwen én E-E-A-T voor Google en AI. -->
  <div class="card reveal" data-delay="100">
    <p class="eyebrow">Onze belofte</p>
    <ul class="checklist">
      <li>{I["check"]}<span>Eén vast aanspreekpunt, van start tot lancering en daarna</span></li>
      <li>{I["check"]}<span>Vooraf een vaste prijs en een duidelijke planning</span></li>
      <li>{I["check"]}<span>Binnen 1 werkdag reactie op je vragen</span></li>
      <li>{I["check"]}<span>Jij bent eigenaar van je website en domein</span></li>
      <li>{I["check"]}<span>Gebouwd volgens de nieuwste SEO-, GEO- en toegankelijkheidsrichtlijnen</span></li>
    </ul>
  </div>
</div></section>
<section class="section section--white" aria-labelledby="waarden-titel"><div class="container">
  <div class="section-head reveal"><p class="eyebrow">Waar we voor staan</p><h2 id="waarden-titel">Onze waarden</h2></div>
  <div class="grid grid--4">{vh}</div>
</div></section>
{cta_band("Laten we kennismaken.", "Benieuwd wat Made for More voor jouw bedrijf kan betekenen? Plan een vrijblijvend gesprek van 30 minuten.")}'''
    title = "Over ons: waarom Made for More | Webdesign voor ondernemers"
    desc = "Made for More helpt ondernemers hun bedrijfsidentiteit online professioneel en functioneel te tonen. Lees ons verhaal, onze waarden en onze belofte."
    render("/over-ons/", title, desc, body, active="/over-ons/",
           ld=[webpage_ld("/over-ons/", title, desc, "AboutPage"), breadcrumb_ld(crumbs)])


def build_contact():
    crumbs = [("/", "Home"), ("/contact/", "Contact")]
    needs = ["Nieuwe website", "Logo &amp; huisstijl", "SEO / GEO", "Teksten", "Onderhoud", "Weet ik nog niet"]
    chips = "".join(f'<label class="chip"><input type="checkbox" name="interesse" value="{strip_tags(n)}"><span>{n}</span></label>' for n in needs)
    body = page_hero(crumbs, "Contact", "Plan een gratis kennismaking.",
                     "Vertel kort over je bedrijf en je wensen. Je hoort binnen 1 werkdag van ons, met een voorstel voor een vrijblijvend gesprek van 30 minuten.")
    body += f'''<section class="section"><div class="container split" style="align-items:start">
  <form class="form card" name="contact" method="POST" action="/bedankt/" data-netlify="true" netlify-honeypot="bot-field" data-validate novalidate>
    <input type="hidden" name="form-name" value="contact">
    <p hidden><label>Niet invullen: <input name="bot-field"></label></p>
    <div class="form__row form__row--2">
      <div class="field"><label for="naam">Naam</label><input id="naam" name="naam" type="text" autocomplete="name" required aria-describedby="naam-error"><span class="field__error" id="naam-error" aria-live="polite"></span></div>
      <div class="field"><label for="bedrijf">Bedrijfsnaam <span class="hint">(optioneel)</span></label><input id="bedrijf" name="bedrijf" type="text" autocomplete="organization"></div>
    </div>
    <div class="form__row form__row--2">
      <div class="field"><label for="email">E-mailadres</label><input id="email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="email-error"><span class="field__error" id="email-error" aria-live="polite"></span></div>
      <div class="field"><label for="telefoon">Telefoonnummer <span class="hint">(optioneel)</span></label><input id="telefoon" name="telefoon" type="tel" autocomplete="tel" inputmode="tel"></div>
    </div>
    <fieldset class="field chips"><legend>Waar kunnen we je mee helpen?</legend>{chips}</fieldset>
    <div class="field"><label for="budget">Indicatie budget <span class="hint">(helpt ons een passend voorstel te maken)</span></label>
      <select id="budget" name="budget"><option value="">Maak een keuze</option><option>Tot €1.500</option><option>€1.500 – €3.000</option><option>€3.000 – €6.000</option><option>Meer dan €6.000</option><option>Weet ik nog niet</option></select></div>
    <div class="field"><label for="bericht">Vertel kort over je bedrijf en je wensen</label><textarea id="bericht" name="bericht" required aria-describedby="bericht-hint bericht-error"></textarea><span class="hint" id="bericht-hint">Bijvoorbeeld: wat doe je, wie zijn je klanten en wat moet je website opleveren?</span><span class="field__error" id="bericht-error" aria-live="polite"></span></div>
    <button class="btn btn--accent btn--block" type="submit">Verstuur aanvraag {ARROW}</button>
    <p class="form__privacy">We gebruiken je gegevens alleen om contact met je op te nemen over je aanvraag. Lees onze <a href="/privacy/">privacyverklaring</a>.</p>
  </form>
  <aside class="contact-aside" aria-label="Contactgegevens">
    <div class="contact-item"><span class="card__icon">{I["mail"]}</span><div><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="contact-item"><span class="card__icon">{I["clock"]}</span><div><strong>Reactietijd</strong>Binnen 1 werkdag, op werkdagen van 9:00 tot 17:30.</div></div>
    <div class="contact-item"><span class="card__icon">{I["map"]}</span><div><strong>Werkgebied</strong>Heel Nederland en België — op locatie of online.</div></div>
    <div class="card card--dark"><h3>Wat gebeurt er na je aanvraag?</h3>
      <ol style="padding-left:1.2rem;margin:0"><li>We nemen binnen 1 werkdag contact op.</li><li>We plannen een kennismaking van 30 minuten.</li><li>Je ontvangt binnen 2 werkdagen een voorstel met vaste prijs.</li></ol></div>
  </aside>
</div></section>'''
    title = "Contact: plan een gratis kennismaking | Made for More"
    desc = "Neem contact op met Made for More voor een nieuwe website, logo, SEO of GEO. Plan een vrijblijvende kennismaking van 30 minuten. Reactie binnen 1 werkdag."
    render("/contact/", title, desc, body, active=None,
           ld=[webpage_ld("/contact/", title, desc, "ContactPage"), breadcrumb_ld(crumbs)])


def build_bedankt():
    body = f'''<section class="section notfound"><div class="container container--narrow">
<p class="eyebrow" style="justify-content:center">Aanvraag ontvangen</p>
<h1>Bedankt! We nemen binnen 1 werkdag contact op.</h1>
<p class="lead">Je ontvangt een bevestiging per e-mail. Kun je niet wachten? Lees alvast in onze kennisbank hoe je in AI-zoekmachines gevonden wordt.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--accent" href="/kennisbank/wat-is-geo/">Lees over GEO {ARROW}</a><a class="btn btn--ghost" href="/">Terug naar home</a></div>
</div></section>'''
    render("/bedankt/", "Bedankt voor je aanvraag | Made for More", "Je aanvraag is ontvangen. We nemen binnen 1 werkdag contact met je op.", body, robots="noindex, follow")


def build_404():
    body = f'''<section class="section notfound"><div class="container container--narrow">
<p class="notfound__code" aria-hidden="true">4<span>+</span>4</p>
<h1 style="font-size:var(--fs-2xl)">Deze pagina bestaat (nog) niet.</h1>
<p class="lead">Misschien is de link verouderd of zit er een typfout in. Geen zorgen — hier vind je de weg terug.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--accent" href="/">Naar de homepage {ARROW}</a><a class="btn btn--ghost" href="/contact/">Contact opnemen</a></div>
</div></section>'''
    render("/404.html", "Pagina niet gevonden | Made for More", "Deze pagina bestaat niet. Ga terug naar de homepage van Made for More.", body,
           robots="noindex, follow", outfile=os.path.join(OUT, "404.html"))


def build_privacy():
    crumbs = [("/", "Home"), ("/privacy/", "Privacyverklaring")]
    body = page_hero(crumbs, "Privacy", "Privacyverklaring", f"Laatst bijgewerkt: 11 oktober 2026. Made for More respecteert je privacy en gaat zorgvuldig om met je persoonsgegevens, in lijn met de AVG.")
    body += f'''<section class="section"><div class="container container--narrow prose">
<!-- TODO: laat deze verklaring controleren en vul KvK-nummer en vestigingsadres in. -->
<h2>Wie zijn wij?</h2>
<p>Made for More is verantwoordelijk voor de verwerking van persoonsgegevens zoals beschreven in deze verklaring. Je kunt ons bereiken via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Welke gegevens verwerken we?</h2>
<p>Als je het contactformulier invult of ons mailt, verwerken we de gegevens die je zelf verstrekt: je naam, bedrijfsnaam, e-mailadres, telefoonnummer en de inhoud van je bericht.</p>
<h2>Waarom verwerken we deze gegevens?</h2>
<ul><li>Om contact met je op te nemen over je aanvraag;</li><li>Om een offerte of voorstel te maken;</li><li>Om onze diensten uit te voeren als je klant wordt.</li></ul>
<p>De grondslag is het uitvoeren van (de voorbereiding van) een overeenkomst of ons gerechtvaardigd belang om op je vraag te reageren.</p>
<h2>Hoe lang bewaren we gegevens?</h2>
<p>Aanvragen die niet tot een opdracht leiden, verwijderen we uiterlijk 12 maanden na het laatste contact. Klantgegevens bewaren we zolang dat nodig is voor de opdracht en de wettelijke (fiscale) bewaarplicht van 7 jaar.</p>
<h2>Cookies en statistieken</h2>
<p>Deze website gebruikt geen tracking- of advertentiecookies. Voor statistieken gebruiken we een privacyvriendelijke, cookieloze oplossing die geen persoonsgegevens opslaat.</p>
<h2>Delen met derden</h2>
<p>We verkopen je gegevens nooit. We delen ze alleen met partijen die nodig zijn voor onze dienstverlening (zoals onze hostingpartij en e-mailprovider), waarmee we verwerkersafspraken hebben.</p>
<h2>Jouw rechten</h2>
<p>Je hebt het recht om je gegevens in te zien, te corrigeren of te laten verwijderen. Stuur hiervoor een e-mail naar <a href="mailto:{EMAIL}">{EMAIL}</a>. Je hebt ook het recht een klacht in te dienen bij de Autoriteit Persoonsgegevens.</p>
</div></section>'''
    title = "Privacyverklaring | Made for More"
    desc = "Lees hoe Made for More omgaat met je persoonsgegevens, cookies en je rechten volgens de AVG."
    render("/privacy/", title, desc, body, ld=[webpage_ld("/privacy/", title, desc), breadcrumb_ld(crumbs)])


# ---------------------------------------------------------------- kennisbank
ARTICLES = [
    {
        "slug": "wat-is-geo",
        "title": "Wat is GEO? Gevonden worden in ChatGPT en AI",
        "h1": "Wat is GEO? Zo word je gevonden in ChatGPT en andere AI-zoekmachines",
        "desc": "GEO zorgt dat ChatGPT, Perplexity en Google AI Overviews je bedrijf noemen. Heldere uitleg, het verschil met SEO en een praktische checklist.",
        "lead": "Steeds meer mensen vragen ChatGPT om een aanbeveling in plaats van te googelen. Hoe zorg je dat jouw bedrijf in dat antwoord staat? Dat heet GEO.",
        "date": "2026-10-11",
        "read": "7 min",
        "tldr": ["GEO staat voor Generative Engine Optimization: je online aanwezigheid zo inrichten dat AI-zoekmachines je begrijpen, vertrouwen en noemen.",
                 "GEO vervangt SEO niet, maar bouwt erop voort. Een technisch goede, vindbare website is de basis.",
                 "De belangrijkste pijlers: duidelijke en citeerbare content, gestructureerde data, consistente bedrijfsgegevens en externe autoriteit."],
        "body": f'''
<h2 id="definitie">Wat is GEO?</h2>
<p><strong>GEO (Generative Engine Optimization) is het optimaliseren van je website en online aanwezigheid zodat generatieve AI-zoekmachines — zoals ChatGPT, Perplexity, Google Gemini, Microsoft Copilot en Google AI Overviews — jouw bedrijf begrijpen, als betrouwbaar beoordelen en noemen of citeren in hun antwoorden.</strong></p>
<p>Waar klassieke SEO draait om een hoge positie in een lijst met tien blauwe links, draait GEO om iets anders: <em>genoemd worden in het antwoord zelf</em>. Een AI-assistent noemt vaak maar een paar bedrijven of bronnen. Sta je daar niet bij, dan besta je voor die zoeker niet.</p>
<p>De term werd in 2023 geïntroduceerd door onderzoekers van onder meer Princeton University in het paper <a href="https://arxiv.org/abs/2311.09735" rel="noopener" target="_blank">“GEO: Generative Engine Optimization”</a>. Zij lieten zien dat aanpassingen aan content — zoals het toevoegen van bronvermeldingen, citaten en statistieken — de zichtbaarheid van een bron in AI-antwoorden aanzienlijk kunnen verhogen.</p>

<h2 id="verschil">Wat is het verschil tussen SEO en GEO?</h2>
<table>
<thead><tr><th scope="col"></th><th scope="col">SEO</th><th scope="col">GEO</th></tr></thead>
<tbody>
<tr><th scope="row">Doel</th><td>Hoog ranken in zoekresultaten</td><td>Genoemd en geciteerd worden in AI-antwoorden</td></tr>
<tr><th scope="row">Waar</th><td>Google, Bing</td><td>ChatGPT, Perplexity, Gemini, Copilot, Google AI Overviews</td></tr>
<tr><th scope="row">Succes meten</th><td>Posities, klikken, verkeer</td><td>Vermeldingen, citaties, verwijzend verkeer uit AI-tools</td></tr>
<tr><th scope="row">Focus</th><td>Zoekwoorden, techniek, backlinks</td><td>Duidelijkheid, feiten, structuur, autoriteit en consistentie</td></tr>
</tbody>
</table>
<p>Belangrijk: <strong>GEO is geen vervanging van SEO</strong>. Veel AI-zoekmachines halen hun informatie (deels) uit zoekindexen. Een website die technisch goed in elkaar zit en goed vindbaar is, heeft dus ook een voorsprong in AI-antwoorden.</p>

<h2 id="werking">Hoe kiezen AI-zoekmachines welke bedrijven ze noemen?</h2>
<p>Precieze algoritmes zijn niet openbaar, maar de signalen die ertoe doen zijn grotendeels bekend:</p>
<ol>
<li><strong>Begrijpelijkheid</strong> — kan een AI-model snel en zonder twijfel opmaken wat je doet, voor wie en waar?</li>
<li><strong>Citeerbaarheid</strong> — staan er heldere, zelfstandige zinnen op je site die een model letterlijk kan overnemen als antwoord?</li>
<li><strong>Betrouwbaarheid</strong> — word je ook elders genoemd (reviews, branchesites, nieuws, bedrijvengidsen), en kloppen die gegevens met elkaar?</li>
<li><strong>Actualiteit</strong> — is je informatie recent en wordt je site onderhouden?</li>
<li><strong>Toegankelijkheid</strong> — mogen AI-crawlers je site lezen, en laadt de inhoud zonder ingewikkelde scripts?</li>
</ol>

<h2 id="checklist">GEO-checklist: 10 dingen die je vandaag kunt doen</h2>
<ol>
<li><strong>Schrijf één heldere bedrijfsomschrijving</strong> van 1–2 zinnen (wie, wat, voor wie, waar) en gebruik die overal consistent: website, LinkedIn, Google Bedrijfsprofiel en bedrijvengidsen.</li>
<li><strong>Beantwoord echte klantvragen</strong> op je site, met de vraag als kop en het antwoord direct in de eerste zin.</li>
<li><strong>Voeg gestructureerde data toe</strong> (schema.org): Organization, LocalBusiness of ProfessionalService, Service, FAQPage en Article.</li>
<li><strong>Gebruik concrete feiten</strong>: prijzen, doorlooptijden, aantallen, werkgebied. Vage marketingtaal wordt zelden geciteerd.</li>
<li><strong>Verwijs naar betrouwbare bronnen</strong> en noem cijfers mét bron.</li>
<li><strong>Laat zien wie erachter zit</strong>: een over-ons-pagina met namen, ervaring en expertise (E-E-A-T).</li>
<li><strong>Sta AI-crawlers toe</strong> in je robots.txt (zoals GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot en Google-Extended), tenzij je daar bewust niet voor kiest.</li>
<li><strong>Overweeg een llms.txt-bestand</strong>: een korte, leesbare samenvatting van je site voor taalmodellen. Het is (nog) geen officiële standaard, maar wel eenvoudig en kosteloos.</li>
<li><strong>Verzamel reviews</strong> op Google en relevante platforms. AI-modellen gebruiken die als vertrouwenssignaal.</li>
<li><strong>Zorg voor een snelle, goed gestructureerde site</strong> met één H1 per pagina, logische koppen en tekst die zonder JavaScript leesbaar is.</li>
</ol>

<h2 id="meten">Hoe meet je of GEO werkt?</h2>
<p>GEO is lastiger te meten dan SEO, maar niet onmogelijk:</p>
<ul>
<li>Stel maandelijks dezelfde vragen aan ChatGPT, Perplexity en Gemini (bijvoorbeeld: “welke webdesigner in [stad] raad je aan?”) en noteer of je genoemd wordt.</li>
<li>Bekijk in je statistieken het verwijzende verkeer van domeinen als chatgpt.com en perplexity.ai.</li>
<li>Houd in Google Search Console bij voor welke vragen je verschijnt in AI Overviews.</li>
</ul>

<h2 id="conclusie">Conclusie</h2>
<p>GEO is geen hype, maar de logische volgende stap in vindbaarheid. De basis is gelukkig hetzelfde als altijd: een snelle, duidelijke en betrouwbare website die echte vragen van je klanten beantwoordt. Wie dat goed doet, wordt gevonden — door mensen, door Google én door AI.</p>
<blockquote><p><strong>Wil je weten hoe jouw bedrijf er nu voor staat in AI-zoekmachines?</strong> Tijdens een gratis kennismaking checken we het samen. <a href="/contact/">Plan een gesprek</a>.</p></blockquote>
''',
        "faqs": [
            ("Wat betekent GEO?", "GEO staat voor Generative Engine Optimization: het optimaliseren van je website en online aanwezigheid zodat AI-zoekmachines zoals ChatGPT, Perplexity en Google AI Overviews je bedrijf noemen in hun antwoorden."),
            ("Is GEO hetzelfde als SEO?", "Nee. SEO richt zich op een hoge positie in zoekresultaten, GEO op vermeldingen in AI-antwoorden. Ze versterken elkaar: een goede SEO-basis helpt ook bij GEO."),
            ("Heeft een klein bedrijf GEO nodig?", "Ja, juist lokale ondernemers en dienstverleners profiteren, omdat mensen AI-assistenten steeds vaker om concrete aanbevelingen vragen, zoals een goede webdesigner of installateur in de buurt."),
        ],
    },
    {
        "slug": "wat-kost-een-website",
        "title": "Wat kost een website laten maken in 2026?",
        "h1": "Wat kost een website laten maken in 2026?",
        "desc": "Wat kost een professionele website in 2026? Overzicht van prijzen voor websitebouwers, freelancers en bureaus, wat de prijs bepaalt en waar je op moet letten.",
        "lead": "Van een paar tientjes per maand tot tienduizenden euro's: de prijzen voor een website lopen enorm uiteen. In dit artikel leggen we uit waar dat verschil vandaan komt en wat je realistisch kunt verwachten.",
        "date": "2026-10-11",
        "read": "6 min",
        "tldr": ["Een professionele bedrijfswebsite laten maken kost in Nederland doorgaans tussen €1.500 en €6.000 (excl. btw).",
                 "Het aantal pagina's, teksten, maatwerk-functies, merkidentiteit en SEO/GEO bepalen het grootste deel van de prijs.",
                 "Reken daarnaast op terugkerende kosten voor hosting, domein en onderhoud: vaak €15 tot €100 per maand."],
        "body": '''
<h2 id="kort">Het korte antwoord</h2>
<p><strong>Een professionele bedrijfswebsite laten maken kost in Nederland in 2026 doorgaans tussen de €1.500 en €6.000 exclusief btw. Een eenvoudige website zelf maken met een websitebouwer kan al vanaf zo'n €15 tot €40 per maand, terwijl uitgebreide maatwerkwebsites en webshops al snel boven de €10.000 uitkomen.</strong></p>
<p>Deze bedragen zijn een indicatie op basis van gangbare marktprijzen. De echte prijs hangt af van wat je nodig hebt — en van wat je website moet opleveren.</p>

<h2 id="overzicht">Prijsoverzicht per type aanbieder</h2>
<table>
<thead><tr><th scope="col">Optie</th><th scope="col">Indicatie</th><th scope="col">Geschikt voor</th></tr></thead>
<tbody>
<tr><td>Zelf bouwen (Wix, Squarespace e.d.)</td><td>€15–€40 per maand</td><td>Hobby, testfase, zeer kleine budgetten</td></tr>
<tr><td>Freelancer met template</td><td>€500–€1.500</td><td>Eenvoudige site zonder strategie of teksten</td></tr>
<tr><td>Webdesignbureau (mkb)</td><td>€1.500–€6.000</td><td>Professionele bedrijfswebsite met strategie, design, SEO</td></tr>
<tr><td>Groot bureau / maatwerk</td><td>€10.000+</td><td>Complexe platformen, webshops, koppelingen</td></tr>
</tbody>
</table>

<h2 id="factoren">Wat bepaalt de prijs van een website?</h2>
<ol>
<li><strong>Aantal pagina's en structuur</strong> — een site van 5 pagina's is minder werk dan een site met 30 diensten- en locatiepagina's.</li>
<li><strong>Ontwerp: template of maatwerk</strong> — een uniek ontwerp kost meer, maar laat je wel onderscheiden van de concurrent.</li>
<li><strong>Teksten</strong> — zelf schrijven of laten schrijven? Goede webteksten zijn vaak de grootste factor voor conversie én vindbaarheid.</li>
<li><strong>Merkidentiteit</strong> — heb je al een logo en huisstijl, of moet die nog ontwikkeld worden?</li>
<li><strong>Functionaliteit</strong> — online boeken, betalen, een klantportaal of koppelingen met je boekhouding of CRM.</li>
<li><strong>SEO en GEO</strong> — zoekwoordonderzoek, technische optimalisatie en vindbaarheid in AI-zoekmachines.</li>
<li><strong>Beheer</strong> — wil je zelf content aanpassen via een beheersysteem?</li>
</ol>

<h2 id="terugkerend">Welke terugkerende kosten moet je verwachten?</h2>
<ul>
<li><strong>Domeinnaam</strong>: meestal €10–€15 per jaar voor een .nl-domein.</li>
<li><strong>Hosting</strong>: €5–€30 per maand, afhankelijk van snelheid en service.</li>
<li><strong>Onderhoud en updates</strong>: €25–€100 per maand voor beveiliging, back-ups en kleine aanpassingen.</li>
<li><strong>Content en SEO</strong> (optioneel): vanaf zo'n €150 per maand als je actief wilt groeien met nieuwe artikelen.</li>
</ul>

<h2 id="goedkoop">Is een goedkope website een goed idee?</h2>
<p>Een goedkope website is niet per se slecht, maar let op de verborgen kosten. Een site die traag laadt, niet gevonden wordt of geen vertrouwen wekt, kost je ongemerkt klanten. Stel jezelf daarom de vraag: <em>wat levert één nieuwe klant mij op?</em> Als dat een paar honderd euro of meer is, verdient een professionele website zich vaak snel terug.</p>

<h2 id="vragen">5 vragen om aan elke webdesigner te stellen</h2>
<ol>
<li>Is de prijs vast, en wat valt er precies onder?</li>
<li>Word ik eigenaar van de website en de domeinnaam?</li>
<li>Hoe zorgen jullie voor vindbaarheid in Google én AI-zoekmachines?</li>
<li>Wat kost onderhoud na de lancering, en ben ik daaraan verplicht?</li>
<li>Kan ik zelf teksten en foto's aanpassen?</li>
</ol>

<h2 id="made-for-more">Wat kost een website bij Made for More?</h2>
<p>Bij Made for More werk je altijd met een vaste prijs. Het <strong>Start-pakket kost €1.495</strong>, het <strong>Groei-pakket €2.950</strong> (inclusief teksten en uitgebreide SEO en GEO) en <strong>maatwerk begint bij €5.500</strong>. Alle prijzen zijn exclusief btw. Onderhoud is optioneel en kost vanaf €39 per maand. <a href="/prijzen/">Bekijk alle pakketten</a>.</p>
''',
        "faqs": [
            ("Wat kost een simpele website?", "Een simpele, professioneel gemaakte website van ongeveer 5 pagina's kost bij een webdesignbureau doorgaans tussen €1.000 en €2.000 exclusief btw. Zelf bouwen met een websitebouwer kan vanaf ongeveer €15 per maand."),
            ("Wat kost het onderhoud van een website per maand?", "Reken op €25 tot €100 per maand voor hosting, updates, back-ups en kleine aanpassingen, afhankelijk van de service en de grootte van je website."),
            ("Is een website aftrekbaar voor de belasting?", "Een website is voor ondernemers een zakelijke kostenpost. Afhankelijk van het bedrag en je situatie wordt deze als kosten of als investering afgeschreven. Vraag je boekhouder naar jouw situatie."),
        ],
    },
]


def build_articles():
    for a in ARTICLES:
        path = f"/kennisbank/{a['slug']}/"
        crumbs = [("/", "Home"), ("/kennisbank/", "Kennisbank"), (path, a["h1"])]
        import re
        toc_items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a["body"])
        toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc_items)
        tldr = "".join(f"<li>{t}</li>" for t in a["tldr"])
        date_nl = "11 oktober 2026"
        body = f'''<article>
<section class="page-hero"><div class="container container--narrow">
  {crumbs_html(crumbs)}
  <p class="eyebrow">Kennisbank</p>
  <h1 style="max-width:none">{a["h1"]}</h1>
  <p>{a["lead"]}</p>
  <div class="article-meta"><span>Door <a href="/over-ons/">Made for More</a></span><span>Gepubliceerd op <time datetime="{a["date"]}">{date_nl}</time></span><span>Leestijd: {a["read"]}</span></div>
</div></section>
<section class="section"><div class="container container--narrow">
  <div class="tldr"><strong>In het kort</strong><ul>{tldr}</ul></div>
  <nav class="toc" aria-label="Inhoudsopgave"><strong>Inhoud</strong><ol>{toc}</ol></nav>
  <div class="prose">{a["body"]}
  <h2 id="faq">Veelgestelde vragen</h2></div>
  {faq_html(a["faqs"])}
</div></section>
</article>
{cta_band()}'''
        art_ld = {
            "@type": "BlogPosting",
            "@id": f"{SITE}{path}#artikel",
            "headline": a["h1"],
            "description": a["desc"],
            "image": f"{SITE}/assets/img/og-image.png",
            "datePublished": a["date"],
            "dateModified": a["date"],
            "inLanguage": "nl-NL",
            "author": {"@id": ORG_ID},
            "publisher": {"@id": ORG_ID},
            "mainEntityOfPage": f"{SITE}{path}",
            "isPartOf": {"@id": WEBSITE_ID},
        }
        render(path, f"{a['title']} | Made for More", a["desc"], body, active="/kennisbank/", og_type="article",
               ld=[art_ld, breadcrumb_ld(crumbs), faq_ld(a["faqs"])])

    crumbs = [("/", "Home"), ("/kennisbank/", "Kennisbank")]
    cards = "".join(
        f'<article class="card card--link post-card reveal" data-delay="{i*80}"><time datetime="{a["date"]}">11 oktober 2026 · {a["read"]}</time><h2 style="margin-top:var(--space-3)"><a href="/kennisbank/{a["slug"]}/" style="color:inherit;text-decoration:none">{a["h1"]}</a></h2><p>{a["lead"]}</p><div class="card__meta"><span class="link-arrow">Lees artikel {ARROW}</span></div></article>'
        for i, a in enumerate(ARTICLES))
    body = page_hero(crumbs, "Kennisbank", "Kennis over websites, SEO en GEO.",
                     "Praktische artikelen voor ondernemers die meer willen halen uit hun website. Zonder vakjargon, met direct toepasbare tips.")
    body += f'<section class="section"><div class="container"><div class="grid grid--2">{cards}</div></div></section>' + cta_band()
    blog_ld = {
        "@type": "Blog",
        "@id": f"{SITE}/kennisbank/#blog",
        "name": "Kennisbank Made for More",
        "url": f"{SITE}/kennisbank/",
        "inLanguage": "nl-NL",
        "publisher": {"@id": ORG_ID},
        "blogPost": [{"@id": f"{SITE}/kennisbank/{a['slug']}/#artikel"} for a in ARTICLES],
    }
    title = "Kennisbank: websites, SEO & GEO uitgelegd | Made for More"
    desc = "Praktische kennis over websites, SEO en GEO voor ondernemers. Lees wat een website kost en hoe je gevonden wordt in ChatGPT en Google."
    render("/kennisbank/", title, desc, body, active="/kennisbank/",
           ld=[webpage_ld("/kennisbank/", title, desc, "CollectionPage"), breadcrumb_ld(crumbs), blog_ld])


def build_sitemap():
    urls = [("/", "1.0"), ("/diensten/", "0.9"), ("/prijzen/", "0.9"), ("/werkwijze/", "0.7"),
            ("/over-ons/", "0.6"), ("/contact/", "0.8"), ("/kennisbank/", "0.7")]
    urls += [(f"/kennisbank/{a['slug']}/", "0.7") for a in ARTICLES]
    urls += [("/privacy/", "0.2")]
    body = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n')


build_home()
build_diensten()
build_werkwijze()
build_prijzen()
build_over()
build_contact()
build_bedankt()
build_privacy()
build_articles()
build_404()
build_sitemap()
print("klaar")
