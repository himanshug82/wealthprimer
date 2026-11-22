# Spec: on-page rolling returns calculator (for owner approval, 22 Nov 2026)

Master plan §7 item 6. Nothing is built until this is approved.

## Why

- **Search evidence:** rolling returns is the site's largest query cluster: 14 variants, 46 impressions on the post at position 72.6. 6 of the 14 are explicit calculator searches ("rolling returns calculator", "how to check rolling returns of mutual funds"). The tool page `/tools/rolling-returns/` has no impressions, because it only describes a Google Sheet (`_review/sprint-1/technical-seo-audit.md` §4–5).
- **Reader need:** the post explains the method; the reader then wants to run it on their own fund or index without making a copy of a Sheet with several thousand rows that takes seconds to recalculate.
- **Hypothesis to check:** an on-page calculator at the same URL gives searchers what they came for and gives the page something to rank with. We judge it on Search Console impressions for the calculator queries and on `calculator_start` / `calculator_complete` events, 8 weeks after launch.

## Scope check (D3)

| D3 rule | How the spec meets it |
|---|---|
| Runs on the reader's own inputs | The reader pastes or opens their own NAV or index history. |
| No real-fund data for the reader to pick from | There is no fund list, search box or picker. The only built-in data is the post's worked example, one series, loaded by a clearly labelled button. |
| Never ranks, screens or scores | One series at a time. No comparison across funds, no "good/bad" labels, no ranking. |
| Never reviews holdings or says what to do | Outputs are the distribution only: counts, worst, median, best, shares below thresholds. No verdicts. The page's "What it can't tell you" section stays. |
| Defaults reproduce the post, labelled | The worked example is labelled with fund, plan, source and as-of date (31 March 2026, more than 3 months old). |

## Inputs

