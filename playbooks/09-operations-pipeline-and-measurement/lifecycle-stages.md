---
title: "Lifecycle stages"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

Marketing calls someone qualified, sales calls them a new inquiry, and the CRM sends a customer email. Shared lifecycle stages help the teams and tools agree on what has happened. Start by defining the evidence behind each state and who is allowed to change it.

## Separate the objects

A person, account, and opportunity can be in different states at the same time. An existing customer can open a new expansion opportunity, and a new contact can belong to that customer account. Avoid overwriting one object with another object's meaning.

## Define and implement the state model

1. **Write each state's meaning.** Specify the object, entry evidence, owner, and allowed next actions. Use the fewest states that support distinct operational decisions.
2. **Explain what moves a record to the next stage.** Record the event, prerequisite, responsible system, timestamp, and behavior for missing evidence. Decide whether regression is allowed and how reactivation is represented.
3. **Preserve history.** Keep stage-change events or equivalent auditable history for cohort analysis. A current-stage field cannot reconstruct time spent in prior states by itself.
4. **Agree which tool or person can change the record.** Document which workflows, integrations, imports, and users may change each field. Set precedence so a stale import cannot silently undo a valid customer transition.
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

## Try it with your own work

Choose one stage that causes disagreement. Ask both teams what must have happened before a record enters it, then compare their answers with a few actual records.

## Sources and scope

- [HubSpot: lifecycle stages](https://knowledge.hubspot.com/records/use-lifecycle-stages?region=canada&ref=b2b-playbook) illustrates contact/company stage behavior in one CRM; design and test your own transition rules rather than assuming identical platform behavior.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[CRM data model](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/crm-data-model) · [Routing and SLA](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/routing-and-sla) · [Lifecycle email](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing/lifecycle-email)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
