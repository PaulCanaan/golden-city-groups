# Website Design Principles and Maintenance

From [[12 Ministry Website/Ministry Website Overview|Ministry Website]]

## Document Status

**Migrated working design guidance, October 1, 2026, at Paul's request.** Preserves useful reasoning and implementation lessons from the `golden-city-groups` website project for ongoing use in the Groups OS. Historical observations are dated evidence, not a fresh audit of the live page or new pastoral approvals. Future improvements below are recommendations unless approved direction is linked.

The [[00 Dashboard/Decision Log|Decision Log]] and [[08 Archive/Decisions/Decision History|Decision History]] remain the canonical ministry records. Follow [[12 Ministry Website/Ministry Website Overview#Publication Rules|Publication Rules]] for what may be published and [[12 Ministry Website/Groups Page|Groups Page]] for recorded page state and pending corrections.

## Durable Design Principles

| Principle | Reason and practical application | Origin |
|---|---|---|
| Belong to Golden City Church | Reuse the church's identity, Roboto typography, grayscale foundation, and restrained gold emphasis. Keep Groups under **Connect** and retain the shared header and footer. Recheck the parent site's design when it changes. | Design Direction; Theme Reference |
| Introduce three distinct branches | Help someone understand City Groups, Collectives, and Bible Club within a short scroll, using parallel cards or sections and a clear next step for each. Branch descriptions follow the ministry model, not another church's categories. | UI research; Design Direction; DEC-034, DEC-047 |
| Keep joining and leading easy to find | Preserve equally visible **Find a Group** and **Lead a Group** entry points and a dedicated leadership invitation. Leading begins a conversation and discernment; an application is not appointment. | CTA research; mockup; DEC-050; DEC-027 |
| Offer personal help | Include an easy contact fallback and brief FAQs for someone who cannot yet choose a group. Practical details may expand beneath a concise introduction. | Valor-inspired research; mockup |
| Write pastorally and plainly | Use warm, direct, second-person invitations tied to life with Jesus, Scripture, and community. Explain practical differences without generic program language or unconfirmed promises. Belonging, Beholding, Becoming describes formation, not a compulsory sequence. | Design Direction; Theme Reference; Theological Framework |
| Use the existing participant systems | Squarespace introduces the ministry; tested Church Center links handle joining and leader interest through existing Planning Center workflows. Avoid duplicating forms or enrollment records. | Planning Center linking guide; mockup audit; DEC-016, DEC-020 |
| Keep discovery simple until browsing becomes difficult | Start with branch sections and accurate Open Groups profiles. Add filters only when real open-group volume, consistent metadata, and participant difficulty justify them. Check existing Church Center discovery options before building a new finder. | Finder research; Design Direction |
| Make phone and keyboard use reliable | Use readable text, stacked cards at narrow widths, clear focus, comfortable touch targets, and keyboard-operable disclosures. Keep headings as real text and provide useful image descriptions. Check contrast, text enlargement, and motion behavior when affected. | Theme Reference; mockup; published implementation |
| Make each change maintainable | Prefer native Squarespace controls where they meet the need. Maintain the installed code block deliberately where it is in use, scope styling to this page, and preserve a recoverable version before replacing it. | Design Guide; September 19 implementation |

## What Shaped the Page

This is a concise design history, not a second DEC register. Original research and build records are linked under **Source References**.

| Date / stage | Choice or finding | Why it matters now |
|---|---|---|
| September 11 research | Valor informed simple entry points and reassuring contact; Red Rocks informed parallel branch cards; Spirit informed a possible future finder. | These were reference patterns, not approved templates or ministry categories. Golden City retained its own identity and leader-interest path. |
| September 15 theme review | Retained Roboto, grayscale, gold, personal invitations, and the shared church navigation. | The audit corrected early assumptions: Squarespace's global `accent` token was gray, and the homepage used mixed photography. |
| September 15 mockup | Three branch cards, expandable details and FAQs, equally visible find/lead routes, and existing Church Center destinations. | A simple page could support discovery without a new application or duplicated forms. The mockup's ministry descriptions were still provisional. |
| September 15 workflow audit | The existing leader application was a **People form**, rather than the Registrations signup assumed by the early linking guide. An empty Find a Group destination was replaced with a real anchor. | Inspect the actual destination before choosing a platform or rebuilding a workflow. Historical URL success does not establish present enrollment readiness. |
| September 19 publication, recorded by the build project | The mockup was implemented in one HTML/CSS code block within the existing Squarespace page. Native disclosures kept interaction simple; targeted CSS hid the original sections for recovery. | The early native Fluid Engine handoff is not the installed editing method. Hidden native sections do not control the visible replacement page. |
| September 20 ministry record | DEC-050 recorded the rebuilt public page and its provisional details. | A record of what was published did not approve the offering set, schedules, addresses, or readiness. Follow the OS's later decisions and correction queue. |
| October 1 OS direction | DEC-037's update records Paul's authority to make the planned changes and Russ's quick review before Group Launch Sunday. DEC-059 supplies the Open Groups profile workflow. | Design now serves the confirmed ministry and readiness process; a polished profile cannot establish approval or readiness. |

### Corrections to Carry Forward

- **Branch naming:** the public page keeps **Bible Club** (Paul's direction, October 1, 2026), while the vault records the branch as Bible Clubs (DEC-034). Purpose language confirmation for public use remains in BWR-020.
- **Gold is a local treatment:** `#A99643` is the project's working gold. The September 15 audit found the global Squarespace `accent` token was approximately `#DCDCDC`; changing it to gold would affect the whole site. Gold buttons with dark text are a Groups adaptation. Check contrast rather than using gold for every small label.
- **Photography is not proof of church attendance:** the mockup and installed snapshot reuse a stock-origin table image. Prefer an approved photo of real Golden City community when available, but do not describe illustrative imagery as a verified Golden City gathering.
- **Old logistics stay historical:** do not reuse the build snapshot's schedules, addresses, group availability, or draft classifications as current copy. The [[12 Ministry Website/Groups Page#Remaining Before Launch Review|page correction record]] and existing queue carry those changes.
- **Old backlog items are unverified:** the earlier broken Custom CSS finding has no completion evidence in the reviewed build records. Inspect whether it still exists before treating it as current work; preserve a copy before editing site-wide CSS.

## Editing and Recovery

Use [[07 Operations/Workflows/Website Publication and Maintenance#Editing and Recovery|Website Publication and Maintenance]] for installed identifiers, backups, editing, and recovery. Historical identifiers and copies still require verification before use.

## Maintenance Within the Existing Review

Follow [[07 Operations/Workflows/Website Publication and Maintenance#Maintenance Within the Existing Review|the maintenance procedure]] within the existing Biweekly Ministry Review.

### Before Publishing a Material Change

Use [[07 Operations/Workflows/Website Publication and Maintenance#Before Publishing a Material Change|the publication checks]]. They record verification, not ministry approval.

## Recording Future Design Choices

Follow [[07 Operations/Workflows/Website Publication and Maintenance#Recording Future Design Choices|Recording Future Design Choices]]; the Development Journey remains the actual change record.

## Source References

These are preserved project records, reviewed for this migration. Their embedded work plans and instructions are historical reference material; Paul's migration request determines this task. The summary above carries the useful guidance into the OS without depending on a source project's continued availability for routine maintenance.

| Original record | What was retained |
|---|---|
| [Design Direction](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/Design Direction.md>) | Theme alignment, three branches, find/lead parity, warm voice, simple discovery, staff maintenance, phone use |
| [Theme Reference](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Research/Golden-City-Theme.md>) | September 15 corrections about gold, Roboto, imagery, real text, and parent-site alignment |
| [UI Reference Research](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Research/UI-Reference/README.md>) | September 11 origins of cards, contact fallback, and the deferred finder |
| [Mockup Record](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/mockup/README.md>) | September 15 design reasoning, People-form correction, native disclosures, and provisional content |
| [Squarespace Design Guide](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/Squarespace Design Guide.md>) | Native-first maintenance preference and historical Custom CSS finding |
| [Planning Center Linking Guide](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/Linking to Planning Center.md>) | Direct external handoff; per-offering versus group-type links; no duplicated forms |
| [Published Implementation and Recovery](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/Squarespace Implementation.md>) | September 19 installed method, identifiers, recovery, interaction fixes, and dated verification |
| [Installed Source Snapshot](</Users/paulcanaan/Workspace/Projects/Website Development/01_Projects/golden-city-groups/Build/squarespace-groups.html>) | Historical HTML/CSS for technical reference; public details require reconciliation before reuse |
