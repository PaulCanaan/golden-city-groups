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

**Recorded installation: September 19, 2026.** Verify these identifiers and the code block still match the page before applying them. The original build source remains in the website project; this migration does not move it or make its historical copy current.

| Item | Recorded location |
|---|---|
| Page | Squarespace **Pages → Connect → Groups → Edit**, page ID `6a60d8adbe9fc61fc3e156c1` |
| Installed component | Code block in section `6aaed596f92e6e235874ecb3`; Layers → Code → Content |
| Code block ID | `block-yui_3_17_2_1_1789840878837_33216` |
| Component scope | `#gc-groups`; structural CSS also targets specific section and block IDs |
| Navigation anchors | `#find`, `#city-groups`, `#collectives`, `#bible-club`, `#lead`, `#questions` |
| Recorded pre-build backup | **Groups Backup 2026-09-19**, under **Not Linked**, disabled, slug `groups-1` |

Before editing, save a dated copy of the installed code or duplicate the current page as a disabled backup. Change the visible code block rather than the hidden native sections. If section/block IDs change, verify the targeted hiding and layout rules still apply correctly.

The recorded full-reversal method is to replace the code block with its original `<div id="city-groups"></div>` content and save. This removes the replacement layout and its hiding rules, revealing the retained native sections. **Those sections and the September backup may contain obsolete public details.** Review and correct content before using either as a public recovery page. For routine recovery, prefer the most recent known-good copy of the current component.

Preserve the interaction fixes unless a tested replacement covers them: the find/lead links stop Squarespace's click propagation from overriding their anchors; header clearance uses `--header-height`; entrance-animation overrides inside the component keep expanded text visible. Retest these behaviors after layout or platform changes.

**Future option:** recreate the layout with native sections if the code block becomes a recurring obstacle for staff. Preserve the participant routes and accessibility, verify equivalent behavior, and remove obsolete hiding rules as part of that migration. There is no recorded requirement to rebuild it now.

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
