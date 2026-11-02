---
tool: position-size
title: "Position size calculator: shares from a risk budget"
description: "Free position size calculator: turn a risk percentage and an ATR-based stop into a number of shares. The 1% and 2× ATR are conventions, not advice."
image: /assets/og/tool-position-size.png
---

## What it does

[Position sizing]({{ '/2026/10/10/position-sizing-and-the-one-percent-rule/' | relative_url }})
starts from the rupees you are prepared to lose, not the rupees you hope to
make. Enter your capital, the percentage of it you'd lose if the stop is hit,
the share price, its ATR (average true range) and how many ATRs away the stop
sits. The calculator shows the rupees at risk, the stop price, the number of
shares and how big the position is relative to your capital.

It starts from the post's calmest day for one stock, a historical example.
**Reset to the post's example** puts it back.

## The formula

```
Risk (₹)       =  Capital × risk %
Stop distance  =  k × ATR
Shares         =  Risk ÷ Stop distance   (rounded down)
```

## What it leaves out

The 1% risk and the 2× ATR stop are conventions from the trading literature,
not recommended settings. The calculator doesn't pick a stock, a price or a
stop for you. It assumes the stop fills at its price: a gap through it, or a
fast market, loses more than the budget. Brokerage, taxes and slippage aren't
modelled, and a stop-based method doesn't map neatly onto long-term investing
in funds, where there's no stop price.
