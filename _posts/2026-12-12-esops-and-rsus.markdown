---
layout: post
title: "ESOPs and RSUs: two taxes on two different amounts"
description: "Stock options are taxed as salary when you exercise and as capital gains when you sell. Why the first bill comes before any cash, on a fictional ESOP."
image: /assets/og/esops-and-rsus.png
date: 2026-12-12 09:00:00 +0530
series: tax
term: "ESOP and RSU taxation"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign e = t2.esop %}
{% assign r = site.data.tax.rates %}

## Two events, two heads of income

This post describes the rules for Tax Year 2026-27 (FY 2026-27, April 2026 to March 2027). Its worked example exercises options on {{ e.exercise_date }} and sells on {{ e.sale_date_long }}; those dates are illustrative scenario dates, and the exercise falls in FY (financial year) 2025-26, which the earlier Act governed. Event 1 below therefore uses that Act's treatment as we understand it (not checked here), while the sale is described under the rules for Tax Year 2026-27. The mechanics are what the example teaches.

An **ESOP — employee stock option plan** — gives you the right to buy your
employer's shares at a fixed price (the *exercise price*) after a waiting
period (*vesting*). An **RSU — restricted stock unit** — is a promise of the
shares themselves, delivered when they vest, for nothing.

Both are pay. The Income-tax Act, 2025 (section 17(1)(d)) treats them that way, and then treats
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

**FMV** is fair market value. Under the Income-tax Rules, 2026, for listed shares it's the average of the opening and closing price on the
exercise date on the exchange (the one with the highest volume, if listed on more than one), and for unlisted shares a valuation by a merchant banker. **TDS** (tax deducted at source) is tax your employer withholds
from pay. The key line above is the second one in event
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
[case study](/case-study/), whose IPO (initial public offering) was priced at ₹640 in June 2025 (a fictional company and price). She holds
{% include inr.html n=e.shares %} vested options with an exercise price of ₹{{ e.exercise_price }}, and
exercises them on {{ e.exercise_date }} when the share trades at ₹{{ e.fmv_at_exercise }}.
Illustrative 30% slab plus {{ r.cess_pct }}% cess, no surcharge; this assumes her other salary already puts the perquisite in the 30% slab, and no other long-term gains this year, so the full ₹{% include inr.html n=e.ltcg_exempt %} exemption is available.
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
exercise, she pays the company ₹{% include inr.html n=e.cash_to_exercise %}. Her employer will deduct
₹{% include inr.html n=e.perquisite_tax_with_cess %} of TDS (tax deducted at source) from her salary —
usually in the month of exercise, though some employers spread it over the
rest of the year. Total
cash out: **₹{% include inr.html n=e.cash_out_total %}**. Cash in from the shares: **zero**, because she
hasn't sold anything. She owns {% include inr.html n=e.shares %} shares worth ₹{% include inr.html n=paper_value %} on paper, and
smaller salary credits to show for it.

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
[holding-period post]({% post_url 2026-11-04-short-term-vs-long-term %}) has the rules; as we read the Act, the
clock starts when the shares are allotted to you on exercise, not at grant and not at vesting. For RSUs, the same reading points to the allotment on vesting.

**Putting it together.** Her economic gain was ₹{% include inr.html n=e.economic_gain %} (bought at ₹{{ e.exercise_price }}, sold
at ₹{{ e.sale_price }}). Total tax: ₹{% include inr.html n=e.perquisite_tax_with_cess %} + ₹{% include inr.html n=e.ltcg_tax_with_cess %} =
**₹{% include inr.html n=e.total_tax_long_route %}**, an effective {{ e.effective_rate_pct }}%. Most of it was
salary tax on the discount, paid {{ e.months_held_long }} months before the sale brought in any money.

The beginner's answer — "I made ₹{% include inr.html n=e.economic_gain %} on shares, so it's long-term
capital gains" — would have come to ₹{% include inr.html n=e.wrong_answer_tax %}. It's wrong, and the
employer's salary certificate (Form 16, check the current form name) shows why: the perquisite is
already in the salary figure.

## RSUs: the same thing with a zero exercise price

An RSU has no exercise price, so the perquisite is the *entire* FMV on the
vesting (settlement) date. {{ e.rsu_units }} units vesting at ₹{{ e.fmv_at_exercise }} is a
₹{% include inr.html n=e.rsu_perquisite %} perquisite and ₹{% include inr.html n=e.rsu_tax_with_cess %} of tax at the
illustrative slab.

