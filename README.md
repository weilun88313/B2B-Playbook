# B2B Playbook

> An open, executable operating system for B2B sales and growth — built for operators and AI agents.

面向 B2B 销售与增长的开放操作系统：SOP、模板、填好示例、检查清单、指标和可运行工具。

[![Validate](https://github.com/weilun88313/B2B-Playbook/actions/workflows/validate.yml/badge.svg)](https://github.com/weilun88313/B2B-Playbook/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Start here:** [10-minute ICP sprint](zh/01-icp/quickstart.md) · [English ICP playbook](en/01-icp/) · [Install as an Agent Skill](#install-as-an-agent-skill) · [Roadmap](ROADMAP.md)

## Get a useful result in 10 minutes

Do not read the whole repository. Start with one account you are considering for outbound.

1. Copy the [ICP canvas](zh/01-icp/templates/icp-canvas.md).
2. Score the account with the [account scorecard](zh/01-icp/templates/account-scorecard.md).
3. Compare your result with the filled [Helion example](zh/01-icp/examples/helion-icp.md).
4. Run the offline scorer:

```bash
node tools/icp-account-scorer.mjs \
  --name "Müller Antriebstechnik" \
  --use-case 2 --budget 2 --alternative 2 --trigger 2 --committee 1
```

The result is a transparent T1/T2/T3 recommendation and a default next action. No API key, package install, or customer data upload is required.

## What makes this different

Most B2B repositories are reading lists. This repository is designed to produce work.

Every complete module ships with the same contract:

```text
when to use / when not to use
        ↓
step-by-step SOP
        ↓
blank template + filled fictional example
        ↓
pre-flight checklist + operating metrics
```

- **Executable:** templates and tools lead to a concrete next action.
- **Evidence-aware:** facts, observations, assumptions, and open questions stay separate.
- **Agent-native:** the repository includes a portable `SKILL.md` entrypoint.
- **Privacy-conscious:** public examples use the fictional company **Helion**, never customer data.
- **Chinese-first, globally usable:** Chinese is the source of truth; the flagship ICP module is available in English.

## Playbooks

| Module | What you can take | Chinese | English |
|---|---|---:|---:|
| ICP & buying committee | ICP canvas, committee map, account tiers, scorer | [Complete](zh/01-icp/) | [Complete](en/01-icp/) |
| Positioning & homepage | Positioning sentence, 10-second test, comparison-page outline | [Complete](zh/02-positioning/) | Planned |
| Outbound | Account research, multi-touch sequence, compliance checks | [Complete](zh/03-outbound/) | Planned |
| Event-led growth | Event scorecard, pre/during/post-show system | [Complete](zh/04-events/) | Planned |
| Enterprise sales | Intro call, demo co-design, pilot, pricing and procurement | [Complete](zh/06-sales/) | Planned |
| Content & demand | — | Planned | Planned |
| Growth operations | — | Planned | Planned |

The [glossary](glossary.md) keeps terms consistent. The [evidence standard](zh/00-system/evidence-standard.md) explains how claims are labeled.

## Install as an Agent Skill

This repository follows the open Agent Skills format and can be installed into Codex, Claude Code, Cursor, OpenCode, and other compatible agents.

```bash
npx skills add weilun88313/B2B-Playbook
```

Then ask your agent:

```text
Use $b2b-playbook to turn these five target accounts into an ICP canvas,
a buying-committee map, T1/T2/T3 tiers, and one next action per account.
Mark unknowns instead of inventing data.
```

The Skill routes the agent to the relevant module; it does not send messages, enrich contacts, or modify a CRM.

## How to use the library

1. Read [how to use the system](zh/00-system/how-to-use.md).
2. Pick only the module tied to the work in front of you.
3. Copy from `templates/`, then compare with `examples/`.
4. Before sending, publishing, or entering a meeting, run the matching `checklists/`.
5. Review the module's `metrics.md` after the work has run.

Do not optimize for finishing the library. Optimize for one observable action and one learning loop.

## Quality contract

A module is not complete unless it includes:

- a clear use case and exclusion;
- an SOP with entry and exit criteria;
- at least one checklist;
- at least one blank template;
- at least one filled fictional or properly anonymized example;
- operating metrics and explicit non-metrics.

Relative Markdown links and module contracts are checked automatically by `npm test` and GitHub Actions.

## Feedback and maintenance

This is an owner-maintained reference. Ivan Xu (`weilun88313`) reviews feedback and makes repository updates so the published guidance keeps one editorial voice and evidence standard.

If a playbook is confusing, expired, or incorrect, use the playbook feedback issue form. Please do not post credentials, customer lists, private contacts, or material you do not have the right to publish. The [roadmap](ROADMAP.md) shows what the maintainer plans to update next.

If this repository helps you complete real B2B work, a ⭐ helps other operators discover it.

## License

[MIT](LICENSE). Templates and playbooks are provided as operational starting points, not legal advice or guaranteed performance claims.
