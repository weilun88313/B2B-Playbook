# Customer onboarding

**Last reviewed:** 2026-08-29

Onboarding is **education**: the customer understands how the product resolves the issue they bought it for. Implementation is **tactical integration**: the software sits in *their* stack, with their data, their permissions, their go-live. Mixing the two is how teams staff CSMs as project managers, skip training, and call a login “adopted.”

Retention starts on day one of implementation, not at the renewal conversation. A bad implementation paints the account red before CS ever “owns” it. Recovering is possible; pretending the kickoff was fine is not.

This page sits after [customer success](customer-success.md) has named who owns the book. It is not [SDR onboarding](../05-outbound-and-prospecting/sdr-onboarding.md) (employees) and not in-app UX design.

## Use this when

- Deals close and customers stall in “we’ll get to the technical bit.”
- CSMs are running implementations they are not good at.
- Sales promised a date nobody scoped.
- You cannot say whether you are measuring time-to-launch or time-to-value.

## Do not use this when

- There is no signed customer. Stay in [first ten](../01-strategy-and-buyers/first-ten-customers.md).
- The product is truly self-serve and the only job is an email series. That is lifecycle communication (still planned in this domain)—do not invent a professional-services factory.
- You need the ongoing CS operating system. That is [customer success](customer-success.md).

## One rule

**It is not a methodology if it is not written down.** Repeatability → standardization → quality. Workshop it with the people who run the work. Identify milestones and a playbook for when a milestone is missed. A named methodology is also a sales tool: it is what you can point to when the buyer asks “what happens after we sign?”

## Operating method

### Step 1: split education from integration on the journey map

From the customer’s side, not yours: acquire → handoff → kickoff → design → build → test → launch → adopt → expand → renew.

Mark which steps are **human**, which can be **product**, and where you go blind. Onboarding (how it solves their pain, training, trainer-the-trainer, in-app teaching) is not the same row as implementation (data in, config, UAT, go-live).

If the motion is PLG, most of this map collapses. If the motion is sales-assist enterprise, almost none of it does. [Channel strategy](../04-channels-and-distribution/channel-strategy.md) decides which map you are on.

### Step 2: win the handoff before you staff the project

Always try for a live conversation. The CRM must already hold what the AE knew. The agenda focuses on what the **CRM does not** hold:

- Who is an advocate? Who is a detractor?
- What did they hear as the promise?
- What business problem are we solving, and which outcomes will we track?
- How will we know they will want to renew?

Codify the success metric in that meeting. A sample checklist is a memory aid; it is not a substitute for the conversation.

### Step 3: kick off like a project you intend to finish

Kickoffs are critical:

- Agenda; goal; success metrics confirmed
- Walk the **order form**—every line. That is also the first honest expansion conversation.
- Introduce the **whole** team and what you need from the customer. Introduce **support at the beginning**, not at go-live.
- After implementation, survey with **CSAT** (was this project good), not NPS (would you recommend the company). If they were unhappy in implementation, the account is red **now**.

Decide, in writing: self-serve vs assisted; standard vs custom; how much is repeatable; whether data ingest and configuration are allowed to be split (usually they should not be); whether CSMs should run it (often they should not).

### Step 4: treat controllable failure as the default risk

A large share of implementation failure is process, not destiny. Write the save path before you need it:

- Weekly **status** (a written report can beat a meeting)
- Buyer on the distribution list, not only the project manager
- Bilateral escalation path named in the kickoff
- Jump early; remediation plan with weekly updates

“Can we recover?” is a yes with a dated plan, or a no you are willing to say.

### Step 5: measure launch and value as different clocks

| Clock | Means | Do not confuse with |
|---|---|---|
| **TTL** (time to launch) | They can use the thing in production | A calendar you promised in the pitch |
| **TTV** (time to value) | The outcome they bought showed up | Logins |
| **Users activated** | They can do the job | Seat count |
| **People trained** | They know how | Attendance on a webinar |
| **Project duration** | Actual vs forecast | Optimism |

What gets measured gets staffed. If you only measure TTL, you will ship empty.

### Step 6: capacity before heroics

How you assign: round-robin, segment, territory, or tech-touch. How long implementation/onboarding *should* take: start from the journey, use your data, break tasks in the written methodology. Revisit the capacity plan when you add segments; update as TTL moves.

Early-stage orgs often park implementation next to CS and support under one lead. Later they split CS, implementation, enablement, support. Do not copy a late-stage org chart onto four people.

