# CLAUDE.md

## What This Repository Is

This is **not a software project**. It is the **Groups OS** — an Obsidian vault that runs the Groups and Classes ministry of **Golden City Church (GCC)**, a church plant in the North Denver area that launched publicly on **September 20, 2026**.

The vault holds the ministry's governing direction, theology, ministry model, leader resources, operations, decision history, and working records. Editing a file here is a ministry act, not a code change: these documents direct real leaders, real participants, and real pastoral decisions.

**People:**

- **Paul** (the user) — Ministry Director for Groups and Classes. Operational owner: ministry design, coordination, leader support, calendar, Planning Center, communication, leader-interest follow-up. Writes in a pastoral, theological, formation-first voice.
- **Russ Daly** — Lead Pastor of GCC. Holds final readiness approval and the pastoral decisions recorded in DEC-021. Never write words on Russ's behalf or represent something as his direction unless the repository records it.

## The Ministry in One Screen

**Formation framework: Belonging → Beholding → Becoming.** All three branches serve it according to their distinct purpose.

| Branch | Purpose | Current form |
|---|---|---|
| **City Groups** | Life together | Location-based groups |
| **Collectives** | Shared encouragement | Men's Collective, Women's Collective |
| **Bible Clubs** | Rooted in Scripture | Facilitator-led study of a book or section of Scripture |

**Classes are not a fourth branch.** They are a future development path *under* Bible Clubs (DEC-034). Financial and marriage classes are illustrative future examples, not approved offerings.

Read before substantive work: [Ministry Context](01%20Governance/Ministry%20Context.md), [Theological Framework](01%20Governance/Theological%20Framework.md), [Ministry Model](01%20Governance/Ministry%20Model.md), [Launch Roadmap](01%20Governance/Launch%20Roadmap.md), [Decision Log](00%20Dashboard/Decision%20Log.md).

## The Cardinal Rule: Authority and Evidence

Most mistakes in this repo are **claiming more certainty than the record supports.** Always distinguish confirmed decisions, proposals, assumptions, and open questions — and say which one you are writing.

Source hierarchy when documents conflict:

1. [Decision Log](00%20Dashboard/Decision%20Log.md) (canonical chronological register) and [Decision History](08%20Archive/Decisions/Decision%20History.md) (full records and evidence)
2. `01 Governance/` — context, theology, model, launch sequence
3. [Open Decisions](00%20Dashboard/Open%20Decisions.md) and [Staff Decision Brief](00%20Dashboard/Staff%20Decision%20Brief.md) — organize unresolved work *without approving it*
4. [Launch Readiness Dashboard](00%20Dashboard/Launch%20Readiness%20Dashboard.md) — implementation evidence, blockers, ownership
5. Area pages (operations, leadership, branches, resources, calendar)
6. [Groups Ministry Dashboard](00%20Dashboard/Groups%20Ministry%20Dashboard.md) — current-state summary

Never silently resolve a conflict between sources. Add a queue item that links both.

Things that do **not** establish approval, appointment, or readiness:

- A file, folder, or city name existing in this vault
- A Planning Center record, Church Center listing, or enrollment setting
- An expression of interest, a sign-up, or a Group Leader Conversation
- A checked box in a biweekly review (those record *review execution only*)
- An item appearing in the Staff Decision Brief, Open Decisions, or the Inbox

Launch readiness has explicit gates in the Launch Roadmap. Readiness vocabulary (`Ready`, `On Track`, `In Progress`, `Blocked`, `At Risk`, `Not Started`, `Not Applicable`) is defined in the Launch Readiness Dashboard — use those words exactly, and never upgrade a status without evidence.

Flag anything needing Russ's approval rather than inventing leadership direction.

## The Operating Loop

One recurring review workflow exists. Do not create a parallel cadence.

```
Inbox (capture) → Biweekly Review Queue (consequential unfinished work)
→ Biweekly Ministry Review (1st/3rd Monday, 7:00 AM America/Denver)
→ Decision Log + Decision History → canonical page updates
→ Launch Readiness Dashboard → Groups Ministry Dashboard
→ dated report in 09 Reports/ → carry forward
```

