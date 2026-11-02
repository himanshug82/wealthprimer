---
layout: post
title: "Margin calls and peak margin: how a position gets closed"
seo_title: "Margin calls and peak margin explained"
description: "A margin call is a demand for more money when losses eat your margin. A hypothetical two-day path shows how one arrives and why the peak counts."
image: /assets/og/margin-calls-and-peak-margin.png
date: 2027-02-22 09:00:00 +0530
series: risk
term: "Margin call and peak margin"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign r4 = site.data.risk4 %}
{% assign m = r4.margin %}
{% assign pk = m.peak %}
{% assign src = site.data.risk3.sources %}

## What is a margin call?

In futures and options, you don't pay for the position in full. You deposit **margin**: money the broker and the exchange's clearing corporation hold as a safeguard against your losses. The position is marked to market every day, which means your gains and losses are settled daily instead of at the end. If losses eat into the deposit, or the required margin rises, you are short of margin. A **margin call** is the broker's demand that you add funds. If you don't, the broker can reduce or close your positions, which is how a falling market turns a paper loss into a realised one.

This post describes the mechanics on a hypothetical example. It isn't a suggestion to take or avoid any position. It builds on [leverage and margin]({% post_url 2026-10-11-leverage-and-margin %}) and the [option writing post]({% post_url 2026-11-18-option-writing-and-margin %}), and belongs to the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series.

## The formula

```
Equity            =  funds deposited  +  cumulative profit or loss (marked to market)
Required margin   =  position value  ×  margin %       (the margin % can rise when markets get volatile)
Shortfall         =  max( required margin  −  equity , 0 )
```

Two things can create a shortfall: your **equity** falls (losses), or your **required margin** rises (the exchange raises the margin percentage). For a long position in a fast-falling market, both happen together. (For the regulator's intraday check below, the margin percentage is fixed at the start of the day, so a rise reaches that check through the next day's parameters; a broker can still ask for more sooner.)

## Worked example: a hypothetical two-day path

Everything here is hypothetical: a long position in a contract worth ₹{% assign x = m.contract %}{% include inr.html n=x %} (the "Sample Index" lot used in the other options posts), ₹{% assign x = m.funds %}{% include inr.html n=x %} deposited, and an invented margin percentage that rises as the market falls. These are not an exchange's margin rates.

| | Index move that day | Position value (₹) | Margin % | Required margin (₹) | Equity (₹) | Shortfall (₹) |
|---|---:|---:|---:|---:|---:|---:|
{% for row in m.rows %}| {{ row.label }} | {% assign mv = row.move_pct %}{% include inr.html n=mv %}% | {% assign a = row.position_value %}{% include inr.html n=a %} | {{ row.margin_pct }}% | {% assign b = row.required %}{% include inr.html n=b %} | {% assign c = row.equity %}{% include inr.html n=c %} | {% assign d = row.shortfall %}{% include inr.html n=d %} |
{% endfor %}
Read the table across. The first fall was modest, and the position shrank slightly, but equity fell by the loss and required margin rose because the margin percentage went up. A shortfall appeared at "{{ m.first_shortfall_label | downcase }}". On the second day, the loss and the rising percentage grew the gap further. The broker's call is for the shortfall. How long you have to meet it depends on the broker's terms and the exchange's rules, so check yours.

Notice what the numbers also show: the position's value fell by single-digit percentages, yet equity fell from ₹{% assign x = m.funds %}{% include inr.html n=x %} to ₹{% assign y = m.rows[2].equity %}{% include inr.html n=y %}. That is leverage: a small move in the price is a large move in your equity.

## What "peak margin" adds

You might think margin only matters at the end of the day. Since December 2020, when SEBI's check began (phased in from 25% to 100% of the peak), it doesn't. SEBI's circular SEBI/HO/MRD2/DCAP/CIR/P/2020/127, dated 20 July 2020, requires clearing corporations to send at least four randomly timed intraday snapshots of each client's margin requirement. The broker's shortfall is the higher of two comparisons: end-of-day margin needed against end-of-day margin held, and peak margin needed across the snapshots against peak margin held during the day. That higher shortfall is what attracts the penalty on the broker: 0.5% or 1% of the shortfall a day, depending on its size, and 5% a day if it continues beyond three days (Master Circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181, 30 December 2024, Chapter 4, para 1.1.14). In derivatives, the same chapter (para 1.1.12, restating amendments of 2022 and 2023) bases the requirement on margin parameters fixed at the beginning of the day, so what moves it during the day is mainly your position, not the market's volatility. We didn't establish that nothing later has changed this, so check the current rule with your broker or the exchange.

The idea is easy to show with a hypothetical day:

| | Required margin (₹) | Your funds (₹) |
|---|---:|---:|
| Morning | {% assign x = pk.morning_required %}{% include inr.html n=x %} | {% assign y = pk.funds %}{% include inr.html n=y %} |
| Mid-day: extra positions held at one snapshot, closed before the close | {% assign x = pk.spike_required %}{% include inr.html n=x %} | {% assign y = pk.funds %}{% include inr.html n=y %} |
| Close of the day | {% assign x = pk.close_required %}{% include inr.html n=x %} | {% assign y = pk.funds %}{% include inr.html n=y %} |

By the close, the requirement is back below your funds. If only the end-of-day figure counted, you would have been fine. With the peak test, the mid-day requirement is what your funds were measured against, and the shortfall was real at that moment. That's why a position that looks comfortable at the close can still lead to a penalty on the broker; your broker's terms decide what reaches you.

Margin rules for derivatives sit in Chapter 5 of the same master circular. Paragraph {{ src.upfront_margin.para }} requires upfront margins to be collected before the trade, and from {{ src.upfront_margin.premium_from }} net option premium payable counts too (paragraph {{ src.upfront_margin.premium_para }}, equity derivatives).

## Common mistakes

- **Sizing the deposit for the average requirement.** Margin percentages tend to rise when markets are volatile, which for a long position is often when equity is falling.
- **Assuming a margin call is a polite notice.** It is a demand with a deadline, and the broker can act on the position when it isn't met. The terms are in your broker agreement.
- **Judging a position by the closing figure.** A requirement that rises at a snapshot and falls back can still count.
- **Treating the shortfall as a loss limit.** The shortfall is the amount demanded; the loss on the position can keep growing after it.

## Doing it in Python

```python
contract, funds = 15_00_000, 2_00_000        # hypothetical long position and deposit
path = [(0, 12), (-3, 14), (-4, 17)]         # (index move %, margin % at that day's close)

value, cum = contract, 0.0
for move, margin_pct in path:
    pnl = value * move / 100
    value, cum = value + pnl, cum + pnl
    equity, required = funds + cum, value * margin_pct / 100
    print(f"value {value:,.0f}  equity {equity:,.0f}  required {required:,.0f}  "
          f"shortfall {max(required - equity, 0):,.0f}")
```

**Takeaway:** A margin call arrives when losses cut your equity or the exchange raises the required margin, and for a long position in a falling market both can happen at once. Because the check also looks at the day's peak requirement, a position can fall short even if it looks fine at the close.
