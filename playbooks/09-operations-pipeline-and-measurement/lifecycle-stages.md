---
title: "Lifecycle stages"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

Lifecycle stages are shared states that help systems and teams agree what has happened and what should happen next. They need explicit transition rules, not just familiar labels such as lead, qualified, or customer.

## Separate the objects

A person, account, and opportunity can be in different states at the same time. An existing customer can open a new expansion opportunity, and a new contact can belong to that customer account. Avoid overwriting one object with another object's meaning.

## Define and implement the state model

1. **Write each state's meaning.** Specify the object, entry evidence, owner, and allowed next actions. Use the fewest states that support distinct operational decisions.
2. **Define transitions.** Record the event, prerequisite, responsible system, timestamp, and behavior for missing evidence. Decide whether regression is allowed and how reactivation is represented.
3. **Preserve history.** Keep stage-change events or equivalent auditable history for cohort analysis. A current-stage field cannot reconstruct time spent in prior states by itself.
4. **Resolve competing writers.** Document which workflows, integrations, imports, and users may change each field. Set precedence so a stale import cannot silently undo a valid customer transition.
5. **Test exceptional paths.** Include skipped stages, duplicate merges, lost opportunities, existing customers, reopened evaluations, and deleted or suppressed contacts. Platform defaults may constrain backward movement or automation.
6. **Migrate with reconciliation.** Map old states to new definitions, keep a recoverable export, preview affected records, and review exceptions. Do not force ambiguous historical data into a confident new label.

## Worked example

A fictional company defines an accepted inquiry as one reviewed by a responsible team and suitable for a next conversation. Downloading a report alone does not enter that state. A contact at an existing customer may request a new product evaluation without changing the account back to “lead.”

The new opportunity tracks the expansion process. Contact communication eligibility remains a separate property, so lifecycle status cannot override an unsubscribe request.

## Transition contract

| From/to | Object | Required evidence | Writer | Event time | Exception handling |
|---|---|---|---|---|---|
| Inquiry → accepted | | | | | |
| Accepted → opportunity | | | | | |
| Opportunity → won/lost | | | | | |

## Audit the result

Sample records from every transition and compare them with actual conversation or transaction evidence. Monitor unexpected reversals, missing timestamps, and competing updates. If teams disagree on what a state means, resolve the definition before adding more automation or dashboards.

## Sources and scope

- [HubSpot: lifecycle stages](https://knowledge.hubspot.com/records/use-lifecycle-stages?region=canada&ref=b2b-playbook) illustrates contact/company stage behavior in one CRM; design and test your own transition rules rather than assuming identical platform behavior.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[CRM data model](crm-data-model.md) · [Routing and SLA](routing-and-sla.md) · [Lifecycle email](../08-lifecycle-and-customer-marketing/lifecycle-email.md)

[Chapter guide](README.md) · [All playbooks](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