| Input | Detail | Default |
|---|---|---|
| Series | Textarea: two columns, date and value, one row per day. Or **Open a CSV file** (read in the browser with `FileReader`; nothing is uploaded). | Empty, with the worked example shown as a result (see Outputs) and a button **Load the worked example**, which fetches `/assets/data/uti-nifty50-index-fund-nav.csv` (already published, 128 KB) and fills the box with its date and regular-plan columns |
| What the series is | Fund growth NAV / Total return index / Price index. Changes only the note under the results (a price index leaves out dividends, so it understates returns). | Fund growth NAV |
| Holding periods | Checkboxes 1, 3, 5, 7, 10 years, plus one optional custom whole number from 1 to 30 | 1, 3, 5, 7, 10 |
| Threshold | "% of windows below ___% a year" | 8 (the post's FD comparison) |

**Parsing rules:**
- Separators: comma, tab, semicolon or runs of spaces. A header row is skipped if its value column isn't a number.
- Date formats: `2026-03-31`, `31-03-2026`, `31/03/2026` and `31-Mar-2026` (AMFI's format). Day-first is assumed for the numeric forms, and the page says so.
- Values: Indian or plain grouping is accepted ("1,00,000"); a value must be above 0.
- Rows are sorted by date. A repeated date keeps the last row. Blank lines are ignored.
- Up to 25,000 rows (about 100 years of trading days).

**Messages:**
- Invalid input shows an error and no result; the form gets `calc-invalid`, so analytics sees it as not completed.
- A period longer than the data shows "needs at least N years of data".
- Warnings, which still show results:
  - fewer than 250 windows for a period ("a series only a little longer than N years says very little");
  - a gap of more than 10 calendar days between rows ("check for missing data").

## Calculation (identical to the post)

For each holding period N:

```
for each row d in date order (each start date):
    end = d + N calendar years      (29 February → 28 February in a non-leap year)
    if end > last date: stop
    value_end = value on the last date on or before end      (pandas "asof")
    cagr(d) = ((value_end / value(d)) ^ (1 / N) − 1) × 100
windows  = count of cagr values
worst    = min, with its start date;  best = max, with its start date
median   = middle value (mean of the two middle values when the count is even)
% negative          = share of windows with cagr < 0
% below threshold   = share of windows with cagr < threshold
```

The lookup of the end value uses binary search, so each period runs in O(n log n). Twenty years of daily data runs in well under a second on a phone.

**Verified today:** this method, run in pandas on the committed CSV, reproduces every figure in the post's table (`_data/mf.yml` → `rolling_returns`):

| Period | Windows | Worst | Median | Best | % negative | % below 8% | Worst start | Best start |
|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 y | 4,670 | −56.3 | 11.77 | 96.01 | 18.9 | 39.3 | 2007-11-20 | 2020-03-23 |
| 3 y | 4,180 | −4.82 | 11.82 | 31.95 | 2.9 | 27.9 | 2017-03-23 | 2020-03-23 |
| 5 y | 3,685 | −1.58 | 12.25 | 26.14 | 1.5 | 23.8 | 2007-11-19 | 2020-03-23 |
| 7 y | 3,192 | 3.57 | 11.66 | 18.29 | 0.0 | 15.4 | 2008-01-07 | 2008-10-27 |
| 10 y | 2,453 | 4.39 | 11.81 | 16.11 | 0.0 | 14.0 | 2010-03-23 | 2009-03-12 |

(Data 3 April 2006 to 31 March 2026, 4,915 rows. The 1-year row matches the post's "81.1% ended higher".)

## Outputs

1. **Results table**, one row per holding period: windows; worst, median and best CAGR (% a year, 2 decimals); the start dates of the worst and best windows; % negative; % below the threshold. A header line states the series' first and last date and row count.
2. **Range chart** (inline SVG, drawn by the script, house palette): one horizontal bar per period from worst to best, with a dot at the median and the threshold as a dashed line. It sits under the table, which stays the main, accessible output. The chart has a text alternative.
3. **Note under the results**, depending on the series type: what NAV, TRI or price index includes. Plus a fixed line: "Past windows describe what happened, not what the next window will do."
4. **On first load** (no data pasted): the worked-example table is shown as static HTML from `_data/mf.yml`, labelled "Worked example: UTI Nifty 50 Index Fund, regular plan, growth, 3 April 2006 – 31 March 2026 (AMFI via mfapi.in), for illustration only". Searchers see a real result straight away, crawlers can read it, and the page doesn't load 128 KB up front.

Percentages are shown to 2 decimals and counts with Indian grouping. Negative values use "−".

## Privacy and analytics

- **Privacy:** the series never leaves the browser. No storage, no network request except the optional worked-example CSV from this site.
- **Analytics:** the existing events work unchanged. `calculator_start` fires on the first edit; `calculator_complete` fires on a valid result after a 2-second pause. `calculator_id` is `rolling-returns`. Nothing about the series or results is sent.

## Implementation plan (one PR, size M)

| File | Change |
|---|---|
| `assets/js/calc.js` | Pure functions `parseSeries(text)` and `rollingReturns(dates, values, years, threshold)` (numbers in, numbers out, testable in Node), plus a separate render path for this form (textarea, table, SVG). The existing calculators are untouched |
| `_includes/calc/rolling-returns.html` | The form, the static worked-example table and the labels |
| `_data/tools.yml` | `rolling-returns`: `kind: Calculator`, `calc: rolling-returns`; the Sheet stays as a new `sheet:` field |
| `_layouts/tool.html` | Show "Prefer a spreadsheet? Make a copy of the Google Sheet" when `sheet:` is set |
| `_tools/rolling-returns.md` | Rewrite "How to use it" for the on-page tool; keep "Price or total return?" and "What it can't tell you". **Same URL and title**, description lightly edited (no retitle) |
| `scripts/derive_tool_defaults.py` → `_data/tool_defaults.json` | Add cases from `_data/mf.yml` (all 30 figures above) and parser cases (AMFI date format, header row, Indian grouping, duplicate date, unsorted input) |
| `scripts/check_tools.mjs` | Load the committed CSV and check `rollingReturns` against those cases |
| Rolling returns post | No content change: the pointer and tool callout already point to `/tools/rolling-returns/` |

**Validation before merge:**
- `check_tools.mjs` shows 0 mismatches, and `check_posts.py` 0 errors.
- The site audit and Lighthouse on `/tools/rolling-returns/` (mobile performance should stay 90 or above, since nothing heavy loads up front).
- In the browser: paste and file paths, every error message, phone width, dark mode, the events in `dataLayer`.

## Questions for the owner

1. **Default view:** a static worked-example result on load plus a "Load the worked example" button (recommended), or load the CSV and compute on page load?
2. **Holding periods:** 1, 3, 5, 7 and 10 years plus one custom period (recommended), or only a single period chosen by the reader, as in the Sheet?
3. **Chart:** include the range chart (recommended), or the table only for the first version?
4. **Sheet:** keep it as a secondary "make a copy" link (recommended, per the brief), or retire it?

## Side note found while writing this

The rolling returns post types two figures into prose ("a spread of nearly 37 percentage points", "a spread of under 12"). They are correct (31.95 − (−4.82) = 36.77; 16.11 − 4.39 = 11.72), but CLAUDE.md wants every figure from `_data/`. That is a small fix to make in the same PR or separately.
