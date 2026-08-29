# 09 · Operations, pipeline & measurement

> **Decision owned:** How should data, process, technology, and measurement make the marketing system repeatable?

**Status:** Domain guide published · 1 tactic playbook published

**Last reviewed:** 2026-08-29

## Scope

This domain provides the operating system underneath B2B marketing. It defines shared lifecycle and pipeline language, data models, scoring, routing, measurement, experimentation, planning, technology governance, and privacy controls.

It owns marketing operations and measurement decisions—not every tool configuration, and not the sales team's opportunity-management process or a full enterprise close. Its purpose is to make work observable, comparable, recoverable, and improvable without pretending attribution can prove causality on its own.

Quota-carrying pay sits here as **GTM operations**: the number marketing and sales share has to be credited, calculated, and paid, or it is not a number. Papering, procurement, and multi-threaded close stay outside this taxonomy.

## Core decisions

1. Which lifecycle, funnel, account, and pipeline states need shared definitions?
2. Which events and fields are required to observe meaningful progression?
3. How should qualification, scoring, routing, ownership, and service levels work?
4. What belongs in the CRM, warehouse, automation layer, and reporting layer?
5. Which metrics are leading indicators, business outcomes, diagnostics, or guardrails?
6. Which questions require attribution, incrementality, experiments, or qualitative evidence?
7. How will budget, technology, privacy, consent, data quality, and change control be governed?
8. When people carry quota, how will they be paid against a credit rule the company can administer?

## Playbook map

| Topic | Status | Operating question |
|---|---|---|
| Sales compensation | Published: [`sales-compensation.md`](sales-compensation.md) | How should quota-carrying people be paid, credited, told the plan, and paid on time? |
| Measurement model | Planned: `measurement-model.md` | Which decisions should each metric support? |
| Funnel model | Planned: `funnel-model.md` | How should audience and buyer progression be represented before pipeline? |
| Pipeline model | Planned: `pipeline-model.md` | How should marketing contribution connect to qualified revenue progression? |
| Lifecycle stages | Planned: `lifecycle-stages.md` | Which shared states and transition rules should systems enforce? |
| Lead scoring | Planned: `lead-scoring.md` | When does person-level fit and behavior justify a different action? |
| Account scoring | Planned: `account-scoring.md` | How should account fit, engagement, relationships, and timing be combined? |
| Routing and SLA | Planned: `routing-and-sla.md` | Who should act on each signal, by when, and with what context? |
| CRM data model | Planned: `crm-data-model.md` | Which objects, fields, relationships, and sources form the commercial record? |
| Attribution | Planned: `attribution.md` | What can touchpoint models reveal, and what can they not prove? |
| Dashboards | Planned: `dashboards.md` | Which views help an operator make a recurring decision? |
| Experimentation | Planned: `experimentation.md` | Which test can produce a credible learning or causal estimate? |
| Budget and planning | Planned: `budget-and-planning.md` | How should resources follow strategy, capacity, evidence, and risk? |
| MarTech governance | Planned: `martech-governance.md` | When should a tool be added, integrated, reviewed, or removed? |
| Privacy and compliance operations | Planned: `privacy-and-compliance-operations.md` | How should consent, lawful use, retention, access, and deletion be operationalized? |

Planned filenames are an editorial roadmap, not empty pages. A tactic file is created only when its guidance, templates, metrics, and evidence are ready.

## Recommended build order

1. Agree on lifecycle, funnel, pipeline, ownership, and success definitions.
2. Define the minimum CRM and event data model required to observe them.
3. Implement qualification, scoring, routing, suppression, and service levels.
4. Build decision-oriented dashboards and explicit attribution boundaries.
5. Add experimentation, budget, MarTech, privacy, and data-quality governance.

When the go-to-market motion includes quota-carrying sellers, run [sales compensation](sales-compensation.md) as a **parallel path**—after the role exists and a credit event can be named—not as step one of marketing ops.

## Interfaces with other domains

- [Strategy & buyers](../01-strategy-and-buyers/) supplies qualification hypotheses and disqualifiers. Compensation for a hunter who still has no [first ten](../01-strategy-and-buyers/first-ten-customers.md) is premature.
- [Product marketing](../02-product-marketing/) sets what the **buyer** pays ([pricing](../02-product-marketing/pricing-and-packaging.md)) and how the first meeting sounds ([sales enablement](../02-product-marketing/sales-enablement.md)). Seller pay is a different contract.
- [Channels & distribution](../04-channels-and-distribution/) decides whether a quota-carrying role should exist ([channel strategy](../04-channels-and-distribution/channel-strategy.md)).
- [Outbound & prospecting](../05-outbound-and-prospecting/) generate signals that require common capture and interpretation.
- [Account, field & partner marketing](../06-account-field-and-partner/) requires account-level orchestration, cost, and progression measurement.
- [Lifecycle & customer marketing](../08-lifecycle-and-customer-marketing/) depends on reliable states, triggers, consent, and customer outcomes.

[Back to the playbook index](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
