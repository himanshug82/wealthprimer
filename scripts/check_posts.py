#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pre-publish checks for every post in _posts/ (and, with --drafts, _drafts/).

WHY: the site publishes on a daily cron with `future: false`, so a post is
built for the first time on its own date, with no human watching. Two classes
of mistake only surface then:

  1. A {% post_url %} that points at a post whose date is LATER than the
     linking post's. That isn't a 404 — it fails the ENTIRE Jekyll build
     ("Could not find post ... in tag 'post_url'"), because unpublished posts
     are not in site.posts. See the build rule in _docs/how-it-works.md.
     A plain link (`{{ '/YYYY/MM/DD/slug/' | relative_url }}`) to a post
     that isn't live yet doesn't fail the build — it is a silent 404 on the
     live site until the target's date — so that is an error here too. Use
     plain text + <!-- RELINK YYYY-MM-DD-slug --> instead; a marker whose
     target is live is a warning (sweep it into a link).
  2. Front matter that the layouts/SEO depend on: a `description` of the
     length Google shows, an `image` that exists in assets/og/, a `series`
     slug that exists in _data/series.yml, a valid date.

Also checks the reader tools: every _data/tools.yml entry has a _tools/<id>.md
page, every tool.html id exists, and each tool's used_in list names real posts.

