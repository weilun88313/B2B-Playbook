---
title: "CS workspace"
sidebarTitle: "CS Workspace"
---

**Last reviewed:** 2026-08-30

[CRM data model](../09-operations-pipeline-and-measurement/crm-data-model.md) is the commercial spine (Lead, Account, Contact, Opportunity). This page is the **post-sale intelligence layer**: which objects, fields, views, and automations must exist so a CSM can do the job in [customer success](customer-success.md) without a second brain in a spreadsheet.

Service clouds and CS platforms give you tools. They do not give you an operating model. If a property does not help you see **value realized**, **relationship cadence**, **renewal risk**, or **leading risk**, it is swamp. HubSpot, Salesforce, Gainsight, or a Sheet are implementations. The four questions are the architecture.

This is not a HubSpot admin course, not a vendor migration SOW, and not a promise that workflows will save a missing charter.

## Use this when

- CSMs live in a private spreadsheet because the CRM cannot show the book.
- Health is a formula nobody trusts, and the dashboard is a screenshot.
- You are “moving to Service Hub / Gainsight / ChurnZero” and the plan is to copy every field.
- Automation creates tasks the team ignores.

## Do not use this when

- There is no CS job sentence. Write [customer success](customer-success.md) first.
- You need the sales opportunity model. That is [CRM data model](../09-operations-pipeline-and-measurement/crm-data-model.md) and [forecasting](../09-operations-pipeline-and-measurement/forecasting.md).
- You need software names. Start in [TOOLS.md](../../TOOLS.md), then [MarTech governance](../09-operations-pipeline-and-measurement/martech-governance.md).
- Legal hold or privacy design is the request. Qualified owners; this is not that advice.

## Words you will use

| Word | Meaning here |
|---|---|
| **Realization** | Are they getting the outcome they bought—not only logins? |
| **Relationship** | Do we have a dated cadence (QBR, check-in) that matches the tier? |
| **Renewal** | Where is the revenue, the date, the owner, the stage? |
| **Risk** | What leading signals (usage drop, champion leave, unpaid, dark) require a play this week? |

## One rule

**Every field, workflow, and saved view must serve one of the four questions—or it is killed.** “Nice to have for a future report” is how you recreate the last CS tool’s swamp. If you are migrating, move what you **operate**; leave ceremonial customs behind—same discipline as a CRM field map.

## Operating method

### Step 1: name where the four answers live

Write, for your stack:

- **Realization:** which object holds outcomes, milestones, TTV (see [customer onboarding](customer-onboarding.md)). Usage may feed it; usage is not it.
- **Relationship:** last strategic touch, next QBR, tier, owner. Cadence is a date, not a vibe.
- **Renewal:** opportunity or equivalent, amount, date, stage language that matches [forecasting](../09-operations-pipeline-and-measurement/forecasting.md). Upsell: same object or a rule you can explain.
- **Risk:** the weekly at-risk list’s fields—why red, owner, next action. Champion-left, gone-dark, unpaid, expected vs surprise churn are **plays** on [customer success](customer-success.md), not mystery scores.

If two systems both claim “health,” pick a source of truth or you will argue in the QBR.

### Step 2: properties that matter—then stop

Inventory like a field map: label, populated count, which of the four jobs, keep / kill / transform. CSMs track activity in the CRM they already work, not in a shadow tool, unless [MarTech governance](../09-operations-pipeline-and-measurement/martech-governance.md) said the overlay may write back.

Do not import another operator’s HubSpot property list. Their 25 years and client ARR are not your schema.

### Step 3: automate last, and only noisy-if-missed work

Automate what the team already does by hand and **misses**: renewal created N days out, inactivity after a defined dark period, handoff task when opp closes. Leave judgment (save-path, commercial exception) manual. Workflows that create false-positive tasks train people to ignore the system.

### Step 4: views the team will open on Monday

