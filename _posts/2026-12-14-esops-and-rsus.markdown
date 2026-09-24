---
layout: post
title: "ESOPs and RSUs: taxed twice, on purpose"
description: "Stock options are taxed as salary when you exercise and again as capital gains when you sell. Why the first bill arrives before any cash does, worked on a fictional ESOP."
image: /assets/og/esops-and-rsus.png
date: 2026-12-14 09:00:00 +0530
series: tax
term: "ESOP and RSU taxation"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign e = t2.esop %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, verified against public
sources in {{ v.verified_on }}. Educational content, not tax advice.*

## Two events, two heads of income

An **ESOP — Employee Stock Option Plan** — gives you the right to buy your
employer's shares at a fixed price (the *exercise price*) after a waiting
period (*vesting*). An **RSU — Restricted Stock Unit** — is a promise of the
shares themselves, delivered when they vest, for nothing.

Both are pay. The tax system treats them exactly that way, and then treats
the shares you end up holding exactly like any other shares. That gives two
taxing events, under two different heads:

```
Event 1  Exercise (ESOP) / vesting (RSU)
         Perquisite = FMV on that date − what you paid
         → taxed as SALARY, at your slab, with employer TDS

Event 2  Sale of the shares
         Capital gain = sale price − the FMV used in event 1
         → taxed as CAPITAL GAINS, by holding period and share type
```

