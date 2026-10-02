# Group Launch Readiness

From [[Group Launch Overview]] · Part of the [[07 Operations/Group Launches/Group Launch MOC.canvas|Group Launch MOC]]

## Document Status

**Confirmed operational workflow under [[08 Archive/Decisions/Decision History#DEC-059 — Group Launch Readiness Workflow|DEC-059]]; supplied by Paul on October 1, 2026.** It turns a leader who is ready to lead into a Planning Center group, a public listing, and a Launch Sunday table card. Paul owns it under the ministry operations and Planning Center responsibility in DEC-021.

This workflow is **separate from the Group Leader workflow** (DEC-042, `Lead a Group`). That workflow takes a person from interest to readiness; this one starts once a leader is ready and ends when the group first meets. Do not merge their stages.

## Purpose

Help people find a group where they can belong, grow, and follow Jesus together, by giving every ready leader a simple way to describe their group and giving the ministry one reliable path from that description to a group people can join.

## Who Enters This Workflow

A City Group leader enters when they are **ready to lead** for the current semester. A leader is ready to lead when all three are true:

1. **Group Leader Conversation completed.** The coffee conversation looks at where the person is in their spiritual journey (are they spiritually mature enough to lead?) and their season of life (is this a good season for them to lead a group?).
2. **Brief group leader training completed.**
3. **Paul and Russ have decided together**, after talking through how the conversation went, that the person is ready to lead.

Paul records the decision in the restricted system. Names, conversation notes, and discernment details stay out of this repository; report aggregate counts only.

In the Group Leader workflow, this leader has reached **Attended Training**. They reach **Small Group Launched** only at step 9 below.

## The Workflow

```text
Leader is ready to lead (Paul and Russ)
  → 1. Send the City Group Profile form
  → 2. Leader submits (5–10 minutes)
  → 3. Paul reviews and follows up
  → 4. Paul builds the Planning Center group and assigns the leaders
  → 5. Russ reviews before Group Launch Sunday
  → 6. Publish: Church Center listing · "Open Groups" on the Groups webpage · lobby table card
  → 7. Group Launch Sunday (October 4); optional second presentation (October 11)
  → 8. People join; the leader manages the group and shares the details privately
  → 9. First gathering → Small Group Launched (DEC-042)
```

| Step | What happens | Owner | Boundary |
|---|---|---|---|
| **1. Send form** | Paul sends the Church Center form [[#City Group Profile Form\|City Group Profile — Fall 2026]] to each ready leader. | Paul | Only to leaders who are ready to lead. |
| **2. Submit** | The leader completes the profile, ideally with a photo of every leader and co-leader. | Leader | — |
| **3. Review** | Paul checks that the profile is complete, the meeting area is general rather than an address, and the description suits a public profile. Gaps are settled by email or text. | Paul | This is the detail finalization in DEC-051. |
| **4. Build** | Paul creates the Planning Center group from the submission and assigns the leaders, who then manage their own group in Planning Center. | Paul | Follows [[Planning Center Groups#4. Build the group record\|Build the group record]]. Capacity may stay open (see [[#Capacity\|Capacity]]). |
| **5. Review** | Russ does a quick review of the webpage and group profiles before Group Launch Sunday. | Russ | Russ has already approved Paul to make the webpage changes. |
| **6. Publish** | The Church Center listing goes public; the profile appears in the **Open Groups** section of the Groups webpage, linked to its Planning Center group; Paul makes the group's table card. | Paul | Rough location only. Every link and QR code must reach a tested destination (BWR-009). |
| **7. Present** | Leaders present at lobby tables on Sunday, October 4. Groups with many open spots may present again on October 11. | Leaders; Paul | DEC-051. |
| **8. Join** | People join through Church Center. The leader manages the group and shares detailed information, including the address, privately with members, for example in a group chat on Planning Center or Church Center. | Leader | Addresses never appear publicly. Sensitive care details stay out of chats (DEC-028). |
| **9. Launch** | After the group first meets, Paul moves the leader to **Small Group Launched** and updates the group record. | Paul | A group counts as launched only once it has actually met. |

**Each semester:** send the form again. A group's rhythm, resource, environment, and character may change from season to season.

## City Group Profile Form

Church Center form: *City Group Profile — Fall 2026*. Church Center always collects first name, last name, and email address.

**Introduction to leaders (summary):** thanks the leader, affirms their creative freedom to shape the group's rhythm, resource, environment, and character, explains that the profile prepares for Group Launch Sunday on October 4, asks them to have leader photos ready, and reminds them the group need not begin immediately after Launch Sunday.

| Section | Field | Type | Required | Guidance shown |
|---|---|---|---|---|
| Your City Group | Co-Leader(s) | Text | No | Additional leaders to include on the profile |
| | City Group Name & Area | Text | Yes | e.g. *Broomfield City Group* |
| | Group Profile Picture | File (up to 5, 10 MB) | Yes | Clear photo of the leader(s), landscape preferred; may be used on Planning Center, the GCC website, and Group Launch materials |
| When & Where | Frequency | Dropdown | Yes | Weekly · Biweekly · Other |
| | Day of the Week | Dropdown | Yes | Sunday through Saturday |
| | Meeting Time | Text | Yes | e.g. *6:30 PM–8:00 PM*; an approximate end time is fine |
| | General Meeting Area | Text | Yes | e.g. *Broomfield near 120th & Sheridan*; no private home address |
| | Starting Date | Text | Yes | One or two weeks after October 4 is fine |
| Your Group | Primary Group Resource | Dropdown | Yes | GCC Weekly Recap · A Book in the Bible · A Contemporary Christian Book · Devotional · Other Resource · Still Deciding |
| | Resource Details | Text | No | e.g. *Gospel of John*, *Practicing the Way*; may be left blank |
| | Group Features | Checkboxes | No | Young Adults · Young Couples · Families · Parents · Singles · Single Moms · Men · Women · Multigenerational · General / Open to All · Other. Descriptive labels, not requirements for joining |
| | Other Group Feature | Text | No | e.g. *Activity-Based*, *Run Club*, *Group Serving Projects* |
| Help People Get to Know Your Group | Group Description | Text | Yes | 2–4 sentences on what to expect; may appear on the public profile |
| | Anything Else We Should Know? | Text | No | Internal only; does not appear publicly |

The fields follow the design freedom in DEC-052: leaders choose frequency, day, time, materials, and features. The form collects no private address.

### Field use

| Form field | Planning Center group | Open Groups webpage | Table card | Vault group record |
|---|---|---|---|---|
| Name & Area | Group name | Yes | Yes | File name |
| Leader photos | Group image | Yes | Optional | — |
| Frequency, Day, Meeting Time | Schedule | Yes | Yes | `meeting_day`, `meeting_time` |
| General Meeting Area | Public location | Yes | Yes | `location_area` |
| Starting Date | First event | Yes | Optional | `launch_date` |
| Resource and Features | Description or tags | Yes | Optional | — |
| Group Description | Public description | Yes | Optional | — |
| Anything Else | Internal only | No | No | — |

The vault record holds non-sensitive working detail only; leader assignment lives in the record's `leaders` property, and Planning Center remains the system of record.

## Collectives and *Planted.*

Men's Collective, Women's Collective, and *Planted.* do not use the City Group Profile form. Paul prepares their profiles with their leaders. They join this workflow at step 4: they are listed in **Open Groups** on the Groups webpage, have a table card, and are presented in the lobby on Group Launch Sunday.

## Capacity

As the church begins, the aim is to help as many people as possible into groups. Capacity is set in follow-up, when it becomes an issue, rather than at launch. Watch the offerings likely to fill first; Women's Collective already has strong interest.

## Possible City Group Expressions

Run Club and a Young Adults City Group are still under discussion, with people in the church interested in leading and joining each. They sit under City Groups. The window stays open; each would enter this workflow like any other City Group once its leader is ready to lead. Until then, neither is published as an active group (DEC-022).

## Boundaries

- Sending the form does not appoint anyone, and a Planning Center group does not prove readiness. The ready-to-lead decision belongs to Paul and Russ together.
- Never publish an address or detailed location. Leaders share details privately with members.
- Keep conversation notes, discernment details, and participant information in the restricted system, never here.
- Safeguarding policy locations and escalation contacts remain open (BWR-007). The DEC-028 minimum boundaries apply in the meantime, including confirming the applicable safeguards before groups meet in private homes.

## Connections

- [[Group Launch Overview]] — launch sequence this workflow serves.
- [[12 Ministry Website/Open Groups Listings|Open Groups Listings]] — how each profile appears on the Groups page.
- [[Planning Center Groups]] — group build, testing, and publishing procedures.
- [[07 Operations/Forms|Forms and Intake]] — all intake and profile forms.
- [[Communication]] — Group Leader workflow messages; this workflow does not replace them.
- [[Launch Checklist]] — readiness checks before a group is published.
- [[City Groups Overview]] — leader design freedom and features.
- [[10 Templates/Records/Group Record|Group Record template]] — vault working record fields.
- [[00 Dashboard/Biweekly Review Queue|Biweekly Review Queue]] — BWR-028 tracks Launch Sunday preparation.
