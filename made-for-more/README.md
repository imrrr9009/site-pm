# Made for More: website

One-page website van **Made for More**, bureau voor influencer sponsorships.

> Zelfstandig project, volledig los van de Project Masters lichtplan-site.
> De eerdere webdesign-versie van deze site staat in de git-geschiedenis (commit `a4de1f5`).

## Structuur

```
made-for-more/
├── site/                 ← dit is de website (deze map publiceer je)
│   ├── index.html        De hele site: tekst, opmaak en contact in één bestand
│   ├── assets/fonts/     Lettertypes (zelf gehost)
│   ├── assets/img/       Logo's, iconen, deelbeeld (og-image.png)
│   ├── favicon.svg, site.webmanifest
│   ├── robots.txt, sitemap.xml, llms.txt
│   └── netlify.toml
└── docs/
    ├── MERKGIDS.md
    └── STAPPENPLAN-LIVEGANG.md
```

## Contactgegevens invullen

In `site/index.html` staan invulplekken tussen blokhaken: `[Jouw naam]`, `[jouw@email.nl]`, `[telefoonnummer]`, `[nummer]` (WhatsApp, internationaal zonder + of 0, bijv. `31612345678`), `[gebruikersnaam]` (Instagram), `KvK [nummer]` en `[plaats]`. Zoek op `[` om ze allemaal te vinden. Vergeet ook de letter in het rondje bij je naam niet (`person__avatar`).

## Lokaal bekijken

```bash
cd made-for-more/site
python3 -m http.server 8000
# open http://localhost:8000
```

## Publiceren

Sleep de map `site/` naar Netlify (*Deploy manually*) of een andere host. Het volledige stappenplan staat in `docs/STAPPENPLAN-LIVEGANG.md`. Controleer of `madeformore.nl` het juiste domein is. Anders pas je het aan in `index.html` (canonical, og:url, og:image, JSON-LD), `robots.txt`, `sitemap.xml`, `llms.txt` en `netlify.toml`.

## Gemeten (Google Lighthouse 12.6, lokaal, 22 oktober 2026)

| | Prestaties | Toegankelijkheid | Best practices | SEO |
|---|---|---|---|---|
| Mobiel | 99 | 100 | 100 | 100 |
| Desktop | 100 | 100 | 100 | 100 |

Meet na livegang opnieuw met [PageSpeed Insights](https://pagespeed.web.dev/).
