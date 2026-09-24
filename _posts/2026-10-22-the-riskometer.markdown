---
layout: post
title: "The riskometer: how SEBI's risk dial is scored, and what it can't see"
description: "SEBI's riskometer scores every fund monthly on six levels. How the score is computed, worked through, and why nearly every equity fund lands on Very High."
image: /assets/og/the-riskometer.png
date: 2026-10-22 09:00:00 +0530
series: mutual-funds
term: "Riskometer"
---

{% assign m = site.data.mf3 %}
{% assign k = m.riskometer %}
{% assign r = m.reg %}
{% assign pa = k.ports[0] %}
{% assign pb = k.ports[1] %}
{% assign pc = k.ports[2] %}
{% assign d = k.debt %}

## The dial on every fund document

Every Indian mutual fund's factsheet, application form and advertisement
carries a semicircular dial with a needle — the **riskometer**. It sorts each
scheme into one of six levels: Low, Low to Moderate, Moderate, Moderately
High, High, Very High.

It's easy to read the dial as SEBI's verdict on how risky a fund is. It's
something narrower: a score computed each month from a checklist of the
portfolio's characteristics, using a formula published by SEBI (the
Securities and Exchange Board of India). Once you know
the formula, you know both what the dial says and what it structurally
can't.

The rules: SEBI's circular {{ k.origin_circular }}, now in paragraph 6.16 and
Annexure 10 of its [Master Circular for Mutual Funds]({{ k.master_circular_url }})
({{ r.mc26.date | date: "%-d %B %Y" }}). The riskometer is evaluated
**monthly**, published with the portfolio on the fund house's website and that of AMFI
(the Association of Mutual Funds in India) within {{ k.disclosure_days }} calendar days of month-end, and any
change must be sent to unitholders by email or SMS. Funds must also disclose,
every year, how many times each scheme's level changed. A change in the
riskometer is expressly *not* a change in the scheme's fundamental
attributes (paragraph 6.16.4), so it doesn't give you a penalty-free exit.

## The formula

Every holding gets a score on a few parameters; each parameter is averaged
across the portfolio by weight; the averages are combined into one **risk
value**; the risk value maps to a level.

**Equity** — three parameters per stock:

