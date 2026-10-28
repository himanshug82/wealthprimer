---
tool: rolling-returns
title: "Rolling returns calculator for mutual funds and indices"
description: "A free rolling returns calculator: paste any fund's daily NAV or an index and see the worst, median and best N-year CAGR across every start date."
image: /assets/og/tool-rolling-returns.png
---

## What it does

A fund's "5-year return" on a factsheet is one number from one start date.
Move the start date by a few months and the number can change a lot. This
sheet works out the CAGR (compound annual growth rate) for **every** N-year
window in a daily series, one window per start date, and summarises the
spread: the worst, the median, the best, and how often the return fell below
zero or below a threshold you choose.

## How to use it

1. Open the sheet and use **File → Make a copy**.
2. On the **Calculator** tab, change the window length or the threshold.
3. To use another fund or index, paste its dates and values into the
   **Data** tab (columns A and B, from row 2, oldest first) and update the
   description cell.
4. Recalculating several thousand rows can take a few seconds after you
   change an input.

With the default data and inputs, every check on the Calculator tab reads
TRUE: the sheet reproduces the table in the explainer post.

## Price or total return?

Say which you are using. A price index leaves out dividends, so its rolling
returns understate what an investor earned. A fund's growth
[NAV]({{ '/2026/09/25/what-a-mutual-fund-is/' | relative_url }}) (net asset
value) and a total return index include them. The
[benchmarks post]({{ '/2026/10/02/benchmarks-and-comparing-like-with-like/' | relative_url }})
shows how big the gap gets.

## What it can't tell you

Rolling returns describe the past spread of outcomes for the windows that
history happened to contain. They don't predict the next window, and a
series that is only a few windows longer than N says very little.
