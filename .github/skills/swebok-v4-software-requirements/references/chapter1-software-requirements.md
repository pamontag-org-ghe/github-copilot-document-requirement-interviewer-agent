# Chapter 1 — Software Requirements

> Source: **SWEBOK Guide v4.0**, Chapter 01 *Software Requirements* (pp. 1-1 → 1-24).
> This file is a cleaned-up, structure-preserving transcription of the chapter for use as a knowledge-base reference. Page numbers `[1-x]` refer to chapter pagination in the source PDF.

## Acronyms

| Acronym | Meaning |
|---|---|
| ATDD | Acceptance Test Driven Development |
| BDD | Behavior Driven Development |
| CIA | Confidentiality, Integrity, and Availability |
| FSM | Functional Size Measurement |
| INCOSE | International Council on Systems Engineering |
| JAD | Joint Application Development |
| JRP | Joint Requirements Planning |
| SME | Subject Matter Expert |
| SysML | Systems Modeling Language |
| TDD | Test Driven Development |
| UML | Unified Modeling Language |

## Introduction `[1-1, 1-2]`

Software requirements should be viewed from two perspectives:

1. an expression of the needs and constraints on a software product or project that contribute to the solution of a real-world problem;
2. the activities necessary to develop and maintain the requirements for a software product and the project that constructs it.

Real-world software projects tend to suffer from two primary requirements-related problems:

1. **Incompleteness** — stakeholder requirements and necessary detail exist but are not revealed and communicated to the software engineers.
2. **Ambiguity** — requirements are communicated in a way that is open to multiple interpretations, with only one possible interpretation being correct.

The role of requirements documentation throughout the service life of the software is to **capture and communicate intent** for software engineers who maintain the code but might not have been its original authors.

The Software Requirements KA provides an understanding that software requirements:

- are not necessarily a discrete front-end activity of the SDLC but rather a process initiated at a project's beginning that often continues to be refined throughout the software's entire service life;
- need to be tailored to the organization and project context.

The whats and hows of software requirements work on a project should be determined by **the nature of the software constructed, not by the life cycle** under which it is constructed.

---

## 1. Software Requirements Fundamentals

### 1.1. Definition of a Software Requirement `[1-2]`

A software requirement is formally defined as:

- a condition or capability needed by a user to solve a problem or achieve an objective;
- a condition or capability that must be met or possessed by a system or system component to satisfy a contract, standard, specification or other formally imposed document;
- a documented representation or capability as in (1) or (2) above.

At its most basic, a software requirement is **a property that must be exhibited to solve a real-world problem**. Clients, customers and users usually impose requirements; however, regulatory authorities, the software organization or the project itself might also impose requirements.

### 1.2. Categories of Software Requirements `[1-3]`

Categories: Software Product Requirements, Software Project Requirements, Functional Requirements, Nonfunctional Requirements (split into Technology Constraints and Quality of Service Constraints).

### 1.3. Software Product Requirements and Software Project Requirements `[1-3]`

- **Software product requirements** specify the software's expected form, fit or function.
- **Software project requirements** (a.k.a. process requirements / business requirements) constrain the project that constructs the software — cost, schedule, staffing, testing environments, data migration, user training, maintenance.

### 1.4. Functional Requirements `[1-4]`

Functional requirements specify **observable behaviors** that the software is to provide — policies to be enforced and processes to be carried out.

Examples (banking): "an account shall always have at least one customer as its owner"; "the balance of an account shall never be negative".

### 1.5. Nonfunctional Requirements `[1-4]`

Nonfunctional requirements constrain the technologies used in the implementation: computing platforms, database engines, accuracy, response time, storage volume, operational characteristics.

Nonfunctional requirements have essential relationships among themselves (positive or negative); whenever one is modified, the impact on others should be considered.

### 1.6. Technology Constraints `[1-4]`

These requirements mandate — or prohibit — use of specific, named automation technologies or defined infrastructures (e.g., Windows, MacOS, Android, iOS, Java, C++, Python, Chrome, Oracle, MySQL, RISC, Relational Database).

### 1.7. Quality of Service Constraints `[1-4, 1-5]`

These specify acceptable performance levels (response time, throughput, accuracy, reliability, scalability). See **ISO/IEC 25010**. **Safety and security** are particularly important and tend to be overlooked (see Security KA).

### 1.8. Why Categorize Requirements This Way? `[1-5]`

Useful because:

- different categories come from different sources;
- elicitation/analysis/specification/validation techniques vary by category;
- different categories affect the resulting software differently;
- divide-and-conquer complexity management;
- distinct areas of expertise can be isolated (business experts vs technology experts).

