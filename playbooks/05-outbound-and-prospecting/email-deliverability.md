---
title: "Email deliverability"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12 · **Reading edit:** 2026-09-12

A customer says the promised email never arrived. Before rewriting the subject line, check how the message was sent, whether the address is valid, and what the receiving system reported. Reliable email starts with recognizable sending identity, an appropriate audience, and a way to act on failures.

## Establish the sending inventory

List every provider sending for your domain: product, billing, support, marketing, and prospecting. Identify the technical owner and business owner for each. A forgotten integration can damage the same domain reputation as an intentional campaign.

## Prepare and operate

1. **Authenticate each authorized stream.** Follow current provider requirements for SPF, DKIM, DMARC, alignment, transport, and DNS. Google distinguishes requirements for all senders and bulk senders to personal Gmail accounts; check the current scope instead of copying an old checklist.
2. **Validate recipient eligibility.** Keep provenance and suppression synchronized. Do not treat an address-verification result as permission or interest. Remove invalid addresses and investigate the source of repeated bad records.
3. **Make the message recognizable.** Use accurate sender identity and subject lines. Avoid fake reply prefixes or misleading urgency. Provide required unsubscribe mechanisms and process them throughout connected tools.
4. **Introduce volume deliberately.** Begin with recipients who expect the message and observe real feedback. Do not manufacture engagement or rotate domains to evade reputation problems. Growth in volume must be supported by audience quality and operational capacity.
5. **Monitor by stream and provider.** Review authentication failures, deferrals, hard bounces, complaints, and unsubscribe processing. Opens are unreliable as a standalone health measure because tracking can be blocked or automated.
6. **Define an incident response.** Pause the affected campaign when quality deteriorates, preserve diagnostic data, fix the cause, and resume cautiously. Keep transactional communications separately managed so a marketing incident does not casually disable essential notices.

## Worked example

A fictional team notices new bounce failures after changing its enrichment source. It pauses that source's prospecting cohort and checks provenance and role freshness. Authentication passes, so changing DNS would not address the observed cause.

A separate billing stream remains healthy. The owner preserves that service while correcting the prospecting import and propagating invalid-address suppressions. The team resumes only after a controlled review, rather than increasing volume to compensate for fewer deliveries.

## Sending control sheet

| Stream/provider | Domain owner | Authentication verified | Audience source | Suppression path | Incident owner |
|---|---|---|---|---|---|
| | | | | | |

## Verify before the next send

Inspect actual received message headers, test unsubscribe end to end, and confirm bounce events update the originating system. Delivery acceptance by a server does not prove inbox placement, reading, or business interest. Report those as separate stages.

## Try it with your own work

Choose one sending tool. Verify its domain authentication, send a test message, and follow an unsubscribe or invalid-address event back to the system that created the record.

## Sources and scope

- [Google: email sender guidelines](https://support.google.com/mail/answer/81126?ref=b2b-playbook) is the current primary reference for personal Gmail requirements. Other receiving providers have their own requirements.

The example is fictional; any numbers illustrate the method rather than a benchmark. Adapt the worksheet to your own situation.

## What to read next

[Contact data](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/contact-data) · [Reply handling](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting/reply-handling) · [Lifecycle email](https://b2-b-playbook.mintlify.app/playbooks/08-lifecycle-and-customer-marketing/lifecycle-email)

[Chapter guide](https://b2-b-playbook.mintlify.app/playbooks/05-outbound-and-prospecting) · [All playbooks](https://b2-b-playbook.mintlify.app/playbooks)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](https://b2-b-playbook.mintlify.app/copyright).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
