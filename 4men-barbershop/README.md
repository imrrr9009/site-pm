# 4MEN Barbershop: one-pager (demo)

Nieuwe one-pager voor 4MEN Barbershop, Goudsesingel 101 in Rotterdam. Eén statisch bestand
(`index.html`) met inline CSS en een klein script; geen build-stap. Publiceer deze map als
website-root (dan klopt `og:image` op `/img/og.jpg`).

```
4men-barbershop/
├── index.html   pagina (NL), JSON-LD HairSalon, inline CSS/JS
├── img/         foto's als WebP + og.jpg
└── fonts/       Cormorant + Montserrat (self-hosted, OFL)
```

Ontwerp: donker met goud, Cormorant voor koppen en Montserrat voor tekst, gekozen met de
`ui-ux-pro-max`-skill in deze repo (design system "premium black + gold").

## Voor livegang

- Haal `<meta name="robots" content="noindex">` weg zodra de eigenaar akkoord is.
- Vervang de Treatwell-link (`https://www.treatwell.nl/en/place/4men-barbershop/`) door de exacte
  link van de "Book now"-knop op de huidige site (5× in `index.html`).
- Vraag de originele foto's in hogere resolutie (minstens 1600 px breed) en vervang die in `img/`.

## Open vragen voor de eigenaar ([TODO] in de pagina)

1. Prijzen per dienst (8×)
2. Sinds wanneer de zaak in Rotterdam zit
3. Drie reviews om te tonen (tekst + voornaam + bron)
4. Treatwell- en Google-score bijwerken vlak voor livegang
5. Wel of geen producten verkopen in de zaak
6. Eigen e-mailadres op het domein, bijvoorbeeld info@4menbarbershop.nl
