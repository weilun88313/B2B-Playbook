---
title: "Conversion-rate optimization"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

People reach the form and leave. You suspect it is too long, but they may also be unsure what happens after submitting it. Improving conversion starts by investigating that uncertainty, making a specific change, and checking whether more suitable people can complete the task.

## Define the outcome

Choose a specific progression, such as eligible visitors completing a valid consultation request. Specify the population, counting rule, and observation window. Keep quality and experience guardrails beside the primary rate.

## Run an interpretable improvement

1. **Diagnose the friction.** Combine analytics with recordings or interviews collected under appropriate rules, support questions, and form-error data. A drop-off identifies where to investigate, not automatically why it happened.
2. **Explain why the change might help.** State the obstacle, proposed change, and expected behavior. For example: explaining response time may reduce uncertainty before submission.
3. **Choose the evaluation method.** Use a randomized experiment when traffic, tooling, and timing support it. With low volume, usability testing and staged observation can guide a change, but do not establish the same causal certainty.
4. **Agree how you will read the result before testing.** Set the randomization unit, primary metric, minimum effect worth detecting, sample/duration plan, and stopping rule with suitable statistical support. Account for multiple comparisons and delayed quality outcomes.
5. **Check implementation and data quality.** Test variants, event deduplication, exposure logging, and allocation. Investigate sample ratio mismatch before interpreting effects; it can indicate an invalid experiment.
6. **Make a bounded decision.** Review uncertainty and guardrails, not only the direction of the headline number. Record whether to ship, revert, investigate, or run a better-designed test.

## Worked example

A hypothetical demo form removes a required phone field. Submissions increase from 40 to 50 in two observed periods, but traffic composition also changes. The team cannot attribute the increase to the field change from this comparison alone.

It checks usability and downstream contactability, then designs a randomized test if volume permits. The primary outcome is a valid request per eligible visitor; accepted meetings and complaints are guardrails. This prevents a superficial conversion improvement from hiding a worse buying experience.

## Experiment brief

| Field | Definition |
|---|---|
| Friction evidence and hypothesis | |
| Population, unit, and variants | |
| Primary metric and denominator | |
| Quality/experience guardrails | |
| Sample, duration, and stopping plan | |
| Data checks and decision rule | |

## Keep the learning

Archive the implemented version, analysis, and limitations. A result from one audience and period may not generalize to another. Re-test when the underlying experience changes materially, rather than treating a winning button or layout as permanent law.

## Try it with your own work

Choose one point where readers struggle. Gather an example of the problem, write a possible explanation, and propose one change. Decide how you will check both completion and the quality of the result.

## Sources and scope

- [Microsoft Research: diagnosing sample ratio mismatch](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/?ref=b2b-playbook) supports the experiment-integrity check; this workflow and example are original.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[Experimentation](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/experimentation) · [Demo request](https://b2-b-playbook.mintlify.app/playbooks/07-website-and-conversion/demo-request) · [Dashboards](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/dashboards)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/07-website-and-conversion) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
