/*
 * On-page calculators (kind "Calculator" in _data/tools.yml).
 *
 * Each calculator is a <form class="calc" data-calc="..."> drawn by
 * _includes/calc/<id>.html, with its default inputs (the post's worked example,
 * from _data/tool_defaults.json) in data-defaults. This file holds the formulas,
 * the number formatting and the wiring. No storage, no network, no libraries.
 *
 * The formulas are also run in Node by scripts/check_tools.mjs against the
 * cases in _data/tool_defaults.json, so keep them pure: numbers in, numbers out.
 */
(function (root) {
  "use strict";

  var F = {
    // The arithmetic of losses: gain needed to get back from a fall.
    recovery: function (i) {
      return { gain_pct: (1 / (1 - i.fall_pct / 100) - 1) * 100 };
    },

    // Leverage and margin: a position funded partly with borrowed money.
    leverage: function (i) {
      var position = i.own + i.borrowed;
      var interest = i.borrowed * i.rate_pct / 100 * i.months / 12;
      var pnl = position * i.move_pct / 100 - interest;
      return {
        position: position,
        leverage: position / i.own,
        interest: interest,
        pnl: pnl,
        return_pct: pnl / i.own * 100,
        breakeven_pct: interest / position * 100,
        wipeout_pct: -(i.own - interest) / position * 100,
        owed: Math.max(0, -pnl - i.own)
      };
    },

    // Expense ratio: Value after N years = Initial × (1 + r − fee)^N
    costDrag: function (i) {
      var low = i.amount * Math.pow(1 + i.rate_pct / 100, i.years);
      var high = i.amount * Math.pow(1 + (i.rate_pct - i.extra_cost_pp) / 100, i.years);
      return {
        low: low,
        high: high,
        diff: low - high,
        diff_pct: (low / high - 1) * 100,
        share_pct: (1 - high / low) * 100
      };
    },

    // Inflation and real returns: Real return = (1 + nominal) / (1 + inflation) − 1
    realReturn: function (i) {
      var n = i.rate_pct / 100, inf = i.inflation_pct / 100;
      var nominal = i.amount * Math.pow(1 + n, i.years);
      return {
        nominal: nominal,
        real: nominal / Math.pow(1 + inf, i.years),
        real_rate_pct: ((1 + n) / (1 + inf) - 1) * 100,
        approx_pct: (n - inf) * 100,
        needed: i.amount * Math.pow(1 + inf, i.years)
      };
    }
  };

  if (typeof module !== "undefined" && module.exports) { module.exports = F; return; }

  // ---- formatting: Indian grouping, a real minus sign, no false ".0" ----------
  var MINUS = "−";
  var grp = new Intl.NumberFormat("en-IN", { maximumFractionDigits: 0 });
  function sign(x, s) { return x < 0 ? MINUS + s : s; }
  function inr(x) { var r = Math.round(x); return sign(r, "₹" + grp.format(Math.abs(r))); }
  function pct(x, d) {
    var r = Number(x.toFixed(d === undefined ? 1 : d));
    if (r === 0) r = 0; // no "−0%"
    return sign(r, Math.abs(r) + "%");
  }
  function times(x) { return Number(x.toFixed(2)) + "×"; }
  var FMT = { inr: inr, pct: pct, times: times, int: function (x) { return grp.format(Math.round(x)); } };

  // What each calculator shows. `check` returns a message when the inputs make no sense.
  var VIEWS = {
    "loss-recovery": [
      {
        calc: "recovery", inputs: ["fall_pct"],
        check: function (i) { if (!(i.fall_pct > 0 && i.fall_pct < 100)) return "Enter a fall between 0% and 100%. A 100% fall can't be recovered: there's nothing left to grow."; },
        show: { gain_pct: "pct", fall_pct_echo: "pct" }
      },
      {
        calc: "leverage", inputs: ["own", "borrowed", "rate_pct", "months", "move_pct"],
        check: function (i) {
          if (!(i.own > 0)) return "Enter how much of your own money goes in (more than ₹0).";
          if (!(i.borrowed >= 0 && i.rate_pct >= 0 && i.months >= 0)) return "Borrowed amount, rate and months can't be negative.";
          if (!(i.move_pct >= -100)) return "A price can't fall more than 100%.";
        },
        show: { position: "inr", leverage: "times", interest: "inr", breakeven_pct: "pct", pnl: "inr", return_pct: "pct", wipeout_pct: "pct", owed: "inr" }
      }
    ],
    "cost-drag": [{
      calc: "costDrag", inputs: ["amount", "years", "rate_pct", "extra_cost_pp"],
      check: function (i) {
        if (!(i.amount > 0 && i.years >= 0)) return "Enter an amount above ₹0 and a number of years.";
        if (!(i.extra_cost_pp >= 0)) return "The extra cost is the higher-cost plan's additional charge, so it can't be negative.";
        if (!(i.rate_pct - i.extra_cost_pp > -100)) return "The higher-cost plan's return would be below −100% a year.";
      },
      show: { low: "inr", high: "inr", diff: "inr", diff_pct: "pct", share_pct: "pct" }
    }],
    "real-return": [{
      calc: "realReturn", inputs: ["amount", "years", "rate_pct", "inflation_pct"],
      check: function (i) {
        if (!(i.amount > 0 && i.years >= 0)) return "Enter an amount above ₹0 and a number of years.";
        if (!(i.rate_pct > -100 && i.inflation_pct > -100)) return "Rates must be above −100% a year.";
      },
      show: { nominal: "inr", real: "inr", real_rate_pct: "pct", approx_pct: "pct", gap_pp: "pp", needed: "inr" }
    }]
  };

  function read(form, names) {
    var i = {};
    names.forEach(function (n) {
      var el = form.elements[n];
      // Accept "1,00,000" and a typed minus sign as well as plain digits.
      i[n] = el.value.trim() === "" ? NaN : Number(el.value.replace(/,/g, "").replace(MINUS, "-"));
    });
    return i;
  }

  function render(form) {
    VIEWS[form.dataset.calc].forEach(function (v, k) {
      var part = form.querySelector('[data-part="' + k + '"]') || form;
      var i = read(form, v.inputs);
      var msg = part.querySelector(".calc-error");
      var bad = v.inputs.some(function (n) { return !isFinite(i[n]); }) ? "Fill in every box with a number." : v.check(i);
      part.classList.toggle("calc-invalid", !!bad);
      if (msg) msg.textContent = bad || "";
      if (bad) return;
      var o = F[v.calc](i);
      o.fall_pct_echo = i.fall_pct;
      if (v.calc === "realReturn") o.gap_pp = o.approx_pct - o.real_rate_pct;
      Object.keys(v.show).forEach(function (key) {
        part.querySelectorAll('[data-out="' + key + '"]').forEach(function (el) {
          var f = v.show[key];
          el.textContent = f === "pp" ? Number(Math.abs(o[key]).toFixed(2)) + " percentage points" : FMT[f](o[key]);
        });
      });
      part.querySelectorAll("[data-show-if]").forEach(function (el) {
        var c = el.dataset.showIf.split(">");
        el.hidden = !(o[c[0]] > Number(c[1]));
      });
    });
  }

  function setup(form) {
    var defaults = JSON.parse(form.dataset.defaults);
    function reset() {
      Object.keys(defaults).forEach(function (n) { if (form.elements[n]) form.elements[n].value = defaults[n]; });
      render(form);
    }
    form.addEventListener("input", function () { render(form); });
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    var btn = form.querySelector(".calc-reset");
    if (btn) btn.addEventListener("click", reset);
    form.classList.add("calc-ready");
    render(form);
  }

  function init() { document.querySelectorAll("form.calc[data-calc]").forEach(setup); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})(this);
