# Measurement model

**Last reviewed:** 2026-08-30

A dashboard that assigns every dollar of pipeline to a UTM is not a measurement model. It is a story the pixel can tell. This page decides **which decisions each metric is allowed to support**—and which questions require a human, an experiment, or a longer clock.

[Channel strategy](../04-channels-and-distribution/channel-strategy.md) splits motions. [Paid media](../04-channels-and-distribution/paid-media.md) splits creation from capture. [Experimentation](experimentation.md) kills a belief. Measurement is the **scoreboard architecture** those pages share. Attribution as a multi-touch math product remains planned; do not wait for it. You can run this page with a form field and two reviews.

This is not a BI tool bake-off, not legal privacy counsel, and not a promise that hybrid data proves causality.

## Use this when

- Last-click ROAS is how brand, podcast, and founder posts get defunded.
- Marketing and sales each have a “source” field and they disagree on every deal.
- Leadership wants “full-funnel attribution” before anyone asked buyers how they heard.
- Capture campaigns look like heroes and creation looks like waste.

## Do not use this when

- Lifecycle words are undefined. You will measure noise. Write shared stages first (still planned) or at least the [lead-scoring](lead-scoring.md) actions.
- You need a test design. That is [experimentation](experimentation.md).
- You need next year’s capacity math. That is [GTM planning](gtm-planning.md).
- The request is to implement a vendor’s multi-touch model as the source of truth.

## Words you will use

| Word | Meaning here |
|---|---|
| **Creation scoreboard** | Memory and future cash flow: reach, evenness, HDYHAU, sales mentions—on a long clock |
| **Capture scoreboard** | In-market response: qualified conversations, sales-accepted pipeline, close—on a short clock |
| **Software attribution** | What cookies, UTMs, and CRM source fields can see |
| **Self-reported (SRA)** | What the buyer says, in their words, when asked |
| **Hybrid** | Read both. Do not average them into one fake ROAS |

## One rule

**Software measures capture paths; humans measure creation paths; neither alone is the budget.** If you only have UTMs, you will over-fund search and retargeting. If you only have stories, you will fund vibes. Ask on the high-intent form, keep the UTM, and refuse to pick a winner with one column.

## Operating method

### Step 1: freeze two scoreboards before you buy another dashboard

