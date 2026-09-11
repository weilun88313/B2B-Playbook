# Maintaining B2B Playbook

Start from the latest origin/main and preserve unrelated edits.
The default branch is the reader's current edition; normal updates may go directly to main.

- English is canonical. Update README.zh.md whenever root README coverage, entry points, or meaning changes.
- Edit the GitHub README sources for chapter and collection introductions. Run `python3 scripts/sync-entrypoints.py` to generate their Mintlify mirrors, refresh homepage coverage counts, and synchronize chapter navigation. Run it with `--check` in CI; do not edit generated mirrors by hand.
- Run `python3 scripts/check-content.py` before committing. CI runs the same checks.
- Write currency as `&#36;100` in Markdown prose and tables so Mintlify does not treat dollar pairs as math. Keep code examples and URL targets unchanged; reading safeguard tests run in CI.
- Add new reading pages to docs.json and an existing collection index.
- Publish company cases only with a named company, dated primary source, reported outcome, and explicit evidence limits.
- Keep third-party links' existing parameters and add exactly one ref=b2b-playbook. Repository and owned reading-site links are exempt.
- This checkout uses weilun88313's Git identity for Ivan's work. Never relabel another person's work or add an agent co-author trailer automatically.
- Verify author and committer before publishing. Historical author corrections require confirmed identity and a recoverable backup.
- Keep growth plans, traffic exports, and outreach drafts outside the public repository.
- Never run the workbook generator over a user's filled working files.
- Write for a reader doing a real task: explain the situation, show an example, and give a useful next step. Avoid unexplained internal jargon, scolding, and slogans presented as facts.
- Visual direction selected by Ivan on 2026-09-06: native Luma, Geist type, white/charcoal surfaces, and restrained violet accents (#7054BA light mode; #B6A0ED dark mode). Do not reintroduce the retired green/paper palette or serif titles.
- Logo selection updated by Ivan on 2026-09-06: round 2 concept C, Editorial. Preserve the outlined bold B2B + italic Playbook wordmark in light/dark versions; favicon uses the same bold B initial. This supersedes the first-round C route symbol. The italic wordmark is a brand-only exception: keep site headings and body text in Geist. Do not restore the route/book icons or substitute Index/Action concepts.
- Illustration direction updated by Ivan on 2026-09-06: 16:9 English-only editorial images inspired by Ian Xiaohei Illustrations. Use original topic-specific metaphors, a deadpan black worker doing the core action, white backgrounds, fine hand-drawn lines, generous whitespace and restrained blue/orange annotations. Website chrome stays violet. Do not copy the reference project's example compositions.
- Export article illustrations as 1600x900 WebP in assets/illustrations, keep meaningful English alternative text, and preserve white artwork in both site themes. Retain source PNGs and generation prompts outside the public repository. Favicons and brand marks are exempt from the 16:9 rule. Preserve third-party attribution in assets/illustrations/ATTRIBUTION.txt. Do not add filler images to every section.
- Retain old heading anchors when renaming sections. Keep last source-review dates honest; use a separate reading-edit date for copy-only revisions.
- Preserve Mintlify's native navigation, image zoom, table scrolling, keyboard focus, and light/dark controls. Check a phone-width page as well as desktop before publishing style changes.
- A chapter guide needs a plain introduction, a few starting links, a published-article map, a separate planned list, and related reading. Keep contributor-facing rules in this file, not in the reader's navigation.

## Reader cleanup policy — 2026-09-11

Ivan requested a cleanup after reviewing the public repository. Illustrations are optional: retain useful article artwork, brand assets, and attribution; omit decorative hero images from short working files. Validate retained assets and links rather than requiring an image count or an image on every article. Keep generation instructions, draft assets, traffic exports, and editorial process notes outside reader pages. Preserve source attribution and evidence limits. Prioritize the three task paths and reader feedback before expanding coverage.

- Workbook source maintenance: rebuild the distributed `.xlsx` files with `python3 scripts/build-working-files.py` (openpyxl) after changing the generator. Keep this command out of reader instructions and never overwrite filled user files.
