# Groups Resource Style

## Document Status

**Working visual style for printable and shareable Groups resources, set October 7, 2026 at Paul's request; length/depth guidance clarified October 13.** It follows goldencity.church (Roboto, a grayscale base, restrained gold; see [[12 Ministry Website/Design Principles and Maintenance|Website Design Principles]]) and the Groups logo Paul supplied. The Weekly Recap PDF is the first resource built to it. Style gives no approval to any resource's content.

## Look in One Line

Neat and quiet: white page, the GROUPS wordmark top left, one thin gold rule, Roboto throughout, small gold section labels, and plenty of space. Gold is an accent, never a fill for whole sections.

## Logo

- `groups-logo.png`: the GROUPS wordmark in emblem gold on a transparent background, for white or light backgrounds.
- Use it once per page, top left, about 19pt tall in letter-size documents. Keep its proportions; don't recolor, outline, or add effects.
- This file is a careful recreation: Montserrat ExtraBold lettering with an "O" redrawn from the Golden City Church city emblem. If an original logo file exists, it replaces this one under the same name. A light version for dark photos has not been made.

## Color

| Use | Color | Note |
|---|---|---|
| Logo, rules, decorative accents | `#CCB079` emblem gold | Too light for text (2.1:1 on white) |
| Small gold text: section labels, list numbers | `#857230` deep gold | 4.7:1 on white |
| Body text and titles | `#1C1C1C` near-black | The website's dark accent |
| Secondary text: dates, series, notes, footer | `#5C5C5C` / `#6B6B6B` gray | |
| Soft panel (one summary block at most) | `#F7F4EC` warm white | |
| Hairlines | `#E2E2E2` | |

`#A99643`, the website's link gold, stays a website treatment.

## Type

Roboto only (files and license in `fonts/`):

- **Title:** 26pt bold, tight tracking (−0.02em).
- **Section labels:** 8pt semibold, uppercase, wide tracking (0.16em), deep gold.
- **Body:** 10.5pt regular, 1.45 line height.
- **Secondary lines:** regular or italic in gray.

## Layout

- Letter size with generous margins; use the resource lengths below rather than forcing every resource onto one page.
- **Header:** logo left; resource name (uppercase label) and date right; a 1.5pt emblem-gold rule beneath.
- **Footer:** hairline, then "Golden City Church · Groups" left and "goldencity.church" right, small gray.
- Numbered questions with deep-gold numerals; no boxes around questions.

## Length and Depth by Ministry Branch

Paul's working guidance of October 13, 2026 keeps one visual family while allowing depth to fit the resource and gathering:

| Resource | Working length | Depth and purpose |
|---|---|---|
| City Groups — Weekly Recap | 1 page | Brief weekend-message connection, check-in/discussion prompts, and room for life together |
| Collectives — separate Men’s and Women’s Galatians participant handouts | 2–3 pages each | Shared biblical study with audience-specific formation goals, actual dates, and clearly marked Block 1/2 teaching and discussion space |
| Bible Clubs — e.g. Planted session notes | 4 pages or more when needed | Sustained biblical study, theological connections, learning movements, reflection, and practice |

These are design targets, not fixed quotas. They serve the branches' different fellowship/discipleship emphases under DEC-053; the ratios stay internal and do not appear in participant-facing resources. Leader notes and slides take the length their function requires. Preserve readable type and writing space rather than shrinking them to hit a page count.

For longer notes, continue the header/footer style across pages, add page numbers, and use clear section breaks. Presentation slides retain the visual family while scaling type and spacing for projection. The development Canvas colors identify content types within [[06 Resources/Curriculum Development/Ministry Curriculum Development#Canvas Color Code|the workspace]]; printed resources retain the grayscale-and-gold palette above.

## Where It Is Applied

- [[07 Operations/Workflows/Weekly Recap Production|Weekly Recap]] PDFs: `scripts/weekly_recap.py` holds the CSS.

When another resource gets a printable form, reuse that CSS and the assets here rather than designing a new look.
