---
name: refresh-post
description: Update an existing published Wealth Primer post that may be stale (rules changed, new data, Search Console shows page-2 queries) without breaking its URL, links or compliance. Use for "refresh this post", "what's stale", "update after the Budget / a new SEBI circular". Prefers improving a post over writing a new one.
---

# refresh-post

## Find candidates

- `python3 .claude/skills/refresh-post/scripts/stale_posts.py` ranks old posts that contain changeable facts (circulars, Tax Year, section numbers, rates).
- Owner-supplied Search Console export: queries at position 8–20 → the post that owns that intent.
- Events: Union Budget (early Feb), new SEBI/CBDT circulars, regulation changes. Use `verify-claims` first to establish what is true now.

## Edit rules

1. **Never rename or delete** a published post (dated URL; no redirects). Edit in place.
2. **Substantive change only** (a rule, number, correction): set `last_modified_at: YYYY-MM-DD` in front matter. Typo, wording or SEO-only edits don't get it — fake freshness is a spam signal.
3. **Say what changed** in the post when a rule changed ("From 1 April 2026 …; before that …"), with the primary source and as-of date. Keep the old rule visible if readers will meet it (historical worked examples).
4. **Links**: `{% post_url %}` only to posts dated on or before this post. A newer target that is already live may be linked with a plain relative link (`{{ '/YYYY/MM/DD/slug/' | relative_url }}`); one still scheduled must not be linked at all (it would 404 on the live site) — log an owed link in `TODO.md` instead.
5. **Numbers** stay in `_data/` via scripts; re-run the derive script, don't hand-edit.
6. **Compliance** unchanged: no verdicts, no tips, lag rule for any new worked-example data, disclaimer from the layout.
7. Title/description changes only when search intent clearly demands (and keep slug). Re-check ≤60-char `<title>`, 140–155 description.
8. Flagged posts (`needs_review`): after a rule change re-check against primary sources, update `rules_as_of` (only if actually re-checked) and `last_modified_at`.

## Finish

`scripts/ship_check.sh`, list the posts changed with one line each on why, and add any owed links/VERIFY rows to `TODO.md`. Ship only when asked.
