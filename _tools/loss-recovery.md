---
tool: loss-recovery
title: "Loss recovery and leverage calculator"
description: "Free calculator: the gain needed to recover from any fall, and what borrowed money and interest do to the return on your own money, in Indian rupees."
image: /assets/og/tool-loss-recovery.png
---

## What it does

Two questions that look simple and aren't.

- **Getting back from a fall.** A fall and the rise that undoes it are not
  the same size, because the rise starts from a smaller base. Enter any fall
  and the calculator gives the rise needed to break even.
- **The same move, with borrowed money.** Enter your own money, what you
  borrow, the interest rate, how long you hold and the price move. It shows
  your leverage, the interest bill, the rise needed just to cover that
  interest, the return on your own money, and the fall that wipes your own
  money out. If a loss is bigger than your own money, it shows what you'd
  still owe.

It starts from the posts' own examples, so you can check it against them
before trying your own numbers. **Reset to the post's example** puts them back.

## The formulas

```
Gain needed to recover from a fall L  =  1 / (1 − L)  −  1

Interest                     =  Borrowed × rate × months / 12
Profit or loss               =  Position × price move  −  Interest
Return on your own money     =  Profit or loss / Your own money
Fall that takes all of it    =  −(Your own money − Interest) / Position
```

The position is your own money plus what you borrow; leverage is the
position divided by your own money.

## What it leaves out

Brokers don't wait for a position to lose everything: a margin call comes
first, and the position may be sold at the low. Margin rules, interest rates,
brokerage and taxes vary and aren't modelled. The interest rate you start
with is the leverage post's illustrative one, not any broker's.
