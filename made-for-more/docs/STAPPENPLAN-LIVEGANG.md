# Stappenplannen: een nieuwe HTML-website online zetten

Vier situaties:

- **0. Voorbereiding:** geldt altijd
- **A. Compleet nieuw bedrijf:** nog geen domein, geen hosting
- **B. Bedrijf heeft al hosting:** de nieuwe site komt op dezelfde server
- **C. Verhuizen:** van hoster A naar hoster B, met een nieuwe site

---

## 0. Voorbereiding (altijd)

1. **Site lokaal testen.** Klik door alle pagina's, test op je telefoon en controleer het formulier.
2. **Mapstructuur controleren.** `index.html` staat in de hoofdmap, en CSS, JS en afbeeldingen staan erbij in `assets/`.
3. **Domeinnaam in de bestanden goedzetten.** Dat gaat om canonical-links, `sitemap.xml`, `robots.txt` en `llms.txt`.
4. **Formulier regelen.** Een HTML-formulier verstuurt niets uit zichzelf. Kies één oplossing:
   - op Netlify: Netlify Forms (zit er al in)
   - op andere hosting: Formspree of Basin, of een PHP-script van de hoster
5. **Toegang verzamelen** en bewaren in een wachtwoordmanager (bijv. Bitwarden of 1Password):
   - registrar (waar het domein staat)
   - DNS-beheer
   - hosting en FTP
   - e-mail
   - Google-account
6. **Eigenaarschap vastleggen.** Domein en accounts staan op naam van **de klant**. Jij krijgt een eigen beheerdersaccount.

---

## A. Compleet nieuw bedrijf (nog niets geregeld)

Doorlooptijd: **1 dag** (meeste tijd gaat naar wachten op DNS).

