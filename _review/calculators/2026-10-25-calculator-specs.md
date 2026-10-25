# Google Sheet calculators: specs for owner approval (25 Oct 2026)

Three view-only Google Sheets ("File → Make a copy to use") for the posts that
need one (CLAUDE.md, Calculators and code). **Built 25 October 2026** (links below); not yet shared publicly.
Building them creates Sheets in the owner's Google account. They must then be
set to "Anyone with the link: Viewer" before a post links them, and that makes
them public. So both steps wait for the owner's go-ahead (`build-calculator`
skill).

Common to all three:

- A **Read me** tab: what the sheet does, units, "Illustration for education
  only; not investment advice", data source and as-of date. It also tells the
  reader to edit only the yellow input cells.
- Inputs in yellow, outputs in bold. ₹ shown in Indian grouping with the
  custom number format `[>=10000000]##\,##\,##\,##0;[>=100000]##\,##\,##0;##,##0`.
- No output that reads as a recommendation or a fair price for a real company.
- A **Checks** tab that reproduces the post's worked example. Each check shows
  the sheet's value, the post's value and TRUE/FALSE. The owner should see all
  TRUE before linking.

---

## 1. DCF: terminal value post (30 Sep 2026)

| Part | Content |
|---|---|
| Purpose | Let a reader change Desi Bites' forecast and see enterprise value, terminal-value share and value per share move, then run the reverse DCF. |
| Inputs | FY25 revenue 2,592; tax 25%; depreciation 4.5% of revenue; NWC 8.68% of revenue; WACC 13.914%; terminal growth 5%; net debt −1,480; shares 12.5 lakh. Five yearly rows: revenue growth (18, 16, 14, 12, 10%), EBITDA margin (17.2, 17.4, 17.5, 17.5, 17.5%), capex % of revenue (8, 8, 6, 5, 5%). All from `_data/case_study.yml` `dcf:`. Desi Bites only; the sheet carries no real company. |
| Calculations | Per year: revenue = prior × (1 + g); D&A = revenue × dep%; EBIT = revenue × margin − D&A; FCFF = EBIT × (1 − t) + D&A − revenue × capex% − (revenue − prior) × NWC%; discount factor = 1/(1 + WACC)^n. TV = FCFF₅ × (1 + g)/(WACC − g); EV = ΣPV + TV/(1 + WACC)^5; equity = EV − net debt; per share = equity/shares. Reverse DCF: a cell for a target price and a GOAL-SEEK note (Sheets has no built-in goal seek, so a 30-row bisection table finds the implied terminal growth). |
| Outputs | PV of forecast, PV of terminal value, terminal % of EV, EV, equity value, value per share; implied terminal growth for the target price; a 5 × 5 WACC × g sensitivity grid. |
| Checks | Base case = ₹397.72 a share, terminal 74.2% of EV, EV 3,491.5 lakh; implied g at ₹640 = 9.62%; market case (25% growth, 20% margin) = ₹596; aggressive (30%, 22%) = ₹769; sensitivity grid equals `dcf.sensitivity` to the rupee. Source: `scripts/derive_dcf_scenarios.py`. |
| Post change | Under "The calculator", add one line: "Prefer a spreadsheet? [Desi Bites DCF (Google Sheet)](…) — File → Make a copy to use." |

## 2. Rolling returns: rolling returns post (27 Sep 2026)

