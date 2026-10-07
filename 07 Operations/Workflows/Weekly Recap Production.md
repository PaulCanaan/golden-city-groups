# Weekly Recap Production

## Document Status

**Working procedure recorded October 7, 2026 from Paul's direction under DEC-055 (owners and content) and DEC-057 (leaders' Church Center chat); see the DEC-055 clarification of October 7.** Russ sends the Sunday sermon script on Sunday afternoon, an AI agent drafts the recap, and Paul reviews, approves, and posts it to the All Group Leaders chat on Sunday evening. Paul approves under his own pastoral authority; Russ can read any recap at any time and does not pre-approve them. Finished recaps are published resources kept in the repository.

**Open:** backup coverage when Paul is unavailable.

## Purpose and Ownership

Carry the weekend message into the week so City Groups that choose the recap can share life, attend to Christ in his Word, and respond faithfully together. The recap remains optional for leaders (DEC-052, DEC-055).

**Owner:** Paul for production, approval, and delivery; Russ supplies the script and may review any recap after the fact. **Start:** Russ's sermon script arrives on Sunday afternoon. **Finish:** the recap PDF is posted in the All Group Leaders chat on Sunday evening, and the Markdown record is marked `Posted` and committed.

## Process Map

| Stage | When | Who | Action | Completion / next step |
|---|---|---|---|---|
| Receive | Sunday afternoon | Russ → Paul | Russ sends the sermon script. | Paul has the script. |
| Drop | Sunday afternoon | Paul | Save it to the [[06 Resources/Resource Inbox/Resource Inbox\|Resource Inbox]] as `YYYY-MM-DD Message Title`. | The script is waiting in the inbox. |
| Draft | Sunday afternoon or evening | AI agent | Run `/weekly-recap`. It writes the Markdown record and the PDF, then moves the script to `Processed/`. | A `Draft` recap and its PDF exist. |
| Review | Sunday evening | Paul | Edit the Markdown, rebuild the PDF if anything changed, and check it against the list below. | Paul is satisfied it is ready. |
| Post | Sunday evening | Paul | Attach the PDF in the All Group Leaders chat with the short message below. | Set `status: Posted` and `posted:` to the date. |
| Record | After posting | Paul | Commit the Markdown record. | The recap is in the repository. |

## Reminders

A launchd job (`scripts/church.goldencity.groups-weekly-recap-reminder.plist`) runs `scripts/weekly_recap.py remind` at **5:00 PM and 8:00 PM every Sunday** and shows a Mac notification when something is still waiting:

| What it finds for that Sunday | Reminder |
|---|---|
| No script in the Resource Inbox and no recap | Drop Russ's script in the Resource Inbox. |
| A script but no recap | Run `/weekly-recap`. |
| A recap not yet marked `Posted` | Post this week's recap. |
| A recap marked `Posted` | Nothing. |

`python3 scripts/weekly_recap.py check` prints the current state without notifying. The job only runs while the Mac is on; if it is asleep at the scheduled time, the reminder appears when it wakes.

## Detailed Steps

### 1. Drop the script

Save the file Russ sends (Word, PDF, text, or Markdown) into `06 Resources/Resource Inbox/`, named with the Sunday date: `2026-10-11 Message Title.docx`. Export other formats (Pages, a Google Doc link) to Word or PDF first.

### 2. Run the agent

In Claude Code, run `/weekly-recap`. In Codex, use `$weekly-recap`. Any other agent: "Follow `.agents/skills/weekly-recap/SKILL.md`." The agent writes:

- `06 Resources/Group Life/Weekly Recaps/YYYY-MM-DD Message Title.md`: the record, kept in the repository.
- The same name as `.pdf`: the copy for the chat, built by `scripts/weekly_recap.py pdf` (requires Google Chrome). PDFs are not committed.

It reports anything it was unsure of or left out in its reply rather than in the file, since the record is public. It never posts, sends, commits, or marks a recap `Posted`.

### 3. Review

- [ ] The summary and every question are faithful to what Russ actually preached; nothing adds doctrine, application, or emphasis the message did not carry.
- [ ] The summary gives context to someone who missed Sunday without reproducing the sermon.
- [ ] Every question works for a group that did not hear the message, using only the page and the passages (Russ, October 7).
- [ ] No names, personal stories, or pastoral details from illustrations appear unless they are clearly fine to repeat publicly.
- [ ] Questions are open, conversational, and about six to eight in total, including one about what might get in the way.
- [ ] Message title, series, and passage reference are correct.
- [ ] It reads in a warm, pastoral voice rather than a curriculum voice.

If you edited the Markdown, rebuild the PDF: `python3 scripts/weekly_recap.py pdf "06 Resources/Group Life/Weekly Recaps/<file>.md"`, or ask the agent to.

### 4. Post and record

Attach the PDF in the All Group Leaders chat with a short note:

> Here's this week's Weekly Recap from Sunday's message, "{Message Title}." Use whatever serves your group.

The recap is for every current leader in that chat; it is shaped for City Groups, but any leader may use it. Then set `status: Posted` and `posted: YYYY-MM-DD` in the record and commit it, for example `docs(groups): add Weekly Recap for 2026-10-11`.

## Exceptions

- **No script** (guest preacher, special service, script unavailable): Paul decides whether to draft from notes or the recording, or skip the week. If skipping, a one-line note in the chat lets leaders know.
- **Late script:** if the recap cannot go out Sunday evening, a short chat note keeps leaders from waiting.
- **Biweekly groups** receive two recaps between gatherings; their leaders choose which to use.

## Tools and Storage

| Item | Location | In version control? |
|---|---|---|
| Russ's scripts | `06 Resources/Resource Inbox/`, then `Processed/` | No; local-only |
| Recap records (Markdown) | `06 Resources/Group Life/Weekly Recaps/` | Yes; published resources |
| Recap PDFs | Same folder | No; regenerated from the record |
| Agent instructions | `.agents/skills/weekly-recap/SKILL.md` (linked for Claude Code at `.claude/skills/`) | Yes |
| PDF builder and reminder | `scripts/weekly_recap.py` and its launchd plist | Yes |
| Structure | [[10 Templates/Gatherings/Weekly Recap\|Weekly Recap template]] | Yes |
| Look of the PDF | [[06 Resources/Brand/Groups Resource Style\|Groups Resource Style]]; logo and Roboto fonts in `06 Resources/Brand/` | Yes |

## Boundaries

- The recap is optional; no leader is evaluated by whether or how much of it they use (DEC-052, DEC-055).
- An AI draft is never released without Paul's review. Approval and posting are human acts.
- Do not put sensitive pastoral, safeguarding, or participant information in the recap, the chat, or this vault (DEC-028).
- Do not write words on Russ's behalf. Quote the script only verbatim and sparingly; describe the message rather than speaking for him.
- Russ's sermon scripts stay out of the repository; only the finished recap is published.
- This page sets no new review cadence. Unresolved items carry through [[00 Dashboard/Biweekly Review Queue|BWR-030]].

## Connections

- [[06 Resources/Group Life/Weekly Recaps|Weekly Recaps]] — purpose and leader use.
- [[10 Templates/Gatherings/Weekly Recap|Weekly Recap template]] — structure and record format.
- [[06 Resources/Resource Inbox/Resource Inbox|Resource Inbox]] — where scripts are dropped.
- [[07 Operations/Workflows/Ministry Communication Workflow|Ministry Communication Workflow]] — channels.
- [[07 Operations/Workflows/Bible Study|Scripture and Sermon Discussion]] — how leaders facilitate.
