---
title: "Dashboards"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

A dashboard should help a named person make a recurring decision. Begin with that decision and the action it can trigger, then select the smallest set of reliable measures needed to support it.

## Choose the operating question

Examples include which requests need ownership today, which campaign cohort needs investigation this week, or whether next quarter's pipeline assumptions remain plausible. A single view rarely serves all three audiences well.

## Build the decision view

1. **Name the owner and cadence.** State who uses the dashboard, when, and what they can change. If no action follows, the information may belong in a reference report instead.
2. **Define each metric.** Record numerator, denominator, unit, population, time window, source, refresh schedule, and exclusions. Distinguish zero from missing or delayed data.
3. **Separate outcomes and diagnostics.** Show the business result with a few measures that help explain it. Avoid treating every activity counter as an equal success metric.
4. **Provide context.** Include comparison periods, cohort maturity, targets or ranges with their basis, and annotations for material changes. A red indicator without a defensible threshold creates noise.
5. **Make records inspectable.** Allow an authorized user to reach the underlying cases while respecting access rules. Aggregates should reconcile to the source and use consistent definitions across teams.
6. **Close the action loop.** Record the decision, owner, deadline, and follow-up outcome in the operating meeting. Retire measures that repeatedly fail to inform decisions.

## Worked example

A fictional daily routing dashboard shows eligible requests awaiting acceptance, their age under the agreed clock, and the responsible queue. It distinguishes five overdue requests from three requests whose region is still unknown.

The operator fixes ownership and escalates the missing-data pattern. The weekly campaign dashboard uses mature inquiry cohorts and qualification outcomes instead. Combining both into a single “marketing score” would hide the different actions each requires.

## Metric contract

| Field | Definition |
|---|---|
| Decision and accountable user | |
| Metric/unit and exact calculation | |
| Population, window, and exclusions | |
| Source, freshness, and missing-data behavior | |
| Comparison or threshold basis | |
| Drill-down and expected action | |

## Check trust before design polish

Manually reconcile a sample period, test filters, and inspect timezone boundaries. Confirm that exports preserve definitions and that stale data is visible. Attractive charts cannot compensate for inconsistent stages or double-counted pipeline. When a metric changes definition, annotate the break rather than displaying an uninterrupted trend.

## Sources and scope

- [HubSpot: manage dashboards](https://knowledge.hubspot.com/dashboards/manage-your-dashboards?ref=b2b-playbook) provides one platform implementation reference. The decision and metric contracts here are original guidance.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Routing and SLA](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/routing-and-sla) · [Funnel model](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/funnel-model) · [Sales operating cadence](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/sales-operating-cadence)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
