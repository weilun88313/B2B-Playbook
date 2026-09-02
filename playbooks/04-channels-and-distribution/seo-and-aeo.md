---
title: "SEO and AEO"
---

**Last reviewed:** 2026-09-02

Search used to mean a list of links. Buyers increasingly ask a model a full question and get an answer with or without a click. [Content strategy](../03-brand-story-and-content/content-strategy.md) still decides **which questions get a durable URL**. This page decides **how that knowledge is findable**—on your site, in places models cite, and in the questions you actually test—without making sessions-in-GA the only scoreboard.

This is not “SEO is dead,” not a promise that LLMs replace the website, and not a PR-agency pitch. [Channel strategy](channel-strategy.md) still names the primary motion. Answer-engine work is an amplifier on that motion, or a capture path if search is how demand already arrives.

## Use this when

- Leadership asks “do we show up in ChatGPT / Perplexity / AI Overviews” and the only answer is last quarter’s organic sessions.
- The team is shipping more posts because “AI needs volume.”
- Traffic is down or flat while sales still hears the same evaluation questions—see [content strategy](../03-brand-story-and-content/content-strategy.md).
- You are about to buy an “AI visibility” SKU with no list of questions you will prompt.

## Do not use this when

- Rows 1–3 of the decision-page map are empty. Write those URLs first.
- There is no ICP. You will optimize for questions nobody in your deals asks.
- The goal is to replace outbound or the first meeting with a citation.
- You need a legal opinion on training data or trademarks. Get qualified owners.

## Words you will use

| Word | Meaning here |
|---|---|
| **AEO** | Answer-engine optimization: being a source an answer system can use, not only a blue link |
| **Query** | The full question a buyer (or a model) asks—not only a two-word keyword |
| **Citation surface** | A place models and buyers actually read: your page, a review listing, a credible article, a forum thread you participate in |
| **Zero-click** | The answer is consumed without a session on your site. Still a visibility event; not automatically a lead |

## One rule

**Document the questions your ICP asks, on surfaces a model can cite—then measure whether the answer is accurate, not only whether anyone clicked.** Volume of new posts is a last resort. Refresh, structure, and third-party corroboration beat a content mill. Clicks remain useful when the motion is inbound capture; they are a **partial** score when the buyer never leaves the chat.

## Operating method

### Step 1: steal questions from deals, then from prompts

Start with the same evaluation questions [content strategy](../03-brand-story-and-content/content-strategy.md) already ranked. Add the **full questions** a buyer would type into an assistant (“what is the best _____ for a team that still lives in _____”). Keywords still matter as vocabulary; they are not the brief.

Write a prompt test list and **freeze it**. Twenty to fifty high-intent questions, held for at least four weeks, beats a new prompt every meeting. Record the date, the model, the answer, whether you are named, whether the facts are right, shortlist position, and which URL or third-party page it leaned on. That table is the experiment—see [experimentation](../09-operations-pipeline-and-measurement/experimentation.md)—not a vanity screenshot in Slack.

Citation share that moves to a decimal every month is not a KPI. Domains in answers churn; overlap across ChatGPT, Perplexity, and Overviews is thin. Measure **movement on a frozen set**, not a score that re-rolls.

### Step 2: make owned pages answer-shaped

For each question that deserves a URL: one primary question, clear headings, a short direct answer near the top, then the comparison or constraint the champion needs. Schema and formatting help machines parse; they do not replace a page that sales would paste.

Refresh evergreen decision pages before you add a twelfth educational post. Teams that only “publish more” train the model on mush and train sales to ignore the blog.

Crawler hygiene is not a strategy, but missing it is a tax. Before you buy an “AI visibility” tool:

- Put the facts a champion would paste in **HTML a crawler can read without executing JavaScript**. A client-rendered shell that looks finished in Chrome and empty to a bot is not an answer page.
- Add schema that matches what is actually on the page (Organization, SoftwareApplication, FAQPage when you have a real FAQ). Markup does not invent a comparison page.
- Write `robots.txt` **on purpose** for LLM crawlers: allow citation, block training, or the reverse—but do not leave the default and call it a policy. Some teams allow answer crawlers and block training crawlers; that is a legal/comms choice, not a ranking trick.

`llms.txt` and prompt-preset buttons are optional experiments. They do not replace rows 1–4 of the [content map](../03-brand-story-and-content/content-strategy.md).

### Step 3: put the same facts where citations come from