| # | Stap | Wat je doet |
|---|---|---|
| 1 | **Domeinnaam kiezen en registreren** | Controleer of de naam vrij is en registreer hem bij een registrar (bijv. TransIP, Versio, Hostnet, Antagonist). Neem eventueel ook `.com` / `.be`. Registreer op naam van het bedrijf. ⏱ 5–15 min |
| 2 | **Soort hosting kiezen** | **Alleen HTML:** statische hosting zoals Netlify, Cloudflare Pages of Vercel. Snel, gratis tot een flinke omvang, SSL automatisch. **Later WordPress, PHP of een webshop nodig:** gedeelde hosting (bijv. Hostinger, TransIP, Antagonist). |
| 3 | **Zakelijke e-mail regelen** | Statische hosting heeft **geen e-mail**. Kies Google Workspace, Microsoft 365 of het mailpakket van je registrar. Maak eerst de mailboxen aan (bijv. info@). |
| 4 | **Website uploaden** | **Netlify:** map in *Deploy manually* slepen; na ±1 min live op `naam.netlify.app`. **Gedeelde hosting:** uploaden via de bestandsbeheerder of SFTP (bijv. met FileZilla) naar de webmap: `public_html`, `httpdocs` of `www`, afhankelijk van de hoster. |
| 5 | **Domein koppelen (DNS)** | Vul bij je registrar de DNS-records in die de hoster opgeeft. **Netlify:** A-record `@` → het IP dat Netlify toont, CNAME `www` → `naam.netlify.app`. Of zet de nameservers op Netlify. **Gedeelde hosting:** meestal automatisch als domein en hosting bij dezelfde partij staan. ⏱ 5 min – enkele uren |
| 6 | **E-mail-DNS instellen** | Vul de MX-records van je mailprovider in, plus **SPF**, **DKIM** en **DMARC**, anders komt je mail in de spam terecht. |
| 7 | **SSL / https aanzetten** | Gaat meestal automatisch (Let's Encrypt). Zet daarna **"HTTPS afdwingen"** aan. |
| 8 | **Kiezen: met of zonder www** | Kies er één en stuur de andere met een 301-redirect door. |
| 9 | **Eindcontrole** | Controleer: alle pagina's, mobiel, het formulier (stuur een testbericht), de 404-pagina, het slotje in de browser en de score in PageSpeed Insights. |
| 10 | **Aanmelden bij zoekmachines** | **Google Search Console:** domein verifiëren via een DNS TXT-record en `sitemap.xml` indienen. **Bing Webmaster Tools:** importeren vanuit Search Console. |
| 11 | **Lokale vindbaarheid** | Maak een Google Bedrijfsprofiel aan en zet de website erin. Gebruik overal precies dezelfde bedrijfsnaam, hetzelfde adres en telefoonnummer. |
| 12 | **Statistieken** | Voeg een cookieloze tool toe (bijv. Plausible of Umami). Dan is geen cookiebanner nodig. |

---

## B. Bedrijf heeft al hosting (nieuwe site op dezelfde server)

Doorlooptijd: **½–1 dag**. De site is maar enkele minuten offline als je het goed voorbereidt.

| # | Stap | Wat je doet |
|---|---|---|
| 1 | **Toegang krijgen** | Vraag de klant om de login van het hostingpaneel (cPanel, DirectAdmin of Plesk), FTP en DNS. Lukt dat niet? Laat de klant je toevoegen als gebruiker. |
| 2 | **Inventariseren wat er draait** | Is het een oude WordPress-site? Draait de **e-mail op dezelfde hosting**? Zijn er databases, subdomeinen of andere apps? **E-mail-instellingen laat je met rust.** |
| 3 | **Volledige back-up maken** | Download alle bestanden en exporteer de database(s). Maak ook een back-up via het hostingpaneel als dat kan. Bewaar die lokaal. |
| 4 | **Oude URL's vastleggen** | Maak een lijst van alle bestaande pagina's. Gebruik daarvoor Google Search Console (*Pagina's* → exporteren) of de gratis versie van Screaming Frog (tot 500 URL's). |
| 5 | **Redirects voorbereiden** | Koppel elke oude URL aan de best passende nieuwe pagina en zet ze als **301-redirect** in `.htaccess` (bij Apache of LiteSpeed), bijvoorbeeld:<br>`Redirect 301 /over-mij /over-ons/`<br>Zo behoud je je posities in Google en werken oude links nog. |
| 6 | **Eerst testen** | Zet de nieuwe site op een testadres, bijv. `test.bedrijf.nl` of een tijdelijke URL van de hoster, met `noindex`. Laat de klant goedkeuren. |
| 7 | **Rustig moment kiezen** | Bijvoorbeeld 's avonds of in het weekend. Laat de klant weten wanneer het gebeurt. |
| 8 | **Wisselen** | Verplaats de oude bestanden naar een back-upmap **buiten** de webmap, of maak er een zip van. Upload daarna de nieuwe bestanden naar de webmap. Let op: **verwijder `index.php`**, anders kan de server die vóór `index.html` laden. Laat de map `.well-known` staan (nodig voor SSL). |
| 9 | **404-pagina instellen** | Zet in `.htaccess`: `ErrorDocument 404 /404.html`. |
| 10 | **Caches legen** | Leeg de hostingcache en de CDN-cache (bijv. Cloudflare) en open de site in een privévenster. |
| 11 | **Controleren** | Loop dezelfde eindcontrole na als bij A9. Test daarnaast **de redirects** en **of e-mail nog werkt** (stuur en ontvang een testmail). |
| 12 | **Search Console** | Dien de nieuwe `sitemap.xml` in. Kijk de eerste 2–4 weken wekelijks naar 404-fouten en voeg zo nodig redirects toe. |
| 13 | **Opruimen** | Haal na 2–4 weken de oude back-upmap van de server. Bewaar wel een kopie lokaal. Was het WordPress? Verwijder dan ook de database, zodat er geen onveilige oude software blijft staan. |

---

## C. Verhuizen van hoster A naar hoster B (met nieuwe site)

Doorlooptijd: **1–3 dagen** voorbereiding, en het overschakelen zelf duurt een paar uur. Het grootste risico is **e-mail**: plan dat apart.

### Fase 1: Inventariseren (bij de oude partij)

| # | Stap | Wat je doet |
|---|---|---|
| 1 | **Zoek uit wat waar staat** | Er zijn drie dingen, en die staan niet altijd bij dezelfde partij:<br>• **Domeinregistratie:** opzoeken via de whois van SIDN (.nl) of de registrar.<br>• **DNS-beheer:** wie beheert de nameservers?<br>• **E-mail:** de MX-records laten zien waar de mail draait (te checken met MXToolbox). |
| 2 | **Alle DNS-records vastleggen** | Maak een export of screenshot van: A, AAAA, CNAME, **MX**, TXT (SPF, DKIM, DMARC, verificaties van Google en Microsoft) en SRV. Records die je vergeet, gaan bij de verhuizing verloren. |
| 3 | **Back-ups maken** | Maak een back-up van de oude website (bestanden en database), en van de **mailboxen** als de e-mail ook verhuist. |
| 4 | **Contract controleren** | Wat is de opzegtermijn? **Zeg pas op als alles over is.** Laat de oude hosting 2–4 weken doorlopen als vangnet. |
| 5 | **Oude URL's en redirects** | Hetzelfde als B4 en B5. |

### Fase 2: Klaarzetten (bij de nieuwe partij)

| # | Stap | Wat je doet |
|---|---|---|
| 6 | **Nieuwe hosting aanmaken** | Upload de nieuwe site en test die op het tijdelijke adres (bijv. `naam.netlify.app`). Je kunt ook je eigen `hosts`-bestand aanpassen om de site onder het echte domein te bekijken. |
| 7 | **Redirects en formulier testen** | Doe dit op de nieuwe omgeving, vóór de overstap. |
| 8 | **E-mail voorbereiden** (alleen als die meeverhuist) | Maak eerst **dezelfde mailboxen** aan bij de nieuwe provider. Plan daarna de migratie van de oude mail (IMAP-migratie; de meeste providers hebben daar een tool voor). |
| 9 | **TTL verlagen** | Zet de TTL van de DNS-records **24–48 uur vooraf** op 300 seconden (5 minuten). Dan gaat de omschakeling straks snel. |

### Fase 3: Overschakelen

Kies **één** van de twee routes:

| Route | Wanneer | Hoe |
|---|---|---|
| **1. Alleen DNS aanpassen** (aanbevolen) | Het domein blijft bij de huidige registrar | Pas alleen de A- en CNAME-records van de website aan naar de nieuwe hoster. **MX-records blijven staan** als de e-mail niet verhuist. Snel, met weinig risico. |
| **2. Domein ook verhuizen** | De klant wil alles bij één partij | Vraag bij de oude registrar de **verhuiscode** (autorisatiecode, token) aan en haal een eventuele domeinvergrendeling eraf. Start de verhuizing bij de nieuwe partij. **Zet alle DNS-records eerst klaar bij de nieuwe partij**, anders valt ook de e-mail weg. Duur: .nl meestal binnen enkele uren, .com 5–7 dagen. |

Tip: verhuis **eerst de website** (route 1) en **daarna pas het domein en de e-mail**, op een ander moment. Dan gaat er nooit alles tegelijk mis.

| # | Stap | Wat je doet |
|---|---|---|
| 10 | **Records omzetten** | Op een rustig moment. |
| 11 | **E-mail omzetten** (indien van toepassing) | Zet de MX-records om naar de nieuwe provider, pas SPF, DKIM en DMARC aan en laat daarna de mailmigratie lopen. |
| 12 | **SSL activeren** | Doe dit op de nieuwe hosting en zet "HTTPS afdwingen" aan. |
| 13 | **Controleren** | Loop dezelfde eindcontrole na als bij B11. Test **e-mail in beide richtingen** en controleer de site met een tool als dnschecker.org vanaf verschillende locaties. |

### Fase 4: Nazorg

| # | Stap | Wat je doet |
|---|---|---|
| 14 | **48 uur monitoren** | Komen alle mails binnen? Werkt het formulier? Komen er 404-fouten binnen? |
| 15 | **TTL terugzetten** | Zet de TTL weer op de normale waarde (bijv. 3600 seconden). |
| 16 | **Search Console** | Dien de sitemap opnieuw in. Verandert ook de **domeinnaam**? Gebruik dan de tool *Adreswijziging* en zet 301-redirects van het oude naar het nieuwe domein. Laat die minstens een jaar staan. |
| 17 | **Oude hosting opzeggen** | Doe dat pas na 2–4 weken zonder problemen, en nadat je alles hebt gedownload. |
| 18 | **Overdracht vastleggen** | Leg alle logins, DNS-records en keuzes vast in een kort document voor de klant. |

---

## Snelle vergelijking

| | A. Nieuw bedrijf | B. Bestaande hosting | C. Verhuizen |
|---|---|---|---|
| Doorlooptijd | ±1 dag | ½–1 dag | 1–3 dagen + 2–4 weken nazorg |
| Grootste risico | E-mail in spam (SPF/DKIM vergeten) | Oude pagina's kwijt in Google (geen redirects) | E-mail valt weg (MX/DNS-records vergeten) |
| Offline tijd | n.v.t. | Enkele minuten | Bijna geen, mits TTL vooraf verlaagd |
| Belangrijkste tool | Registrar + Netlify | Hostingpaneel + `.htaccess` | DNS-overzicht + verhuiscode |

## Intakevragen voor de klant (bij B en C)

1. Bij welke partij staan je domein, je hosting en je e-mail?
2. Heb je de logins van alle drie, of wie heeft die?
3. Welke e-mailadressen zijn er, en gebruik je Outlook, Gmail of iets anders?
4. Draaien er nog andere dingen op het domein (webshop, klantportaal, subdomeinen)?
5. Wanneer loopt je huidige contract af, en wat is de opzegtermijn?
6. Wanneer kan de overstap het beste (rustig moment)?
