---
title: "09 · Operations, pipeline & measurement"
---

> **Decision owned:** How should data, process, technology, and measurement make the marketing system repeatable?

**Status:** Domain guide published · 16 tactic playbooks published

**Last reviewed:** 2026-08-30

## Scope

This domain provides the operating system underneath B2B marketing. It defines shared lifecycle and pipeline language, data models, scoring, routing, measurement, experimentation, planning, technology governance, and privacy controls.

It owns marketing operations and measurement decisions—not every tool configuration, and not the sales team's opportunity-management process or a full enterprise close. Its purpose is to make work observable, comparable, recoverable, and improvable without pretending attribution can prove causality on its own.

Quota-carrying pay, **when** that pay is safe, the **forecast**, and the **weekly calendar** that keeps those jobs from eating each other sit here as **GTM operations**. Papering, procurement, and multi-threaded close stay outside this taxonomy.

## Core decisions

1. Which lifecycle, funnel, account, and pipeline states need shared definitions?
2. Which events and fields are required to observe meaningful progression?
3. How should qualification, scoring, routing, ownership, and service levels work?
4. What belongs in the CRM, warehouse, automation layer, and reporting layer?
5. Which metrics are leading indicators, business outcomes, diagnostics, or guardrails?
6. Which questions require attribution, incrementality, experiments, or qualitative evidence?
7. How will budget, technology, privacy, consent, data quality, and change control be governed?
8. When people carry quota, how will they be paid against a credit rule the company can administer?
9. How will hygiene, stages, categories, and calls make a forecast that leadership can defend?
10. When does person-level fit and behavior justify a different action?
11. Can demand creation and sales capacity produce the same number?
12. What should a new sales leader actually do in 90 days?
13. Which objects and fields are the commercial record, and what will we refuse to migrate?
14. Which job may a tool do, and when do we remove it?
15. How should weekly meetings split pipeline, forecast, and coaching?
16. When is commission safe, and how do we reverse or advance it without improvising?
17. How should RevOps be paid without a second sales quota?
18. Which test can produce a credible learning or causal estimate?
19. Where does each GTM motion sit on the AI ladder, and which rung do we climb next?
20. Which company problem deserves an AI bet this quarter—not which tool?
21. What artifact, gate, and collapse must exist before we build a workflow?
22. How do the sales–finance and product–marketing calendars snap together without a launch on the close?

## Playbook map

