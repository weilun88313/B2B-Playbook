# 10-minute ICP sprint

The goal is not to finish a persona. The goal is to decide whether one account deserves active sales time and what should happen next.

## Inputs

Choose one account and collect only information you can verify:

- the business job it must complete;
- an observable size or budget-owner signal;
- the current alternative process or tool;
- a trigger that matters this quarter;
- known buying-committee seats.

Write `unknown` when evidence is missing. Do not turn model output into a fact.

## 1. Apply disqualifiers

Open the [ICP canvas](templates/icp-canvas.md) and write at least five hard exclusions. If an account matches one, classify it as T3 without rescuing it through scoring.

## 2. Score five dimensions

Use only 0, 1, or 2 for each dimension. The full definitions are in the [account scorecard](templates/account-scorecard.md).

```bash
node tools/icp-account-scorer.mjs \
  --name "Example account" \
  --use-case 2 --budget 2 --alternative 1 --trigger 2 --committee 1
```

T1 requires at least 7/10 and a non-zero trigger. An account without an observable trigger can be no higher than T2. A hard disqualifier always results in T3.

## 3. Assign the default action

| Tier | Default action |
|---|---|
| T1 | One-to-one research, resolve committee unknowns, and prepare a personalized next step |
| T2 | Run a small segment test around one shared trigger hypothesis |
| T3 | Keep out of active outbound and record the disqualifier or missing evidence |

## 4. Leave six outputs

1. A one-sentence ICP
2. Five disqualifiers
3. A buying-committee map
4. Dimension-level evidence and a T1/T2/T3 tier
5. One default next action
6. Unknowns and how to resolve them

Compare the level of detail with the [filled Helion example](examples/helion-icp.md), then finish with the [completion checklist](checklists/icp-complete.md).