The **Perfect Technology Filter**: functional requirements are those that would still need to be stated even if a computer with infinite speed, unlimited memory, zero cost, and no failures existed. All other product requirements are constraints on automation technologies and therefore nonfunctional.

### 1.9. System Requirements and Software Requirements `[1-5, 1-6]`

INCOSE definition of *system*: "an interacting combination of elements to accomplish a defined objective. These include hardware, software, firmware, people, information, techniques, facilities, services, and other support elements".

System requirements apply to the larger system (e.g., an autonomous vehicle); software requirements apply only to the software element. Some software requirements may be derived from system requirements.

### 1.10. Derived Requirements `[1-6]`

Requirements can be context-sensitive and perspective-dependent. A **derived requirement** is a requirement not imposed by an external stakeholder but imposed inside the larger development team (e.g., an architect's choice of pipes-and-filters is a design decision from the project view but a requirement for the sub-team building each filter).

### 1.11. Software Requirements Activities `[1-6]`

- **Requirements development** = reaching an agreement on what software is to be constructed (Elicitation, Analysis, Specification, Validation).
- **Requirements management** = maintaining that agreement over time (Scrubbing, Change Control, Scope Matching).

---

## 2. Requirements Elicitation

### 2.1. Requirements Sources `[1-6, 1-7]`

A **stakeholder** is any person, group or organization that is actively involved in the project, is affected by the project's outcome, or can influence the project's outcome.

Typical stakeholders: clients, customers, users (broken into user classes), SMEs, operations staff, first-level product support staff, professional bodies, regulatory agencies, special interest groups, people negatively affected by success, developers.

Working in terms of **stakeholder classes** rather than individuals adds insight. A **stakeholder analysis** reduces bias toward better-represented stakeholders and informs conflict resolution.

Non-person requirements sources: documentation (previous versions, mission statements, concept of operations), other systems, larger business context (organizational policies and processes), computing environment.

### 2.2. Common Requirements Elicitation Techniques `[1-7]`

From stakeholders: interviews; meetings (incl. brainstorming); JAD/JRP and other facilitated workshops; protocol analysis; focus groups; questionnaires and market surveys; exploratory prototyping (low/high-fidelity UI prototyping); user story mapping.

Elicitation is **not a passive activity**. Many product requirements are tacit or can be found only in information that has yet to be collected.

Other sources/techniques: previous versions; defect tracking database; interfacing systems; competitive benchmarking; literature search; QFD House of Quality; observation; apprenticing; usage scenario descriptions; decomposition (capabilities → epics → features → stories); task analysis; design thinking; ISO/IEC 25010; security requirements; applicable standards and regulations.

---

## 3. Requirements Analysis

### 3.1. Basic Requirements Analysis `[1-8]`

Each **individual requirement** should:

- be **unambiguous** (interpretable in only one way);
- be **testable (quantified)** — compliance/noncompliance can be clearly demonstrated;
- be **binding** — clients are willing to pay for it and unwilling not to have it;
- be **atomic** — represent a single decision;
- represent **true, actual stakeholder needs**;
- use **stakeholder vocabulary**;
- be **acceptable to all stakeholders**.

The overall **collection** of requirements should be:

- **complete** — adequately addresses boundary conditions, exception conditions and security needs;
- **concise** — no extraneous content;
- **internally consistent** — no requirement conflicts with any other;
- **externally consistent** — no requirement conflicts with any source material;
- **feasible** — a viable, cost-effective solution can be created within cost, schedule, staffing and other constraints.

**5-whys** technique: repeatedly ask "Why is this the requirement?" to converge on the true problem.

### 3.2. Economics of Quality of Service Constraints `[1-8, 1-9]`

Each QoS constraint has, over its relevant range:

- **Perfection point** — most favorable level beyond which no additional benefit accrues.
- **Fail point** — least favorable level beyond which no further reduction in benefit occurs.

The cost to achieve a level is a step function; the **most cost-effective level** maximizes the positive difference between value and cost. Pay attention to positive/negative relationships between QoS constraints (e.g., modifiability vs raw speed).

### 3.3. Formal Analysis `[1-9, 1-10]`

Formal expression of requirements (formally defined specification language) gives precision and the ability to reason and prove properties (e.g., absence of deadlock). Particularly valuable for high-integrity systems.

### 3.4. Addressing Conflict in Requirements `[1-10]`

Two approaches (among others):

1. **Negotiate a resolution** among conflicting stakeholders (avoid unilateral engineer decisions; preserve traceability back to the customer).
2. **Product family development** — separate **invariant** requirements (agreed by all) from **variant** requirements (conflict exists); use *design to invariants* and *design for change* for customization points.

---

## 4. Requirements Specification `[1-10, 1-11]`

Decisions about whether/how/when to document requirements depend on: domain familiarity, precedent, risk of incorrect requirements, staff turnover, geographic distribution, stakeholder involvement, third-party/open source use, outsourcing, requirements-based testing extent, specification technique effort, estimate accuracy needed, tracing extent, contractual impositions.

Base documentation decisions on an **audience analysis**: who consumes the spec, what info they need, how to package it for minimum effort.

Documented software requirements should be subject to **configuration management** like any other SDLC deliverable, and individual requirements ideally subject to CM and traceability via a requirements management tool. Templates from ISO/IEC/IEEE 29148.

### 4.1. Unstructured Natural Language Requirements Specification `[1-11]`

Statements in common, ordinary language ("The system shall ..."). Business rules count (e.g., "A student cannot register in next semester's courses if there remain any unpaid tuition fees"). User manuals can sometimes serve as the spec, with limits.

### 4.2. Structured Natural Language Requirements Specification `[1-12]`

Imposes structural constraints to increase precision and conciseness. Examples:

- **Actor-action format**: optional triggering event + actor + action + optional condition/qualification.
- **Use case specification template** (Cockburn).
- **User story format**: "As a `<user>` I want `<capability>` so that `<benefit>`".
- Decision tables.

### 4.3. Acceptance Criteria-Based Requirements Specification `[1-12, 1-13]`

Two variants: **ATDD** (part of TDD) and **BDD**.

**ATDD process**:

1. Select a unit of functionality (e.g., a user story) for implementation.
2. Engineers + business domain experts + QA/test professionals meet, before any production design, to agree on a set of test cases that must pass.
3. At least one acceptance test case must fail on the existing software; engineers may then create/modify production code to pass all agreed test cases.

**BDD scenarios** (Gherkin-style): "Given `<context>` [and ...], when `<stimulus>`, then `<outcome>` [and ...]".

Acceptance criteria directly address **ambiguity**. Combined with functional test coverage criteria (Domain Testing, Boundary Value Analysis, Pairwise Testing) they help reduce **incompleteness** too.

### 4.4. Model-Based Requirements Specification `[1-14]`

Modeling languages (selected UML, SysML) reduce inherent natural-language ambiguity. Models fall into two categories:

1. **Structural models** — logical class models (conceptual/logical data models, ERDs).
2. **Behavioral models** — use case modeling, interaction diagrams, state modeling, activity diagrams, data-flow modeling.

Degrees of formality:

1. **Agile modeling** — least formal (sketches; communication > notation).
2. **Semiformal modeling** — defined semantics but not proved complete/consistent.
3. **Formal modeling** — precisely defined semantics (Z, VDM, SDL), enables mechanical analysis. *Correctness by construction*.

### 4.5. Additional Attributes of Requirements `[1-14, 1-15]`

Useful attributes per requirement: tag for tracing, description, rationale, source, use case/triggering event, type, dependencies, conflicts, acceptance criteria, priority, stability, common-or-variant indicator (product family), supporting materials, change history. Gilb's Planguage adds: scale, meter, minimum, target, outstanding, past, trend, record.

### 4.6. Incremental and Comprehensive Requirements Specification `[1-15]`

- **Incremental specification** — only deltas from the previous version (smaller volume).
- **Comprehensive specification** — every version contains all requirements (single reading).

Many organizations combine: incremental intermediate releases (x.1, x.2 …) + comprehensive major releases (1.0, 2.0 …).

---

## 5. Requirements Validation `[1-15]`

Validation seeks confidence that the requirements represent the stakeholders' true needs as currently understood. Key questions: are these all the relevant requirements? are any not representative? are they appropriately stated, understandable, consistent and complete? does the documentation conform to relevant standards?

Three methods: **reviews, simulation/execution, prototyping**.

### 5.1. Requirements Reviews `[1-15, 1-16]`

Reviewers look for errors, omissions, invalid assumptions, lack of clarity, deviation from accepted practice. Review from multiple perspectives:

- **Clients/customers/users** — wants and needs completely and accurately represented;
- **Other requirements specialists** — clear and standards-conformant;
- **Downstream engineers** (architecture/design/construction) — sufficient to support their work.

Provide checklists, quality criteria or a "definition of done" to focus reviewers.

### 5.2. Simulation and Execution `[1-16]`

When stakeholders won't review in detail, simulate or execute the specification (especially model-based specs). Demonstration scenarios convince stakeholders the spec captures their policies/processes.

### 5.3. Prototyping `[1-16]`

When the spec isn't directly executable, build a prototype to demonstrate engineer's interpretation. Useful for dynamic UI behavior. Risk: cosmetic issues can distract reviewers; prototypes can be costly.

---

## 6. Requirements Management Activities `[1-16]`

### 6.1. Requirements Scrubbing `[1-16, 1-17]`

Find the smallest set of simply stated requirements that meet stakeholder needs. Eliminate requirements that are out of scope, would not yield adequate ROI, or are not important. Simplify unnecessarily complicated requirements. In waterfall: scrub just before validation review. In Agile: implicit in iteration planning.

### 6.2. Requirements Change Control `[1-17]`

Plan-based life cycles should have an explicit change control process including:

- a means to **request changes** to previously agreed requirements;
- an optional **impact analysis** stage;
- a **responsible person/group** who accepts, rejects, or defers each change;
- a means to **notify all affected stakeholders** of the decision;
- a means to **track accepted changes to closure**.

All stakeholders must agree that accepting a change means accepting impact on schedule/resources or commensurate scope change. Quantify change in scope objectively (functional size units) where possible. In Agile: changes become backlog items; they are "accepted" by being prioritized into an iteration.

### 6.3. Scope Matching `[1-17]`

Ensure requirements scope does not exceed cost/schedule/staffing constraints. When it does: reduce scope (remove lowest-priority requirements), increase capacity, or negotiate a combination. Prefer quantitative scope matching (functional size units). In Agile: handled by velocity-based sprint planning.

---

## 7. Practical Considerations

### 7.1. Iterative Nature of the Requirements Process `[1-17]`

Real-world projects need both breadth and depth in requirements; teams perform requirements activities iteratively, switching between expanding breadth and depth.

### 7.2. Requirements Prioritization `[1-17, 1-18]`

Helps focus delivery on highest value; supports trade-offs in conflict resolution and scope matching; helps prioritize defect repairs.

Relevant factors: value/desirability/satisfaction; undesirability/dissatisfaction (Kano model); cost to deliver; cost to maintain; technical risk; risk of non-use.

Convert factors to priority via an objective function (e.g., `Priority = (Value × (1 - Risk)) / Cost`). Communicate priority via enumerated scales (must have / should have / nice to have), numerical scales (1..10), or sorted lists. Focus on **groups of requirements with similar priorities**, not rigorous scales.

### 7.3. Requirements Tracing `[1-18, 1-19]`

Two purposes:

1. **Accounting** — for each requirement, are there design elements that satisfy it? for each design element, are there requirements that justify it?
2. **Impact analysis** — trace requirement → linked requirements → design elements → code → test cases to establish change footprint.

Trace **backward** to source documentation (system requirements, standards, specifications) and **forward** to design elements, requirements-based test cases, and user manual sections.

### 7.4. Requirements Stability and Volatility `[1-19]`

Some requirements are stable across the service life; some change after development; some change during the project. Assess likelihood of change to design a more change-tolerant solution.

### 7.5. Measuring Requirements `[1-19]`

Volume of requirements informs new-project sizing, change sizing, cost estimation, and ratios. **Functional Size Measurement (FSM)** and **story points** are common measures. Quality indicators tying requirements quality to cost/acceptance/performance/schedule can be derived from the desirable properties in §3.1.

### 7.6. Requirements Process Quality and Improvement `[1-19, 1-20]`

Assess and improve the requirements process. Aligns with quality standards and process improvement models. Includes:

- requirements process coverage by process improvement standards and models;
- requirements process measures and benchmarking;
- improvement planning and implementation;
- **security / CIA** improvement planning and implementation.

---

## 8. Software Requirements Tools `[1-20]`

Three categories: management tools, modeling tools, functional test case generation tools.

### 8.1. Requirements Management Tools `[1-20]`

Storing requirement attributes, tracing, document generation, change control. Tracing and change control may be practical **only** when tool-supported. Many organizations still use ad-hoc/spreadsheet approaches (less satisfactory).

### 8.2. Requirements Modeling Tools `[1-20]`

Visually create/modify/publish model-based specs; some perform static analysis (syntax, completeness, consistency). Formal analysis tools fall into theorem provers or model checkers; neither fully automates proof. Some tools dynamically execute (simulate) a specification.

### 8.3. Functional Test Case Generation Tools `[1-20]`

The more formal the spec language, the more mechanically derivable test cases become (e.g., BDD → tests; state models → positive tests for defined transitions, negative tests for undefined state/event combinations). Tools generally generate only inputs; expected results still need domain expertise.
