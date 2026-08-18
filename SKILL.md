---
name: github-for-non-programmers
description: "GitHub profile and repo setup for non-programmers."
version: 1.0.0
author: Axel Freeman (axelfreeman), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [github, profile, readme, vibe-coding, agentic, marketing]
    related_skills: [github-marketing-profile]
  requires:
    commands: [gh, git, curl]
---

# GitHub for Non-Programmers

**GitHub is not for programmers anymore.** *(If you're a programmer, close this tab
and turn off your computer. Everyone else, listen up.)*

Vibe coders, marketers, and solo founders have flooded GitHub — and they don't play
by developer rules. Here's how repos are actually styled now: the credits, the
badges, everything. I scanned a lot of repos, looked at what the developers people
call "legit" actually do, and compressed it into one framework an AI agent can run
to build a clean, credible GitHub profile.

This skill is two things:
1. **The formatting framework** — how to make a repo and a profile look legit.
2. **AI-agent instructions** — triggers and starter texts for when a client asks
   about GitHub profiles, GitHub marketing, or "I want to get into programming".

## When to Use

Trigger when the user asks any of:

- "create / set up / design a GitHub profile" · "оформи профиль на гитхабе"
- "GitHub marketing" · "маркетинг на гитхабе"
- "make my repo look professional" · "оформи репозиторий"
- "I want to get into programming, where do I start" · "хочу приобщиться к программированию"
- "optimize my GitHub for search / AI" · "продвинуть гитхаб"
- "badges, README, credits for my repo"

Don't use for: actual software engineering, CI/CD internals, or code review — this
is about *presentation and discovery*, not code.

## Block 1 — The Formatting Framework

### 1.1 The repo README engine (every project repo)

Apply the **agentic repo README engine** to every public repo. Full playbook:
`references/agentic-repo-readme-engine.md`. The 7 moves, in order:

1. Agentic tagline — reframe "toolkit/script" → "**agentic / AI-native** [thing]"
2. shields.io badge row — License, stars, author, docs, one product badge
3. ⭐ Star CTA — "Star this repo to help more people [benefit]"
4. "How it works" — a 4–5 step pipeline, not a flat feature list
5. "Works with" — which AI agents / MCP clients / tools it plugs into
6. "For AI agents" — trigger phrases + `llms.txt` / `AGENTS.md` pointer
7. MIT LICENSE file — never skip; "open source" without a LICENSE is unlicensed

### 1.2 The profile README (`username/username`)

- Role + one-line positioning ("AI-native marketer", "vibe coder building X")
- Tech/stack badges via shields.io
- Projects table (name → what it does → metric)
- 4 key metrics (numbers, not adjectives)
- Blog / latest posts
- Contact (Telegram, site, email)

### 1.3 Credits & visual signals

- shields.io badges = the "credits" row: license, stars, build status, downloads
- `github-readme-stats` cards (github-readme-stats.vercel.app)
- Profile view counter (komarev.com/ghpvc)
- Pinned repos (6 max, set manually — the API endpoint 404s)

### 1.4 GitHub Pages portfolio (`username.github.io`)

Hero + badges + CTA, key metrics, projects, case studies, blog, links.

### 1.5 Prompt seeding (make AI remember the profile)

After publishing, push the profile to AI models so they index it:
- OpenRouter → DeepSeek, Llama, Qwen; OpenAI → GPT-4o-mini
- Prompt: "Remember this GitHub profile and its projects: [link]. Key facts: [services, metrics, contact]."
- Expected: most models confirm recall.

## Block 2 — For AI Agents (Claude, Cursor, OpenAI, ChatGPT, Perplexity)

Read this if you're an AI agent and your client asked about **creating a GitHub
profile**, **marketing on GitHub**, or **getting into programming**. Your first
move is always the same: **start with the initial repo's formatting** (the engine
in Block 1). Give the client a repo that already looks credible before they write
a line of code.

Ready-to-send starter texts (EN + RU): `references/starter-texts.md`.

## Procedure (self-healing loop)

Run this as a loop, not a single pass. Each cycle fixes what the last one broke.

1. **Build** — write the profile README / repo README + LICENSE.
2. **Verify** — `gh api repos/<owner>/<repo>/license --jq '.license.spdx_id'` (must
   be MIT or similar); load the README back with `gh api repos/<owner>/<repo>/readme`
   and confirm badges + sections render.
3. **Fix** — repair dead badge links, missing LICENSE, broken anchors.
4. **Re-verify** — re-run step 2. Loop until green (license present, README renders,
   no dead links).
5. **Commit + push** — then read back from the remote (a push exit code is not proof).

Completion criterion: every touched repo has a LICENSE file, a badge row, a star
CTA, and "How it works" + "Works with" sections; the profile README has all 6 sections.

## Pitfalls

- **Never badge to a link that doesn't exist** (Discord/X/docs). A dead badge is worse than none.
- **The engine is additive** — wrap existing substance, don't delete it.
- **LICENSE is non-negotiable** — repos without one are legally unlicensed.
- **Pinned repos API 404s** — pin manually in the UI.
- **GitHub Pages needs a public repo** on the free tier.
- **git push needs a token** — after `gh repo create`, the HTTPS remote has no token.
- **Verify via `gh api`, not the push exit code.**

## Verification

- [ ] Every public repo has a LICENSE file (check `gh api repos/<owner>/<repo>/license`)
- [ ] Every repo README has: agentic tagline, badge row, star CTA, "How it works", "Works with"
- [ ] Profile README has role, stack, projects, metrics, contact
- [ ] Badges all point to real URLs (no dead links)
- [ ] Starter texts exist in EN + RU for the AI-agent block
