#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a per-post Open Graph / Twitter card image for every post in _posts/.

WHY: jekyll-seo-tag emits og:image and twitter:image from a page's `image:`
front matter, falling back to the site default. Every post used to fall back,
so all 69 posts shared ONE social card (assets/logo.png). Every link to this
blog on Twitter, LinkedIn, WhatsApp or Slack looked identical, which throws away
the single biggest lever on click-through a text blog has.

    python3 scripts/make_og_cards.py            # write cards for all posts
    python3 scripts/make_og_cards.py --check    # exit 1 if any are missing/stale

Output: assets/og/<slug>.png at 1200x630 (the size Twitter, Facebook, LinkedIn
and Slack all render), checked in — the Pages build does not run this.

RE-RUN THIS WHEN A POST TITLE CHANGES, or the card will show the old title.
--check is there so CI can catch that; it compares each card against the title
and series it was generated from, recorded in the PNG's own metadata.
"""
import argparse
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml: pip3 install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# _drafts too: a draft carries the same `image:` front matter it will keep when
# it moves to _posts, so its card should exist before the promotion, not after.
SOURCE_DIRS = [os.path.join(ROOT, "_posts"), os.path.join(ROOT, "_drafts")]
OUT = os.path.join(ROOT, "assets", "og")

W, H = 1200, 630
BLUE, BLUE_LIGHT, INK, MUTED, RULE = "#184f95", "#cde2fb", "#0b0b0b", "#52514e", "#dfe3e8"

# Fallback chain so this runs on a Linux CI box too, not just macOS.
FONTS = {
    "bold": [("/System/Library/Fonts/HelveticaNeue.ttc", 1),
             ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0),
             ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0)],
    "regular": [("/System/Library/Fonts/HelveticaNeue.ttc", 0),
                ("/System/Library/Fonts/Supplemental/Arial.ttf", 0),
                ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0)],
}


def font(kind, size):
    for path, idx in FONTS[kind]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=idx)
            except Exception:
                continue
    sys.exit("no usable %s font found — add one to FONTS in this script" % kind)


def width_of(draw, s, f):
    return draw.textbbox((0, 0), s, font=f)[2]


def wrap(draw, s, f, max_w):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if width_of(draw, trial, f) > max_w and cur:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def tracked(draw, xy, s, f, fill, spacing):
    """PIL has no letter-spacing, so draw the string a character at a time."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += width_of(draw, ch, f) + spacing
    return x


def logo_mark(img, x, y, size):
    """The icon from assets/icon.svg: rounded square, ascending line, end dot."""
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + size, y + size], radius=int(size * 0.17), fill=BLUE_LIGHT)
    pts = [(0.214, 0.714), (0.428, 0.500), (0.571, 0.643), (0.785, 0.214), (0.857, 0.321)]
    px = [(x + a * size, y + b * size) for a, b in pts]
    d.line(px, fill=BLUE, width=max(3, int(size * 0.055)), joint="curve")
    r = max(3, int(size * 0.048))
    cx, cy = px[-1]
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE)


def read_front_matter(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    if not m:
        return None
    return yaml.safe_load(m.group(1))


def smarten(s):
    """Match what kramdown renders on the page, so the card and the post agree.
    Straight quotes in the source become curly in the HTML; a card showing
    'beat its index' next to a page showing ‘beat its index’ looks like a bug."""
    s = re.sub(r'(^|[\s(\[])"', "\\1\u201c", s)
    s = s.replace('"', "\u201d")
    s = re.sub(r"(^|[\s(\[])'", "\\1\u2018", s)
    s = s.replace("'", "\u2019")
    return s


def build_card(title, series_title):
    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)

    d.rectangle([0, 0, 14, H], fill=BLUE)                     # left spine
    logo_mark(img, 74, 62, 74)
    d.text((166, 78), "Wealth Primer", font=font("bold", 34), fill=INK)
    d.text((168, 118), "LEARN. INVEST. GROW.", font=font("regular", 15), fill=MUTED)

    if series_title:
        tracked(d, (76, 214), series_title.upper(), font("bold", 21), BLUE, 2.2)

    # Shrink the title until it fits four lines — long titles are common here
    # ("ROCE (Return on Capital Employed): return on ALL the money...").
    for size in (62, 57, 52, 47, 43, 39):
        f = font("bold", size)
        lines = wrap(d, smarten(title), f, W - 150)
        if len(lines) <= 4:
            break
    lh = int(size * 1.22)
    y = 268
    for line in lines[:4]:
        d.text((74, y), line, font=f, fill=INK)
        y += lh

    d.line([74, H - 92, W - 60, H - 92], fill=RULE, width=1)
    d.text((74, H - 72), "dummynotes.com", font=font("bold", 24), fill=BLUE)
    tail = "Educational content — not investment advice"
    ft = font("regular", 21)
    d.text((W - 60 - width_of(d, tail, ft), H - 69), tail, font=ft, fill=MUTED)
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="verify every card exists and matches its post's current title")
    args = ap.parse_args()

    series_titles = {s["slug"]: s["title"]
                     for s in yaml.safe_load(open(os.path.join(ROOT, "_data", "series.yml")))}
    if not os.path.isdir(OUT):
        os.makedirs(OUT)

    entries = []
    for d in SOURCE_DIRS:
        if os.path.isdir(d):
            entries += [(d, n) for n in sorted(os.listdir(d)) if n.endswith(".markdown")]

    stale, written = [], 0
    for src_dir, name in entries:
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name[: -len(".markdown")])
        fm = read_front_matter(os.path.join(src_dir, name))
        if not fm:
            continue
        title = fm.get("title", "")
        series_title = series_titles.get(fm.get("series"), "")
        stamp = "%s\x1f%s" % (title, series_title)
        dest = os.path.join(OUT, slug + ".png")

        if args.check:
            if not os.path.exists(dest):
                stale.append("%s (missing)" % slug)
                continue
            got = Image.open(dest).info.get("wp-stamp")
            if got != stamp:
                stale.append("%s (title/series changed since the card was made)" % slug)
            continue

        meta = PngImagePlugin.PngInfo()
        meta.add_text("wp-stamp", stamp)
        build_card(title, series_title).save(dest, "PNG", optimize=True, pnginfo=meta)
        written += 1

    if args.check:
        if stale:
            print("OG cards out of date — re-run scripts/make_og_cards.py:")
            for s in stale:
                print("  -", s)
            return 1
        print("all OG cards present and current")
        return 0

    total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith(".png"))
    print("wrote %d cards to assets/og/  (%.1f MB total)" % (written, total / 1024.0 / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
