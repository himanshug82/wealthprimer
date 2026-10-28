---
tool: sip-xirr
title: "SIP and XIRR calculator"
description: "A free SIP and XIRR calculator: see what a monthly SIP into a fund became between any two dates, or the XIRR of any list of dated cash flows."
image: /assets/og/tool-sip-xirr.png
---

## What it does

The sheet has two calculators.

- **SIP tab.** What a monthly SIP (systematic investment plan) into a fund
  became between two dates, and its XIRR (extended internal rate of
  return): the single annual rate that makes every dated cash flow add up.
- **Any cash flows tab.** The XIRR of any list of dated amounts: a step-up
  SIP, irregular top-ups, a part-withdrawal.

## How to use it

1. Open the sheet and use **File → Make a copy**.
2. On the **SIP** tab, change the instalment, the first instalment date or
   the valuation date (the yellow cells). Instalments fall on the same day
   each month, up to and including the valuation date.
3. For anything that isn't a level monthly SIP, list each date and amount on
   the **Any cash flows** tab: money in as a negative number, the final value
   as a positive one.
4. To use another fund, paste its dates and NAVs into the **Data** tab
   (columns A and B, from row 2, oldest first).

The **Checks** tab reproduces the SIP scenarios in the explainer post; with
the default data every row reads TRUE.

## How each instalment is priced

At the last NAV (net asset value) published on or before the instalment
date. An instalment dated before the fund's first NAV is skipped. Google
Sheets counts a year as 365 days and the post's Python uses 365.25, so XIRR
can differ in the second decimal place.

## What it leaves out

Stamp duty on purchases, [exit loads]({{ '/2026/10/07/exit-load/' | relative_url }})
and tax. A growth NAV is already after the fund's
[expense ratio]({{ '/2026/09/28/expense-ratios-direct-vs-regular/' | relative_url }}).
XIRR also assumes every cash flow earned the same rate, which is a summary,
not a description of what each instalment did.
