# Biweekly Ministry Review

## Document Status

**Canonical operating procedure for the queue-based ministry review loop; not a governing decision record or a second dashboard.** The [[00 Dashboard/Biweekly Review Queue|Biweekly Review Queue]] carries unresolved work, dated reports preserve review history, and the [[00 Dashboard/Groups Ministry Dashboard|Groups Ministry Dashboard]] shows the current state.

## Purpose and Cadence

The review exists to move Groups Ministry toward faithful launch readiness, healthy execution, and sustainable development across City Groups, Collectives, and Bible Clubs. It runs at **7:00 AM America/Denver on the first and third Monday of each month**. Mountain Time is the authority so the local time remains correct through daylight-saving changes.

Each report covers the period after the previous completed biweekly review through the current review. If no completed report exists, record an initial baseline rather than implying a historical review window.

## Scope and Ownership

**Owner:** reviewer for inspection and reconciliation; Paul supplies ministry judgment and missing facts; Russ retains pastoral/approval decisions. **Output:** dated review report from the canonical template, reconciled queue and sources, updated dashboards, and explicit human-review status. No parallel cadence is created.

## Process Map

| Stage | Action | Completion / next step |
|---|---|---|
| Intake | Read previous review, Inbox, queue, and meaningful changes. | Review window and actual priorities are clear. |
| Reconcile | Inspect queue, people, environments, events, readiness, and decisions. | Evidence, gaps, owners, and next actions are distinguished. |
| Write back | Update canonical sources before dashboards. | Current summaries agree with supported source changes. |
| Report / carry forward | Use the dated report template and preserve unresolved items. | Execution and human review are separately recorded; next review is named. |

## Recenter

Begin from Golden City Church's mission and the approved ministry purpose in [[01 Governance/Ministry Context|Ministry Context]], with [[01 Governance/Theological Framework#Belonging, Beholding, Becoming|Belonging → Beholding → Becoming]] as the formation framework.

- People matter more than completion metrics.
- Handle leadership, care, and safeguarding with pastoral attentiveness and appropriate privacy.
- Prefer faithful formation and truthful execution over merely closing tasks.

## Source Hierarchy

Use the existing system; do not create a parallel plan.

1. [[00 Dashboard/Decision Log|Decision Log]] and [[08 Archive/Decisions/Decision History|Decision History]] govern approved direction and preserve its history.
2. The governing documents in `01 Governance` define ministry context, theology, model, and launch sequence.
3. [[00 Dashboard/Open Decisions|Open Decisions]] and [[00 Dashboard/Staff Decision Brief|Staff Decision Brief]] organize unresolved questions and proposals without approving them.
4. [[00 Dashboard/Launch Readiness Dashboard|Launch Readiness Dashboard]] controls implementation evidence, blockers, ownership, and readiness.
5. Operations, leadership, branch, resource, and calendar pages hold their subject-specific instructions and evidence.
6. The [[00 Dashboard/Groups Ministry Dashboard|Groups Ministry Dashboard]] summarizes current state; this procedure is the sole recurring review workflow.

When sources conflict, add a queue item linked to both sources. Do not silently choose one.

## The Loop

```text
Canonical sources → meaningful change detection → review queue → biweekly analysis
→ dated-event reconciliation → human review → decision capture → canonical updates
→ dashboard refresh → archive or carry forward → next review queue
```

### Intake between reviews

Add a queue item when a repository or ministry update has an operational consequence: a governing decision changes, an event outcome is supplied, a blocker changes, a leader advances an approved stage, a launch date changes, or a downstream document needs reconciliation. Routine edits with no consequence do not belong in the queue.

Staff-meeting direction from Paul and Russ is authoritative only after its source, date, approver, and actual direction are recorded. Determine whether it needs a DEC record, then update affected canonical pages and queue any unfinished downstream work.

Process the [[00 Dashboard/Inbox|Inbox]] during each review. Between reviews, file clarified items directly into their canonical destination and add only consequential unfinished work to the queue. This removes the need for a separate weekly review while keeping urgent changes visible.

### Full review procedure

1. Find the newest completed report and set the review window. Read its carry-forward section, the current queue, and every Inbox item first.
2. Inspect meaningful repository changes across governance, readiness, operations, leadership, communication, safeguarding, resources, calendars, and ministry-area pages. Flag stale TODOs, conflicting statuses, and missing next actions.
3. Reconcile every queue item. Review owners, deadlines, status changes, blockers, and the leader pipeline; every unresolved item keeps a dependency, prioritized next action, and next review date.
4. Reconcile events and milestones whose dates entered the window or are now past. Do not infer outcomes. Ask Paul only for missing facts or decisions, preserve confirmed history, and clean up stale future tense.
5. Review the next two to four weeks of the calendar and critical path, including offering readiness, leader preparation, systems, communication, and shared dependencies.
6. Capture decisions from Paul, Russ, and staff meetings. Record approved direction in the Decision Log and Decision History before updating dependent sources; keep expressions of interest and proposals distinct from appointments or approval.
7. Assess each ministry area and the actual critical path using the readiness vocabulary in the Launch Readiness Dashboard. Surface what moved, what is blocked, and the few highest-leverage next actions.
8. Update canonical source documents, then the Launch Readiness Dashboard, then the primary dashboard. File or archive resolved Inbox and event material without deleting ministry evidence.
9. Create `09 Reports/Biweekly Reviews/YYYY-MM-DD Groups Ministry Biweekly Review.md`, carry every unresolved item forward, record focused questions for Paul and Russ, and name the next first- or third-Monday review date.