Answer systems do not only scrape your `/blog`. They weigh reputation: reviews, analyst and press mentions, documentation others already trust. Treat those as **citation surfaces**, not as a random channel spree.

A practical stack to test (not a mandatory media plan):

- **Reviews:** product description and customer proof on the sites that already appear in your category’s answers. Fake volume is a trust tax.
- **Earned / documented third party:** a real story worth citing, not a synonym for “hire an agency.”
- **Public conversations:** forums and communities your ICP already uses—participate as a practitioner, not a dump of press releases.
- **People:** executive or practitioner pages that match the names in your [content](../03-brand-story-and-content/content-strategy.md) and [pitch](../02-product-marketing/sales-enablement.md).

If you cannot name the surface and the fact it should repeat, you are “doing PR for AI” as a slogan.

### Step 4: change the dashboard before the board meeting

Executives still want revenue and CAC. Organic sessions and rankings no longer tell the whole visibility story when answers are zero-click. Last-click “AI referral” under-counts the job the way a Super Bowl QR code under-counts the ad. Add a **ladder** you can collect without pretending the top rung is pipeline:

- **Visibility (leading):** named or cited on the frozen prompt set, by model. Weekly.
- **Comprehension (quality):** the answer describes the product accurately, not last year’s packaging. Weekly.
- **Conversion (lagging):** signups or opportunities *sales* can trace to “they asked an assistant”—rare, labeled, not modeled into a sourced-pipeline percentage without evidence.

A page models already cite is a better place to add agent-readable facts than a new URL nobody retrieves. Markdown that a crawler can parse beats schema theater. Different models will ignore the same page—test per model, the way you already test per channel. Do not treat `llms.txt` as a strategy until you can show a lift on *your* frozen set.

Aggregate traffic can fall while the remaining visits convert harder. That is not “SEO is dead.” It is why sessions without a quality cut are a misleading growth metric.

Do not replace [GTM planning](../09-operations-pipeline-and-measurement/gtm-planning.md) with “share of AI answers.” Brand spend vs demand spend is a portfolio choice; AI search is not a reason to abandon rows 1–4 of the content map.

### Step 5: refuse the two superstitions

**Clicks-only:** you will under-invest in being cited. **Citations-only:** you will celebrate a mention that sends no one to a sales-usable next step. Hold both. The next step still lives on a URL, a review that names the category correctly, or a human conversation.

## Teaching fill (invented—not a customer)

Ops-tool, sales-assist. Not a survey.

| Question we prompt | Owned URL | Other surface | Last test | Action |
|---|---|---|---|---|
| “When is a shared inbox not enough for a 12-person ops team?” | Alternative page (row 2) | None yet | Named us; skipped the constraint page | Link constraint from the answer block |
| “&#123;us&#125; vs &#123;incumbent we actually lose to&#125;” | Comparison draft | G2 listing stale | Model used last year’s packaging | Refresh review copy + ship comparison |
| “Best &#123;category&#125; for SOC2-conscious mid-market” | Constraint page not started | No earned mention | Not named | Do not buy an AI-visibility tool yet |

## Copy: visibility one-pager (fill)

- Prompt-test questions (buyer voice):
- Owned URL for each (or “not this quarter”):
- Citation surfaces we will actually maintain:
- Accuracy errors we will fix this month:
- Diagnostics on the dashboard (mentions / accuracy / citations)—and what is **not** pipeline:
- Experiment we will run (link the ledger row):

Working file: [answer-visibility.xlsx](../../templates/answer-visibility.xlsx). Pages to write first: [content strategy](../03-brand-story-and-content/content-strategy.md).

## Pre-flight checklist

- [ ] Decision-page rows 1–3 exist or are explicitly deferred.
- [ ] Critical answers exist in crawlable HTML; schema matches the page; robots.txt states an LLM-crawler policy.
- [ ] Prompt list is questions from deals, not keyword daydreams—and frozen long enough to measure change.
- [ ] Each question has an owned answer or a written “not yet.”
- [ ] At least one non-owned citation surface has an owner, or we admitted we have none.
- [ ] Dashboard includes accuracy, not only sessions.
- [ ] No invented “AI-sourced pipeline %” without a sales-traced example.
- [ ] Agency or tool proposals were scored as [MarTech](../09-operations-pipeline-and-measurement/martech-governance.md), not as a panic buy.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Prompt-test hit rate (named, accurate) | Whether the knowledge is in the answer |
| Stale facts in answers | Refresh debt / comprehension |
| Sales forwards of the owned URL | Whether AEO served the champion |
| Sessions / rankings | Capture motion—partial under zero-click; useless without a quality cut |

