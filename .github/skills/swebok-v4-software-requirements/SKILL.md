---
name: swebok-v4-software-requirements
description: Interview-driven knowledge base for eliciting and validating software requirements according to SWEBOK Guide v4.0 (Software Requirements, Software Testing, Software Quality, Software Security KAs) plus ISO/IEC/IEEE 29148, ISO/IEC 25010, ISO/IEC 27001, and IEEE 1012. Use this skill whenever you must interview a user/stakeholder to produce a Software Requirements Specification (SRS) — especially when the source material is a free-form narrative ("racconto frontale"), a meeting transcript, or partial notes — to make sure no macro topic (functional, nonfunctional/QoS, security, testing, compliance, traceability) is missed. Produces a prioritised set of interview questions, drives the dialogue per macro topic, and validates the gathered material against prioritised checklists (Critical → High → Medium → Low) before handing off to the `software-requirements-spec` skill that builds the final .md document.
---

# SWEBOK v4 — Software Requirements Interview & Validation Skill

## When to use this skill

Trigger this skill whenever the user asks to:

- Run a **requirements interview** with a stakeholder or product owner.
- Extract / structure / validate requirements from a **free-form narrative**, meeting transcript, voice memo, or notes.
- **Identify missing requirements** ("what didn't they tell me?") before drafting the SRS.
- **Validate** an existing SRS or backlog against SWEBOK v4 / ISO best practices.
- Decide which questions to ask **next** during an ongoing elicitation session.

Do **not** use this skill to author the final SRS document — for that, chain to the `software-requirements-spec` skill (it owns the canonical template, ToC, revision history, and section structure). This skill produces the *content* and *gap analysis*; the other skill produces the *document*.

## Related skills

- **`babok-v3-software-requirements`** — upstream of this skill: **conducts the elicitation interview** (BABOK® Guide v3) and produces structured findings classified as Business / Stakeholder / Solution (Functional + Non-Functional) / Transition requirements. Use it whenever the source material is a live stakeholder rather than an existing document or backlog.
- **`iso-29148-software-requirements`** — downstream / parallel: provides the **normative ISO/IEC/IEEE 29148:2018 audit** of every individual requirement (`shall`, unambiguous, verifiable, singular, …) and of the requirement *set* (complete, consistent, feasible, comprehensible, validatable). Many SWEBOK checks here reinforce ISO checks one-to-one. Run the ISO skill's [checklist-iso-conformance.md](../iso-29148-software-requirements/references/checklist-iso-conformance.md) before sign-off if conformance is in scope.
- **`software-requirements-spec`** — final-step skill that renders the validated content as a Markdown SRS document.

## Reference knowledge base

Every macro topic below has two reference files in the workspace root: a **knowledge file** (general explanation, SWEBOK chapter extract) and a **checklist** (prioritised verification rows, Critical → Low). Open them when you need depth on a topic or when you are validating the elicited material.

| Macro topic | Knowledge file | Checklist |
|---|---|---|
| Software Requirements (foundations, elicitation, analysis, specification, validation, management) | [references/chapter1-software-requirements.md](references/chapter1-software-requirements.md) | [references/checklist-software-requirements.md](references/checklist-software-requirements.md) |
| Software Testing (test levels, objectives, acceptance criteria, conformance/compliance, non-functional, security/privacy testing) | [references/chapter5-software-testing.md](references/chapter5-software-testing.md) | [references/checklist-software-testing.md](references/checklist-software-testing.md) |
| Software Quality (ISO/IEC 25010 model, dependability, integrity levels, V&V, traceability) | [references/chapter12-software-quality.md](references/chapter12-software-quality.md) | [references/checklist-software-quality.md](references/checklist-software-quality.md) |
| Software Security (CIA, ISMS / ISO 27001, secure SDLC, threat modeling, CERT top-10, CVE/CWE/CAPEC/CVSS) | [references/chapter13-software-security.md](references/chapter13-software-security.md) | [references/checklist-software-security.md](references/checklist-software-security.md) |

For the SRS document structure itself (table of contents, section numbering, italic guidance blocks), defer to the **`software-requirements-spec`** skill and its [srs-template.md](../software-requirements-spec/assets/srs-template.md).

For the **section-by-section minimum information** that must be elicited per ISO/IEC/IEEE 29148 + the Wiegers template — i.e., the *"what must I extract from the user to fill each SRS section"* view — use the companion asset **[assets/phase1-iso-mandatory-info.md](assets/phase1-iso-mandatory-info.md)**. Open it whenever you are about to start a topic and want the per-section elicitation targets and cross-references back to the prioritised checklists.

## Procedure

### Step 1 — Frame the session

Before asking anything, capture:

1. **Project name** and one-sentence purpose.
2. **Interviewee role** (sponsor, end-user, SME, regulator, ops, support, …).
3. **Format of input** (live interview / transcript / written narrative / partial backlog).
4. **Time budget** for the session.

If only a written narrative is available, mark it as a *one-shot pass* and prepare a single batch of clarifying questions instead of a dialogue.

### Step 2 — Pass 1: extract what is already stated

From the user's narrative or transcript, extract — without asking questions yet — a draft of:

- Problem statement / business goal.
- User classes mentioned.
- Features / capabilities mentioned (group as candidate `3.x System Features`).
- Constraints mentioned (tech, policy, regulatory).
- Quality / non-functional adjectives ("fast", "secure", "easy") — flag each as **ambiguous → must be quantified**.
- Data mentioned (entities, sensitive data).
- External systems mentioned.

Use the **SR KA §3.1** desirable-properties lens (unambiguous, testable, atomic, feasible, complete, consistent, …) to mark each extracted item as `OK`, `AMBIGUOUS`, `UNTESTABLE`, `COMPOUND`, or `MISSING-ACCEPTANCE`.

