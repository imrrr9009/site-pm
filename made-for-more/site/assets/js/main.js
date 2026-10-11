/* Made for More — kleine, progressieve verbeteringen. De site werkt volledig zonder JS. */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* Header-rand bij scrollen */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobiele navigatie */
  var toggle = document.querySelector(".nav-toggle");
  var panel = document.getElementById("nav-panel");
  if (toggle && panel) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Menu sluiten" : "Menu openen");
      panel.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
    panel.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    window.matchMedia("(min-width: 960px)").addEventListener("change", function (mq) {
      if (mq.matches) setOpen(false);
    });
  }

  /* Elementen laten verschijnen bij scrollen (respecteert reduced motion) */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          el.classList.remove("is-pending");
          io.unobserve(el);
          // vertraging weghalen na het verschijnen, zodat hover-effecten direct reageren
          setTimeout(function () { el.style.transitionDelay = ""; }, 700 + Number(el.dataset.delay || 0));
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    document.querySelectorAll(".reveal").forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight) return; // al in beeld: direct zichtbaar
      el.style.transitionDelay = (el.dataset.delay || 0) + "ms";
      el.classList.add("is-pending");
      io.observe(el);
    });
  }

  /* Contactformulier: validatie bij het veld zelf */
  var form = document.querySelector("form[data-validate]");
  if (form) {
    var messages = {
      naam: "Vul je naam in.",
      email: "Vul een geldig e-mailadres in, bijvoorbeeld naam@bedrijf.nl.",
      bericht: "Vertel kort waar je mee geholpen wilt worden."
    };
    var check = function (field) {
      var error = document.getElementById(field.id + "-error");
      var valid = field.checkValidity();
      field.setAttribute("aria-invalid", String(!valid));
      if (error) error.textContent = valid ? "" : (messages[field.name] || "Dit veld is verplicht.");
      return valid;
    };
    form.querySelectorAll("[required]").forEach(function (field) {
      field.addEventListener("blur", function () { check(field); });
      field.addEventListener("input", function () {
        if (field.getAttribute("aria-invalid") === "true") check(field);
      });
    });
    form.addEventListener("submit", function (e) {
      var firstInvalid = null;
      form.querySelectorAll("[required]").forEach(function (field) {
        if (!check(field) && !firstInvalid) firstInvalid = field;
      });
      if (firstInvalid) {
        e.preventDefault();
        firstInvalid.focus();
      } else {
        var btn = form.querySelector("[type=submit]");
        if (btn) { btn.disabled = true; btn.textContent = "Versturen…"; }
      }
    });
  }

  /* Jaartal in footer */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
})();