| Part | Content |
|---|---|
| Purpose | Paste any daily NAV or total-return-index series and see the spread of N-year CAGRs (compound annual growth rates) across every start date, not one point-to-point number. |
| Inputs | Columns A:B: date, NAV, pasted; prefilled with UTI Nifty 50 Index Fund regular growth to 31 March 2026 (`assets/data/uti-nifty50-index-fund-nav.csv`, AMFI via mfapi.in). Window in years (default 5). Threshold % (default 8). A cell saying whether the series is a price index or total return, shown in the output. |
| Calculations | For each row: end date = `EDATE(date, 12 × years)`; end NAV = `XLOOKUP(end, dates, navs, , -1)` (last NAV on or before the end date, matching pandas `asof`); blank if end date > last date; CAGR = (end/start)^(1/years) − 1. |
| Outputs | Windows counted, min / median / max CAGR with their start dates, % of windows negative, % below the threshold. A histogram chart. |
| Checks | With the default data: 5y = 3,685 windows, min −1.58%, median 12.25%, max 26.14%, 1.5% negative, 23.8% below 8%. 3y and 10y rows match `mf.yml` `rolling_returns` (3y: 4,180 windows, min −4.82%, max 31.95%; 10y: 2,453 windows, min 4.39%, max 16.11%). |
| Post change | Replace the `GOOGLE-SHEET-TODO` comment with the link line. |
| Note | About 5,000 rows of formulas. Sheets handles it, but say "can take a few seconds to recalculate" on the Read me tab. |

## 3. SIP / XIRR: SIPs, XIRR and timing myths post (1 Oct 2026)

| Part | Content |
|---|---|
| Purpose | Work out what a monthly SIP (systematic investment plan) became and its XIRR (extended internal rate of return), for any start and end date. A second tab takes any list of dated cash flows. |
| Inputs | Tab "SIP": monthly amount (₹10,000), start date, end date, NAV series (same as sheet 2, pasted). Tab "Any cash flows": date and amount columns (outflows negative). |
| Calculations | Instalment dates = the same day each month from start, up to and including the valuation date (as `pd.date_range(..., freq="MS")` does); price = last NAV on or before that date (`XLOOKUP … -1`); an instalment before the first NAV is skipped and counted (the post's 239-not-240 point); units = amount/price; final value = Σunits × NAV on or before the end date. XIRR = `XIRR(values, dates)` with the final value as the last positive flow. |
| Outputs | Instalments, skipped instalments, total invested, final value, XIRR; for comparison, the same total as a lump sum on the start date (its CAGR). |
| Checks | Full 20 years (1 Apr 2006 – 31 Mar 2026): 239 instalments, ₹23,90,000 in, ₹77,80,190 out, XIRR 10.69%. Last 5 years: 60, ₹6,00,000 → ₹6,88,376, 5.44%. Jan 2007 – Jan 2012: 61, ₹6,10,000 → ₹6,09,712, −0.02%. All from `mf.yml` `sip.scenarios`. Sheets' XIRR uses a 365-day year and the post's Python 365.25, so they can differ by up to about 0.01 percentage point (10.68% vs 10.69% for the full 20 years); the check allows ±0.01. |
| Notes | Say on the Read me tab that XIRR assumes every flow is reinvested at the same rate, and that the model ignores stamp duty, exit loads and tax. |
| Post change | Replace the `GOOGLE-SHEET-TODO` comment with the link line. |

---

## As built (25 October 2026)

| Sheet | Link | Checks |
|---|---|---|
| Desi Bites DCF | https://docs.google.com/spreadsheets/d/1bcK0b7i_-xZKrH_MGSuW0b78CPBrN31v3LEC-ssNfro/edit | all TRUE (EV within ₹0.1 lakh: the post adds two rounded parts) |
| Rolling returns | https://docs.google.com/spreadsheets/d/1O8HKLVxA5V3rzWz1FfQ12wVqvQ0MfyvKEEK4EUTN3v4/edit | all TRUE at 5 years; 3 years checked by hand (4,180 windows, −4.82%, 11.82%, 31.95%) |
| SIP and XIRR | https://docs.google.com/spreadsheets/d/1GhKA_QTOxRAM2_nokMzj-ouciaRpHZYwYuojFxcXSBo/edit | all four scenarios TRUE |

Differences from the spec: the NAV history is pasted as values (Sheets'
`IMPORTDATA` needs each copy to click "Allow access"); the reverse DCF uses a
closed-form solve instead of a bisection table; the rolling-returns checks
cover the 5-year window automatically and list the other windows to check by
eye. The posts link to these sheets. **Owner step before the links go live:**
in each sheet, Share → General access → "Anyone with the link" → Viewer (the
sharing tool available here can only share with named people).
