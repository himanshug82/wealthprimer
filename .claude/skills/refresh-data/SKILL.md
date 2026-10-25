---
name: refresh-data
description: Check and refresh the datasets behind Wealth Primer worked examples (Nifty 50 TRI, mutual-fund NAVs, price history) while respecting the 3-month lag. Use for "is our data stale", "extend the data for a new post", "add a new fund's NAV". Reports status first; downloads only what a planned post needs.
---

# refresh-data

Worked-example data must be **at least 3 months old on the post's publish date** (house rule, stricter than SEBI's). Data files live in `assets/data/`; `scripts/derive_*.py` turn them into `_data/*.yml`; posts read only `_data/`.

## Steps

1. **Status.** `python3 .claude/skills/refresh-data/scripts/data_status.py [--for-date YYYY-MM-DD]` shows each dataset's last date, the lag cutoff for that post date, which scripts read it, and the next posts. `TOO FRESH` means the file extends past the cutoff, so a post must not use the tail.
2. **Decide.** Do not refresh just because data is old: existing posts state their as-of date and stay valid. Refresh only when a planned post needs a later window, a new fund or a new index, and the target end date is ≤ post date − 3 months.
3. **Download.**
   - Nifty TRI: `fetch_nifty_tri.py --extend assets/data/nifty50-tri.csv --end YYYY-MM-DD` (validated against the committed file: values match).
   - Fund NAV: `fetch_nav.py --search "name"` → `--code N --out assets/data/<slug>.csv --until YYYY-MM-DD`. State plan and option (Regular/Direct, Growth/IDCW) in the post.
   - Price history (e.g. a stock): no scripted source here; ask the owner or use a file they provide (NSE/BSE). Don't scrape.
4. **Re-derive**, never hand-edit `_data/`: re-run the listed `scripts/derive_*.py`, `git diff _data/` and read it. Changed figures in already-published posts mean those posts' as-of dates now disagree with their data — **stop and ask**; extending a file should not change old windows.
5. **Check**: `python3 scripts/check_posts.py`, `scripts/ship_check.sh`, then re-read the numbers in the post against the data.
6. **Record** the source, fetch date and end date in the commit message and in `TODO.md` if a VERIFY item remains.

## Rules

- Source honesty: mfapi.in is a community mirror of AMFI; NSE Indices is the preferred index source. Say which in the post.
- No data inside the lag window in any post, even "for context".
- Commit CSVs only if a script reads them; keep them small and in `assets/data/`.
