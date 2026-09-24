---
layout: post
title: "Reading quarterly results: YoY, QoQ, TTM, and why one quarter proves nothing"
description: "Quarterly results are misread four times a year. YoY vs QoQ, the festive-season trap, trailing twelve months, and what a single quarter can't tell you."
image: /assets/og/reading-quarterly-results.png
date: 2026-11-15 09:00:00 +0530
series: fundamental-analysis
term: "Quarterly results (YoY, QoQ, TTM)"
---

{% assign c2 = site.data.case_study_2 %}
{% assign q = c2.quarterly %}
{% assign q25 = q.FY25 %}
{% assign q26 = q.FY26 %}
{% assign fy25 = site.data.case_study.income_statement.FY25 %}

## Four times a year, misread four times a year

Listed companies in India publish results every quarter, within 45 days of
the quarter's end (60 for the fourth). That's the good news: you don't wait
a year to learn how the business is doing. The bad news is that a quarter
is a short, noisy, seasonal slice of a year, and most of what gets said
about quarterly results on the day they land is a misreading of one kind or
another.

This post uses Desi Bites Foods' first two quarters as a listed company —
Q1 and Q2 of FY26 (April to September 2025) — to show the three
comparisons that matter, the one trap that catches everyone, and why the
honest answer to "how was the quarter?" is usually "ask me in three more."

## First, the shape of the year

Every business has a rhythm. Snacks sell most during {{ q.festive_quarter }}.
Desi Bites' FY25 revenue of ₹{{ fy25.revenue }} lakh didn't arrive in four equal
pieces:

| FY25 | Q1 (Apr–Jun) | Q2 (Jul–Sep) | Q3 (Oct–Dec) | Q4 (Jan–Mar) | Year |
|---|---:|---:|---:|---:|---:|
| Revenue (₹ lakh) | {{ q25.Q1.revenue }} | {{ q25.Q2.revenue }} | {{ q25.Q3.revenue }} | {{ q25.Q4.revenue }} | {{ fy25.revenue }} |
| Share of year | {{ q.seasonality_shares_pct.Q1 }}% | {{ q.seasonality_shares_pct.Q2 }}% | **{{ q.seasonality_shares_pct.Q3 }}%** | {{ q.seasonality_shares_pct.Q4 }}% | 100% |
| EBITDA (₹ lakh) | {{ q25.Q1.ebitda }} | {{ q25.Q2.ebitda }} | {{ q25.Q3.ebitda }} | {{ q25.Q4.ebitda }} | {{ fy25.ebitda }} |
| EBITDA margin | {{ q25.Q1.ebitda_margin }}% | {{ q25.Q2.ebitda_margin }}% | **{{ q25.Q3.ebitda_margin }}%** | {{ q25.Q4.ebitda_margin }}% | 17.0% |

Two things about that table before any comparison is made.

The festive quarter carries {{ q.seasonality_shares_pct.Q3 }}% of the year's revenue and a
visibly higher margin. That margin isn't a sign of better management in
October; it's *operating leverage* — the factory, the sales force and the
rent cost roughly the same every quarter, so when volumes are 36% higher
than Q1, more of each extra rupee falls through to profit.

And every quarter is a bit different from the one before it *for reasons
that have nothing to do with the business getting better or worse*. That
is the whole problem with quarterly numbers, and it's why the choice of
comparison matters so much.

## The three comparisons

```
YoY  (year on year)        = this quarter vs the SAME quarter last year
QoQ  (quarter on quarter)  = this quarter vs the PREVIOUS quarter
TTM  (trailing twelve months) = the last four quarters added together
```

**YoY** removes seasonality, because Q1 is compared with Q1. It's the
default for a seasonal business and the number the company will lead with
when it's good.

**QoQ** removes nothing — it compares a lean quarter with a fat one — but
it tells you what happened *recently*, which YoY can't. A business that
grew 20% YoY but fell 10% QoQ against its usual seasonal pattern has a
recent problem that the YoY figure is still hiding.

**TTM** smooths all of it into a rolling year, and is the right denominator
for any ratio that needs a full year — [P/E]({% post_url 2026-09-24-price-to-earnings %})
on a quarter's earnings times four is a guess; on trailing twelve months
it's a number.

## Desi Bites, Q1 and Q2 FY26

| | Q1 FY26 | Q2 FY26 |
|---|---:|---:|
| Revenue (₹ lakh) | {{ q26.Q1.revenue }} | {{ q26.Q2.revenue }} |
| **YoY** growth | **+{{ q26.Q1.yoy_revenue_growth }}%** | **+{{ q26.Q2.yoy_revenue_growth }}%** |
| **QoQ** growth | +{{ q26.Q1.qoq_revenue_growth }}% (vs Q4 FY25) | +{{ q26.Q2.qoq_revenue_growth }}% (vs Q1 FY26) |
| EBITDA (₹ lakh) | {{ q26.Q1.ebitda }} | {{ q26.Q2.ebitda }} |
| EBITDA margin | {{ q26.Q1.ebitda_margin }}% | {{ q26.Q2.ebitda_margin }}% |
| EBITDA YoY | +{{ q26.Q1.yoy_ebitda_growth }}% | +{{ q26.Q2.yoy_ebitda_growth }}% |

Read the YoY row and the story is simple and consistent: the existing
business is growing at about 18% a year, with margins a touch better than
the same quarters last year. That is, as it happens, exactly the FY26
growth the [DCF]({% post_url 2026-10-04-forecasting-free-cash-flow %}) assumed —
two quarters in, the forecast is on track.