## Dated Report Execution Layer

Use [[10 Templates/Reports/Biweekly Ministry Review Report|Biweekly Ministry Review Report]] for metadata, the execution checklist, ministry-area matrix, risks, actions, and completion record. A checked box means inspected and reconciled; it never proves task completion, readiness, appointment, or approval. An automated pass remains **In Progress** until required human review is complete.

## Queue Lifecycle

Use these statuses: `Ready`, `In Progress`, `Waiting — Paul`, `Waiting — Russ`, `Waiting — External`, `Blocked`, `Scheduled`, `Completed`, `Archived`, or `Cancelled`.

Every item must end in one of four places:

- it remains active with a next review date;
- it is completed and names the canonical destination or evidence;
- it is archived or cancelled with a reason; or
- it becomes a dated future action with an owner only when the repository establishes one.

Do not infer an owner. Use `Unresolved` and ask for ownership when evidence is absent. Do not put participant identities, interview notes, screening details, pastoral narratives, or safeguarding reports in the queue or reports.

## Human and Decision Boundaries

- Codex may update facts clearly supported by repository evidence.
- Operational recommendations must remain labeled as recommendations.
- Paul supplies ministry judgment and missing event outcomes.
- Items within Russ's pastoral or approval authority remain `Waiting — Russ` until recorded.
- Automation must never invent an event outcome, appointment, approval, policy, owner, or date.

## Event and Archive Lifecycle

After Paul confirms an event outcome, update the relevant calendar, plan, readiness page, and operational record; capture decisions and follow-ups; replace stale future tense; and archive temporary planning material when repository conventions call for it. Archive means preserve, not delete. If another occurrence is expected, create a new dated queue item rather than leaving the completed event active.

## Dashboard and Report Behavior

The primary dashboard links only the newest review, current window, next review, queue, outstanding human input, and critical blockers. Dated reports retain prior analysis. The queue carries unresolved work between reports. None of these replaces a canonical governance or subject-matter page.

## Automation Contract

