---
name: iso-29148-software-requirements
description: "Authoritative knowledge base for producing requirements information items (BRS / StRS / SyRS / SRS) that conform to ISO/IEC/IEEE 29148:2018 (Systems and software engineering — Life cycle processes — Requirements engineering). Use this skill whenever the user must (a) write or validate individual textual requirements against the standard's well-formedness rules (shall, unambiguous, verifiable, etc.), (b) check a requirements set for completeness / consistency / feasibility per the standard, (c) assemble the canonical structure (information items) of a Business Requirements Specification, Stakeholder Requirements Specification, System Requirements Specification, or Software Requirements Specification, (d) tailor or claim conformance to the standard. This skill is the **normative reference**: it complements the `babok-v3-software-requirements` skill (how to elicit), the `swebok-v4-software-requirements` skill (engineering perspective), and the `software-requirements-spec` skill (Markdown SRS authoring against the Wiegers template)."
---

# ISO/IEC/IEEE 29148:2018 — Requirements Engineering Skill

## When to use this skill

Trigger this skill whenever the user asks to:

- **Write or rewrite a textual requirement** so it satisfies the standard's well-formedness rules (use of *shall*, avoidance of vague terms, singular, verifiable, …).
- **Audit / validate** an existing requirement, set of requirements, or specification against ISO/IEC/IEEE 29148.
- Decide **which information items** to produce on a project (Business Requirements Specification, Stakeholder Requirements Specification, System Requirements Specification, Software Requirements Specification) and **what the normative content of each** must be.
- Build the **outline** of a BRS / StRS / SyRS / SRS according to the standard's example outlines (Clause 8).
- Decide whether to claim **full** or **tailored conformance** and what that implies.
- Add or check **requirements attributes** (identification, owner, priority, risk, rationale, type, …).
- Translate the requirements found by `babok-v3-software-requirements` (elicitation) or validated by `swebok-v4-software-requirements` (engineering) into a structure that survives an ISO audit.

Do **not** use this skill to *conduct the elicitation* (use `babok-v3-software-requirements`) or to produce a Markdown SRS following the Wiegers template (use `software-requirements-spec`). This skill is the **normative spine** to which the other three connect.

## Reference knowledge base

All references live inside this skill's `references/` folder — the skill is self-contained.

| Topic | Reference file |
|---|---|
| Conformance options (full / process / information item / tailored) and what each one means | [references/clause04-conformance.md](references/clause04-conformance.md) |
| **Requirements fundamentals** — construct, mandatory verbs (*shall* / *should* / *may* / *will*), characteristics of an individual requirement (9), characteristics of a requirement set (5), language criteria (vague terms to avoid), and requirements attributes (identification, owner, priority, rationale, risk, type) | [references/clause05-fundamentals.md](references/clause05-fundamentals.md) |
| **Information items** the project must produce, and example outlines (Clauses 7 and 8) — BRS, StRS, SyRS, SRS | [references/clause07-08-information-items.md](references/clause07-08-information-items.md) |
| **Detailed normative content** of each information item, section-by-section (Clause 9) — what each section of a BRS / StRS / SyRS / SRS must contain | [references/clause09-information-item-content.md](references/clause09-information-item-content.md) |
| Prioritised **checklist for ISO/IEC/IEEE 29148 conformance** at the document / set level (Critical → Low) | [references/checklist-iso-conformance.md](references/checklist-iso-conformance.md) |
| Prioritised **checklist for writing an individual well-formed requirement** (Critical → Low) — apply per requirement | [references/checklist-requirement-writing.md](references/checklist-requirement-writing.md) |

## Procedure

### Step 1 — Identify the information item being produced

Ask the user (or infer from context) which of the four normative information items the work is targeting:

| Item | Acronym | Purpose | Detailed content reference |
|---|---|---|---|
| Business Requirements Specification | **BRS** | Why the system is being developed or changed; top-level requirements from the business / organisational perspective | [references/clause09-information-item-content.md](references/clause09-information-item-content.md) §9.3 |
| Stakeholder Requirements Specification | **StRS** | Requirements from the stakeholders' perspective; how the organisation will use the system | [references/clause09-information-item-content.md](references/clause09-information-item-content.md) §9.4 |
| System Requirements Specification | **SyRS** | Technical requirements for the system-of-interest; usability for human-system interaction | [references/clause09-information-item-content.md](references/clause09-information-item-content.md) §9.5 |
| Software Requirements Specification | **SRS** | Requirements for a software product / program / set of programs | [references/clause09-information-item-content.md](references/clause09-information-item-content.md) §9.6 |

> NOTE — In many industries the **BRS** and **StRS** are merged. Information items do not have to be physical documents — content stored in a repository / model is acceptable as long as the required content is easily available and logically organised (Clause 7).

### Step 2 — Decide the conformance posture

Following [references/clause04-conformance.md](references/clause04-conformance.md), decide whether the project will claim:

- **Full conformance** — to the requirements engineering process clauses (5.2.4, 5.2.5, 5.2.6, 5.2.7), to the processes of ISO/IEC/IEEE 15288 and 12207 cited in Clause 6.1, to the information items in Clause 7, and to the content of Clause 9 and Annex A.
- **Conformance to processes only** — only the process provisions of Clause 6.
- **Conformance to information item content only** — only the information item content requirements of Clauses 7 / 9 / Annex A.
- **Tailored conformance** — selected / modified clauses per Annex C; tailored text is declared.

Document the chosen posture at the top of the specification.

### Step 3 — Build the information item structure

Use the **example outlines in Clause 8** ([references/clause07-08-information-items.md](references/clause07-08-information-items.md)) as the starting structure for the chosen information item. Then fill the normative content per Clause 9.

Common general content for any information item (per §9.2):

