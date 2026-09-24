---
layout: post
title: "CASA and the deposit franchise: why the cheapest money is the hardest to get"
description: "Current and savings accounts are a bank's cheapest money, so a high CASA ratio is a structural edge. What it measures, why it moves, and the CD ratio beside it."
image: /assets/og/casa-and-the-deposit-franchise.png
date: 2026-11-22 09:00:00 +0530
series: fundamental-analysis
term: "CASA ratio"
---

{% assign b = site.data.real_bank %}
{% assign f25 = b.reported.FY25 %}
{% assign f24 = b.reported.FY24 %}
{% assign d = b.derived_fy25 %}
{% assign casa_lakh_cr = f25.casa_deposits | divided_by: 100000 | round: 2 %}

## The raw material has a price list

The [NIM post]({% post_url 2026-11-21-nim-and-the-spread %}) found HDFC
Bank's cost of funds at about {{ d.cost_of_funds_pct }}% for FY25. That is a
blend. Underneath it, a bank pays wildly different rates for different kinds
of money:

| Source of funds | What the bank typically pays | Stickiness |
|---|---|---|
| Current accounts (businesses' operating accounts) | Nothing | Stays as long as the business banks there |
| Savings accounts | Low — a few percent | Stays for years; people rarely move their salary account |
| Fixed / term deposits | The advertised FD rate — often the highest a bank pays | Repriced at maturity; leaves if a rival pays more |
| Borrowings (bonds, interbank, refinance) | Market rates | Leaves the moment it matures |

Current and savings accounts together are **CASA**. The **CASA ratio** is
their share of total deposits:

```
CASA ratio  =  (Current account deposits + Savings account deposits)  /  Total deposits
```

A bank with a high CASA ratio is paying very little for a large slice of its
raw material. That feeds straight into cost of funds, and from there into
NIM. Two banks lending at the same yield can have very different margins
purely because of what sits on the liability side.

There is no ratio quite like this for a manufacturer. The nearest analogy is
a company that gets a large share of its inputs at a permanent discount
because customers *choose* to leave money with it. That is what a
**deposit franchise** means: the ability to attract cheap, sticky money on
the strength of the brand, the branch network, and the salary accounts.

## Worked example: HDFC Bank, 31 March 2025

From HDFC Bank's [results for the year ended 31 March 2025]({{ b.company.source_url }})
(standalone). ₹ crore, historical, for illustration only. The filing gives the
two CASA components in ₹ billion; converted here (1 billion = 100 crore).

| | ₹ crore |
|---|---:|
| Savings account deposits | {% include inr.html n=f25.savings_deposits %} |
| Current account deposits | {% include inr.html n=f25.current_deposits %} |
| **CASA deposits** | **{% include inr.html n=f25.casa_deposits %}** |
| Term deposits | {% include inr.html n=f25.term_deposits %} |
| **Total deposits** | **{% include inr.html n=f25.deposits %}** |
| **CASA ratio** | **{{ f25.casa_ratio_pct }}%** |

The bank's release states the same figure: "CASA deposits comprising
{{ f25.casa_ratio_pct_reported }}% of total deposits as of March 31, 2025."
So roughly ₹{{ casa_lakh_cr }} lakh crore of the bank's funding costs it very
little, and the remaining two-thirds is priced at term-deposit rates.

## The ratio moved, and why that matters

A year earlier the CASA ratio was {{ f24.casa_ratio_pct_reported_external }}% (as of 31 March 2024, from HDFC Bank's
[Q4 FY24 results](https://www.hdfcbank.com/content/bbp/repositories/723fb80a-2dde-42a3-9793-7ae1be57c87f/?path=/Footer/About+Us/Investor+Relation/Detail+PAges/financial+results/PDFs/2024/20April/Q4FY24-Earnings-Presentation.pdf),
released 20 April 2024; it isn't in the FY25 release itself). Over the same year:

| | FY24 | FY25 | Change |
|---|---:|---:|---:|
| Deposits | {% include inr.html n=f24.deposits %} | {% include inr.html n=f25.deposits %} | +{{ d.deposit_growth_pct }}% |
| Borrowings | {% include inr.html n=f24.borrowings %} | {% include inr.html n=f25.borrowings %} | {{ d.borrowings_change_pct }}% |
| Advances | {% include inr.html n=f24.advances %} | {% include inr.html n=f25.advances %} | +{{ d.advances_growth_pct }}% |
| Deposits as share of funding | {{ f24.deposits_share_of_funding_pct }}% | {{ f25.deposits_share_of_funding_pct }}% | |

The pattern is readable without any inside knowledge. Deposits grew nearly
three times as fast as loans; borrowings shrank by a sixth. The bank was
replacing market borrowings with deposits — and the deposits it added were
mostly term deposits, which is why CASA's *share* fell even as CASA rupees
grew.

The context, widely reported and not analysis: HDFC Ltd, the housing-finance
company, merged into the bank on 1 July 2023. HDFC Ltd was funded largely by
bonds and borrowings, not deposits, so the combined bank started FY24 with a
funding mix heavier in borrowings and a loan book larger than its deposit
base could comfortably carry. Rebuilding deposits faster than loans — visible
in the table — is what that looks like from the outside. Whether it is going
well, or fast enough, is a judgement this blog doesn't make.

## The other ratio on this page: credit-deposit

```
Credit-deposit (CD) ratio  =  Advances  /  Deposits
```

| | FY24 | FY25 |
|---|---:|---:|
| CD ratio | {{ f24.credit_deposit_ratio_pct }}% | {{ f25.credit_deposit_ratio_pct }}% |

A CD ratio near 100% means nearly every rupee of deposits is lent out; the
rest of the loan book is funded by borrowings and equity. For the banking
system as a whole the ratio usually sits well below 100%, because a chunk of deposits must
be parked with the RBI (the **cash reserve ratio**, CRR) or in government
securities (the **statutory liquidity ratio**, SLR) rather than lent. A ratio
well above the pack says the bank is leaning on non-deposit funding — which
is more expensive and less sticky, and is the thing the deposit drive above is
meant to fix.

Read CASA and CD together. CASA tells you how cheap the deposits are; CD tells
you whether there are enough of them.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you run a lemonade stand and you need lemons.

Some neighbours leave lemons on your doorstep every week for almost nothing,
because they like you and it's convenient (that's current and savings
accounts). Others will sell you lemons, but only at the market price, and
they'll go to the stand across the road if it pays a rupee more (that's fixed
deposits and borrowings).

The more of your lemons come from the doorstep, the cheaper your lemonade is
to make. CASA ratio is simply: what share of my lemons arrive almost free?

</details>

## Why CASA is hard to buy

A bank can raise term deposits tomorrow by advertising a higher rate. It
cannot do that with CASA. Savings balances follow salary accounts, which
follow employers, which follow years of relationship-building; current
accounts follow businesses' operating needs. The only lever is service and
reach, and the payoff is slow.

That is why CASA ratio is treated as a measure of franchise quality rather
than a quarterly performance metric, and why a bank that grows deposits
quickly by paying up for FDs is doing something different from one that grows
them through salary accounts — even if both report the same deposit growth.

It also means the ratio has a natural ceiling. When interest rates are high,
savers move money from savings accounts into FDs, and every bank's CASA ratio
drifts down regardless of franchise. Compare across banks in the same year,
not across years for the same bank, unless you account for the rate cycle.

## Common mistakes

- **Reading deposit growth as one number.** ₹1 lakh crore of new term
  deposits at 7% and ₹1 lakh crore of new savings balances at 3% have the
  same effect on the deposit line and a very different effect on cost of
  funds.
- **Comparing CASA ratios across a rate cycle.** Rising rates pull money into
  FDs everywhere. A falling ratio in a high-rate year says less about the
  franchise than the same fall in a low-rate year.
- **Treating a high CD ratio as efficiency.** "Every rupee lent out" sounds
  productive. It also means the loan book is leaning on wholesale funding,
  which is exactly what disappears in a squeeze.
- **Ignoring what current accounts actually are.** They are businesses'
  working balances — volatile day to day, but structurally sticky. A bank
  with a large current-account base has a corporate franchise, not just a
  retail one.

**Takeaway:** CASA is the share of a bank's deposits it gets nearly free —
about {{ f25.casa_ratio_pct }}% for HDFC Bank at March 2025 — and it is the
single biggest reason two banks lending at the same rate can earn different
margins. It can't be bought with a higher FD rate, which is why it's read as a
measure of the franchise; and it should be read alongside the credit-deposit
ratio, which says whether there are enough deposits at all.
