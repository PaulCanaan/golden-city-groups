# Calendar

Ministry milestones, schedule changes, and review dates. Times are Mountain Time. Open this note in Reading view to see the Dataview calendar and agenda. The agenda lists every event, including days with multiple events.

## Month

```dataview
CALENDAR event_date
FROM "Groups Ministry/07 Operations/Calendar Events" OR "07 Operations/Calendar Events"
WHERE typeof(event_date) = "date"
```

## Key dates

### Upcoming

```dataview
TABLE WITHOUT ID event_date AS Date, file.link AS Event, event_time AS Time, event_status AS Status
FROM "Groups Ministry/07 Operations/Calendar Events" OR "07 Operations/Calendar Events"
WHERE typeof(event_date) = "date" AND event_date >= date(today)
SORT event_date ASC, file.name ASC
```

### History

```dataview
TABLE WITHOUT ID event_date AS Date, file.link AS Event, event_time AS Time, event_status AS Status
FROM "Groups Ministry/07 Operations/Calendar Events" OR "07 Operations/Calendar Events"
WHERE typeof(event_date) = "date" AND event_date < date(today)
SORT event_date DESC, file.name ASC
```

## Add or update an event

Create a note in `07 Operations/Calendar Events` and insert the [[10 Templates/Records/Calendar Event|Calendar Event template]]. Set `event_date` to the confirmed date and `event_status` to `Scheduled`, `Occurred`, `Outcome unrecorded`, or `Skipped`. Add the source to the note. Keep undated plans below until a date is set. When an event is skipped, record what happened and add a replacement once its date is confirmed.

Record only non-sensitive details. The [[07 Operations/Workflows/Biweekly Ministry Review|existing biweekly review]] reconciles dates and outcomes. Planning Center remains the operational source for group meetings.

## Annual rhythm

- [[07 Operations/Annual Rhythm/Annual Calendar|Approved seasonal pattern]] — February–May, June–August, September–early December; January prayer and fasting with optional meetings (DEC-080). The first week is the general planning target for February and September launches. Spring 2027 is set for February 7.
- Group Leader Collaborations: three times a year, before the spring and fall launches and before summer activities (DEC-086, replacing DEC-079's first and third Saturday mornings). The next is the [[07 Operations/Calendar Events/2027-01-30 Group Leader Collaboration|January 30 Group Leader Collaboration]], ahead of the [[07 Operations/Calendar Events/Spring 2027 Launch Day|February 7 Spring Group Launch]].
- [[07 Operations/Annual Rhythm/2026/Fall and Winter 2026]]

## Pending Milestones

- Group Launch Day outcome and October 11 second-presentation decision
- Actual first-gathering outcomes for Erie, Lafayette, Broomfield, Thornton, Westminster, Run Club, and Planted
- Completion of City Group leader discernment and appointment evidence
- Leader training
- Group assignments and location confirmation
- Leader commissioning
- Final launch-readiness review
- Rescheduled Women's Collective Galatians Session 4 and both Collectives' Sessions 5–6
- Planted venue confirmation and complete calendar; a future on-site Collective location

Track open outcomes and decisions through the [[00 Dashboard/Biweekly Review Queue|review queue]].

## Connections

- [[Operation Overview]] — Calendar is a core operations tool for scheduling the ministry year.
- [[07 Operations/Semester Outline]] — Outline provides the structure that key dates on the calendar follow.
- [[07 Operations/Workflows/Group Launch Overview]] — Governs the ordered sequence and readiness requirements behind these dates.
- [[07 Operations/Annual Rhythm/2026/Fall and Winter 2026]] — Current semester rhythm with fall launch items.
- [[Groups Overview]] — Planned group rhythms should be added only after confirmation.
- [[Classes Overview]] — Future Class rhythms should be added only after offering-specific approval.