- [Inbox](00%20Dashboard/Inbox.md) is temporary capture. File clarified items to their permanent home; never treat raw notes as approved direction.
- [Biweekly Ministry Review](07%20Operations/Biweekly%20Ministry%20Review.md) is the canonical procedure. Reports land at `09 Reports/Biweekly Reviews/YYYY-MM-DD Groups Ministry Biweekly Review.md`.
- Queue items carry owner, status, dependency, priority, next action, next review date.
- Decisions get the next `DEC-###` in the Decision Log **and** a full record in Decision History. Proposals under discussion use `PRO-###` in the Staff Decision Brief. A PRO becomes a DEC only after recorded staff or pastoral direction with source, date, and approver.
- Governance Index and Open Decisions are navigation aids. They never become decision records.

`scripts/biweekly_review.py` (driven by `scripts/church.goldencity.groups-biweekly-review.plist` via launchd) fires the review on schedule with overdue catch-up. It has a `--self-test` and a `--check` mode; `.review-runtime/` is local state and gitignored. An automated pass stays `In Progress` until a human completes review.

## Privacy — Non-Negotiable

Keep out of this vault entirely: pastoral notes, counseling records, safeguarding or screening details, assessment narratives, participant lists, phone numbers, addresses, anything about minors or vulnerable adults, and confidential staff discussion. Those live in the church-approved restricted system.

In reviews and dashboards, report **non-sensitive aggregate pipeline state only** — stages and counts, not people and details.

`11 Database/` reflects this: the `.base` view definitions are committed, but the record folders (`All Leaders/`, `All Groups/`, `People/`, `Groups/`) are **gitignored and local-only**. Records you can read on disk are not in version control — do not assume a collaborator sees them, and do not move their contents into tracked files.

Planning Center remains operationally authoritative for group and people records; this vault holds working views.

## Conventions

**Obsidian.** Numbered top-level folders (`00`–`11`) are the vault's spine; keep new material inside the existing structure. Internal links are `[[Wikilinks]]` inside vault documents; `README.md` and `CONTRIBUTING.md` use relative Markdown links with `%20` escapes for GitHub. `.canvas` files are Obsidian canvases. `.base` files are Obsidian Bases — YAML defining filters, formulas, properties, and table views over note frontmatter; they cross-reference notes by `record_type`, folder, and backlinks, so changing a record's frontmatter changes what the Bases show.

**Records.** New group and leader records come from `10 Templates/Records/`. Frontmatter drives everything: groups use `record_type: group` with `branch`, `group_status`, `semester`, `current_semester`, `leaders`; leaders use `record_type: group-leader` with `workflow_stage` (`Welcome email / call` → `Interviewed` → `Attended Training` → `Small Group Launched`). Leader–group assignment lives in the group's `leaders` property, not in a label on the leader note.

**Documents.** Most substantive pages open with a `## Document Status` block stating what is confirmed and what is not — preserve and update it. Use ISO dates (`YYYY-MM-DD`) in operational records and status labels (`Draft`, `Under Review`, `Approved`, `Archived`). Link to governing material instead of restating it.

**Commits.** Conventional commits with a ministry-area scope: `feat(governance):`, `docs(groups):`, `fix(model):`, `refactor(os):`, `chore(inbox):`.

## How to Write Here

- Preserve Paul's pastoral and theological voice. Avoid generic corporate ministry language.
- Prefer formation over information alone; prefer simple, sustainable structures over premature complexity.
- Explain major proposed changes before implementing them.
- Never silently delete substantive ministry content; superseded material moves to `08 Archive/`, and previously approved wording (like the Approved Ministry Purpose) is preserved rather than rewritten.
- Every major ministry proposal should state: theological rationale, ministry purpose, target participants, relationship to Belonging–Beholding–Becoming, operational requirements, leadership responsibility, launch priority, and approval status.
- `.agents/skills/complexity-discipline/` applies to scripts and structure: smallest correct solution, no speculative scaffolding.

**Done** means theologically coherent, operationally usable, internally consistent, appropriately approved, and connected to the rest of the ministry system — not merely well-written.

See [AGENTS.md](AGENTS.md) for the working rules this file builds on and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution and privacy expectations.
