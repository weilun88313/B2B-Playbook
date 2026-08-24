# Tools

Small, dependency-free helpers for manual playbooks. Tools make rules repeatable; they do not replace account research or judgment.

## ICP account scorer

Scores the five dimensions in `zh/01-icp/templates/account-scorecard.md` and applies the trigger gate.

```bash
node tools/icp-account-scorer.mjs \
  --name "Acme Manufacturing" \
  --use-case 2 \
  --budget 2 \
  --alternative 1 \
  --trigger 2 \
  --committee 1
```

Add `--json` for machine-readable output. Add `--disqualified "reason"` when a hard exclusion applies.

```bash
node tools/icp-account-scorer.mjs --help
```

The scorer accepts only 0, 1, or 2 for each dimension. It does not research companies, upload data, call an API, or decide whether a claim is true.

## Tool contract

- One operational job
- Explicit inputs and outputs
- No secrets or network access
- Deterministic checks and tests
- The corresponding manual workflow remains readable without the tool