| Topic | Status | Operating question |
|---|---|---|
| Sales compensation | Published: [`sales-compensation.md`](/playbooks/09-operations-pipeline-and-measurement/sales-compensation) | How should quota-carrying people be paid, credited, told the plan, and paid on time? |
| Forecasting | Published: [`forecasting.md`](/playbooks/09-operations-pipeline-and-measurement/forecasting) | How should hygiene, stages, categories, and calls make a number leadership can defend? |
| Lead scoring | Published: [`lead-scoring.md`](/playbooks/09-operations-pipeline-and-measurement/lead-scoring) | When does person-level fit and behavior justify a different action? |
| GTM planning | Published: [`gtm-planning.md`](/playbooks/09-operations-pipeline-and-measurement/gtm-planning) | Can demand creation and sales capacity produce the same number? |
| Sales-leadership ramp | Published: [`sales-leadership-ramp.md`](/playbooks/09-operations-pipeline-and-measurement/sales-leadership-ramp) | What should a new sales leader actually do in 90 days? |
| CRM data model | Published: [`crm-data-model.md`](/playbooks/09-operations-pipeline-and-measurement/crm-data-model) | Which objects and fields are the commercial record, and what will we refuse to migrate? |
| MarTech governance | Published: [`martech-governance.md`](/playbooks/09-operations-pipeline-and-measurement/martech-governance) | Which job may a tool do, and when do we remove it? |
| Sales operating cadence | Published: [`sales-operating-cadence.md`](/playbooks/09-operations-pipeline-and-measurement/sales-operating-cadence) | How should weekly meetings split pipeline, forecast, and coaching? |
| Company cadence | Published: [`company-cadence.md`](/playbooks/09-operations-pipeline-and-measurement/company-cadence) | How do the sales–finance and product–marketing calendars snap together? |
| Incentive timing | Published: [`incentive-timing.md`](/playbooks/09-operations-pipeline-and-measurement/incentive-timing) | When is commission safe, and how do we reverse or advance it without improvising? |
| RevOps compensation | Published: [`revops-compensation.md`](/playbooks/09-operations-pipeline-and-measurement/revops-compensation) | How should RevOps be paid without a second sales quota? |
| Experimentation | Published: [`experimentation.md`](/playbooks/09-operations-pipeline-and-measurement/experimentation) | Which test can produce a credible learning or causal estimate? |
| GTM AI maturity | Published: [`gtm-ai-maturity.md`](/playbooks/09-operations-pipeline-and-measurement/gtm-ai-maturity) | Where does each motion sit on the AI ladder, and which rung do we climb next? |
| AI use-case selection | Published: [`ai-use-case-selection.md`](/playbooks/09-operations-pipeline-and-measurement/ai-use-case-selection) | Which company problem deserves an AI bet this quarter—not which tool? |
| AI workflow | Published: [`ai-workflow.md`](/playbooks/09-operations-pipeline-and-measurement/ai-workflow) | What artifact, gate, and collapse must exist before we build? |
| [Measurement model](/playbooks/09-operations-pipeline-and-measurement/measurement-model) | Published | Which decisions should each metric support—and what requires a human or a test? |
| Funnel model | Planned: `funnel-model.md` | How should audience and buyer progression be represented before pipeline? |
| Pipeline model | Planned: `pipeline-model.md` | How should marketing contribution connect to qualified revenue progression? |
| Lifecycle stages | Planned: `lifecycle-stages.md` | Which shared states and transition rules should systems enforce? |
| Account scoring | Planned: `account-scoring.md` | How should account fit, engagement, relationships, and timing be combined? |
| Routing and SLA | Planned: `routing-and-sla.md` | Who should act on each signal, by when, and with what context? |
| Attribution | Planned: `attribution.md` | Deeper model math. Two scoreboards and HDYHAU already live in [measurement model](/playbooks/09-operations-pipeline-and-measurement/measurement-model). |
| Dashboards | Planned: `dashboards.md` | Which views help an operator make a recurring decision? |
| Budget and planning | Planned: `budget-and-planning.md` | How should resources follow strategy, capacity, evidence, and risk? |
| Privacy and compliance operations | Planned: `privacy-and-compliance-operations.md` | How should consent, lawful use, retention, access, and deletion be operationalized? |

Planned filenames are an editorial roadmap, not empty pages. A tactic file is created only when its guidance, templates, metrics, and evidence are ready.

## Recommended build order

1. Agree on lifecycle, funnel, pipeline, ownership, and success definitions.
2. Define the minimum CRM and event data model required to observe them.
3. Implement qualification, scoring, routing, suppression, and service levels.
4. Write [measurement model](/playbooks/09-operations-pipeline-and-measurement/measurement-model) (two scoreboards + HDYHAU) before buying another attribution schema. Dashboards stay planned.
5. Add experimentation, budget, MarTech, privacy, and data-quality governance.