Now read the QoQ row and notice how little it tells you on its own. Q1 was
up {{ q26.Q1.qoq_revenue_growth }}% on Q4; Q2 up {{ q26.Q2.qoq_revenue_growth }}% on Q1. Is that good? You can't know
without the seasonal template: Q1 is normally the leanest quarter, carrying
{{ q.seasonality_shares_pct.Q1 }}% of the year against Q4's {{ q.seasonality_shares_pct.Q4 }}%, so revenue *rising* from Q4 into
Q1 is genuinely strong — it means the underlying growth outran the seasonal
dip. QoQ is only readable against the seasonal template.

## The trap

Here's the comparison a headline writer in a hurry makes:

> Desi Bites' Q1 FY26 revenue of ₹{{ q26.Q1.revenue }} lakh is **{{ q.q1fy26_vs_q3fy25_pct }}%** below its Q3 FY25 figure of ₹{{ q25.Q3.revenue }} lakh.

Every word of that is accurate. It's also meaningless: it compares the
leanest quarter of the year with the festive one. A business growing 18% a
year *will* show a double-digit fall from Q3 to Q1, every year, forever.
Anyone who sells on that number has confused a calendar with a trend.

The reverse trap exists too. A company whose Q3 is up 40% on Q2 is
usually just a company with a festive season. Growth is measured against
the same quarter a year ago, or not at all.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

An ice-cream shop sells a lot in May and very little in December. If the
owner says "December sales crashed 70% compared with May," nobody's
worried. Of course they did. It's December.

The useful question is: "How did this December compare with *last*
December?" If it's up, the shop is doing better. That's year-on-year.

"How did December compare with November?" tells you if something changed
*just now* — but only if you already know that December is normally a bit
lower than November anyway.

</details>

## TTM: turning quarters back into a year

After Q2 FY26, the last four quarters are Q3 FY25, Q4 FY25, Q1 FY26 and
Q2 FY26:

| Trailing twelve months to 30 September 2025 | ₹ lakh |
|---|---:|
| Revenue | {{ q.ttm_after_q2_fy26.revenue }} |
| EBITDA | {{ q.ttm_after_q2_fy26.ebitda }} |
| Revenue vs full-year FY25 | +{{ q.ttm_after_q2_fy26.revenue_growth_vs_fy25 }}% |

Careful with that +{{ q.ttm_after_q2_fy26.revenue_growth_vs_fy25 }}%, though — it isn't a growth rate. The TTM and
FY25 share two quarters (Q3 and Q4 FY25), so only half of each total has
changed, and the comparison mechanically shows about half the real growth:
the two new quarters grew {{ q.FY26.Q1.yoy_revenue_growth }}% YoY, the two shared ones by definition
0%. TTM growth means something only against the *previous* TTM, the twelve
months to 30 September 2024.

Where TTM earns its place is as a *level*. It has two new quarters in it and
two old ones, so it moves slowly and is never seasonal, which makes it the
right figure for ratios like P/E. When you see a [P/E]({% post_url 2026-09-24-price-to-earnings %}) quoted
mid-year, ask whether the E is last financial year's, this year's
annualised quarter, or TTM. They can differ by a lot, and only the last is
both current and complete.

## What one quarter can tell you

Not nothing. A quarter is where you first see:

- **A change in direction.** If Q2 YoY growth had been 6% after five
  quarters of 18%, that's information — not proof, but the first data
  point of a trend, and worth watching for in Q3.
- **Margin pressure.** Input costs (edible oil, flour) move faster than
  quarterly prices. Gross margin down 200 basis points in a quarter, with
  the MD&A citing raw material, is the kind of thing that shows up
  quarterly and resolves — or doesn't — over the next two.
- **A one-off.** Exceptional items, a fire, a plant shutdown. Quarterly
  results are where you learn it happened; the annual report is where you
  learn what it cost.
- **Acquisitions changing the base.** Desi Bites bought a regional brand
  on 1 October 2025. From Q3 FY26 onwards, its reported revenue includes
  the acquired sales (₹{{ q.acquired_revenue_by_quarter.Q3 }} lakh in Q3, ₹{{ q.acquired_revenue_by_quarter.Q4 }} lakh in Q4). YoY growth
  from Q3 will look spectacular and will be partly bought. Companies that
  do this are supposed to disclose *organic* growth separately; when they
  don't, compute it.

What a quarter can't tell you is whether any of the above is a trend. Three
quarters can start to. Twelve can.

## Common mistakes

- **Comparing a quarter with the previous quarter in a seasonal business.**
  Use YoY. Use QoQ only against the seasonal template.
- **Annualising one quarter.** Q3 times four overstates a snacks
  company's year by roughly 20%; Q1 times four understates it. Use TTM.
- **Reading "record quarter" as news.** A growing seasonal business sets
  a record every Q3. The question is the YoY rate, not the level.
- **Missing the base change after an acquisition.** Reported growth and
  organic growth diverge from the first post-deal quarter. Find the
  organic number or work it out.
- **Treating the quarter's margin as the business's margin.** Q3 margins
  are higher than Q1 margins for reasons of volume, not competence.
  Compare margins YoY, or annually.
- **Reacting on the day.** Results land, the stock moves, the commentary
  follows the stock. None of that is analysis. The number you need is the
  one that will be visible in three quarters' time.

**Takeaway:** A quarter is a short, seasonal, noisy slice of a year. Compare
it with the same quarter last year (YoY), read quarter-on-quarter only
against the seasonal pattern, and use the trailing twelve months for
anything that needs a full year. Desi Bites' Q1 FY26 was {{ q.q1fy26_vs_q3fy25_pct }}% below its
festive Q3 and 18% above last year's Q1 — and only one of those numbers
means anything.
