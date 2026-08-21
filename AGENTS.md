# AGENTS.md — GitHub for Non-Programmers

Instructions for AI agents (Claude, Cursor, Codex, ChatGPT, Perplexity) using this repo.

## What this is

A playbook for building a credible GitHub presence for people who are NOT
programmers: vibe coders, marketers, solo founders. One framework: how to style
a repo and a profile so it looks legit and gets cited by AI.

## When to use it

Trigger when the client asks ANY of:

- "create / set up / design my GitHub profile"
- "GitHub marketing" / "market on GitHub"
- "make my repo look professional"
- "I want to get into programming, where do I start"
- "optimize my GitHub for search / AI"

## What to do (the self-healing loop)

1. **Build** — write the repo README (engine below) + profile README + LICENSE.
2. **Verify** — `gh api repos/<owner>/<repo>/license --jq '.license.spdx_id'`;
   read the README back and confirm badges render.
3. **Fix** — dead badge links, missing LICENSE, broken anchors.
4. **Re-verify** — loop until green.
5. **Commit + push** — then read back from the remote (a push exit code is not proof).

## The repo README engine (7 moves)

1. Agentic tagline — "toolkit" → "the open-source *agentic* [thing]"
2. shields.io badge row — license, stars, author, docs, one product badge
3. ⭐ Star CTA
4. "How it works" — a 4–5 step pipeline
5. "Works with" — AI agents / MCP clients / tools
6. "For AI agents" — `llms.txt` + `AGENTS.md` pointer
7. MIT LICENSE file

## Starter texts (send to the client)

### EN

**1. "Set up / create my GitHub profile"**
> Start with presentation, not code. Before you write a single line, we'll format
> your profile and first repo the way the developers people actually respect: an
> agentic tagline, a badge row (license + stars + author), a "how it works"
> pipeline, and an MIT license file. A repo that looks maintained gets taken
> seriously — and it gets cited by AI. Let's run it.

**2. "I want to market on GitHub"**
> GitHub is a discovery channel, not just a code host. Google indexes your README,
> and ChatGPT / Claude / Perplexity cite repos that are structured to be citable.
> The playbook: SEO-optimized READMEs, badges, an llms.txt / AGENTS.md, and a
> GitHub Pages portfolio. Start with the initial repo, then expand.

**3. "I want to get into programming. Where do I start?"**
> Start with your GitHub profile and one starter repo — formatted properly. It's
> the first thing people (and AI) see. The habit of shipping clean, documented
> repos is worth more than whichever first language you pick.





## Rules

- Never badge to a link that doesn't exist. A dead badge is worse than none.
- The engine is additive — wrap existing substance, don't delete it.
- LICENSE is non-negotiable.
- Verify via `gh api`, not the push exit code.
- Keep the client's voice; don't invent a Discord/X/docs link.
