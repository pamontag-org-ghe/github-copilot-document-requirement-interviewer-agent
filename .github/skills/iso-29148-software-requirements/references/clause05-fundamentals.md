# Clause 5 — Concepts / Requirements Fundamentals (ISO/IEC/IEEE 29148:2018)

> Source: **ISO/IEC/IEEE 29148:2018**, Clause 5 *Concepts* (pp. 9–19).
> This is the **most important reference of the skill** — it defines what a well-formed requirement and a well-formed requirement set are, the language criteria, and the standard requirements attributes.

## 5.1 General

Clause 5 presents concepts that apply to **requirements statements themselves** and to the **information items** generated during the documenting process. The concepts apply to the properties of requirements at all levels of the system-of-interest and to the processes used in elicitation, analysis, allocation, documentation and management.

## 5.2 Requirements fundamentals

### 5.2.1 General

Requirements engineering is an interdisciplinary function that mediates between the domains of the acquirer and supplier/developer to establish and maintain the requirements to be met by the system, software or service of interest. Its primary result is **sets of requirements**, each set:

- being with reference to a defined system, software or service;
- enabling an agreed understanding between stakeholders (acquirers, users, customers, operators, suppliers);
- having been validated against real-world needs;
- able to be implemented; and
- providing a reference for verifying designs and solutions.

### 5.2.2 Stakeholders

Stakeholders vary across projects. A **minimum set** consists of **users and acquirers** (who may not be the same). Complex projects may impact many users and many acquirers, each with different concerns. Two further groups often need to be added to the minimum set:

1. the **organisation(s)** developing, maintaining or operating the system — legitimate interest in benefiting from the system;
2. **regulatory authorities** with statutory, industry, or other external requirements demanding careful analysis.

### 5.2.3 Transformation of needs into requirements

Defining requirements **begins with stakeholder needs** (goals, objectives) that are refined and evolve before becoming valid stakeholder requirements. Initial concerns lack definition, analysis, and possibly consistency / feasibility. The **Concept of Operations** (organisational level) and **System Operational Concept** (system perspective) help understanding.

The stakeholder-owned system requirements are then transformed into **lower-level system element requirements**. Significant iteration is expected when risk due to technology / complexity is significant, when needs genuinely change, or when requirements were never properly defined.

### 5.2.4 Requirements construct *(normative — full conformance ref.)*

Well-formed stakeholder, system, and system-element requirements **shall** be developed.

A **well-formed specified requirement** contains one or more of the following:

- it **shall** be met or possessed by a system to solve a problem, achieve an objective or address a stakeholder concern;
- it is qualified by **measurable conditions**;
- it is bounded by **constraints**;
- it defines the **performance of the system** when used by a specific stakeholder, or the corresponding capability of the system — **not** a capability of the user/operator/other stakeholder;
- it can be **verified** (its realisation in the system can be demonstrated).

#### Statement form

A requirement is a statement that translates or expresses a need and its associated constraints and conditions. In natural-language form, the statement should include a **subject + verb**, plus other elements needed. **A requirement shall state the subject** (the system, the software, …), **what shall be done** (operate at a power level, provide a field for, …) **or a constraint** on the system.

#### Keyword convention

| Verb | Provision type | Use |
|---|---|---|
| **shall** | mandatory binding | Requirements |
| **will** | non-mandatory, non-binding statement of fact / futurity / purpose / context | Non-requirements |
| **should** | desired but non-mandatory preference / goal | Non-requirements |
| **may** | suggestion or allowance, non-mandatory | Non-requirements |
| **are / is / was** | descriptive text | Non-requirements |
| ~~must~~ | **AVOID** — risk of misinterpretation as a requirement |
| ~~shall not~~ | **AVOID** — use positive statements |
| ~~shall be able to~~ | **AVOID** |
| passive voice ("it is required that …") | **AVOID** — use active voice |

> **NOTE** — Agile may use alternative formulations such as user stories without explicitly using *shall*. See ISO/IEC/IEEE 12207:2017 Annex H.

All terms specific to requirements engineering should be **formally defined and applied consistently** across all requirements of the system.

#### Conditions and constraints

- **Conditions** are measurable qualitative or quantitative attributes stipulated for a requirement. They permit the requirement to be validated and verified. They may limit the options open to a designer.
- **Constraints** restrict the design solution or the implementation of the systems engineering process. Examples:
  - interfaces to already-existing systems (format, protocol, content) where the interface cannot be changed;
  - physical size limitations;
  - laws of a particular country;
  - available duration or budget;
  - pre-existing technology platform;
  - maintenance constraints;
  - user or operator capabilities and limitations.

Requirements may be **ranked or weighted** to indicate priority, timing or relative importance. Requirements in **scenario form** depict the system's action from a user's perspective.

### 5.2.5 Characteristics of individual requirements *(normative — full conformance ref.)*

