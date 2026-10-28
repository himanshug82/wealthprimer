---
tool: dcf
title: "DCF calculator, worked on a fictional company"
description: "A free DCF calculator on Desi Bites Foods, our fictional company: change the forecast, WACC or terminal growth and watch the value per share move."
image: /assets/og/tool-dcf.png
---

## What it does

It values [Desi Bites Foods]({{ '/case-study/' | relative_url }}), the
blog's fictional company, with a five-year DCF (discounted cash flow) and a
terminal value. It then runs the reverse DCF: what terminal growth, or what
scale of cash flows, a given share price implies. A sensitivity grid shows
how far the answer moves when WACC (weighted average cost of capital) and
terminal growth change together.

## How to use it

1. Open the sheet and use **File → Make a copy**.
2. On the **DCF** tab, edit only the yellow cells: the assumptions and the
   five-year forecast. Everything else recalculates.
3. Units are ₹ lakh unless a cell says otherwise. Values are as at
   1 April 2025, after the IPO, and cash flows are discounted at year end.

The **Checks** tab confirms that, with the default inputs, the sheet
reproduces the worked example in the explainer post.

## The formulas

```
FCFF            =  EBIT × (1 − tax) + depreciation − capex − change in net working capital
Terminal value  =  FCFF in the final forecast year × (1 + g) ÷ (WACC − g)
```

FCFF is free cash flow to the firm; g is the terminal growth rate. The
[forecasting post]({{ '/2026/09/29/forecasting-free-cash-flow/' | relative_url }})
builds the forecast and the
[margin of safety post]({{ '/2026/10/01/margin-of-safety-and-sensitivity/' | relative_url }})
shows how sensitive the answer is.

## What it can't tell you

A DCF is only as good as its forecast, and the terminal value is usually
most of the answer. This sheet teaches the method on a company that doesn't
exist. It doesn't value any real listed company, and its output is not a
fair price or a recommendation.
