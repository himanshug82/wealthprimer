---
layout: post
title: "Margin pledge: using your shares as collateral"
seo_title: "Margin pledge explained: shares as collateral for trading"
description: "A margin pledge lets shares in your own demat account serve as collateral with your broker. How pledge and re-pledge work, the haircut, and invocation."
image: /assets/og/margin-pledge.png
date: 2027-02-18 09:00:00 +0530
series: market-basics
term: "Margin pledge"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign p = site.data.market_basics_m2.pledge %}

## What a margin pledge is

Trading in derivatives, or intraday, needs
[margin]({% post_url 2026-10-11-leverage-and-margin %}): money or collateral
held against possible losses. A **margin pledge** lets you use shares you
already own as that collateral, without selling or moving them. They stay in
your own demat account, marked as pledged to your broker, and the broker
passes the pledge on to the clearing corporation that settles trades.

Since 1 June 2020 this has been the only way brokers may take securities from
clients as collateral, under a circular of 25 February 2020 from SEBI (the
Securities and Exchange Board of India). This post sets out how it works, as
read in November 2026. It's distinct from a
[promoter pledge]({% post_url 2026-10-06-contingent-liabilities-pledges-and-promoter-holding %}),
where a company's founders borrow against their own shares. It's part of
[Your first year in the market]({{ '/series/market-basics/' | relative_url }}).

## The rules

From SEBI's [circular of 25 February 2020]({{ p.url2020 }}) and its
amendment of [3 June 2025]({{ p.url2025 }}):

| Step | What happens |
|---|---|
| Pledge | You pledge securities to your broker's "Client Securities Margin Pledge Account", by an instruction you confirm, for example with a one-time password. The shares stay in your demat account |
| Release | You ask the broker to release the pledge; it does so after its own exposure and risk checks |
| Re-pledge | The broker re-pledges them to its clearing member, which re-pledges them to the clearing corporation. The whole trail shows in your demat account |
| Use | Securities re-pledged to the clearing corporation can give margin to you only, not to the broker's other clients |
| Invocation | If you don't meet a [margin call]({% post_url 2027-01-07-margin-calls-and-peak-margin %}) or a debit, the broker can invoke the pledge and sell the shares to recover the money |

The 2025 amendment changes two steps. When you sell pledged shares, a single
instruction is to release the pledge and block the shares for delivery. And
invoked shares are to be blocked for delivery in your own account rather than
moved out first, with exceptions such as mutual fund units and accounts barred
from trading. The amendment was due to apply from 5 September 2025; SEBI
later extended that date by another circular, which this post hasn't checked.
Ask your broker whether these steps are in force.

## Worked example: what the pledge is worth

A hypothetical investor pledges shares worth ₹{% include inr.html n=p.holding %}.
The margin they count for is less than that: a **haircut** is taken off,
because the shares could fall before they're sold. The rate depends on the
stock and on the clearing corporation's rules; here it is assumed to be
{{ p.haircut_pct }}%.

```
Margin credit           =  market value × (1 − haircut)
                        =  ₹{% include inr.html n=p.holding %} × (1 − {{ p.haircut_pct }}%)  =  ₹{% include inr.html n=p.credit %}
```

**If the shares fall {{ p.fall_pct }}%**, their value drops to
₹{% include inr.html n=p.holding_after %} and the margin credit to
₹{% include inr.html n=p.credit_after %}, ₹{% include inr.html n=p.credit_drop %}
less. If the positions it supports still need the old amount, that's a
shortfall: a margin call. Not meeting it is what lets the broker invoke the pledge.

So the shares you pledge carry two risks at once: their own price, and any
loss on the trades they support. A fall in the market can hit both on the same
day.

## Common mistakes

1. **Thinking pledged shares are sold or moved.** They stay in your demat
   account, marked as pledged, until released or invoked.
2. **Counting the full market value as margin.** The haircut cuts it, and the
   credit falls further when the shares fall.
3. **Expecting a release on demand.** The broker releases a pledge after its
   own risk checks, and pledged shares have to be released before they can be
   delivered on a sale.
4. **Assuming invocation needs your consent each time.** Agreeing to the
   pledge includes consent to re-pledge, and the broker can invoke it if you
   default on a margin call.

**Takeaway:** A margin pledge lets shares in your own demat account count as
margin, after a haircut, without selling them. They stay yours until you
default on a margin call, when the broker can invoke and sell them.

## Sources

- SEBI circular SEBI/HO/MIRSD/DOP/CIR/P/2020/28, [25 February 2020]({{ p.url2020 }}): "Margin obligations to be given by way of Pledge/Re-pledge in the Depository System", paras 2–9 and Annexure A, read on 21 November 2026.
- SEBI circular SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/82, [3 June 2025]({{ p.url2025 }}): pledge release for early pay-in, and invocation blocked for pay-in (para 4 and its exceptions), due to apply from 5 September 2025 (para 6). Its start date was later extended by another circular, not checked here.
