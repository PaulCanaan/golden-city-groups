# Website Publication and Maintenance

## Document Status

**Existing working procedure consolidated October 2, 2026 from Website Design Principles and Maintenance.** Historical implementation details are dated evidence, not a new live verification. Recommendations and remaining review arrangements retain their original status.

## Purpose and Ownership

Keep the Groups webpage accurate, accessible, recoverable, and connected to a truthful participant next step. **Owner:** Paul under DEC-037; Russ’s recorded review and pastoral/publication boundaries remain in force. This does not authorize new website publication.

**Start:** a profile, schedule, availability, content, design, or platform change requires attention. **Finish:** the authorized change is tested, the public result is actually checked, and the page record and Development Journey describe what occurred. Routine reconciliation uses the sole existing Biweekly Ministry Review.

## Process Map

| Stage | Action | Completion / next step |
|---|---|---|
| Reconcile | Compare governing direction, reviewed profiles, and current displayed information. | Verified corrections and unresolved matters are distinguished. |
| Prepare | Save a recovery copy and confirm review/approval requirements. | The change is recoverable and within authority. |
| Edit and test | Apply the change and test affected visitor paths and accessibility. | Publication checks below are satisfied. |
| Verify and record | Inspect the saved public result and update its records. | Actual publication and validation are recorded; unresolved work joins the existing queue. |

## Editing and Recovery

**Recorded installation: October 1, 2026 (native rebuild).** Taken from the build record in the Website Development project (`01_Projects/golden-city-groups/Build/Squarespace Implementation.md`) and matched to the live pages on October 2. Verify identifiers against the page before relying on them.

| Page | Squarespace location | Page ID | Route |
|---|---|---|---|
| Groups overview | **Pages → Connect → Groups** | `6abf21aecbfe5672822ec8e8` | `/groups` |
| Open Groups · Fall 2026 | **Pages → Not Linked → Fall 2026 Groups** | `6abf3242dcbef32a164f2b30` | `/groups/fall2026` |
| Groups Backup (former single page) | **Pages → Not Linked**, disabled | `6a60d8adbe9fc61fc3e156c1` | slug `groups-backup-2026-10-01` |
| Groups Backup 2026-09-19 | **Pages → Not Linked**, disabled | — | slug `groups-1` |

**Overview sections:** welcome `6abf21aecbfe5672822ec8ec`, semester invitation `6abf355955e2438928d89610`, branch cards `6abf309c27d49e690b78c149`, leading `6abf3595c78362634b0f86f3`, questions `6abf35ba601d114362cde31c`. Anchors: `#ways`, `#lead`, `#questions`.

**Directory sections:** introduction `6abf3242dcbef32a164f2b34`, seven-card list `6abf3242dcbef32a164f2b36`. Anchors `#city-groups`, `#collectives`, and `#bible-club` are added to the matching cards by the page's Code block.

### Routine edits (no code)

- **Overview:** open the page and edit the welcome, semester invitation, three branch cards (**Edit Content → Content**), leading invitation, or the FAQ Accordion directly.
- **A group card:** open the directory → **Edit Content → Content** → select the group. Replace the image (check the crop), edit the title and description, or change the **Join Group** link. Keep the leader names as the first description paragraph; later paragraphs appear inside **Group details**. Leave a missing link as `#join-link-pending`; a real Church Center URL replaces the "coming soon" behavior once the page is reloaded.
- Layout overrides are switched off while editing. Exit the editor to check the finished layout on desktop and phone.

### Code blocks

Each page has one small, page-scoped Code block for presentation and interaction only. Copies are archived in the build project's `semester-preview` folder (`squarespace-overview-enhancements.html` and `squarespace-directory-enhancements.html`). Before changing either block, save a dated copy. The church's global header, footer, and Site Styles are untouched.

### Rollback