### Step 7: charging is a packaging decision, not a vibe

Free implementation trains sales to give away the project and trains customers to treat your time as infinite. Paid implementation (especially packaged, not bespoke) can recoup cost-to-serve and force a real scope. Sales will complain unless they are **incented** to sell it—see [sales compensation](../09-operations-pipeline-and-measurement/sales-compensation.md).

Steer to packaged offerings. Customization is where fixed-fee projects die. Premium support and managed services are different SKUs; do not mix them into “onboarding” so NRR becomes mush.

Where the cost sits (CAC vs COGS / above vs below the line) is a finance call. Write it once with finance; do not let every deal invent it.

## Teaching fill (invented—not a customer)

Sales-assist B2B. Implementation is a two-person specialist lane. CSMs take the account at “first value,” not at contract signature.

| Field | Fill |
|---|---|
| Split | Implementation owns data + config + UAT. CS owns training design, trainer-the-trainer, adoption. |
| Handoff | 30-minute live; success metric written; advocate/detractor named. |
| Kickoff | Order form line by line; support alias in the room; CSAT survey date on the calendar. |
| Clocks | TTL target from historical median, not from the AE’s slide. TTV = the metric in the handoff. |
| Save path | Written status Fridays; buyer cc’d; escalation named as VP customer + VP sales. |
| Package | One standard implementation SKU sales can sell; custom is a change order. |
| Capacity | One new project per specialist per two weeks until TTL data says otherwise. |

## Copy: onboarding design (fill)

- Education vs implementation: who owns which journey steps:
- Handoff required fields + live agenda:
- Kickoff: order-form review · team intro · support intro · CSAT date:
- Standard vs custom · self-serve vs assisted:
- TTL vs TTV definitions:
- Milestone-missed playbook:
- Assignment model and capacity math:
- Paid vs free implementation (and how sales is paid on it):
- Where the cost sits (finance owner):

## Pre-flight checklist

- [ ] Education and integration are not the same workstream with the same owner by accident.
- [ ] Handoff is live plus CRM, with a success metric.
- [ ] Kickoff walks the order form and introduces support.
- [ ] Post-implementation CSAT exists; unhappy ⇒ account red.
- [ ] TTL and TTV are both defined.
- [ ] Methodology is written; missed-milestone play exists.
- [ ] Capacity is a number, not “we’ll stretch.”

## Metrics

| Metric | Diagnostic use |
|---|---|
| TTL actual vs forecast | Scoping honesty |
| TTV vs TTL | Shipped empty vs used |
| Implementation CSAT | Whether kickoff quality is real |
| Red accounts originating in implementation | Retention started on day one |
| Change-order rate on “fixed fee” | Packaging vs customization leak |

Do not count LMS enrollments, kickoff decks, or a named methodology with no document as success.

## Common mistakes

- Calling a login “onboarded.”
- CSMs as default implementers.
- Support appearing at go-live.
- Measuring only time-to-launch.
- Unwritten “methodology.”
- Giving implementation away, then wondering why scope exploded.
- Copying a 12-step platinum package onto a PLG product.

## What to read next

The ongoing book is [customer success](customer-success.md). What they receive in writing is [onboarding communication](onboarding-communication.md). The promise they bought is [positioning](../02-product-marketing/positioning.md) and [pricing](../02-product-marketing/pricing-and-packaging.md). Whether implementation revenue is in the number is [forecasting](../09-operations-pipeline-and-measurement/forecasting.md). Named-account context is [account planning](../06-account-field-and-partner/account-planning.md).

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not professional-services pricing advice, not PMI certification, and not legal advice.

The education-versus-implementation split, journey-map breakpoints, handoff conversation contents, kickoff discipline (order form, support early, CSAT not NPS after the project), controllable-failure save path, TTL vs TTV, written methodology, capacity planning, and “charge vs free” packaging logic are distilled from an operator class deck on deep-dive onboarding (undated presentation; class labeled #3). That deck cites public and book pointers (including a Baton article on implementation vs customer onboarding, Donna Webber’s *Onboarding Matters*, Jeff Kushmerek / Infinite Renewals, Alli Temple Tiscornia). Those are **named pointers**, not pages this repository abridges. Statistics quoted in the class (avoidable-churn dollar figures, PMI failure mixes, survey “willing to pay for experience” claims) are **not** adopted as this library’s facts. Sample packaged price points in that deck are teaching theater, not a price book.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
