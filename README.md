# B2B Playbook

> Practical B2B marketing knowledge, tool choices, and an Agent Skill for turning go-to-market ideas into observable work.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**[English](#english) | [中文](#中文简介)**

## English

### Start with one decision

Do not read the entire repository. Pick the decision in front of you:

| Collection | Use it to | Start here |
|---|---|---|
| **Playbooks** | Follow a practical method and copy its working templates | [Choose a playbook](#playbooks) |
| **Tools** | Choose software for a specific job instead of assembling a fashionable stack | [Browse the tool directory](TOOLS.md) |
| **Agent Skill** | Let an AI agent route a B2B task through the right method | [Install the Skill](#agent-skill) |

For the fastest useful result, run the [10-minute ICP field test](playbooks/icp.md#10-minute-field-test) on one target account.

### Playbooks

Each playbook is one self-contained page. It includes when to use the method, the operating steps, copyable templates, a checklist, and metrics.

| Playbook | Decision it helps you make |
|---|---|
| [ICP & buying committee](playbooks/icp.md) | Which accounts deserve active sales time, who must participate, and what happens next |
| [Positioning](playbooks/positioning.md) | Why a specific buyer should change from the current alternative |
| [Outbound](playbooks/outbound.md) | How to turn account evidence into a relevant conversation |
| [Event-led growth](playbooks/event-led-growth.md) | Whether to attend, sponsor, exhibit, or skip—and how to operate the event |
| [Enterprise sales](playbooks/enterprise-sales.md) | How to coordinate the buyer journey from first conversation to signature |

### Tool directory

[TOOLS.md](TOOLS.md) is a small, opinionated directory of B2B software. Tools are organized by job—not affiliate value or popularity—and include a use case, a reason to avoid the tool, an official link, and a last-review date.

The directory is not a ranking and does not replace security, privacy, deliverability, or legal review.

### Agent Skill

Install the repository as an Agent Skill in Codex, Claude Code, Cursor, OpenCode, or another compatible agent:

```bash
npx skills add weilun88313/B2B-Playbook
```

Then ask:

```text
Use $b2b-playbook to evaluate these five target accounts.
Produce an ICP, buying-committee map, T1/T2/T3 decision,
and one next action per account. Mark unknowns instead of inventing facts.
```

The Skill routes the task to the relevant playbook. It does not send messages, enrich contacts, or modify a CRM.

### Evidence rules

Keep four evidence states separate:

| State | Meaning |
|---|---|
| **Fact** | A dated record, public source, direct quote, or system event that can be checked |
| **Observation** | A pattern found in a limited sample |
| **Assumption** | An unverified belief that changes the next action |
| **To validate** | A question paired with a test that can close it |

Every week should end with one documented decision and one next test—not a longer activity report.

### Maintenance

This is an owner-maintained reference. Ivan Xu (`weilun88313`) keeps one editorial voice and evidence standard. Guidance is a starting method, not a guaranteed formula or legal advice.

If this repository helps you complete real B2B work, a star helps other operators discover it.

### License

[MIT](LICENSE)

---

## 中文简介

**B2B Playbook** 是一个面向 B2B 销售与增长从业者和人工智能智能体的开放知识库。

仓库当前保留三个核心入口：

1. **行动手册**：客户画像与购买委员会、市场定位、主动外联、活动型增长和企业销售。
2. **工具清单**：按实际任务整理的软件推荐，同时说明适用条件和限制。
3. **智能体技能**：让兼容的人工智能智能体读取并执行这套方法。

英文是仓库正文的唯一维护版本。中文只保留在本简介中，避免双语正文产生版本漂移。