| Parameter | Score |
|---|---|
| Market cap (AMFI's list) | Large cap 5 · Mid cap 7 · Small cap 9 |
| The stock's own daily price volatility, past two years | ≤ 1%: 5 · above 1%: 6 |
| Average impact cost (a measure of how much buying moves the price) | ≤ 1%: 5 · 1–2%: 7 · above 2%: 9 |

```
Equity risk value = average of (weighted market-cap score,
                                weighted volatility score,
                                weighted impact-cost score)
```

**Debt** — credit rating (government securities and AAA score 1, stepping
up to 12 for below investment grade), interest-rate risk from the portfolio's
Macaulay duration (1 for six months or less, up to 6 for more than four years),
and a liquidity score (1 for government securities and TREPS — tri-party
repos, overnight lending secured by government bonds — rising for
lower ratings, unlisted paper and special structures):

```
Debt risk value = average of (credit, interest-rate, liquidity scores)
                  — or the liquidity score alone, if it is higher than that average
```

Cash scores 1. Hedged positions (a share plus the future sold against it)
are left out entirely, which helps explain why an arbitrage fund scores low. Mixed
funds add up the weighted parts. Then:

| Risk value | Level |
|---|---|{% for l in k.levels %}
| {{ l.value }} | {{ l.level }} |{% endfor %}

## Worked example: three equity funds and a debt fund

All four portfolios are **hypothetical**, and each equity one is fully
invested (no cash), which keeps the arithmetic unambiguous.

**Fund A** — 100% in large caps, every one with daily volatility of
{{ pa.holdings[0].vol_pct }}% and tiny impact cost.

1. Market cap: 1.00 × 5 = {{ pa.mcap }}
2. Volatility: 1.00 × 5 = {{ pa.volatility }}
3. Impact cost: 1.00 × 5 = {{ pa.impact }}
4. Risk value = {{ pa.value }} → **{{ pa.level }}**

**Fund B** — the same, except 10% of the fund sits in large caps whose daily
volatility is {{ pb.holdings[1].vol_pct }}% instead of {{ pb.holdings[0].vol_pct }}%.

1. Market cap: {{ pb.mcap }} (still all large caps)
2. Volatility: 0.90 × 5 + 0.10 × 6 = {{ pb.volatility }}
3. Impact cost: {{ pb.impact }}
4. Risk value = ({{ pb.mcap }} + {{ pb.volatility }} + {{ pb.impact }}) ÷ 3 = {{ pb.value }} → **{{ pb.level }}**

**Fund C** — {{ pc.holdings[0].weight_pct }}% large caps, {{ pc.holdings[1].weight_pct }}% mid caps, {{ pc.holdings[2].weight_pct }}% small caps, all with daily
volatility above 1%, and the small caps harder to trade.

1. Market cap: 0.40 × 5 + 0.35 × 7 + 0.25 × 9 = {{ pc.mcap }}
2. Volatility: every holding above 1% → {{ pc.volatility }}
3. Impact cost: 0.75 × 5 + 0.25 × 7 = {{ pc.impact }}
4. Risk value = {{ pc.value }} → **{{ pc.level }}**

Look at what just happened. Fund A and Fund B are nearly identical portfolios
and sit on *different* levels. Fund B and Fund C are very different portfolios
— one all large caps, one a quarter in small caps — and sit on the *same*
level.

The reason is the floor. The lowest score an equity holding can get on every
parameter is {{ k.min_equity_value }}, so a fully invested equity fund can't score below
{{ k.min_equity_value }} — the top of "High" — and a single holding that scores above {{ k.min_equity_value }} on
anything (a mid cap, a stock with daily volatility above 1%, a thinly traded
share) tips it into "Very High". For scale, the Nifty 50 index fund used in
this series had daily volatility of {{ k.index_fund_daily_vol_2y_pct }}% between 1 April 2024 and 31 March 2026
— and that's a diversified index. Individual stocks swing more than the
index that contains them, and the riskometer scores **each stock's own
volatility**, not the portfolio's. In our reading of this arithmetic, that's
why almost every equity fund's needle points to Very High.

**Debt fund** — {{ d.rows[0].weight_pct }}% government securities, T-bills and TREPS;
{{ d.rows[1].weight_pct }}% listed AAA bonds; {{ d.rows[2].weight_pct }}% listed AA bonds;
portfolio Macaulay duration {{ d.md_years }} years.

1. Credit: 0.4 × 1 + 0.4 × 1 + 0.2 × 3 = {{ d.credit }}
2. Interest rate (duration over 2 and up to 3 years): {{ d.interest_rate }}
3. Liquidity: 0.4 × 1 + 0.4 × 2 + 0.2 × 4 = {{ d.liquidity }}
4. Average = {{ d.average }}; liquidity ({{ d.liquidity }}) isn't higher, so the risk
   value is {{ d.average }} → **{{ d.level }}**

{% assign ds = k.debt_short %}Here the dial does useful work. Keep the same bonds but cut the portfolio's
duration to {{ ds.md_years }} years, and the interest-rate score drops to {{ ds.interest_rate }}. The average
falls to {{ ds.average }} — but now the liquidity score ({{ ds.liquidity }}) is higher than the
average, so the liquidity rule sets the risk value at {{ ds.value }}, and the level
drops to **{{ ds.level }}**. Debt funds spread across
the six levels in a way equity funds can't.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a spiciness meter for curries that only checks each ingredient on its
own. A mild chilli scores 5. A hot chilli scores 6. Anything with 5 or less is
"Hot"; anything over 5 is "Very Hot".

Every curry in the equity kitchen is made of chillies. One slightly-hot
chilli and the curry is "Very Hot". A curry made *entirely* of the hottest
chillies in the shop is also "Very Hot". The meter can't tell those two
apart.

And it never actually tastes the curry — it just reads the list of
ingredients. Mixing chillies with yoghurt might make the curry milder to eat,
but the meter only sees the chillies.

</details>

## What the riskometer does and doesn't tell you

**It does tell you** what kind of assets a fund holds this month, scored the
same way for every fund. Its movements are informative: a fund whose level
rose over the year changed its portfolio. And for debt funds it separates
very short, top-rated portfolios from long or lower-rated ones. Debt funds
also carry a separate **potential risk class** grid (paragraph 6.18, from
circular {{ k.prc_circular }}) showing the *maximum* duration and credit
risk the scheme may take — the most a fund can do, not what it holds today.
(That grid scores credit the opposite way round — higher numbers mean safer
paper — so don't mix the two scales up.)

**It doesn't tell you**:

- **How much the fund could fall.** No drawdown enters the formula. The
  aggressive hybrid fund in the
  [hybrid funds post]({% post_url 2026-10-18-hybrid-funds %}) fell nearly half
  its value in 2008; the index fund fell more. The dial for a fully invested
  equity fund can't express the difference between a 30% fall and a 60% one.
- **Anything about diversification.** Scoring each stock's own volatility and
  averaging means fifty stocks score the same as five of the same kind. The
  [diversification post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %})
  explained why the portfolio's risk depends on how its holdings move
  together — something this formula doesn't look at.
- **Next month.** It's a snapshot of month-end holdings, published after the
  month closes.
- **Whether it suits you.** The dial scores the product. Your horizon and
  what else you own aren't in it.

## Common mistakes

- **Reading "Very High" as a warning to avoid a fund.** For a fully invested
  equity fund it's close to the default, not a special alarm. What matters
  is how you'd cope with the falls equity funds have, which the
  [drawdown post]({% post_url 2026-09-29-drawdown %}) measured.
- **Comparing two equity funds by their dial.** They'll usually show the same
  level. Compare their holdings, volatility and drawdowns instead.
- **Assuming the dial is fixed.** It's recomputed monthly. A fund that was
  "Moderately High" when you bought it can be "Very High" today, and a change
  doesn't come with an exit window.
- **Treating a low reading as "safe".** A debt fund at "Low to Moderate" still
  holds bonds that can be downgraded — which is where the side-pocket rules
  come in, covered later in this series.

**Takeaway:** The riskometer is a monthly score of a fund's holdings — market
cap, each stock's own volatility and liquidity for equity; rating, duration
and liquidity for debt — mapped onto six levels. It's useful for debt funds
and nearly blind among equity funds, because a fully invested equity fund
can't score below High.