1. **Identification** — title + revision notice.
2. **Front matter** — table of contents, list of figures, list of tables.
3. **Definitions** — words / phrases with special meaning.
4. **References** — complete list; subdivided into *Compliance* (cited documents whose requirements apply) and *Guidance* (informative references).
5. **Acronyms and abbreviations** — every acronym spelled out / defined.

### Step 4 — Write each requirement against the well-formedness rules

For **every textual requirement**, walk [references/checklist-requirement-writing.md](references/checklist-requirement-writing.md) (Critical → Low). The non-negotiable rules from §5.2.4 / §5.2.5 / §5.2.7:

- Use **shall** for mandatory binding provisions; **should** for non-mandatory preferences; **may** for allowances; **will** for statements of fact / context. **Avoid "must"** (potential misinterpretation as requirement). **Avoid "shall not"** (use positive form). **Use active voice; avoid "it is required that" / "shall be able to"**.
- Subject + verb. The requirement states the *subject* (the system / the software / etc.), *what shall be done*, or a *constraint*.
- One requirement = one decision (singular). Decompose compound "and/or" statements.
- No vague modifiers: avoid **superlatives** (best, most), **subjective** language (user friendly, easy to use, cost effective), **vague pronouns** (it, this, that), **ambiguous adverbs / adjectives** (almost always, significant, minimal), **ambiguous logical operators** (or, and/or), **open-ended non-verifiable terms** (provide support, but not limited to, as a minimum), **comparative phrases** (better than, higher quality), **loopholes** (if possible, as appropriate, as applicable), **totality terms** (all, always, never, every), **incomplete references**.
- Each requirement satisfies the **9 individual-requirement characteristics**: Necessary, Appropriate, Unambiguous, Complete, Singular, Feasible, Verifiable, Correct, Conforming.

### Step 5 — Attach the requirements attributes

For every requirement, populate the attributes from §5.2.8 (see [references/clause05-fundamentals.md](references/clause05-fundamentals.md)):

- **Identification** — unique, immutable identifier (never re-used after deletion).
- **Version number** of the requirement (volatility indicator).
- **Owner** — person / element that maintains it and approves changes.
- **Stakeholder priority** — e.g., High / Medium / Low or 1..5.
- **Risk** — risk value (low maturity tech ⇒ higher risk; can be inherited from a parent requirement).
- **Rationale** — why this requirement is needed; pointer to analysis / trade-study / modelling.
- **Difficulty** — Easy / Nominal / Difficult.
- **Type** — Functional/Performance, Interface, Process, Quality (Non-Functional / "-ilities"), Usability/Quality-in-Use, Human Factors.

### Step 6 — Validate the requirements **set**

After all requirements are written, walk the **5 characteristics of a requirement set** (§5.2.6):

1. **Complete** — describes all necessary capabilities; **no TBD / TBS / TBR left at baseline**.
2. **Consistent** — no conflicts / overlaps; homogeneous units and terminology.
3. **Feasible** — realisable within cost / schedule / technical constraints with acceptable risk (includes "affordable").
4. **Comprehensible** — clear as to what is expected.
5. **Able to be validated** — satisfaction will demonstrably meet the entity needs (incl. legal & regulatory).

### Step 7 — Run the conformance checklist

Before signing off, walk [references/checklist-iso-conformance.md](references/checklist-iso-conformance.md) in priority order. Any open Critical or High row blocks conformance claim.

### Step 8 — Hand-off / interoperate with sibling skills

This skill is the **normative reference**. It interoperates with:

| Skill | Direction | What flows |
|---|---|---|
| `babok-v3-software-requirements` | upstream → here | elicited requirements classified as Business / Stakeholder / Solution (Functional+Non-functional) / Transition map naturally onto BRS / StRS / SyRS+SRS / appropriate sections. |
| `swebok-v4-software-requirements` | parallel | engineering-quality validation of testability / traceability / completeness / security / testing / compliance — many SWEBOK checks reinforce ISO 29148 checks (e.g., SR-001..SR-005 in SWEBOK ↔ §5.2.5 / §5.2.6 here). |
| `software-requirements-spec` | downstream → final document | when the deliverable is a Markdown SRS following the Wiegers template, the ISO 29148 §9.6 content requirements map onto the Wiegers sections; this skill's checklists validate the resulting document against the ISO normative content. |

## Inputs to gather before starting

Ask the user only if missing:

1. **Information item type** — BRS / StRS / SyRS / SRS (or combination).
2. **Conformance target** — Full / process only / information item only / tailored.
3. **Project name, version, date, owner**.
4. **Domain or industry** (drives applicable standards and quality characteristics).
5. **Source of the requirements** — elicitation output, existing document, model repository.

## Output

When invoked stand-alone, this skill produces:

1. The **conformance statement** (Step 2 outcome) — declaring full / partial / tailored conformance with citations.
2. The **information item outline** (per Clause 8) populated with the normative content sections of Clause 9.
3. A **requirement-by-requirement audit table** (output of [references/checklist-requirement-writing.md](references/checklist-requirement-writing.md)) — every requirement scored against the 9 individual characteristics and the language criteria.
4. A **requirement-set audit** (output of [references/checklist-iso-conformance.md](references/checklist-iso-conformance.md)) — set-level characteristics, attributes presence, TBD/TBS/TBR closure, traceability.
5. A short **handoff summary** mapping findings to `software-requirements-spec` (for Markdown rendering) and to `swebok-v4-software-requirements` (for engineering checks).

## Assets

- **[references/](references/)** — self-contained ISO/IEC/IEEE 29148:2018 knowledge base (cleaned, structure-preserving extracts of Clauses 4, 5, 7, 8, 9 + two prioritised checklists). The skill is autonomous; no files outside this folder are required at runtime.
