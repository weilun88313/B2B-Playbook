---
title: "Lifecycle email"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

Lifecycle email connects a customer's current state with a useful next action. The trigger should reflect a real event or unmet need, and the message should stop being eligible when that need disappears.

## Define the state before the message

Start with one transition, such as completing setup or recovering from an incomplete configuration. Separate essential service communications from promotional campaigns under applicable rules. A product account does not automatically justify every marketing message.

## Specify the automation

1. **Write entry conditions.** Define the event, required account/user state, eligibility, and observation delay. Account-level progress and individual user progress may differ.
2. **Define exit and suppression first.** Stop when the task is complete, the account changes state, permission is withdrawn where relevant, or a support situation makes the message inappropriate.
3. **Choose the useful action.** Give one clear instruction, explain why it matters now, and link directly to the relevant task. Avoid a generic product tour when only one setup step is missing.
4. **Coordinate frequency and priority.** Check overlapping onboarding, renewal, promotional, and service streams. A global contact policy should resolve collisions and respect essential notices.
5. **Test timing and re-entry.** Simulate late events, duplicate events, completed tasks, replies, and multiple users in one account. Confirm that a delayed message is rechecked before sending.
6. **Measure task completion.** Compare eligible cohorts and downstream outcomes. Opens and clicks can diagnose message behavior, but the task is the primary reason to send.

## Worked example

A fictional reporting product detects an account with a connected data source but no completed first report. After a defined delay, the responsible user receives a short guide to building the first report.

If a teammate completes the account's report before delivery, the message is suppressed. If the connection has failed, the user receives the appropriate troubleshooting route instead. The workflow does not keep sending setup reminders merely because the original event remains in a queue.

## Automation specification

| Rule | Definition |
|---|---|
| Entry event/state and delay | |
| Intended user and account relationship | |
| Exit, suppression, and priority | |
| Message promise and task destination | |
| Re-entry and duplicate handling | |
| Completion metric and owner | |

## Review the experience

Read the complete set of messages received by a test account over time. Individually reasonable emails can form an unreasonable sequence. Use support feedback and actual task progression to remove unnecessary sends, especially after the product experience itself improves.

## Sources and scope

- [Intercom: Series FAQs](https://www.intercom.com/help/en/articles/8780861-series-faqs?ref=b2b-playbook) illustrates platform-specific entry, exit, and re-entry behavior. Verify equivalent semantics in your own tool.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Onboarding communication](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing/onboarding-communication) · [Email deliverability](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/email-deliverability) · [Lifecycle stages](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/lifecycle-stages)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
