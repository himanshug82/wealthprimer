# .claude/ — tooling inventory

Project instructions live in `/CLAUDE.md` (rules for what the blog may say). This folder holds the *procedures* and helpers. Nothing here publishes anything by itself; the daily GitHub Pages rebuild does that.

## Skills (`.claude/skills/<name>/SKILL.md`)

| Skill | Use when | Key helper |
|---|---|---|
| `plan-module` | "What should we write next?" - roadmap for approval, no posts | - |
| `write-post` | Draft, edit, audit or SEO-check a post | `scripts/lint_post.py`, `references/{seo,audit,post-skeleton}.md` |
| `verify-claims` | A rule, rate or citation must be checked against the primary source | `scripts/fetch_source.py` |
| `refresh-data` | Datasets stale / new fund or window needed (3-month lag) | `data_status.py`, `fetch_nav.py`, `fetch_nifty_tri.py` |
| `refresh-post` | Update a live post after a rule or data change | `stale_posts.py` |
| `make-chart` | Add an SVG chart in house style | `chartkit.py` |
| `build-calculator` | Specify (then build on request) a Sheet or Python calculator | - |
| `social-hooks` | One-tweet hook per post, with compliance flags | `hooks.py` |
| `site-audit` | Monthly or post-template-change SEO/technical audit | `audit_site.py`, `lighthouse_run.sh`, `references/gsc.md` |
| `ship` | Pre-merge checks, PR, merge, live verification (only when asked) | `scripts/ship_check.sh`, `verify_live.py` |

Typical flow for a module: `plan-module` → (approve) → `refresh-data` if needed → `write-post` (+ `make-chart`, `verify-claims`) → `post-auditor` agent → `ship`.

## Agents

Full usage guide: the repository `README.md`.

`agents/post-researcher.md` — weekly research for future posts (writes `_review/research/<date>.md` + a TODO row; research only). Scheduled Sundays 06:11 IST (`trig_01B2BK6zgJHbZG6DhFWFykPJ`).

`agents/post-auditor.md` — independent read-only reviewer with a fresh context. Run it on every batch before scheduling; it reports P0/P1/P2 findings and never edits.

## Hooks and settings

`settings.json` registers `hooks/session-start.sh` (cloud sessions only): installs the Python packages the scripts need (pandas, numpy, pyyaml, matplotlib, pillow, requests). Build the site with `scripts/jekyll_build.sh OUT [--future]` (the sandbox has no `jekyll` on PATH).

## CI

- `.github/workflows/pages.yml` - build and deploy; daily 09:00 IST rebuild publishes scheduled posts. The `og-cards` job there is advisory.
- `.github/workflows/pr-checks.yml` - PR checks: `check_posts.py`, lint on changed posts, OG cards, image dimensions, `jekyll build --future`. Not part of publishing; make them required only by choice.

## Scheduled tasks (read-only reporters; created in the owner's Claude account)

1. Daily after the 09:00 IST rebuild: did today's post(s) go live, and does each page pass checks?
2. Monthly: site health audit (`site-audit`) and stale-post list.
3. Yearly, early February: post-Budget review of rules and tax posts (`verify-claims`, `refresh-post`).

They report; they do not edit, merge or publish. IDs (for update/delete): daily `trig_01JpMrvSVsvxtSCvfRnejobK` (04:20 UTC), monthly `trig_01R2mMjNsWCJDAJawwwTui3x` (1st, 05:26 UTC), yearly `trig_01Tqpq9VY1KyQdcAsYQ5K6z7` (5 Feb, 10:41 IST). They were created with no repository source attached: if a fired session shows no repo, attach `himanshug82/wealthprimer` to the task in the Claude routines UI. Until the tooling PR is merged to main, the prompts report that and stop.

## Owner-only things no tool here can do

Search Console (Domain property, sitemap, indexing requests, reading reports), GA4 custom-dimension registration, DNS, AdSense `ads.txt`, a professional read of tax posts, deciding anything marked "owner decision" in `TODO.md`.