One queue for at-risk. One for renewals this quarter. One for onboarding still open. Filters that match [sales operating cadence](../09-operations-pipeline-and-measurement/sales-operating-cadence.md) thinking: one view, one question. Vanity NRR charts for Slack are not a workspace.

### Step 5: integrate only if the job needs a write

Another system’s data is not a reason to sync. If you cannot name the field on the four-question list, do not connect it. Consolidation beats a fourth “CS source of truth.”

### Step 6: migrate with a freeze date

From Gainsight, ChurnZero, Salesforce CS clouds, or Sheets: sequence like [CRM data model](../09-operations-pipeline-and-measurement/crm-data-model.md)—objects you operate, populated fields, picklists that match forecast language. Leave the swamp. A “lift and shift” is how you pay for two swamps.

## Teaching fill (invented—not a customer)

Forty logos. CRM is the system of record. Not a HubSpot blueprint.

| Job | Keep | Kill |
|---|---|---|
| Realization | Milestone “first value” date, TTV vs plan | Twelve unused “sentiment” customs |
| Relationship | Next QBR, last strategic touch, tier | Duplicate “check-in vibe” |
| Renewal | Renewal opp 120 days out, amount, stage = forecast names | A second ARR field CS updates by hand |
| Risk | At-risk reason, owner, next action; unpaid flag | Health 0–100 nobody can explain |

## Copy: workspace one-pager (fill)

- Realization fields / object:
- Relationship fields (cadence dates, tier, owner):
- Renewal object and stage language:
- Risk fields and the Monday view:
- Automations we will ship (and ones we refuse):
- Systems we will **not** sync:
- Migration: from-system, freeze date, what we leave behind:

Working file: [cs-workspace.xlsx](../../templates/cs-workspace.xlsx).

## Pre-flight checklist

- [ ] Each kept field maps to realization, relationship, renewal, or risk.
- [ ] Renewal stages match the forecast page.
- [ ] One Monday view per question; no dashboard of everything.
- [ ] Automation has a miss-cost, not a “would be cool.”
- [ ] Migration has a kill list, not only a keep list.
- [ ] Health, if it exists, has a written formula and an owner.
- [ ] No HubSpot/Gainsight property dump as the model.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Fields mapped to one of four jobs vs live org | Swamp vs record |
| CSM time in CRM vs shadow sheet | Whether the workspace is real |
| Workflows opened vs completed | Noise |
| At-risk list age | Risk view vs theater |

Do not count objects created, or resemblance to a paid HubSpot CS manual, as a workspace.

## Common mistakes

- Copying Service Hub defaults and calling it a playbook.
- Health score with no formula.
- Automating judgment.
- Syncing everything “in case.”
- Migrating unused Gainsight fields.
- Treating vendor ARR claims as evidence your schema will work.
- Building the workspace before [customer success](customer-success.md) names who owns renewals.

## What to read next

The jobs this record serves are [customer success](customer-success.md). Implementation clocks are [customer onboarding](customer-onboarding.md). Additional value on evidence is [expansion marketing](expansion-marketing.md). The clock before the commercial path is [renewal marketing](renewal-marketing.md). The commercial spine is [CRM data model](../09-operations-pipeline-and-measurement/crm-data-model.md). Tools still need [MarTech governance](../09-operations-pipeline-and-measurement/martech-governance.md). A new CS leader’s audit of this workspace is [CS-leadership ramp](cs-leadership-ramp.md).

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not HubSpot documentation, not a Gainsight implementation, and not a licensed CS platform.

The four-job test (realization, relationship, renewal, risk) and the instruction that properties, workflows, and views must serve those jobs—or they do not belong—are distilled from a public operator landing page for a HubSpot CS workspace manual ([Infinite Renewals](https://info.infiniterenewals.com/customer-success-in-hubspot?ref=b2b-playbook)). That page is a **method prompt**, not a source to copy. The gated manual, HubSpot click-paths, $1.8B client-ARR claim, and partner pitches are **not** this library’s schema or a requirement to buy a course. Object-model and migration *discipline* still follow this repository’s CRM field-map page.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
