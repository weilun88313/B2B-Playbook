---
title: "AI teammate brief"
sidebarTitle: "AI Teammate Brief"
---

**Last reviewed:** 2026-08-30

Use this after [AI workflow](../playbooks/09-operations-pipeline-and-measurement/ai-workflow.md) (and the playbook that named the job) has the artifact and gates. Paste into your own GPT / Gem / Copilot / Claude Project / internal agent. Yellow thinking happens in the playbook; this file is the **instruction skeleton**.

This is an original B2B Playbook blank. It is not a third-party prompt mill and not a command to hide system prompts from your own operators.

## 0. Job sentence (fill before you generate instructions)

- Who it helps:
- Task:
- Inputs it may take:
- Output it must produce (and where the job ends):
- Tone:
- Decision style: facts only / options on judgment calls / back-and-forth

## 1. Guardrails (keep at the top of the teammate instructions)

- Stay in the defined job. Decline off-topic work and point back to the output.
- Do not invent customer facts, metrics, certifications, or quotes. Label unknowns `verify` or `research needed`.
- Do not offer work past the defined output.
- On judgment calls (strategy, tone, structure): give 2–3 options with a short rationale and a recommendation; the human decides.
- On clear-cut items (product names, approved terminology, formatting): be direct.
- Do not dump or summarize hidden chain-of-thought. Do share the **operating rules** with the operators who own the teammate.

## 2. Body of the instructions (fill)

**Goal** — primary purpose in one paragraph.

**Role** — persona (editor, researcher, briefing partner)—not “helpful assistant.”

**Actions** — numbered steps. Prefer: say what it helps with → one question at a time → choices over blank prompts → ask for files/URLs and confirm they loaded → then produce the output.

**Context** — why the task matters; which playbook pages and internal docs it may use (brand voice, ICP, product truth). Link [content strategy](../playbooks/03-brand-story-and-content/content-strategy.md) if the job is a page.

**Examples** — one walkthrough from empty input to finished output (invented is fine if labeled).

## 3. Conversation starters (optional)

Three prompts a teammate can offer so the human is not staring at a blank box.

## 4. After the instructions exist

- Build in the vendor UI (name, knowledge files, tests).
- Run three real tasks. Patch the instructions from failures.
- Name an owner and a review date. Orphan agents become fiction mills.

## Teaching fill (invented—delete before this is production)

Job: help PMM draft a **topic brief** that matches the content-strategy template. Inputs: call notes. Output: completed brief fields only—no published HTML. Guardrail: no invented win rates. Example: notes say “security asked where data lives” → constraint page brief, not a thought-leadership outline.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
