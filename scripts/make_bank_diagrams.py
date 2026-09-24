#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Schematics for the "banks and NBFCs" module (BANK-1..6), read from
_data/real_bank.yml so the numbers in the pictures are the numbers in the posts.

    python3 scripts/derive_bank.py        # first, if reported figures changed
    python3 scripts/make_bank_diagrams.py

Output: assets/charts/bank-*.svg (checked in — the Pages build does not run this)

Same approach and palette as scripts/make_diagrams.py: hand-authored SVG
schematics generated from YAML, not matplotlib plots.
"""
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml (use the project venv)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "charts")

BLUE, BLUE_LIGHT, BLUE_PALE = "#184f95", "#cde2fb", "#e8f1fc"
GREEN, GREEN_PALE = "#2e7d5b", "#9ec9b5"
RED, RED_PALE = "#b3403a", "#e0b0ad"
INK, MUTED, RULE = "#0b0b0b", "#52514e", "#d8d8d8"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"


def inr(n, dec=0):
    neg = n < 0
    n = abs(n)
    s = "%.*f" % (dec, n)
    ip, dp = (s.split(".") + [""])[:2]
    dp = "." + dp if dp else ""
    if len(ip) > 3:
        head, tail = ip[:-3], ip[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        ip = ",".join(parts + [tail])
    return ("-" if neg else "") + ip + dp


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
            'font-weight="%s" text-anchor="%s">%s</text>' % (x, y, FONT, size, fill, weight, anchor, esc(s)))


def box(x, y, w, h, fill, stroke=None, r=5):
    st = ' stroke="%s" stroke-width="1.2"' % stroke if stroke else ""
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s"%s/>' % (x, y, w, h, r, fill, st)


def svg(w, h, title, desc, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" '
            'aria-labelledby="t d">\n<title id="t">%s</title>\n<desc id="d">%s</desc>\n'
            '<rect width="%d" height="%d" fill="#ffffff"/>\n%s\n</svg>\n' % (w, h, w, h, esc(title), esc(desc), w, h, body))


def note(x, y, s):
    return text(x, y, s, size=11, fill=MUTED)


def bank_pnl_waterfall(b):
    """BANK-1: how a bank's P&L is built. Bars in ₹ thousand crore."""
    f = b["reported"]["FY25"]
    steps = [
        ("Interest earned", f["interest_earned"], BLUE),
        ("− Interest expended", -f["interest_expended"], RED_PALE),
        ("= Net interest income", f["net_interest_income"], BLUE_LIGHT),
        ("+ Other income", f["other_income"], GREEN_PALE),
        ("− Operating expenses", -f["operating_expenses"], RED_PALE),
        ("= Pre-provision profit", f["pre_provision_operating_profit"], BLUE_LIGHT),
        ("− Provisions", -f["provisions_and_contingencies"], RED_PALE),
        ("− Tax", -f["tax"], RED_PALE),
        ("= Profit after tax", f["pat"], GREEN),
    ]
    W, H = 760, 400
    left, top, plot_h = 40, 40, 260
    scale = plot_h / f["interest_earned"]
    base = top + plot_h
    bw, gap = 62, 16
    o = [text(left, 24, "HDFC Bank FY25: how a bank's profit is built (₹ crore, standalone)", 14, weight="600")]
    running = 0.0
    x = left
    for label, val, col in steps:
        is_total = label.startswith("=")
        if is_total:
            y0, y1 = base - val * scale, base
            running = val
        else:
            if val >= 0:
                y0, y1 = base - (running + val) * scale, base - running * scale
            else:
                y0, y1 = base - running * scale, base - (running + val) * scale
            running += val
        o.append(box(x, y0, bw, max(y1 - y0, 1.5), col, stroke=BLUE if is_total else None, r=3))
        o.append(text(x + bw / 2, y0 - 6, inr(abs(val)), 10.5, anchor="middle", fill=INK))
        for i, part in enumerate(label.replace("= ", "").replace("− ", "−").replace("+ ", "+").split(" ", 1)):
            o.append(text(x + bw / 2, base + 16 + 12 * i, part, 10, anchor="middle", fill=MUTED))
        x += bw + gap
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (left, base, W - 30, base, RULE))
    o.append(note(left, H - 34, "No 'revenue', no 'COGS', no EBITDA: interest expended is the bank's raw-material cost, provisions are"))
    o.append(note(left, H - 20, "the cost of loans going bad. Source: results for the year ended 31 Mar 2025 (Form 6-K exhibit, 21 Apr 2025)."))
    return svg(W, H, "How a bank's P&L is built",
               "Waterfall from interest earned to profit after tax for HDFC Bank FY25, standalone.", "\n".join(o))


