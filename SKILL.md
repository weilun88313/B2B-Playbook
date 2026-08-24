---
name: b2b-playbook
description: Turn B2B sales and growth work into evidence-aware, executable outputs using ICP, buying committee, positioning, outbound, event-led GTM, and enterprise-sales playbooks. Use when the user needs a concrete plan, checklist, template, account tier, or next action; do not use for generic inspiration or legal advice.
---

# B2B Playbook

Produce usable B2B operating artifacts, not broad advice.

## Route the task

| Need | Read |
|---|---|
| Start or understand the system | `playbooks/00-system/how-to-use.md` and `glossary.md` |
| ICP, account qualification, buying committee | `playbooks/01-icp/README.md`, then `playbooks/01-icp/sop.md` |
| Positioning, homepage, comparison page | `playbooks/02-positioning/README.md`, then `playbooks/02-positioning/sop.md` |
| Outbound research or sequence | `playbooks/03-outbound/README.md`, then `playbooks/03-outbound/sop.md` |
| Event selection and execution | `playbooks/04-events/README.md`, then `playbooks/04-events/sop.md` |
| First meeting through signature | `playbooks/06-sales/README.md`, then `playbooks/06-sales/sop.md` |

All maintained content is in English under `playbooks/`. The Chinese section in the root README is an orientation summary, not a second source of truth.

## Working rules

- Begin with the buyer, account, business problem, and observable trigger.
- Separate facts, observations, assumptions, and unknowns using `playbooks/00-system/evidence-standard.md`.
- Name the economic buyer, champion, technical buyer, and blocker when evidence exists. Write `unknown` and a discovery action when it does not.
- Use the module's blank template for structure and its fictional example only to calibrate detail.
- End with a checklist or concrete next action and the metric that will evaluate it.
- Never invent customer facts, contacts, proof points, legal requirements, or performance claims.
- Do not expose or request customer lists, credentials, private contact data, or unapproved sources.

## ICP fast path

For account qualification, read `playbooks/01-icp/quickstart.md`. Produce:

1. a one-sentence ICP;
2. five disqualifiers;
3. a buying-committee map;
4. a T1/T2/T3 score with evidence for each dimension;
5. one default next action per account;
6. an explicit list of unknowns and how to resolve them.

If local execution is available, `node tools/icp-account-scorer.mjs --help` provides a deterministic score check. Human-readable reasoning remains the primary output.
