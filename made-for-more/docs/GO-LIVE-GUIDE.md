# Step-by-step plans: putting a new HTML website online

Four situations:

- **0. Preparation:** always applies
- **A. Brand-new business:** no domain, no hosting yet
- **B. Business already has hosting:** the new site goes on the same server
- **C. Migration:** moving from host A to host B, with a new site

---

## 0. Preparation (always)

1. **Test the site locally.** Click through every page, test on your phone and check the contact options.
2. **Check the folder structure.** `index.html` sits in the root folder, with CSS, JS and images next to it in `assets/`.
3. **Set the domain name in the files.** That covers canonical links, `sitemap.xml`, `robots.txt` and `llms.txt`.
4. **Sort out forms (if any).** An HTML form doesn't send anything by itself. Pick one option:
   - on Netlify: Netlify Forms
   - on other hosting: Formspree or Basin, or a PHP script from the host
5. **Collect all logins** and keep them in a password manager (e.g. Bitwarden or 1Password):
   - registrar (where the domain is registered)
   - DNS management
   - hosting and FTP
   - email
   - Google account
6. **Record ownership.** The domain and accounts are in the **client's** name. You get your own admin account.

---

## A. Brand-new business (nothing set up yet)

Time needed: **about 1 day** (most of it is waiting for DNS).

