# Working files

**Last reviewed:** 2026-08-29

Playbook pages teach the method. Files in this folder are the **blank you actually fill**. Markdown checklists stay on the page so an agent can execute; these files exist so a human can work in Sheets, Docs, or Slides without fighting GitHub preview.

## How to use a file

1. Open the matching playbook first. If you skip that, you will decorate a spreadsheet.
2. Download the file from GitHub (or clone the repo).
3. Make **your** copy. The intended home is Google Drive:

   | File type | Open it as |
   |---|---|
   | `.xlsx` | Upload to Drive → Open with **Google Sheets** |
   | `.md` slide outline | New **Google Slides** or Docs; paste one block per slide |
   | `.csv` | File → Import in Sheets |

4. Yellow / “INPUT” cells are yours. Gray / formula cells are the model. The **Teaching fill** sheet is invented—delete it before the file becomes your operating record.
5. Do not commit your customer data back to this repository.

Canonical files live here so they stay versioned, reviewable, and not locked in one Drive account. When a Google copy exists, it is listed in [TEMPLATES.md](../TEMPLATES.md). Rebuild the `.xlsx` files with `python scripts/build-working-files.py` (openpyxl) after you change the generator—do not hand-edit the binaries as the source of truth.

## What these files are not

They are not Pavilion, HubSpot, or classroom originals. They are original B2B Playbook working files distilled from method. Sample conversion rates, quotas, and point tables in source decks are **not** imported as facts.

[Catalog](../TEMPLATES.md) · [Playbook index](../playbooks/README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
