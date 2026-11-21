---
layout: post
title: "Reading a debt fund's portfolio: ratings, maturity and yield"
seo_title: "How to read a debt fund portfolio: rating mix and maturity"
description: "A debt fund's monthly portfolio shows what it lends to, for how long and at what rating. How to read the rating mix, average maturity, duration and yield."
image: /assets/og/reading-a-debt-fund-portfolio.png
date: 2027-02-06 09:00:00 +0530
series: mutual-funds
term: "Debt fund portfolio (rating mix and maturity)"
---

{% assign d = site.data.mf5.debt_portfolio %}

## What the portfolio tells you

A debt fund is a pile of loans: government bonds, company bonds,
certificates of deposit, treasury bills. Its published portfolio lists each
one, and four numbers summarise them: the **rating mix** (how
creditworthy the borrowers are), the **average maturity** (how long until
the money comes back), the **modified duration** (how much prices move when
rates move) and the **yield to maturity** (what the holdings would earn if
held to the end, before costs).

Those four numbers answer most of what the [riskometer]({% post_url 2026-10-22-the-riskometer %})
compresses into one dial. This post reads a made-up portfolio line by line.
It's part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}),
and builds on [how debt funds work]({% post_url 2026-10-12-debt-funds-explained %}).

## The formulas

Each summary number is a weighted average, using each holding's share of the
fund as its weight. YTM is the holding's yield to maturity; the formula for
portfolio yield is the usual convention, and only approximates the
portfolio's true yield.

```
Average maturity    =  Σ (weight × years until the holding matures)
Portfolio yield     ≈  Σ (weight × the holding's YTM)
Modified duration   =  Σ (weight × the holding's modified duration)

Price change if rates move  ≈  − modified duration × change in yield
```

YTM is yield to maturity ([the YTM post]({% post_url 2026-10-05-yield-to-maturity %})),
and [modified duration]({% post_url 2026-10-06-modified-duration %}) is the
sensitivity of price to yield. Ratings come from credit rating agencies
([the credit ratings post]({% post_url 2026-12-30-credit-ratings-explained %})):
AAA is the highest for long-term debt, A1+ the highest for short-term, and
"sovereign" means government debt, which isn't rated the same way.

## Worked example: a made-up portfolio

A hypothetical fund. The holdings, weights, ratings and yields are invented
to show the method, not taken from any real fund. PSU is a public sector
undertaking; NCD a non-convertible debenture; NBFC a non-banking financial
company.

| Holding | Rating | Weight | Years to maturity | YTM | Modified duration |
|---|---|---:|---:|---:|---:|
{% for h in d.rows -%}
| {{ h.name }} | {{ h.rating }} | {{ h.weight }}% | {{ h.maturity }} | {{ h.ytm }}% | {{ h.mod_dur }} |
{% endfor %}

**Step 1: the rating mix.**

| Bucket | Share of the fund |
|---|---:|
{% for b in d.mix -%}
| {{ b.bucket }} | {{ b.pct }}% |
{% endfor %}

**Step 2: the summary numbers.** Weighting each column by the holding's
share: average maturity {{ d.avg_maturity }} years, portfolio yield
{{ d.ytm }}%, modified duration {{ d.mod_dur }}.

**Step 3: what they mean together.**

1. **Rate risk:** with a modified duration of {{ d.mod_dur }}, a
   {{ d.rate_move_bp }} basis point (one percentage point) rise in yields
   would cut the portfolio's value by roughly
   {{ d.price_change_pct | abs }}%, and a similar fall would add about as
   much. That's the swing the fund carries for its rate exposure.
2. **Credit risk:** {{ d.below_aaa_pct }}% of the fund is in bonds rated
   below AAA. Those carry the higher yields in the table, which is where part
   of the portfolio's {{ d.ytm }}% comes from. A downgrade or default in that
   slice is what credit risk means in practice.
3. **Yield is not return.** The {{ d.ytm }}% is what today's holdings would
   earn if held to maturity with no defaults, before the fund's expenses.
   The fund's actual return also depends on rate moves, reinvestment and
   costs.

## Common mistakes

1. **Reading the yield as the return you'll get.** The portfolio yield is
   before expenses and assumes no defaults and no rate moves. A fund's
   factsheet yield is a starting point, not a forecast.
2. **Looking only at the average rating.** A fund can be mostly AAA and still
   hold a slice of lower-rated paper that drives much of its extra yield.
   Read the full list, not just the headline mix.
3. **Confusing average maturity with duration.** Maturity is when the money
   comes back; duration measures price sensitivity. For bonds that pay
   coupons, duration is shorter than maturity. Factsheets often also show
   Macaulay duration, the measure SEBI's debt category limits use; modified
   duration is roughly Macaulay duration divided by (1 + yield).
4. **Comparing funds in different categories.** A short-duration fund and a
   gilt fund are built to carry different risks. Compare a fund's numbers with
   others in its own category, as the
   [fund categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %})
   explains.

**Takeaway:** A debt fund's portfolio comes down to four numbers: rating mix,
average maturity, modified duration and yield. Together they show how much
credit risk the fund takes, how much rate risk it carries, and what its
holdings would earn before costs if nothing went wrong.
