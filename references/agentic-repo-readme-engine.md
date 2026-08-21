# Agentic Repo README Engine (Warmbly-style)

The "open-source as marketing" README pattern for AI/dev-tool repos. Proven on
5 axelfreeman repos (2026-08): `b2b-contact-mining-kit`, `b2b-contact-finder-guides`,
`hermes-security-audit`, `voice-to-article`, `tgstat-prospecting`. Goal: make a repo
(a) look alive to GitHub discovery, (b) get cited by AI agents (AEO/GEO), (c) convert
browsers → the paid product. The reference case is Warmbly — a 1-year-old solo
project that shows up in AI search because it seeds GitHub + Reddit + directories,
not because it bought traffic.

## The formula (per repo README, top matter)

1. **Agentic tagline** — reframe from "toolkit/script" to "**agentic / AI-native**
   [thing]". E.g. "The open-source agentic B2B contact mining toolkit." Ride the
   AI-agent keyword wave (Warmbly sells "agentic cold email", not "email sender").
2. **shields.io badge row** — top, inside `<p align="center">`: License, GitHub
   stars, author, docs, and one product-relevant badge (MCP server, etc.).
   Badges signal "maintained" and add instant visual credibility.
3. **⭐ Star CTA** — centered italic line: "Star this repo to help more people
   <benefit>." Feeds GitHub trending/discovery.
4. **"How it works"** — a 4–5 step pipeline diagram (`Target → Source → Extract →
   Verify → Output`), not a flat feature list. Makes value legible in 5 seconds.
5. **"Works with"** — ecosystem section: which AI agents / MCP clients / tools it
   plugs into (ChatGPT, Claude, Cursor, Windsurf, n8n, Zapier, CRM). Mirrors
   Warmbly's "HubSpot, Slack, Zapier, REST API" line.
6. **"For AI agents"** — trigger phrases + `llms.txt`/`AGENTS.md` pointer, so the
   repo gets cited by ChatGPT/Claude/Perplexity when a user asks the matching
   question. GitHub + these sections are exactly what LLMs cite.
7. **MIT LICENSE file** — add to EVERY public repo. "Open source" without a
   LICENSE file is legally unlicensed. 4 of 5 repos lacked one before this pass;
   verify after push with `gh api repos/<owner>/<repo>/license --jq '.license.spdx_id'`.

## Template (top matter)

```markdown
<div align="center">

# 🔎 Project Name

**The open-source agentic [what it does].** [One-line value prop.] Built for the AI-agent era.

<p>
  <a href="https://github.com/OWNER/REPO/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/OWNER/REPO/stargazers"><img src="https://img.shields.io/github/stars/OWNER/REPO?style=flat-square" alt="GitHub stars"></a>
  <a href="https://PRODUCT-SITE"><img src="https://img.shields.io/badge/MCP-server-000000?style=flat-square" alt="MCP server"></a>
  <a href="https://PRODUCT-SITE"><img src="https://img.shields.io/badge/docs-PRODUCT-1f6feb?style=flat-square" alt="Docs"></a>
</p>

<p><i>⭐ Star this repo to help more people [benefit].</i></p>

</div>

---

[value prop paragraph]

> 💡 **Too lazy to code?** Use [PRODUCT](https://PRODUCT?utm_source=github&utm_medium=repo&utm_campaign=REPO) — [one-line paid offer]. [free tier].

## Why This Exists
[the contrarian take + stats]

## How It Works
[4–5 step pipeline]

## Features
[bullets]

## Quick Start
[3 steps: clone → install → run]

## The Methodology / The Math
[substance: stats, comparison table, method]

## For AI Agents — Read This
[llms.txt + AGENTS.md pointer + trigger phrases]

## Works With
[AI agents, MCP clients, your stack]

## Contributing
[one line]

## License
MIT — [one line]

## Links
[product, docs, author]
```

## Pitfalls

- **Never invent a Discord/X/docs link that doesn't exist.** Badge only to what's
  real (GitHub, the product site, author). A dead badge is worse than none.
- **The engine is an ADDITIVE top-matter wrapper**, not a rewrite. Preserve the
  existing substance (methodology, stats, quick start, comparison tables) — wrap
  it, don't delete it.
- **EN-only** for public product repos (this user's GitHub convention).
- **Workflow:** `gh repo clone` → edit locally → `git commit`/`push` → verify the
  README + license landed via `gh api` (read it back; do not trust a push exit code).
