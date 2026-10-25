---
name: write-post
description: Draft, outline, edit or SEO-optimise a Wealth Primer blog post (personal finance, trading, fundamental analysis, technical analysis, mutual funds, tax, risk). Use for any request to write, rewrite, plan or improve a post, pick a keyword or title, or check a draft before it is scheduled.
---

# Write a Wealth Primer post

`CLAUDE.md` is the rulebook (voice, compliance, accuracy, style, file conventions) and wins on any conflict. This skill is the **workflow** that applies it, plus the **SEO layer** `CLAUDE.md` doesn't have. Don't restate the rules from memory — open `CLAUDE.md` first in every session and work from it.

The goal is a post that ranks *because* it is the most careful explainer on the topic. This blog cannot win by being louder, so it wins by being right, sourced and clear. Where SEO and compliance pull apart, compliance wins and the post gets a different target keyword.

## Step 0 — Triage the request (before any writing)

| Request looks like | Do |
|---|---|
| "What is / how to calculate / difference between / how to read X" | Write it. |
| "How to pick / evaluate / compare X" | Write it as a *method*. Show how to evaluate; name no winners. |
| Real company used as illustration | Allowed: observables only, one-year backward-looking facts, ≥3-month lag. No valuation or management verdicts, no DCF/WACC/justified multiple. |
| "Best / top N stocks or funds", "multibagger", "should I buy X", "is X a good investment", "X vs Y which is better", "IPO review / GMP", "Nifty target", "intraday tips", "best indicator settings", "is X overvalued", "how to save tax on…" (full list: `references/seo.md` §1) | **Do not target.** Say why, and offer the educational sibling ("how to evaluate…", "what a screener can't tell you", "what the Act allows"). Never put the head term in a title as bait. |
| Tax, SEBI/RBI rule, limit or rate | Allowed, under "Rules, regulations and tax" in `CLAUDE.md`. **Hard stop:** if you cannot open the primary document this session, do not write a circular number, date, rate, threshold or section number. Write "check the current rule", add a VERIFY row, tell the user. Tax posts are delivered as "draft pending professional read", never "ready". |
| Topic outside the six series (emergency fund, EPF/PPF/NPS, insurance) | Scope decision is open in `TODO.md` ("R8"). Don't create a new series; ask. |
| Topic already covered | Search `_posts/` first (`grep -il "<term>" _posts/*`, and `term:` front matter). One term, one owner (`references/seo.md` §2): update the owner post, or give the new post a different intent. When you add links to an older post, still link only to posts dated on or before *that* post. |

If the request is ambiguous on audience level or series, ask one short question. Otherwise decide, state the assumption, and go.

## Step 1 — Place the post

