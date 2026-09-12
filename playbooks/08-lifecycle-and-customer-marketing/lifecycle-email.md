---
title: "Lifecycle email"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

A new customer finishes setup and then receives an email asking them to begin. The message was reasonable when scheduled, but their situation changed. Lifecycle email works from the customer’s current progress, with a useful next action and rules for stopping messages that no longer apply.

## Define the state before the message

Start with one transition, such as completing setup or recovering from an incomplete configuration. Separate essential service communications from promotional campaigns under applicable rules. A product account does not automatically justify every marketing message.

## Specify the automation

1. **Write entry conditions.** Define the event, required account/user state, eligibility, and observation delay. Account-level progress and individual user progress may differ.
2. **Decide when the message should stop.** Stop when the task is complete, the account changes state, permission is withdrawn where relevant, or a support situation makes the message inappropriate.
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

## Try it with your own work

Choose one automated email. Write what must be true when it is sent and what should cancel it. Test the case where the customer completes the task just before delivery.

## Sources and scope

- [Intercom: Series FAQs](https://www.intercom.com/help/en/articles/8780861-series-faqs?ref=b2b-playbook) illustrates platform-specific entry, exit, and re-entry behavior. Verify equivalent semantics in your own tool.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[Onboarding communication](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing/onboarding-communication) · [Email deliverability](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/email-deliverability) · [Lifecycle stages](https://b2-b-playbook.mintlify.app/playbooks/09-operations-pipeline-and-measurement/lifecycle-stages)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
