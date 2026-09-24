---
layout: post
title: "Payout ratio: how much of the profit goes out the door"
description: "Payout ratio is dividends as a share of profit; retention is the rest. Britannia paid out 81% of FY25 earnings, Desi Bites 40%; ROE times retention sets growth."
image: /assets/og/payout-ratio.png
date: 2026-12-05 09:00:00 +0530
series: jargon
term: "Payout ratio"
---

{% assign p = site.data.jargon_m6.payout %}
{% assign b = p.britannia %}
{% assign d = p.desi_bites %}
{% assign bi_dps_decl = site.data.real_company.market.dividend_per_share_fy25_declared %}
{% assign bi_payout_decl = bi_dps_decl | times: 100.0 | divided_by: b.eps | round: 1 %}

## What the payout ratio means

A company that earns a profit can do two things with it: hand some to
shareholders as a dividend, or keep it in the business. The **payout ratio**
is the share handed out; the **retention ratio** is the share kept. They sum
to 100%.

The [dividend yield post]({% post_url 2026-09-28-dividend-yield %}) measured
the dividend against the *share price* — what the investor receives per rupee
invested. Payout measures it against *profit* — what the company chooses to
distribute per rupee earned. Same dividend, two denominators, two different
questions. Yield is about you. Payout is about the company's strategy.

## The formula

```
Payout ratio     =  Dividends / PAT   =  DPS / EPS

  PAT = profit after tax; DPS = dividend per share; EPS = earnings per share
Retention ratio  =  1 − Payout ratio

Sustainable growth rate  ≈  ROE × Retention ratio
```

The third line is why payout matters beyond the dividend cheque. If a company
retains a fraction *r* of its profit and earns a return on equity of *ROE* on
what it keeps, its equity — and, all else equal, its earnings — can grow at
roughly ROE × r a year without borrowing more or issuing shares. This is the
"sustainable" or "internal" growth rate, and it links three things this blog
has covered separately: [ROE]({% post_url 2026-09-01-roe %}), dividends, and
the growth assumptions behind a [DCF]({% post_url 2026-10-04-forecasting-free-cash-flow %}).

## Worked example: Desi Bites Foods, FY25

From the [case study](/case-study/), the year before the IPO:

| | |
|---|---:|
| FY25 PAT (₹ lakh) | {{ d.pat_lakh }} |
| FY25 dividend (₹ lakh) | {{ d.dividend_lakh }} |
| **Payout ratio** = {{ d.dividend_lakh }} / {{ d.pat_lakh }} | **{{ d.payout_pct }}%** |
| Retention ratio | {{ d.retention_pct }}% |
| Per share: DPS ₹{{ d.dps }} / pre-issue EPS ₹{{ d.eps_undiluted }} | {{ d.payout_pct }}% |
| FY25 ROE | {{ d.roe_pct }}% |
| **Sustainable growth** = {{ d.roe_pct }}% × {{ d.retention_pct }}% | **≈ {{ d.sustainable_growth_pct }}%** |

Desi Bites kept about sixty paise of every rupee and earned {{ d.roe_pct | round }}% on its equity, so it
could fund roughly {{ d.sustainable_growth_pct | round }}% growth a year from retained profit alone. That's a
useful sanity check on the [DCF]({% post_url 2026-10-05-terminal-value-and-the-full-dcf %}),
which assumed 18% revenue growth in FY26 — in range. It also explains why the
company *could* have grown without the IPO, and why the
[capital allocation question]({% post_url 2026-11-18-capital-allocation %}) of what to do with
₹{% include inr.html n=site.data.case_study.listing.ipo_proceeds %} lakh of fresh cash is a real one.

## Worked example: Britannia Industries, FY25

DPS from the [dividend yield post]({% post_url 2026-09-28-dividend-yield %}):
₹{{ b.dps }}, the dividend actually *paid* during FY25 (in August 2024). Strictly,
that was the final dividend for FY24, so this is a trailing ratio — the
dividend paid in FY25 divided by FY25 EPS. EPS and ROE from the
[audited FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025). For illustration only.

