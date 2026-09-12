---
title: "Privacy and compliance operations"
---

**Published:** 2026-09-12 · **Last reviewed:** 2026-09-12

Privacy operations turns applicable data-use requirements into repeatable work: knowing what data exists, why it is used, who can access it, and how requests or restrictions propagate. This guide is an operating design, not a determination that a particular campaign is lawful.

## Establish jurisdiction and responsibility

Identify the relevant organizations, people, regions, channels, and purposes with the responsible privacy or legal adviser. Rules differ across jurisdictions and activities. Consent is not the only possible basis for every processing activity, and a lawful basis for one purpose does not authorize all others.

## Build the control system

1. **Inventory data flows.** Map collection, enrichment, CRM, analytics, sending tools, partners, exports, and deletion paths. Record categories, purpose, source, recipients, and accountable owner.
2. **Document the approved use.** Record the applicable basis, notices, consent evidence where required, restrictions, and vendor responsibilities. Review new purposes or destinations before extending an existing workflow.
3. **Minimize access and retention.** Collect what the task requires, restrict access by role, and set purpose-based review or deletion rules. Avoid a universal retention period copied from another business.
4. **Operationalize rights and preferences.** Provide an intake route, verify identity proportionately, assign an owner, and follow applicable deadlines. Propagate corrections, withdrawals, objections, or deletion decisions through connected systems and processors as required.
5. **Handle exceptions deliberately.** Some records may need restricted retention for a valid obligation or suppression purpose. Document that decision and limit use; do not promise unconditional deletion of every record or retain everything “just in case.”
6. **Test and review.** Use synthetic records to verify preference changes, exports, access controls, and deletion propagation. Review incidents and vendor changes, and retain evidence that controls actually ran.

## Worked example

A fictional contact asks to stop marketing. The request updates the CRM and email platform, but a weekly enrichment import could recreate the old eligibility field. The operator fixes the import precedence and tests the complete flow with a synthetic record.

A minimal suppression record is handled under the approved policy so the person is not re-added by another source. The team distinguishes this marketing restriction from any separately justified service or recordkeeping need rather than assuming all communication has the same purpose.

## Data-use register

| Flow/purpose | Data and source | Approved basis/restrictions | Owner/vendor | Retention | Request propagation |
|---|---|---|---|---|---|
| | | | | | |

## Review before a new campaign

Check whether the audience source, destination, purpose, or jurisdiction has changed. Escalate unresolved legal questions to the appropriate adviser; do not hide uncertainty behind a checked box. The operational evidence should show which decision was made, by whom, and how it is enforced.

## Sources and scope

- [ICO: data protection principles](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/?ref=b2b-playbook) is a UK-specific primary reference. Apply current requirements for the actual jurisdiction and activity with appropriate advice.

The workflow and worked example are original operating guidance. Example numbers are illustrative, not benchmarks or reported customer results. Apply the method to your own evidence and constraints.

## What to read next

[MarTech governance](martech-governance.md) · [Contact research](../05-outbound-and-prospecting/contact-research.md) · [Lifecycle email](../08-lifecycle-and-customer-marketing/lifecycle-email.md)

[Chapter guide](README.md) · [All playbooks](../README.md)

---

Copyright © 2026 Ivan Xu. All rights reserved. See the [copyright and reuse terms](../../LICENSE).

Canonical source: [github.com/weilun88313/B2B-Playbook](https://github.com/weilun88313/B2B-Playbook)
