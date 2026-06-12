# The artifact is the demo — HTML in the enterprise

Thirteen self-contained `.html` artifacts showing what **M365 Copilot** (business users) and
**GitHub Copilot** (engineers in regulated environments) users can produce by asking for **one
HTML file** instead of a wall of text — plus a gallery page that ties it together.

**Live site:** https://vishal8shah.github.io/Power-of-HTML-with-LLMs/ *(enable GitHub Pages:
Settings → Pages → Deploy from branch → `main`, root)*

## What's here

```
index.html              the gallery — start here
demos/m365-01 … 06      business-user artifacts (status, actions, KPIs, guide, RAID, town-hall)
demos/gh-07 … 12        engineering artifacts (review pack, ADR, post-mortem, evidence, deps, map)
demos/deck-13           the talk itself, as an arrow-key HTML deck
assets/og-image.png     LinkedIn/social preview card (used only via absolute URL in meta tags)
tools/make_og_image.py  regenerates the card (build-time only; Pillow required)
```

Every file works opened directly from disk (`file://`), makes **zero external requests**, uses
no frameworks and no build step. The whole tree can be copied as a subfolder into any website.

## Honesty note

The artifacts are **reference outputs built with an AI coding agent** (Claude Code) to show the
format — they are not screenshots of Copilot output, and each artifact says so on itself. Each
contains the prompt you would give Copilot to reproduce something like it. Every claim about what
Copilot can do links to official documentation (sources below). All data is fictional — ABC Corp
does not exist.

## Sources for every capability claim

| Claim | Source |
|---|---|
| Copilot Pages "lightweight apps": create, edit, preview runnable code in a page | [Microsoft Support](https://support.microsoft.com/en-us/topic/build-lightweight-apps-within-microsoft-365-copilot-pages-fd42d9f3-258e-4bf9-8c5e-a73083a197cc) |
| Code previews Cloud Policy — enabled by default, admin-controllable | [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration) |
| App Builder agent builds lightweight apps from a description | [Microsoft 365 blog, 28 Oct 2025](https://www.microsoft.com/en-us/microsoft-365/blog/2025/10/28/microsoft-365-copilot-now-enables-you-to-build-apps-and-workflows/) |
| Agent mode determines files to change, proposes edits/commands for approval | [GitHub Docs — Copilot features](https://docs.github.com/en/copilot/get-started/features) |
| Copilot governed by enterprise policies (incl. content exclusion, feature toggles) | [GitHub Docs — enterprise policies](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies) |
| Data residency: "code, prompts, and Copilot responses never leave your region" (EU/US) | [GitHub Docs — Copilot data residency](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency) |
| No training on Business/Enterprise data; IP indemnification (duplicate-detection filter "Block") | [GitHub Copilot Trust Center](https://copilot.github.trust.page/faq) |

## Re-skinning

Every page carries the same `:root { --ground… }` token block at the top of its `<style>` —
edit those ~15 lines (colors + font stacks) in each file to match another site's identity.
A find-and-replace of the token block across `index.html` and `demos/*.html` re-skins everything.

## Publishing checklist

1. Merge to `main`, enable GitHub Pages (root). `.nojekyll` is already in place.
2. Verify `https://vishal8shah.github.io/Power-of-HTML-with-LLMs/` renders.
3. Before posting on LinkedIn, run the URL through the [Post Inspector](https://www.linkedin.com/post-inspector/)
   to prime the preview card (`assets/og-image.png`).
4. If copying into vishalshah.app, optionally update `og:url`/`og:image` in `index.html` for that copy.

## Credit

The original idea — agents handing you HTML artifacts instead of markdown walls — is
[Thariq Shihipar's "The unreasonable effectiveness of HTML"](https://thariqs.github.io/html-effectiveness/).
The enterprise lens, governance framing, prompts and all examples here are new work inspired by it.

MIT © 2026 Vishal Shah
