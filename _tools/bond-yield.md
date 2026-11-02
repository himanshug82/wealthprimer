---
tool: bond-yield
title: "Bond price, yield and duration calculator (YTM)"
description: "Free bond calculator: turn a yield into a price and duration, or a price into the yield to maturity. Annual coupons, whole years, a fictional bond."
image: /assets/og/tool-bond-yield.png
---

## What it does

A bond's price and its yield are the same fact said two ways. Enter the face
value, the coupon and the years to maturity. Then either give a yield and see
the price, the
[duration]({{ '/2026/10/06/modified-duration/' | relative_url }}) and what a
one-point move in yields does to the price, or give a price and see the
[yield to maturity]({{ '/2026/10/05/yield-to-maturity/' | relative_url }}) it
implies.

It starts from the YTM post's fictional bond: ₹1,000 face value, a 7% coupon,
five years, bought at ₹960. **Reset to the post's example** puts those back.

## The formula

```
Price  =  Σ  coupon / (1 + y)^t   +   face / (1 + y)^n

Macaulay duration  =  Σ  t × PV(cash flow t)  /  Price
Modified duration  =  Macaulay duration / (1 + y)
```

There is no closed form for the yield given a price, so the calculator
searches for the rate that makes the discounted cash flows equal the price.

## What it leaves out

One annual coupon and whole years, as in the posts; Indian government bonds
usually pay half-yearly, so a real bond's figures differ a little. Price
excludes accrued interest, tax, charges and any call or put feature. Modified
duration is a straight-line estimate, which is why it misses the actual price
change a little for larger moves. The calculator is arithmetic on a bond you
type in. It doesn't say whether any real bond is worth buying.
