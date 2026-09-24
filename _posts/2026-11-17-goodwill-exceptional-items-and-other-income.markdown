---
layout: post
title: "Goodwill, exceptional items and other income: three lines that arrive with an acquisition"
description: "Desi Bites buys a regional brand. Where the ₹600 lakh went, why 41% of it is goodwill, what an exceptional item is, and how other income flatters profit."
image: /assets/og/goodwill-exceptional-items-and-other-income.png
date: 2026-11-17 09:00:00 +0530
series: fundamental-analysis
term: "Goodwill"
---

{% assign c2 = site.data.case_study_2 %}
{% assign a = c2.acquisition %}
{% assign f = c2.fy26 %}
{% assign r = f.ratios %}
{% assign fy25 = site.data.case_study.income_statement.FY25 %}

## The deal

On {{ a.date }}, Desi Bites Foods bought {{ a.target }} for
₹{% include inr.html n=a.price %} lakh in cash, paid out of the money raised in its June 2025 IPO.
It was the company's first acquisition, and it did three things to the
accounts that hadn't been there before: it put **goodwill** on the balance
sheet, it produced an **exceptional item** on the P&L, and — together with
the interest earned on the IPO cash — it made **other income** a line big
enough to matter.

All three are places where a reader who knows only the ratios from the
first thirty posts will be misled. This post is about reading them.
(Fictional company, fictional deal; the accounting is real.)

## Where the ₹600 lakh went: purchase price allocation

When a company buys another, it doesn't just record "investment: ₹600
lakh." Under Ind AS 103, it has to identify everything it bought, value
each piece at fair value, and record the leftover as goodwill:

```
Goodwill = Purchase price − Fair value of identifiable net assets acquired
```

![Purchase price allocation]({{ '/assets/charts/fa2-purchase-price-allocation.svg' | relative_url }})

For Chatpata Foods:

| What Desi Bites got | ₹ lakh |
|---|---:|
| Plant and equipment (at fair value) | {{ a.fixed_assets }} |
| Inventory | {{ a.inventory }} |
| Trade receivables | {{ a.receivables }} |
| The brand (an identifiable intangible, 10-year life) | {{ a.brand_intangible }} |
| Less: trade payables taken over | −{{ a.payables }} |
| **Identifiable net assets** | **{{ a.identifiable_net_assets }}** |
| **Goodwill** (₹{{ a.price }} − ₹{{ a.identifiable_net_assets }}) | **{{ a.goodwill }}** |

{{ a.goodwill_pct_of_price }}% of the price is goodwill. That's the premium Desi Bites paid over
what it could point to: distributor relationships, a regional customer
habit, the expected savings from running two brands through one sales
force. Goodwill is real in the sense that the money was really spent. It
is not an asset in the sense that anything in the [balance sheet post]({% post_url 2026-08-20-reading-a-balance-sheet %})
was — you can't sell it, depreciate it, or borrow against it.

Two consequences follow.

**Goodwill isn't amortised; it's tested.** The brand intangible is written
off over ten years (₹{{ a.h2_brand_amortisation }} lakh charged in H2 FY26). Goodwill just sits there,
at ₹{{ a.goodwill }} lakh, until management concludes the acquired business is worth
less than they paid — at which point it's *impaired*, in one lump, through
the P&L. Impairments arrive years after the deal, usually in a bad year
when they can be buried, and they are the accounts finally admitting the
price was wrong.

**Goodwill inflates equity and total assets.** Desi Bites' FY26 equity
includes ₹{{ a.goodwill }} lakh of goodwill — {{ r.goodwill_pct_equity }}% of it. Every ratio with equity or
assets in the denominator ([ROE]({% post_url 2026-09-01-roe %}), [ROA]({% post_url 2026-09-05-roa %}),
[P/B]({% post_url 2026-09-25-price-to-book %})) is now a little softer than it looks. Serial
acquirers can have balance sheets that are half goodwill; strip it out
("tangible book value") before comparing them with anyone else.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine buying a friend's lemonade stand for ₹600. The table, the jug and
the leftover lemons are worth ₹355. Why pay ₹600?

Because everyone on the street already knows to buy lemonade from *that*
corner. That habit — the customers who'll keep coming — is worth something,
but you can't put it in a box. Accountants call the extra ₹245 "goodwill"
and write it down as a thing you own.

If the customers stop coming, the ₹245 was wasted, and one day you have to
admit it. That admission is called an impairment.

</details>

## Was it a good deal? The first-year arithmetic

The [capital allocation post]({{ '/series/fundamental-analysis/' | relative_url }}) tomorrow
does this properly. The short version, on the numbers so far:

