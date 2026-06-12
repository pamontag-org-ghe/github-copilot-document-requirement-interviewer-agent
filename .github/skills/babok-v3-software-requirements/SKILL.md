---
name: babok-v3-software-requirements
description: "Interview-driven knowledge base for eliciting software requirements according to the BABOK® Guide v3 (Business Analysis Body of Knowledge — IIBA®). Use this skill whenever you must conduct or coach a requirements interview, plan stakeholder elicitation, choose between elicitation techniques (interviews, workshops, observation, brainstorming, focus groups, surveys, prototyping, document analysis), formulate the right questions to elicit business / stakeholder / solution / transition requirements, or validate that an elicitation activity is complete. Heavy emphasis on **how to conduct the elicitation**: preparation, conduct, confirmation, communication, stakeholder collaboration, and the underlying competencies (facilitation, listening, questioning, negotiation, conflict resolution). Complements the `swebok-v4-software-requirements` skill (engineering perspective) and the `software-requirements-spec` skill (document authoring)."
---

# BABOK v3 — Requirements Elicitation Interview Skill

## When to use this skill

Trigger this skill whenever the user asks to:

- **Conduct or coach a requirements interview** with a stakeholder or end user.
- **Plan an elicitation activity** (which technique, with whom, when, where, what to prepare).
- **Generate the right questions** for a session — open / closed, structured / unstructured.
- **Identify all stakeholders** that should participate in elicitation (Stakeholder List / Map / Personas).
- **Confirm elicitation results** and reconcile contradictions.
- **Manage stakeholder collaboration** during a long-running analysis.
- Extract Business / Stakeholder / Solution (functional & non-functional) / Transition requirements from a free-form narrative or transcript.
- Audit an existing elicitation process against IIBA BABOK v3 best practices.

Do **not** use this skill to author the SRS document (use `software-requirements-spec`) or to validate engineering quality of the requirements set (use `swebok-v4-software-requirements`). This skill is upstream of both: it owns the **conversation with the stakeholder**.

## Related skills

This skill is the **upstream entry point** of the requirements pipeline. After elicitation, hand off as follows:

- **`swebok-v4-software-requirements`** — engineering-quality validation: testability, traceability, completeness, security, testing, quality, dependability, compliance (SWEBOK v4 + ISO/IEC 25010 + ISO/IEC 27001 + IEEE 1012).
- **`iso-29148-software-requirements`** — **normative audit**: well-formed `shall`-statement rules, individual-requirement characteristics (Necessary, Appropriate, Unambiguous, Complete, Singular, Feasible, Verifiable, Correct, Conforming), set-level characteristics (Complete, Consistent, Feasible, Comprehensible, Validatable), language criteria, requirements attributes, and the normative content of BRS / StRS / SyRS / SRS information items. The elicited Business / Stakeholder / Solution / Transition requirement classification of BABOK maps directly onto the ISO information items.
- **`software-requirements-spec`** — final-step skill that renders the validated content as a Markdown SRS document (Wiegers/Seilevel template).

## Reference knowledge base

All references live inside this skill's `references/` folder — the skill is self-contained.

| Topic | Reference file |
|---|---|
| BACCM core concepts, requirements classification (Business / Stakeholder / Solution / Transition), stakeholder generic roles | [references/chapter02-key-concepts.md](references/chapter02-key-concepts.md) |
| Plan Stakeholder Engagement: stakeholder analysis, attitudes, authority, influence, collaboration & communication planning | [references/chapter03-plan-stakeholder-engagement.md](references/chapter03-plan-stakeholder-engagement.md) |
| **Elicitation and Collaboration KA (chapter 4)** — Prepare / Conduct / Confirm / Communicate / Manage Collaboration | [references/chapter04-elicitation.md](references/chapter04-elicitation.md) |
| Underlying competencies: analytical thinking, behavioural characteristics, communication skills, interaction skills, facilitation, listening, negotiation | [references/chapter09-competencies.md](references/chapter09-competencies.md) |
| **Elicitation techniques (chapter 10 selection)** — Interviews, Workshops, Observation, Brainstorming, Focus Groups, Document Analysis, Survey/Questionnaire, Prototyping, Stakeholder List/Map/Personas, Collaborative Games, Non-Functional Requirements Analysis, Acceptance and Evaluation Criteria, Use Cases & Scenarios, User Stories, Reviews, Item Tracking, Prioritization, Glossary | [references/chapter10-techniques.md](references/chapter10-techniques.md) |
| Prioritised **checklist for an elicitation activity** (Critical → Low) | [references/checklist-elicitation.md](references/checklist-elicitation.md) |
| **Interview question bank** grouped by requirement type (Business / Stakeholder / Solution / Transition) and by BACCM concept (Change / Need / Solution / Stakeholder / Value / Context) | [references/checklist-interview-questions.md](references/checklist-interview-questions.md) |

