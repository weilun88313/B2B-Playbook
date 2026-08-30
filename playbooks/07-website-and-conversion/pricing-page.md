---
title: "Pricing page"
sidebarTitle: "Pricing Page"
---

**Last reviewed:** 2026-08-30

[Pricing and packaging](../02-product-marketing/pricing-and-packaging.md) decides who pays, for what unit, and when you revisit the number. This page decides **what a serious buyer can understand in one scan of `/pricing`**: the unit, the plans, who each plan is for, and what happens next.

Hiding the number so sales can “control the conversation” is a tactic with a shortening half-life. Buyers who shop with a bottom-up or self-serve alternative will not sit through three meetings to learn the unit. High-ACV sales-assist still benefits from a published range, a value metric, and an honest enterprise path—not from a blank page that says “contact us” and nothing else.

This is not a packaging redesign, not a Van Westendorp survey, and not a CRO lab for button color.

## Use this when

- `/pricing` is a hero sentence and a “Talk to sales” button.
- Sales refuses to publish any number, and inbound asks “what does this cost?” on every first call.
- Four editions are on the page and the tenth customer does not exist yet.
- The value metric is obvious internally and invisible in the first five seconds.

## Do not use this when

- You have not decided the unit or the first offer. Stay in [pricing and packaging](../02-product-marketing/pricing-and-packaging.md).
- Public-procurement or regulated quoting forbids a public number. Write the constraint; this page is not legal advice.
- The work is a multi-product catalog redesign. Position [the way you sell](../02-product-marketing/positioning.md#step-8-position-the-way-you-sell) first.
- You want to A/B-test plan names before the metric is readable.

## Words you will use

| Word | Meaning here |
|---|---|
| **Value metric** | The unit the buyer already believes is “more value” (seat, active user, outcome)—stated in the summary, not in a footnote |
| **Plan** | A package a named seat can recognize themselves in. Three is the usual shape; five is the ceiling |
| **Enterprise path** | What is actually different (security, admin, contract)—not a black box that only means “more expensive” |
| **Add-on** | A capability used by a minority on a plan; stuffing it into the tier trains people they overpay |

## One rule

**Show the unit in five seconds.** If a stranger cannot say what they pay *for*, the rest of the page is decoration. Clever headlines, tabbed product families, and “most popular” on the most expensive tier do not fix an invisible metric.

## Operating method

### Step 1: put price in the main navigation and make the page transactional

`/pricing` is not a landing page. No newsletter pop-up. CTA above the fold. Restate who this is for in one line (positioning, not a new slogan). Clean structure over a revolutionary layout.

### Step 2: publish a number—or a bounded path to one

Default: **yes, show pricing.** For a sales-assist motion, a public starting price, a range, or “from $X / [unit]” plus what enterprise adds is still a number. A page that only says “contact us” teaches the buyer you are expensive *and* opaque.

If legal truly forbids a figure, show the metric, the plan jobs, and the questions sales will ask—so the call is not a blank.

### Step 3: three plans, a summary table, waterfall below

- Three plans is the usual; never more than five.
- Summary table: the few differences a buyer uses to self-qualify. Full feature list below the fold.
- Waterfall the features so value visibly rises with price—and the features are actually valuable.
- Suggest a plan with “recommended” or “best value” only if it is true. Do not tag the top tier “most popular” as a lie.
- Add-ons sit beside the table when a capability is used by a small share of a plan (Elena Verna’s operating heuristic: think hard below ~30% use). Do not hide them as fake checkmarks.

### Step 4: do not expect tabs to discover the second product

Multi-product tabs are a hub, not a discovery engine. Most people will not click the other tab. Drive the second product with [content strategy](../03-brand-story-and-content/content-strategy.md) links and sales motion—not with a tab bar. Salesforce-style box salad is what not to do if you need the page to decide.

### Step 5: measure unique visitors, then decide what to test

Feature-gated products often see repeat pricing visits before pay. Usage-gated products often convert on the visit that hits the limit. Track **unique visitors**, not raw pageviews, before you call conversion “low.” If you have not tested the page in a year, you are running a 100% holdout with no log. Tests still need a decision—see [experimentation](../09-operations-pipeline-and-measurement/experimentation.md). Do not A/B a strategy question (which metric, which motion) as a headline.

## Teaching fill (invented—not a customer)

Sales-assist. Seat-based. Enterprise is SSO, DPA, and a named CSM—not a mystery SKU.

| Field | Fill |
|---|---|
| Value metric | Per named operator seat / year—on the first row, not in a tooltip |
| Plans | Team / Business / Enterprise. Three. |
| Who each is for | Team = one queue owner. Business = several queues + reporting. Enterprise = security questionnaire + contract. |
| Public number | Team and Business list price. Enterprise: “from $X” + what is actually different. |
| Add-on | Advanced audit log—used by a minority; priced beside the table |
| CTA | Team: start. Business/Enterprise: scoped conversation, not “Get a demo.” |
| Will not do | Tabs for a second product that is not sold yet. “Most popular” on Enterprise. |

## Copy: pricing-page brief (fill)

- Value metric (one sentence a stranger can repeat):
- Plans (≤5) and who each is for:
- What is public vs “talk to us,” and why:
- Add-ons (and why they are not stuffed into a tier):
- Primary CTA above the fold:
- Multi-product: single lineup / tabs / separate URLs — and how the others get traffic:
- Unique-visitor conversion we will read (not raw views):
- Last test date / next test allowed to change:

Working file: [pricing-page.md](../../templates/pricing-page.md).

## Pre-flight checklist

- [ ] The commercial unit is already decided on [pricing and packaging](../02-product-marketing/pricing-and-packaging.md).
- [ ] Pricing is in the main nav.
- [ ] A stranger can name the unit in five seconds.
- [ ] ≤5 plans; summary above, full list below.
- [ ] Enterprise path names what is different.
- [ ] No pop-up. CTA above the fold.
- [ ] “Most popular” is true or absent.
- [ ] Self-serve metrics (if any) are unique-visitor based.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Unit recall | Five strangers can say what they pay *for* |
| Pricing in nav | The URL is findable without search |
| Unique-visitor conversion | Pricing → next step (checkout or qualified conversation), on uniques |
| Repeat-visit pattern | Feature-wall products: visits-before-pay. Usage-wall: visit ≈ decision |
| Sales “what does it cost?” | First-call time still spent explaining the unit (page failed) |

Elena Verna’s public PLG tape (signups who hit pricing ~25%; checkout-to-order ~50%; reverse-trial free-to-paid ~10–15%) is **her** self-serve sample. Use it as a **method prompt**, not as your target. High-ACV sales-assist should not import those percentages.

## Common mistakes

- Blank “contact us” as a strategy.
- Four editions for the tenth customer.
- Feature-stuffing so nobody feels they overpay—then they churn because they use one of ten.
- Tabs as the discovery plan for a second product.
- Testing copy before the metric is readable.
- Treating pageviews as conversion.

## What to read next

The high-intent form that should skip the leisurely score ladder is [demo request](demo-request.md). The scan that must still work if they never open `/pricing` is the [homepage](homepage.md). How you will read whether ads or content created this visit is [measurement model](../09-operations-pipeline-and-measurement/measurement-model.md). The commercial revisit calendar stays on [pricing and packaging](../02-product-marketing/pricing-and-packaging.md).

## Sources and evidence boundary

This is an owner-maintained operating synthesis.

- **Show the number; unit in five seconds; three-to-five plans; summary then waterfall; no pop-ups; add-ons when use is minority; tabs do not discover the second product; unique-visitor conversion; contextual in-product upsells.** Distilled from Elena Verna, “The DNA of a Great Pricing Page” (2024-10-11), which also points at Emily Kramer / [MKT1](https://newsletter.mkt1.co/p/pricing-pages?ref=b2b-playbook) as the checklist to follow. Teardowns of Figma, Slack, Miro, Zoom, HubSpot, and Salesforce in that essay are **their** grades on **those** pages on that date—not a command to copy a layout.
- Plan count, value metric, and “charge sooner / simpler first offer” stay owned by [pricing and packaging](../02-product-marketing/pricing-and-packaging.md).
- This page does not re-gate a Reforge course. PLG benchmarks stay labeled as someone else’s tape.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