1. **Series**: a slug from `_data/series.yml`. Bump `planned:` there if the series grows.
2. **Prerequisites**: list earlier posts this one will link to (jargon links are mandatory at first use; see `CLAUDE.md` voice rules). Link only to posts dated **on or before** this post.
3. **Date and file**: `_posts/YYYY-MM-DD-slug.markdown`; one post per series per day; front matter `date` matches the filename and the time is ≤ `09:00:00 +0530`. Pick the first free day after the series' last post unless told otherwise. Slug: short, keyword-led, no date, never renamed once live.
4. **Data**: every figure comes from `_data/` via Liquid. If new data is needed, add it through the matching script in `scripts/` (see the table in `TODO.md`), don't hand-edit derived files. Lag is measured from the **post's publish date**, not today: a post dated 12 November 2026 needs data from 12 August 2026 or earlier — **every row and chart point, last one included**, not just the as-of header. Never pull newer data, even if a tool returns it. (New research statistics, e.g. a fresh SEBI study, aren't worked-example prices and may be quoted when released; say so.) Write the as-of date in the post.
5. Desi Bites is fictional, listed on the **NSE and BSE main board** (DRHP Dec 2024, RHP June 2025, listed 15 June 2025) — never "SME". Take its facts from `_data/case_study*.yml`, never from memory; add new facts to the data/script so all posts agree. Only Desi Bites or a generic company gets a DCF, WACC or justified multiple.

## Step 2 — SEO brief (write it down before drafting)

Produce this block in your reply (not in the post):

```
Primary keyword:      <the phrase a reader types>
Secondary / long-tail: <2–4, incl. "how to calculate", "formula", "meaning", "example" variants where natural>
Search intent:        informational | method | rules-lookup
SERP check:           <what the top results are, their format, what they miss>
Our angle:            <what this post does that they don't: common mistakes, Desi Bites worked example, honest limits>
Compliance risk:      <none | what to keep neutral>
```

Run the SERP check with WebSearch when it is available. **Never invent search volumes, rankings or "people also ask" questions** — if you can't check, say so and use the reader-question phrasing you can justify from the topic. See `references/seo.md` for the full SEO rules and per-series keyword patterns.

## Step 3 — Draft to the template

Use the structure in `references/post-skeleton.md` (front matter, Liquid data pattern, section order). Order: Definition → Formula → Worked example → Common mistakes → Takeaway; optional "Explain it like I'm 10" only for genuinely non-obvious concepts. Glossary posts may be shorter; no-formula posts swap in a sourced illustration.

The Takeaway: starts `**Takeaway:**`, 2–3 sentences, first sentence ≤ 280 characters and quotable alone, few figures, no verdict on a real company.

Writing rules that most often slip, all from `CLAUDE.md`: acronyms defined in *every* post; sentence-case headings; ₹ with Indian grouping via `{% include inr.html n=… %}`; "−" not "-"; no line starting "number. "; no hard-coded figures; no series-structure counts ("the next nine posts").

## Step 4 — SEO pass

Apply `references/seo.md`: title (keyword in the first ~45 chars, aim ≤ 60), description (140–160), a direct-answer definition under the first H2 (never a "good" threshold), question-style H2s where natural, descriptive internal links (series hub, jargon owners, one cross-series), primary-source external links, alt text, OG card, `term:` if it defines a term. SEO edits never change a number, a claim, or a heading's meaning.

## Step 5 — Audit like a reviewer

Work through `references/audit.md`. Its core move: **for every interpretive sentence, find the table or figure beside it and check the sentence says no more than the numbers do** — direction, sign, like-with-like, base rate, horizon. Recompute every worked-example figure from its inputs. Then run:

```bash
python3 .claude/skills/write-post/scripts/lint_post.py _posts/<file>   # advisory lint
python3 scripts/check_posts.py                                         # must be 0 errors
python3 scripts/make_og_cards.py                                       # OG card for the new title
```

Then build with future posts (command in `TODO.md` → "Build and publish"; Docker) and **read the rendered page**: a post can pass every script and still say something wrong.

## Step 6 — Hand off honestly

- Log in `TODO.md`: every claim resting on memory or a secondary source as a VERIFY row (claim · post · publish date · basis); every link you couldn't make because the target is dated later as a RELINK/owed link; tax posts as needing the professional read.
- Report to the user: files changed, the SEO brief, what you could not verify, and which checks you ran vs didn't (e.g. "Docker build not run", "professional read pending"). Say "draft", not "ready", until those are done. Don't say "verified" for something you only recomputed from the same inputs.
- Owner decisions the SEO work surfaces (author/`sameAs` metadata, a named reviewer credit, a redirect gem, referral-link policy): flag them, don't implement them.
- Don't commit, push or open a PR unless asked.

## Editing an existing post

Keep the URL (filename date + slug) and the `date`. Add `last_modified_at: YYYY-MM-DD` only for substantive changes — a rule, number or correction, not typos or SEO tweaks (the layout shows "Updated"). If the title changes, re-run `scripts/make_og_cards.py`. Rule or tax changes: re-source from the primary document, update the as-of date, and note it in `TODO.md`.

## Never

Claims of credentials, a team or personal results; buy/sell/hold language, targets, "best" lists of securities or funds, hype words, soft verdicts on real companies, invented citations, unsourced rules from memory, fabricated reader stories or "I made ₹X" claims, a per-post reworded disclaimer, a `{% post_url %}` to a later-dated post.
