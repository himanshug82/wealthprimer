---
layout: post
title: "Buybacks: the tax that moved three times"
description: "How a buyback is taxed depends on its date: company-paid tax, then a deemed dividend, then capital gains from April 2026 — worked on the same 100 shares."
image: /assets/og/buyback-taxation.png
date: 2026-12-15 09:00:00 +0530
series: tax
term: "Buyback taxation"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign b = t2.buyback %}
{% assign a = b.regime_a %}
{% assign rb = b.regime_b %}
{% assign rc = b.regime_c %}
{% assign r = site.data.tax.rates %}

*Rules described here are date-specific — three regimes are shown, the current
one applying from 1 April 2026. Verified against public sources in
{{ v.verified_on }}. Educational content, not tax advice.*

## What a buyback is, and why the tax kept changing

In a **buyback**, a company uses its cash to purchase its own shares from
shareholders and cancels them. Fewer shares remain, so each one owns a
slightly larger slice of the same business — the
[EPS post]({% post_url 2026-09-23-eps %}) flagged this as a reason EPS can rise
without profit rising.

Economically a buyback is a way of returning cash to shareholders, like a
dividend. Unlike a dividend, it's optional — you tender your shares or you
don't — and the money comes back as a sale rather than as income. That
difference is exactly why the tax treatment has been argued over for a
decade: **is buyback money a dividend or a sale?** The law has given three
different answers over the years, and the answer depends on the date the
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
bought in the [IPO](/case-study/) at ₹{{ b.cost_per_share }} on 15 June 2025, tendered in a
hypothetical buyback at ₹{{ b.buyback_price }}. Consideration
₹{% include inr.html n=b.consideration %}, cost ₹{% include inr.html n=b.cost_total %}, economic gain
**₹{% include inr.html n=b.gain %}**. Illustrative 30% slab plus {{ r.cess_pct }}% cess, no
surcharge, no other capital gains in the year unless stated.

### Regime A — {{ a.period }}: the company paid

Our shareholder bought in June 2025, after this regime ended, so this one is
hypothetical — as if the same shares had been tendered under the old rule.
The company paid a **buyback tax of {{ a.company_tax_rate_pct }}%** (20% plus surcharge and
cess) on the *distributed income* — what it paid out minus what it had
originally received for those shares — and the shareholder paid nothing.

| | |
|---|---:|
| Distributed income ({{ b.shares }} × (₹{{ b.buyback_price }} − ₹{{ b.cost_per_share }})) | ₹{% include inr.html n=b.gain %} |
| Tax paid by the company | ₹{% include inr.html n=a.company_tax %} |
| **Tax paid by the shareholder** | **₹0** |

Simple, but it had a flaw the government disliked: the company-level rate
was the same for everyone, so a promoter in the 30% slab and a small investor
below the taxable limit bore the same effective tax. Buybacks became a way to
extract cash at a flat rate.

### Regime B — {{ rb.period }}: the whole cheque was a dividend

From 1 October 2024 the buyback tax was abolished and the **entire
consideration** — not the gain, the whole amount — was treated as a dividend
in the shareholder's hands, taxed at slab like any other
[dividend]({% post_url 2026-10-31-dividends-and-interest %}), with 10% TDS. No deduction
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
it against (or will within the [eight-year carry-forward]({% post_url 2026-11-01-losses-set-off-and-harvesting %})).
A retiree with no other gains simply paid slab-rate tax on their own capital
coming back. The loss's holding period matters too: our shareholder bought
in June 2025, so any Regime B buyback came within twelve months and the loss
is short-term, usable against any capital gain. Shares held longer would have
produced a long-term loss, usable only against long-term gains. For most
individuals in higher slabs, this regime made tendering tax-expensive.

### Regime C — {{ rc.period }}: a sale, taxed on the gain

The Finance Act, 2026 reversed course. From 1 April 2026 a buyback is taxed
as what it economically is: a **sale of shares**, with the cost deductible
and the gain taxed under the normal equity rules from the
[equity post]({% post_url 2026-10-29-equity-and-equity-funds %}).

| | Held > {{ r.equity_holding_months }} months | Held ≤ {{ r.equity_holding_months }} months |
|---|---:|---:|
| Gain | ₹{% include inr.html n=rc.gain %} | ₹{% include inr.html n=rc.gain %} |
| Rate | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption | {{ r.equity_stcg_pct }}% |
| **Tax with cess** | **₹{{ rc.ltcg_tax_with_cess }}** (gain sits inside the exemption) | **₹{% include inr.html n=rc.stcg_tax_with_cess %}** |