| # | Step | What you do |
|---|---|---|
| 1 | **Choose and register a domain name** | Check the name is available and register it with a registrar (e.g. TransIP, Versio, Hostnet, Antagonist, Namecheap). Consider `.com` / `.nl` / `.be` as well. Register it in the business's name. ⏱ 5–15 min |
| 2 | **Choose the type of hosting** | **HTML only:** static hosting such as Netlify, Cloudflare Pages or Vercel. Fast, free up to a generous size, SSL included. **Will need WordPress, PHP or a webshop later:** shared hosting (e.g. Hostinger, TransIP, Antagonist). |
| 3 | **Set up business email** | Static hosting has **no email**. Choose Google Workspace, Microsoft 365 or your registrar's email package. Create the mailboxes first (e.g. hello@). |
| 4 | **Upload the website** | **Netlify:** drag the folder into *Deploy manually*; live in about 1 minute on `name.netlify.app`. **Shared hosting:** upload via the file manager or SFTP (e.g. with FileZilla) to the web folder: `public_html`, `httpdocs` or `www`, depending on the host. |
| 5 | **Connect the domain (DNS)** | Enter the DNS records your host gives you at your registrar. **Netlify:** A record `@` → the IP Netlify shows, CNAME `www` → `name.netlify.app`. Or point the nameservers to Netlify. **Shared hosting:** usually automatic if domain and hosting are with the same provider. ⏱ 5 min to a few hours |
| 6 | **Set up email DNS** | Add your email provider's MX records, plus **SPF**, **DKIM** and **DMARC**, or your mail will end up in spam. |
| 7 | **Turn on SSL / https** | Usually automatic (Let's Encrypt). Then switch on **"Force HTTPS"**. |
| 8 | **Choose: with or without www** | Pick one and redirect the other with a 301 redirect. |
| 9 | **Final check** | Check: all pages, mobile, contact links (send a test message), the 404 page, the padlock in the browser and the score in PageSpeed Insights. |
| 10 | **Register with search engines** | **Google Search Console:** verify the domain with a DNS TXT record and submit `sitemap.xml`. **Bing Webmaster Tools:** import from Search Console. |
| 11 | **Local visibility** | Create a Google Business Profile and add the website. Use exactly the same business name, address and phone number everywhere. |
| 12 | **Analytics** | Add a cookieless tool (e.g. Plausible or Umami). Then no cookie banner is needed. |

---

## B. Business already has hosting (new site on the same server)

Time needed: **half a day to 1 day**. The site is only offline for a few minutes if you prepare well.

| # | Step | What you do |
|---|---|---|
| 1 | **Get access** | Ask the client for the hosting panel login (cPanel, DirectAdmin or Plesk), FTP and DNS. If that's not possible, have the client add you as a user. |
| 2 | **Take stock of what's running** | Is it an old WordPress site? Does **email run on the same hosting**? Are there databases, subdomains or other apps? **Leave the email settings alone.** |
| 3 | **Make a full backup** | Download all files and export the database(s). Also make a backup through the hosting panel if possible. Keep it locally. |
| 4 | **Record the old URLs** | Make a list of all existing pages. Use Google Search Console (*Pages* → export) or the free version of Screaming Frog (up to 500 URLs). |
| 5 | **Prepare redirects** | Map each old URL to the best matching new page and add them as **301 redirects** in `.htaccess` (on Apache or LiteSpeed), for example:<br>`Redirect 301 /about-me /#contact`<br>This keeps your Google rankings and old links keep working. |
| 6 | **Test first** | Put the new site on a test address, e.g. `test.business.com` or a temporary URL from the host, with `noindex`. Have the client approve it. |
| 7 | **Pick a quiet moment** | For example in the evening or at the weekend. Let the client know when it will happen. |
| 8 | **Switch over** | Move the old files to a backup folder **outside** the web folder, or zip them. Then upload the new files to the web folder. Note: **delete `index.php`**, otherwise the server may load it before `index.html`. Leave the `.well-known` folder in place (needed for SSL). |
| 9 | **Set up a 404 page** | Add to `.htaccess`: `ErrorDocument 404 /404.html`. |
| 10 | **Clear caches** | Clear the hosting cache and the CDN cache (e.g. Cloudflare), and open the site in a private window. |
| 11 | **Check** | Run the same final check as in A9. Also test **the redirects** and **that email still works** (send and receive a test email). |
| 12 | **Search Console** | Submit the new `sitemap.xml`. Check weekly for 404 errors during the first 2–4 weeks and add redirects where needed. |
| 13 | **Clean up** | After 2–4 weeks, remove the old backup folder from the server. Keep a local copy. Was it WordPress? Delete the database too, so no outdated, insecure software is left behind. |

---

## C. Moving from host A to host B (with a new site)

Time needed: **1–3 days** of preparation; the switch itself takes a few hours. The biggest risk is **email**: plan that separately.

### Phase 1: Take stock (at the old provider)

| # | Step | What you do |
|---|---|---|
| 1 | **Find out what is where** | There are three things, and they are not always with the same provider:<br>• **Domain registration:** look it up via WHOIS (for .nl: SIDN) or the registrar.<br>• **DNS management:** who manages the nameservers?<br>• **Email:** the MX records show where mail runs (check with MXToolbox). |
| 2 | **Record all DNS records** | Export or screenshot: A, AAAA, CNAME, **MX**, TXT (SPF, DKIM, DMARC, Google and Microsoft verifications) and SRV. Any record you forget is lost in the move. |
| 3 | **Make backups** | Back up the old website (files and database), and the **mailboxes** if email is moving too. |
| 4 | **Check the contract** | What is the notice period? **Only cancel once everything has moved.** Keep the old hosting running for 2–4 weeks as a safety net. |
| 5 | **Old URLs and redirects** | Same as B4 and B5. |

### Phase 2: Prepare (at the new provider)

| # | Step | What you do |
|---|---|---|
| 6 | **Create the new hosting** | Upload the new site and test it on the temporary address (e.g. `name.netlify.app`). You can also edit your own `hosts` file to view the site under the real domain. |
| 7 | **Test redirects and forms** | Do this on the new environment, before the switch. |
| 8 | **Prepare email** (only if it moves) | First create **the same mailboxes** at the new provider. Then plan the migration of the old mail (IMAP migration; most providers have a tool for it). |
| 9 | **Lower the TTL** | Set the TTL of the DNS records to 300 seconds (5 minutes) **24–48 hours in advance**. That makes the switch fast later. |

### Phase 3: Switch over

Choose **one** of the two routes:

| Route | When | How |
|---|---|---|
| **1. Change DNS only** (recommended) | The domain stays with the current registrar | Only change the website's A and CNAME records to the new host. **MX records stay as they are** if email isn't moving. Fast, low risk. |
| **2. Transfer the domain too** | The client wants everything with one provider | Request the **transfer code** (authorisation code, EPP code) from the old registrar and remove any domain lock. Start the transfer at the new provider. **Set up all DNS records at the new provider first**, or email will go down too. Time: .nl usually within a few hours, .com 5–7 days. |

Tip: move **the website first** (route 1) and **the domain and email later**, at a different time. That way everything never goes wrong at once.

| # | Step | What you do |
|---|---|---|
| 10 | **Switch the records** | At a quiet moment. |
| 11 | **Switch email** (if applicable) | Point the MX records to the new provider, update SPF, DKIM and DMARC, then run the mail migration. |
| 12 | **Activate SSL** | Do this on the new hosting and switch on "Force HTTPS". |
| 13 | **Check** | Run the same final check as in B11. Test **email in both directions** and check the site with a tool like dnschecker.org from different locations. |

### Phase 4: Aftercare

| # | Step | What you do |
|---|---|---|
| 14 | **Monitor for 48 hours** | Is all mail arriving? Do the contact links and forms work? Are 404 errors coming in? |
| 15 | **Reset the TTL** | Set the TTL back to its normal value (e.g. 3600 seconds). |
| 16 | **Search Console** | Resubmit the sitemap. Is the **domain name** changing as well? Use the *Change of Address* tool and set up 301 redirects from the old domain to the new one. Keep them for at least a year. |
| 17 | **Cancel the old hosting** | Only after 2–4 weeks without problems, and after you have downloaded everything. |
| 18 | **Document the handover** | Record all logins, DNS records and decisions in a short document for the client. |

---

## Quick comparison

| | A. New business | B. Existing hosting | C. Migration |
|---|---|---|---|
| Time needed | ~1 day | ½–1 day | 1–3 days + 2–4 weeks aftercare |
| Biggest risk | Email in spam (SPF/DKIM forgotten) | Old pages lost in Google (no redirects) | Email goes down (MX/DNS records forgotten) |
| Downtime | n/a | A few minutes | Almost none, if TTL is lowered in advance |
| Key tool | Registrar + Netlify | Hosting panel + `.htaccess` | DNS overview + transfer code |

## Intake questions for the client (B and C)

1. Which provider holds your domain, your hosting and your email?
2. Do you have the logins for all three, or who does?
3. Which email addresses exist, and do you use Outlook, Gmail or something else?
4. Is anything else running on the domain (webshop, client portal, subdomains)?
5. When does your current contract end, and what is the notice period?
6. When is the best moment for the switch (a quiet time)?
