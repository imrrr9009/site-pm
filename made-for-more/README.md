# Made for More: website

One-page website for **Made for More**, an influencer sponsorship agency.

> Standalone project, completely separate from the Project Masters lighting-plan site.
> The earlier web design version of this site is in the git history (commit `a4de1f5`).

## Structure

```
made-for-more/
├── site/                 ← the website (this is the folder you publish)
│   ├── index.html        The whole site: copy, styling and contact in one file
│   ├── assets/fonts/     Fonts (self-hosted)
│   ├── assets/img/       Logos, icons, social share image (og-image.png)
│   ├── favicon.svg, site.webmanifest
│   ├── robots.txt, sitemap.xml, llms.txt
│   └── netlify.toml
└── docs/
    ├── BRAND-GUIDE.md
    └── GO-LIVE-GUIDE.md
```

## Filling in your contact details

`site/index.html` contains placeholders in square brackets: `[Your name]`, `[you@email.com]`, `[phone number]`, `[number]` (WhatsApp, international format without + or leading 0, e.g. `31612345678`), `[username]` (Instagram), `KvK [number]` and `[city]`. Search for `[` to find them all. Also update the initial in the circle next to your name (`person__avatar`).

## Preview locally

```bash
cd made-for-more/site
python3 -m http.server 8000
# open http://localhost:8000
```

## Publishing

Drag the `site/` folder into Netlify (*Deploy manually*) or upload it to any other host. The full step-by-step plan is in `docs/GO-LIVE-GUIDE.md`. Check that `madeformore.nl` is the right domain. If not, update it in `index.html` (canonical, og:url, og:image, JSON-LD), `robots.txt`, `sitemap.xml`, `llms.txt` and `netlify.toml`.

## Measured (Google Lighthouse 12.6, local, 22 October 2026)

| | Performance | Accessibility | Best practices | SEO |
|---|---|---|---|---|
| Mobile | 99 | 100 | 100 | 100 |
| Desktop | 100 | 100 | 100 | 100 |

Measure again after going live with [PageSpeed Insights](https://pagespeed.web.dev/).