## Procedure

The skill drives the elicitation in the same four-task loop defined by BABOK §4: **Prepare → Conduct → Confirm → Communicate**, plus the ongoing **Manage Stakeholder Collaboration**.

### Step 0 — Frame the session

Before any preparation, capture:

1. **Project name** and one-sentence change being analysed.
2. **Interviewee(s)**: name, role, stakeholder class (use BABOK generic roles: Sponsor, Customer, Domain SME, End User, Implementation SME, Operational Support, PM, Regulator, Supplier, Tester — see [references/chapter02-key-concepts.md](references/chapter02-key-concepts.md) §2.4).
3. **Format of input**: live one-on-one, group interview, workshop, transcript, written narrative, survey result, observation notes, document analysis result.
4. **Time budget** for this session and how many sessions are foreseen.
5. **Decision-making authority and attitudes** of the interviewee (champion / neutral / detractor) — drives tone and approach.

If the source is a **free-form narrative** ("racconto frontale"), do a single pass and produce one batch of clarifying questions; otherwise plan a back-and-forth.

### Step 1 — Prepare for Elicitation (BABOK §4.1)

Follow [references/chapter04-elicitation.md](references/chapter04-elicitation.md) §4.1. Always answer, before the session:

1. **Understand the scope of the elicitation** — business domain, organisational culture, stakeholder locations, group dynamics, expected outputs the session feeds, the skill level of the analyst, complementary activities planned, scope of the future solution, possible sources of information.
2. **Select elicitation techniques** — combine 2 or more from [references/chapter10-techniques.md](references/chapter10-techniques.md). The default mix for a single stakeholder is **structured/unstructured interview + document analysis**; for a group it is **workshop + brainstorming + prototyping**; for end users it is **observation + interview**; for many distant respondents it is **survey/questionnaire + follow-up interviews**.
3. **Set up logistics** — goals, participants and roles, scheduled resources (people, rooms, tools), locations, communication channels, technique(s) chosen, languages used (oral and written), agenda.
4. **Secure supporting material** — existing system docs, business rules, organisational policies, regulations, contracts, prior analysis models, prototypes; procure or develop missing material.
5. **Prepare the stakeholders** — explain the technique, share agenda and pre-read material in advance, secure buy-in from all necessary stakeholders.

Produce a small **Elicitation Activity Plan** containing: goal(s), scope, techniques, participants & roles, logistics, supporting material, expected output format.

### Step 2 — Conduct Elicitation (BABOK §4.2)

Three modes can be combined: **Collaborative** (direct interaction), **Research** (analysing materials and data), **Experiments** (controlled tests / prototypes / observation).

While conducting:

- **Guide the activity** — stay on the goals; recognise when discussion strays out of scope and explicitly choose to acknowledge-and-continue or redirect; decide when sufficient elicitation has been reached and stop.
- **Capture outcomes** — record decisions, ideas, open issues, conflicting statements, and follow-up actions.

For **interviews specifically** ([references/chapter10-techniques.md](references/chapter10-techniques.md) §10.25), follow this flow:

1. **Opening** — describe the purpose; confirm roles; explain how info will be recorded and shared.
2. **During** — keep focus on stated goals and predefined questions; adapt to the interviewee's responses and **non-verbal cues**; use **active listening**; ask **open questions** to elicit dialogue and **closed questions** to confirm; manage concerns immediately or capture them for follow-up; take notes (or record with consent).
3. **Closing** — ask "what have we overlooked?"; share contact for follow-up; summarise the session; outline next steps; thank them.
4. **Follow-up** — organise notes and **confirm results with the interviewee as soon as possible** to let them point out missed or wrongly recorded items.

For **workshops** ([references/chapter10-techniques.md](references/chapter10-techniques.md) §10.50), assign Sponsor / Facilitator / Scribe / Timekeeper / Participants roles; agree ground rules at the start.

### Step 3 — Apply disambiguation rules continuously

When a stakeholder uses any of these vague words / patterns, stop and ask a follow-up question that forces a measurable answer or surfaces the underlying need:

| Pattern | Follow-up |
|---|---|
| "fast", "quick", "responsive" | "compared to what — and measured how (response time, throughput, at which percentile)?" |
| "user-friendly", "intuitive", "easy to use" | "easy for whom doing what task in how much time, measured how (success rate, time-on-task, SUS)?" |
| "secure" | "against which threat actor, protecting which asset, in terms of CIA — and what control do you have in mind?" |
| "scalable", "high-volume" | "scaling along which axis (RPS, MAU, data GB), to what upper bound, and what should happen beyond it?" |
| "reliable", "always available" | "availability % over what window, allowed downtime, RTO/RPO, exclusions?" |
| "compliant", "follows standards" | "which standard / regulation / clause exactly, and how is conformance demonstrated?" |
| "the user wants X" (where X is a solution) | **5-Whys**: "why X? what need would X satisfy?" — discover the underlying need before locking in a design. |
| "everyone agrees" | "who has formally accepted this — and are there stakeholders whose objections we have not heard?" |
| solution implied without need stated | re-anchor on BACCM Need: "what problem or opportunity does this address?" |

