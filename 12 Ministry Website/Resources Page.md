# Resources Page

From [[12 Ministry Website/Ministry Website Overview|Ministry Website]]

## Document Status

**Resource publication and planning record; updated October 26, 2026.** DEC-072 established the page. The [[07 Operations/Workflows/Website Publication and Maintenance#Groups Resources Release|Groups Resources release procedure]] governs Sanity/Vercel publication at `resources.goldencity.church`. This update does not independently verify the live site. Russ approved both leader guides and the agreement under **Other Resources** today (DEC-082); their final review, public editions, and actual release remain implementation work (BWR-033, BWR-037). Other resource access questions remain open.

**Live at [resources.goldencity.church](https://resources.goldencity.church/), with the church-domain redirect and Groups entrance verified October 24, 2026.** Russ and Paul decided on October 19, 2026 to build a Groups resources page ([[08 Archive/Decisions/Decision History#DEC-072 — Groups Resources Page|DEC-072]]). The current three-category layout follows Paul’s October 22 request. Paul approved the first eight PDF editions for public distribution on October 22 and the October 25 *Patience* recap as the ninth public resource; future resources retain their own review requirements. The independent Astro/Sanity implementation is deployed at [GCC Resources](https://gcc-groups-resources.vercel.app), with the church subdomain and redirect selected by Paul and verified October 24. BWR-037 is complete; resource-specific review, leader-guide production, and third-party CoJourner rights remain in their own queue items.

**Paul's October 22 clarification:** Leadership training belongs among ministry resources and may appear on the resources page, including Belonging, Beholding, Becoming. The earlier limit concerns placing that formation line on the Groups overview prematurely, not a blanket prohibition on public use. This clarification does not publish or approve every individual resource.

## Plan

- **Current address in the publishing procedure:** `resources.goldencity.church`; the October 19 plan named `goldencity.church/groups/resources`.
- **Owner:** Paul, as Groups website owner (DEC-037)
- **Look:** retain the resource website's own presentation; downloadable resources keep the [[06 Resources/Brand/Groups Resource Style|Groups Resource Style]] (DEC-071)

| Category | Planned resources | Current state |
|---|---|---|
| City Groups Resources | Weekly Recap | Sunday production includes Paul's review, leader-chat delivery, and public publication. As of November 16, 2026, the October 4 through November 8 recaps (Weeks 1–6 of *The Fruit of the Spirit*) are live; the November 15 recap is a draft awaiting Paul's review. Chat posting is recorded only in each record (BWR-030). |
| Collectives Resources | Galatians Study | Six sessions with two-page handouts (DEC-076). Paul approved the Session 1–2 handouts for both Collectives for public publication on October 22, and they went live that day; later sessions follow the standing publishing process. |
| Other Resources | CoJourner leader equipping | Continued development for the library approved November 23 (DEC-090). See [[06 Resources/Leader Development/CoJourner\|CoJourner]] for the early source, development plan, and applicable release review (BWR-019). |
| Other Resources | [[06 Resources/Leader Development/City Group Guide\|City Group Guide]]; [[06 Resources/Leader Development/Collective Leader Guide\|Collective Leader Guide]]; [[06 Resources/Leader Development/GCC Group Leader Agreement\|GCC Group Leader Agreement]] | Placement and public access approved by Russ October 26 (DEC-082). Paul gave review notes on both guides October 26 and his final review is still pending; public PDFs are prepared, and unpublished Sanity drafts (`city-group-guide`, `collective-leader-guide`) were staged October 29 with web text matching the PDFs. Not yet published. The agreement's public edition (`gcc-group-leader-agreement`) was seen live under Other Resources on October 29. |

## Before Publishing

Check each resource before it goes on the page:

- **Audience:** DEC-082 settles public access for both guides and the agreement under Other Resources. They are written to support leaders while being publicly accessible. Decide other resources individually.
- **Public language:** DEC-082 authorizes Belonging, Beholding, Becoming in both guides, superseding the October 1 restriction for these resources. It does not authorize a separate rewrite of the Groups landing page.
- **Third-party material:** CoJourner comes from The Garden Project Ministry. Describe it and link to the source; republishing its material needs attribution and permission ([[06 Resources/External Adaptations/Highlands Resource Adaptation\|External Adaptations]] shows the copyright boundary).
- **Approval:** guide direction is approved; Paul's review of the new prose, export checks, and publication are still pending. Policies come from the approved agreement; unresolved reporting and church-wide-policy questions remain open (BWR-041). Do not fill those gaps with new policy in a guide.
- **Privacy:** no participant names, prayer requests, addresses, staff phone numbers, or completed acknowledgements in public editions (DEC-028, DEC-082). Do not upload the existing private agreement PDF.

## Guide Development

Both drafts follow DEC-082–083: supportive and encouraging language; identity and purpose; community, prayer, and Scripture; Belonging, Beholding, Becoming; an adaptable gathering example; leader discernment; and links to the agreement for emergency responses. The City Group Guide includes “In the city, for the city.” The Collective Leader Guide serves Men's and Women's leaders/co-leaders and helps a new leader pick up the shared rhythm. Keep policy in the agreement rather than reproducing it in competing versions.

## Technical Proposal — October 22, 2026

### Ministry Purpose and Scope

Help group participants and leaders find usable resources for Scripture, prayer, shared life, and faithful response to Christ. Belonging, Beholding, Becoming and formation over information guide resource design and may be explained in leadership training materials. This is a resource library within Golden City Church, serving the church's shared life, group relationships, and pastoral care.

Start with a simple resource index and individual resource pages/downloads. Keep the planned City Groups, Collectives, CoJourner, and Others categories as editorial groupings, not additional ministry branches. Show categories only when they contain resources cleared for public use. Bible Club resources and Leadership Training may be included as usable content becomes available; Classes do not become a fourth branch. Weekly Recaps remain optional for City Groups. The draft guides and Galatians handouts listed above retain their review status. CoJourner begins with an appropriate description and source link when available; republishing third-party course files requires permission.

This is post-launch support work: church launch and Group Launch Day have passed. There is no newly approved website deadline. Prioritize a small, reliable collection over a complete curriculum portal, accounts, search infrastructure, or leader training tracking.

### Responsibilities and Sources

| System | Responsibility | Boundary |
|---|---|---|
| Squarespace | Church website, `/groups`, and `/groups/fall2026`; proposed resources entry link/redirect | Existing public group information remains here. |
| This ministry vault and existing Notion curriculum | Governance, research, curriculum development, review evidence, and source materials | No automatic export of `06 Resources` or the whole vault to the public site. |
| `gcc-groups-resources` on GitHub | Public website code and public-safe configuration | No internal decision records, confidential data, unpublished source files, credentials, or third-party materials without permission. |
| Sanity | Editorial copy and files intended for public distribution | A publication CMS; ministry approval stays with existing authority and confidential materials stay elsewhere. |
| Astro | Static resource index and resource detail pages generated from Sanity at build time | Visitors do not need a live CMS connection to read generated pages. |
| Vercel | Independent resources-site builds, previews, and hosting | Main church hosting stays on Squarespace in the recommended first phase. |
| Planning Center / Church Center | Existing group and enrollment records and participant paths | Link to verified destinations; do not duplicate participant records or build a second enrollment system. |

Paul owns technical implementation and routine resource editing within existing authority. Russ or the appropriate pastoral authority retains review of new theological claims, policy changes, and resources awaiting pastoral review. Using Belonging, Beholding, Becoming in leadership training is not itself an additional public-language approval barrier. Church-domain administration access and ongoing technical backup still need to be identified before connecting the church hostname.

### URL and Main-Site Isolation

The planned public entry remains `goldencity.church/groups/resources`. DNS selects hosts, not URL paths; a CNAME cannot assign just this path to Vercel. A rewrite in the new Vercel project also cannot affect requests that still arrive at Squarespace.

| Approach | Visitor address | Effect on the main site | Recommendation |
|---|---|---|---|
| Native Squarespace resources page | Original `/groups/resources` path | Smallest hosting change; staff edit native blocks | Viable smaller alternative if a short download list meets the actual need. |
| Independent Astro site on a resource subdomain, with a Squarespace redirect | Starts at `/groups/resources`, then changes to the resource subdomain | Only the resource subdomain needs Vercel DNS; existing main-site hosting remains | Recommended first phase for the requested stack. |
| Reverse proxy in front of the church hostname | Keeps `/groups/resources` in the address bar | Proxy becomes part of the delivery path for the main site, including Squarespace routes | Defer unless keeping the exact address is a firm requirement. |

Proposed subdomain: `resources.goldencity.church`, subject to availability and the church's domain administrator. Host the Astro index at `/` on that subdomain, use `/resources/<slug>/` for individual resources, and set the site's canonical origin to the chosen resource hostname. Use normal links back to the church's Groups and group directory pages. The Astro site will need its own matching header/footer; Squarespace's shared navigation does not automatically carry over.

After the resources deployment and its domain are verified, the proposed Squarespace URL mapping is:

```text
/groups/resources -> https://resources.goldencity.church/ 302
```

Start with a temporary redirect while validating the arrangement; use 301 only after the destination is settled. Squarespace requires any page occupying the source route to be disabled or removed for the redirect to work; preserve a recovery copy rather than deleting substantive content. Verify the church's primary `www`/apex behavior and both entry URLs. Set only the resource subdomain's DNS using the values Vercel supplies; do not replace the main church's DNS records as part of this phase.

If the exact original path must remain visible, prepare a separate proxy design before changing DNS: route `/groups/resources` and its descendants to Astro, provide a collision-free route for Astro's generated assets, and route other paths to a verified Squarespace origin that cannot loop back through the proxy. Test redirects, canonical URLs, cookies, forms, navigation, static assets, TLS, and rollback across the main site. Vercel supports external rewrites, but compatibility with this particular Squarespace installation is untested. This alternative provides application separation while introducing shared ingress operations.

### Minimum Content and Publication Model

Propose one `resource` document type: title, slug, short description, category, resource date, optional Scripture reference, optional series/session label, file or external source link, and a public-distribution clearance flag. Use fixed category choices initially. Sanity's native draft/published state handles editorial work; the public build reads the published perspective and includes only resources explicitly cleared for public distribution. Distinguish target audience from access restrictions: Leadership Training may serve leaders while remaining publicly accessible. Published-but-uncleared documents and restricted material must not enter a public dataset at all: a website filter is not access control. Review evidence remains in its existing ministry home.

Only upload files already safe for public access. Sanity's ordinary dataset assets are publicly accessible on its CDN even when the dataset itself is private. A hidden page, unlisted URL, Studio login, or `noindex` does not secure a download. Keep genuinely restricted materials in existing access-controlled channels outside the public site and public asset store; design authenticated delivery when a demonstrated need warrants it. No participant names, prayer requests, private addresses, screening records, or pastoral-care notes enter this project.

The proposed publication sequence is: review the source and intended audience → prepare a public-safe edition → obtain any applicable pastoral/copyright clearance → edit in Sanity → Paul publishes → rebuild Astro on Vercel → inspect the actual public page and download. Rebuild on changes to published content, including unpublishing and deletion; editing or unpublishing in Sanity alone does not remove an older static page. A Sanity webhook can call a Vercel Deploy Hook; keep that hook URL and any read token out of the public repository and browser bundle. CMS outages or build failures should leave the last successful deployment available, with Paul checking and resolving failed builds.

Keep code previews separate from production and use a known public-safe sample for draft development. Defer live editorial preview, a custom approval application, member accounts, advanced search, and custom CI until a demonstrated need justifies them. Configure the project's production branch and publication behavior deliberately before connecting automatic deployments.

### Current Implementation and Next Gate

On October 22, the empty public repository [PaulCanaan/gcc-groups-resources](https://github.com/PaulCanaan/gcc-groups-resources) was first cloned into a sibling directory. At Paul’s subsequent request, that checkout was moved to `/Users/paulcanaan/Workspace/Projects/Golden City Church/Groups Ministry/06 Resources/Resources Page`, which is now the website build home. Its `origin` remains `git@github.com:PaulCanaan/gcc-groups-resources.git`. The parent ministry repository ignores that independent checkout and retains its own `golden-city-groups` remote. The local implementation includes an Astro index, static resource pages, print styling, a Sanity resource schema/Studio, and Vercel configuration. Design examples are explicitly labeled and cannot enter a production build. Runtime, browser, CMS, and deployment verification are recorded separately rather than inferred from code creation.

Paul subsequently chose the existing **PaulCanaan** Hobby team (`paul-canaan`) as the shared home for his web projects, superseding the request for a separate GCC Groups team. The team name and Hobby plan were verified through the authenticated Vercel CLI. The plugin still returns 403 for this team, so the official CLI is the hosting fallback. No Sanity plugin was found in the connected catalog; the build uses official Sanity tooling. Sanity project `1consdwv`, dataset `production`, has been created and claimed. A temporary published resource and a draft verified the CMS-to-static-build path; the draft was excluded, both test documents were removed, and rebuilding removed the old resource route. Vercel project `gcc-groups-resources` is linked to the local checkout under PaulCanaan. Vercel classified the first explicit preview attempt as production; it failed before release with the sample-content guard in place. The next attempt was correctly classified as Preview and reached READY: [design preview](https://gcc-groups-resources-1vmherbm4-paul-canaan.vercel.app), protected by Vercel sign-in. The initial scaffold was pushed at `475d233`. The subsequent `d981d90` Git push produced the first live PDF library and verified automatic production deployment from `main`. The later church-domain, redirect, and Groups-entrance implementation is recorded below.

BWR-037 is complete: Paul selected the resource subdomain and redirect, the church-domain entry and Groups-page link are live, and the publication path has been exercised through nine reviewed resources. Resource-specific clearance continues under the standing publishing process; the leader guides remain BWR-033 and CoJourner source/permission remains BWR-019. CMS-only changes still need a deliberate rebuild. Neither implementation success nor a public resource establishes group readiness.

### Public PDF Release — October 22, 2026

Paul explicitly answered **“Approve all 8 PDF editions”** after the exact files and dates were listed. The public library at **https://gcc-groups-resources.vercel.app/** contains:

- **City Groups Resources:** Weekly Recaps — Love (October 4), Joy (October 11), Peace (October 18).
- **Collectives Resources:** Galatians 1 and 2 for both Men’s and Women’s Collectives, including the Women’s October 27 handout.
- **Other Resources:** GCC Group Leader Agreement, public edition. Private pastoral phone numbers were removed throughout; the approved policy text and blank acknowledgement remain. Completed acknowledgements stay private.

Sanity project `1consdwv`, dataset `production`, holds the eight published resource entries and PDF assets. At the initial release, cards opened PDFs directly; the later reading-page update below adds separate web/PDF choices. CoJourner and design examples do not appear in this release. All eight assets were checked anonymously against the approved source hashes, and all eighteen PDF pages were visually inspected. Astro tests, type checks, static build, and Studio build pass; phone and desktop navigation were checked. GitHub pushes to `main` now trigger production builds. CMS-only changes currently require a deliberate rebuild; a Deploy Hook/webhook has not been configured.

The Vercel production domain is public. The church-domain DNS and Squarespace redirect/link were completed October 24; later resources retain their own clearance. The release does not record Church Center posting, leader appointment, or gathering outcomes. Recovery uses the previous known-good Git/deployment and deliberate resource unpublishing plus rebuild; a public PDF URL is not revoked by hiding its card.

### Library Simplification — October 22, 2026

At Paul’s request, the public library now opens with exactly three collapsed categories: **City Groups Resources**, **Collectives Resources**, and **Other Resources**. Other Resources includes the public Leader Agreement and is the home for future Group Leader Collaboration resources when cleared for publication. The category list and Sanity Studio choices follow this structure; older CoJourner category values normalize to Other Resources without changing CMS documents or public PDF files.

Reviewed the Groups page’s development and design records: the October 1 rebuild separated the overview and directory into native Squarespace pages, using small scoped enhancements and collapsed details. The resource library carries forward Roboto, grayscale, restrained gold, direct navigation, and keyboard-operable disclosures while retaining its own clean Astro design. Removed the tall decorative document illustration, repeated introductory sections/category navigation, duplicate card-cover titles, and secondary joining banner so visitors can see the categories immediately. Replaced the placeholder cross favicon with the official GCC skyline logo already used by the church’s public site; the Groups wordmark remains in the page header.

Published from independent repository commit `50f7154` to [the public Vercel library](https://gcc-groups-resources.vercel.app/); production deployment reached READY. Tests and Astro checks pass (17 files, zero errors/warnings), and the static build generates ten pages. Verified collapsed entry, independent expansion, Enter/Space controls, visible keyboard focus, direct category links, no horizontal overflow at 320/375/1280px, all eight public PDF downloads, and the deployed favicon bytes. Recovery: previous source/deployment `f53dc67`; no CMS resource or asset changes were needed. Squarespace work is deferred until Russ can help Paul sign in.

### Visual Polish — October 22, 2026

Paul requested modest graphic enrichment after reviewing the simplified library. Published commit `7946b32`: compact decorative open-book illustration on desktop/tablet, category line icons, warm gold/sage/clay accents, softly bordered panels, resource-count pills, and clearer open/hover states. Kept the three initially collapsed categories, original copy, official favicon, and all eight PDF destinations. Decorative SVGs are hidden from assistive technology, and the existing reduced-motion rules remain in effect. The illustration is hidden on phones to preserve the compact opening.

Astro checks report zero errors/warnings, and the static build passes. Browser checks at 320/375/768/1280px show no horizontal overflow; Enter/Space expansion and visible keyboard focus work. The public production page displays the illustration and three category icons, with all eight PDF links preserved. Recovery: prior commit/deployment `50f7154`. Squarespace remains deferred.

### Approved Bible Illustration — October 22, 2026

After reviewing the local preview, Paul approved the generated open Bible illustration with a slightly smaller display. Published commit `4152d33`: the ivory-page, olive-cover, gold-ribbon artwork replaces the earlier line illustration at 200px wide on desktop (previously 240px) and 160px on tablet; the existing phone behavior is preserved. The transparent image is optimized as a 768×512 WebP, about 74KB, at `public/images/open-bible.webp` in the independent website repository.

Astro checks and static build pass. Verified the public production page loads the new image at 200px, the tablet preview uses 160px, neither layout overflows, and all eight PDF links remain present. Recovery: prior commit/deployment `7946b32`. No Sanity or Squarespace changes.

### Full Resource Pages and PDF Downloads — October 22, 2026

Paul requested web pages from the existing Markdown resources and two options on every card: **View Full Resource** and **Download Printable PDF**. Published independent repository commit `ba01501`; Vercel production reached READY. All eight existing resource routes now contain the full approved public text: three Weekly Recaps, four Galatians handouts, and the public Agreement. Sanity’s body field holds Markdown; no PDF assets, slugs, dates, or clearance flags changed. Source frontmatter, print-layout comments, and internal governance notes are excluded. The Agreement web edition includes its nineteen policies and acknowledgement without private phone numbers. Galatians pages retain their Scripture credit.

Cards use separate accessible links rather than a single PDF-only link. The page link opens the full resource in the same tab; the PDF action uses Sanity’s attachment-download parameter and a readable filename. Each reading page also has a printable-PDF link and a return link that reopens the matching category. The existing dated slugs remain stable, for example [Weekly Recap · Love](https://gcc-groups-resources.vercel.app/resources/weekly-recap-2026-10-04-love/). Church-domain paths such as `goldencity.church/groups/resources/<slug>` are not configured by this release; the Squarespace work below remains deferred until access is available.

Validation: four tests pass, Astro checks report zero errors/warnings across eighteen files, and website/Studio builds pass. All eight reading pages return HTTP 200 with one page title, complete sections, correct canonicals, and no source metadata; the library contains eight reading links and eight download actions. All eight PDF responses confirm attachment headers and the intended filenames. Browser checks cover card-to-page navigation, full headings/questions, category return links, keyboard controls, and narrow 320/375/501px layouts without overflow.

Recovery: restore the previous known-good Vercel deployment (`a08bd5c`). The pre-update CMS entries are saved locally in the ignored `.sanity/markdown-backup-1792711730504.json`; restore their body fields before rebuilding old source that expects summary-only text. Future updates should keep the approved web and PDF editions aligned; CMS-only changes still need a deliberate rebuild.

### Warmer Actions and In-Page PDF Preview — October 22, 2026

At Paul’s request, **View Full Resource** now uses a lighter warm parchment color. **Preview Printable PDF** opens a small dialog in the current page, with Previous/Next page controls, close/Escape support, keyboard focus containment and return, a full-resource link, and an explicit download choice. Opening the preview neither navigates to another tab nor starts a download. The same flow is available on resource reading pages.

Published independent repository commit `8850f24` (Vercel production READY). The live library and reading-page previews render the actual PDFs successfully. This release adds a PDF.js viewer loaded only when a preview opens. The build copies the eight approved PDFs byte-for-byte to same-origin static routes because the asset host rejects browser-origin reads. No CMS documents, assets, or access settings changed. Missing/invalid PDFs fail the build; unpublishing and rebuilding removes the corresponding static routes. Future web/PDF editions still require publication review and a deliberate rebuild.

Validation: four tests pass; Astro checks report zero errors/warnings across twenty-one files; static build passes. All eight emitted PDFs match the approved source hashes. Browser checks verify actual PDF rendering, multi-page navigation, Escape/focus return, Tab wrapping, and 320/375px layouts without horizontal overflow. Recovery: previous source/deployment `ba01501`. Squarespace remains deferred.

### Squarespace Entry — October 22 Request (Superseded October 24)

Paul requested a native Squarespace resources page at `goldencity.church/groups/resources` linking to the existing Vercel library, and a resource link from the Groups overview. This was the prepared implementation scope. Paul subsequently chose the subdomain-and-redirect arrangement recorded below; this native landing page was not retained.

Use the existing Squarespace header, footer, typography, colors, and native blocks. Keep the page small:

| Field | Prepared value |
|---|---|
| Page / navigation title | Groups Resources |
| URL slug | `groups/resources` |
| Eyebrow | GOLDEN CITY / GROUPS |
| Heading | Resources for life together. |
| Description | Find Weekly Recaps, Galatians Study handouts, and the GCC Group Leader Agreement to help you prepare, gather, and follow Jesus together. |
| Primary button | Open Resource Library |
| Button destination | `https://gcc-groups-resources.vercel.app/` |
| Secondary link | Back to Groups → `/groups` |
| SEO title | Groups Resources | Golden City Church |
| SEO description | Download Weekly Recaps, Galatians Study handouts, and the GCC Group Leader Agreement for Golden City Groups. |

Add a native **Group Resources** link/button on `/groups` to `/groups/resources`, matching its existing styles. Exact block placement will follow inspection of the live editor. The library itself remains in the independent `gcc-groups-resources` repository; Groups OS ignores `/06 Resources/Resources Page/`, and no website build files are tracked in Groups OS.

**Historical access state (October 22):** Deferred at Paul’s request until sign-in could be arranged. At that point, no Squarespace page or overview link had been changed. Existing public `/groups` content was inspected before editing. Save a recovery copy of the affected block before changing it. Rollback removes the added overview link and disables/moves the new page without deleting existing ministry content. Verify the saved public page, the overview-to-resources link, the Vercel button, and phone/keyboard use before recording publication.

### Church Domain and Groups Entrance — October 24, 2026

Paul explicitly selected **resources.goldencity.church with a redirect**, preserving the existing resource-library design. Attached the hostname to Vercel project `gcc-groups-resources` on PaulCanaan, added only `CNAME resources → 9b57026cd5d86626.vercel-dns-017.com` through Squarespace DNS, verified the domain, and issued its TLS certificate. Main-site and email DNS records were preserved. Updated `SITE_URL` to `https://resources.goldencity.church` and rebuilt the existing application source; production deployment `6aw2TmChAZJF5u953wuh1zPTEfAs` reached READY. The original Vercel URL remains available.

The existing empty Squarespace `/groups/resources` page is disabled and retained for recovery. The saved URL mapping is `/groups/resources -> https://resources.goldencity.church/ 302`; the existing `/Launch` mapping is preserved. The apex entry first normalizes to `www`, then redirects; the `www` source with and without a trailing slash returns 302 to the library. Resource reading pages live at `resources.goldencity.church/resources/<slug>/`; exact church-domain descendant paths are not configured.

Added a native **Group Resources** heading, short description, and **Browse Group Resources ↗** link in the overview’s existing semester invitation section. The link points to `/groups/resources`. Reused its previously empty second text block, removing only that block’s selector from the scoped CSS hiding empty blocks. Hero, branch cards, directory and enrollment destinations retain their existing content. No standalone Squarespace resource landing page is needed.

Verification: the saved public Groups entrance is visible at desktop and 375px phone width without horizontal overflow; keyboard activation follows the redirect to the library. The new origin serves all eight reading pages and PDFs; all eight PDF hashes match the approved originals. The actual Peace PDF renders in the in-page viewer. HTTPS, canonical origin, apex/`www` normalization, and trailing-slash redirect were checked. No enrollment requests were submitted. CMS-only publishing still requires a deliberate rebuild; future editions retain their own clearance.

Recovery: return the added text block to blank and restore its prior hide selector to remove the Groups entrance; remove only the new URL mapping to undo the redirect. The existing empty resources page can be re-enabled after removing the mapping. If reverting the hostname, remove only its CNAME/project domain, restore `SITE_URL` and a compatible known-good deployment together, and use the original Vercel URL. Before-edit Groups HTML and URL mappings were saved locally in `/private/tmp/gcc-groups-before-resources-link.html` and `/private/tmp/gcc-url-mappings-before.txt`. This routine implementation does not approve additional resources or change ministry governance.

### Standing Publishing Process — October 25, 2026

Paul directed that once he has reviewed a resource Claude produced, such as a Weekly Recap or a Collectives Galatians handout, Claude adds it to this page. Paul's review comes first; a draft is never published. Use [[07 Operations/Workflows/Website Publication and Maintenance#Groups Resources Release|Groups Resources Release]] for the shared release steps and [[07 Operations/Workflows/Weekly Recap Production#6. Publish to the resources page|Weekly Recap Production]] for recap entry fields. Each resource still passes Before Publishing above.

Access: the Sanity and Vercel connectors are connected to Claude (October 25). The agent shells on the Mac and in the cloud cannot reach Sanity or Vercel directly. A standalone Sanity Studio now lives beside the site at `06 Resources/studio-gcc-groups-resources`, carrying a copy of the site's `resource` schema; its schema is deployed to `1consdwv/production`. Keep its category list in step with `src/lib/resource.ts`. No Sanity webhook or Vercel Deploy Hook is configured yet, so each CMS change still needs a deliberate rebuild.

### Technical References

Official documentation checked October 22, 2026: [Astro with Sanity](https://docs.astro.build/en/guides/cms/sanity/), [Squarespace URL mappings](https://support.squarespace.com/hc/en-us/articles/205815308-URL-mappings), [Squarespace domain pointing and path limitations](https://support.squarespace.com/hc/en-us/articles/215744668-Pointing-a-Squarespace-domain), [Vercel external rewrites](https://vercel.com/docs/routing/rewrites), [Vercel Deploy Hooks](https://vercel.com/docs/deploy-hooks), and [Sanity asset visibility](https://www.sanity.io/docs/media-library/asset-visibility).

Paul's referenced ChatGPT conversation, *Architecture Suggestions*, was read through the conversation tool, but its assistant replies were returned only as content-reference placeholders. This proposal responds to the readable Astro + Sanity + Vercel / Squarespace requirements, the ministry's current records, and Paul's October 22 clarification; it is not a verified line-by-line revision of the unavailable replies.

## Connections

- [[12 Ministry Website/Groups Page|Groups Page]] — the existing Groups overview and directory.
- [[06 Resources/Resources Overview|Ministry Resources]] — the vault's resource library.
- [[08 Archive/Decisions/2026-10-19 Staff Meeting Minutes#2 — Groups Resources Page|October 19 staff meeting, item 2]] — the source of this plan.
