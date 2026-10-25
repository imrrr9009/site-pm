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

- Haal `<meta name="robots" content="noindex">` weg zodra de site op 4menbarbershop.nl komt.
- Controleer de prijzen op Treatwell (`https://www.treatwell.nl/salon/4men-barbershop/`): ze komen uit
  Treatwell-pagina's van verschillende datums. Tondeuse + baard en Hot towel scheerbeurt staan als
  "prijs via Treatwell" omdat er geen prijs voor te vinden was.
- Vraag de originele foto's in hogere resolutie (minstens 1600 px breed) en vervang die in `img/`.
- Optioneel: drie reviews om te tonen, sinds welk jaar de zaak in Rotterdam zit, producten in de zaak,
  een eigen e-mailadres op het domein.