Each stakeholder, system and system-element requirement **shall** possess the following **9 characteristics**:

1. **Necessary** — defines an essential capability / characteristic / constraint / quality factor. Removing it would leave a deficiency that cannot be fulfilled by implementing other requirements. The requirement is currently applicable and not made obsolete by passage of time. Requirements with planned expiration / applicability dates are clearly identified.
2. **Appropriate** — the specific intent and amount of detail is appropriate to the level of the entity (level of abstraction matches the level of entity). Avoid unnecessary constraints on architecture or design; allow implementation independence to the extent possible.
3. **Unambiguous** — interpretable in only one way. Stated simply and easy to understand.
4. **Complete** — sufficiently describes the necessary capability / characteristic / constraint / quality factor to meet the entity need **without needing other information** to understand the requirement.
5. **Singular** — states a single capability / characteristic / constraint / quality factor.
   > A single requirement consists of a single function, quality or constraint, but **can have multiple conditions** under which the requirement is to be met.
6. **Feasible** — can be realised within system constraints (cost, schedule, technical) with acceptable risk.
7. **Verifiable** — structured and worded so its realisation can be proven (verified) to the customer's satisfaction at the level the requirement exists. Verifiability is enhanced when the requirement is **measurable**.
8. **Correct** — an accurate representation of the entity need from which it was transformed.
9. **Conforming** — conforms to an approved standard template and style for writing requirements, when applicable.

### 5.2.6 Characteristics of a set of requirements *(normative — full conformance ref.)*

Each **set** of requirements (for a system, software or service) **shall** possess the following **5 characteristics**:

1. **Complete** — the set stands alone and sufficiently describes the necessary capabilities / characteristics / constraints / quality factors without needing further information. The set **does not contain any TBD (To Be Defined), TBS (To Be Specified), or TBR (To Be Resolved) clauses** — resolution may be iterative within an acceptable timeframe determined by risks and dependencies.
   > To improve completeness:
   >
   > - include all requirements types relevant to the system;
   > - account for requirements at all stages of the life cycle;
   > - involve **all** stakeholders in elicitation, capture, and analysis.
   >
   > It is common to have TBx markers during the evolution; the set **cannot be considered complete** until all TBx items have been resolved.
2. **Consistent** — individual requirements are unique, do not conflict or overlap; **units and measurement systems are homogeneous**; terminology is **consistent** (the same term is used throughout to mean the same thing).
3. **Feasible** — the complete set can be realised within entity constraints (cost, schedule, technical) with acceptable risk. *Feasible includes "affordable".*
4. **Comprehensible** — clear as to what is expected by the entity and its relation to the system of which it is a part.
5. **Able to be validated** — it is practicable that satisfaction of the requirement set will lead to the achievement of the entity needs within constraints (cost, schedule, technical, legal and regulatory compliance).

> Careful checking of the requirement set for these characteristics is critical to avoiding **requirements creep** during the life cycle.

### 5.2.7 Requirement language criteria *(normative — full conformance ref.)*

Requirements should state **'what'** is needed, **not 'how'**. They state what is needed for the system-of-interest and **do not include design decisions**.

**Vague and general terms shall be avoided.** They produce requirements difficult or impossible to verify and admit multiple interpretations. Types of unbounded or ambiguous terms:

| Category | Examples to AVOID |
|---|---|
| Superlatives | *best, most* |
| Subjective language | *user friendly, easy to use, cost effective* |
| Vague pronouns | *it, this, that* |
| Ambiguous adverbs / adjectives | *almost always, significant, minimal* |
| Ambiguous logical statements | *or, and/or* — consider multiple requirements when encountering these |
| Open-ended / non-verifiable terms | *provide support, but not limited to, as a minimum* |
| Comparative phrases | *better than, higher quality* |
| Loopholes | *if possible, as appropriate, as applicable* |
| Totality terms | *all, always, never, every* — very difficult to verify |
| Incomplete references | a reference without date / version / applicable parts |

All **assumptions** made regarding a requirement **shall be documented and validated** in one of the requirement's attributes (e.g., *rationale*) or in an accompanying document. Include **definitions as declarative statements, not requirements**.

### 5.2.8 Requirements attributes

#### 5.2.8.1 General

Well-formed requirements should include **descriptive attributes** to support analysis, identification, understanding and management. The attribute information should be associated with the requirement in the chosen requirements repository.

#### 5.2.8.2 Examples of requirements attributes

