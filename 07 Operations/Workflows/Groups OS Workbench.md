# Groups OS Workbench

## Document Status

Personal workspace configuration and usage guide, authorized by Paul on October 21, 2026. It adds navigation and tooling to the existing ministry system. It does not change ministry direction, curriculum approval, readiness, or the biweekly review cadence.

## Start a Working Session

Open [[Home]]. The Groups OS toolbar provides Home, Dashboard, Board, Curriculum, Canvas, Templates, New, Search, and AI. The homepage keeps existing notes open. AnuPpuccin supplies the theme; the Groups OS CSS snippets apply restrained gold accents, Home cards, and Dashboard readability. The six Canvas content colors retain their existing meaning.

## Create Only the Next Needed Item

Use **New** (QuickAdd) or search the command palette for:

| Command | Existing template and destination | Use condition |
|---|---|---|
| New curriculum project | [[10 Templates/Records/Curriculum Project|Curriculum Project]] → phase 02 | A real project, source, audience, and immediate question |
| New curriculum session | [[10 Templates/Records/Curriculum Session|Curriculum Session]] → phase 03; choose the actual project folder | Paul has confirmed the synthesis, formation goals, and outline |
| New research source | [[10 Templates/Records/Research Source|Research Source]] → dated phase 01 inbox note | A real source or question; access and source location stated |
| New brainstorm Canvas | [[10 Templates/Canvas/Curriculum Session Brainstorm.canvas|Curriculum Session Brainstorm]] → dated phase 01 Canvas | Original thinking; maintained project maps remain in phase 02 |

The filename prompt asks for the actual subject. Existing-file collisions prompt rather than silently overwriting. Core Templates and Templater point to the existing template library. Automatic new-file templates and shell commands are not needed for these entries.

## Scripture and Research

Keep the passage and Bible translation explicit. Record author, edition, precise page/section, URL or Notion/Zotero item, and access state. Separate source wording, biblical observations, interpretation, formation proposals, and open questions. For Galatians, retain the current project brief's source priorities and distinct Men's/Women's formation goals and dated resources.

Use **Search** (Omnisearch) for notes and indexed PDF text. PDF indexing is local and is not OCR of scanned pages; image/AI indexing and the HTTP API remain off. Search by a distinctive passage, author, title, or phrase, and verify the actual source page. An indexed match is not proof of an interpretive claim.

Zotero Integration has a **Groups OS Research Source** import format targeting the existing local-only phase 01 inbox. It uses [[10 Templates/Records/Zotero Research Import|the Zotero import template]], which preserves the `research-notes` section on repeat imports. The template records bibliographic metadata without bulk-copying annotations or whole source texts. Use the manual **Research Source** entry when Zotero is unavailable. A live import requires Zotero running with Better BibTeX and an actual item; the presence of this configuration does not prove that connection works.

## Canvas and AI Handoff

Follow [[06 Resources/Curriculum Development/Ministry Curriculum Development|the existing development workflow]] and [[06 Resources/Curriculum Development/AI Agent Roles|AI Agent Roles]]. One agent can perform the roles sequentially.

1. Open the actual Canvas or brief and the specific source note. In the AI panel, provide the file or selected cards and the immediate question.
2. Ask for **Canvas Organizer**, **Curriculum Editor**, or **Resource Producer** as appropriate. State the intended artifact, audience, actual source version, and current review state.
3. Review the proposed changes and actual files. Record Paul's real review in the existing project brief at the existing handoffs; notes, checkboxes, and polished formatting do not establish approval.

Reusable starting instruction:

> Read the linked project brief, Canvas, actual sources, and applicable AGENTS.md. Work as [existing role] on [one question/output] for [audience]. Preserve original inputs, distinguish evidence/proposals/open questions, and return the actual changed files and the next review decision. Stay within the current authorization and the existing curriculum handoffs.

Claudian is configured to locate the installed Claude Code and Codex executables. Provider authentication and available models are discovered from those tools; no API key or fixed model is embedded here. Claude uses manual permissions; Codex retains a workspace sandbox and user approval review. Automatic AI title generation is off. The setup does not send course material to a model as a connectivity test.

For IDE work, open the **Groups Ministry** folder as the workspace so its root AGENTS.md and Git repository apply. Keep Obsidian open for Canvas and backlinks. In Codex, select that same existing folder and name the actual brief/Canvas. The downloadable Groups OS IDE workspace accompanying this setup opens that folder without modifying IDE account or trust settings.

## Version History and Recovery

The Obsidian Vault root is **Golden City Church**; the Git repository is its **Groups Ministry** subfolder. The Git plugin points to that subfolder; automatic commit, pull, and push are off. `.obsidian` configuration lives outside that Git repository. Existing raw curriculum inputs and working database records remain ignored according to `.gitignore`.

Use the separate pre-enhancement ZIP for the changed workspace/configuration baseline. It is not a full Vault backup. Restore only the needed files after checking for newer work; do not overwrite a live editing session or treat Git as protection for ignored inputs. Configuration changes do not authorize a sync or publication.

## Connections

- [[07 Operations/Workflows/Workflows Overview|Workflows]]
- [[10 Templates/Templates Overview|Templates]]
- [[06 Resources/Curriculum Development/Ministry Curriculum Development|Curriculum development]]
- [[06 Resources/Curriculum Development/AI Agent Roles|Existing AI roles]]

## Curriculum Board

[[00 Dashboard/Curriculum Board|Curriculum Board]] is Paul's visual working view of existing research, synthesis, editable drafts, and resource-library guidance. It uses the installed Kanban plugin. Cards link to real files; no source files are moved or duplicated by the board. The four columns describe workspace homes rather than course approval or event execution.

Drag cards to organize your working view, open a card's linked note or Canvas to do the actual work, and add a card only for a real next step. Card placement or a checked card never records Paul's review, approves curriculum, completes a ministry action, or changes a project's canonical state. Keep actual direction, versions, and review evidence in the existing project brief; retain the Biweekly Review Queue as the operational queue. The initial draft cards follow the Galatians brief's current record that the Session 1 and 2 handouts await Paul.

## Appearance and Home Cards

AnuPpuccin uses Latte in light mode and Mocha in dark mode, with its card layout and restrained Groups gold accents. Home provides ministry, course, research, people, resource, and decision entrances. Dashboard styling changes the presentation only; its recorded dates, readiness, and next actions remain intact.

Minimal remains installed. Use Obsidian Appearance to switch back to Minimal. The separate pre-AnuPpuccin ZIP restores this round's Home, Dashboard, toolbar, and appearance baseline. `groups-os-studio` is the added page-layout snippet; disabling it removes the new card and dashboard layouts without deleting notes or links.
