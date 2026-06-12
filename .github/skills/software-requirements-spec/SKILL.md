---
name: software-requirements-spec
description: Build a Software Requirements Specification (SRS) as a Markdown (.md) file following the Wiegers/Seilevel template structure. Use this skill whenever the user asks to create, draft, scaffold, or fill in a software requirements document, an "SRS", a "requirements spec", or a "documento dei requisiti software" in .md format. Produces a structured document with table of contents, revision history, and all standard SRS sections (Introduction, Overall Description, System Features, Data Requirements, External Interfaces, Quality Attributes, I18n/L10n, Other Requirements, Glossary, Analysis Models).
---

# Software Requirements Specification (SRS) — Markdown Builder

## When to use this skill

Trigger this skill when the user asks to:

- Create / draft / generate a Software Requirements Specification (SRS) in Markdown.
- Produce a "requirements document", "specifica dei requisiti", "documento SRS", or "requirements spec" as a `.md` file.
- Scaffold an empty SRS template they will fill in later.
- Fill in or update specific sections of an existing SRS that follows this template.

Do **not** use this skill for: code-level design docs, ADRs, API references, user manuals, or test plans.

## Related skills

This skill builds the **Markdown document** following the Wiegers/Seilevel template. For the upstream activities and for cross-standard validation, chain to:

- **`babok-v3-software-requirements`** — to **conduct the elicitation interview** with stakeholders (BABOK® Guide v3) before authoring the document.
- **`swebok-v4-software-requirements`** — to **validate the engineering quality** of the requirements (testability, traceability, completeness, security, testing, quality, dependability) against SWEBOK v4.
- **`iso-29148-software-requirements`** — to **audit the resulting document against the ISO/IEC/IEEE 29148:2018 normative requirements** (well-formed `shall` statements, individual + set characteristics, language criteria, attributes, information item content) and to declare conformance.

The Wiegers SRS template that this skill assembles maps cleanly onto the **SRS information item** defined in ISO/IEC/IEEE 29148:2018 §9.6 — use the ISO skill's [checklist-iso-conformance.md](../iso-29148-software-requirements/references/checklist-iso-conformance.md) and [checklist-requirement-writing.md](../iso-29148-software-requirements/references/checklist-requirement-writing.md) as the final gate before sign-off.

## Inputs to gather before writing

Ask the user only if missing:

1. **Project name** (replaces `<Project>` / `<Progetto>` in the title).
2. **Author** (replaces `<author>` / `<autore>`).
3. **Organization** (replaces `<organization>` / `<organizzazione>`).
4. **Date created** (replaces `<date created>` / `<data di creazione>` — use ISO `YYYY-MM-DD`).
5. **Version** (default `1.0 approved` if not specified).
6. **Output file path** (default: `<project-slug>-srs.md` in the current workspace root).
7. **Language** — `en` (English, default) or `it` (Italian). **Detect automatically from the user's first messages**; if the user has been writing in Italian, choose `it`. Once the language is chosen, **do not switch** mid-document.

If the user only wants the **empty template**, copy the appropriate template ([assets/srs-template.md](assets/srs-template.md) for `en`, [assets/srs-template-it.md](assets/srs-template-it.md) for `it`) verbatim and stop there.

## Language convention

The document language is the **user's conversational language**. Two template assets are provided:

| Language | Template file | Mandatory verb (per ISO/IEC/IEEE 29148 §5.2.4) |
|---|---|---|
| **English** (default) | [assets/srs-template.md](assets/srs-template.md) | `shall` |
| **Italian** | [assets/srs-template-it.md](assets/srs-template-it.md) | `deve` (plurale `devono`) |

When authoring the document in Italian, use the following keyword convention (ISO/IEC/IEEE 29148 §5.2.4 — Italian transposition):

