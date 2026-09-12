---
title: "Funnel model"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

A funnel model represents observable progression toward a defined outcome. It is useful for locating operational gaps, but it should not imply that every buyer follows one linear path or that anonymous audience reach can be joined perfectly to CRM records.

## Define the unit and boundary

Choose whether the model counts people, accounts, sessions, or buying opportunities. Keep different units in separate views unless the relationship is explicitly modeled. Ten contacts at one company are not ten independent account opportunities.

## Build the model

1. **Name the stages in plain language.** Use observable states such as valid inquiry, accepted conversation, and qualified opportunity. Define the evidence required for entry and which team records it.
2. **Specify counting rules.** Decide how duplicates, repeated inquiries, reactivation, and multiple opportunities are treated. Preserve event dates instead of relying only on today's stage.
3. **Choose cohort or period reporting.** A cohort follows entities entering in one window; a period report counts events happening in that window. They answer different questions and should not share an unlabeled conversion rate.
4. **Account for time.** Allow a suitable observation window and show unresolved entities. A recent cohort may look weak simply because its buying process has not had time to progress.
5. **Inspect exits and skipped stages.** Record disqualification reasons and legitimate alternate paths. Do not invent missing intermediate events to make every record fit the diagram.
6. **Use the model to choose an investigation.** Compare segments with consistent definitions, then read actual records around the suspected gap. A rate alone does not explain the cause.

## Worked example

A hypothetical September cohort contains 100 valid inquiries. By the review date, 30 have an accepted conversation and 12 have become qualified opportunities. The observed inquiry-to-opportunity rate is 12%, while accepted-conversation-to-opportunity progression is 40%, assuming those 12 belong to the same 30.

If October's opportunity count includes older inquiries, dividing it by September's inquiries would mix populations. The dashboard shows the cohort's age and unresolved cases so the team does not treat the early rate as final.

## Stage dictionary

| Stage | Unit | Entry evidence | Timestamp | Owner | Exit/re-entry rule |
|---|---|---|---|---|---|
| Valid inquiry | | | | | |
| Accepted conversation | | | | | |
| Qualified opportunity | | | | | |

## Sanity checks

Reconcile a sample of records to the source system. Investigate impossible dates, duplicate entities, and changes in stage definitions. Keep reach and brand research in companion views when they cannot be reliably joined to individual buying records. The model's visibility limit is part of the report.

## Sources and scope

- [HubSpot: lifecycle stages](https://knowledge.hubspot.com/records/use-lifecycle-stages?region=canada&ref=b2b-playbook) illustrates contact/company stage behavior in one CRM; design and test your own transition rules rather than assuming identical platform behavior.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Lifecycle stages](lifecycle-stages.md) · [Pipeline model](pipeline-model.md) · [Measurement model](measurement-model.md)

[Chapter guide](README.md) · [All playbooks](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