Write which weekly review reads **capture** (qualified conversations, accept rate, capture CAC you actually believe) and which quarterly review reads **creation** (category reach/evenness if you pay for it, HDYHAU mix, branded search, sales “I have been seeing you”). The [CMO Scorecard](https://business.linkedin.com/advertise/resources/b2b-institute/cmo-scorecard?ref=b2b-playbook) is the public version of “creative and media inputs, long-horizon outcomes.” You do not need their product to refuse a 14-day CPL on a memory campaign.

Kellblog-style board metrics (pipeline coverage, CAC payback, NRR) stay **company** numbers. Do not let a channel dashboard impersonate them.

### Step 2: put open-text HDYHAU on declared-intent forms

On [demo request](../07-website-and-conversion/demo-request.md) and other hand-raises: mandatory **free text**, no dropdown, no “Google / LinkedIn / Event” hints. Categorize after—string-match or a human pass. Prompting the list biases the study.

Do not put HDYHAU on every content gate. You will train “idk” and you will think you measured demand.

### Step 3: keep software fields honest and narrow

UTMs: first meaningful marketing touch **and** the session that converted—both stored, neither holy. Source = the offer or destination when that is more predictive than the referring hostname (a Refine Labs ops note, not a law). Sales may overwrite with a human source only through a written rule; silent edits are how two truths appear.

Last-touch and first-touch are **diagnostics**. They are not the budget.

### Step 4: read the mismatch; do not reconcile it into one number

Hybrid means: *software says X, buyers say Y, here is what we will fund anyway.* Refine Labs’ public study (620 declared-intent conversions, twelve months, software vs SRA) reported a large gap on dark social—podcast was a majority of *their* self-reported revenue and ~0% of *their* software credit. That is **their** tape. Your mix will differ. The method is the mismatch review, not their 90%.

### Step 5: send strategy questions to experiments, not to attribution

“Does this channel work?” on a small, new buy is [experimentation](experimentation.md): hypothesis, kill date, decision. Multi-touch models will not save a campaign that never defined the job. Incrementality tests and holdouts beat another attribution schema when the spend is large enough to justify them.

## Teaching fill (invented—not a customer)

Sales-assist. Founder posts. Light search capture. No podcast yet.

| Field | Fill |
|---|---|
| Capture review | Weekly: sales-accepted from search + demo form. Owner: demand lead. |
| Creation review | Quarterly: HDYHAU categories + founder-mention rate in first meetings. Owner: founder + marketing. |
| SRA surface | Demo form only, open text |
| Software we keep | First UTM, last UTM, campaign on the converting session |
| We will not do | One ROAS to rank founder posts vs branded search |
| Mismatch we expect | Direct / unknown in CRM; “your LinkedIn” / “a colleague” in HDYHAU |

## Copy: measurement card (fill)

- Capture metrics, owner, cadence:
- Creation metrics, owner, cadence:
- HDYHAU: which forms, open text (yes/no), who categorizes:
- Software fields we will trust—and only for what:
- Board metrics we will not let a channel dashboard impersonate:
- Disagreement rule (what we fund when SRA and software fight):
- What we will test instead of attributing:

Working file: [measurement-model.md](../../templates/measurement-model.md).

## Pre-flight checklist

- [ ] Two scoreboards are written; one weekly meeting does not mix them without a label.
- [ ] HDYHAU is open text on declared intent.
- [ ] UTM/source rules are written; sales edits are governed.
- [ ] Creation campaigns are excluded from 14-day CPL kill decisions.
- [ ] A mismatch review exists (even a spreadsheet).
- [ ] Privacy/consent owner knows what you store. This page is not that review.
- [ ] No vendor model is the single source of truth.

## Metrics

The model *is* a metric policy. Use this table as the refuse list:

| Allowed as a decision | Not allowed as the decision |
|---|---|
| Capture: qualified conversations, accept, win rate on captured demand | Platform ROAS on a creation campaign |
| Creation: HDYHAU mix, evenness, branded search, sales mentions | Last-click pipeline % as “marketing did this” |
| Hybrid mismatch notes | A blended “influenced” number nobody can audit |
| Experiment result with a kill date | Another attribution schema when the job was undefined |

## Common mistakes

- Buying HockeyStack / Dreamdata / a CDP to postpone asking buyers.
- Dropdown HDYHAU.
- One source field to rule them all.
- Firing the podcast because Salesforce said Organic.
- Treating Refine Labs’ 90% as your KPI.
- Asking attribution to answer a strategy question.

## What to read next

The form that collects SRA is [demo request](../07-website-and-conversion/demo-request.md). The buys that need two scoreboards are [paid media](../04-channels-and-distribution/paid-media.md) and [LinkedIn organic](../04-channels-and-distribution/linkedin-organic.md). Tests that can change the plan are [experimentation](experimentation.md). Whether next year’s number is possible is [GTM planning](gtm-planning.md). Person-level routing stays [lead scoring](lead-scoring.md). Funnel and pipeline *shapes* are still planned; do not fake them with this card.

## Sources and evidence boundary

This is an owner-maintained operating synthesis.

- **Two clocks: capture the 5, create among the 95; creative and media as inputs.** LinkedIn B2B Institute [95-5](https://www.linkedin.com/business/marketing/blog/research-and-insights/why-you-should-follow-the-95-5-rule?ref=b2b-playbook) and [CMO Scorecard](https://business.linkedin.com/advertise/resources/b2b-institute/cmo-scorecard?ref=b2b-playbook).
- **Open-text HDYHAU on declared-intent forms; software = capture, SRA = creation; read both.** Refine Labs [Attribution Mirage](https://www.refinelabs.com/blog/attribution-mirage?ref=b2b-playbook) and [Hybrid Attribution Framework](https://www.refinelabs.com/blog/hybrid-attribution-framework?ref=b2b-playbook). Sample sizes, $21.5MM, and the 90% figure are **their** study. Method only.
- Board-level SaaS metrics: Kellblog as a **company** scoreboard voice—not as channel attribution.
- Multi-touch SaaS products are tools. They are not this method. A planned `attribution.md` may go deeper on model math; it must not contradict the two-scoreboard rule.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
