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
    },

    // Bond from its yield: annual coupons, whole years. Macaulay duration is the
    // present-value-weighted average time to the cash flows; modified = Macaulay / (1 + y).
    bond: function (i) {
      var y = i.ytm_pct / 100, c = i.face * i.coupon_pct / 100;
      function price(r) {
        var p = i.face / Math.pow(1 + r, i.years);
        for (var t = 1; t <= i.years; t++) p += c / Math.pow(1 + r, t);
        return p;
      }
      var p0 = price(y), w = i.years * i.face / Math.pow(1 + y, i.years);
      for (var t = 1; t <= i.years; t++) w += t * c / Math.pow(1 + y, t);
      var mac = w / p0, mod = mac / (1 + y);
      var up = price(y + 0.01), dn = price(y - 0.01);
      return {
        price: p0, current_yield_pct: c / p0 * 100, macaulay: mac, modified: mod,
        price_up: up, pct_up: (up / p0 - 1) * 100,
        price_dn: dn, pct_dn: (dn / p0 - 1) * 100, est_pct: mod
      };
    },

    // Yield to maturity from a price: the rate that makes the discounted cash flows equal it (bisection).
    ytm: function (i) {
      var c = i.face * i.coupon_pct / 100;
      function price(r) {
        var p = i.face / Math.pow(1 + r, i.years);
        for (var t = 1; t <= i.years; t++) p += c / Math.pow(1 + r, t);
        return p;
      }
      var lo = -0.9, hi = 5;
      for (var k = 0; k < 200; k++) {
        var mid = (lo + hi) / 2;
        if (price(mid) > i.price) lo = mid; else hi = mid;
      }
      return { ytm_pct: (lo + hi) / 2 * 100, current_yield_pct: c / i.price * 100 };
    },

    // Position sizing: rupees at risk / stop distance (k x ATR), rounded down to whole shares.
    positionSize: function (i) {
      var risk = i.capital * i.risk_pct / 100, stop = i.atr_multiple * i.atr;
      var shares = Math.floor(risk / stop + 1e-9);
      return {
        risk_rupees: risk, stop_distance: stop, stop_price: i.close - stop,
        shares: shares, position_value: shares * i.close,
        position_pct: shares * i.close / i.capital * 100
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
  function inr2(x) { var r = Number(x.toFixed(2)); return sign(r, "₹" + new Intl.NumberFormat("en-IN", { maximumFractionDigits: 2 }).format(Math.abs(r))); }
  function yrs(x) { return Number(x.toFixed(2)) + " years"; }
  function pct2(x) { return pct(x, 2); }
  var FMT = { inr: inr, inr2: inr2, yrs: yrs, pct2: pct2, pct: pct, times: times, int: function (x) { return grp.format(Math.round(x)); } };

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
    }],
    "bond-yield": [
      {
        calc: "bond", inputs: ["face", "coupon_pct", "years", "ytm_pct"],
        check: function (i) {
          if (!(i.face > 0)) return "Enter a face value above ₹0.";
          if (!(i.coupon_pct >= 0)) return "The coupon can't be negative (use 0 for a zero-coupon bond).";
          if (!(i.years >= 1 && i.years <= 50 && Number.isInteger(i.years))) return "Enter whole years to maturity, from 1 to 50.";
          if (!(i.ytm_pct > -50)) return "Enter a yield above −50%.";
        },
        show: { price: "inr2", current_yield_pct: "pct2", macaulay: "yrs", modified: "yrs", price_up: "inr2", pct_up: "pct2", price_dn: "inr2", pct_dn: "pct2", est_pct: "pct2" }
      },
      {
        calc: "ytm", inputs: ["face", "coupon_pct", "years", "price"],
        check: function (i) {
          if (!(i.face > 0 && i.price > 0)) return "Enter a face value and a price above ₹0.";
          if (!(i.coupon_pct >= 0)) return "The coupon can't be negative.";
          if (!(i.years >= 1 && i.years <= 50 && Number.isInteger(i.years))) return "Enter whole years to maturity, from 1 to 50.";
        },
        show: { ytm_pct: "pct2" }
      }
    ],
    "position-size": [{
      calc: "positionSize", inputs: ["capital", "risk_pct", "atr", "atr_multiple", "close"],
      check: function (i) {
        if (!(i.capital > 0 && i.close > 0 && i.atr > 0)) return "Capital, price and ATR must be above zero.";
        if (!(i.risk_pct > 0 && i.risk_pct <= 100)) return "Enter a risk percentage between 0 and 100.";
        if (!(i.atr_multiple > 0)) return "Enter a stop multiple above zero.";
      },
      show: { risk_rupees: "inr", stop_distance: "inr2", stop_price: "inr2", shares: "int", position_value: "inr", position_pct: "pct" }
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
