# Post skeleton

Copy the shape of a recent post in the same series (e.g. `_posts/2026-09-03-roce.markdown` for a ratio) rather than inventing a layout.

## Front matter

```yaml
---
layout: post
title: "ROCE explained: formula and example"   # the H1; aim ≤ 50 (never > 60), keyword first, sentence case
# seo_title: "…"                    # optional search-result title ≤ 60 when the H1 must be longer
description: "…140–155 characters, primary keyword once, concrete promise…"
image: /assets/og/roce.png          # generate with scripts/make_og_cards.py
date: 2026-09-03 09:00:00 +0530     # matches filename; time ≤ 09:00 +0530 (house convention, _docs/how-it-works.md)
series: jargon                      # slug from _data/series.yml
term: "ROCE (return on capital employed)"   # glossary posts only
# last_modified_at: 2026-10-01      # only on material updates
# needs_review: tax                 # REQUIRED for Tax series and any post stating a tax rule (key in _data/review.yml)
# rules_as_of: "August 2026"        # when the rules were last checked against primary sources (required with needs_review)
# rules_for: "Tax Year 2026-27 (FY 2026-27)"   # optional label shown in the notice
# reviewed_by: / reviewed_on:       # ONLY after a professional actually read it; set together; owner supplies
# toc: false                        # TOC auto-shows at ≥ 6 H2s
---
```

## Data pattern

Assign everything the post uses at the top, then print with Liquid. Never type a figure into prose.

```liquid
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
...
| EBIT (FY25) | {{ db_is25.ebit }} |
```

Simple arithmetic on `_data` values in Liquid (`plus`, `minus`, `times`, `divided_by` with a float, `round`) is fine; write a `scripts/derive_*.py` only when the figure is reused across posts or needs invariants asserted. Inputs for a generic/illustrative example still live in `_data/`, not in prose.

`inr.html` takes a variable, not a filter chain: `assign` first, then `{% include inr.html n=x %}`. It drops a trailing `.0` and gives a true minus, so pass computed floats through it.

Table from a loop — no blank lines between rows, or kramdown ends the table:

```liquid
| Year | Charge |
|---|---:|
{% for y in rows -%}
| {{ y.year }} | {% assign c = y.charge %}{% include inr.html n=c %} |
{% endfor %}
```

Prose rupee amounts: `{% include inr.html n=db_is25.ebit %}`. Table cells with pure numbers are grouped automatically.

## Section order

1. **Definition** (`## What <X> means`) — one or two tight paragraphs; the 40–60-word direct answer first; define every acronym; jargon links.
2. **Formula** (`## The formula`) — in a code block.
3. **Worked example** (`## Worked example: <company>, FY25`) — numbered steps; as-of date stated; source linked; "for illustration only"; Desi Bites first, then at most one real company (house convention, not a CLAUDE.md rule) — observables only, one-year and backward-looking, no verdict.
4. **Common mistakes** (`## Common mistakes`) — 2–4 real misreadings, each concrete, not "don't rely on one ratio".
5. **Takeaway** — paragraph starting exactly `**Takeaway:**`; first sentence stands alone at ≤ 280 characters; no figures crammed in; no verdict on a real company.

Optional, before Takeaway or after Definition:

```markdown
<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

…playful, accurate, never required to follow the post…

</details>
```

No-formula posts (biases, how finfluencers earn, reading a DRHP): replace Formula/Worked example with a sourced illustration; keep Common mistakes and Takeaway. Honest-limits sections are a feature, not a closer to apologise away.

## Series hub link

Link the series page once in the body, e.g. `[Jargon, Decoded]({{ '/series/jargon/' | relative_url }})` (slug from `_data/series.yml`); `post_url` can't target it. The linter looks for `/series/<slug>/`.

## Charts

SVG from a `scripts/make_*` file with a fixed seed, saved in `assets/charts/`; reference with `![alt]({{ '/assets/charts/x.svg' | relative_url }})`. `check_posts.py` errors on a missing chart file. Then run `python3 scripts/add_img_dims.py` (adds width/height from the SVG viewBox; `--check` to verify).
