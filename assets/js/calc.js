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
    },
    // Goal-based investing: inflate a cost, then work back at an assumed return.
    // Monthly instalments at the start of each month; m = (1 + r)^(1/12) − 1.
    // A step-up raises the instalment once a year by step_up_pct.
    goal: function (i) {
      var n = Math.round(i.years) * 12, r = i.return_pct / 100;
      var m = Math.pow(1 + r, 1 / 12) - 1;
      var future = i.cost_today * Math.pow(1 + i.inflation_pct / 100, i.years);
      function fv(step) {
        var total = 0;
        for (var k = 0; k < n; k++) total = (total + Math.pow(1 + step, Math.floor(k / 12))) * (1 + m);
        return total;
      }
      function paid(step) {
        var t = 0;
        for (var k = 0; k < n; k++) t += Math.pow(1 + step, Math.floor(k / 12));
        return t;
      }
      var s = i.step_up_pct / 100;
      var monthly = future / fv(0), first = future / fv(s);
      return {
        future_cost: future,
        lump_today: future / Math.pow(1 + r, i.years),
        monthly: monthly,
        flat_paid: monthly * paid(0),
        step_first: first,
        step_last: first * Math.pow(1 + s, Math.round(i.years) - 1),
        step_paid: first * paid(s)
      };
    },

    // Rolling returns: parse a pasted two-column series (date, value). Returns
    // { dates: [UTC ms], values: [], rows, error, gap } — `error` is a message for
    // the first bad line; `gap` is the first jump of more than 10 calendar days.
    // Separators: tab, semicolon, comma (double quotes respected, so "24,123.45"
    // stays one field) or spaces. Dates: 2026-03-31, 31-03-2026, 31/03/2026,
    // 31-Mar-2026 (day first). A first line that isn't data is a header and is
    // skipped. A repeated date keeps its last row. Extra columns are ignored.
    parseSeries: function (text) {
      var MONTHS = { jan: 1, feb: 2, mar: 3, apr: 4, may: 5, jun: 6, jul: 7, aug: 8, sep: 9, oct: 10, nov: 11, dec: 12 };
      function fields(line) {
        if (line.indexOf("\t") >= 0) return line.split("\t");
        if (line.indexOf(";") >= 0) return line.split(";");
        if (line.indexOf(",") >= 0) {
          var out = [], cur = "", q = false;
          for (var k = 0; k < line.length; k++) {
            var ch = line[k];
            if (ch === '"') q = !q;
            else if (ch === "," && !q) { out.push(cur); cur = ""; }
            else cur += ch;
          }
          out.push(cur);
          return out;
        }
        return line.trim().split(/\s+/);
      }
      function day(s) {
        var m, y, mo, d;
        s = s.trim().replace(/^"|"$/g, "");
        if ((m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/))) { y = +m[1]; mo = +m[2]; d = +m[3]; }
        else if ((m = s.match(/^(\d{1,2})[-\/.](\d{1,2})[-\/.](\d{4})$/))) { d = +m[1]; mo = +m[2]; y = +m[3]; }
        else if ((m = s.match(/^(\d{1,2})[- ]([A-Za-z]{3})[A-Za-z]*[- ](\d{4})$/)) && MONTHS[m[2].toLowerCase()]) { d = +m[1]; mo = MONTHS[m[2].toLowerCase()]; y = +m[3]; }
        else return NaN;
        var t = Date.UTC(y, mo - 1, d), c = new Date(t);
        return c.getUTCFullYear() === y && c.getUTCMonth() === mo - 1 && c.getUTCDate() === d ? t : NaN;
      }
      function num(s) {
        s = (s || "").trim().replace(/^"|"$/g, "").replace(/,/g, "").replace(/−/g, "-");
        return s === "" ? NaN : Number(s);
      }
      var lines = String(text).split(/\r\n|\n|\r/), byDate = {}, first = true;
      for (var i = 0; i < lines.length; i++) {
        if (!lines[i].trim()) continue;
        var f = fields(lines[i]), t = day(f[0] || ""), v = num(f[1]);
        if (isNaN(t) && f.length >= 4 && !/[\t;,]/.test(lines[i])) { // "29 Feb 2024 123.4"
          t = day(f.slice(0, 3).join(" ")); v = num(f[3]);
        }
        if (first && isNaN(t)) { first = false; continue; } // header
        first = false;
        if (isNaN(t)) return { error: "Line " + (i + 1) + ": the first column isn't a date this calculator reads (use 2026-03-31, 31-03-2026 or 31-Mar-2026)." };
        if (!(v > 0)) return { error: "Line " + (i + 1) + ": the value must be a number above 0." };
        byDate[t] = v;
      }
      var dates = Object.keys(byDate).map(Number).sort(function (a, b) { return a - b; });
      if (dates.length > 25000) return { error: "That's more than 25,000 rows. Paste daily data of up to about 100 years." };
      if (dates.length < 2) return { error: "Paste at least two rows: a date and a value on each line, oldest or newest first." };
      var gap = null;
      for (var j = 1; j < dates.length && !gap; j++) if (dates[j] - dates[j - 1] > 10 * 864e5) gap = [dates[j - 1], dates[j]];
      return { dates: dates, values: dates.map(function (t) { return byDate[t]; }), rows: dates.length, gap: gap };
    },

    // Every start date d with d + N calendar years inside the data (29 Feb ->
    // 28 Feb); the end value is the last one on or before that date; CAGR in %.
    // The same method as the rolling returns post (pandas DateOffset + asof).
    rollingReturns: function (dates, values, years, threshold) {
      var last = dates[dates.length - 1], cagr = [], starts = [];
      function plusYears(t) {
        var d = new Date(t), y = d.getUTCFullYear() + years, m = d.getUTCMonth();
        var dim = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
        return Date.UTC(y, m, Math.min(d.getUTCDate(), dim));
      }
      function asof(t) { // index of the last date <= t
        var lo = 0, hi = dates.length - 1;
        while (lo < hi) { var mid = (lo + hi + 1) >> 1; if (dates[mid] <= t) lo = mid; else hi = mid - 1; }
        return lo;
      }
      for (var i = 0; i < dates.length; i++) {
        var end = plusYears(dates[i]);
        if (end > last) break;
        cagr.push((Math.pow(values[asof(end)] / values[i], 1 / years) - 1) * 100);
        starts.push(dates[i]);
      }
      var n = cagr.length;
      if (!n) return { windows: 0 };
      var lo = 0, hi = 0, neg = 0, below = 0;
      for (var k = 0; k < n; k++) {
        if (cagr[k] < cagr[lo]) lo = k;
        if (cagr[k] > cagr[hi]) hi = k;
        if (cagr[k] < 0) neg++;
        if (cagr[k] < threshold) below++;
      }
      var s = cagr.slice().sort(function (a, b) { return a - b; });
      var iso = function (t) { return new Date(t).toISOString().slice(0, 10); };
      return {
        windows: n, min: cagr[lo], max: cagr[hi],
        median: n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2,
        worst_start: iso(starts[lo]), best_start: iso(starts[hi]),
        pct_negative: neg / n * 100, pct_below: below / n * 100
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
    "goal": [{
      calc: "goal", inputs: ["cost_today", "years", "inflation_pct", "return_pct", "step_up_pct"],
      check: function (i) {
        if (!(i.cost_today > 0)) return "Enter today's cost of the goal (more than ₹0).";
        if (!(i.years >= 1 && i.years <= 50 && Number.isInteger(i.years))) return "Enter whole years to the goal, from 1 to 50.";
        if (!(i.inflation_pct > -50 && i.return_pct > -50)) return "Enter inflation and return above −50% a year.";
        if (!(i.step_up_pct >= 0 && i.step_up_pct <= 50)) return "Enter a yearly step-up from 0% to 50%.";
      },
      show: { future_cost: "inr", lump_today: "inr", monthly: "inr", flat_paid: "inr", step_first: "inr", step_last: "inr", step_paid: "inr" }
    }],
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

  // ---- rolling returns: a pasted series, a results table and a range chart ----
  var NOTES = {
    nav: "A fund's growth NAV includes reinvested dividends and is after the fund's expenses.",
    tri: "A total return index includes reinvested dividends and has no costs; a fund that tracks it earns a little less.",
    price: "A price index leaves out dividends, so these returns understate what an investor in the index earned."
  };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function dmy(t) { return new Date(t).toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" }); }

  function rollingChart(rows, threshold, width) {
    var ok = rows.filter(function (r) { return r.res.windows; });
    if (!ok.length) return "";
    var lo = Math.min(0, threshold), hi = Math.max(0, threshold);
    ok.forEach(function (r) { lo = Math.min(lo, r.res.min); hi = Math.max(hi, r.res.max); });
    var pad = (hi - lo) * 0.06 || 1; lo -= pad; hi += pad;
    // Drawn at the container's own width (320–600) so the text stays readable on a phone.
    var W = Math.round(Math.max(320, Math.min(600, width || 600))), L = W < 420 ? 64 : 104, R = W < 420 ? 44 : 58;
    var top = 26, rowH = 30, H = top + ok.length * rowH + 8;
    var x = function (v) { return (L + (v - lo) / (hi - lo) * (W - L - R)).toFixed(1); };
    var svg = '<svg class="rr-chart" viewBox="0 0 ' + W + " " + H + '" role="img" aria-labelledby="rr-chart-t"><title id="rr-chart-t">Range of rolling returns by holding period: ' +
      ok.map(function (r) { return r.years + " years from " + pct(r.res.min, 2) + " to " + pct(r.res.max, 2) + ", median " + pct(r.res.median, 2); }).join("; ") + ".</title>";
    svg += '<line class="rr-zero" x1="' + x(0) + '" x2="' + x(0) + '" y1="' + (top - 6) + '" y2="' + (H - 4) + '"/>';
    svg += '<line class="rr-thr" x1="' + x(threshold) + '" x2="' + x(threshold) + '" y1="' + (top - 6) + '" y2="' + (H - 4) + '"/>';
    svg += '<text class="rr-thr-label" x="' + x(threshold) + '" y="' + (top - 10) + '" text-anchor="middle">' + esc(pct(threshold, 2)) + "</text>";
    ok.forEach(function (r, k) {
      var y = top + k * rowH + rowH / 2;
      svg += '<text class="rr-row-label" x="0" y="' + (y + 4) + '" text-anchor="start">' + r.years + (W < 420 ? " y" : r.years > 1 ? " years" : " year") + "</text>";
      svg += '<line class="rr-range" x1="' + x(r.res.min) + '" x2="' + x(r.res.max) + '" y1="' + y + '" y2="' + y + '"/>';
      svg += '<circle class="rr-median" cx="' + x(r.res.median) + '" cy="' + y + '" r="5"/>';
      svg += '<text class="rr-end" x="' + (+x(r.res.min) - 9) + '" y="' + (y + 4) + '" text-anchor="end">' + esc(pct(r.res.min, 1)) + "</text>";
      svg += '<text class="rr-end" x="' + (+x(r.res.max) + 9) + '" y="' + (y + 4) + '" text-anchor="start">' + esc(pct(r.res.max, 1)) + "</text>";
    });
    return svg + "</svg>";
  }

  function setupRolling(form) {
    var box = form.elements.series, err = form.querySelector(".calc-error"), warn = form.querySelector(".calc-warn");
    var live = form.querySelector(".rr-live"), example = form.querySelector(".rr-example");
    var timer = null;
    function fail(msg) { form.classList.add("calc-invalid"); err.textContent = msg || ""; live.hidden = true; example.hidden = !!msg; }
    function periods() {
      var ys = [].slice.call(form.querySelectorAll('input[name="period"]:checked')).map(function (c) { return +c.value; });
      var c = form.elements.custom_years.value.trim();
      if (c !== "") {
        var n = Number(c);
        if (!(Number.isInteger(n) && n >= 1 && n <= 30)) return "Enter the extra holding period as whole years, from 1 to 30.";
        if (ys.indexOf(n) < 0) ys.push(n);
      }
      if (!ys.length) return "Tick at least one holding period.";
      return ys.sort(function (a, b) { return a - b; });
    }
    function render() {
      warn.textContent = "";
      if (!box.value.trim()) { fail(""); example.hidden = false; return; }
      var thrRaw = form.elements.threshold.value.trim().replace(MINUS, "-"), thr = Number(thrRaw);
      if (thrRaw === "" || !(thr > -50 && thr < 100)) return fail("Enter a threshold between −50% and 100% a year.");
      var ys = periods();
      if (typeof ys === "string") return fail(ys);
      var p = F.parseSeries(box.value);
      if (p.error) return fail(p.error);
      var rows = ys.map(function (y) { return { years: y, res: F.rollingReturns(p.dates, p.values, y, thr) }; });
      if (!rows.some(function (r) { return r.res.windows; })) return fail("The series is too short: the shortest holding period ticked needs " + ys[0] + " year" + (ys[0] > 1 ? "s" : "") + " of data, plus a day.");
      form.classList.remove("calc-invalid"); err.textContent = ""; example.hidden = true; live.hidden = false;
      var warnings = [];
      if (p.gap) warnings.push("There is a gap of more than 10 days between " + dmy(p.gap[0]) + " and " + dmy(p.gap[1]) + ": check for missing data.");
      var thin = rows.filter(function (r) { return r.res.windows && r.res.windows < 250; }).map(function (r) { return r.years + "-year"; });
      if (thin.length) warnings.push("Fewer than 250 windows for the " + thin.join(", ") + " period" + (thin.length > 1 ? "s" : "") + ": a series only a little longer than the holding period says very little.");
      warn.textContent = warnings.join(" ");
      form.querySelector(".rr-meta").textContent = grp.format(p.rows) + " rows, " + dmy(p.dates[0]) + " to " + dmy(p.dates[p.rows - 1]) + ".";
      form.querySelector(".rr-thr-head").textContent = "% below " + pct(thr, 2);
      form.querySelector(".rr-body").innerHTML = rows.map(function (r) {
        var o = r.res;
        if (!o.windows) return "<tr><th scope=\"row\">" + r.years + " years</th><td colspan=\"6\">Needs at least " + r.years + " years of data</td></tr>";
        return "<tr><th scope=\"row\">" + r.years + (r.years > 1 ? " years" : " year") + "</th><td>" + grp.format(o.windows) + "</td><td>" + pct(o.min, 2) +
          "<span class=\"rr-date\">from " + dmy(Date.parse(o.worst_start)) + "</span></td><td>" + pct(o.median, 2) + "</td><td>" + pct(o.max, 2) +
          "<span class=\"rr-date\">from " + dmy(Date.parse(o.best_start)) + "</span></td><td>" + pct(o.pct_negative, 1) + "</td><td>" + pct(o.pct_below, 1) + "</td></tr>";
      }).join("");
      var wrap = form.querySelector(".rr-chart-wrap");
      wrap.innerHTML = rollingChart(rows, thr, wrap.clientWidth);
      form.querySelector(".rr-note").textContent = NOTES[form.elements.kind.value] + " Past windows describe what happened in this series; they don't predict the next window.";
    }
    form.addEventListener("input", function (e) {
      clearTimeout(timer);
      if (e.target === box) timer = setTimeout(render, 250); else render();
    });
    form.addEventListener("change", function (e) { if (e.target.type === "checkbox" || e.target.tagName === "SELECT") render(); });
    form.addEventListener("submit", function (e) { e.preventDefault(); });
    function fill(text) {
      box.value = text;
      box.dispatchEvent(new Event("input", { bubbles: true })); // also starts the analytics timer
    }
    var file = form.elements.file;
    if (file) file.addEventListener("change", function () {
      var f = file.files && file.files[0];
      if (!f) return;
      var rd = new FileReader();
      rd.onload = function () { fill(String(rd.result)); };
      rd.onerror = function () { fail("Couldn't read that file. Paste its two columns instead."); };
      rd.readAsText(f);
    });
    var load = form.querySelector(".rr-load");
    if (load) load.addEventListener("click", function () {
      load.disabled = true;
      fetch(load.dataset.src).then(function (r) { if (!r.ok) throw 0; return r.text(); })
        .then(function (t) { // keep the date and the regular-plan column only
          form.elements.kind.value = "nav";
          fill(t.split(/\r?\n/).map(function (l) { return l.split(",").slice(0, 2).join(","); }).join("\n"));
        })
        .catch(function () { fail("Couldn't load the worked example. Check your connection and try again."); })
        .then(function () { load.disabled = false; });
    });
    var inline = form.querySelector(".rr-inline-load");
    if (inline && load) inline.addEventListener("click", function () { load.click(); });
    var reset = form.querySelector(".calc-actions .calc-reset");
    if (reset) reset.addEventListener("click", function () { box.value = ""; if (file) file.value = ""; render(); });
    form.classList.add("calc-ready");
    render();
  }

  function setup(form) {
    if (form.dataset.calc === "rolling-returns") return setupRolling(form);
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