### Step 3 — Drive the interview by macro topic, in priority order

For each macro topic below, walk the prioritised checklist in the order **Critical → High → Medium → Low** and ask only the questions for items that are not already answered by the narrative.

> **Rule:** never ask a Medium/Low question while a Critical/High one is still open for the same macro topic.

Macro topics, in the order you should drive them:

1. **Scope & Stakeholders** (SR KA §1, §2.1)
2. **Functional Requirements & Acceptance Criteria** (SR KA §1.4, §3.1, §4.3 + Testing §2.1.4, §3.1.8)
3. **Data Requirements** (SRS §4 + Quality KA §3.3 data quality + Security KA §1.2 CIA per data class)
4. **External Interfaces** (SRS §5 + Testing §2.2.10)
5. **Quality Attributes / Non-functional / QoS** (Quality KA §3.3 ISO 25010 + SR KA §1.7, §3.2 fail/perfection points)
6. **Security** (Security KA §1, §4 + Quality KA §3.3 *security* characteristic)
7. **Safety & Dependability** (Quality KA §1.4 + integrity levels)
8. **Compliance & Standards** (SR KA §3.1 external consistency + Testing §2.2.2 + Quality KA §1.3 + Security KA §2.2 ISMS)
9. **Operating Environment & Constraints** (SRS §2.3, §2.4)
10. **Internationalisation / Localisation** (SRS §7)
11. **Testing strategy implied by requirements** (Testing KA §2.1 levels, §3.5 operational profile)
12. **Traceability, Change Control, Volatility, Prioritisation** (SR KA §6.2, §7.2, §7.3, §7.4)

For each macro topic, the question template is:

```
Topic: <name>            Checklist file: <path>
- For each Critical/High row not yet covered:
  1. Quote the row's "What must be verified".
  2. Ask one focused question (use the row's ✅/❌ example to disambiguate).
  3. Record the answer; mark the row Covered / Partial / Unknown.
- Stop the topic when all Critical & High rows are Covered or explicitly Out-of-scope.
```

### Step 4 — Disambiguation rules (apply continuously)

When a stakeholder uses any of these, **stop and ask**:

| Vague word | Force a measurable answer about… |
|---|---|
| "fast", "responsive", "performant" | response time / throughput at percentile, with units and load |
| "secure" | which threat actor, which asset, which CIA property, which control |
| "user-friendly", "intuitive" | task, success rate, completion time, satisfaction (SUS) |
| "scalable" | load axis (RPS, MAU, GB), upper bound, degradation rule |
| "reliable", "stable" | MTBF, availability %, RTO/RPO |
| "robust" | which inputs, which error conditions, which recovery |
| "available", "always on" | availability %, allowed downtime window, scheduled vs unplanned |
| "compliant", "standards-based" | which laws/standards/clauses verbatim |
| "private" | which personal data, legal basis, retention, data-subject rights |

Apply the **5-whys** when the stakeholder states a *solution* instead of a need (SR KA §3.1).

### Step 5 — Continuous validation pass

After each macro topic or at any natural break, run the relevant checklists in **Critical → Low** order and produce a gap report with three buckets:

- **Blocking** — Critical rows not covered.
- **High-risk** — High rows not covered.
- **Hygiene** — Medium / Low rows not covered.

The interview is not "done" while any **Blocking** row exists for a topic that is in scope.

### Step 6 — Hand off to the SRS author

When the elicitation has produced enough material:

1. Group findings under the canonical SRS sections (see [software-requirements-spec/SKILL.md](../software-requirements-spec/SKILL.md)).
2. Mark items with stable IDs (e.g., `FR-3.1-01`, `NFR-PERF-02`, `SEC-014`, `COMP-GDPR-Art-32`).
3. For unresolved items, mark `TBD` (functional) or keep the italic guidance prompt (other sections), and list them in the **Gap Report** so they are visible.
4. (Recommended) Hand the findings to **`iso-29148-software-requirements`** to audit each individual requirement against the ISO `shall`-statement rules and to audit the requirement set; address any Critical / High issue *before* invoking the document-authoring skill.
5. Invoke the **`software-requirements-spec`** skill with the structured findings + the target output path.

## Inputs to gather before starting

Ask the user only if missing:

1. **Project name**.
2. **Stakeholder(s) being interviewed** and their role.
3. **Source material** (transcript / narrative / notes / live session).
4. **Mandatory standards or regulations** the product must comply with (or ask: "are there any?").
5. **Domain class** (e.g., enterprise SaaS, mobile app, embedded real-time, safety-critical, ML-based, data product) — drives which Testing KA §3.6 domain rules and Security KA §6 sub-topics apply.

## Output

When invoked stand-alone (not via the `software-requirements-spec` skill), this skill produces:

1. A **structured findings document** (Markdown) with one section per macro topic, each listing: covered items, partial items, gaps.
2. A **Gap Report** sorted Blocking → High-risk → Hygiene, citing the originating checklist row ID (e.g., `SR-001`, `ST-007`, `SQ-006`, `SS-004`).
3. A **next-questions list** to bring to the next interview round (if any Blocking gap remains).
4. A short **handoff summary** for the `software-requirements-spec` skill: mapping of findings → SRS sections.

## Assets

- **[assets/phase1-iso-mandatory-info.md](assets/phase1-iso-mandatory-info.md)** — per-section minimum information to elicit, distilled from the canonical SRS template and aligned with ISO/IEC/IEEE 29148. Each row points back to the relevant prioritised checklist IDs.
- **[references/](references/)** — self-contained knowledge base: SWEBOK v4 chapter extracts (Requirements, Testing, Quality, Security) and prioritised checklists (Critical → Low). The skill is autonomous: no files outside this folder are required at runtime.