| English | Italian | Provision type | Use |
|---|---|---|---|
| **shall** | **deve / devono** | mandatory binding | Requirements |
| **will** | **sarà / è** | non-mandatory, statement of fact / context | Non-requirements |
| **should** | **dovrebbe** | non-mandatory preference / goal | Non-requirements |
| **may** | **può** | non-mandatory allowance | Non-requirements |
| **are / is / was** | **è / sono / era** | descriptive text | Non-requirements |
| ~~must~~ | ~~dovrà~~ (avoid as synonym of `deve`) | AVOID | risk of misinterpretation |
| ~~shall not~~ | ~~non deve~~ | AVOID | use positive statements |
| ~~shall be able to~~ | ~~deve essere in grado di~~ | AVOID | |
| passive voice | passive voice | AVOID | use active voice |

**Hard rule** — a document being authored in Italian must **not** contain the English keywords `shall / should / may / will` in normative text. A document being authored in English must not contain `deve / dovrebbe / può`. The Reviewer will flag mixed-language normative verbs as `IR-002` Fail.

## Procedure

### Step 1 — Start from the canonical template

Always begin by reading the template corresponding to the chosen language:

- **English** → [assets/srs-template.md](assets/srs-template.md)
- **Italian** → [assets/srs-template-it.md](assets/srs-template-it.md)

Do not invent section names or reorder sections. The template is the source of truth for:

- Heading hierarchy and exact section numbering (`1.`, `1.1`, `3.1.1`, …).
- Italic guidance blocks (`*<...>*`) that describe what each section must contain.
- The mandatory **Table of Contents** and **Revision History** table that appear before section 1.

### Step 2 — Replace the cover placeholders

In the top block, substitute:

| Placeholder        | Replace with                            |
|--------------------|-----------------------------------------|
| `<Project>`        | Project name                            |
| `<author>`         | Author full name                        |
| `<organization>`   | Organization / team name                |
| `<date created>`   | ISO date                                |
| `Version 1.0 approved` | Actual version + status              |

### Step 3 — Keep the Table of Contents and Revision History

Both are mandatory and must appear in this order **before section 1**:

1. **Table of Contents** — a Markdown list with anchor links to every section and subsection down to level 3 (`3.1.1`, etc.). Regenerate it any time headings change. Anchor format: lowercase, spaces → `-`, drop punctuation.
2. **Revision History** — a Markdown table with columns `Name | Date | Reason For Changes | Version`. Seed it with the initial row (author, creation date, "Initial draft", version).

### Step 4 — Fill each section using the guidance blocks

For every `*<...>*` italic block in the template, do one of:

- **If the user provided content for that section** → replace the italic guidance with the user's content.
- **If the user did not provide content but the section is required** → keep the italic guidance as a prompt for the author, OR replace it with `TBD` (use `TBD` only inside *functional requirements*, per section 3.1.3 of the template).
- **If the user explicitly says the section is not applicable** → keep the heading and write `Not applicable.` underneath. Do not delete numbered sections — numbering must stay stable.

What goes in each section (summary the agent must respect):