def bank_balance_sheet(b):
    """BANK-1/BANK-3: the balance sheet IS the business. Two stacked columns."""
    f = b["reported"]["FY25"]
    liabs = [("Deposits", f["deposits"], BLUE), ("Borrowings", f["borrowings"], BLUE_LIGHT),
             ("Other liabilities", f["other_liabilities"], BLUE_PALE), ("Shareholders' equity", f["shareholders_equity"], GREEN)]
    assets = [("Advances (loans)", f["advances"], BLUE), ("Investments", f["investments"], BLUE_LIGHT),
              ("Cash & RBI balances", f["cash_with_rbi"], BLUE_PALE),
              ("Other assets", f["total_assets"] - f["advances"] - f["investments"] - f["cash_with_rbi"], "#f1f1f1")]
    W, H = 720, 420
    top, ph = 50, 300
    scale = ph / f["total_assets"]
    o = [text(30, 24, "HDFC Bank, 31 March 2025: where the money comes from, and where it sits (₹ crore)", 14, weight="600")]
    for col_x, title, items in ((60, "Liabilities: funding", liabs), (400, "Assets: what it's lent out as", assets)):
        o.append(text(col_x, top - 10, title, 12, weight="600", fill=MUTED))
        y = top
        for label, val, colr in items:
            h = val * scale
            o.append(box(col_x, y, 250, h, colr, stroke="#ffffff", r=2))
            fill = "#ffffff" if colr in (BLUE, GREEN) else INK
            if h > 22:
                o.append(text(col_x + 8, y + h / 2 + 4, "%s  %s" % (label, inr(val)), 11, fill=fill))
            else:
                o.append(text(col_x + 258, y + h / 2 + 4, "%s  %s" % (label, inr(val)), 10, fill=MUTED))
            y += h
    eq_pct = b["reported"]["FY25"]["equity_to_assets_pct"]
    o.append(note(30, H - 40, "Equity is %.1f%% of the balance sheet; deposits are %s%% of funding. A 'debt-to-equity' of %.0f would be alarming for a" % (
        eq_pct, b["reported"]["FY25"]["deposits_share_of_funding_pct"], (f["deposits"] + f["borrowings"]) / f["shareholders_equity"])))
    o.append(note(30, H - 26, "factory and is simply what a bank is. Source: results for the year ended 31 Mar 2025 (Form 6-K exhibit, 21 Apr 2025)."))
    return svg(W, H, "A bank's balance sheet", "Stacked funding and asset columns for HDFC Bank at 31 March 2025.", "\n".join(o))


def npa_lifecycle(b):
    """BANK-4: overdue → NPA → provisions → net NPA, with the FY25 numbers."""
    f = b["reported"]["FY25"]
    W, H = 760, 330
    o = [text(30, 24, "From a missed EMI to net NPA (HDFC Bank, 31 March 2025, ₹ crore)", 14, weight="600")]
    stages = [("Standard", "paying on time", BLUE_PALE), ("SMA-0/1/2", "1–90 days overdue", BLUE_LIGHT),
              ("Sub-standard", "NPA ≤ 12 months", RED_PALE), ("Doubtful", "NPA > 12 months", RED_PALE),
              ("Loss", "unrecoverable", RED)]
    x = 30
    for i, (a, bb, c) in enumerate(stages):
        o.append(box(x, 50, 130, 54, c, r=6))
        o.append(text(x + 65, 72, a, 12, weight="600", anchor="middle", fill="#ffffff" if c == RED else INK))
        o.append(text(x + 65, 90, bb, 10, anchor="middle", fill="#ffffff" if c == RED else MUTED))
        if i < len(stages) - 1:
            o.append('<path d="M %.1f 77 L %.1f 77" stroke="%s" stroke-width="1.5" marker-end="url(#a)"/>' % (x + 132, x + 144, MUTED))
        x += 146
    o.append('<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
             '<path d="M0,0 L6,3 L0,6 z" fill="%s"/></marker></defs>' % MUTED)
    o.append('<line x1="30" y1="122" x2="730" y2="122" stroke="%s"/>' % RULE)
    # bars: gross NPA, provisions held, net NPA
    top, ph = 150, 110
    scale = ph / f["gross_npa"]
    bars = [("Gross NPA", f["gross_npa"], RED_PALE), ("− Provisions held", f["npa_provisions_held"], GREEN_PALE),
            ("= Net NPA", f["net_npa"], RED)]
    x = 60
    for label, val, c in bars:
        h = val * scale
        o.append(box(x, top + ph - h, 120, h, c, r=3))
        o.append(text(x + 60, top + ph - h - 6, inr(val), 11, anchor="middle"))
        o.append(text(x + 60, top + ph + 16, label, 11, anchor="middle", fill=MUTED))
        x += 160
    o.append(text(560, top + 30, "Gross NPA  %.2f%% of advances" % f["gross_npa_pct_reported"], 12, weight="600"))
    o.append(text(560, top + 52, "Net NPA    %.2f%% of net advances" % f["net_npa_pct_reported"], 12, weight="600"))
    o.append(text(560, top + 74, "Provision coverage  %.1f%%" % f["provision_coverage_pct"], 12, weight="600"))
    o.append(note(560, top + 96, "= provisions held ÷ gross NPA"))
    o.append(note(30, H - 26, "Net NPA is what is left after the bank's own provisioning judgement — which is why two banks with the same gross NPA can report different net NPA."))
    return svg(W, H, "NPA lifecycle", "Stages from standard asset to loss asset, and gross NPA less provisions equals net NPA for HDFC Bank FY25.", "\n".join(o))