Do not count posts published, or a survey’s “% of leaders seeing AI leads,” as your program.

## Common mistakes

- Declaring SEO dead while the site still has no comparison page.
- Publishing more instead of structuring and refreshing.
- Buying citations (fake reviews, doorway pages).
- Measuring only GA because the board still has that tab.
- Treating a Kickstand/Pavilion-style industry % as your baseline.
- Prompt-testing brand vanity queries (“who is the leader in X”) instead of evaluation questions.
- Skipping [experimentation](../09-operations-pipeline-and-measurement/experimentation.md) and calling a one-off ChatGPT screenshot a strategy.
- Shipping a JS-only shell, empty schema, or an untouched robots.txt and calling it AEO.

## What to read next

The URLs are [content strategy](../03-brand-story-and-content/content-strategy.md). The motion is [channel strategy](channel-strategy.md). Tests of message and channel still need a hypothesis card: [experimentation](../09-operations-pipeline-and-measurement/experimentation.md). Agents that *use* those facts still need stages and a send gate: [AI workflow](../09-operations-pipeline-and-measurement/ai-workflow.md). Listings as a citation surface—how they are earned and governed—are [review sites](review-sites.md). If strangers already trust someone else, that is [ecosystem](../06-account-field-and-partner/ecosystem.md).

## Sources and evidence boundary

This is an owner-maintained operating synthesis. It is not an SEO ranking product, not a measurement vendor, and not a claim that LLMs replace websites.

Question-shaped queries, zero-click as a measurement problem, owned pages plus citation surfaces (earned, reviews, public conversation), refresh/structure over raw volume, and diagnostics beyond sessions are distilled from a September 2025 industry report on AI-search visibility ([Kickstand × Pavilion, *The New Rules of Visibility*](https://5242563.fs1.hubspotusercontent-na1.net/hubfs/5242563/eBooks/Kickstand%20x%20Pavilion-TheNewRulesofVisibility-eBook.pdf?ref=b2b-playbook)). That report is a **method prompt**, not a source to copy. Its survey (606 marketing managers+, Jul 31–Aug 13 2025, NA/UK) percentages, industry splits, “AI-sourced leads,” and agency recommendations are **not** this library’s facts or a ranking. Named third-party claims inside the report (including Bain/Google consideration-set figures via HBR, 2022) stay with those authors—check the current source before you plan from them. Pavilion is a paid community listed in [RESOURCES.md](../../RESOURCES.md); membership is not required to use this page.

The warning that aggregate traffic misleads when remaining visits convert harder, the visibility / comprehension / conversion split, and the instruction not to treat referral clicks as the whole AEO score draw on Kyle Poyar / Kevin Indig ([Growth Unhinged, 2025-11-02](https://www.growthunhinged.com/p/traffic-is-no-longer-reliable?ref=b2b-playbook) and [2026-07-15](https://www.growthunhinged.com/p/how-to-measure-the-impact-of-ai-search-the-right-way?ref=b2b-playbook)). Webflow conversion multiples, Pew/ChatGPT CTR figures, Profound churn rates, and vendor dashboards stay with those authors. They are not this library’s baseline. Serving markdown to known AI bots and testing per model is a **method prompt** from a public Ramp experiment ([builders.ramp.com, Marketing to AI agents](https://builders.ramp.com/post/marketing-to-ai-agents?ref=b2b-playbook)); bot-count and relay figures there are one company’s log, not a playbook SLA.

Crawler hygiene (JS-rendered shells, schema that matches the page, an explicit LLM `robots.txt` policy) draws on Emily Kramer’s 100-company scrape ([MKT1, 2026-04-27](https://newsletter.mkt1.co/p/state-of-marketing-report-web-social-content-part-2?ref=b2b-playbook)) and the companion research note ([MKT1, 2026-05-06](https://newsletter.mkt1.co/p/state-of-marketing-report-part-3-how-to-research-in-claude-code?ref=b2b-playbook)). Sample percentages in those reports (“less than 2% have the basics”) are **their** scrape of **their** 100 companies on those dates—not this library’s SLA. Do not copy another company’s robots rules or treat `llms.txt` as strategy.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
