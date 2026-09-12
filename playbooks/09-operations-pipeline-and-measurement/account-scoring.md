---
title: "Account scoring"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

Account scoring prioritizes accounts for a defined action. It combines evidence about fit and readiness without pretending that a numerical score is a measured probability of purchase. The useful output is an explainable decision and its supporting signals.

## Choose the action first

Decide whether the score selects research, sales review, an account program, or customer expansion support. Different actions need different evidence. A universal score often hides these differences and becomes difficult to interpret.

## Build an explainable model

1. **Separate dimensions.** Keep structural fit, observed engagement, relationship coverage, and timing signals visible. A poor-fit account should not become ideal merely by generating many clicks.
2. **Define the evidence.** Record source, freshness, confidence, and entity matching. A signal attached to the wrong subsidiary can mislead the whole account view.
3. **Control aggregation.** Deduplicate events, cap repeated activity, and distinguish multiple relevant roles from repeated behavior by one person. Exclude known bots and irrelevant activity where identifiable.
4. **Handle unknowns explicitly.** Missing revenue or system data is not automatically poor fit. Use an unknown state and a research action where the uncertainty matters.
5. **Map bands to actions.** Specify who reviews each band and what they should do. Start with transparent rules and manual review before introducing more complex prediction.
6. **Validate against outcomes and capacity.** Backtest on time-appropriate data without using future information. Inspect false positives, missed accounts, segment bias, and workload. Recalibrate when the market, product, or data source changes.

## Worked example

A hypothetical model gives separate fit and readiness bands. An account has strong fit but no recent signal, so it enters a research queue. Another has heavy content activity but an unsupported deployment requirement, so it does not automatically enter a high-priority sales queue.

A third account has activity from operations and security plus a verified evaluation request. The operator sees those reasons and reviews it promptly. The model supports judgment instead of hiding the evidence behind “87 points.”

## Scoring specification

| Dimension | Evidence | Freshness/cap | Unknown treatment | Action |
|---|---|---|---|---|
| Fit | | | | |
| Engagement | | | | |
| Relationships | | | | |
| Timing | | | | |

## Review the queue

Sample both selected and unselected accounts. If the system overwhelms the team, adjust the action threshold or capacity rather than quietly ignoring records. Keep a versioned rule set so changes in outcomes can be distinguished from changes in scoring.

## Sources and scope

- [HubSpot: lead scoring tool](https://knowledge.hubspot.com/scoring/understand-the-lead-scoring-tool?ref=b2b-playbook) illustrates scoring records from actions and properties. The prioritization model here is original, not a required vendor formula.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Lead scoring](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/lead-scoring) · [ABM strategy](https://b2-b-playbook.mintlify.app/playbooks/06-account-field-and-partner/abm-strategy) · [Buying signals](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/buying-signals)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