When the go-to-market motion includes quota-carrying sellers, run [sales compensation](/playbooks/09-operations-pipeline-and-measurement/sales-compensation) and [forecasting](/playbooks/09-operations-pipeline-and-measurement/forecasting) as **parallel paths**—after the role exists and a credit event can be named—not as step one of marketing ops. Compensation is how people get paid. [Incentive timing](/playbooks/09-operations-pipeline-and-measurement/incentive-timing) is when that pay is safe. Forecasting is whether the path to that number is real. The calendar that keeps pipe-gen, the call, and coaching from sharing one hour is [sales operating cadence](/playbooks/09-operations-pipeline-and-measurement/sales-operating-cadence). The quarterly superstructure that keeps launch off the close is [company cadence](/playbooks/09-operations-pipeline-and-measurement/company-cadence). Whether next year’s number is even possible is [GTM planning](/playbooks/09-operations-pipeline-and-measurement/gtm-planning). Assumptions inside that plan that have not been tested belong in [experimentation](/playbooks/09-operations-pipeline-and-measurement/experimentation). A new sales leader’s first 90 days are [sales-leadership ramp](/playbooks/09-operations-pipeline-and-measurement/sales-leadership-ramp). Ops leaders are not a second AE quota: [RevOps compensation](/playbooks/09-operations-pipeline-and-measurement/revops-compensation). Inbound volume that needs a routing hypothesis uses [lead scoring](/playbooks/09-operations-pipeline-and-measurement/lead-scoring). The commercial record is [CRM data model](/playbooks/09-operations-pipeline-and-measurement/crm-data-model). Tools that write into it need [MarTech governance](/playbooks/09-operations-pipeline-and-measurement/martech-governance). Whether the team is actually climbing an AI ladder—or collecting seats—is [GTM AI maturity](/playbooks/09-operations-pipeline-and-measurement/gtm-ai-maturity). Which problem deserves a bet is [AI use-case selection](/playbooks/09-operations-pipeline-and-measurement/ai-use-case-selection). How that bet is staged is [AI workflow](/playbooks/09-operations-pipeline-and-measurement/ai-workflow). Which decisions a metric may support is [measurement model](/playbooks/09-operations-pipeline-and-measurement/measurement-model).

## Interfaces with other domains

- [Strategy & buyers](/playbooks/01-strategy-and-buyers) supplies qualification hypotheses and disqualifiers. Compensation for a hunter who still has no [first ten](/playbooks/01-strategy-and-buyers/first-ten-customers) is premature.
- [Product marketing](/playbooks/02-product-marketing) sets what the **buyer** pays ([pricing](/playbooks/02-product-marketing/pricing-and-packaging)), how the first meeting sounds ([sales enablement](/playbooks/02-product-marketing/sales-enablement)), and how the product walk is scored ([demo](/playbooks/02-product-marketing/demo)). Seller pay is a different contract.
- [Channels & distribution](/playbooks/04-channels-and-distribution) decides whether a quota-carrying role should exist ([channel strategy](/playbooks/04-channels-and-distribution/channel-strategy)). Message and channel bets that are still assumptions use [experimentation](/playbooks/09-operations-pipeline-and-measurement/experimentation). Discoverability of owned answers is [SEO and AEO](/playbooks/04-channels-and-distribution/seo-and-aeo).
- [Outbound & prospecting](/playbooks/05-outbound-and-prospecting) generate signals that require common capture and interpretation. Hired SDRs need [onboarding](/playbooks/05-outbound-and-prospecting/sdr-onboarding) that teaches the same credit rule [sales compensation](/playbooks/09-operations-pipeline-and-measurement/sales-compensation) writes.
- [Account, field & partner marketing](/playbooks/06-account-field-and-partner) requires account-level orchestration, cost, and progression measurement. Named-account quality that feeds a call lives in [account planning](/playbooks/06-account-field-and-partner/account-planning).
- [Lifecycle & customer marketing](/playbooks/08-lifecycle-and-customer-marketing) depends on reliable states, triggers, consent, and customer outcomes. After close, [customer success](/playbooks/08-lifecycle-and-customer-marketing/customer-success) and [customer onboarding](/playbooks/08-lifecycle-and-customer-marketing/customer-onboarding) keep the book observable; post-sale fields that serve CS sit in [CS workspace](/playbooks/08-lifecycle-and-customer-marketing/cs-workspace).

[Back to the playbook index](/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
