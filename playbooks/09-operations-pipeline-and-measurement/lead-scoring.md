# Lead scoring

**Last reviewed:** 2026-08-29

Lead scoring is a **routing hypothesis**: which known people deserve a different action this week. It is not a personality, not a HubSpot feature tour, and not a substitute for an [ICP](../01-strategy-and-buyers/icp.md). If you cannot say what happens at the threshold—who is notified, what they must do, by when—you do not have scoring. You have a vanity integer.

This page sits in operations because the score must be a shared definition. Marketing cannot invent “MQL” while sales invents “ready.” [Channel strategy](../04-channels-and-distribution/channel-strategy.md) still decides whether a human should touch the lead at all.

## Use this when

- Inbound volume is large enough that “work everything” is how good leads die.
- Sales says marketing sends junk; marketing says sales never follows up; nobody wrote the threshold.
- Every page view adds a point and employees keep becoming “hot.”
- You are about to turn scoring on retroactively in a MAP without a change-control note.

## Do not use this when

- You do not yet have an ICP or a disqualifier. You will score the wrong market precisely.
- Volume is a handful of inbound names a week. A human queue beats a model.
- You need account-level orchestration. Person scores are not an account program. Account scoring is still planned in this domain—do not fake it with a contact integer.
- Legal or consent rules forbid the events you want to count. This page is not privacy advice.

## Words you will use

| Word | Meaning here |
|---|---|
| **Fit** | Firmographic / role evidence they belong in the ICP |
| **Intent** | Behavior that suggests they are in a buying job *now* |
| **Negative** | Evidence they are not a buyer (jobs, students, customers already, competitors) |
| **Threshold** | The score (or rule) that changes **action**, not a feeling |
| **MQL** | Marketing believes this person deserves sales time—only if the action is written |
| **SQL** | Sales has accepted the person as worth a working motion. Often a **human** set, not more points |

## One rule

**Do not pay out points for every small action.** Opens, social clicks, and uncritical page views will manufacture MQLs. Use **intervals** (every *n* events) and **high-value URLs** (pricing, demo) instead of “+1 per breath.” Use **negative scoring** for people you must not chase.

## Operating method

### Step 1: write the action, then the math

Complete this sentence: *at score ≥ ____ (or rule ____), ____ is notified, must ____, within ____.* If SQL is a Salesforce checkbox a human ticks, say so. Connecting lifecycle stage to a MAP score without a human is a choice—write it. Changing a live model **re-scores the whole database**. Small tweaks only; radical rewrites need a migration note.

### Step 2: split fit from intent

Fit without intent is a good logo browsing. Intent without fit is a student on the pricing page. Score both, or you will route the wrong people. Hand-raisers (demo, pricing, contact) should **skip the leisurely ladder** and notify whoever owns speed-to-lead. That is a workflow, not a polite +3.

### Step 3: map content and forms to buying stage—not to “more fields”

Awareness forms should be short enough that a stranger will complete them. Consideration can ask role and size. Decision can ask the questions that make the **meeting** useful. Progressive profiling: if you already have the field, ask the next one—not the same form twice. Reuse forms; segment with **lists** off page + form, not a new form per PDF.

Do not copy another company’s industry dropdown or “50 employees or we disqualify” as your ICP. That is their wedge.

### Step 4: write negatives and exceptions

Employees, job seekers, known customers, agencies you do not sell, competitors: either large negatives or a persona that routes elsewhere (HR, CS, partnerships). Customers often need a **different** motion, not a fake MQL. Decide whether customers get a high score for identification or a block from the hunter queue.

### Step 5: review with closed-won, then freeze

Seed points from **your** past leads, not a vendor blog. After go-live, review MQLs that sales rejected and SQLs that never closed. Adjust intervals before you adjust philosophy. The ledger is the artifact; the MAP is the implementation.

## Teaching fill (invented—not a customer)

B2B workflow product. Sales-assist inbound. HubSpot is the MAP; SQL is accepted in the CRM by an SDR.

| Field | Fill |
|---|---|
| Action | Score ≥ 40 + fit = ICP → SDR task, 4 business hours. Demo form → same task immediately, ignore the leisurely threshold. |
| Fit | Target industries, 50–2,000 employees, role in ops or IT. Below 50 employees: nurture, not SDR. |
| Intent | Demo / pricing highest. Decision content next. Blog in intervals (every 3 posts). No points per email open; clicks in intervals. |
| Negative | Careers, student emails, own employees. Customers: blocked from hunter queue; CS owns them. |
| SQL | Human accept in CRM. Not a second point gate. |
| Change control | Point changes logged; no silent rewrite after week two. |

## Copy: scoring ledger (fill)

- Action at threshold (who, what, SLA):
- Fit attributes and disqualifiers:
- Intent events (high-value URLs and forms vs interval behaviors):
- Negatives and customer/employee handling:
- MQL definition vs SQL definition:
- Form fields by awareness / consideration / decision:
- Progressive-profiling rule:
- Review cadence and what would trigger a migration:

Working file: [lead-scoring-ledger.xlsx](../../templates/lead-scoring-ledger.xlsx).

## Pre-flight checklist

- [ ] ICP and disqualifiers exist in writing.
- [ ] Threshold changes a **task**, not a dashboard color.
- [ ] Fit and intent are both represented.
- [ ] Hand-raisers bypass the slow ladder.
- [ ] Negatives exist; careers are not “engaged.”
- [ ] SQL ownership is named (human vs automatic).
- [ ] Forms match stage; progressive profiling is on.
- [ ] A change log exists before go-live.

## Metrics

| Metric | Diagnostic use |
|---|---|
| SDR accept rate of scored MQLs | Whether the threshold is a hypothesis or a leak |
| Time-to-first-touch on hand-raisers | Whether the skip-ahead workflow is real |
| % of MQLs that are employees/jobs | Negative scoring failure |
| Score distribution vs closed-won | Whether points predict anything |

Do not count “model turned on” or resemblance to a HubSpot sample guide as success.

## Common mistakes

- Points for every open, visit, and like.
- MQL = SQL = more points.
- Radical rescoring with no note, then wondering where the pipeline went.
- Copying another company’s form fields and employee-count floor.
- Scoring customers into the hunter queue.
- Launching without an SLA.

## What to read next

Who may be touched at all is [ICP](../01-strategy-and-buyers/icp.md). What the first meeting must teach is the [pitch](../02-product-marketing/sales-enablement.md). If humans work the queue, they need [SDR onboarding](../05-outbound-and-prospecting/sdr-onboarding.md). Whether marketing can **create** the volume behind the scores is [GTM planning](gtm-planning.md). Routing SLAs (still planned in this domain) are the sister of this page—until that file exists, write the SLA in the ledger.

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not a HubSpot implementation guide, not GDPR advice, and not a benchmark point table.

The split of fit vs behavior, negative scoring, high-value pages, interval scoring for cheap actions, explicit MQL vs SQL, caution against live radical changes, stage-based forms, progressive profiling, lists off reused forms, and workflow-at-threshold are distilled from an operator sample lead-scoring guide (Google Doc; HubSpot-shaped; company placeholders). That file is a **method prompt**, not a source to copy. Its example point values, industry lists, employee-count floors, and product-specific form fields are not this library’s facts.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