And the guides (_guides/*.md): every `post:` key names a file in _posts/ (a reschedule
that renames a post must update its guide), every `tool:` is in _data/tools.yml, every
question's post is also in the guide's stages, and the guide has a date and journey.

Also warns (not fails) on: missing `term:` (glossary), two posts from the same series on one date,
a `{{ site.data.X }}` reference to a data file that doesn't exist, and any
Liquid variable of the form `{{ foo.bar }}` whose root `foo` was never
assigned in the post (catches typos in {% assign %} names).

    python3 scripts/check_posts.py            # exit 1 on any error
    python3 scripts/check_posts.py --drafts   # include _drafts/ too

Pure standard library so it runs on the system python3 and in CI.
"""
import argparse
import glob
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.(markdown|md)$")
POST_URL_RE = re.compile(r"{%-?\s*post_url\s+([^\s%]+)\s*-?%}")
# A plain link to a post, e.g. {{ '/2026/11/26/slug/' | relative_url }} or ](/2026/11/26/slug/)
PLAIN_LINK_RE = re.compile(r"(?<![\w/])/(\d{4})/(\d{2})/(\d{2})/([a-z0-9][a-z0-9-]*)/")
RELINK_RE = re.compile(r"<!--\s*RELINK\s+(\d{4}-\d{2}-\d{2}-[a-z0-9-]+)\s*-->")
ASSIGN_RE = re.compile(r"{%-?\s*assign\s+([A-Za-z_][A-Za-z0-9_]*)\s*=")
FOR_RE = re.compile(r"{%-?\s*for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+")
CAPTURE_RE = re.compile(r"{%-?\s*capture\s+([A-Za-z_][A-Za-z0-9_]*)")
VAR_RE = re.compile(r"{{-?\s*([A-Za-z_][A-Za-z0-9_]*)[\.\[\s|}]")
DATA_RE = re.compile(r"site\.data\.([A-Za-z_][A-Za-z0-9_]*)")
TOOL_RE = re.compile(r"{%-?\s*include\s+tool\.html\s+id=\"([^\"]+)\"")
BUILTIN = {"site", "page", "content", "include", "forloop", "layout", "paginator", "jekyll"}


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[m.group(1)] = v
    return fm, text[end + 4:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drafts", action="store_true")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(ROOT, "_posts", "*.markdown")) + glob.glob(os.path.join(ROOT, "_posts", "*.md")))
    if args.drafts:
        files += sorted(glob.glob(os.path.join(ROOT, "_drafts", "*.markdown")))

    series_slugs = set(re.findall(r"^- slug:\s*(\S+)", open(os.path.join(ROOT, "_data", "series.yml"), encoding="utf-8").read(), re.M))
    data_files = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(ROOT, "_data", "*.yml"))}

    posts = {}
    for path in files:
        name = os.path.basename(path)
        m = POST_RE.match(name)
        if not m:
            if "_posts" in path:
                print(f"ERROR {name}: filename is not YYYY-MM-DD-slug.markdown")
            continue
        posts[m.group(1) + "-" + m.group(2)] = (path, date.fromisoformat(m.group(1)))

    errors = warnings = 0
    today = date.today()
    by_date = {}
    tool_refs = []
    # _data/related.yml is generated (scripts/build_related.py); a post missing from it
    # still renders (cards fall back to its own series), but its cards are weaker.
    related_path = os.path.join(ROOT, "_data", "related.yml")
    related_keys = set(re.findall(r"^([a-z0-9][a-z0-9-]*):", open(related_path, encoding="utf-8").read(), re.M)) if os.path.exists(related_path) else set()
    for key, (path, d) in posts.items():
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        fm, body = front_matter(text)
        # One post per SERIES per day is the publishing cadence, so only a
        # clash within the same series is worth flagging.
        by_date.setdefault((d, fm.get("series", "")), []).append(name)

        # --- post_url direction -------------------------------------------
        for target in POST_URL_RE.findall(body):
            if target not in posts:
                print(f"ERROR {name}: post_url target '{target}' does not exist")
                errors += 1
            elif posts[target][1] > d:
                print(f"ERROR {name}: post_url '{target}' is dated {posts[target][1]} — AFTER this post ({d}); the build breaks on {d}")
                errors += 1

        # --- plain links to posts -----------------------------------------
        # These never break the build, so they fail silently: a link to a post
        # that isn't live yet is a 404 on the live site from the day the linking
        # post publishes (or today, if it already has) until the target's date.
        # Use plain text + <!-- RELINK YYYY-MM-DD-slug --> instead.
        for y, mo, dd, slug in sorted(set(PLAIN_LINK_RE.findall(body))):
            target = f"{y}-{mo}-{dd}-{slug}"
            if target not in posts:
                print(f"ERROR {name}: link /{y}/{mo}/{dd}/{slug}/ is not a post (wrong date or slug)")
                errors += 1
            elif posts[target][1] > max(d, today):
                print(f"ERROR {name}: links /{y}/{mo}/{dd}/{slug}/, which publishes {posts[target][1]} — a live 404 from {max(d, today)}; "
                      f"use plain text + <!-- RELINK {target} --> until then")
                errors += 1
        for target in RELINK_RE.findall(body):
            if target not in posts:
                print(f"ERROR {name}: RELINK marker names '{target}', which is not a post")
                errors += 1
            elif posts[target][1] <= today and d <= today:
                print(f"WARN  {name}: RELINK {target} is live now — replace the marker with a link")
                warnings += 1

        # --- front matter -------------------------------------------------
        for k in ("title", "description", "date", "layout"):
            if k not in fm:
                print(f"ERROR {name}: front matter missing '{k}'")
                errors += 1
        desc = fm.get("description", "")
        if desc and not (140 <= len(desc) <= 155):
            print(f"WARN  {name}: description is {len(desc)} chars (aim 140–155)")
            warnings += 1
        if fm.get("date", "")[:10] != d.isoformat():
            print(f"ERROR {name}: front matter date '{fm.get('date')}' disagrees with filename date {d}")
            errors += 1
        if "_posts" in path:
            if fm.get("series") not in series_slugs:
                print(f"ERROR {name}: series '{fm.get('series')}' is not in _data/series.yml")
                errors += 1
            review_kinds = set(re.findall(r"^([a-z][\w-]*):\s*$", open(os.path.join(ROOT, "_data", "review.yml"), encoding="utf-8").read(), re.M))
            if fm.get("series") == "tax" and fm.get("needs_review") != "tax":
                print(f"ERROR {name}: Tax series posts must set needs_review: tax (professional-review notice)")
                errors += 1
            if fm.get("needs_review"):
                if fm["needs_review"] not in review_kinds:
                    print(f"ERROR {name}: needs_review '{fm['needs_review']}' is not a key in _data/review.yml")
                    errors += 1
                if not fm.get("rules_as_of"):
                    print(f"ERROR {name}: needs_review requires rules_as_of (when the facts were last checked)")
                    errors += 1
                if bool(fm.get("reviewed_by")) != bool(fm.get("reviewed_on")):
                    print(f"ERROR {name}: reviewed_by and reviewed_on must be set together (only when a professional really reviewed it)")
                    errors += 1
            if "term" not in fm:
                print(f"WARN  {name}: no term: (won't appear in /glossary/)")
                warnings += 1
        if "_posts" in path and key[11:] not in related_keys:
            print(f"WARN  {name}: not in _data/related.yml (run scripts/build_related.py)")
            warnings += 1
        img = fm.get("image", "")
        if img and not os.path.exists(os.path.join(ROOT, img.lstrip("/"))):
            print(f"WARN  {name}: image '{img}' does not exist yet (run scripts/make_og_cards.py)")
            warnings += 1

        # --- data references and undefined Liquid roots -------------------
        for dref in set(DATA_RE.findall(body)):
            if dref not in data_files:
                print(f"ERROR {name}: site.data.{dref} — no _data/{dref}.yml")
                errors += 1
        defined = set(ASSIGN_RE.findall(body)) | set(FOR_RE.findall(body)) | set(CAPTURE_RE.findall(body)) | BUILTIN
        for root_var in set(VAR_RE.findall(body)):
            if root_var not in defined:
                print(f"ERROR {name}: Liquid variable '{root_var}' is used but never assigned")
                errors += 1

        tool_refs += [(tid, key[11:], name) for tid in TOOL_RE.findall(body)]

        # --- chart references ---------------------------------------------
        for chart in re.findall(r"/assets/charts/([A-Za-z0-9_\-\.]+)", body):
            if not os.path.exists(os.path.join(ROOT, "assets", "charts", chart)):
                print(f"ERROR {name}: chart assets/charts/{chart} does not exist")
                errors += 1

    # --- reader tools: _data/tools.yml, its _tools/<id>.md pages, and the
    # posts that link a tool with {% include tool.html id="..." %} -----------
    tools_path = os.path.join(ROOT, "_data", "tools.yml")
    if os.path.exists(tools_path):
        used_in = {}
        built = {}
        for block in re.split(r"^(?=- id:)", open(tools_path, encoding="utf-8").read(), flags=re.M):
            m = re.match(r"- id:\s*(\S+)", block)
            if m:
                u = re.search(r"^\s+used_in:\s*\[(.*)\]", block, re.M)
                used_in[m.group(1)] = {x.strip() for x in u.group(1).split(",") if x.strip()} if u else set()
                b = re.search(r"^\s+built:\s*(\d{4}-\d{2}-\d{2})", block, re.M)
                built[m.group(1)] = b.group(1) if b else None
        slugs = {k[11:] for k in posts}
        for tid, users in used_in.items():
            stub = os.path.join(ROOT, "_tools", tid + ".md")
            if not os.path.exists(stub):
                print(f"ERROR tools.yml: '{tid}' has no page _tools/{tid}.md")
                errors += 1
            else:
                fm, _ = front_matter(open(stub, encoding="utf-8").read())
                # A tool page with no date gets the BUILD time as its published date
                # (Jekyll gives every collection document one), which changes daily.
                if built.get(tid) and fm.get("date", "")[:10] != built[tid]:
                    print(f"ERROR _tools/{tid}.md: date '{fm.get('date', '')}' should equal built: {built[tid]} in _data/tools.yml")
                    errors += 1
                desc = fm.get("description", "")
                if not (140 <= len(desc) <= 155):
                    print(f"WARN  _tools/{tid}.md: description is {len(desc)} chars (aim 140–155)")
                    warnings += 1
                img = fm.get("image", "")
                if img and not os.path.exists(os.path.join(ROOT, img.lstrip("/"))):
                    print(f"WARN  _tools/{tid}.md: image '{img}' does not exist yet (run scripts/make_og_cards.py)")
                    warnings += 1
            for slug in sorted(users - slugs):
                print(f"ERROR tools.yml: '{tid}' used_in names '{slug}', which is not a post")
                errors += 1
        for stub in sorted(glob.glob(os.path.join(ROOT, "_tools", "*.md"))):
            if os.path.basename(stub)[:-3] not in used_in:
                print(f"ERROR _tools/{os.path.basename(stub)}: no entry with that id in _data/tools.yml")
                errors += 1
        for tid, slug, name in tool_refs:
            if tid not in used_in:
                print(f"ERROR {name}: tool.html id '{tid}' is not in _data/tools.yml (the callout renders nothing)")
                errors += 1
            elif slug not in used_in[tid]:
                print(f"WARN  {name}: links tool '{tid}' but isn't in its used_in list in _data/tools.yml")
                warnings += 1

    # --- guides: _guides/<id>.md (see _layouts/guide.html) -----------------
    tool_ids = set(re.findall(r"^- id:\s*(\S+)", open(tools_path, encoding="utf-8").read(), re.M)) if os.path.exists(tools_path) else set()
    journeys_path = os.path.join(ROOT, "_data", "journeys.yml")
    journey_slugs = set(re.findall(r"^- slug:\s*(\S+)", open(journeys_path, encoding="utf-8").read(), re.M)) if os.path.exists(journeys_path) else set()
    for gpath in sorted(glob.glob(os.path.join(ROOT, "_guides", "*.md"))):
        gname = "_guides/" + os.path.basename(gpath)
        gtext = open(gpath, encoding="utf-8").read()
        gfm, _ = front_matter(gtext)
        head = gtext[3:gtext.find("\n---", 3)] if gtext.startswith("---") else ""
        for k in ("title", "description", "date", "journey"):
            if not gfm.get(k):
                print(f"ERROR {gname}: front matter missing '{k}'")
                errors += 1
        if gfm.get("journey") and gfm["journey"] not in journey_slugs:
            print(f"ERROR {gname}: journey '{gfm['journey']}' is not in _data/journeys.yml")
            errors += 1
        desc = gfm.get("description", "")
        if desc and not (140 <= len(desc) <= 155):
            print(f"WARN  {gname}: description is {len(desc)} chars (aim 140–155)")
            warnings += 1
        question_part, _, stage_part = head.partition("\nstages:")
        stage_keys = re.findall(r"^\s+- post:\s*(\S+)", stage_part.split("\nafter:")[0], re.M)
        for key in sorted(set(re.findall(r"^\s+-? ?post:\s*(\S+)", head, re.M))):
            if key not in posts:
                print(f"ERROR {gname}: post '{key}' is not a file in _posts/ (renamed or rescheduled?)")
                errors += 1
        for key in re.findall(r"^\s+post:\s*(\S+)", question_part, re.M):
            if key not in stage_keys:
                print(f"WARN  {gname}: question post '{key}' is not in the guide's stages")
                warnings += 1
        for tid in re.findall(r"^\s+tool:\s*(\S+)", head, re.M):
            if tid not in tool_ids:
                print(f"ERROR {gname}: tool '{tid}' is not in _data/tools.yml")
                errors += 1

    for (d, ser), names in sorted(by_date.items()):
        if len(names) > 1:
            print(f"WARN  {d}: {len(names)} '{ser}' posts share this date: {', '.join(names)}")
            warnings += 1

    print(f"\n{len(posts)} posts checked: {errors} error(s), {warnings} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