| Section | What to write |
|---------|---------------|
| **1.1 Document Purpose** | Product identity, revision, intended readers (devs, PM, testers, …). |
| **1.2 Document Conventions** | Typographic conventions, requirement-ID format if used. |
| **1.3 Project Scope** | Short description, link to business goals; reference vision/scope doc if it exists. |
| **1.4 References** | Linked list of related docs (style guides, standards, related SRSs) with title/author/version/date/URL. |
| **2.1 Product Perspective** | Context and origin (new / replacement / next version), context diagram if relevant. |
| **2.2 User Classes and Characteristics** | User classes with characteristics; mark the favored ones. |
| **2.3 Operating Environment** | Hardware, OS, locations, co-existing software. |
| **2.4 Design and Implementation Constraints** | Policies, hw limits, mandated technologies / languages. |
| **2.5 Assumptions and Dependencies** | Assumed factors and external dependencies. |
| **3.x System Feature** | One subsection per feature. Use the `3.x.1 Description / 3.x.2 Stimulus-Response / 3.x.3 Functional Requirements` triplet. Add `3.2`, `3.3`, … by duplicating the block. |
| **3.x.1 Description** | One-paragraph description + priority (High / Medium / Low). |
| **3.x.2 Stimulus/Response Sequences** | User action → system response pairs (bulleted or numbered). |
| **3.x.3 Functional Requirements** | Itemized requirements (use stable IDs, e.g. `FR-3.1-01`). Include error handling. `TBD` allowed. |
| **4.1 Logical Data Model** | ER-style data model (Mermaid `erDiagram` recommended). |
| **4.2 Data Dictionary** | Table of data elements: name, type, length, format, allowed values. Or link to external file. |
| **4.3 Reports** | List of generated reports with content / sort / totals. |
| **4.4 Data Acquisition, Integrity, Retention, and Disposal** | Acquisition flow, integrity rules, retention / disposal policy. |
| **5.1 User Interfaces** | UI logical characteristics, GUI standards, common elements. |
| **5.2 Software Interfaces** | Named external systems with versions, message formats, mappings. |
| **5.3 Hardware Interfaces** | Devices, protocols, I/O formats and ranges. |
| **5.4 Communications Interfaces** | Email / web / network protocols, encryption, transfer rates. |
| **6.1–6.4 Quality Attributes** | Usability, Performance, Security, Safety — quantitative and verifiable. |
| **6.5 Others as relevant** | Add subsections for availability, reliability, portability, scalability, etc. |
| **7. Internationalization and Localization** | Currency, date/number formats, languages, character sets, regulations. |
| **8. Other Requirements** | Compliance, install/config/startup/shutdown, logging, audit. Omit if empty. |
| **9. Glossary** | Markdown table `Term | Definition`. Spell out every acronym. |
| **10. Analysis Models** | Mermaid diagrams (data flow, state, feature tree, ER) or links to them. |

### Step 5 — Numbering and structure rules

- Use `#` for the document title, `##` for top-level numbered sections (`## 1. Introduction`), `###` for level 2, `####` for level 3.
- Never renumber sections to "compact" the document. If a section is empty, write `Not applicable.` and leave the heading.
- Keep horizontal rules (`---`) between top-level sections for readability.
- When adding a new feature subsection, mirror the `3.1.1 / 3.1.2 / 3.1.3` triplet exactly.

### Step 6 — Validate before delivering

Before saving / returning the document, check:

- [ ] Title line, author, organization, date, version are filled (no `<...>` placeholders remain on the cover).
- [ ] Table of Contents present, links match actual headings.
- [ ] Revision History table present with at least one row.
- [ ] All 10 top-level sections present, in order, with original numbering.
- [ ] Every `### 3.x.1 / 3.x.2 / 3.x.3` triplet present for each feature.
- [ ] No copyright / page-number footer was carried in from the source PDF.
- [ ] Glossary acronyms each have a definition.
- [ ] **No emojis, Unicode icons, pictographs, stars, sparkles, checkmarks or decorative symbols anywhere in the document** (✅ ❌ ⚠️ ✨ ⭐ 🎉 🚀 🔥 ✓ ✗ → ← in headings, etc.). The document is a formal, professional specification — plain Markdown only (standard headings, paragraphs, lists, tables, fenced code blocks, blockquotes, links, Mermaid diagrams). Bold / italic are allowed only when they carry semantic meaning. If a draft contains decorative symbols, **strip them before delivering**.

## Output

Write the final document to the path the user provided (or the default `<project-slug>-srs.md`). Report back:

1. The file path created.
2. A short list of sections left as `TBD` or `Not applicable.` so the user knows what still needs input.

## Assets

- [assets/srs-template.md](assets/srs-template.md) — canonical empty template in **English**. Use this when the document language is `en`.
- [assets/srs-template-it.md](assets/srs-template-it.md) — canonical empty template in **Italian**. Use this when the document language is `it`. All section titles, ToC anchors, italic guidance blocks and revision-history columns are localised; the Italian keyword convention (deve / dovrebbe / può / sarà) is embedded in §1.2 *Convenzioni del Documento* and in §3.1.3.

Never regenerate the template structure from scratch — always start from one of these two assets.
