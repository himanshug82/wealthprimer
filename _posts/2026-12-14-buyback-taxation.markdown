---
layout: post
title: "Buybacks: three tax regimes, two changes in 18 months"
description: "How a buyback is taxed depends on its date: company-paid tax, then a deemed dividend, then capital gains from April 2026 — worked on the same 100 shares."
image: /assets/og/buyback-taxation.png
date: 2026-12-14 09:00:00 +0530
series: tax
term: "Buyback taxation"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign b = t2.buyback %}
{% assign a = b.regime_a %}
{% assign rb = b.regime_b %}
{% assign rc = b.regime_c %}
{% assign r = site.data.tax.rates %}

*Rules described here are date-specific: three regimes are shown, the latest
one applying from 1 April 2026. Tax Year 2026-27 (FY 2026-27), rules as at November 2026. Regime C comes from the Income-tax Act, 2025 and the Finance Act, 2026. Regime A and the start date of Regime B come from secondary sources (listed at the end), not from the Act.*

## What a buyback is, and why the tax kept changing

In a **buyback**, a company uses its cash to purchase its own shares from
shareholders and cancels them. Fewer shares remain, so each one owns a
slightly larger slice of the same business — the
[EPS (earnings per share) post]({% post_url 2026-09-23-eps %}) flagged this as a reason EPS can rise
without profit rising.

Economically a buyback is a way of returning cash to shareholders, like a
dividend. Unlike a dividend, it's optional — you tender your shares or you
don't — and the money comes back as a sale rather than as income. That
difference is why the tax treatment has changed: **is buyback money a dividend or a sale?** The law has given three
different answers, and the answer depends on the date the
buyback happened.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A club has 100 members who each paid ₹640 to join. The club has spare money
and offers to buy back a few memberships at ₹700.

Is your ₹700 a "prize from the club" (like pocket money — taxed as income) or
"selling your membership card for more than you paid" (taxed on just the ₹60
profit)?

For a while the club paid a tax so members didn't have to. Then the rule
said: the whole ₹700 is a prize, tax it all. Now the rule says: it's a sale,
tax only the ₹60 profit. Same ₹700, three different bills, depending on the
year.

</details>

## One example, three regimes

Throughout, the same fictional shareholder: {{ b.shares }} shares of Desi Bites Foods
bought in the [IPO (initial public offering)](/case-study/) at ₹{{ b.cost_per_share }} on {{ b.purchase_date }}, tendered in a
hypothetical buyback at ₹{{ b.buyback_price }}. Consideration
₹{% include inr.html n=b.consideration %}, cost ₹{% include inr.html n=b.cost_total %}, economic gain
**₹{% include inr.html n=b.gain %}**. Illustrative 30% slab plus {{ r.cess_pct }}% cess, no
surcharge, no other capital gains in the year unless stated.

### Regime A — {{ a.period }}: the company paid

Our shareholder bought in June 2025, after this regime ended, so this one is
hypothetical — as if the same shares had been tendered under the old rule.
As described in secondary sources (check the current rule), the company paid a **buyback tax of {{ a.company_tax_rate_pct }}%** — 20% × 1.12 (a 12% surcharge) × 1.04 (4% cess) = 23.296% — on the *distributed income* — what it paid out minus what it had
originally received for those shares — and the shareholder paid nothing.

| | |
|---|---:|
| Distributed income ({{ b.shares }} × (₹{{ b.buyback_price }} − ₹{{ b.cost_per_share }})) | ₹{% include inr.html n=b.gain %} |
| Tax paid by the company | ₹{% include inr.html n=a.company_tax %} |
| **Tax paid by the shareholder** | **₹0** |

Under this regime the company-level rate did not depend on the shareholder's slab,
so a promoter in the 30% slab and a small investor below the taxable limit
faced the same company-level tax.

### Regime B — {{ rb.period }}: the whole cheque was a dividend

