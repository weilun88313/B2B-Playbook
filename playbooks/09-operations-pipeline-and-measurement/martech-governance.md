---
title: "MarTech governance"
sidebarTitle: "Martech Governance"
---

# MarTech governance

**Last reviewed:** 2026-08-29

Buying a logo because a community scorecard ranked it is not governance. **Governance is: which job this tool is allowed to do, who owns it, what it may write into the [CRM](crm-data-model.md), and when you will remove it.** A newer SKU is not automatically the stack. [TOOLS.md](../../TOOLS.md) is a shortlist of products. This page is how you run a bake-off without importing someone else’s satisfaction scores.

## Use this when

- Sales wants a cadence tool, CS wants conversation intelligence, finance wants a forecast UI—and everyone thinks it is “one platform.”
- The last purchase cannot two-way sync with the CRM and nobody wrote that as a requirement.
- Implementation is “the vendor will configure it” with no owner and no exit test.
- You found a vendor grid with scores out of 10 and are about to paste it into a board deck.

## Do not use this when

- There is no motion and no CRM map. Stay in [channel strategy](../04-channels-and-distribution/channel-strategy.md) and [CRM data model](crm-data-model.md).
- You need software names for a job. Start in [TOOLS.md](../../TOOLS.md), then come back here to evaluate.
- Procurement, security, or privacy review must be done by qualified owners. This page will not sign a DPA.

## Words you will use

| Word | Meaning here |
|---|---|
| **Job** | One operating job (cadence, conversation intelligence, forecast UI)—not a vendor’s product family name |
| **Win reason** | Why a recent buyer said yes, in their words |
| **Opportunity area** | What still hurts after they bought |
| **Pricing model** | Per seat, platform + seat, implementation fee—not a screenshot of list price |
| **Time to implement** | Range from “usable” to “the team actually lives in it,” not the sales cycle |

## One rule

**Split the jobs before you split the vendors.** Cadence / engagement, conversation intelligence / coaching, and pipeline / forecast are often sold as one suite and fail as one suite. If two-way CRM sync is not in the contract of requirements, you will re-key forever.

## Operating method

### Step 1: write the jobs, not the category slogan

Complete: *we are buying a tool so that ____ can ____ every ____, writing ____ into the CRM.* If you cannot finish that sentence, you are shopping. [Outbound](../05-outbound-and-prospecting/multichannel-sequence.md) needs a sequence home. [Forecasting](forecasting.md) needs a source of truth—often the CRM, sometimes an overlay. Conversation intelligence is coaching and inspection, not a second forecast.

### Step 2: interview recent buyers—or refuse the score

A published grid of “overall satisfaction” is **their** interviews, **their** year, **their** segments. Use it only as a **prompt for questions**, never as your score. Ask: win reasons, what is still weak, who they also evaluated, pricing shape, implementation calendar, CRM (and whether sync is two-way). Write **your** answers in the working file.

### Step 3: put opportunity areas on the same page as wins

Recurring failure modes in this category of tools (from buyer-shaped grids, not as our benchmarks): CRM sync that is one-way or brittle; conversation intelligence that does not match the category leader the buyer compared; support that collapses across time zones or during implementation; forecast that cannot hold large, slow deals; pricing that only looks cheap per seat. Treat these as **test cases**, not as a ranking of named vendors.

### Step 4: capture commercial shape without stealing a median

Pricing model, discount logic (seats vs term), implementation as a line item, and a **range** for time-to-live-in-the-tool. Do not copy a community PDF’s median ACV into your model. Quote **your** seats and **your** legal. AI and usage pricing change the bill; treat software as a **portfolio with a kill date**, not a growing stack of seats. A vendor-spend benchmark landing page is a prompt for those questions—not your budget ([Stackpack 2026 spend report](https://www.stackpack.ai/2026-Vendor-Spend-Benchmarks-Report?ref=b2b-playbook) is gated; we did not import its tables).

### Step 5: decide, then assign an owner and a kill date

One owner. Fields it may write (from the [CRM map](crm-data-model.md)). A date you will review usage and sync errors. If the bake-off winner cannot do two-way sync on required fields, that is a no—not a “phase two.”

## Teaching fill (invented—not a customer)

Outbound-assist, ~12 sellers. CRM is the forecast source of truth. Not a vendor ranking.

| Job | Decision |
|---|---|
| Cadence | Need sequences + mailbox control. Conversation intelligence is a **separate** job this year. |
| Win reasons we will test | Customization of the cadence builder; CRM objects we already use; whether support answers in our hours. |
| Opportunity tests | Two-way opportunity sync; spam/reputation; CI quality if we bolt it on later. |
| Commercial | Per-seat + implementation. Multi-year discount only if we can exit fields. |
| Owner | RevOps. Review in 90 days against sync error rate and sequence completion—not seats provisioned. |

## Copy: evaluation one-pager (fill)

- Jobs in scope this buy (and jobs we will **not** bundle):
- Required CRM writes (objects/fields, two-way yes/no):
- Recent-buyer questions we will actually ask:
- Win reasons we will test:
- Opportunity areas we will test:
- Pricing model we will quote:
- Time-to-live-in-tool we will believe:
- Alternatives we must see in the same bake-off:
- Owner, review date, kill criteria:

Working file: [vendor-evaluation.xlsx](../../templates/vendor-evaluation.xlsx). Shortlist of products: [TOOLS.md](../../TOOLS.md).

## Pre-flight checklist

- [ ] Jobs are split; a suite is a choice, not a default.
- [ ] CRM map exists for every field the tool will touch.
- [ ] Two-way sync is a requirement or an explicit out-of-scope.
- [ ] Community scores were not pasted as our scores.
- [ ] Implementation has an owner and an exit test.
- [ ] Pricing model is written; a borrowed median ACV is not.
- [ ] Kill / review date exists.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Sync errors / stale CRM fields | Whether the record stays true |
| Time from purchase to team living in the tool | Implementation theater |
| Seats provisioned vs seats in the weekly job | Shelfware |
| Bake-off jobs covered vs SKUs bought | Suite sprawl |

Do not count vendor demos attended, or a 9.2/10 in a partner PDF, as governance.

## Common mistakes

- One SKU for cadence, CI, and forecast because the logo is famous.
- Skipping two-way CRM sync until after contract.
- Treating implementation time as the vendor’s optimistic week.
- Importing another researcher’s satisfaction scores as facts.
- No owner after the invoice.
- Expanding [TOOLS.md](../../TOOLS.md) with a Slack list of AI apps instead of a job.

## What to read next

The record the tools must obey is [CRM data model](crm-data-model.md). Sequences live in [multichannel sequence](../05-outbound-and-prospecting/multichannel-sequence.md). The call still lives in [forecasting](forecasting.md). Product names for a defined job start in [TOOLS.md](../../TOOLS.md)—start with the job table there, then the row. A community logo sheet or a marketplace-first skill pack is not the stack—pick the problem in [AI use-case selection](ai-use-case-selection.md) and the rung in [GTM AI maturity](gtm-ai-maturity.md) first.

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not a ranking, not a price guide, and not an endorsement of any vendor.

The evaluation shape (overall buyer sentiment as a prompt not a score, win reasons vs opportunity areas, products/use cases, pricing model, typical alternatives, time to implement, headquarters as context only) is distilled from a two-page vendor scorecard on sales engagement and revenue intelligence produced with a GTM community (buyer-interview grid). That file is a **method prompt**, not a source to copy. Its satisfaction scores, median ACVs, discount anecdotes, implementation ranges, and named vendor columns are **not** this library’s facts or a ranking. Vendor marks remain theirs.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
