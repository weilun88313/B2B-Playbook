# B2B Playbook

**[English](#english) | [中文](#中文)**

## English

> A practical B2B marketing operating library for making better go-to-market decisions—and turning them into observable work.

**Current coverage:** 64 published playbooks · 42 working files · 43 curated tools · 19 reading sources · 9 domain guides

**Last reviewed:** 2026-08-30

### What this is

An owner-maintained knowledge base for B2B marketers, founders, revenue teams, and AI agents. Durable capabilities sit in nine domains; each published tactic is an execution-ready page. The [master index](playbooks/) is where you look up a motion. This README is the entrance, not a second catalog.

Typical questions this library is built for:

- Is this idea real pain, and who should we sell first?
- What should the market believe, and which motion actually creates customers?
- What should the site, the outbound sentence, or the paid buy do—and how will we know?
- After they buy, how do we run the book, and is the number real?

Every tactic has its own operating question in the [master index](playbooks/). Do not grow this list when a page ships.

### Read it like a book

Read in order. Follow each page’s **What to read next**. Skip a chapter only when that decision is already written down.

1. [Idea discovery](playbooks/01-strategy-and-buyers/idea-discovery.md)
2. [Idea validation](playbooks/01-strategy-and-buyers/idea-validation.md)
3. [Ideal customer profile](playbooks/01-strategy-and-buyers/icp.md)
4. [Buying committee](playbooks/01-strategy-and-buyers/buying-committee.md)
5. [First ten customers](playbooks/01-strategy-and-buyers/first-ten-customers.md)
6. [Product-market fit](playbooks/01-strategy-and-buyers/product-market-fit.md)
7. [Four Fits](playbooks/01-strategy-and-buyers/four-fits.md)
8. [Positioning](playbooks/02-product-marketing/positioning.md)
9. [Sales enablement](playbooks/02-product-marketing/sales-enablement.md)
10. [Pricing and packaging](playbooks/02-product-marketing/pricing-and-packaging.md)
11. [Content strategy](playbooks/03-brand-story-and-content/content-strategy.md)
12. [Channel strategy](playbooks/04-channels-and-distribution/channel-strategy.md)
13. Then only the motion you named: [outbound](playbooks/05-outbound-and-prospecting/), [events](playbooks/06-account-field-and-partner/event-marketing.md) / [trade shows](playbooks/06-account-field-and-partner/trade-shows.md), or [ecosystem](playbooks/06-account-field-and-partner/ecosystem.md)

After positioning, the site scan starts at the [homepage](playbooks/07-website-and-conversion/homepage.md). Two scoreboards for what you publish or buy: [measurement model](playbooks/09-operations-pipeline-and-measurement/measurement-model.md). Ten minutes and no idea yet: [idea discovery](playbooks/01-strategy-and-buyers/idea-discovery.md). Already know the job: the [ICP field test](playbooks/01-strategy-and-buyers/icp.md#10-minute-field-test). Jumping to cold email with neither is how teams stay busy.

### Start with one decision

| Collection | Use it to | Start here |
|---|---|---|
| **Playbooks** | Find a capability, channel, or tactic | [Master index](playbooks/) |
| **Working files** | Open a sheet, scorecard, or 90-day outline | [42 working files](TEMPLATES.md) |
| **Tools** | Pick software for a defined job | [43-tool directory](TOOLS.md) |
| **Reading sources** | Follow operators without treating a feed as strategy | [19-source directory](RESOURCES.md) |
| **Agent Skill** | Route a task through the right method | [Install](#agent-skill) |
| **Verified use cases** | A named company, one motion, dated sources | Planned |

### Domains

Two levels: a **domain** owns a durable decision; a **tactic** executes one motion. All nine domains have a guide and at least one published tactic. Full maps live on each domain README.

| # | Domain | Decision | Published |
|---|---|---|---|
| 01 | [Strategy & buyers](playbooks/01-strategy-and-buyers/) | Where to compete, and who buys | 7 |
| 02 | [Product marketing](playbooks/02-product-marketing/) | What the market should understand and buy | 5 |
| 03 | [Brand, story & content](playbooks/03-brand-story-and-content/) | What future buyers remember before they are in-market | 2 |
| 04 | [Channels & distribution](playbooks/04-channels-and-distribution/) | Where the market repeatedly encounters the offer | 8 |
| 05 | [Outbound & prospecting](playbooks/05-outbound-and-prospecting/) | How to create conversations that have not been requested | 9 |
| 06 | [Account, field & partner](playbooks/06-account-field-and-partner/) | How marketing and sales coordinate around named accounts | 5 |
| 07 | [Website & conversion](playbooks/07-website-and-conversion/) | How owned pages help a buyer take the next step | 5 |
| 08 | [Lifecycle & customer](playbooks/08-lifecycle-and-customer-marketing/) | How to educate, retain, and expand after interest or purchase | 7 |
| 09 | [Operations, pipeline & measurement](playbooks/09-operations-pipeline-and-measurement/) | How data and process make the system repeatable | 16 |

Enterprise close (papering, procurement, multi-threaded negotiation) is outside this taxonomy. Quota pay, forecast, and post-sale operations that marketing must share sit in domains 06, 08, and 09. A later sales-ops collection would be separate.

### What every published playbook contains

1. A judgment a practitioner can argue with
2. When to use it and when not to
3. Operating method, with at least one worked pattern
4. Copyable templates, plus a [working file](TEMPLATES.md) when the job is a sheet or 90-day deck
5. Pre-flight checklist, metrics and non-metrics, common mistakes
6. Sources, evidence boundary, last-reviewed date, and **What to read next**

No empty placeholders. No anonymous “case studies” as fact. Named companies inside pages are **attributed illustrations** from dated sources, not the planned verified-use-case collection.

### Tools, sources, and the Skill

[TOOLS.md](TOOLS.md) — 43 products, 14 jobs. One primary job per product. Newer is not automatically better. Lensmor is owned by Ivan Xu and is disclosed in its row.

[RESOURCES.md](RESOURCES.md) — newsletters and operators, graded A/B/C, with access (free / freemium / paid). A feed is not a playbook.

### Agent Skill

```bash
npx skills add weilun88313/B2B-Playbook
```

```text
Use $b2b-playbook to evaluate these five target accounts.
Produce an ICP, buying-committee map, T1/T2/T3 decision,
and one next action per account. Mark unknowns instead of inventing facts.
```

The Skill routes. It does not send mail, enrich contacts, or write the CRM.

Third-party links keep existing query parameters and add `ref=b2b-playbook` before any fragment. That is a referrer tag, not an affiliate code.

### Evidence, language, maintenance

| State | Meaning |
|---|---|
| **Fact** | Dated, checkable record or quote |
| **Observation** | Pattern in a limited sample |
| **Assumption** | Unverified belief that changes the next action |
| **To validate** | A question plus a test that can close it |

End a work cycle with one decision and one next test.

- English is canonical for playbooks, tools, and the Skill. Chinese exists only in this README, as a full mirror of the entrance and coverage counts.
- Coverage or structure changes update both languages in the same commit.
- Ivan Xu (`weilun88313`) keeps one editorial voice. The library grows one complete tactic at a time.
- A verified use case ships only with a named company, a primary source, and a date.

Guidance is a starting method, not a guarantee or legal advice. If the library helps you do real work, a star helps other operators find it.

### Copyright and reuse

Copyright © 2026 Ivan Xu. All rights reserved. You may read, link to, and quote brief attributed excerpts. Republishing, translation, mirroring, substantial copying, commercial reuse, and reuse in redistributed datasets, knowledge bases, RAG systems, or model training require prior written permission. See the [full terms](LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)

---

## 中文

> 一个实用的 B2B 营销操作知识库，用于做出更好的市场进入决策，并将决策转化为可观察的工作。

**当前覆盖：** 64 篇已发布 Playbook · 42 份工作文件 · 43 个精选工具 · 19 个阅读源 · 9 个领域指南

**最后核验：** 2026-08-30

### 这是什么

面向 B2B 市场营销、创始人、营收团队和智能体的公开知识库。九个能力域管长期决策；每篇已发布战术都是可执行页。查具体动作请走 [总索引](playbooks/)。本 README 是入口，不是第二份目录。

它主要回答这类问题：

- 这个想法是真痛吗，先卖给谁？
- 市场该相信什么，哪条动作真正制造客户？
- 网站、外联句子、付费投放各该干什么——我们怎么知道有效？
- 成交之后这本书怎么管，那个数字是不是真的？

每篇战术自己的操作问题在 [总索引](playbooks/) 里。新页面上线时，不要再往这里加一条。

### 像一本书那样读

按顺序读。顺着每页的 **What to read next**。只有那一章的决策已经写下来了，才跳章。

1. [想法发现](playbooks/01-strategy-and-buyers/idea-discovery.md)
2. [想法验证](playbooks/01-strategy-and-buyers/idea-validation.md)
3. [理想客户画像](playbooks/01-strategy-and-buyers/icp.md)
4. [购买委员会](playbooks/01-strategy-and-buyers/buying-committee.md)
5. [前十个客户](playbooks/01-strategy-and-buyers/first-ten-customers.md)
6. [产品市场契合](playbooks/01-strategy-and-buyers/product-market-fit.md)
7. [四重契合](playbooks/01-strategy-and-buyers/four-fits.md)
8. [定位](playbooks/02-product-marketing/positioning.md)
9. [销售赋能](playbooks/02-product-marketing/sales-enablement.md)
10. [定价与包装](playbooks/02-product-marketing/pricing-and-packaging.md)
11. [内容策略](playbooks/03-brand-story-and-content/content-strategy.md)
12. [渠道策略](playbooks/04-channels-and-distribution/channel-strategy.md)
13. 然后只做你点名的那条：[外联](playbooks/05-outbound-and-prospecting/)、[活动](playbooks/06-account-field-and-partner/event-marketing.md) / [展会](playbooks/06-account-field-and-partner/trade-shows.md)，或 [生态](playbooks/06-account-field-and-partner/ecosystem.md)

定位之后，网站扫描从 [首页](playbooks/07-website-and-conversion/homepage.md) 开始。发布或买来的东西用两套计分板：[衡量模型](playbooks/09-operations-pipeline-and-measurement/measurement-model.md)。只有十分钟、还没有想法：[想法发现](playbooks/01-strategy-and-buyers/idea-discovery.md)。已经知道给谁做：[ICP 十分钟测试](playbooks/01-strategy-and-buyers/icp.md#10-minute-field-test)。两边都没有就写冷邮件，是团队一直很忙的原因。

### 从一个决策开始

| 内容入口 | 用来解决什么 | 从这里开始 |
|---|---|---|
| **Playbooks** | 查找能力、渠道或战术 | [总索引](playbooks/) |
| **工作文件** | 打开表格、记分表或 90 天大纲 | [42 份工作文件](TEMPLATES.md) |
| **工具** | 为明确任务选软件 | [43 个产品](TOOLS.md) |
| **阅读源** | 跟运营者，不把信息流当战略 | [19 个来源](RESOURCES.md) |
| **Agent Skill** | 把任务路由到正确方法 | [安装](#智能体-skill) |
| **已验证案例** | 具名公司、一个动作、带日期来源 | 计划中 |

### 领域

两层：**能力域**管长期决策，**战术页**执行一个动作。九个域都有指南，且都至少有一篇已发布战术。完整地图在各域 README。

| 编号 | 能力域 | 决策 | 已发布 |
|---|---|---|---|
| 01 | [战略与买家](playbooks/01-strategy-and-buyers/) | 在哪里竞争，谁来买 | 7 |
| 02 | [产品营销](playbooks/02-product-marketing/) | 市场该理解并购买什么 | 5 |
| 03 | [品牌、故事与内容](playbooks/03-brand-story-and-content/) | 进采购期前记住什么 | 2 |
| 04 | [渠道与分发](playbooks/04-channels-and-distribution/) | 市场在哪里反复碰到你 | 8 |
| 05 | [主动外联与潜客](playbooks/05-outbound-and-prospecting/) | 如何发起未被请求的对话 | 9 |
| 06 | [大客户、线下与伙伴](playbooks/06-account-field-and-partner/) | 如何围着具名账户协同 | 5 |
| 07 | [网站与转化](playbooks/07-website-and-conversion/) | 自有页面如何帮买家走下一步 | 5 |
| 08 | [生命周期与客户](playbooks/08-lifecycle-and-customer-marketing/) | 兴趣或成交之后如何教育、留存、扩展 | 7 |
| 09 | [运营、Pipeline 与衡量](playbooks/09-operations-pipeline-and-measurement/) | 数据和流程如何让系统可重复 | 16 |

企业成交流程（合同、采购、多线程谈判）不在这套分类里。营销必须共享的配额、预测和成交后运营放在 06、08、09。若以后单独做销售运营，会另开顶层。

### 每篇已发布 Playbook 包含什么

1. 一个从业者可以争论的判断
2. 何时用、何时不用
3. 操作方法，至少有一个可对照的模式
4. 可复制模板；工作是表格或 90 天大纲时另有 [工作文件](TEMPLATES.md)
5. 起飞前清单、该看和不该看的指标、常见错误
6. 来源、证据边界、核验日期，以及 **What to read next**

不发布空占位，也不把匿名「案例」当成事实。正文里的具名公司是带日期来源的**插图**，不是计划中的已验证案例专栏。

### 工具、阅读源与 Skill

[TOOLS.md](TOOLS.md) — 43 个产品、14 个任务。每个产品一个主任务。新不等于更好。Lensmor 由 Ivan Xu 维护，条目中已披露。

[RESOURCES.md](RESOURCES.md) — Newsletter 与运营者，A/B/C 分级，并标明免费 / 免费+付费层 / 付费。信息流不能代替 Playbook。

### 智能体 Skill

```bash
npx skills add weilun88313/B2B-Playbook
```

```text
使用 $b2b-playbook 评估这 5 个目标账户。
输出 ICP、购买委员会地图、T1/T2/T3 分级，
以及每个账户的下一步行动。标记未知信息，不要编造事实。
```

Skill 只负责路由，不发信、不补全联系人、不改 CRM。

第三方链接保留原有参数，并在锚点前加上 `ref=b2b-playbook`。这是来源标记，不是 Affiliate。

### 证据、语言与维护

| 状态 | 含义 |
|---|---|
| **事实** | 可核验的带日期记录或引语 |
| **观察** | 有限样本里的模式 |
| **假设** | 未验证、但会改变下一步的判断 |
| **待验证** | 一个问题，加上能关掉它的测试 |

每个工作周期以一个决策和下一个测试结束。

- Playbook、工具和 Skill 的正文只维护英文。中文只在本 README，完整同步入口和覆盖数。
- 结构或覆盖变化时，中英文必须同一次提交更新。
- Ivan Xu（`weilun88313`）用同一套口径维护。知识库一次只完整发布一篇战术。
- 已验证案例必须有企业名、一手来源和日期。

内容是行动起点，不是结果保证或法律意见。如果它对你的真实工作有用，欢迎点 Star，让更多人发现。

### 版权与使用

版权所有 © 2026 Ivan Xu，保留全部权利。允许阅读、分享链接，以及在注明作者和正版来源的前提下少量引用；转载、翻译、镜像、大段复制、商业使用，以及用于对外分发的数据集、知识库、RAG 或模型训练，须事先书面许可。完整规则见 [LICENSE](LICENSE)。

唯一正版来源：[github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
