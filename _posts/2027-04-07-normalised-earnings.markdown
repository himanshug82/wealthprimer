---
layout: post
title: "Normalised earnings: profit in a typical year"
description: "Normalised earnings strip one-offs and smooth a cyclical cost to estimate profit in a typical year. Why it changes the P/E, worked on Desi Bites' FY26."
image: /assets/og/normalised-earnings.png
date: 2027-04-07 09:00:00 +0530
series: fundamental-analysis
term: "Normalised earnings"
---

{% assign n = site.data.fa5.normalised %}
{% assign rp = n.reported %}
{% assign sp = n.spike %}
{% assign nm = n.normal %}
{% assign co = n.core %}

## What normalised earnings are

**Normalised earnings** are an estimate of what a company would earn in a
typical year: reported profit with one-off items taken out and costs that
swing with a cycle, such as a raw-material price, set to a middle-of-the-cycle
level. It isn't an accounting figure. No standard defines it, so every
analyst's version rests on their own adjustments, and a reader should be
able to see each one.

It matters for valuation because a [P/E]({% post_url 2026-09-24-price-to-earnings %})
(price-to-earnings ratio) on one
unusual year can mislead. A company whose costs spiked shows a high P/E; one
with a windfall shows a low one. This post works through the adjustments on the
fictional [Desi Bites Foods]({{ '/case-study/' | relative_url }}), part of
[Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}).

## The formula

```
Normalised PBT     =  reported profit before tax (PBT)
                      −  one-off gains   +  one-off losses   (exceptional items)
                      ±  (normal level of a cyclical item − this year's level)
Normalised profit  =  normalised PBT × (1 − normal tax rate)

Normalised P/E  =  market capitalisation ÷ normalised profit
```

A further, separate question is whether to keep income that isn't from the
business, such as interest on surplus cash. If you take it out of profit, take
the cash out of the price too, or the two sides no longer match.

## Worked example: Desi Bites, FY26

Figures from Desi Bites' FY26 accounts, in ₹ lakh, valued at its ₹{{ n.price }}
IPO (initial public offering) price on {{ n.shares_lakh }} lakh shares: a market capitalisation of
₹{% include inr.html n=n.mcap %} lakh. Tax is applied at FY26's effective rate,
{{ n.eff_tax_pct }}% (see the [effective tax rate post]({% post_url 2026-12-04-effective-tax-rate %})).

**Step 1: what's normal for the cost of goods?** Desi Bites' gross margin
(gross profit as a share of revenue) by year:

| | {% for g in n.gross_margins %}{{ g.fy }} | {% endfor %}Average |
|---|{% for g in n.gross_margins %}---:|{% endfor %}---:|
| Gross margin | {% for g in n.gross_margins %}{{ g.pct }}% | {% endfor %}{{ n.avg_gm_pct }}% |

FY26's margin is a little above its four-year average, so normalising it
lowers profit slightly. One caveat: FY23 to FY25 are Desi Bites alone, while
FY26 includes six months of the lower-margin Chatpata business it bought, so
the average mixes two slightly different businesses.

**Step 2: a bad year, for contrast.** Desi Bites' DRHP (draft red herring
prospectus) lists edible oil and flour as roughly {{ n.oil_share_pct }}% of
its raw-material cost, unhedged. Suppose, as a simplifying assumption, they
are {{ n.oil_share_pct }}% of its whole cost of goods sold (which overstates
the effect a little, since that cost includes more than raw materials), and
their prices rise {{ n.spike_pct }}% in a year with nothing else changed.

**Step 3: the four views of FY26.**

| ₹ lakh | Reported FY26 | If oil and flour spiked | Normalised | Normalised, ex cash income |
|---|---:|---:|---:|---:|
| Gross margin | {{ rp.gm_pct }}% | {{ sp.gm_pct }}% | {{ n.avg_gm_pct }}% | {{ n.avg_gm_pct }}% |
| EBIT | {{ rp.ebit }} | {{ sp.ebit }} | {{ nm.ebit }} | {{ co.ebit }} |
| Other income (mostly interest on IPO cash) | {{ n.other_income }} | {{ n.other_income }} | {{ n.other_income }} | 0 |
| Exceptional items | {{ n.exceptional | replace: "-", "−" }} | {{ n.exceptional | replace: "-", "−" }} | 0 | 0 |
| Profit before tax | {{ rp.pbt }} | {{ sp.pbt }} | {{ nm.pbt }} | {{ co.pbt }} |
| Profit after tax | {{ rp.pat }} | {{ sp.pat }} | {{ nm.pat }} | {{ co.pat }} |
| P/E at ₹{{ n.price }} | {{ rp.pe }} | {{ sp.pe }} | {{ nm.pe }} | {{ co.pe_ex_cash }} (on price less cash) |

EBIT is earnings before interest and tax.

What each column shows:

1. **Normalised, against reported.** Taking out the
   ₹{{ n.exceptional | abs }} lakh of acquisition integration costs (a
   one-off, from the [goodwill post]({% post_url 2026-10-07-goodwill-exceptional-items-and-other-income %}))
   raises profit; trimming the gross margin to its average lowers it. Here
   the two nearly cancel: normalised profit is ₹{{ nm.pat }} lakh against
   ₹{{ rp.pat }} lakh reported, and the P/E barely moves.
2. **The spike year.** The same company, in a year of dear oil and flour,
   reports far less profit and a P/E of {{ sp.pe }}. Assuming the spike
   reverses, nothing about the business's normal earning power changed; one
   cost moved. Normalising that
   year would bring the P/E back near {{ nm.pe }}.
3. **Taking out the cash income.** Other income is mostly interest on the
   IPO cash. Remove it from profit and remove the ₹{% include inr.html n=n.cash %}
   lakh of cash from the price, and the P/E on the operating business alone
   is {{ co.pe_ex_cash }}.

None of these is "the right" P/E. Each answers a different question, and
whether any of them is high or low for Desi Bites isn't assessed here.

## Common mistakes

1. **Calling recurring costs one-off.** A company that books
   "restructuring" or "exceptional" charges most years is reporting a normal
   cost of doing business. Check how often the item recurs before removing
   it; the [cooking-the-books post]({% post_url 2026-10-04-desi-bites-cooks-the-books %})
   shows how presentation can flatter profit.
2. **Normalising only the bad years.** Adjusting a weak year upwards but
   accepting a strong year as it is biases every estimate upwards. A
   cyclical peak needs normalising down as much as a trough needs it up.
3. **Picking the averaging window to suit.** Four years is a choice. A
   window that includes only good years, or only bad ones, decides the
   answer. Say which years you used.
4. **Mismatching price and profit.** Excluding interest income from profit
   while valuing the whole company, cash included, understates earnings
   against the price. Adjust both or neither. The
   [P/E post]({% post_url 2026-09-24-price-to-earnings %}) and the
   [EV/EBITDA (enterprise value to EBITDA) post]({% post_url 2026-09-26-ev-ebitda %})
   cover the matching rule.

**Takeaway:** Normalised earnings estimate a typical year's profit by
removing one-offs and smoothing a cycle, so a P/E reflects earning power
rather than one unusual year. Every adjustment is a judgement, so the useful
version shows each one.
