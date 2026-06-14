# The artifact is the demo: HTML in the enterprise

Thirteen self-contained `.html` artifacts showing what LLMs can produce for **business users**
and for **engineers in regulated environments**, plus a gallery page that ties it together.
Each artifact carries the brief that produces it. Run that brief in the model of your choice
(GPT, Claude, Gemini, Grok, DeepSeek, or your enterprise assistant), iterate a few rounds, and
you will get similar output. Not identical, and that is the point: the capability belongs to
LLMs, not to any one product.

**Live site:** https://vishal8shah.github.io/HTML-with-Claude/

## What's here

```
index.html              the gallery. Start here.
demos/biz-01 ... 06     business artifacts (status, actions, KPIs, guide, RAID, town hall)
demos/eng-07 ... 12     engineering artifacts (review pack, ADR, post-mortem, evidence, deps, map)
demos/deck-13           the talk itself, as an arrow-key HTML deck
assets/og-image.png     social preview card (used only via absolute URL in meta tags)
tools/make_og_image.py  regenerates the card (build-time only; Pillow required)
```

Every file works opened directly from disk (`file://`), makes **zero external requests**, uses
no frameworks and no build step. The whole tree can be copied as a subfolder into any website.

## Reading paths

The gallery opens with **"Start here"** lanes — business user, engineer, leader, risk / audit —
that point each reader at the three or four artifacts most relevant to them. It also carries a
**Markdown vs HTML** comparison, an **enterprise objections, answered** table, and a **when to use
/ when not to use HTML** split.

The thirteen artifacts link in a ring: each carries a `1/13` … `13/13` position with previous /
next navigation and a back-to-gallery link, and the HTML deck is artifact 13. Artifacts that are
interactive in the browser — the KPI dashboard, the RAID board and the module map — also render a
**static, printable fallback table**, so every figure stays readable with JavaScript disabled and
in print. All pages support light / dark themes and keyboard focus styles.

## Honesty note

The artifacts were built with **Claude Code, an LLM coding agent**, over several rounds of
iteration. They are shown as the bar to aim for, not as a guaranteed first answer; each artifact
says so on itself and includes its brief so you can reproduce something similar with your own
model. All data is fictional. ABC Corp does not exist.

## Enterprise tools footnote (sources)

Nothing in the gallery depends on any vendor. The index page carries one small appendix for the
common question "can our enterprise tools do this?". Its sources:

| Documented fact | Source |
|---|---|
| Microsoft 365 Copilot Pages "lightweight apps": create, edit, preview runnable code in a page | [Microsoft Support](https://support.microsoft.com/en-us/topic/build-lightweight-apps-within-microsoft-365-copilot-pages-fd42d9f3-258e-4bf9-8c5e-a73083a197cc) |
| Code previews Cloud Policy: enabled by default, admin-controllable | [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration) |
| GitHub Copilot agent mode edits files under enterprise policies | [GitHub Docs: features](https://docs.github.com/en/copilot/get-started/features) · [policies](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies) |
| EU data residency: code, prompts and responses stay in region; no training on Business/Enterprise data | [GitHub Docs](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency) · [Trust Center](https://copilot.github.trust.page/faq) |

## Re-skinning

Every page carries the same `:root { --ground ... }` token block at the top of its `<style>`.
Edit those lines (colors and font stacks) to match another site's identity. A find-and-replace
of the token block across `index.html` and `demos/*.html` re-skins everything.

## Publishing checklist

1. GitHub Pages serves `main` (root). `.nojekyll` is in place.
2. Before posting on LinkedIn, run the URL through the [Post Inspector](https://www.linkedin.com/post-inspector/)
   to refresh the preview card (`assets/og-image.png`).
3. If copying into another site, optionally update `og:url` and `og:image` in `index.html` for that copy.

Note: demo file names changed from `m365-`/`gh-` prefixes to `biz-`/`eng-` on 12 Jun 2026.

## Credit

The original idea, agents handing you HTML artifacts instead of markdown walls, is
[Thariq Shihipar's "The unreasonable effectiveness of HTML"](https://thariqs.github.io/html-effectiveness/).
The enterprise lens, the briefs and all examples here are new work inspired by it.

MIT © 2026 Vishal Shah
