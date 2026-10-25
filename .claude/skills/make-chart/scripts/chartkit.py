#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared brand style for Wealth Primer charts (same palette/fonts as the existing make_*_charts.py).

    import sys; sys.path.insert(0, ".claude/skills/make-chart/scripts")
    import chartkit as ck
    fig, ax = ck.figure(w=7.2, h=3.6)
    ax.plot(dates, values, color=ck.NAVY, lw=1.6, label="Fund")
    ck.finish(ax, title="…", source="Source: NSE Indices; as of 31 March 2026", ylabel="₹")
    ck.save(fig, "assets/charts/<series>-<name>.svg")      # fixed metadata so reruns are byte-stable

Rules: data from committed CSVs or `_data/`, never typed values; say price vs total return; date range in the title or
caption; a source line with an as-of date at least 3 months before the post date; fixed seeds for any simulation;
colours distinguishable without hue (line style differs too); SVG text stays text (svg.fonttype none).
After saving run `python3 scripts/add_img_dims.py`.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

NAVY, GREEN, RED, ORANGE, GREY, GRID, LIGHT = "#2b4c7e", "#2e7d5b", "#b3403a", "#c77d21", "#555555", "#e8e8e8", "#b9c4d4"
STYLES = ["-", "--", ":", "-."]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "svg.fonttype": "none", "svg.hashsalt": "wealthprimer",
})


def figure(w=7.2, h=3.6, **kw):
    fig, ax = plt.subplots(figsize=(w, h), **kw)
    return fig, ax


def finish(ax, title=None, source=None, xlabel=None, ylabel=None, legend=True):
    if title: ax.set_title(title, loc="left", fontsize=10, color="#222222")
    if xlabel: ax.set_xlabel(xlabel)
    if ylabel: ax.set_ylabel(ylabel)
    if legend and ax.get_legend_handles_labels()[0]: ax.legend(loc="best")
    if source:
        ax.figure.text(0.01, 0.005, source, fontsize=7, color=GREY, ha="left", va="bottom")
    ax.figure.tight_layout(rect=(0, 0.03, 1, 1))


def save(fig, path):
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": "wealthprimer chartkit"})
    plt.close(fig)
    print("saved", path)