As described in secondary sources (check the current rule), from 1 October 2024 the buyback tax was abolished and the **entire
consideration** — not the gain, the whole amount — was treated as a dividend
in the shareholder's hands, taxed at slab like any other
[dividend]({% post_url 2026-12-08-dividends-and-interest %}), with 10% TDS (tax deducted at source). No deduction
of cost was allowed against it.

Instead, the cost of the shares became a **capital loss**: for capital-gains
purposes the sale consideration was deemed to be nil, so you "sold" ₹{% include inr.html n=b.cost_total %}
of shares for nothing.

| | |
|---|---:|
| Deemed dividend (the full consideration) | ₹{% include inr.html n=rb.deemed_dividend %} |
| **Tax at 30% + cess** | **₹{% include inr.html n=rb.tax_with_cess %}** |
| of which TDS deducted by the company at 10% | ₹{% include inr.html n=rb.tds %} |
| Capital loss created (cost, sold for "nil") — short-term, since the shares were held under 12 months | ₹{% include inr.html n=rb.capital_loss %} |
| Worth of that loss if set off against short-term gains at {{ r.equity_stcg_pct }}% + cess | ₹{% include inr.html n=rb.loss_worth_against_stcg %} |
| Worth if set off against long-term gains at {{ r.equity_ltcg_pct }}% + cess | ₹{% include inr.html n=rb.loss_worth_against_ltcg %} |
| **Net cost, if the loss could be fully used against STCG** | **₹{% include inr.html n=rb.net_cost_if_loss_used_against_stcg %}** |

Read that again: a ₹{% include inr.html n=b.gain %} gain, and a ₹{% include inr.html n=rb.tax_with_cess %} tax bill
up front. The capital loss softens it only if you *have* capital gains to set
it against (or will within the [eight-year carry-forward]({% post_url 2026-11-16-losses-set-off-and-harvesting %})).
Someone with no other gains could pay slab-rate tax on their own capital
coming back. The loss's holding period matters too: our shareholder bought
in June 2025, so any Regime B buyback came within twelve months and the loss
is short-term, usable against any capital gain. Shares held longer would have
produced a long-term loss, usable only against long-term gains. For an individual in a higher slab, the tax on the whole cheque was larger than the tax on the gain.

### Regime C — {{ rc.period }}: a sale, taxed on the gain

From 1 April 2026, the Finance Act, 2026 took buybacks out of the definition of dividend (section 35). Section 69 of the Income-tax Act, 2025 now treats the consideration minus your cost as a
capital gain.
**The rate turns on one condition.** The Act has no separate buyback rate, so the normal rules apply, and the [equity post]({% post_url 2026-11-08-equity-and-equity-funds %}) rates need securities transaction tax (STT) on the sale and, for long-term gains on shares, generally on the purchase too. We didn't find a source saying whether a given buyback bears STT, so the table below shows what those rates give *if* it did. Without STT, a short-term gain would go to your slab and a long-term gain to 12.5% with no annual exemption.

| | Held > {{ r.equity_holding_months }} months | Held ≤ {{ r.equity_holding_months }} months |
|---|---:|---:|
| Gain | ₹{% include inr.html n=rc.gain %} | ₹{% include inr.html n=rc.gain %} |
| Rate | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption | {{ r.equity_stcg_pct }}% |
| **Tax with cess, if the STT condition is met** | **₹{{ rc.ltcg_tax_with_cess }}** (gain sits inside the exemption) | **₹{% include inr.html n=rc.stcg_tax_with_cess %}** |

On that basis, taxing the gain rather than the whole cheque produces a much smaller bill for
this example than Regime B's ₹{% include inr.html n=rb.tax_with_cess %}, for the
identical transaction. Without STT, the Regime C figure here would differ.

