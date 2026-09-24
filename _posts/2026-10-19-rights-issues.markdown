---
layout: post
title: "Rights issues: new shares offered to you first, at a discount, and what ignoring them costs"
description: "A rights issue offers existing shareholders new shares at a discount. Ratio, price, renunciation and dilution, worked on a fictional Desi Bites 1-for-5 issue."
image: /assets/og/rights-issues.png
date: 2026-10-19 09:00:00 +0530
series: jargon
term: "Rights issue"
---

{% assign r = site.data.jargon_m7.rights %}
{% assign o1 = r.options[0] %}
{% assign o2 = r.options[1] %}
{% assign o3 = r.options[2] %}
{% assign lapse_loss = o3.net_wealth_change | abs %}

## What a rights issue is

A company that needs money can sell new shares to anyone (a fresh issue or
placement), or it can offer them first to the people who already own it. A
**rights issue** does the second: every existing shareholder gets the
*right* to buy new shares in proportion to what they hold, usually at a
price below the market.

Three terms do most of the work:

- **Ratio** — "1 for 5" means one new share for every five you hold on the
  [record date]({% post_url 2026-10-17-record-date-and-ex-date %}).
- **Issue price** — what you pay per new share, usually at a discount.
- **Rights entitlement (RE)** — the right itself. Since 2020 REs are
  credited to your demat account as a separate security, and you can
  **renounce** them: sell them on the exchange, or transfer them off-market,
  to someone who will subscribe instead (SEBI circular
  [SEBI/HO/CFD/DIL2/CIR/P/2020/13, 22 January 2020](https://nsearchives.nseindia.com/content/equities/SEBI_Circular_22012020_01.pdf)).
  REs that are neither used nor renounced lapse when the issue closes.

SEBI (the Securities and Exchange Board of India) sped the process up in 2025.
For issues approved by a company's board from April 2025, a rights
issue must be completed within 23 working days of that approval; the draft
letter of offer goes to the stock exchanges rather than to SEBI for
observations; the issue stays open for 7 to 30 days; and on-exchange RE
trading closes three working days before the issue does
([SEBI/HO/CFD/CFD-PoD-1/P/CIR/2025/31, 11 March 2025](https://www.sebi.gov.in/legal/circulars/mar-2025/faster-rights-issue-with-a-flexibility-of-allotment-to-specific-investor-s-_92622.html),
under the [ICDR (Amendment) Regulations, 2025](https://www.sebi.gov.in/legal/regulations/mar-2025/securities-and-exchange-board-of-india-issue-of-capital-and-disclosure-requirements-amendment-regulations-2025_92539.html)).

## The formula

Because the new shares come in below market, the share price adjusts when it
goes ex-rights. The standard estimate is the **theoretical ex-rights price
(TERP)** — the same calculation Ind AS 33 uses to adjust EPS for the "bonus
element" in a rights issue:

```
TERP = (Old shares × Price before ex-rights  +  New shares × Issue price)
       ÷ (Old shares + New shares)

Theoretical value of one RE = TERP − Issue price
```

## Worked example: a fictional Desi Bites rights issue

*Every term here is invented for teaching. Desi Bites has announced no
rights issue — and with the cash it holds after its IPO it wouldn't need
one. We borrow only its share count.*

| Term | |
|---|---:|
| Ratio | {{ r.ratio_new }} for {{ r.ratio_held }} |
| Shares before (lakh) | {{ r.shares_before_lakh }} |
| New shares (lakh) | {{ r.rights_shares_lakh }} |
| Issue price | ₹{{ r.issue_price }} |
| Market price just before ex-rights | ₹{{ r.cum_price }} |
| Discount to market | {{ r.discount_pct }}% |
| Money raised | ₹{% include inr.html n=r.raise_lakh %} lakh |

1. TERP = ({{ r.ratio_held }} × {{ r.cum_price }} + {{ r.ratio_new }} × {{ r.issue_price }}) ÷ {{ r.ratio_held | plus: r.ratio_new }} = **₹{{ r.terp }}**.
2. Each RE is worth about ₹{{ r.terp }} − ₹{{ r.issue_price }} = **₹{{ r.re_value }}**: the discount you'd
   capture by subscribing.
3. You hold {{ r.holder_shares }} shares worth ₹{% include inr.html n=r.holder_value_before %} and get {{ r.holder_entitlement }} REs. Your three
   choices, valued at the TERP:

| Choice | You pay | You receive | Shares after | Value of shares | **Change in your wealth** |
|---|---:|---:|---:|---:|---:|{% for o in r.options %}
| {{ o.option }} | {% include inr.html n=o.cash_paid %} | {% include inr.html n=o.cash_received %} | {{ o.shares_after }} | {% include inr.html n=o.holding_value %} | **{% include inr.html n=o.net_wealth_change %}** |{% endfor %}

Subscribing and selling the REs both leave you where you started — one puts
₹{% include inr.html n=o1.cash_paid %} more into the company, the other takes ₹{% include inr.html n=o2.cash_received %} out in cash. Doing nothing
is the only choice that costs money: ₹{% include inr.html n=lapse_loss %}, the value of REs you let lapse.

And the dilution. The share count rises from {{ r.shares_before_lakh }} lakh to
{{ r.shares_after_lakh }} lakh, so a holder who doesn't subscribe ends up with a stake
{{ r.stake_shrink_if_not_subscribing_pct }}% smaller than before. Per-share earnings shrink the
same way until the new money earns something: FY26 profit of ₹{{ r.fy26_pat_lakh }} lakh
is ₹{{ r.eps_before }} a share on the old count and ₹{{ r.eps_after_same_pat }} on the new. Whether the
issue was a good idea depends entirely on what the ₹{% include inr.html n=r.raise_lakh %} lakh earns.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Five friends own a lemonade stand together. It needs a new fridge, so they
decide to make a sixth slice of the stand and sell it cheaply — but only to
themselves first. Each friend can buy a bit of the new slice, or give their
turn to someone else for a small fee.

If you don't buy and don't give your turn away, the stand now has more
slices and yours is a smaller part of it. You didn't get anything for it.

</details>

## Common mistakes

- **Ignoring the rights letter.** Letting REs lapse is the one choice that
  loses money — it hands your discount to whoever does subscribe. If you
  don't want to invest more, selling the REs before RE trading closes is
  the alternative.
- **Thinking the discount is a gift.** A deep discount doesn't make you
  richer; the share price adjusts toward the TERP. A rights issue priced
  at 50% off and one priced at 5% off can raise the same money and be worth
  the same to a shareholder who takes part.
- **Comparing prices across the ex-rights date without adjusting.** Charts,
  EPS and returns all need the rights adjustment, as with a bonus. The same
  bonus element that moves the price also moves reported EPS.
- **Not asking why.** A company raising equity from its own shareholders is
  telling you it wants money. Funding growth is one reason; paying down
  debt it can't service is another. The letter of offer's "objects of the
  issue" section says which — read it the way the
  [DRHP post]({% post_url 2026-10-09-reading-a-drhp %}) reads an IPO's.

**Takeaway:** a rights issue offers new shares to existing holders first,
usually at a discount; the price adjusts, so the discount isn't free money.
Subscribing or selling your rights leaves you whole — letting them lapse is
the one choice that quietly costs you.