| Chatpata Foods, H2 FY26 (six months) | ₹ lakh |
|---|---:|
| Revenue | {{ a.h2_revenue }} |
| EBITDA | {{ a.h2_ebitda }} ({{ a.ebitda_margin_h2 }}% margin, vs Desi Bites' {{ r.organic_ebitda_margin }}%) |
| EBIT after depreciation and brand amortisation | {{ a.h2_ebit }} |
| Price ÷ annualised revenue | {{ a.price_to_h2_revenue_annualised }}x |
| **Year-one return on the ₹{{ a.price }} lakh** | **{{ a.year1_roic_pct }}%** |

A {{ a.year1_roic_pct }}% return on money that the [WACC post]({% post_url 2026-10-03-wacc-cost-of-capital %})
said costs about 14% is, in year one, value-destroying. Management's case
is that margins will converge to Desi Bites' own once the brand runs
through its distribution. That's the standard acquisition story and it's
sometimes true. The reader's job is to hold management to it: the deal is
judged on Chatpata's margin in FY27 and FY28, not on the press release.

Note also the blended effect. Desi Bites' own EBITDA margin was
{{ r.organic_ebitda_margin }}%; reported FY26 margin is {{ r.ebitda_margin }}%. The acquisition *diluted* the group
margin while *adding* to revenue growth ({{ r.revenue_growth }}% reported versus
{{ r.organic_revenue_growth }}% organic). A reader who saw "revenue up 27%, margin down" without
knowing about the deal would draw exactly the wrong conclusion about the
core business. Acquisitions change the base; always separate organic from
acquired.

## Exceptional items: the one-off that shouldn't recur

The deal cost ₹{{ a.integration_costs }} lakh in stamp duty, advisers and rebranding. That's a
real cost of FY26 and a cost that has nothing to do with making namkeen,
so it's shown on its own line as an **exceptional item** rather than
inside operating expenses:

| FY26 P&L below EBIT | ₹ lakh |
|---|---:|
| EBIT (operating) | {{ f.ebit }} |
| Other income | +{{ f.other_income }} |
| Exceptional items | {{ f.exceptional_items }} |
| Interest | −{{ f.interest }} |
| **PBT** | **{{ f.pbt }}** |

Separating it is the honest presentation — it lets you see the operating
business without the deal costs. The abuse is in the *labelling*. Watch
for companies whose "exceptional" items are exceptional every single
year: restructuring charges four years running, "one-time" inventory
write-downs each Q4, impairments of last decade's acquisitions. If it
recurs, it's operating, whatever the line says. A useful discipline is
to compute a five-year PAT *including* everything the company called
exceptional; if the total is a large share of profit, the business is
worse than its headline numbers.

The opposite abuse also exists: a genuine one-off *gain* (selling a
building, an insurance receipt) reported inside operating revenue or
other income, where it lifts the margin quietly. The
[forensic post]({% post_url 2026-11-14-desi-bites-cooks-the-books %}) had one of those.

## Other income: when the interest is bigger than the business deserves

**Other income** is everything the company earned that isn't its business:
interest on deposits, dividends on investments, gains on selling assets,
rent, foreign exchange gains. Desi Bites' was zero until the IPO and
₹{{ f.other_income }} lakh in FY26, almost all interest on the ₹1,600 lakh raised and not yet
spent.

| FY26 | ₹ lakh |
|---|---:|
| Other income | {{ f.other_income }} |
| As a share of PBT | **{{ r.other_income_pct_pbt }}%** |
| PAT as reported | {{ f.pat }} |
| PAT excluding other income and the exceptional item (after tax) | {{ r.pat_ex_other_income_and_exceptional }} |

A fifth of Desi Bites' pre-tax profit came from a fixed deposit. That's
not wrong — the money is real — but it's not the snacks business, and it
won't last: the cash is meant to be spent on the things the prospectus
promised. A [P/E]({% post_url 2026-09-24-price-to-earnings %}) computed on ₹{{ f.pat }} lakh values the FD interest
at the same multiple as the brand, which is absurd. Analysts strip it out:
value the operating business on operating profit, and add the cash at face
value.

The reading rule: **other income above about 10% of PBT deserves a
sentence in your notes, and above 20% it deserves a paragraph.** Find out
what it is (the note will list it). Interest on a genuine cash pile is
benign. A gain on asset sales is a one-off wearing a recurring label. A
large "miscellaneous income" line with no explanation is a question for
the next investor call.

## Common mistakes

- **Reading goodwill as an asset like any other.** It's the unexplained
  part of a price. It produces nothing, can't be sold, and is written off
  only when management admits the deal underperformed.
- **Comparing P/B or ROE across companies without stripping goodwill.**
  An acquisitive company's equity is padded with premiums it paid;
  tangible book value is the like-for-like figure.
- **Taking "exceptional" at face value.** Count how many years in the last
  five had one. Recurring exceptionals are operating costs.
- **Valuing other income at the business's multiple.** Interest on cash
  is worth face value, not 38 times.
- **Missing the base change.** Reported growth after an acquisition is
  partly bought. Organic and acquired growth are different facts.
- **Judging the deal on the announcement.** Year-one returns on
  acquisitions are almost always poor. The verdict is the acquired
  business's margin two and three years later — and whether goodwill is
  still on the books at full value.

**Takeaway:** An acquisition brings three new lines a ratio reader can
misread: goodwill (the {{ a.goodwill_pct_of_price }}% of the price nobody could point to, which
pads equity until it's impaired), an exceptional item (honest if it's
truly one-off, an operating cost if it recurs), and other income (a fifth
of Desi Bites' profit came from a fixed deposit, and it deserves a fixed
deposit's valuation, not a brand's). Separate organic from acquired,
operating from other, and judge the deal in year three, not year one.
