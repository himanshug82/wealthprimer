# Design tokens

All visual values live at the top of `assets/main.scss`. Use a token instead of typing a value; add a token when a new value is needed in more than one place. Dark mode is one block of overrides (`@mixin dark-tokens`), applied when the system prefers dark (unless `data-theme="light"`) or when `data-theme="dark"`, so a component styled only with tokens gets dark mode for free.

## Colour (CSS custom properties)

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#fcfbf8` | `#0e1217` | Page background |
| `--surface` | `#ffffff` | `#151b23` | Cards, inputs |
| `--surface-2` | `#f4f2ec` | `#1b222c` | Secondary panels |
| `--ink` | `#14171c` | `#eef1f5` | Headings, strong text |
| `--text` | `#2a2e35` | `#d2d7df` | Body text |
| `--muted` | `#585f6b` | `#9aa3b0` | Meta lines, captions |
| `--rule` / `--rule-strong` | `#e6e2d8` / `#d6d1c4` | `#26303c` / `#334050` | Borders |
| `--brand` | `#184f95` | `#7fb0f0` | Brand blue (logo, charts), buttons |
| `--brand-strong` | `#0f3a70` | `#a8c9f6` | Hover |
| `--brand-soft` / `--brand-tint` | `#eaf1fb` / `#cde2fb` | `#132236` / `#1b3150` | Tinted backgrounds, selection |
| `--brand-mid` | `#3a7bd5` | (same) | Middle stop of the header gradient |
| `--on-brand` | `#fff` | `#0b1a2e` | Text on a solid `--brand` background |
| `--link` | `#1a56a8` | `#8ebcf5` | Links |
| `--warm-bg` / `--warm-rule` / `--warm-ink` | `#fdf5e7` / `#efd6a8` / `#8a4b0f` | `#231c12` / `#4a3a1f` / `#f0bd72` | Warm panels (case study, notices) |
| `--code-bg` / `--code-rule` | `#f5f7fb` / `#dfe5ef` | `#111821` / `#253041` | Code blocks |

Syntax-highlighting colours stay as literals in the `.highlight` rules near the end of the file: they are a self-contained Rouge theme, with the contrast ratios noted in comments.

## Type

| Token | Value |
|---|---|
| `--font-serif` | Charter, Sitka, Cambria, Georgia (post bodies) |
| `--font-sans` | System UI stack (UI, headings, tables, numbers) |
| `--font-mono` | System monospace stack |
| `--fs-2xs` | 0.72rem |
| `--fs-xs` | 0.78rem |
| `--fs-sm` | 0.88rem (the most used: meta lines, small UI) |
| `--fs-md` | 0.95rem |
| `--fw-regular` / `--fw-medium` / `--fw-semibold` / `--fw-strong` / `--fw-bold` | 400 / 500 / 600 / 650 / 700 |

Fonts are system stacks on purpose: `/privacy/` promises no third-party resources on page load, which rules out web fonts.

**Still literal (candidates for a tighter scale):** other font sizes (0.74, 0.8, 0.82, 0.85, 0.9, 0.92, 0.93, 0.98, 1.02, 1.04, 1.05, 1.06, 1.1, 1.12, 1.15, 1.2, 1.25, 1.85 and 2.4rem, plus the two `clamp()` title sizes), one `font-weight: 550`, and the spacing values (about 25 distinct rem values, 1rem the most common). Folding them into the scale above would change the look slightly, so it needs before/after screenshots; it was deliberately left out of the 21 Nov 2026 tokenisation.

## Shape and layout

| Token | Value | Use |
|---|---|---|
| `--radius` | 12px | Cards, panels |
| `--radius-sm` | 8px | Smaller cards, inputs |
| `--radius-xs` | 6px | Small chips |
| `--radius-pill` | 999px | Buttons, pills, search boxes |
| `--radius-circle` | 50% | Avatars, round markers |
| `--measure` | 44rem | Reading column (posts, pages) |
| `--page-max` | 72rem | Header, footer, homepage |
| `--shadow-sm` / `--shadow-md` | see file | Card resting / hover |

A few one-off radii (3, 5, 7 and 9px) stay literal.

## Breakpoints (Sass variables)

Media queries can't read CSS custom properties, so breakpoints are Sass variables:

| Variable | Value | Meaning |
|---|---|---|
| `$bp-phone` | 599px (max) | Single-column phone layouts |
| `$bp-small` | 699px (max) | Small tablets and large phones |
| `$bp-narrow` | 799px (max) | Footer stacks |
| `$bp-nav-max` / `$bp-nav-min` | 819px / 820px | Header switches between the menu button and the full nav |
| `$bp-search` | 1000px (min) | Header search box appears |

## Checking a refactor

A token change that shouldn't alter the look can be proved: build before and after, replace each new `var(--token)` in the new `_site/assets/main.css` with its value (Sass writes `0.88rem` as `.88rem`), drop the new declarations from `:root`, and compare the two files. The 21 Nov 2026 tokenisation was checked this way and came out identical.