Because the employee didn't pay anything and may have no cash for the TDS,
many plans are described as choosing to **sell to cover**: the employer sells enough shares on vesting day
to fund the tax and delivers the rest. Here that is {{ e.rsu_sell_to_cover_shares }} shares sold, {{ e.rsu_net_shares }}
delivered. Two consequences people miss:

- The {{ e.rsu_sell_to_cover_shares }} shares were *sold*, on the day they vested. Their capital gain is
  roughly zero, but the sale still exists and belongs in your return.
- Your cost for the remaining {{ e.rsu_net_shares }} shares is ₹{{ e.fmv_at_exercise }} each — the FMV on
  vesting day — not zero.

## When the shares are foreign or unlisted (Tax Year 2026-27)

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

The foreign-or-unlisted column follows from the Act: the twelve-month line and sections 196 and 198 need a listing on a recognised exchange in India, and section 197 sets the 12.5%.

Foreign shares also bring **Schedule FA** — the foreign-asset disclosure in
the return — and a foreign brokerage account to report. That is the subject
of the foreign-stocks post later in this module.

## The startup deferral

Employees of eligible startups get one concession, and it's narrower than it
sounds. If the employer is recognised by DPIIT (the Department for Promotion
of Industry and Internal Trade) **and** holds the Inter-Ministerial Board
(IMB) certificate (section 140 of the Income-tax Act, 2025 requires that certificate, incorporation from 1 April 2016 to before 1 April 2030, and a turnover limit; DPIIT recognition alone is described as not
enough), the tax on the perquisite is *computed* in the year of exercise but
*paid* later: within 14 days of the earliest of

1. 60 months from the end of the tax year in which the shares were allotted,
2. the date you sell the shares, or
3. the date you leave the company.

Older articles say "48 months from the end of the assessment year", the wording of the earlier Act as those articles describe it (not checked here). It would point to the same date: the assessment year
ended a year after the year of allotment, and the Income-tax Act, 2025, which
replaced it with a single Tax Year, counts 60 months from the end of the tax
year itself (section 289 of the Income-tax Act, 2025).

It's a payment deferral, not a reduction. The rate is the rate of the year
you exercised. And for most private-company employees it doesn't apply at
all, which means the tax on exercise falls due before any sale proceeds.

## Common mistakes

- **Treating the whole gain as capital gains.** The discount at exercise is
  salary. Form 16 already includes it; reporting it again as a gain, or not
  reporting it at all, both go wrong.
- **Using the exercise price as your cost.** Cost is the FMV that was taxed
  as perquisite. Using ₹{{ e.exercise_price }} instead of ₹{{ e.fmv_at_exercise }} taxes the same ₹{{ e.perquisite_per_share }} twice.
- **Starting the holding clock at grant or vesting.** It starts at exercise
  (allotment). Options held for years can still produce a short-term
  gain if exercised and sold within the short-term period for the asset (twelve months for listed Indian shares).
- **Forgetting the sell-to-cover sale.** Those shares were sold and belong in
  the capital-gains schedule, even at a near-zero gain.
- **Assuming "startup" means deferral.** Only IMB-certified startups qualify,
  and the deferral ends the day the employee leaves the company.

**Takeaway:** Stock options meet two taxes on two different amounts: the discount at exercise is salary, taxed at the slab rate through the payroll (typically around the time of exercise), and only the *further* rise after that is a capital gain when the shares are sold. On a ₹{% include inr.html n=e.economic_gain %} gain in our
example, ₹{% include inr.html n=e.perquisite_tax_with_cess %} of the ₹{% include inr.html n=e.total_tax_long_route %} total fell due before any
share was sold.

## Sources

- Income-tax Act, 2025 (ICAI copy of the Gazette text): the start-up deferral (14 days after the earliest of 60 months from the end of the tax year, sale, or leaving the employer), as read in that copy.
- [Income-tax Rules, 2026, G.S.R. 198(E), 20 March 2026](https://egazette.gov.in/WriteReadData/2026/271092.pdf): the FMV method. Opened 2 November 2026. Later amendments to the Rules were not traced.
- The same Act: the perquisite (section 17(1)(d)), the cost of acquisition (the FMV taken into account for the perquisite), and the foreign or unlisted share column (sections 2(101) and 196 to 198).

