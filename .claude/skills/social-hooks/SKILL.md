---
name: social-hooks
description: Draft the one-tweet hook (Takeaway first sentence plus link) for a Wealth Primer post, with compliance flags. Use for "tweet for this post", "social copy", "announce today's post". Twitter is distribution, not a second content stream - no threads that repeat the post.
---

# social-hooks

1. Run `python3 .claude/skills/social-hooks/scripts/hooks.py _posts/<file>` (one or many). It prints the Takeaway's first sentence (must stand alone at ≤ 280 characters), the live URL, and flags from the write-post word lists.
2. **Fix at the source.** If the hook is too long, vague or flagged, edit the Takeaway in the post (small wording edit; no `last_modified_at`), not just the tweet.
3. Output per post: *hook + link*, optionally one alternative that opens with the reader's question. Nothing more.

## Rules

- No stock names framed as signals, no "buy/sell", no targets, no performance claims, no hype words, no emojis that imply gains, no hashtags that look like tips (#multibagger, #stocktowatch).
- A real company named only as in the post's illustration; no verdict.
- Don't link a post that isn't live yet (`NOT LIVE YET` in the output) — draft for its publish date.
- Don't invent engagement numbers, quotes or reader stories.
- The owner posts; this skill never posts anywhere.
- Disclosure/disclaimer lives on the site; link goes to the post, which carries it.
