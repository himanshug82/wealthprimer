#!/usr/bin/env bash
# Local Lighthouse, mobile and desktop, against a URL (usually a local server of a built site).
#
#   scripts/jekyll_build.sh /tmp/site && (cd /tmp/site && python3 -m http.server 8099 &)
#   .claude/skills/site-audit/scripts/lighthouse_run.sh http://localhost:8099/ [OUTDIR]
#
# Installs lighthouse into ~/.cache/wealthprimer-lh on first use (needs npm). Uses Playwright's
# Chromium (CHROME_PATH or /opt/pw-browsers). Prints category scores and the main lab metrics.
# Live-site runs from the cloud sandbox are distorted by the egress proxy: audit a local build.
set -euo pipefail
url="${1:?usage: lighthouse_run.sh URL [OUTDIR]}"; out="${2:-$(mktemp -d)}"
mkdir -p "$out"
lh="$HOME/.cache/wealthprimer-lh"
if [ ! -x "$lh/node_modules/.bin/lighthouse" ]; then
  mkdir -p "$lh"; (cd "$lh" && npm init -y >/dev/null && npm install lighthouse >/dev/null 2>&1)
fi
chrome="${CHROME_PATH:-$(ls /opt/pw-browsers/chromium-*/chrome-linux*/chrome 2>/dev/null | tail -1)}"
[ -n "$chrome" ] || { echo "no Chromium found; set CHROME_PATH" >&2; exit 1; }
export CHROME_PATH="$chrome"
for mode in mobile desktop; do
  extra=""; [ "$mode" = desktop ] && extra="--preset=desktop"
  "$lh/node_modules/.bin/lighthouse" "$url" $extra --quiet --output=json --output-path="$out/$mode.json" \
    --chrome-flags="--headless=new --no-sandbox" >/dev/null 2>&1 || echo "lighthouse $mode failed" >&2
done
python3 - "$out" <<'PY'
import json, sys, os
for m in ("mobile", "desktop"):
    p = os.path.join(sys.argv[1], m + ".json")
    if not os.path.exists(p): continue
    r = json.load(open(p)); c = r["categories"]; a = r["audits"]
    print(m.upper(), {k: round(v["score"] * 100) for k, v in c.items()})
    print("  ", {k: a[k]["displayValue"] for k in
          ("first-contentful-paint", "largest-contentful-paint", "total-blocking-time", "cumulative-layout-shift")
          if k in a and "displayValue" in a[k]})
    bad = [(a[k]["title"]) for k in a if a[k].get("score") is not None and a[k]["score"] < 0.9
           and a[k].get("scoreDisplayMode") in ("binary", "numeric") and k not in c]
    if bad: print("   below 90:", "; ".join(bad[:8]))
PY
echo "reports in $out"
