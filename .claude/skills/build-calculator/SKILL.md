---
name: build-calculator
description: Specify (and, only when the owner asks, build) a reader calculator for Wealth Primer - Google Sheet or Python snippet - such as DCF, rolling returns, SIP/XIRR. Use for "calculator for this post", "make the DCF sheet", "XIRR sheet". Produces a spec the owner can approve; creates files or Sheets only on request.
---

# build-calculator

CLAUDE.md: calculators go where the topic naturally needs one (DCF, rolling returns, SIP/XIRR), not on every post. View-only Google Sheet with "make a copy to use"; Python/pandas when the point is *how* the calculation works (10–20 liftable lines).

## Spec first (always)

Write a short spec and show it before building anything:

| Part | Content |
|---|---|
| Purpose & post | which post, which question the reader can answer with it |
| Inputs | each cell, unit, default (from `_data/`, generic/illustrative company or Desi Bites — never a real company's fair value) |
| Calculations | named ranges and formulas, written out |
| Outputs | what shows, with units; ₹ with Indian grouping where possible |
| Checks | cases to reproduce: the post's worked example must come out equal to the post's figures |
| Disclaimers | "illustration; not advice"; no output that reads as a recommendation or a "fair price" for a real company |

## Starter specs

- **DCF** (Fundamental Analysis): inputs = free cash flow, growth years 1–5, terminal growth, discount rate; outputs = PV per year, terminal value, equity value, per-share value. Defaults from a *generic* company in `_data/`; real listed companies get observables only (no discount rate, no fair value).
- **Rolling returns**: input = NAV/TRI series (paste), window; outputs = min / median / max and share of windows below a threshold. Python alternative: `pandas` `rolling` on the committed CSV. State price vs total return.
- **SIP/XIRR**: inputs = dated cash flows; outputs = XIRR (`=XIRR(values,dates)`), total invested, ending value; add a note that XIRR assumes reinvestment at the same rate and that Sheets and Excel agree to about 4 decimals.

## Build (only on request)

- Google Sheets tools (`mcp__Google_Sheets__*`, via ToolSearch) can create/fill a sheet; **don't create or share anything externally unless the owner asks**, and set view-only before linking from a post.
- Reproduce the post's worked example; screenshot-check values; add the link in the post with "make a copy to use".
- Any Python snippet: ≤ 20 lines, imports at top, runs on the committed CSV, no network.
