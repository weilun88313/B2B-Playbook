---
title: "Attribution"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

The ad platform credits a sale to an advertisement. The buyer says a colleague recommended you. Both can describe part of what happened. Attribution assigns credit to recorded interactions under a chosen rule; understanding that rule helps you use the report without asking it to explain the entire buying decision.

## State the measurement boundary

Define the outcome, entity, eligible touchpoints, lookback window, and identity rules. Decide how anonymous visits, offline conversations, multiple contacts, and missing data are represented. Preserve an unknown category instead of inventing a complete path.

## Build and compare models

1. **Check the records you are counting.** Deduplicate conversions or opportunities and use a consistent value basis. Separate created pipeline, won revenue, and collected cash.
2. **Decide which interactions count.** Decide which interactions count and how repeated events are collapsed. A thousand page events should not automatically earn a thousand times the credit of a meaningful conversation.
3. **Apply transparent rules first.** First-touch assigns eligible credit to the earliest recorded touch; last-touch to the latest; a custom linear model divides it across eligible touches. These are analytical examples, not a claim that every platform currently offers each model.
4. **Reconcile totals.** Within one model and outcome ledger, allocated value plus explicitly unallocated value should equal the included outcome value. Do not add platform totals when several systems claim the same conversion.
5. **See whether changing the rule changes your conclusion.** Change the model or lookback window and inspect which conclusions move. Keep data-driven platform models labeled with their scope and limitations.
6. **Use other evidence for budget decisions.** Combine recorded paths with buyer-reported discovery, qualitative context, and well-designed incrementality experiments where feasible.

## Worked example

A hypothetical &#36;12,000 won deal has three eligible recorded touches: a newsletter, a webinar, and a search ad. A simple custom linear allocation assigns &#36;4,000 to each; first-touch assigns &#36;12,000 to the newsletter; last-touch assigns &#36;12,000 to the ad.

The three reports describe the same deal. Adding them would falsely create &#36;36,000. If an untracked peer recommendation drove the buyer's interest, none of those click-based allocations reveals its contribution. Record the buyer's answer separately rather than rewriting observed history to manufacture agreement.

## Model specification

| Choice | Definition |
|---|---|
| Outcome ledger and amount basis | |
| Entity/identity and eligible touches | |
| Lookback and deduplication rules | |
| Credit allocation and unknown handling | |
| Reconciliation and sensitivity checks | |
| Decision use and causal limits | |

## Read the disagreement

Large differences between models can be useful evidence about the recorded journey and its gaps. Investigate them before choosing the model that flatters a preferred channel. Keep an explicit distinction between attributed, influenced, and experimentally estimated incremental outcomes.

## Try it with your own work

Take one won deal and compare its recorded touchpoints with the buyer’s account of how they found you. Note the gaps before deciding what the channel report means for your budget.

## Sources and scope

- [Google Analytics: attribution](https://support.google.com/analytics/answer/10596866?ref=b2b-playbook) defines model-based credit allocation and current platform options; the three-touch arithmetic is a custom illustrative example.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[Measurement model](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/measurement-model) · [Experimentation](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/experimentation) · [Pipeline model](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/pipeline-model)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
