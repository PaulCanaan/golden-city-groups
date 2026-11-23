# Weekly Recap Production

## Document Status

**Working procedure recorded October 7, 2026 from Paul's direction under DEC-055 (owners and content) and DEC-057 (leaders' Church Center chat); see the DEC-055 clarification of October 7.** Russ sends the Sunday sermon script on Sunday afternoon, an AI agent drafts the recap, and Paul reviews, approves, and posts it to the All Group Leaders chat on Sunday evening. Paul approves under his own pastoral authority; Russ can read any recap at any time and does not pre-approve them. Finished recaps are published resources kept in the repository. Since October 25, 2026 (Paul's direction), each approved recap is also added to the public [[12 Ministry Website/Resources Page|Groups resources page]] after Paul's review. On October 26, 2026, Paul moved the scheduled drafting task to a single Sunday run at 6:00 PM.

**Amendment, November 18, 2026 (Paul's direction):** a research step now sits between receiving the script and drafting. It follows group feedback Paul received on November 17, 2026: the recaps can go beyond the Sunday message so groups can dive deeper into the week's specific topic (his example: faithfulness, Week 7). The research runs on Paul's `research` skill and produces a theme brief before drafting begins. The Message summary remains faithful to the script alone; research adds depth on the theme — additional verified passages and deeper questions — and is never attributed to the message.

**Open:** Paul confirms who can cover the Sunday handoff and in what capacity (BWR-030). If Paul is unavailable and no approved backup has been recorded, keep the draft and checked PDF ready and mark approval, posting, or release as pending. The *Weekly Recap Draft* task still runs its earlier prompt (now at 6:00 PM), which drafts and reports but has no Publish stage; the updated prompt kept in the Claude project as *Weekly Recap Task Prompt* still needs to be pasted into the task in the Claude desktop app, with the Sanity and Vercel connectors attached. Until then, ask Claude in a chat that has those connectors to publish a reviewed recap.

## Purpose and Ownership

Carry the weekend message into the week so City Groups that choose the recap can share life, attend to Christ in his Word, and respond faithfully together. The recap is not a repeat of the Sunday message: it is a guided study and discussion built on top of a summary of the message (Paul, November 18, 2026) — the summary carries the message faithfully, and the study and discussion lead the group deeper into its theme. The recap remains optional for leaders (DEC-052, DEC-055).

**Owner:** Paul for production, approval, and delivery; Russ supplies the script and may review any recap after the fact. **Start:** Russ's sermon script arrives on Sunday afternoon. **Finish:** the recap PDF is posted in the All Group Leaders chat on Sunday evening, the Markdown record is marked `Posted` and committed, and the recap is live on the resources page.

## Process Map

| Stage | When | Who | Action | Completion / next step |
|---|---|---|---|---|
| Receive | Sunday afternoon | Russ → Paul | Russ sends the sermon script. | Paul has the script. |
| Drop | Sunday afternoon | Paul | Save it to the [[06 Resources/Resource Inbox/Resource Inbox\|Resource Inbox]] as `YYYY-MM-DD Message Title`. | The script is waiting in the inbox. |
| Research | Sunday afternoon | AI agent | Run the `research` skill on the message's theme: a brief with the theme in one line, 2–3 additional passages (CSB text verified), background, and candidate deeper questions — keeping what the message said and what research adds clearly separate. | The theme brief is saved with the week's work files. |
| Draft | Sunday afternoon or evening | AI agent | Run `/weekly-recap`, drafting from the script and the brief. It writes the Markdown record and the PDF, then moves the script to `Processed/`. | A `Draft` recap and its PDF exist. |
| Review | Sunday evening | Paul | Edit the Markdown, rebuild the PDF if anything changed, and check it against the list below. | Paul is satisfied it is ready. |
| Post | Sunday evening | Paul | Attach the PDF in the All Group Leaders chat with the short message below. | Set `status: Posted` and `posted:` to the date. |
| Record | After posting | Paul | Commit the Markdown record. | The recap is in the repository. |
| Publish | After Paul's review | AI agent, at Paul's word | Add the reviewed recap to the resources page (step 6 below). | The recap is live at `resources.goldencity.church`. |

## Reminders

A launchd job (`scripts/church.goldencity.groups-weekly-recap-reminder.plist`) runs `scripts/weekly_recap.py remind` at **5:00 PM and 8:00 PM every Sunday** and shows a Mac notification when something is still waiting:

| What it finds for that Sunday | Reminder |
|---|---|
| No script in the Resource Inbox and no recap | Drop Russ's script in the Resource Inbox. |
| A script but no recap | Run `/weekly-recap`. |
| A recap not yet marked `Posted` | Post this week's recap. |
| A recap marked `Posted` | Nothing. |

`python3 scripts/weekly_recap.py check` prints the current state without notifying. The job only runs while the Mac is on; if it is asleep at the scheduled time, the reminder appears when it wakes.

**Scheduled drafting (Claude, added 2026-10-11 at Paul's request; one 6:00 PM run since 2026-10-26):** a Claude scheduled task, *Weekly Recap Draft*, checks the Resource Inbox at **6:00 PM every Sunday**, between the 5:00 and 8:00 PM reminders. When a script is waiting and no recap exists for that Sunday, it follows the `weekly-recap` skill: it writes the `Draft` record, builds the PDF with this repository's renderer, moves the script to `Processed/`, and sends Paul the PDF with its notes. If no script has arrived by 6:00 PM, it sends a one-line nudge; once the script is in the Resource Inbox, Paul replies in that task's session and it drafts then. There is no later automatic check that evening. It never posts, commits, or marks a recap `Posted`, so the Review, Post, and Record stages are unchanged. With its updated prompt in place (see **Open** above), when Paul replies in that task's session that the recap is reviewed and ready, it carries out the Publish stage (step 6). The task's full intended prompt is kept in the Golden City Groups Claude project as *Weekly Recap Task Prompt*; changing the task itself needs Paul's approval in the Claude desktop app. It needs the Mac awake with the Claude desktop app open. Running `/weekly-recap` by hand still works, and the task skips any Sunday that already has a recap.

## Detailed Steps

### 1. Drop the script

Save the file Russ sends (Word, PDF, text, or Markdown) into `06 Resources/Resource Inbox/`, named with the Sunday date: `2026-10-11 Message Title.docx`. Export other formats (Pages, a Google Doc link) to Word or PDF first.

### 2. Research the theme

After the script is dropped and before drafting, the agent runs the `research` skill on the message's theme and saves a working brief with the week's recap work files (not committed, not published):

- the theme in one line, in the message's own terms;
- 2–3 additional passages on that theme, each with its CSB text verified against a source actually opened, and a line of background for each;
- candidate deeper questions drawn from those passages, in the recap's question style (short, one idea each, phrased as a person asks aloud);
- any correction to the source (a wrong reference, a misnamed book) and anything unverified, flagged at the top of the brief — never smoothed over.

The brief keeps a hard line between what the message said and what research adds. Research never speaks for Russ, and nothing in the brief is attributed to the sermon.

### 3. Run the agent

In Claude Code, run `/weekly-recap`. In Codex, use `$weekly-recap`. Any other agent: "Follow `.agents/skills/weekly-recap/SKILL.md`." The agent drafts from the script and the research brief: the Message summary stays faithful to the script alone, and research material may deepen Read Together and Discuss within the existing caps (two Check In, four Discuss). The agent writes:

- `06 Resources/Group Life/Weekly Recaps/YYYY-MM-DD Message Title.md`: the record, kept in the repository.
- The same name as `.pdf`: the copy for the chat, built by `scripts/weekly_recap.py pdf` (requires Google Chrome). PDFs are not committed.

It reports anything it was unsure of or left out in its reply rather than in the file, since the record is public. It never posts, sends, commits, or marks a recap `Posted`.

### 4. Review

- [ ] The summary is faithful to what Russ actually preached; it adds no doctrine, application, or emphasis the message did not carry.
- [ ] Everything beyond the message traces to the research brief, reads as the group's own deeper study of the theme, and is nowhere attributed to the sermon.
- [ ] Every passage added by research is verified CSB text, and the brief's corrections and unverified items are resolved or the material is cut.
- [ ] The summary gives context to someone who missed Sunday without reproducing the sermon.
- [ ] Every question works for a group that did not hear the message, using only the page and the passages (Russ, October 7).
- [ ] No names, personal stories, or pastoral details from illustrations appear unless they are clearly fine to repeat publicly.
- [ ] Questions are open, conversational, and six in total (two Check In, four Discuss), including one about what might get in the way.
- [ ] Message title, series, and passage reference are correct.
- [ ] It reads in a warm, pastoral voice rather than a curriculum voice.

If you edited the Markdown, rebuild the PDF: `python3 scripts/weekly_recap.py pdf "06 Resources/Group Life/Weekly Recaps/<file>.md"`, or ask the agent to.

### 5. Post and record

Attach the PDF in the All Group Leaders chat with a short note:

> Here's this week's Weekly Recap from Sunday's message, "{Message Title}." Use whatever serves your group.

The recap is for every current leader in that chat; it is shaped for City Groups, but any leader may use it. Then set `status: Posted` and `posted: YYYY-MM-DD` in the record and commit it, for example `docs(groups): add Weekly Recap for 2026-10-11`.

### 6. Publish to the resources page

Added October 25, 2026 at Paul's direction. Only a recap Paul has reviewed is published; a draft never goes on the page. Paul's word that it is ready (for example, replying "approved" or "publish it") is the trigger.

Use the [[07 Operations/Workflows/Website Publication and Maintenance#Groups Resources Release|shared Groups Resources release checks]]. The current recap entry uses Sanity project `1consdwv` and dataset `production` with these fields:

- `_id` `weekly-recap-YYYY-MM-DD`, title `Weekly Recap · {Message Title}`, and slug `weekly-recap-YYYY-MM-DD-{title-lowercase}`.
- Category `city-groups`, kind `Discussion guide`, audience `everyone`, message date, series and the week's Scripture from the record.
- Summary `The {Month D, YYYY} message recap, with check-in questions, Scripture, discussion, and prayer.`
- Body from `## Check In` through the final Pray list, omitting frontmatter and the title. Attach the approved PDF as `weekly-recap-YYYY-MM-DD-{title}.pdf` with `publicDistribution: true`.

Rebuild `gcc-groups-resources` under the `paul-canaan` team and verify the public result. Keep `public_publication_approved:` for Paul's approval date. Record the verified release in `public_released:` and `public_url:`, share the verified link with Paul, and record the entry, file URL, hash, deployment, and verification in the existing website `.sanity/publication-YYYY-MM-DD.json` record. Mark `posted:` only for confirmed leader-chat delivery.

If the Sanity or Vercel connector is unavailable, preserve the reviewed edition and record which release step remains pending for Paul.

## Exceptions

- **No script** (guest preacher, special service, script unavailable): Paul decides whether to draft from notes or the recording, or skip the week. If skipping, a one-line note in the chat lets leaders know.
- **Late script:** if the recap cannot go out Sunday evening, a short chat note keeps leaders from waiting.
- **Biweekly groups** receive two recaps between gatherings; their leaders choose which to use.

## Tools and Storage

| Item | Location | In version control? |
|---|---|---|
| Russ's scripts | `06 Resources/Resource Inbox/`, then `Processed/` | No; local-only |
| Research briefs | With the week's recap work files (agent workspace) | No; working material |
| Resources page entries | Sanity `1consdwv/production`; site code in `06 Resources/Resources Page/` (its own `gcc-groups-resources` repo) | Site code yes, in its own repository; entries live in Sanity |
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
- Research material is the group's deeper study, never the preacher's words: it is not attributed to the message, and the brief itself is never published.
- Russ's sermon scripts stay out of the repository; only the finished recap is published.
- This page sets no new review cadence. Unresolved items carry through [[00 Dashboard/Biweekly Review Queue|BWR-030]].

## Connections

- [[06 Resources/Group Life/Weekly Recaps|Weekly Recaps]] — purpose and leader use.
- [[10 Templates/Gatherings/Weekly Recap|Weekly Recap template]] — structure and record format.
- [[06 Resources/Resource Inbox/Resource Inbox|Resource Inbox]] — where scripts are dropped.
- [[07 Operations/Workflows/Ministry Communication Workflow|Ministry Communication Workflow]] — channels.
- [[07 Operations/Workflows/Bible Study|Scripture and Sermon Discussion]] — how leaders facilitate.
