# Made for More: website

One-page website for **Made for More**, an influencer sponsorship agency. English is the main language; a Dutch version lives at `/nl/`.

> Standalone project, completely separate from the Project Masters lighting-plan site.
> The earlier web design version of this site is in the git history (commit `a4de1f5`).

## Structure

```
made-for-more/
├── site/                 ← the website (this is the folder you publish)
│   ├── index.html        English page (main language): copy, styling and contact in one file
│   ├── nl/index.html     Dutch page, same layout
│   ├── assets/fonts/     Fonts (self-hosted)
│   ├── assets/img/       Logos, icons, social share image (og-image.png)
│   ├── favicon.svg, site.webmanifest
│   ├── robots.txt, sitemap.xml, llms.txt
│   └── netlify.toml
└── docs/
    ├── BRAND-GUIDE.md
    └── GO-LIVE-GUIDE.md
```

## Contact details

Both pages show the same details:

- **Name:** Imran El Mayouri (Founder / Oprichter)
- **Email:** madeformorebureau@outlook.com
- **Phone and WhatsApp:** +31 6 44767638

The pages are two separate files (`site/index.html` and `site/nl/index.html`). When you change the layout or contact details, change both. The EN | NL switch in the header links the two pages, and both pages tell search engines about each other with `hreflang` tags (also listed in `sitemap.xml`).

Once registered with the Dutch Chamber of Commerce, add your **KvK number** to the footer of both pages: Dutch law requires it on a business website.

## Preview locally

```bash
cd made-for-more/site
python3 -m http.server 8000
# open http://localhost:8000
```

## Publishing

Drag the `site/` folder into Netlify (*Deploy manually*) or upload it to any other host. The full step-by-step plan is in `docs/GO-LIVE-GUIDE.md`. The domain is **`www.madeformore.com`** (the bare `madeformore.com` redirects to www via `netlify.toml`). To change it, update it in `index.html` and `nl/index.html` (canonical, hreflang, og:url, og:image, JSON-LD), `robots.txt`, `sitemap.xml`, `llms.txt` and `netlify.toml`.

## Measured (Google Lighthouse 12.6, local, 22 October 2026)

| | Performance | Accessibility | Best practices | SEO |
|---|---|---|---|---|
| Mobile (EN / NL) | 99 / 100 | 100 | 100 | 100 |
| Desktop (EN / NL) | 100 | 100 | 100 | 100 |

Measure again after going live with [PageSpeed Insights](https://pagespeed.web.dev/).
