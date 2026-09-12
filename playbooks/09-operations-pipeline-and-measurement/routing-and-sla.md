---
title: "Routing and SLA"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

A demo request arrives, but each team assumes someone else is handling it. Routing decides who owns the request; a service-level agreement, or SLA, says what they should do and by when. A useful setup also covers missing information, absences, and requests that do not fit the usual rules.

## Define what the clock measures

Separate receipt, assignment, acceptance, first meaningful response, and resolution. An automated acknowledgement is not necessarily a useful response. State whether the clock uses elapsed time or business hours, including timezone and holiday treatment.

## Build the rules

1. **Classify the request.** Distinguish buying inquiries, support issues, partner requests, customer expansion, and irrelevant submissions. Use the promise made at the entry point as context.
2. **Set rule precedence.** Define how account ownership, geography, segment, language, product expertise, and availability interact. Test overlaps instead of relying on the order someone happened to build workflows.
3. **Assign a fallback.** Every eligible request needs an owner or monitored exception queue. Missing territory data must not leave the record silently unassigned.
4. **Define acceptance and response.** Agree realistic deadlines, required context, reassignment reasons, and escalation. The receiving team should explicitly accept or return a request under a clear rule.
5. **Handle absence and failure.** Include vacations, capacity limits, integration outages, duplicates, and stale account owners. Ensure retries do not create competing owners or duplicate outreach.
6. **Review breaches by cause.** Distinguish data problems, rule defects, capacity gaps, and missed execution. Repair the systemic cause before escalating every case as individual underperformance.

## Worked example

A fictional demo request arrives outside the regional team's business hours and lacks a company country. The rule sends it to a monitored fallback queue. The response clock follows the published business-hours policy, while the system records the original receipt time separately.

The operator establishes the correct region and transfers ownership with context. The new owner accepts; the clock is not reset merely to hide the initial delay. The team later makes the relevant form field clearer if missing geography is a recurring problem.

## Routing contract

| Signal | Precedence rule | Owner/fallback | Clock | Required action | Escalation |
|---|---|---|---|---|---|
| Buying inquiry | | | | | |
| Customer request | | | | | |
| Exception | | | | | |

## Test before launch

Use synthetic records covering each branch and at least one overlap, missing value, unavailable owner, and duplicate. Check the receiving person's actual view, not just the workflow's success log. A record can be technically assigned yet practically invisible.

## Try it with your own work

Send a synthetic request with one important field missing. Check who sees it, who owns it, and when they are expected to act. Fix any point where it becomes unowned.

## Sources and scope

- [HubSpot: assign and rotate owners](https://knowledge.hubspot.com/workflows/assign-and-rotate-record-owners-using-workflows?ref=b2b-playbook) illustrates implementation options in one CRM. The ownership contract, clock, and exception policy must be defined for your operation.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[SDR handoff](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/sdr-handoff) · [CRM data model](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/crm-data-model) · [Dashboards](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/dashboards)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