def capital_stack(b):
    """BANK-5: CAR vs the 11.7% floor, in percentage points of RWA."""
    f = b["reported"]["FY25"]
    m = b["regulatory_minimum"]
    W, H = 720, 360
    o = [text(30, 24, "Capital adequacy: what the 19.55% is measured against (HDFC Bank, 31 March 2025)", 14, weight="600")]
    top, ph, x0 = 50, 240, 90
    scale = ph / 20.0
    base = top + ph
    # regulatory stack
    stack = [("Minimum CRAR", m["crar"], BLUE), ("Capital conservation buffer", m["ccb"], BLUE_LIGHT), ("D-SIB surcharge", m["dsib_surcharge"], BLUE_PALE)]
    y = base
    for label, v, c in stack:
        h = v * scale
        y -= h
        o.append(box(x0, y, 150, h, c, stroke="#ffffff", r=2))
        o.append(text(x0 + 158, y + h / 2 + 4, "%s  %.1f%%" % (label, v), 11, fill=MUTED))
    o.append(text(x0 + 75, y - 8, "Required: %.1f%%" % m["total"], 12, weight="600", anchor="middle"))
    # bank's stack
    x1 = 430
    tiers = [("CET1", f["cet1_pct"], GREEN), ("Additional Tier 1", f["tier1_pct"] - f["cet1_pct"], GREEN_PALE), ("Tier 2", f["car_pct"] - f["tier1_pct"], BLUE_LIGHT)]
    y = base
    for label, v, c in tiers:
        h = v * scale
        y -= h
        o.append(box(x1, y, 150, h, c, stroke="#ffffff", r=2))
        o.append(text(x1 + 158, y + h / 2 + 4, "%s  %.1f%%" % (label, v), 11, fill=MUTED))
    o.append(text(x1 + 75, y - 8, "Held: %.2f%%" % f["car_pct"], 12, weight="600", anchor="middle"))
    # dotted floor line across
    yf = base - m["total"] * scale
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-dasharray="5,4"/>' % (x0 - 20, yf, x1 + 300, yf, RED))
    o.append(text(x1 + 305, yf + 4, "floor", 10, fill=RED))
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s"/>' % (x0 - 20, base, W - 30, base, RULE))
    o.append(note(30, H - 40, "Both stacks are percentages of risk-weighted assets (₹%s crore), not of the ₹%s crore balance sheet." % (
        inr(b["capital"]["rwa"]), inr(f["total_assets"]))))
    o.append(note(30, H - 26, "Headroom above the floor: %.2f points ≈ ₹%s crore. Source: results for the year ended 31 Mar 2025 (Form 6-K exhibit)." % (
        b["capital"]["headroom_pct_points"], inr(b["capital"]["headroom_rupees"]))))
    return svg(W, H, "Capital adequacy stack", "Regulatory minimum stack versus HDFC Bank's CET1, AT1 and Tier 2 capital ratios at 31 March 2025.", "\n".join(o))


def main():
    with open(os.path.join(ROOT, "_data", "real_bank.yml"), encoding="utf-8") as fh:
        b = yaml.safe_load(fh)
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("bank-pnl-waterfall", bank_pnl_waterfall), ("bank-balance-sheet", bank_balance_sheet),
                     ("bank-npa-lifecycle", npa_lifecycle), ("bank-capital-stack", capital_stack)):
        p = os.path.join(OUT, name + ".svg")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(fn(b))
        print("wrote", p)


if __name__ == "__main__":
    main()
