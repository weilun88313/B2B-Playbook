# B2B Playbook

> An open, executable operating system for B2B sales and growth — built for operators and AI agents.

[![Validate](https://github.com/weilun88313/B2B-Playbook/actions/workflows/validate.yml/badge.svg)](https://github.com/weilun88313/B2B-Playbook/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**[English](#english) | [中文](#中文简介)**

## English

### Get a useful result in 10 minutes

Do not read the entire repository. Start with one account you are considering for outbound.

1. Open the [10-minute ICP sprint](playbooks/01-icp/quickstart.md).
2. Copy the [ICP canvas](playbooks/01-icp/templates/icp-canvas.md).
3. Score the account with the [account scorecard](playbooks/01-icp/templates/account-scorecard.md).
4. Compare the result with the filled [Helion example](playbooks/01-icp/examples/helion-icp.md).
5. Run the offline scorer:

```bash
node tools/icp-account-scorer.mjs \
  --name "Müller Antriebstechnik" \
  --use-case 2 --budget 2 --alternative 2 --trigger 2 --committee 1
```

The output is a transparent T1/T2/T3 recommendation and a default next action. No API key, package installation, or customer-data upload is required.

### What makes this different

Most B2B repositories are reading lists. This repository is designed to produce work.

Every complete module follows the same contract:

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
- **Evidence-aware:** facts, observations, assumptions, and unknowns remain separate.
- **Agent-native:** a portable `SKILL.md` routes AI agents to the correct playbook.
- **Privacy-conscious:** public examples use the fictional company **Helion**, never customer data.
- **English-first:** all maintained playbooks, templates, examples, tools, and Agent instructions are written in English.

### Playbooks

| Module | What you can take | Status |
|---|---|---|
| [System](playbooks/00-system/) | Usage model, evidence standard, weekly cadence | Complete |
| [ICP & buying committee](playbooks/01-icp/) | ICP canvas, committee map, account tiers, offline scorer | Complete |
| [Positioning & homepage](playbooks/02-positioning/) | Positioning sentence, 10-second test, comparison-page outline | Complete |
| [Outbound](playbooks/03-outbound/) | Account research, sequence, pre-send and compliance checks | Complete |
| [Event-led growth](playbooks/04-events/) | Event scorecard, pre/on-site/post-event operating system | Complete |
| [Content & demand](playbooks/05-content/) | Planned | Planned |
| [Enterprise sales](playbooks/06-sales/) | Intro call, demo co-design, pilot, pricing, procurement | Complete |
| [Growth operations](playbooks/07-ops/) | Planned | Planned |

The [glossary](glossary.md) keeps operating terms consistent. The [evidence standard](playbooks/00-system/evidence-standard.md) explains how claims are labeled.

### Install as an Agent Skill

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

### How to use the library

1. Read [how to use the system](playbooks/00-system/how-to-use.md).
2. Pick only the module tied to the work in front of you.
3. Copy from `templates/`, then compare with `examples/`.
4. Before sending, publishing, or entering a meeting, run the matching `checklists/`.
5. Review the module's `metrics.md` after the work has run.

Do not optimize for finishing the library. Optimize for one observable action and one learning loop.

### Quality contract

A module is not complete unless it includes:

- a clear use case and exclusion;
- an SOP with entry and exit criteria;
- at least one checklist;
- at least one blank template;
- at least one filled fictional or properly anonymized example;
- operating metrics and explicit non-metrics.

Relative Markdown links, module contracts, Skill frontmatter, and the English-only content policy are checked automatically by `npm test` and GitHub Actions.

### Feedback and maintenance

This is an owner-maintained reference. Ivan Xu (`weilun88313`) reviews feedback and makes repository updates so the published guidance keeps one editorial voice and evidence standard.

If a playbook is confusing, expired, or incorrect, use the playbook feedback issue form. Do not post credentials, customer lists, private contacts, or material you do not have the right to publish. The [roadmap](ROADMAP.md) shows what the maintainer plans to update next.

If this repository helps you complete real B2B work, a ⭐ helps other operators discover it.

### License

[MIT](LICENSE). Templates and playbooks are operational starting points, not legal advice or guaranteed performance claims.

---

## 中文简介

**B2B Playbook** 是一个面向 B2B 销售与增长从业者和 AI Agent 的开放执行系统。

仓库正文以英文为唯一维护版本，包含：

- ICP 与购买委员会
- 定位与官网
- 主动外联
- 展会与活动型增长
- 从首次会面到签约的企业销售流程
- 可复制模板、完整虚构示例、检查清单、指标和离线工具

推荐从英文版 [10-minute ICP sprint](playbooks/01-icp/quickstart.md) 开始。它可以帮助你为目标账户建立 ICP、购买委员会和 T1/T2/T3 分级，并确定下一步行动。

也可以将仓库安装为 Agent Skill：

```bash
npx skills add weilun88313/B2B-Playbook
```

除本节中文简介外，所有 Playbook、模板、示例、工具说明和 Agent 指令均以英文维护，避免中英文内容混写或版本漂移。
