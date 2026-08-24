# B2B Playbook

> Practical B2B marketing knowledge, tool choices, and an Agent Skill for turning go-to-market ideas into observable work.

**[English](#english) | [中文](#中文简介)**

## English

### Start with one decision

Do not read the entire repository. Pick the decision in front of you:

| Collection | Use it to | Start here |
|---|---|---|
| **Playbooks** | Find a specific B2B marketing capability, channel, or tactic | [Browse the master index](playbooks/) |
| **Tools** | Choose software for a specific job instead of assembling a fashionable stack | [Browse the tool directory](TOOLS.md) |
| **Agent Skill** | Let an AI agent route a B2B task through the right method | [Install the Skill](#agent-skill) |

For the fastest useful result, run the [10-minute ICP field test](playbooks/01-strategy-and-buyers/icp.md#10-minute-field-test) on one target account.

### Playbooks

The [master playbook index](playbooks/) organizes B2B marketing into nine durable capability domains, then routes each concrete tactic—such as cold email, trade shows, founder story, LinkedIn, affiliate programs, and pipeline—to its own playbook.

| Published domain | Available playbooks |
|---|---|
| [Strategy & buyers](playbooks/01-strategy-and-buyers/) | ICP, buying committee |
| [Product marketing](playbooks/02-product-marketing/) | Positioning |
| [Outbound & prospecting](playbooks/05-outbound-and-prospecting/) | Account research, cold email, multichannel sequence |
| [Account, field & partner marketing](playbooks/06-account-field-and-partner/) | Event marketing, trade shows |

Unpublished topics are mapped in the master index without empty placeholder files. Each published tactic keeps its strategy, execution steps, templates, checklist, metrics, mistakes, and sources in one page.

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

### Copyright and reuse

Copyright © 2026 Ivan Xu. All rights reserved. You may read, link to, and quote brief attributed excerpts. Republishing, translation, mirroring, substantial copying, commercial reuse, and reuse in redistributed datasets, knowledge bases, RAG systems, or model training require prior written permission. See the [full terms](LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)

---

## 中文简介

**B2B Playbook** 是一个面向 B2B 销售与增长从业者和人工智能智能体的开放知识库。

仓库当前保留三个核心入口：

1. **行动手册**：按照九个稳定的 B2B 营销能力域组织，再将冷邮件、展会、创始人故事、白皮书、领英、联盟营销和 Pipeline 等具体打法放入各自页面。
2. **工具清单**：按实际任务整理的软件推荐，同时说明适用条件和限制。
3. **智能体技能**：让兼容的人工智能智能体读取并执行这套方法。

英文是仓库正文的唯一维护版本。中文只保留在本简介中，避免双语正文产生版本漂移。

版权归 Ivan Xu 所有。允许阅读、分享本仓库链接及在注明作者和正版来源的前提下少量引用；转载全文或大段内容、翻译、镜像、商业使用，以及将内容打包进对外分发的数据集、知识库、RAG 系统或模型训练材料，须事先取得书面许可。完整规则见 [LICENSE](LICENSE)。

唯一正版来源：[github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
