---
name: make-chart
description: Make a Wealth Primer chart (SVG) in the house style from committed data, reproducibly, with alt text and dimensions. Use for "add a chart to this post", "draw X vs Y", "make a diagram". For anything that plots market prices, applies the 3-month lag and as-of date.
---

# make-chart

1. **Decide the one claim** the chart supports. If the table already says it, skip the chart. Chart type by purpose: trend → line, comparison → bars, distribution → histogram/box; no 3D, no dual axes unless unavoidable.
2. **Data**: only from `assets/data/*.csv` or `_data/*.yml`. Run `refresh-data/scripts/data_status.py` if you need later data; the window must end ≥ 3 months before the post date.
3. **Script**: add `scripts/make_<series>_charts.py` (or extend the existing one for the module) using `.claude/skills/make-chart/scripts/chartkit.py` (palette, fonts, source line, byte-stable SVG). Fixed random seed for simulations. Output to `assets/charts/<series>-<name>.svg`.
4. **Honest labelling**: title states what and when; axis units (₹, %, index level); say price index vs total-return; source line with as-of date; no truncated y-axis that exaggerates (or label it); don't mark "buy/sell" points.
5. **In the post**: `![Alt text describing the content and the period]({{ '/assets/charts/x.svg' | relative_url }})`. Alt text names the series and date range, e.g. "Nifty 50 TRI and a fund's NAV rebased to 100, April 2016 to March 2026". Then `python3 scripts/add_img_dims.py` (adds width/height) and `python3 scripts/check_posts.py` (errors on missing files).
6. **Check**: open the SVG in a browser render (Playwright screenshot) at mobile width; text must be legible, no clipped labels. Look at it; don't assume.
7. Size: keep SVG under ~150 KB (thin out points with resampling rather than rasterising).

Diagrams (flows, balance-sheet boxes): follow `scripts/make_diagrams.py` / `make_fa2_diagrams.py`.
