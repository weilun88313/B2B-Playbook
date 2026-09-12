---
title: "Reply handling"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

A reply changes the state of a conversation. The system should stop treating the recipient as an untouched sequence record and let a responsible person interpret what was actually said.

## Define the response states

Separate interest, a question, a referral, a timing request, a clear refusal, an unsubscribe request, an automated absence notice, and a delivery failure. These states require different actions; a positive-sounding word is not enough to classify a message.

## Build the handling routine

1. **Pause automation on a human reply.** Prevent the next scheduled follow-up from contradicting the conversation. Automated absence notices need their own handling and should not count as engagement.
2. **Read for meaning and scope.** “Not now” may permit a specific later check-in if agreed; “remove me” requires suppression. Do not turn an ambiguous refusal into assumed future permission.
3. **Answer the actual question.** If someone asks for pricing or a technical limitation, provide the relevant answer or a clear owner and response time. Do not force a meeting before answering every basic question.
4. **Route with context.** Preserve the message, the campaign promise, relevant account facts, and any commitment made. Apply privacy and access rules to the record.
5. **Confirm the next action.** Use a concrete proposal when there is interest: a suitable time, a document, or a short clarification. A referral should be checked for relevance and eligibility before a new outreach begins.
6. **Audit edge cases.** Review sarcasm, forwarded replies, multilingual requests, shared inboxes, and conflicting records. Let uncertain automated classifications enter human review rather than trigger irreversible actions.

## Worked example

A fictional prospect replies, “Interesting, but we are changing systems in November. Send the migration requirements.” The operator pauses the sequence, sends the requirements, and asks whether a November check-in would be useful.

The contact is not marked as a booked opportunity. If they agree to a date, the owner records that commitment. If they instead ask to stop, suppression takes precedence over the earlier expression of interest.

## Reply decision table

| Meaning | Immediate action | Record |
|---|---|---|
| Wants an answer | Reply or assign an informed owner | Question and commitment |
| Agrees to a next step | Arrange the specific step | Owner and date |
| Requests removal | Suppress through connected sending tools | Scope and processing status |
| Automated absence | Apply absence policy | Return date if reliable |
| Ambiguous | Human review | Original text and uncertainty |

## Review quality

Measure response time, accurate suppression, fulfilled commitments, and accepted next steps. Sample classifications instead of optimizing a single “positive reply rate.” A fast but wrong reply can be worse than a slower, informed answer.

## Sources and scope

- [ICO direct marketing guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/?ref=b2b-playbook) is a UK-specific reference. Applicable requirements depend on jurisdiction, recipient, channel, and purpose; validate the intended operation before sending.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[Cold email](cold-email.md) · [SDR handoff](sdr-handoff.md) · [Routing and SLA](../09-operations-pipeline-and-measurement/routing-and-sla.md)

[Chapter guide](README.md) · [All playbooks](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