**The promoter add-on.** Section 42 of the Finance Act, 2026 adds an *additional* income-tax when the
tendering shareholder is a **promoter**: 2% on a short-term gain under section 196 and 9.5% on a long-term gain, if the promoter is a domestic company, and 10% and 17.5% otherwise. On top of the 20% or 12.5% that gives
**{{ rc.promoter_effective_rate_corp_pct }}%** and
**{{ rc.promoter_effective_rate_noncorp_pct }}%**. For a listed company, a promoter is as defined in regulation 2(k) of SEBI's (the Securities and Exchange Board of India's) buy-back regulations of 2018. Those rates are before surcharge and cess. At {{ rc.promoter_effective_rate_noncorp_pct }}%, the same
₹{% include inr.html n=b.gain %} gain would bear
₹{% include inr.html n=rc.promoter_tax_noncorp %} before them.

## The three regimes side by side

| | A: to Sep 2024 | B: Oct 2024 – Mar 2026 | C: from Apr 2026 |
|---|---|---|---|
| Who pays | Company | Shareholder | Shareholder |
| Taxed as | Buyback tax on distributed income | **Dividend**, on the *whole* consideration | **Capital gain**, on consideration − cost |
| Cost of shares | Irrelevant to you | Becomes a separate capital loss | Deducted directly |
| Rate for an individual | 0% (company paid {{ a.company_tax_rate_pct }}%) | Slab | {{ r.equity_stcg_pct }}% / {{ r.equity_ltcg_pct }}% with exemption, if STT applies |
| Our example's tax | ₹0 | ₹{% include inr.html n=rb.tax_with_cess %} (less loss value later) | ₹{{ rc.ltcg_tax_with_cess }} or ₹{% include inr.html n=rc.stcg_tax_with_cess %}, if STT applies |
| Promoter add-on | — | — | 22% / 30% before surcharge and cess |

## Why the date matters for your return

Section 69 charges the gain "in the year in which the company purchases the shares" — not the year of the announcement. On that wording a buyback announced in March 2026 and completed in April 2026 looks like a
Regime C event. The Act doesn't spell out the date a purchase completes, so check the current rule for a buyback that straddles the change.

If you tendered shares in a Regime B buyback, your return for that year needs
two entries that don't feel like they belong together: a dividend (the whole
amount, with its TDS in the tax credit statement) and a capital loss (your cost). Both must
be reported; the [AIS (Annual Information Statement)]({% post_url 2026-12-10-before-you-file %}) will show the
company's payment and the department will expect to see it somewhere.

## Common mistakes

- **Reporting only the gain under Regime B.** The whole consideration was a
  dividend. The gain was irrelevant; the cost became a loss.
- **Forgetting to claim the Regime B capital loss.** It's real, it carries
  forward eight years, and it is easy to miss because the "sale" had nil
  consideration.
- **Assuming the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption and equity rates certainly apply under Regime C.** They depend on the STT conditions; see above.
- **Treating a buyback as always lower-taxed or higher-taxed than a dividend.** In Regime C the comparison
  is between a capital-gains rate on the gain and the slab rate on the whole payout. If the STT rates apply, then for a
  taxpayer in the 30% slab the gain-only tax is lower at any gain size; for a taxpayer in a low slab, a dividend
  can be taxed at a lower rate than the capital-gains rate, and the answer depends on the slab.

**Takeaway:** How a buyback is taxed has depended on the date it happened. As described in secondary sources, the company paid until September 2024; from October 2024 the
whole cheque was a dividend at your slab, turning a ₹{% include inr.html n=b.gain %} gain into a
₹{% include inr.html n=rb.tax_with_cess %} bill in our example, before any loss offset. From April 2026 it is taxed as a capital gain, with an additional tax for promoters.

## Sources

- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026, opened 2 November 2026: sections 35 (removing buyback from the definition of dividend) and 42 (the promoter add-on, and who counts as a promoter).
- Income-tax Act, 2025 ([ICAI copy of the Gazette text](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf)): section 69 (consideration minus cost deemed capital gains "in the year in which the company purchases the shares") and sections 196 to 198 (rates and STT conditions). It was not used to confirm Regime A or the start date of Regime B.
- Regimes A and B (dates, the 23.296% build, 10% TDS, nil consideration): secondary sources only, listed in the module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml). Check the current rule.

