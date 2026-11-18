---
name: weekly-recap
description: Turn Russ's Sunday sermon script in the Resource Inbox into a draft Weekly Recap for Golden City Church group leaders. Use when Paul asks to process, draft, or make this week's Weekly Recap, or when a sermon script is waiting in `06 Resources/Resource Inbox/`.
---

# Weekly Recap

Draft the Weekly Recap from the weekend message so Paul can review it and post it to the All Group Leaders chat in Church Center on Sunday evening. You produce a draft only: a Markdown record for the repository and a PDF for the chat. Paul reviews, approves, and posts. The recap is not a repeat of the message: it is a guided study and discussion built on top of a summary of the message — the summary stays faithful to what was preached, and the study and discussion lead the group deeper into the week's theme.

## 1. Find the script

List `06 Resources/Resource Inbox/`, ignoring `Resource Inbox.md` and `Processed/`. Each remaining file is one unprocessed script named `YYYY-MM-DD Message Title`. If there is none, say so and stop. If there are several, draft each one.

Read it as text:

- `.md`, `.txt`: read directly.
- `.docx`: `textutil -convert txt -stdout "<file>"` on macOS.
- `.pdf`: your PDF reader, or `pdftotext "<file>" -`.
- Anything else: stop and ask Paul to export it to Word or PDF.

## 2. Read the governing material

- `10 Templates/Gatherings/Weekly Recap.md`: the required shape and copy format. Follow it exactly.
- `06 Resources/Group Life/Weekly Recaps.md`: purpose and leader use.
- `07 Operations/Workflows/Weekly Recap Production.md`: the review checklist your draft must survive.

## 3. Understand the message

From the script, identify: the Sunday date (from the filename unless the script says otherwise), message title, series, the week's key passage, the central emphasis in one sentence using Russ's own terms, and the main movements of the message. If any of these is unclear, write your best reading and flag it.

## 4. Research the theme

Before drafting, run Paul's `research` skill on the message's theme and save a working brief with the week's work files:

- the theme in one line, in the message's own terms;
- 2–3 additional passages on that theme, each with CSB text verified against a source actually opened, plus a line of background each;
- candidate deeper questions from those passages, in the recap's question style (short, one idea each);
- corrections to the source and anything unverified, flagged at the top of the brief.

Keep a hard line in the brief between what the message said and what research adds. Research never speaks for Russ and is never attributed to the sermon. The brief is working material: it is not committed and not published.

## 5. Draft

Write the sections in order: Check In, This Week's Message, Read Together, Discuss, Pray. Hold to these rules:

- **Faithful to what was preached.** The Message summary and every claim in it must trace to the script. Add no doctrine, application, cross-references, or emphasis the message did not carry. If the script is thin on something, the summary leaves it thin.
- **Depth comes from the brief, not from drafting.** Read Together and Discuss may go beyond the message on the week's theme — additional passages and deeper questions — using ONLY material from the research brief (step 4): verified, and never attributed to the sermon. Invent nothing at drafting time; if the brief doesn't carry it, the recap doesn't either.
- **Do not speak for Russ.** Describe what the message said ("Sunday's message walked through…"). Quote only verbatim from the script, briefly, and rarely.
- **Christ at the center.** Where the message points to Christ, keep that thread visible in the summary and at least one question. Do not reduce it to moral advice.
- **Context, not reproduction.** The summary is 120–180 words and gives everyone, including anyone who missed Sunday, enough context to join in.
- **Usable without hearing the message.** Every Discuss question must work for a group with only this page and their Bibles. Anchor questions in the Read Together passages or in what the summary explains. Never ask what people remember or took away from Sunday, and don't reference a story or passage the page doesn't supply.
- **Questions invite conversation.** Open, answerable by anyone present, no recall tests, no prior study. Check In is about people's actual week. Include one question about what might get in the way of responding. Six questions in total: two Check In questions and four Discuss questions (Paul, November 2, 2026). Write each question the way a person would actually say it out loud: short, one idea each, contractions and plain words over written, curriculum phrasing.
- **The week's passage first.** Read Together and the record's `passage` field carry the week's key passage(s); a passage added from the research brief may sit alongside the key passage in both (the Faithfulness precedent: Revelation 19:11; Hebrews 11:11). A series key passage (for example Galatians 5:22–23 for the Fruit of the Spirit series) frames the series and is not repeated every week.
- **Subtitle.** The record's subtitle line names the series and, when the series numbers its weeks, the week (`week:` in the front matter) — never the passages.
- **Pray is a list.** The Pray section is a short numbered list of prompts drawn from the message, not a paragraph.
- **Pronouns for God.** Capitalize pronouns that refer to God (He, His, Him) throughout the recap; pronouns for people stay lowercase.
- **No closing line.** The record ends with the Pray list. Do not add a "use what serves your group" line or a note about skipping questions; leaders know how to use the recap.
- **Leave out people.** The record is public. No names, personal stories, or pastoral details from illustrations. No participant or sensitive information of any kind.
- **Keep the record format.** Follow the template's Record Format exactly; the PDF builder only understands `#`, `##`, numbered lines, paragraphs, `**bold**`, and `*italic*`.
- **Paul's voice.** Warm, pastoral, simple. Avoid curriculum or corporate language.

## 6. Write the files

1. Create `06 Resources/Group Life/Weekly Recaps/YYYY-MM-DD Message Title.md` in the template's Record Format, with `status: Draft`. Create the folder if it is missing.
2. Build the PDF: `python3 scripts/weekly_recap.py pdf "<that file>"`. It writes the PDF beside the record. Open or read it to check it rendered on one page.
3. Move the script into `06 Resources/Resource Inbox/Processed/`, creating the folder if it is missing.

## 7. Report and stop

Tell Paul the paths to the record and the PDF, and deliver the research brief alongside the draft so he can see what came from the sermon and what came from research. Give your notes in the reply, not in the file:

- anything uncertain (title, series, passage, central emphasis);
- which elements of the recap came from the research brief;
- anything from the script you deliberately left out, and why (for example, a personal illustration);
- anything Paul may want to adjust before posting.

Remind Paul it is a draft awaiting his review, and that he should rebuild the PDF if he edits the record. Do not:

- set `status` to anything other than `Draft`;
- post, send, or share the recap anywhere;
- `git add` or commit anything. Paul commits the record after posting; scripts and PDFs are gitignored and must never be force-added.

After Paul has reviewed the recap and says it is ready, publish it to the resources page by following step 6 of `07 Operations/Workflows/Weekly Recap Production.md`. Never publish a draft he has not reviewed.
