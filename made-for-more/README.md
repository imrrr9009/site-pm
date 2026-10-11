# Made for More — website

Website van **Made for More**, webdesign, merkidentiteit en vindbaarheid (SEO & GEO) voor ondernemers.

> Dit is een **zelfstandig project**, volledig los van de Project Masters lichtplan-site. Er worden geen bestanden gedeeld. De map `made-for-more/` kan in zijn geheel naar een eigen repository worden verplaatst.

## Structuur

```
made-for-more/
├── site/                  ← dit is de website (deze map publiceer je)
│   ├── index.html         Home
│   ├── diensten/          Diensten (webdesign, merk, SEO, GEO, teksten, onderhoud)
│   ├── werkwijze/         Stappenplan
│   ├── prijzen/           Pakketten, abonnementen, extra's
│   ├── over-ons/          Verhaal, waarden, belofte
│   ├── contact/           Contactformulier
│   ├── kennisbank/        Blog + 2 artikelen (GEO, websiteprijzen)
│   ├── privacy/ bedankt/ 404.html
│   ├── assets/css|js|img  Stijl, scripts, logo's, OG-afbeelding, iconen
│   ├── robots.txt         AI-crawlers expliciet toegestaan
│   ├── sitemap.xml
│   ├── llms.txt           Samenvatting voor AI-modellen (GEO)
│   ├── site.webmanifest
│   └── netlify.toml       Headers, caching, redirect
├── tools/build.py         Genereert alle HTML-pagina's (header/footer/schema op één plek)
└── docs/
    ├── BEDRIJFSPLAN.md    Advies & groeiplan voor Made for More
    └── MERKGIDS.md        Logo, kleuren, typografie, tone of voice
```

Geen framework, geen build-stap nodig om te publiceren: pure HTML/CSS en ~3 kB JavaScript. Dat is de snelste en meest crawlbare basis voor SEO en GEO.

## Lokaal bekijken

```bash
cd made-for-more/site
python3 -m http.server 8000
# open http://localhost:8000
```

## Teksten of pagina's aanpassen

Alle inhoud staat in `tools/build.py`. Pas daar de tekst aan en genereer opnieuw:

```bash
python3 made-for-more/tools/build.py
```

Zo blijven header, footer, menu, sitemap en schema.org-gegevens op alle pagina's gelijk. (Je kunt de HTML-bestanden ook direct bewerken, maar dan worden je wijzigingen bij een volgende build overschreven.)

## Publiceren

**Aanbevolen: Netlify** (gratis voor deze omvang)
1. Maak een account op netlify.com → *Add new site* → koppel deze repository, of sleep de map `site/` in het venster.
2. Publish directory: `made-for-more/site` (bij koppelen aan de repo).
3. Het contactformulier werkt direct via **Netlify Forms**. Stel onder *Forms → Notifications* in dat aanvragen naar je e-mail gaan.
4. Koppel je domein onder *Domain management*. HTTPS gaat automatisch.

Andere hosts (Cloudflare Pages, Vercel, GitHub Pages) werken ook. Het formulier heeft daar wel een dienst als Formspree nodig: vervang dan de `action` van het formulier in `build.py`.

## Checklist vóór livegang

- [ ] **Domeinnaam** registreren (`madeformore.nl` is aangenomen, controleer of hij vrij is). Ander domein? Vervang `SITE` in `tools/build.py` en het domein in `robots.txt`, `llms.txt` en `netlify.toml`.
- [ ] **E-mailadres** `info@madeformore.nl` aanmaken, of `EMAIL` in `build.py` aanpassen.
- [ ] **Prijzen** controleren in `build.py` (`PACKAGES`, abonnementen, extra's) en `llms.txt`.
- [ ] **Over ons**: persoonlijke foto, naam en achtergrond van de oprichter toevoegen (zie TODO in de pagina). Dit is belangrijk voor vertrouwen én E-E-A-T.
- [ ] **Privacyverklaring** laten controleren en KvK-nummer en adres invullen.
- [ ] **Footer**: KvK-nummer en btw-id toevoegen zodra je ingeschreven bent (wettelijk verplicht op een zakelijke website).
- [ ] **Schema.org** (`ORG` in `build.py`): `telephone`, `address`, `vatID` en `sameAs` (LinkedIn, Instagram, Google Bedrijfsprofiel) toevoegen.
- [ ] **Google Search Console** en **Bing Webmaster Tools**: site verifiëren en `sitemap.xml` indienen. Bing is belangrijk voor GEO, omdat ChatGPT Search mede op Bing leunt.
- [ ] **Statistieken**: een cookieloze tool kiezen (bijv. Plausible, Umami of Simple Analytics) en het script toevoegen. Dan is geen cookiebanner nodig.
- [ ] **Google Bedrijfsprofiel** aanmaken.
- [ ] Testen met PageSpeed Insights, de Rich Results Test en de Schema Markup Validator.

## Wat er aan SEO & GEO is ingebouwd

| Onderdeel | Waar |
|---|---|
| Unieke `<title>` (≤ 60 tekens) en meta-description (≤ 160) per pagina | alle pagina's |
| Eén H1 per pagina, logische kopstructuur, kruimelpaden | alle pagina's |
| Canonical, `hreflang="nl-NL"`, Open Graph + Twitter Card, OG-afbeelding | `<head>` |
| JSON-LD `@graph`: Organization/ProfessionalService, WebSite, WebPage, BreadcrumbList, Service, OfferCatalog, HowTo, FAQPage, Blog, BlogPosting | per pagina |
| Citeerbare definities, "In het kort"-blokken, vraag-als-kop, feiten met bron | home, kennisbank |
| `robots.txt` met AI-crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended…) | `site/robots.txt` |
| `llms.txt` met feitelijke bedrijfssamenvatting | `site/llms.txt` |
| XML-sitemap met `lastmod` | `site/sitemap.xml` |
| Snel: geen framework, `defer`-script, font-preconnect, geen layout shift | overal |
| Toegankelijk: skip-link, zichtbare focus, labels, aria, contrast ≥ 4,5:1, `prefers-reduced-motion` | overal |

Eerlijke kanttekeningen: Google toont FAQ-rich-results sinds 2023 vrijwel alleen nog voor overheids- en zorgsites. De FAQ-markup helpt wel bij het begrip door zoekmachines en AI. `llms.txt` is een voorstel en nog geen officiële standaard. Het kost niets en kan geen kwaad.
