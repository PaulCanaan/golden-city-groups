# Proposed Planning Center Workflows

## Document Status

**Proposed — nothing in this document is implemented or approved.** *Implementation record (November 20, 2026): Paul approved and Baby Fish executed Part 1 items 1, 1b, 2, 4, 6, 7, 8, 9, and 10 the same evening (item 5 is a standing decision, not an action); the overdue-marking items 3 and 11 were left unapproved and remain proposed. Part 2 workflow A (Leader Development & Multiplication) was built November 20, 2026; workflows B and C remain proposed.* Prepared November 20, 2026 from a live, read-only audit of Paul's Planning Center account the same day and from the operating knowledge in the ministry's Planning Center records. Paul reviews; any change to a live workflow, form, or card happens only on his explicit approval of that specific change. Appointment and readiness authority remain with Russ as elsewhere in this vault.

## Purpose

Fix what is stale or fragile in the two live People workflows, then add workflow support where the Groups & Classes ministry is actually growing: leader multiplication toward Spring 2027, the first-30-days support of new groups, and season transitions. Planning Center mechanics assumed throughout (verified live): workflow steps are manual "assign to a person" actions unless a step automation is configured; "Mark overdue after" is per-step; form routing into workflows happens through workflow fields on forms; cards belong to people, never to groups.

## Part 1 — Fixes to the current workflows

### Small Group Leader Application (10 open cards at audit)

