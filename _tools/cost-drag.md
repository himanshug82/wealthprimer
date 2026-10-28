---
tool: cost-drag
title: "Cost drag calculator: direct vs regular plan"
description: "Free calculator: what an extra annual cost, like a regular plan's higher expense ratio, takes out of a lump sum over any number of years, in rupees."
image: /assets/og/tool-cost-drag.png
---

## What it does

A fund's [expense ratio]({{ '/2026/09/28/expense-ratios-direct-vs-regular/' | relative_url }})
comes out of its NAV (net asset value) every day, so you never see it charged.
This calculator shows what a difference in that cost adds up to. Enter a lump
sum, the number of years, the lower-cost plan's return after its costs, and
how much more the higher-cost plan charges each year. It shows what each grows
to, the gap in rupees, and the share of the final value the extra cost took.

It starts from the expense ratio post's example: the direct and regular plans
of one actively managed fund. The rates are the exact ones from their daily
NAVs, which is why they carry several decimals: rounded, the answer moves by a
few rupees and no longer matches the post. **Reset to the post's example**
puts them back.

## The formula

```
Lower-cost plan   =  Amount × (1 + r)^N
Higher-cost plan  =  Amount × (1 + r − extra cost)^N
```

r is the lower-cost plan's return a year after its own costs; N is the
number of years. The extra cost compounds: you lose the fee, and also the
growth the fee would have produced.

## What it leaves out

It handles a single lump sum, before tax. It treats the extra cost as a flat
annual percentage, which fits a direct vs regular plan of the same fund; a
product whose charges are built differently, such as a ULIP (unit-linked
insurance plan), needs its own arithmetic. And a lower cost is only half the
comparison: the regular plan's extra cost pays for distribution and advice,
which the post discusses.