For our shareholder the buyback in Regime C costs nothing if the shares were
held over a year and other long-term gains haven't used up the exemption —
against ₹{% include inr.html n=rb.tax_with_cess %} a few months earlier under Regime B, for the
identical transaction.

**The promoter surcharge.** To stop buybacks becoming a low-tax route for
controlling shareholders again, Regime C adds an *additional* tax when the
tendering shareholder is a **promoter** (for a listed company, as defined in
SEBI's buyback regulations; otherwise a Companies Act promoter or a holder of
more than 10%). Their effective rate on the gain becomes about
**{{ rc.promoter_effective_rate_corp_pct }}%** for a promoter that is a domestic company and
**{{ rc.promoter_effective_rate_noncorp_pct }}%** for other promoters, regardless of holding period. On the
same ₹{% include inr.html n=b.gain %} gain a non-corporate promoter would pay roughly
₹{% include inr.html n=rc.promoter_tax_noncorp %}. Ordinary shareholders are unaffected by this part.

## The three regimes side by side

| | A: to Sep 2024 | B: Oct 2024 – Mar 2026 | C: from Apr 2026 |
|---|---|---|---|
| Who pays | Company | Shareholder | Shareholder |
| Taxed as | Buyback tax on distributed income | **Dividend**, on the *whole* consideration | **Capital gain**, on consideration − cost |
| Cost of shares | Irrelevant to you | Becomes a separate capital loss | Deducted directly |
| Rate for an individual | 0% (company paid {{ a.company_tax_rate_pct }}%) | Slab | {{ r.equity_stcg_pct }}% / {{ r.equity_ltcg_pct }}% with exemption |
| Our example's tax | ₹0 | ₹{% include inr.html n=rb.tax_with_cess %} (less loss value later) | ₹{{ rc.ltcg_tax_with_cess }} or ₹{% include inr.html n=rc.stcg_tax_with_cess %} |
| Promoter add-on | — | — | Effective 22% / 30% |

## Why the date matters for your return

A buyback is taxed by the regime in force **on the date the shares were
bought back**, which on the current reading is the date the company pays you
— not the date of the announcement, and not the date you tendered. On that
reading, a buyback announced in March 2026 and settled in April 2026 is a
Regime C event. For a buyback straddling the change, confirm the date with a
professional.

If you tendered shares in a Regime B buyback, your return for that year needs
two entries that don't feel like they belong together: a dividend (the whole
amount, with its TDS in Form 26AS) and a capital loss (your cost). Both must
be reported; the [AIS]({% post_url 2026-11-04-before-you-file %}) will show the
company's payment and the department will expect to see it somewhere.

## Common mistakes

- **Reporting only the gain under Regime B.** The whole consideration was a
  dividend. The gain was irrelevant; the cost became a loss.
- **Forgetting to claim the Regime B capital loss.** It's real, it carries
  forward eight years, and it is easy to miss because the "sale" had nil
  consideration.
- **Using the announcement date to pick the regime.** The payout date
  decides, on the current reading.
- **Assuming the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption always applies under Regime C.** It
  applies to long-term gains on listed shares, once per year, across all your
  equity gains — and the sources describe buyback gains as taxed "under the
  capital gains head at normal rates" rather than stating the exemption
  outright. Confirm with a professional before relying on it.
- **Believing "buyback is more tax-efficient than a dividend" as a rule.**
  True in Regime A, false in Regime B, and in Regime C true only when the
  gain is small relative to the payout — as it was here.
- **Promoters assuming the ordinary rates.** The additional tax applies to
  them alone, and it changes the arithmetic of a buyback entirely.

**Takeaway:** How a buyback is taxed depends on the date it happened. Until
September 2024 the company paid and you owed nothing; from October 2024 the
whole cheque was a dividend at your slab, turning a ₹{% include inr.html n=b.gain %} gain into a
₹{% include inr.html n=rb.tax_with_cess %} bill in our example; from April 2026 it is a plain sale
taxed on the gain, with a surcharge reserved for promoters. Check the payout
date before you check anything else.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists every source these rules were checked against, and the points a
professional should confirm before you rely on them.*
