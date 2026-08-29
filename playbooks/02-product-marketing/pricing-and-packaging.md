# Pricing and packaging

**Last reviewed:** 2026-08-29

A year of free users who give generous product advice is a common way to delay the only question that matters: **who will pay, and for what?** Unpaid usage is a weak signal. People who will not pay still have opinions. Founders then underprice the thing they built, because “startup software should be cheap,” and spend a quarter designing four editions for a tenth customer who does not exist yet.

Early B2B pricing is a learning system: charge soon enough to find who will pay, high enough to match value, simple enough to explain, and scheduled for revisit. It is not a four-tier spreadsheet that must survive the next decade.

Positioning names the alternative and the result. Pricing converts that result into a number a champion can defend. Complete [positioning](positioning.md) first so you are not discounting a slogan. If nobody loves the product in production, charging will not create [fit](../01-strategy-and-buyers/product-market-fit.md)—but refusing to charge will hide whether fit was ever going to include a buyer.

## Use this when

- Users love the product and still have not been asked to pay.
- Founders are setting price from “what feels fair” rather than from value or comps.
- The team is designing four editions before the tenth customer.
- Usage-based billing is on the table and nobody can name the utility metric.

## Do not use this when

- There is no ICP or alternative. Complete [ICP](../01-strategy-and-buyers/icp.md) first.
- Legal, tax, or public-procurement rules must set the offer. Get a qualified owner; this page is not legal or accounting advice.
- The work is a full packaging redesign for a multi-product enterprise catalog. Start with [position the way you sell](positioning.md#step-8-position-the-way-you-sell), then return here for the commercial mechanic.

## Operating method

### Step 1: charge sooner than feels polite

Unpaid usage is a weak signal. People who will not pay still give advice. Ask “will you pay for this?” while the product is early. A year of free users who collapse to a token amount is a lost year of finding someone who will.

In one founder interview set, teams that delayed charging (including stories told around Amplitude, Zip, and Front) later described the delay as lost learning, not kindness. Treat those as illustrations with dates in the source, not as a command to copy their later list price.

Exceptions exist (delaying monetization to become the default tool inside companies). Treat delay as an explicit strategy with a date, not as fear of asking.

Early revenue also buys focus: less fundraising theater, more time on customers. That is a side effect, not a reason to underprice.

### Step 2: charge more than the founder’s gut

Founders systematically underprice what they built. Whatever number feels comfortable, test a higher one. A first account executive will often quote deals the founder would never have asked for.

A practical loop used by several teams: raise price on the next similar deal until it stops working, then triangulate. Anchor on **value** (time saved, headcount not hired, revenue unlocked, risk reduced)—not on “startup software should be cheap.” How the market already buys (seat vs consumption) is Step 4.

### Step 3: keep the first offer stupid-simple

One public tier plus “contact us” for the genuinely different enterprise path beats four cells nobody can explain. You can change price later. The first few deals, if the company works, are a rounding error of later revenue.

Make the commercial term explicit (for example valid for one year) and move on. Do not spend the week designing grandfathering for deal number three.

Be decent to design partners who used unfinished software: simplicity and a clear upgrade path beat a surprise list-price attack. Friendship is not a forever discount with no review.

### Step 4: pick a metric that matches value, not what is easy to count

For seat-based products, seats are often enough at the start.

For usage-based products, name the **utility metric**: the unit the buyer already believes is “more value.” Easy-to-meter units (API calls, tests, rows) fail when they punish the behavior you want or when they do not track value.

Two shapes from that same interview set, useful as tests rather than as prices to copy:

- Charging per **test run** can punish the team for testing every build. A unit closer to **who derives value** (for example contributing developers, in Snyk’s telling) may track the job better.
- Putting a dollar on **share** or **invite** can tax the loop that spreads the product. Coda’s version of this warning: do not meter the action you need to be free unless you are deliberately applying a brake.

If a dominant incumbent already trained the market on a model (per seat, pay-as-you-go, annual license), default to that model unless you have a strong reason to deviate. Databricks’ version: buyers already understood cloud consumption the way Amazon had taught it. Deviating is a teaching cost.

If you cannot measure the true value unit yet, quote by hand for a while and listen: do they understand the metric, and do they accept where they sit on the curve? Made-up quotes are research, not a forever price book.

Surveys (including Van Westendorp-style questions), competitor list prices, and plots of “this customer pays X at usage Y” are inputs. They do not replace live deals.

### Step 5: put a revisit on the calendar

Simple on day one is correct. Never looking again is the failure. Revisit at least every six to twelve months, or sooner after a new segment, a new product, or a repeated “yes” at a price that still feels too low.

The first hard packaging change (for example an org or security tier) will feel thin. Ask buyers how they justify spend against savings and against other tools they already buy. Feature-to-price mapping is a hypothesis; the market will tell you.

## Copyable templates

### How a filled price card reads

Teaching fill from the same 2023 interview set, not a price book to copy.

- **Snyk-shaped metric:** per test run is easy to meter and punishes testing every build. A unit closer to who derives value (contributing developers, in that telling) survives the “does this punish good behavior?” test.
- **Coda-shaped brake:** a dollar on share or invite taxes the loop you need to be free.
- **Databricks-shaped model:** buyers already understood cloud consumption the way Amazon had taught it; inventing a new commercial language is a teaching cost.
- **Amplitude / Zip / Front-shaped timing:** delaying the ask felt kind; they later described it as lost learning.

### Early price card

- Champion seat and alternative:
- Value story in one sentence (from positioning):
- Model: seat / usage / hybrid / other:
- Utility metric (if usage):
- Why this metric matches value (and what bad behavior it might cause):
- List or starting quote:
- Comp we used (incumbent or none):
- Term (e.g. 12 months):
- What is explicitly out of scope:
- Next similar deal we will quote **higher** unless this one already broke:
- Revisit date:

### Utility-metric test

| Candidate unit | Easy to meter? | Tracks value? | Punishes a behavior we want? | Buyer understands it? | Keep / kill |
|---|---|---|---|---|---|
| API calls / test runs | Yes | Often no | Yes—teams stop testing or splitting work | Sometimes | Kill unless the job *is* the call |
| Seats | Yes | Yes, if value is per human | Rarely, unless you need viral share | Usually | Keep at the start for seat products |
| Contributing developers (Snyk-shaped) | Harder | Closer to who gets safer code | Less than per-test | Needs a one-sentence explain | Test live |
| Share / invite (Coda-shaped) | Yes | No—it meters spread | Yes | Painfully | Kill unless you want a brake |

Kill units that are easy to bill and wrong to optimize. Copy: write your candidate units through the same five columns.

### Revisit agenda (30 minutes)

1. What did the last 10 wins actually pay, and how did they justify it?
2. Where did we lose or discount, and was it fit or price?
3. Which segment now needs a different door (self-serve vs sales-assist)—see [channel strategy](../04-channels-and-distribution/channel-strategy.md)?
4. One change we will test on the **next** deals, not a rewrite of every contract.

## Pre-flight checklist

- [ ] Someone has asked for money, not only for feedback.
- [ ] The number is above the founder’s first gut, or a written reason explains why not.
- [ ] A buyer can explain the price in one sentence.
- [ ] There is one default public path; enterprise exceptions are named, not a maze.
- [ ] If usage-based, the utility metric survives the “does this punish good behavior?” test.
- [ ] First-customer terms have an end date.
- [ ] A revisit date exists on a calendar, not in a strategy doc.
- [ ] Claims in the value story stay inside dated evidence.

## Metrics

| Metric | Diagnostic use |
|---|---|
| Time from first serious use to first paid invoice | Detects “charge later” drift |
| Quote-to-close at current price | Tests whether the number is imaginary |
| Discount rate on qualified deals | High rate often means weak value story or wrong segment, not “sales needs room” |
| Expansion vs initial ACV | Whether year-one simplicity is blocking later packaging |
| Metric disputes | Tickets or calls about “what we are billing”—a bad utility metric shows up here |

Do not count a completed pricing workshop, the number of tiers, or alignment with a famous SaaS price as success.

## Common mistakes

- Waiting for the product to feel finished before asking for money.
- Pricing from founder fairness instead of buyer value.
- Four tiers and a matrix before ten customers.
- Choosing a billing unit because the product already logs it.
- Never revisiting a “temporary” simple price.
- Copying an incumbent’s price without their category power.
- Letting a single customer invent a billing model the systems and contracts cannot run.
- Putting a dollar sign on the action that spreads the product (share, invite, test-every-build) unless that is a deliberate brake.

## What to read next

The number only holds if the champion can tell the value story: stay inside [positioning](positioning.md) and the [pitch](sales-enablement.md). How you collect the number is a channel fact—[channel strategy](../04-channels-and-distribution/channel-strategy.md). If you are still counting unpaid “love,” that is the [PMF ladder](../01-strategy-and-buyers/product-market-fit.md), not a packaging workshop.

## Sources and evidence boundary

This is an owner-maintained operating synthesis. Price, tax, invoicing, and consumer-law rules vary by jurisdiction and contract.

The charge-sooner / charge-more / keep-simple / revisit cadence, the warning that founders underprice, the utility-metric test, and the “default to how the market already buys” heuristic draw on founder interviews collected by Lenny Rachitsky ([Lenny’s Newsletter, 2023-10-24](https://www.lennysnewsletter.com/p/scaling-your-b2b-growth-engine?ref=b2b-playbook)). Named companies and survey methods in that source are illustrations with the author’s attribution, not this repository’s price book or a recommendation to copy any list price. Van Westendorp and similar instruments are research tools; they are not a substitute for signed deals.

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