**FMV** is fair market value — for listed shares, the market price on the
exercise date (the rules use the average of that day's opening and closing
price on the exchange with the higher trading volume; for unlisted shares a
merchant banker's valuation). The single most important line above is the second one in event
2: your cost of acquisition for capital gains is *not* what you paid. It's the
FMV that was already taxed as salary. That is what stops the same rupee being
taxed twice — and it is also what people get wrong.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your school lets you buy a ₹700 cricket bat for ₹200 because you helped at
the sports day. The ₹500 discount is a reward for work — so it's treated like
pocket money you earned, and taxed like pocket money, on the day you buy the
bat.

Later you sell the bat to a friend for ₹850. Your profit on the *sale* isn't
₹650. You already "earned" ₹500 of that as a reward. The sale profit is
₹850 − ₹700 = ₹150, and that gets the tax that selling things gets.

Two different things happened — earning a reward, then selling an item — so
there are two different taxes. Not one tax charged twice.

</details>

## Worked example: a Desi Bites Foods employee

Take an employee of Desi Bites Foods, the fictional company from the
[case study](/case-study/), which listed at ₹640 in June 2025. She holds
{% include inr.html n=e.shares %} vested options with an exercise price of ₹{{ e.exercise_price }}, and
exercises them on {{ e.exercise_date }} when the share trades at ₹{{ e.fmv_at_exercise }}.
Illustrative 30% slab plus {{ r.cess_pct }}% cess, no surcharge.
{% assign paper_value = e.perquisite | plus: e.cash_to_exercise %}

**Event 1 — exercise:**

| | |
|---|---:|
| FMV on exercise date | ₹{{ e.fmv_at_exercise }} |
| − Exercise price | ₹{{ e.exercise_price }} |
| Perquisite per share | ₹{{ e.perquisite_per_share }} |
| × Shares | {% include inr.html n=e.shares %} |
| **Perquisite, added to salary** | **₹{% include inr.html n=e.perquisite %}** |
| Tax at 30% | ₹{% include inr.html n=e.perquisite_tax_before_cess %} |
| **Tax with {{ r.cess_pct }}% cess (deducted by employer)** | **₹{% include inr.html n=e.perquisite_tax_with_cess %}** |

Now the cash-flow problem, which is the real subject of this post. To
exercise, she pays the company ₹{% include inr.html n=e.cash_to_exercise %}. Her employer must deduct
₹{% include inr.html n=e.perquisite_tax_with_cess %} of TDS (tax deducted at source) from her salary in the
month of exercise. Total
cash out: **₹{% include inr.html n=e.cash_out_total %}**. Cash in from the shares: **zero**, because she
hasn't sold anything. She owns {% include inr.html n=e.shares %} shares worth ₹{% include inr.html n=paper_value %} on paper, and
a smaller salary credit that month.

**Event 2 — sale, {{ e.months_held_long }} months later at ₹{{ e.sale_price }}:**

| | |
|---|---:|
| Sale price | ₹{{ e.sale_price }} |
| − Cost of acquisition (the FMV already taxed) | ₹{{ e.fmv_at_exercise }} |
| Gain per share | ₹{{ e.sale_price | minus: e.fmv_at_exercise }} |
| **Long-term capital gain** (held > {{ r.equity_holding_months }} months, listed shares) | **₹{% include inr.html n=e.capital_gain %}** |
| − Annual exemption | ₹{% include inr.html n=e.ltcg_exempt %} |
| Taxable | ₹{% include inr.html n=e.ltcg_taxable %} |
| **Tax at {{ r.equity_ltcg_pct }}% with cess** | **₹{% include inr.html n=e.ltcg_tax_with_cess %}** |

Had she sold inside twelve months instead, the same ₹{% include inr.html n=e.capital_gain %} would be a
short-term gain at {{ r.equity_stcg_pct }}%: ₹{% include inr.html n=e.stcg_tax_with_cess_if_sold_within_12m %}. The
[holding-period post]({% post_url 2026-10-28-short-term-vs-long-term %}) has the rules; the
clock starts on the exercise date, not the grant date and not the vesting
date.

**Putting it together.** Her economic gain was ₹{% include inr.html n=e.economic_gain %} (bought at ₹{{ e.exercise_price }}, sold
at ₹{{ e.sale_price }}). Total tax: ₹{% include inr.html n=e.perquisite_tax_with_cess %} + ₹{% include inr.html n=e.ltcg_tax_with_cess %} =
**₹{% include inr.html n=e.total_tax_long_route %}**, an effective {{ e.effective_rate_pct }}%. Most of it was
salary tax on the discount, paid a year before she saw any money.

The beginner's answer — "I made ₹{% include inr.html n=e.economic_gain %} on shares, so it's long-term
capital gains" — would have come to ₹{% include inr.html n=e.wrong_answer_tax %}. It's wrong, and the
employer's Form 16 makes it obviously wrong, because the perquisite is
already sitting in the salary figure.

## RSUs: the same thing with a zero exercise price

An RSU has no exercise price, so the perquisite is the *entire* FMV on the
vesting (settlement) date. {{ e.rsu_units }} units vesting at ₹{{ e.fmv_at_exercise }} is a
₹{% include inr.html n=e.rsu_perquisite %} perquisite and ₹{% include inr.html n=e.rsu_tax_with_cess %} of tax at the
illustrative slab.

Because the employee didn't pay anything and may have no cash for the TDS,
most plans **sell to cover**: the employer sells enough shares on vesting day
to fund the tax and delivers the rest. Here that is {{ e.rsu_sell_to_cover_shares }} shares sold, {{ e.rsu_net_shares }}
delivered. Two consequences people miss:

- The {{ e.rsu_sell_to_cover_shares }} shares were *sold*. On the day they vested. Their capital gain is
  roughly zero, but the sale still exists and belongs in your return.
- Your cost for the remaining {{ e.rsu_net_shares }} shares is ₹{{ e.fmv_at_exercise }} each — the FMV on
  vesting day — not zero.

## When the shares are foreign or unlisted

Many RSUs in India come from a foreign parent (the US-listed employer of an
Indian subsidiary). The perquisite half is identical. The capital-gains half
follows the rules for foreign or unlisted shares instead of Indian listed
ones:

| | Indian listed shares | Foreign or unlisted shares |
|---|---|---|
| Long-term after | {{ r.equity_holding_months }} months | {{ r.other_holding_months }} months |
| Short-term rate | {{ r.equity_stcg_pct }}% | Your slab rate |
| Long-term rate | {{ r.equity_ltcg_pct }}% | {{ r.equity_ltcg_pct }}% (no indexation) |
| ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption | Yes | **No** |

Foreign shares also bring **Schedule FA** — the foreign-asset disclosure in
the return — and a foreign brokerage account to report. That is the subject
of the last post in this module.

## The startup deferral

Employees of eligible startups get one concession, and it's narrower than it
sounds. If the employer is recognised by DPIIT (the Department for Promotion
of Industry and Internal Trade) **and** holds the Inter-Ministerial Board
(IMB) certificate (the old section 80-IAC startups — DPIIT recognition alone is not
enough), the tax on the perquisite is *computed* in the year of exercise but
*paid* later: within 14 days of the earliest of

1. 60 months from the end of the tax year in which the shares were allotted,
2. the date you sell the shares, or
3. the date you leave the company.

Older articles say "48 months from the end of the assessment year". That was
the 1961 Act's wording, and it points to the same date: the assessment year
ended a year after the year of allotment, and the Income-tax Act, 2025, which
replaced it with a single Tax Year, counts 60 months from the end of the tax
year itself (per the Act's text as published in September 2026 — worth
confirming against the current version).

It's a payment deferral, not a reduction. The rate is the rate of the year
you exercised. And for most private-company employees it doesn't apply at
all, which is why exercising options in an unlisted startup is a decision
about cash, not just about the company.

## Common mistakes

- **Treating the whole gain as capital gains.** The discount at exercise is
  salary. Form 16 already includes it; reporting it again as a gain, or not
  reporting it at all, both go wrong.
- **Using the exercise price as your cost.** Cost is the FMV that was taxed
  as perquisite. Using ₹{{ e.exercise_price }} instead of ₹{{ e.fmv_at_exercise }} taxes the same ₹{{ e.perquisite_per_share }} twice.
- **Starting the holding clock at grant or vesting.** It starts at exercise
  (allotment). Options you've held for years can still produce a short-term
  gain if you exercise and sell within twelve months.
- **Forgetting the sell-to-cover sale.** Those shares were sold and belong in
  the capital-gains schedule, even at a near-zero gain.
- **Exercising without the cash for the TDS.** The tax is deducted from
  salary in the month of exercise. A large exercise can take most of that
  month's pay.
- **Assuming "startup" means deferral.** Only IMB-certified startups qualify,
  and the deferral ends the day you resign.

**Takeaway:** Stock options are taxed twice by design — the discount you got is
salary, taxed at your slab the month you exercise, and only the *further* rise
after that is a capital gain when you sell. On a ₹{% include inr.html n=e.economic_gain %} gain in our
example, ₹{% include inr.html n=e.perquisite_tax_with_cess %} of the ₹{% include inr.html n=e.total_tax_long_route %} total was due a year before any
share was sold. Plan the exercise around the cash, not just the price.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists every source these rules were checked against, and the points a
professional should confirm before you rely on them.*