1. **Complete the finished pipeline.** The 5 cards at Small Group Launched belong to leaders whose groups launched in the fall — that stage is workflow completion, so the cards should be Completed. The 2 cards at Attended Training belong to leaders who are also now leading groups; advance them through Launched and Complete them. Effect: 10 open cards → 3. *Verified November 20, 2026 against the public Fall 2026 roster (goldencity.church/groups/fall2026, the roster source of truth): all 7 leaders are listed leading groups that began in October.*
1b. **Backfill the missing leader records.** The same roster check found six people publicly leading Fall 2026 groups (the Erie City Group pair, the Run Club pair, and the co-leaders of the Westminster City Group and the Women's Collective) who have **no card in this workflow at all** — neither open nor completed. Add a card for each and complete it, so the pipeline record matches who actually leads. Whether any of them passed through cards later removed is itself part of the record gap.
2. **Decide the remaining 3, one by one.** One card has sat at Interviewed since early September (advance, pause with a note, or remove — Paul's call). One Welcome-stage card is an October Serve Team Interest submission awaiting a decision. One Welcome-stage card is the last residue of the Connection Card misrouting: a Launch Sunday newcomer whose contact details are now on file — send the participant Groups Introduction (the fixed template, through the usual email checks), remove the leader-workflow card, and let Find a Small Group be the home if placement follow-up is wanted.
3. **Turn on overdue marking.** "Mark overdue after" is off on every step, which is why September cards sat invisibly for months. Proposed: 7 days at Welcome Email / Call, 14 days at Interviewed and Attended Training, 7 days at Small Group Launched.
4. **Write the step descriptions.** Every step's description field is empty. One line per step, taken from the advance conditions in [[07 Operations/Workflows/Planning Center Groups#3. Move prospective leaders from intake to launch|Planning Center Groups §3]], so each card states what "done" means at its stage.
5. **Do not automate the welcome send.** Planning Center can send an email automatically when a card enters a step, but the Welcome step's work is a personal coffee invitation written to the person; an auto-send would break that pattern and the ministry's send-approval practice. The manual step plus the overdue flag is the right level of automation here.

### Lead a Group form (the routing field)

6. **Make the group-type dropdown required.** Today it is optional, and a submission that skips it creates no workflow card — a leader-interest submission can be silently lost.
7. **Check "Skip people who have already started or completed this workflow"** on every option. The workflow's removed-card history is full of duplicate cards from repeat submissions.
8. **Pin the assignment** to the Groups Director explicitly instead of relying on the workflow's default assignee, so a future default change cannot reroute new cards silently.

### Find a Small Group (1 open card at audit)

9. **Fix the step-name spelling:** "Intersted in a Group" → "Interested in a Group."
10. **Close the open card's loop.** Its person joined a group in late October; move the card to Connected to a Group and complete it. The workflow has never had a completed card.
11. **Turn on overdue marking (7 days).** Participant interest is the most time-sensitive queue in the ministry; the proposed one-business-day response target during signup windows needs a visible stall signal.

### Not Paul's to fix

12. **The Connection Card routing (BWR-021)** still belongs to Russ or an organization administrator; the November 20 audit confirms the form still does not appear in Paul's account. Nothing in Part 1 depends on it once fix 2 clears the last misfiled card.

## Part 2 — New workflows for growth

### A. Leader Development & Multiplication (Spring 2027)

- **Serves:** the Spring 2027 objective in [[07 Operations/Workflows/Semester Planning|Semester Planning]] — expand intentional leader development and multiplication, integrating the four-session CoJourner pathway.
- **Cards:** current group leaders Paul invites into the pathway (invitation-only; Paul adds cards by hand, so discernment stays human and no form implies a public pathway).
- **Steps:** Invited → In the Pathway → Apprentice Identified → New Group Planned → (Completed at the new group's launch, handing off to workflow B).
- **Owner:** Paul. Overdue marking on (14 days) so a stalling multiplication conversation surfaces before the February launch window, not after.
- **Replaces:** ad hoc memory and conversation. Multiplication is a months-long pipeline across many leaders; the board is what makes "who is stuck where" visible at a glance. This is the one new workflow with a clear growth payoff.

### B. New Group First 30 Days

- **Serves:** the support rhythm in [[07 Operations/Workflows/Leader Support Check-In|Leader Support Check-In]] — a personal connection before the first meeting, a check-in after the first gathering, periodic contact, timely response when a leader asks for help.
- **Cards:** the leader of each newly launched group, started by Paul when a Leader Application card completes.
- **Steps:** Launched → First Gathering Confirmed → Week 2 Check-In → Week 4 Check-In → Steady State (Completed).
- **Owner:** Paul. Overdue marking on (7 days per step).
- **Replaces:** memory and scattered notes for the highest-risk month of a group's life. It is the tracking layer for the support rhythm, not a new care model, and it records only operational follow-up — never pastoral detail (the support workflow's recordkeeping boundary applies).

### C. Season Transition

- **Serves:** the February and September launch rhythm (DEC-080) and leader retention across seasons — a group continues when its leader is carried through the transition on purpose.
- **Cards:** every current group leader, added by Paul about a month before a season ends.
- **Steps:** Season Ending → Transition Conversation → Next Season Confirmed (relaunch, rest, or hand over) → Completed.
- **Owner:** Paul.
- **Replaces:** rollover handled from memory and calendar each season. Runs twice a year; between runs the workflow sits empty, which is fine.

### Candidates considered and not proposed

- **A per-member welcome workflow for every group join.** Join requests already land with group leaders in Groups, and Planted carries its own approved welcome path. A People workflow card for every new member would duplicate both, add manual card creation at the exact moment of growth, and drift toward tracking people rather than supporting leaders. The manual route wins.
- **A separate class-participant workflow.** Planted is the only live class and has its own intake and communication workflow. When a second class launches, reuse workflow B's shape for its leader and Planted's pattern for participants rather than building a class workflow now.

## Boundaries

- A workflow card is not an appointment, an approval, or a measure of anyone's faithfulness; movement records operational progress only.
- No card, step, or note carries pastoral, safeguarding, or discernment detail (DEC-028 boundaries apply).
- Every workflow above keeps a single named owner; backup coverage for the leader pipeline remains an open decision for Paul and Russ, not something a workflow setting can settle.

## Connections

- [[07 Operations/Workflows/Planning Center Groups|Planning Center Groups]] — the governing platform procedure this proposal amends.
- [[07 Operations/Workflows/Forms|Forms]] — intake triggers and the routing field.
- [[07 Operations/Workflows/Semester Planning|Semester Planning]] — the Spring 2027 multiplication objective behind workflow A.
- [[07 Operations/Workflows/Leader Support Check-In|Leader Support Check-In]] — the support rhythm behind workflow B.
