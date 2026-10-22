/* Cookie consent for Made for More.
   The impact.com tracking script is only loaded after the visitor clicks "Accept".
   The choice is stored in localStorage; "Cookie settings" in the footer reopens the banner. */
(function () {
  "use strict";
  var KEY = "mfm-cookie-consent";
  var IMPACT_SRC = "https://utt.impactcdn.com/P-A8025348-a1f4-4590-b8f6-998c19c3d2f71.js";

  function getChoice() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setChoice(v) { try { localStorage.setItem(KEY, v); } catch (e) { /* storage blocked: ask again next visit */ } }

  function loadImpact() {
    if (window.__mfmImpactLoaded) return;
    window.__mfmImpactLoaded = true;
    // impact.com Universal Tracking Tag (as supplied by impact.com)
    (function (i, m, p, a, c, t) {
      c.ire_o = p;
      c[p] = c[p] || function () { (c[p].a = c[p].a || []).push(arguments); };
      t = a.createElement(m);
      var z = a.getElementsByTagName(m)[0];
      t.async = 1; t.src = i;
      z.parentNode.insertBefore(t, z);
    })(IMPACT_SRC, "script", "impactStat", document, window);
    window.impactStat("transformLinks");
    window.impactStat("trackImpression");
  }

  // Remove first-party cookies set by impact.com (they start with "IR_") when consent is withdrawn.
  function clearImpactCookies() {
    var host = location.hostname.replace(/^www\./, "");
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (name.indexOf("IR_") === 0) {
        ["", "; domain=" + host, "; domain=." + host].forEach(function (d) {
          document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
        });
      }
    });
  }

  var banner = document.getElementById("cookie-banner");
  if (!banner) return;
  var accept = document.getElementById("cookie-accept");
  var decline = document.getElementById("cookie-decline");

  function show() { banner.hidden = false; }
  function hide() { banner.hidden = true; }

  var choice = getChoice();
  if (choice === "accepted") loadImpact();
  else if (choice !== "declined") show();

  accept.addEventListener("click", function () {
    setChoice("accepted");
    hide();
    loadImpact();
  });

  decline.addEventListener("click", function () {
    var wasLoaded = window.__mfmImpactLoaded;
    setChoice("declined");
    hide();
    clearImpactCookies();
    if (wasLoaded) location.reload(); // stop the already-running script
  });

  document.querySelectorAll("[data-cookie-settings]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      show();
      accept.focus();
    });
  });
})();
