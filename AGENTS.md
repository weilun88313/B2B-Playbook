# Maintaining B2B Playbook

Start from the latest origin/main and preserve unrelated edits.
The default branch is the reader's current edition; normal updates may go directly to main.

- English is canonical. Update README.zh.md whenever root README coverage, entry points, or meaning changes.
- Keep each domain README.md and index.md synchronized; only frontmatter and platform link destinations differ.
- Run `python3 scripts/check-content.py` before committing. CI runs the same checks.
- Add new reading pages to docs.json and an existing collection index.
- Publish company cases only with a named company, dated primary source, reported outcome, and explicit evidence limits.
- Keep third-party links' existing parameters and add exactly one ref=b2b-playbook. Repository and owned reading-site links are exempt.
- This checkout uses weilun88313's Git identity for Ivan's work. Never relabel another person's work or add an agent co-author trailer automatically.
- Verify author and committer before publishing. Historical author corrections require confirmed identity and a recoverable backup.
- Keep growth plans, traffic exports, and outreach drafts outside the public repository.
- Never run the workbook generator over a user's filled working files.