**Installed and verified September 8, 2026:** Paul reported that the desktop app has no Scheduled/Automations controls. At his request, Codex installed the local macOS LaunchAgent `church.goldencity.groups-biweekly-review` with the repository-owned runner at `scripts/biweekly_review.py`. The catch-up report was delivered into the vault, links and the success receipt were checked, and a repeat invocation was idle. BWR-013 is complete; see the [[09 Reports/Biweekly Reviews/2026-09-08 Groups Ministry Biweekly Review#Post-Run Scheduler Verification|verification record]].

- **Trigger:** first and third Monday of each month at 7:00 AM
- **Time zone:** `America/Denver`
- **Working directory:** repository root
- **Recurrence:** `DTSTART;TZID=America/Denver:20260907T070000` with `RRULE:FREQ=MONTHLY;BYDAY=1MO,3MO;BYHOUR=7;BYMINUTE=0`
- **Instruction:** use the durable task prompt below
- **Runner:** installed Codex CLI with the existing ChatGPT sign-in, `gpt-5.6-sol`, workspace-write sandbox, and no interactive approvals. The September 8 test of `gpt-6-astra` was rejected because CLI 0.151.0 requires an upgrade for that model; Sol is advertised by this installed CLI.
- **Safety:** leave changes reviewable; do not commit, publish, message people, or record human decisions without explicit authority

The LaunchAgent checks at login, daily at 7:00 AM system time, and hourly for catch-up. These checks invoke Codex only when the latest first/third-Monday 7:00 AM **America/Denver** occurrence is due and has no successful run. The Mac currently uses America/Denver; the Python date guard uses that named zone independently, including daylight-saving changes. There is still only one ministry-review cadence. Keep the Mac on, logged in, and connected to the internet; the desktop app itself is not required. An overdue run is attempted on a later check when the Mac is available. Multiple missed cycles are covered by one current catch-up report, not fabricated historical reports.

Each report uses its actual execution date and records `Scheduled for` separately. The runner resumes an interrupted same-day report, prevents concurrent runner instances, and records success only after Codex exits successfully and the expected report contains the scheduled occurrence. This records delivery, not the quality or human approval of the review. A failed run remains due for a later check. Human review remains `In Progress`.

### Local operation and verification

- **Installed job:** `/Users/paulcanaan/Library/LaunchAgents/church.goldencity.groups-biweekly-review.plist`; source copy in `scripts/`.
- **Check due state without running:** `/usr/local/bin/python3 scripts/biweekly_review.py --check` from the repository root.
- **Run a due review now:** `/usr/local/bin/python3 scripts/biweekly_review.py` from the repository root, or `launchctl kickstart gui/501/church.goldencity.groups-biweekly-review` for this Mac.
- **Check job:** `launchctl print gui/501/church.goldencity.groups-biweekly-review`.
- **Pause job:** `launchctl bootout gui/501/church.goldencity.groups-biweekly-review`; restore with `launchctl bootstrap gui/501 /Users/paulcanaan/Library/LaunchAgents/church.goldencity.groups-biweekly-review.plist`.
- **Local evidence:** `.review-runtime/last-success.json`, `last-run.log`, and `last-message.txt`; runtime files are ignored by Git. Agent output is replaced on each actual attempt; canonical dated reports are preserved.
- **Delivery destination:** `09 Reports/Biweekly Reviews/` inside this repository, which is already inside the open Golden City Church Obsidian vault. No second vault copy or Git pull is needed for this local job.
- **Acceptance:** verify the loaded job, a successful due run, its actual report and dashboard/index links, and an idle second invocation before closing BWR-013. An empty application automation registry does not describe this LaunchAgent.

Do not enable a desktop Scheduled task alongside this job. If desktop scheduling becomes available, pause the LaunchAgent before switching, preserve the same procedure and time zone, and verify delivery in the actual vault. The earlier desktop-only setup required the app to remain running; see [OpenAI scheduled-task documentation](https://learn.chatgpt.com/docs/automations). The fallback uses [macOS launchd](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html).

### Durable scheduled-task prompt

> Run the sole recurring review procedure in `07 Operations/Workflows/Biweekly Ministry Review.md` for the current first- or third-Monday review. Read `AGENTS.md`, the governing sources named there, the newest completed biweekly report, `00 Dashboard/Inbox.md`, and `00 Dashboard/Biweekly Review Queue.md` before editing. Create the dated report from `10 Templates/Reports/Biweekly Ministry Review Report.md` with metadata, current emphasis, and the canonical execution checklist; leave it `In Progress` until required human review is complete. Review meaningful repository changes, every queue item, past events, stale TODOs, the next two to four weeks, the leader pipeline, every ministry environment, readiness, blockers, and decisions supplied by Paul, Russ, or staff. Check an execution item only after inspecting its source, reconciling changes, writing back where needed, and routing missing evidence or human input. Preserve every unresolved item; distinguish facts, recommendations, expressed interest, appointments, and approvals; update canonical sources before dashboards; archive resolved evidence; include only queue-backed priority actions; and refresh the primary dashboard. Keep confidential participant, leader-assessment, pastoral, screening, and safeguarding details out of the repository. Leave changes reviewable and do not commit, publish, message people, or infer approvals.

## Review Report Structure

Create the dated report from [[10 Templates/Reports/Biweekly Ministry Review Report|the report template]], apply this procedure, and preserve every unresolved item in the existing queue.

## Operating Boundaries

- **[[00 Dashboard/Inbox|Inbox]]:** temporary intake and triage; not a durable task list.
- **[[00 Dashboard/Biweekly Review Queue|Biweekly Review Queue]]:** persistent unresolved operational work carried across reviews.
- **[[00 Dashboard/Groups Ministry Dashboard|Groups Ministry Dashboard]]:** executive current-state control surface.
- **[[00 Dashboard/Launch Readiness Dashboard|Launch Readiness Dashboard]]:** implementation evidence, blockers, ownership, and controlled readiness status.
- **[[00 Dashboard/Staff Decision Brief|Staff Decision Brief]]:** proposals and matters needing staff or pastoral direction.
- **[[00 Dashboard/Open Decisions|Open Decisions]]:** unresolved governing questions; not approval.
- **[[00 Dashboard/Decision Log|Decision Log]]:** approved current direction and canonical register.
- **[[08 Archive/Decisions/Decision History|Decision History]]:** full evidence, implications, boundaries, and historical traceability.
- **Biweekly Review report:** dated evidence of what was inspected, reconciled, learned, written back, and carried forward; also the human-review interface.

## Connections

- [[00 Dashboard/Biweekly Review Queue|Biweekly Review Queue]] — single carry-forward queue.
- [[09 Reports/Biweekly Reviews/Biweekly Review Index|Biweekly Review Index]] — completed review history.
- [[00 Dashboard/Groups Ministry Dashboard|Groups Ministry Dashboard]] — current operational summary.
- [[00 Dashboard/Launch Readiness Dashboard|Launch Readiness Dashboard]] — detailed readiness evidence and critical path.
- [[08 Archive/Operations/Weekly Review|Superseded Weekly Review]] — preserved historical checklist whose useful functions are incorporated here.
- [[00 Dashboard/Decision Log|Decision Log]] — approved direction.
- [[00 Dashboard/Staff Decision Brief|Staff Decision Brief]] — proposals and staff-meeting direction awaiting canonical capture.
