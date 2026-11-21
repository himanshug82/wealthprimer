---
tool: goal
date: 2026-11-21
title: "Goal-based investing calculator: cost, lump sum, SIP"
description: "Free goal calculator: inflate a cost to the year it falls due, then see the lump sum or monthly SIP, flat or stepped up, at a return you assume."
image: /assets/og/tool-goal.png
---

## What it does

Start from what the money is for. Enter what the goal costs today, how many
years away it is, the inflation you assume for that cost and the yearly
return you assume the money earns. The calculator shows what the goal may
cost when it falls due, and three ways of getting there under those
assumptions: a lump sum invested today, a flat monthly SIP (systematic
investment plan) and a SIP that rises by a fixed percentage each year.

The starting figures are an illustrative goal (₹10 lakh today, 12 years
away), not a recommendation. **Reset to the post's example** puts them back;
the example is worked step by step in this blog's goal-based investing post,
published 24 January 2027.

## The formula

```
Future cost       =  cost today × (1 + inflation) ^ years
Lump sum today    =  future cost / (1 + return) ^ years
Monthly amount    =  future cost / FV (future value) of ₹1 a month

FV of ₹1 a month  =  Σ (1 + m) ^ k  for k = 1 … months,   m = (1 + return) ^ (1/12) − 1
```

Each instalment is paid at the start of the month. With a step-up, the
instalment rises once a year, and the first year's amount is set so the total
still reaches the future cost.

## What it leaves out

It assumes the return arrives at a steady rate every month. Real returns
don't: the same average can end in very different places depending on the
order of good and bad years. It ignores tax and costs, and it treats the
goal's inflation as one fixed rate. Small changes in either assumption move
the answer a lot over long periods, so it's worth running a few combinations
rather than trusting one.
