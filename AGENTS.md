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
- Write for a reader doing a real task: explain the situation, show an example, and give a useful next step. Avoid unexplained internal jargon, scolding, and slogans presented as facts.
- Visual direction selected by Ivan on 2026-09-06: native Luma, Geist type, white/charcoal surfaces, and restrained violet accents (#7054BA light mode; #B6A0ED dark mode). Do not reintroduce the retired green/paper palette or serif titles.
- Each playbook and chapter guide has a relevant SVG in assets/illustrations: neutral surface (#F7F7FA), charcoal text (#29282F), violet (#7054BA), simple lines, readable labels, and an accurate text alternative. Keep the visual helpful; do not add filler images to every section. Preserve dark-mode contrast when updating SVG colors.
- Retain old heading anchors when renaming sections. Keep last source-review dates honest; use a separate reading-edit date for copy-only revisions.
- Preserve Mintlify's native navigation, image zoom, table scrolling, keyboard focus, and light/dark controls. Check a phone-width page as well as desktop before publishing style changes.
- A chapter guide needs a plain introduction, a few starting links, a published-article map, a separate planned list, and related reading. Keep contributor-facing rules in this file, not in the reader's navigation.
