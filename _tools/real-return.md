---
tool: real-return
title: "Real return calculator: returns after inflation"
description: "Free real return calculator: see what a return bought after inflation, the real rate a year, and how far off the return-minus-inflation shortcut is."
image: /assets/og/tool-real-return.png
---

## What it does

A return in rupees isn't the same as a return in what those rupees buy. Enter
an amount, the number of years, a return a year and an inflation rate. The
calculator shows what the amount grows to, what that is worth in start-year
rupees, the real return a year, and how much you'd need at the end to buy what
the amount bought at the start.

It also shows the common shortcut, return minus inflation, beside the exact
figure. The two are close when the numbers are small and drift apart when
they aren't, which is the point the
[inflation post]({{ '/2026/10/20/inflation-and-real-returns/' | relative_url }})
makes with one of its years.

It starts from that post's example: a one-year SBI fixed deposit rolled over
each year, against CPI (consumer price index) inflation over the same years.
The rates carry several decimals because they're the exact ones; rounded,
the answer no longer matches the post to the rupee. **Reset to the post's
example** puts them back.

## The formula

```
Real return  =  (1 + return) / (1 + inflation)  −  1
             ≈  return − inflation        (only for small numbers)

Worth in start-year rupees  =  Amount × ((1 + return) / (1 + inflation))^N
```

## What it leaves out

It is before tax; tax lowers the real return further. CPI is a national
average basket, and your own costs may rise faster or slower. A constant rate
each year is a summary: real returns jump around from year to year, as the
post's year-by-year table shows.
