# Tools

Small, transparent utilities that support the playbooks.

## Design rules

- Solve one recurring operational problem.
- Keep inputs and outputs explicit.
- Prefer local files and reproducible transformations.
- Never require secrets in a tracked file.
- Include a short example and a way to verify the result.

## Planned tools

- Account research brief generator
- Campaign and experiment ledger
- Content-to-pipeline tracker
- Opportunity review checklist

Tools are added only after the manual workflow has been used enough to
understand the problem. A script should remove repeated work, not hide the
reasoning behind a recommendation.
