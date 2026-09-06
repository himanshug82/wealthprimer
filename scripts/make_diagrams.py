#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the schematic diagrams for the Jargon / Fundamental Analysis posts.

WHY THIS IS A SCRIPT AND NOT HAND-DRAWN SVG
The Mutual Funds and Technical Analysis series ship charts; the 41 posts of
Jargon + Fundamental Analysis shipped no images at all. These six diagrams fill
the worst of that gap — but every number in them also appears in a post, where
it is rendered from _data/case_study.yml. Hand-drawing them would create two
sources of truth that silently drift. So the numbers are READ from that YAML and
the SVG is emitted. If the case study model ever changes, re-run this.

    python3 scripts/make_diagrams.py

Output: assets/charts/fa-*.svg  (checked in — the Pages build does not run this)

These are SCHEMATICS, not plots of a dataset, which is why they're authored as
SVG rather than through matplotlib like the TA/MF charts. Palette is taken from
assets/logo.svg so the whole site stays one visual system.
"""
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml: pip3 install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "charts")

BLUE       = "#184f95"
BLUE_LIGHT = "#cde2fb"
BLUE_PALE  = "#e8f1fc"
GREEN      = "#2e7d5b"
GREEN_PALE = "#9ec9b5"
RED        = "#b3403a"
RED_PALE   = "#e0b0ad"
INK        = "#0b0b0b"
MUTED      = "#52514e"
RULE       = "#d8d8d8"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"


def inr(n, dec=0):
    """Indian digit grouping: 1234567 -> 12,34,567. Matches _includes/inr.html."""
    neg = n < 0
    n = abs(n)
    s = "%.*f" % (dec, n)
    if "." in s:
        ip, dp = s.split(".")
        dp = "." + dp
    else:
        ip, dp = s, ""
    if len(ip) > 3:
        head, tail = ip[:-3], ip[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        ip = ",".join(parts) + "," + tail
    return ("-" if neg else "") + ip + dp


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start", style=""):
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
            'font-weight="%s" text-anchor="%s"%s>%s</text>'
            % (x, y, FONT, size, fill, weight, anchor,
               ' font-style="italic"' if style == "i" else "", esc(s)))


def box(x, y, w, h, fill, stroke=None, r=5):
    st = ' stroke="%s" stroke-width="1"' % stroke if stroke else ""
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s"%s/>' % (
        x, y, w, h, r, fill, st)


def svg(w, h, title, desc, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
            'width="100%%" role="img" aria-labelledby="t d">\n'
            '<title id="t">%s</title>\n<desc id="d">%s</desc>\n'
            '<rect width="%d" height="%d" fill="#ffffff"/>\n%s\n</svg>\n'
            % (w, h, esc(title), esc(desc), w, h, "\n".join(body)))


def _wrap(s, width):
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) > width and cur:
            lines.append(cur); cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def note(x, y, s):
    return text(x, y, s, size=11, fill=MUTED)


# ---------------------------------------------------------------- diagrams
def balance_sheet(cs, fy="FY25"):
    """Assets on the left, how they were funded on the right. Same total."""
    b = cs["balance_sheet"][fy]
    W, H = 720, 430
    total = b["total_assets"]
    top, bot = 78, 386
    avail = bot - top

    left = [("Net fixed assets", b["net_fixed_assets"], BLUE_LIGHT),
            ("Inventory", b["inventory"], BLUE_PALE),
            ("Receivables", b["receivables"], BLUE_PALE),
            ("Cash", b["cash"], BLUE_PALE)]
    right = [("Equity", b["equity"], GREEN_PALE),
             ("Term loan", b["term_loan"], RED_PALE),
             ("Payables", b["payables"], RED_PALE),
             ("Other current liabilities", b["other_current_liabilities"], RED_PALE)]

    o = [text(W / 2, 30, "The balance sheet identity", 16, INK, "600", "middle"),
         note(W / 2 - 150, 50, "Desi Bites Foods, %s — figures in Rs Lakh" % fy)]
    o[-1] = text(W / 2, 50, "Desi Bites Foods, %s — figures in Rs Lakh" % fy, 11, MUTED, "normal", "middle")
    o.append(text(180, 70, "WHAT IT OWNS (assets)", 11, MUTED, "600", "middle"))
    o.append(text(540, 70, "WHO PAID FOR IT (liabilities + equity)", 11, MUTED, "600", "middle"))

    for col_x, items in ((60, left), (420, right)):
        y = top
        for label, val, colour in items:
            h = avail * val / float(total)
            o.append(box(col_x, y, 240, h - 3, colour, RULE))
            cy = y + (h - 3) / 2
            # thin slices can't take 12px type without spilling over the edge
            fs = 12 if h >= 26 else 10
            o.append(text(col_x + 12, cy + fs * 0.35, label, fs, INK, "500"))
            o.append(text(col_x + 228, cy + fs * 0.35, inr(val), fs, MUTED, "normal", "end"))
            y += h

    o.append('<line x1="360" y1="%d" x2="360" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="4 4"/>' % (top, bot, RULE))
    o.append(text(180, bot + 26, "Total assets  %s" % inr(total), 13, BLUE, "600", "middle"))
    o.append(text(540, bot + 26, "Total funding  %s" % inr(b["total_liab_eq"]), 13, BLUE, "600", "middle"))
    o.append(text(W / 2, bot + 44, "The two sides are equal by construction — that is what “balance” means.",
                  11, MUTED, "normal", "middle"))
    return svg(W, H + 20, "Balance sheet identity",
               "Assets on the left and the equity and liabilities funding them on the right, "
               "drawn to scale for Desi Bites Foods %s. Both sides total %s lakh." % (fy, inr(total)), o)


def income_waterfall(cs, fy="FY25"):
    """Revenue at the top, costs subtracted in order, profit at the bottom."""
    i = cs["income_statement"][fy]
    W, H = 720, 400
    steps = [("Revenue", i["revenue"], "total"),
             ("COGS", -i["cogs"], "cost"),
             ("Gross profit", i["gross_profit"], "sub"),
             ("Operating expenses", -i["opex"], "cost"),
             ("EBITDA", i["ebitda"], "sub"),
             ("Depreciation", -i["depreciation"], "cost"),
             ("EBIT", i["ebit"], "sub"),
             ("Interest", -i["interest"], "cost"),
             ("Tax", -i["tax"], "cost"),
             ("PAT", i["pat"], "total")]
    top, row_h, bar_x, bar_max = 74, 30, 210, 430
    scale = bar_max / float(i["revenue"])

    o = [text(W / 2, 30, "The income statement is a waterfall", 16, INK, "600", "middle"),
         text(W / 2, 50, "Desi Bites Foods, %s — figures in Rs Lakh" % fy, 11, MUTED, "normal", "middle")]
    running = 0
    for n, (label, val, kind) in enumerate(steps):
        y = top + n * row_h
        if kind in ("total", "sub"):
            running = val
            w = max(running * scale, 2)
            colour = BLUE if kind == "total" else BLUE_LIGHT
            o.append(box(bar_x, y, w, 20, colour, RULE if kind == "sub" else None, 3))
            o.append(text(bar_x + w + 8, y + 14, inr(val), 11,
                          INK if kind == "total" else MUTED, "600" if kind == "total" else "normal"))
            o.append(text(bar_x - 10, y + 14, label, 12, INK, "600", "end"))
        else:
            w = max(abs(val) * scale, 2)
            x = bar_x + max(running * scale, 2) - w
            o.append(box(x, y + 3, w, 14, RED_PALE, None, 2))
            o.append(text(bar_x - 10, y + 14, label, 12, MUTED, "normal", "end"))
            o.append(text(x - 8, y + 14, inr(val), 11, RED, "normal", "end"))
            running += val
    o.append(text(W / 2, top + len(steps) * row_h + 26,
                  "Each stop answers a different question. Only the last one is “profit”.",
                  11, MUTED, "normal", "middle"))
    return svg(W, H, "Income statement waterfall",
               "Revenue of %s lakh reduced step by step through COGS, operating expenses, "
               "depreciation, interest and tax down to PAT of %s lakh."
               % (inr(i["revenue"]), inr(i["pat"])), o)


def cash_flow_bridge(cs, fy="FY25"):
    """Opening cash, plus the three activity sections, to closing cash."""
    c = cs["cash_flow"][fy]
    W, H = 720, 380
    items = [("Opening cash", c["opening_cash"], BLUE, None),
             ("Operating (CFO)", c["cfo"], GREEN, "Cash the business itself threw off"),
             ("Investing (CFI)", c["cfi"], RED, "Mostly capex — buying capacity"),
             ("Financing (CFF)", c["cff"], RED, "Debt repaid and dividends paid"),
             ("Closing cash", c["closing_cash"], BLUE, None)]
    base, top_y, max_h = 250, 96, 130
    peak = max(abs(v) for _, v, _, _ in items)
    col_w, gap = 96, 40
    x0 = (W - (len(items) * col_w + (len(items) - 1) * gap)) / 2

    deepest = max((abs(v) / float(peak) * max_h) for _, v, _, _ in items if v < 0)
    label_y = base + deepest + 30
    o = [text(W / 2, 30, "Where the cash actually went", 16, INK, "600", "middle"),
         text(W / 2, 50, "Desi Bites Foods, %s — figures in Rs Lakh" % fy, 11, MUTED, "normal", "middle"),
         '<line x1="30" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1"/>' % (base, W - 30, base, RULE)]
    for n, (label, val, colour, sub) in enumerate(items):
        x = x0 + n * (col_w + gap)
        h = max(abs(val) / float(peak) * max_h, 3)
        y = base - h if val >= 0 else base
        o.append(box(x, y, col_w, h, colour, None, 3))
        o.append(text(x + col_w / 2, y - 8 if val >= 0 else y + h + 16,
                      inr(val), 12, INK, "600", "middle"))
        # One shared baseline for every caption, clear of the deepest bar, so the
        # row reads straight across instead of stair-stepping with the bars.
        o.append(text(x + col_w / 2, label_y, label, 11, INK, "500", "middle"))
        if sub:
            for li, part in enumerate(_wrap(sub, 22)):
                o.append(text(x + col_w / 2, label_y + 15 + li * 11, part, 9, MUTED, "normal", "middle"))
    o.append(text(W / 2, top_y - 18,
                  "Profit was %s lakh. Operating cash was %s lakh. The gap is the whole point of this statement."
                  % (inr(cs["income_statement"][fy]["pat"]), inr(c["cfo"])), 11, MUTED, "normal", "middle"))
    return svg(W, H, "Cash flow bridge",
               "Opening cash of %s lakh, adjusted by operating, investing and financing cash flows, "
               "reaching closing cash of %s lakh." % (inr(c["opening_cash"]), inr(c["closing_cash"])), o)


def cash_conversion_cycle(cs, fy="FY25"):
    """Inventory days + receivable days - payable days = the cash gap."""
    r = cs["ratios"][fy]
    inv, rec, pay, ccc = r["inventory_days"], r["receivable_days"], r["payable_days"], r["ccc"]
    W, H = 720, 330
    ppd = 8.0
    x0, y_op = 60, 130

    o = [text(W / 2, 30, "The cash conversion cycle", 16, INK, "600", "middle"),
         text(W / 2, 50, "Desi Bites Foods, %s — days" % fy, 11, MUTED, "normal", "middle")]
    o.append(text(x0, y_op - 26, "The operating cycle: raw material in → cash back from the customer", 11, MUTED))
    w_inv, w_rec = inv * ppd, rec * ppd
    o.append(box(x0, y_op, w_inv, 30, BLUE_LIGHT, RULE, 3))
    o.append(text(x0 + w_inv / 2, y_op + 19, "Inventory %d d" % inv, 12, INK, "500", "middle"))
    o.append(box(x0 + w_inv, y_op, w_rec, 30, BLUE_PALE, RULE, 3))
    o.append(text(x0 + w_inv + w_rec / 2, y_op + 19, "Receivables %d d" % rec, 12, INK, "500", "middle"))

    y_pay = y_op + 52
    w_pay = pay * ppd
    o.append(box(x0, y_pay, w_pay, 30, GREEN_PALE, RULE, 3))
    o.append(text(x0 + w_pay / 2, y_pay + 19, "Payables %d d" % pay, 12, INK, "500", "middle"))
    o.append(text(x0 + w_pay + 10, y_pay + 19, "← the supplier funds this stretch, free", 11, GREEN))

    y_gap = y_pay + 62
    gx0, gw = x0 + w_pay, ccc * ppd
    o.append(box(gx0, y_gap, gw, 30, "#f6d9a8", "#c99a3f", 3))
    o.append(text(gx0 + gw / 2, y_gap + 19, "%d d" % ccc, 12, INK, "600", "middle"))
    # anchored to the bar's RIGHT edge and sitting above it — at 34 days the bar
    # already ends near x=668, so any trailing label would run off a 720-wide canvas.
    o.append(text(gx0 + gw, y_gap - 9, "the company's own cash is tied up here ↓", 11, INK, "500", "end"))
    for x in (x0, gx0, x0 + w_inv + w_rec):
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>'
                 % (x, y_op, x, y_gap + 30, RULE))
    o.append(text(x0, y_gap + 64, "%d  +  %d  −  %d  =  %d days" % (inv, rec, pay, ccc), 14, BLUE, "600"))
    o.append(text(x0, y_gap + 84,
                  "Shorter is better. Negative means suppliers fund the whole cycle and the company never dips in.",
                  11, MUTED))
    return svg(W, H, "Cash conversion cycle",
               "Inventory days of %d plus receivable days of %d minus payable days of %d gives a cash "
               "conversion cycle of %d days." % (inv, rec, pay, ccc), o)


def dupont_tree(cs, fy="FY25"):
    """ROE split into the three things that actually drive it."""
    d = cs["dupont"][fy]
    W, H = 720, 330
    o = [text(W / 2, 30, "DuPont: one score, three reasons", 16, INK, "600", "middle"),
         text(W / 2, 50, "Desi Bites Foods, %s" % fy, 11, MUTED, "normal", "middle")]
    o.append(box(W / 2 - 90, 74, 180, 52, BLUE, None, 6))
    o.append(text(W / 2, 96, "ROE", 12, "#ffffff", "600", "middle"))
    o.append(text(W / 2, 116, "%.1f%%" % d["roe_reconciled"], 17, "#ffffff", "600", "middle"))

    kids = [("Net margin", "%.2f%%" % d["net_margin"], "How much of each rupee\nof sales it keeps", "Profitability"),
            ("Asset turnover", "%.2f×" % d["asset_turnover"], "Revenue generated per\nrupee of assets", "Efficiency"),
            ("Equity multiplier", "%.2f×" % d["equity_multiplier_avg"], "How far equity is\nlevered up", "Leverage")]
    bw, gap = 190, 25
    x0 = (W - (3 * bw + 2 * gap)) / 2
    for n, (label, val, blurb, tag) in enumerate(kids):
        x = x0 + n * (bw + gap)
        o.append('<path d="M %.1f 126 L %.1f 152 L %.1f 152 L %.1f 176" fill="none" stroke="%s" stroke-width="1.5"/>'
                 % (W / 2, W / 2, x + bw / 2, x + bw / 2, RULE))
        o.append(box(x, 176, bw, 86, BLUE_PALE, RULE, 6))
        o.append(text(x + bw / 2, 196, tag.upper(), 9, MUTED, "600", "middle"))
        o.append(text(x + bw / 2, 216, label, 12, INK, "500", "middle"))
        o.append(text(x + bw / 2, 238, val, 16, BLUE, "600", "middle"))
        for li, line in enumerate(blurb.split("\n")):
            o.append(text(x + bw / 2, 252 + li * 12, line, 9.5, MUTED, "normal", "middle"))
    for n in range(2):
        o.append(text(x0 + bw + gap / 2 + n * (bw + gap), 224, "×", 15, MUTED, "600", "middle"))
    o.append(text(W / 2, 292, "%.2f%%  ×  %.2f  ×  %.2f  =  %.1f%%"
                  % (d["net_margin"], d["asset_turnover"], d["equity_multiplier_avg"], d["roe_reconciled"]),
                  13, INK, "600", "middle"))
    o.append(text(W / 2, 312, "Two companies can reach the same ROE through completely different routes.",
                  11, MUTED, "normal", "middle"))
    return svg(W, H, "DuPont decomposition of ROE",
               "ROE of %.1f percent decomposed into net margin %.2f percent, asset turnover %.2f times and "
               "equity multiplier %.2f times." % (d["roe_reconciled"], d["net_margin"],
                                                  d["asset_turnover"], d["equity_multiplier_avg"]), o)


def dcf_structure(cs):
    """Where a DCF's answer actually comes from — mostly the terminal value."""
    r = cs["dcf"]["result"]
    W, H = 720, 360
    o = [text(W / 2, 30, "What a DCF is actually made of", 16, INK, "600", "middle"),
         text(W / 2, 50, "Desi Bites Foods — figures in Rs Lakh", 11, MUTED, "normal", "middle")]
    ev = r["enterprise_value"]
    bar_x, bar_w, y = 60, 600, 84
    pv_f = r["pv_forecast_fcff"] / float(ev) * bar_w
    pv_t = r["pv_terminal_value"] / float(ev) * bar_w
    o.append(box(bar_x, y, pv_f, 48, BLUE, None, 4))
    o.append(box(bar_x + pv_f, y, pv_t, 48, BLUE_LIGHT, RULE, 4))
    o.append(text(bar_x + pv_f / 2, y + 30, "%.0f%%" % (100 - r["terminal_pct_of_ev"]), 14, "#ffffff", "600", "middle"))
    o.append(text(bar_x + pv_f + pv_t / 2, y + 30, "%.1f%%" % r["terminal_pct_of_ev"], 14, INK, "600", "middle"))
    o.append(text(bar_x, y - 10, "PV of 5 forecast years", 11, BLUE, "600"))
    o.append(text(bar_x + pv_f + 6, y - 10, "PV of terminal value", 11, MUTED, "600"))
    o.append(text(bar_x, y + 68, "%s" % inr(r["pv_forecast_fcff"], 1), 11, MUTED))
    o.append(text(bar_x + pv_f + 6, y + 68, "%s" % inr(r["pv_terminal_value"], 1), 11, MUTED))
    o.append(text(W / 2, y + 96,
                  "%.1f%% of the answer comes from a single assumption about life after year five."
                  % r["terminal_pct_of_ev"], 12, RED, "600", "middle"))

    rows = [("Enterprise value", inr(ev, 1), False),
            ("less net debt (a net cash position)", inr(r["net_debt"], 0), False),
            ("Equity value", inr(r["equity_value"], 1), True),
            ("÷ shares outstanding (lakh)", "%.1f" % r["shares_lakh"], False),
            ("Value per share", "Rs %s" % inr(r["value_per_share"], 2), True)]
    ry = y + 126
    for label, val, strong in rows:
        o.append(text(bar_x, ry, label, 12, INK if strong else MUTED, "600" if strong else "normal"))
        o.append(text(bar_x + bar_w, ry, val, 12, INK if strong else MUTED, "600" if strong else "normal", "end"))
        if strong:
            o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>'
                     % (bar_x, ry + 8, bar_x + bar_w, ry + 8, RULE))
        ry += 26
    o.append(text(W / 2, ry + 6,
                  "Computed on the FICTIONAL case study — never on a listed stock. Illustration of a method only.",
                  10.5, MUTED, "normal", "middle"))
    return svg(W, H, "Composition of a DCF valuation",
               "A bar showing that %.1f percent of enterprise value comes from terminal value, then the "
               "bridge from enterprise value to a per-share figure." % r["terminal_pct_of_ev"], o)


def main():
    cs = yaml.safe_load(open(os.path.join(ROOT, "_data", "case_study.yml")))
    out = {
        "fa-balance-sheet.svg":          balance_sheet(cs),
        "fa-income-waterfall.svg":       income_waterfall(cs),
        "fa-cash-flow-bridge.svg":       cash_flow_bridge(cs),
        "fa-cash-conversion-cycle.svg":  cash_conversion_cycle(cs),
        "fa-dupont-tree.svg":            dupont_tree(cs),
        "fa-dcf-structure.svg":          dcf_structure(cs),
    }
    for name, body in out.items():
        with open(os.path.join(OUT, name), "w") as fh:
            fh.write(body)
        print("  wrote assets/charts/%-32s %5d bytes" % (name, len(body)))


if __name__ == "__main__":
    main()
