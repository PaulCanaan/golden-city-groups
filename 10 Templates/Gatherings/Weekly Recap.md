# Weekly Recap

## Document Status

**Canonical structure for an approved optional resource (DEC-055).** Check-in questions and discussion questions come from DEC-055. The order (check-in, then a summary for those who missed the message, then discussion), Sunday-evening delivery as a PDF, and the Markdown record come from Paul's October 7, 2026 direction (DEC-055 clarification). The standalone rule below comes from Russ's feedback on the first recap, relayed by Paul on October 7, 2026. Production steps live in [[07 Operations/Workflows/Weekly Recap Production|Weekly Recap Production]].

## Purpose and Use

Prepare a concise resource from the weekend message that serves community, Scripture, prayer, and faithful response. City Group leaders may choose whether to use it.

- **Owner:** Russ and Paul under DEC-055; Paul approves and posts.
- **Trigger:** Russ's sermon script for the weekend message is in the [[06 Resources/Resource Inbox/Resource Inbox|Resource Inbox]].
- **Variables / inputs:** message date, title, series, primary passage, central emphasis, main movements of the message.

## Shape

The recap follows the movement of a gathering: people arrive and are known, attend to Christ in his Word, and turn toward faithful response.

| Section | Contents | Serves |
|---|---|---|
| **Check In** | One or two questions about how people's week has actually gone. Lightly connected to the message at most; no preparation required. | Belonging |
| **This Week's Message** | About 120–180 words: the central emphasis and main movement of the message, so everyone, including anyone who missed it, can join the conversation. Context, not a reproduction of the sermon. | Beholding |
| **Read Together** | The primary passage reference, read aloud from the group's Bibles. | Beholding |
| **Discuss** | Four or five open questions: what stands out in the passage → what the text shows us of God in Christ → how it meets ordinary life, relationships, service, or witness → what might get in the way of that response. | Beholding → Becoming |
| **Pray** | One prompt drawn from the message. | Becoming |

**Usable without hearing the message.** A group must be able to use the recap with only this page and their Bibles. Every Discuss question draws on the Read Together passages or on something the summary itself explains; none asks what people remember or took away from Sunday.

**Launch season (October 2026, until Paul says otherwise):** groups are still getting to know one another, so give a little more room to fellowship and a little less to study: two Check In questions that help people know each other, and three or four Discuss questions (Paul, October 7, 2026).

Keep the total to about six to eight questions. The guide should invite conversation rather than test recall, require prior study, or turn the leader into a lecturer. The preaching has already done most of the observation and interpretation; group time moves toward shared reflection and response.

## Record Format

Each recap is one Markdown file, `06 Resources/Group Life/Weekly Recaps/YYYY-MM-DD Message Title.md`. It is the published record in the repository and the source for the chat PDF (`scripts/weekly_recap.py pdf`), so keep to this shape: `#` for the title, `##` for sections, numbered lines for questions, plain paragraphs otherwise.

```markdown
---
record_type: weekly-recap
message_date: YYYY-MM-DD
message_title: "{Message Title}"
series: "{Series}"
passage: "{Passage}"
status: Draft
posted:
---

# {Message Title}

**Weekly Recap · {Month D, YYYY}** · *{Series}* · {Passage}

## Check In

1. {Question}

## This Week's Message

{120–180 word summary}

## Read Together

{Passage}

## Discuss

1. {What stands out in the passage}
2. {The text and Christ}
3. {The text and Christ, or life}
4. {Ordinary life, relationships, service, or witness}
5. {What might get in the way}

## Pray

{One prompt}

*Use what serves your group; you don't need to get through every question.*
```

`status` moves from `Draft` to `Posted` when Paul shares it; `posted` takes that date.

## Before Use

- [ ] Every summary claim and question is faithful to what was actually preached; no new doctrinal claims.
- [ ] A group that did not hear the message can use every question with only this page and the passages.
- [ ] No names, personal stories, or pastoral details from sermon illustrations that should not be repeated publicly; the record is published.
- [ ] Keep confidential participant, pastoral, screening, and safeguarding details out of the vault and the chat.
- [ ] Record completion only when the action actually occurs; a template grants no approval.

## Connections

- [[06 Resources/Group Life/Weekly Recaps|Weekly Recaps]] — purpose, optional use, and leader guidance.
- [[07 Operations/Workflows/Weekly Recap Production|Weekly Recap Production]] — weekly production and delivery.
- [[07 Operations/Workflows/Bible Study|Scripture and Sermon Discussion]] — facilitation procedure.
