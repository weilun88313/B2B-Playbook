---
title: "CRM data model"
sidebarTitle: "CRM Data Model"
---

# CRM data model

**Last reviewed:** 2026-08-29

A CRM is a **commercial record**: the objects, fields, relationships, and sources the company will actually operate. It is not a museum of every field anyone ever added. Migrating without a map is how junk travels, integrations break, and [forecasting](forecasting.md) inherits two dictionaries for “stage.”

This page is the field map and the spring-clean. It is not a Salesforce admin course, not a vendor bake-off ([MarTech governance](martech-governance.md)), and not the credit rule in [sales compensation](sales-compensation.md). Those pages assume this record exists.

## Use this when

- You are moving orgs, or “we will clean it after go-live” is the current plan.
- Marketing, sales, and CS cannot name the same fields for MQL, owner, and next step.
- Nobody knows which fields are populated versus ceremonial.
- You are about to buy automation on top of a model nobody mapped.

## Do not use this when

- There is no [ICP](../01-strategy-and-buyers/icp.md) and no stages. You will migrate a mess with better branding.
- You need a weekly forecast call. That is [forecasting](forecasting.md).
- Legal hold, privacy, or deletion rules must be designed by qualified owners. This is not that advice.

## One rule

**Map left to right, and count records before you keep a field.** Legacy label, API name, data type, and **how many records actually have a value**. New side: label, API name, data type, standard vs custom. Types must match. A picklist (or multi-select) is not “text we will fix later”—it gets its own value list.

## Operating method

### Step 1: name the objects you will actually move

Start with **Lead, Account, Contact, Opportunity** if that is your commercial spine. Duplicate the map for every extra object you insist on (Task, Contract, custom objects). If you cannot say who lives in the object day-to-day, do not migrate it “just in case.”

### Step 2: inventory the legacy side with population

For each field: label, API name, type, populated count. Empty custom fields are candidates for death, not for a matching custom field in the new org. Operators often run a field-population audit in the current CRM before they copy the schema. The point is the **count**, not a branded app.

### Step 3: match to the new org—or refuse the field

Right side: the counterpart. Standard if the new CRM already has the job. Custom only if you can name the report, workflow, or legal need. Data types must match (date is not text; picklist is not a long dump). If the new system cannot hold the type, you are designing a transformation, not a rename.

### Step 4: picklists are a separate sheet

Every picklist and multi-select: object, field, values. Stage names here must be the same words [forecasting](forecasting.md) and [lead scoring](lead-scoring.md) use. Hidden synonyms (“SQL” vs “Sales Qualified”) are how routing dies.

### Step 5: freeze the map before automation

Integrations, sequences, and scoring write to **this** map. If [MarTech governance](martech-governance.md) later finds a tool that cannot two-way sync a field you marked required, that is a stack decision—not a surprise in week three. Date the map. Changing it after go-live is a migration of its own.

## Teaching fill (invented—not a customer)

Sales-assist. Leaving a cluttered HubSpot for a tighter CRM. Not your schema.

| Object | Keep | Kill or transform |
|---|---|---|
| Lead | Email, company, source, score, owner, MQL date | Twelve unused “UTM extra” customs with &lt;20 populated rows |
| Account | Domain, segment, ICP tier, owner | Duplicate “industry” picklists with different values |
| Contact | Role, buying seat, consent | Personal mobile with no lawful-use note—parked, not mapped |
| Opportunity | Amount, close date, stage, next step, forecast category | “Temperature” as a vibe field with no entry criteria |
| Picklist | Stages = the five names on the forecast page | “Open / Working / Hot” retired |

## Copy: model one-pager (fill)

- From-org / to-org / freeze date / owner:
- Objects in scope (and objects we will **not** move):
- Required fields for MQL, SQL, opportunity, handoff:
- Population rule (below *n* records → kill or archive):
- Picklist fields that must match forecast/scoring language:
- Integrations that write to this map:
- Who may add a custom field after freeze:

Working file: [crm-field-map.xlsx](../../templates/crm-field-map.xlsx).

## Pre-flight checklist

- [ ] Lead, Account, Contact, Opportunity (or your spine) each have a map.
- [ ] Every kept field has a populated-count or an explicit “new, empty on purpose.”
- [ ] Standard vs custom is marked on the new side.
- [ ] Data types match or a transform is written.
- [ ] Picklist values are listed, not implied.
- [ ] Extra objects were duplicated as tabs, not forgotten in Slack.
- [ ] Stage language matches the forecast page.
- [ ] The map is dated before automation is rebuilt.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Fields mapped vs fields in the live org | Completeness of the inventory |
| Kept fields with near-zero population | Museum vs record |
| Stage-name mismatches vs forecast | Two dictionaries |
| Custom fields created after freeze | Model drift |

Do not count objects created, or resemblance to a Salesforce-shaped template, as a model.

## Common mistakes

- Migrating every field because someone might need it.
- Matching labels and ignoring types.
- Picklists left as free text.
- Stage names that do not match [forecasting](forecasting.md).
- Rebuilding scoring and sequences before the map exists.
- Copying another company’s objects (including a sample Lead/Account/Contact/Opportunity set) as if they were yours.

## What to read next

What the score **does** at a threshold is [lead scoring](lead-scoring.md). Whether a tool may write into this record is [MarTech governance](martech-governance.md). Post-sale intelligence (value, cadence, renewal, risk) is [CS workspace](../08-lifecycle-and-customer-marketing/cs-workspace.md). The number people call sits in [forecasting](forecasting.md). If you are still inventing the commercial motion, stay in [channel strategy](../04-channels-and-distribution/channel-strategy.md).

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not a licensed migration product, not Salesforce administration advice, and not a vendor implementation quote.

The left-to-right field map (label, API name, type, record count → new label, API, type, standard/custom), object tabs for Lead / Account / Contact / Opportunity, duplicating sheets for extra objects, a dedicated picklist-values tab, and “audit population before you copy junk” are distilled from an operator CRM-migration workbook (blank mapping file). That file is a **method prompt**, not a source to copy. Author contact details, community Slack handles, agency matching, and named admin utilities in its pro tips are not imported as requirements.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
