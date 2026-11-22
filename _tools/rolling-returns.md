---
tool: rolling-returns
date: 2026-11-22
title: "Rolling returns calculator for mutual funds and indices"
description: "A free rolling returns calculator: paste any fund's daily NAV or an index and see the worst, median and best N-year CAGR across every start date."
image: /assets/og/tool-rolling-returns.png
---

## What it does

A fund's "5-year return" on a factsheet is one number from one start date.
Move the start date by a few months and the number can change a lot. This
calculator works out the CAGR (compound annual growth rate) for **every**
N-year window in a daily series, one window per start date, and summarises the
spread: the worst, the median, the best, and how often the return fell below
zero or below a threshold you choose.

## How to use it

1. Paste two columns into the box: a date and a value (the fund's growth
   [NAV]({{ '/2026/09/25/what-a-mutual-fund-is/' | relative_url }}), net asset
   value, or an index level), one day per line. Or open a CSV file. AMFI's
   NAV history and most index downloads work as they are; a header line and
   extra columns are ignored.
2. Say what the series is, choose the holding periods and set the
   threshold. The results update as you go.
3. Read the table row by row: how many windows there were, the worst,
   median and best CAGR (with the date the worst and best windows began),
   and the share of windows that lost money or fell below your threshold.

To see it on the explainer post's data first, press **Load the worked
example**. Your series never leaves your browser: nothing is uploaded or
saved.

## Price or total return?

Say which you are using. A price index leaves out dividends, so its rolling
returns understate what an investor earned. A fund's growth NAV and a total
return index include them. The
[benchmarks post]({{ '/2026/10/02/benchmarks-and-comparing-like-with-like/' | relative_url }})
shows how big the gap gets.

## What it can't tell you

Rolling returns describe the past spread of outcomes for the windows that
history happened to contain. They don't predict the next window, and a
series that is only a few windows longer than N says very little. They also
don't compare funds: run one series at a time, and compare like with like
(same period, same kind of series) if you run two.