To revert the overview: move the new overview to an unused slug and disable it; restore **Groups Backup** to the `groups` slug, enable it, and move it under Connect. Keep both pages rather than deleting either. The directory can stay published unless you mean to revert it too. **The backups may contain outdated public details** (old schedules, the former Women's address); review them before making either public.

The September 19 code-block build and its October 1 afternoon update are historical. Their source files stay in the build project for reference and are not the installed source.

## Maintenance Within the Existing Review

Paul owns updates under DEC-037. Use [[07 Operations/Workflows/Biweekly Ministry Review|Biweekly Ministry Review]] and its existing queue; this does not create a second maintenance cadence. A known wrong schedule, exposed address, or broken join route should be corrected promptly within Paul's authority rather than waiting for the next review.

| Trigger | Maintenance action |
|---|---|
| Regular biweekly review | Reconcile meaningful website changes, offering availability, dated announcements, and participant-path evidence with the OS and Planning Center. Carry unresolved consequential work in the existing queue. Do not infer live verification from a repository-only check. |
| New profile, changed rhythm, closure, or full group | Follow [[12 Ministry Website/Open Groups Listings|Open Groups Listings]]; update Planning Center and reconcile any manually displayed profile text. A Church Center list can update dynamically, but copied Squarespace details cannot. |
| Semester refresh | Refresh listings from reviewed City Group Profiles, remove expired dates and obsolete invitations, and verify destinations for the new offerings. |
| Material content or design change | Save a recovery copy, test the affected visitor paths and layout, update the page record, and record the change and review in the Development Journey. Use the review path recorded in DEC-037; future review arrangements beyond its pre-launch quick review must be recorded rather than assumed. |
| Parent-site redesign or Squarespace behavior change | Recheck visual alignment, component selectors, header clearance, disclosures, and shared navigation before changing global styles. |
| Repeated participant or maintenance difficulty | Record the actual problem and evaluate the smallest improvement. A finder, new tool, or native-section rebuild remains a proposal until justified and authorized within the relevant authority. |

### Before Publishing a Material Change

- [ ] Compare copy with current governing direction and reviewed profiles; distinguish active, upcoming, and future offerings, and follow rough-location and internal-field rules.
- [ ] Open every affected join, lead, contact, and QR destination; verify the intended offering, enrollment state, and follow-up path using [[07 Operations/Workflows/Forms#Pre-Publication Test|Pre-Publication Test]]. A successful page response alone is insufficient.
- [ ] Check desktop and narrow phone layouts (the original publication checked 390px and 320px): no horizontal overflow, legible copy, reachable actions, and working shared navigation.
- [ ] Check affected disclosures, FAQs, keyboard focus, find/lead anchors, and header clearance. Confirm useful image text and contrast; check text enlargement and reduced motion when styling changes.
- [ ] Confirm the recovery copy and any applicable review. After saving, inspect the public result and record only what was actually verified.

These checks record publication work; they do not grant ministry approval or establish offering readiness.

## Recording Future Design Choices

For a material design change, add a brief rationale to [[12 Ministry Website/Development Journey|Development Journey]]: **problem and evidence → alternatives considered → choice and reason → implementation/review status → validation and recovery reference**. One or two sentences are enough for a simple change. Label proposed work as pending; record publication only once it occurs.

If the choice changes ministry purpose, offerings, leadership authority, public theological claims, or another matter requiring pastoral direction, use the existing [[00 Dashboard/Decision Log#Decision Workflow|Decision Workflow]] and link its DEC record. Keep unresolved implementation in the [[00 Dashboard/Biweekly Review Queue|Biweekly Review Queue]], not in a new design backlog. A Development Journey entry does not approve a ministry decision.

## Connections

- [[12 Ministry Website/Design Principles and Maintenance|Website Design Principles and Maintenance]] — design rationale, history, and source references.
- [[12 Ministry Website/Ministry Website Overview#Publication Rules|Publication Rules]] — authority and public-information boundaries.
- [[12 Ministry Website/Open Groups Listings|Open Groups Listings]] — profile standard.
- [[12 Ministry Website/Groups Page|Groups Page]] — recorded live state and verification limits.
- [[12 Ministry Website/Development Journey|Development Journey]] — actual change record.