| Attribute | Definition |
|---|---|
| **Identification** | Unique identifier (number, name tag, mnemonic). May reflect linkages or be separate from them. Unique IDs aid tracing. **Once assigned, the identifier is never changed (even if the requirement changes) and never reused (even if deleted)**. |
| **Version Number** | Of the requirement itself — ensures the correct version is implemented and indicates **volatility** (a requirement that changes a lot can indicate a problem or risk). |
| **Owner** | Person or element of the organisation that maintains the requirement, has the right to say something about it, approves changes and reports status. |
| **Stakeholder Priority** | Established through consensus. A scale such as 1–5 or High / Medium / Low can be used. Priority does not imply that some requirements are unnecessary; it indicates **candidates for the trade space** when alternative decisions are needed. Must consider the stakeholders who need the requirements. |
| **Risk** | Risk value assigned based on risk factors. At-risk requirements include those that fail to have the well-formedness characteristics — risk of failing verification (not implemented) or failing validation (entity needs not realised). Risk can also address feasibility/attainability in terms of technology, schedule, cost, politics. Risk can be **inherited** from a parent requirement. (Cf. ISO/IEC 16085 for additional guidance.) |
| **Rationale** | The reason the requirement is needed; points to supporting analysis, trade study, modelling, simulation or other substantive objective evidence. |
| **Difficulty** | Assumed difficulty (e.g., Easy / Nominal / Difficult). Provides additional context for breadth and affordability; helps cost modelling. |
| **Type** | The kind of requirement — used to identify relevant requirements and to categorise into groups for analysis and allocation. See 5.2.8.3 below. |

#### 5.2.8.3 Examples of the requirements type attribute

| Type | Definition |
|---|---|
| **Functional / Performance** | Functions or tasks to be performed by the system. **Performance is an attribute of function** — a performance requirement alone is incomplete. Performance is normally expressed quantitatively. There can be more than one performance requirement associated with a single function. |
| **Interface** | How the system interacts with external systems (external interface), or how internal system elements / human elements interact (internal interface). External interface requirements state characteristics required at the point of connection — location, geometry, what passes in each direction. |
| **Process Requirements** | Stakeholder (usually acquirer / user) requirements imposed through the contract or statement of work — compliance with laws (national / state / local / environmental), administrative requirements, acquirer/supplier relationship requirements, specific work directives. May also be imposed by corporate policy or practice. Usually captured in project agreement documentation (contracts, statements of work, quality plans). |
| **Quality (Non-Functional) Requirements** | Number of "-ilities": transportability, survivability, flexibility, portability, reusability, reliability, maintainability, security. **The kinds of quality requirements should be identified prior to initiating the requirements activities** and tailored to the system being developed. Measures should be included where appropriate. (Cf. ISO/IEC SQuaRE, especially ISO/IEC 25030 and ISO/IEC 25010.) |
| **Usability / Quality-in-Use Requirements** | For user performance and satisfaction — the basis for design and evaluation of systems to meet user needs. Developed in conjunction with and form part of the overall requirements specification. |
| **Human Factors Requirements** | Required characteristics for outcomes of interaction with human users (and other stakeholders affected by use) in terms of safety, performance, effectiveness, efficiency, reliability, maintainability, health, well-being and satisfaction. Includes measures of usability (effectiveness, efficiency, satisfaction); human reliability; freedom from adverse health effects. |

## 5.3 Practical considerations

### 5.3.1 Application of iteration and recursion

Two forms of process application are essential:

- **Iterative** — same process / set of processes repeated on the **same level** of the system. New information typically takes the form of questions; iteration adds value to the system to which the processes are applied.
- **Recursive** — same processes applied to **successive levels** of system elements within the system structure. Outcomes from one application are inputs to the next lower (or higher) level to arrive at a more detailed / mature set of outcomes.

The stakeholder requirements definition process may only be applied at the system-of-interest level. The requirements, architecture and design processes may be applied at each successive level of recursion.

### 5.3.2 Iteration and recursion in requirements engineering

Different groups of stakeholders view the system from different levels, so requirements must be defined and documented at lower, more detailed levels than the overall system-of-interest. Allocating system requirements to system elements is part of the **Architecture Definition** process and proceeds in parallel with the architecture.

Main forms of appropriate iteration within RE:

- purposeful iteration within requirements analysis;
- planned iteration from downstream activities back to RE because of genuine change of need;
- planned/unplanned iteration back because of feasibility / balance issues arising from technology or implementation risk;
- unplanned iteration back because of other solution issues (changes/defects in non-developmental elements, obsolescence);
- **reverse engineering** of requirements for regulatory compliance;
- limited iteration back because requirements can never be perfect.

**Recursion** is a major strategy for non-trivial systems. Design creates requirements on system elements; design of those creates requirements on lower elements, and so on. **Derived requirements** define relationships between architectural elements, add clarity at lower abstraction levels, or specify design constraints / performance levels on system elements.

> **Critical requirements** (high risk, impacting public safety, environment or health) **should always be analysed more rigorously**.

## 5.4 Requirement information items (overview)

This sub-clause describes the relationship between the requirements processes and the requirement information items by illustrating a typical application style — see **Clause 7** for the normative list of information items and **Clauses 8 and 9** for outlines and content (covered in [clause07-08-information-items.md](clause07-08-information-items.md) and [clause09-information-item-content.md](clause09-information-item-content.md)).