| | |
|---|---:|
| DPS paid in FY25 (trailing) | ₹{{ b.dps }} |
| FY25 EPS | ₹{{ b.eps }} |
| **Payout ratio** = {{ b.dps }} / {{ b.eps }} | **{{ b.payout_pct }}%** |
| Retention ratio | {{ b.retention_pct }}% |
| FY25 ROE | {{ b.roe_pct }}% |
| **Sustainable growth** = {{ b.roe_pct }}% × {{ b.retention_pct }}% | **≈ {{ b.sustainable_growth_pct }}%** |

The dividend declared *for* FY25 — ₹{{ bi_dps_decl | round }} a share, paid in August 2025 (per
[stockanalysis.com's dividend history](https://stockanalysis.com/quote/nse/BRITANNIA/dividend/)) —
gives a payout of {{ bi_payout_decl }}% on the same EPS. Matching the dividend to the
year it was declared for is the tidier method; the two land close here.

Britannia pays out about four-fifths of what it earns. That pattern is
common in mature companies, where the business often throws off more cash
than it can reinvest at a similar return. Its sustainable growth rate is
about {{ b.sustainable_growth_pct }}% — a consequence of returning most of the profit rather than
retaining it. A company with a {{ b.roe_pct }}% ROE that retained everything could in
theory grow equity at {{ b.roe_pct }}% a year. Why a particular board picks a particular
payout isn't something these numbers can tell you.

This is also the arithmetic behind a point the
[PEG post]({% post_url 2026-09-29-peg-ratio %}) stumbled on: Britannia's FY25
profit growth was {{ site.data.real_company.market.pat_growth_fy24_fy25_pct }}%. With an {{ b.payout_pct | round }}% payout, retained profit alone funds
growth of roughly {{ b.sustainable_growth_pct }}% a year — so modest growth is what the arithmetic
points to, even if {{ site.data.real_company.market.pat_growth_fy24_fy25_pct }}% sits well below that. The rest of that year's gap
was the cost squeeze covered in the
[operating leverage post]({% post_url 2026-12-03-operating-leverage %}), not the payout.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You and your parents own your lemonade stand half each. It earns ₹100. You
pay out ₹80 — ₹40 to your parents, who own half the stand, and ₹40 to you —
and keep ₹20 in the stand to buy more lemons. The stand's payout is 80%.

Next summer, the extra lemons you bought with ₹20 earn you a bit more. If you
had kept all ₹100, you'd have five times as many extra lemons — and grow a
lot faster. Keeping less means paying out more *now* and growing less *later*.
Neither is wrong; it depends on whether more lemons would actually sell.

</details>

## Common mistakes

- **Confusing payout ratio with dividend yield.** Payout is dividend ÷ profit;
  yield is dividend ÷ price. Britannia's payout is {{ b.payout_pct | round }}%; its yield is {{ site.data.jargon_m6.yields.britannia.dividend_yield_pct }}%.
- **Reading a high payout as generosity.** Often it means the company has run
  out of high-return places to reinvest. That can be the right call — or a
  sign growth has stalled.
- **Reading a low payout as stinginess.** A company retaining 60% and earning
  34% on it is compounding your money for you. Ask what the ROE on retained
  capital is, not just the payout.
- **Ignoring buybacks.** Companies also return cash by buying back shares.
  A dividend-only payout ratio understates total distribution for companies
  that buy back regularly.
- **Computing payout on one year's EPS with an exceptional item in it.** A
  one-off gain shrinks the ratio; a one-off charge inflates it. Use a normal
  year, or several.

**Takeaway:** payout ratio is the share of profit paid out as dividends;
retention is what's kept, and ROE times retention says how fast a company can
grow on its own money. A high or low payout isn't better or worse — each is an
answer to "can we reinvest this well?"
