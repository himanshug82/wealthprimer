---
name: site-audit
description: Audit the whole Wealth Primer site for SEO and technical health - titles, descriptions, canonicals, headings, images, broken links, orphans, near-duplicates, noindex, JSON-LD, plus local Lighthouse mobile/desktop. Use for "audit the site", "monthly health check", "why does Search Console say X", or after template changes. Read-only: reports, then fixes only what the owner approves.
---

# site-audit

## Run

```
scripts/jekyll_build.sh /tmp/site                        # as live (add --future to include scheduled posts)
python3 .claude/skills/site-audit/scripts/audit_site.py /tmp/site
(cd /tmp/site && nohup python3 -m http.server 8099 >/dev/null 2>&1 &)
.claude/skills/site-audit/scripts/lighthouse_run.sh http://localhost:8099/ /tmp/lh
```

Baseline on 25 October 2026 (see `_review/SEO-AUDIT-2026-10-25.md`): 0 errors, 0 warnings, one intentional noindex (`/series/tax/` until its first post is live); accessibility 100.

## Interpret

- **ERROR** = fix. **WARN** = look; most are small. **INFO** = confirm intent.
- Titles >60 chars: add `seo_title`. Descriptions outside 140–160: edit. Image without dimensions: `python3 scripts/add_img_dims.py`. Orphan: add an internal link from a related post (`post_url` only to earlier-dated; plain relative link for later-dated already-live targets).
- Near-duplicate bodies: decide which URL owns the term; don't delete or rename (no redirects).
- Lighthouse: judge local numbers only. Live runs from the sandbox are inflated by the egress proxy; say so if you report them.
- Search Console issues: see `references/gsc.md`. You can't see Search Console; ask for a screenshot or export.

## Report

Counts per level, each ERROR with the fix, WARN grouped, Lighthouse mobile/desktop scores, and a short "owner-only" list (Search Console, GA4, DNS). Don't change files unless asked; offer the fix PR.