The questions in [references/checklist-interview-questions.md](references/checklist-interview-questions.md) implement this disambiguation systematically.

### Step 4 — Confirm Elicitation Results (BABOK §4.3)

Before committing resources to use the elicitation output, run two checks:

1. **Compare results against source information** — go back to the interviewee or document; in follow-up meetings let stakeholders correct what was captured; allow asynchronous confirmation when appropriate.
2. **Compare results against other elicitation results** — cross-check with information from other interviews, surveys, observations, document analysis; surface variations explicitly and resolve them collaboratively (or escalate using **Item Tracking** — [references/chapter10-techniques.md](references/chapter10-techniques.md) §10.26).

Confirmation is **less formal** than later analysis-time validation — its purpose is to make sure what was captured matches what was said and is internally consistent.

### Step 5 — Communicate Business Analysis Information (BABOK §4.4)

Package and convey the elicited information to all stakeholders who need it. Decide format and channel by asking:

- Who is the audience? what do they need from this?
- What is their preferred style of communication / learning?
- What information matters most?
- Are the presentation and format right for this audience?
- Does this support downstream activities?
- Any regulatory or contractual constraints on format?

Possible packages: **Formal Documentation** (template-based, long-term record), **Informal Documentation** (text/diagrams used within the change), **Presentations** (high-level overviews). Delivery via **group collaboration**, **individual collaboration**, or **e-mail / asynchronous** depending on maturity of the information.

### Step 6 — Manage Stakeholder Collaboration (BABOK §4.5)

Continuous activity in parallel with all of the above. Three elements:

1. **Gain agreement on commitments** — explicit understanding of time and resource commitments from stakeholders.
2. **Monitor stakeholder engagement** — verify the right SMEs are participating, attitudes stay stable or improve, results are confirmed in time, agreements are kept; watch for risks (stakeholders diverted, low-quality elicitation output, delayed approvals).
3. **Collaboration** — encourage free, bi-directional flow of ideas; make every stakeholder feel heard.

### Step 7 — Validate against the elicitation checklist

Before declaring a session "done", walk [references/checklist-elicitation.md](references/checklist-elicitation.md) in priority order (Critical → High → Medium → Low). Any open Critical or High row blocks closure.

### Step 8 — Hand off

Map the elicited and confirmed information onto the four BABOK requirement types (Business / Stakeholder / Solution → Functional + Non-Functional / Transition — see [references/chapter02-key-concepts.md](references/chapter02-key-concepts.md) §2.3) and hand off to:

- **`swebok-v4-software-requirements`** for engineering-quality validation (testability, traceability, completeness, security, testing, quality);
- **`iso-29148-software-requirements`** for the normative ISO/IEC/IEEE 29148:2018 audit (well-formed `shall`-statement rules + set-level characteristics + information-item content), especially when a formal conformance claim is needed;
- **`software-requirements-spec`** to produce the final SRS Markdown document.

## Inputs to gather before starting

Ask the user only if missing:

1. **Project name** and one-sentence purpose / business goal.
2. **Stakeholder(s) being interviewed** — name and stakeholder class.
3. **Source material** (transcript / narrative / live session / notes).
4. **Domain class** and any mandatory standards / regulations.
5. **Elicitation activity type** if known (interview / workshop / observation / survey / mixed).

## Output

When invoked stand-alone (not via `software-requirements-spec`), this skill produces:

1. An **Elicitation Activity Plan** (one per session) — goal, scope, technique, participants, logistics, supporting material.
2. A **structured findings document** in Markdown, organised by BACCM (Change / Need / Solution / Stakeholder / Value / Context) and cross-classified by requirement type (Business / Stakeholder / Solution-Functional / Solution-NonFunctional / Transition).
3. An **Open Issues / Items log** (Item Tracking, [references/chapter10-techniques.md](references/chapter10-techniques.md) §10.26) for contradictions, gaps, deferred questions.
4. A **next-questions list** for the next round (if any Critical/High row of [references/checklist-elicitation.md](references/checklist-elicitation.md) is still open).
5. A short **handoff summary** mapping findings to the entry points of `swebok-v4-software-requirements` and `software-requirements-spec`.

## Assets

- **[references/](references/)** — self-contained BABOK v3 knowledge base (chapter extracts + checklists + interview question bank). The skill is autonomous; no files outside this folder are required at runtime.
