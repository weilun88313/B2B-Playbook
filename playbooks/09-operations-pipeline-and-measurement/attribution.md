---
title: "Attribution"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

Attribution allocates credit among recorded interactions under a defined model. It answers how a system distributes observed credit. It does not, by itself, prove how much revenue would disappear if a channel were removed.

## State the measurement boundary

Define the outcome, entity, eligible touchpoints, lookback window, and identity rules. Decide how anonymous visits, offline conversations, multiple contacts, and missing data are represented. Preserve an unknown category instead of inventing a complete path.

## Build and compare models

1. **Clean the outcome ledger.** Deduplicate conversions or opportunities and use a consistent value basis. Separate created pipeline, won revenue, and collected cash.
2. **Specify touch eligibility.** Decide which interactions count and how repeated events are collapsed. A thousand page events should not automatically earn a thousand times the credit of a meaningful conversation.
3. **Apply transparent rules first.** First-touch assigns eligible credit to the earliest recorded touch; last-touch to the latest; a custom linear model divides it across eligible touches. These are analytical examples, not a claim that every platform currently offers each model.
4. **Reconcile totals.** Within one model and outcome ledger, allocated value plus explicitly unallocated value should equal the included outcome value. Do not add platform totals when several systems claim the same conversion.
5. **Compare sensitivity.** Change the model or lookback window and inspect which conclusions move. Keep data-driven platform models labeled with their scope and limitations.
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

## Sources and scope

- [Google Analytics: attribution](https://support.google.com/analytics/answer/10596866?ref=b2b-playbook) defines model-based credit allocation and current platform options; the three-touch arithmetic is a custom illustrative example.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Measurement model](measurement-model.md) · [Experimentation](experimentation.md) · [Pipeline model](pipeline-model.md)

[Chapter guide](README.md) · [All playbooks](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
