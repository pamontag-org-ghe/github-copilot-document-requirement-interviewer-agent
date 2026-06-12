# Chapter 12 — Software Quality (requirements-relevant extract)

> Source: **SWEBOK Guide v4.0**, Chapter 12 *Software Quality* (pp. 12-1 → 12-18).
> This file is a cleaned, structure-preserving extract of the quality material that is **directly relevant when eliciting and specifying software quality (nonfunctional / Quality of Service) requirements**: the quality model, dependability, integrity levels, and the V&V tasks that act on requirements. Process-management subsections (SQA planning, audits, CoSQ) are summarised or omitted.
> Page numbers `[12-x]` refer to chapter pagination in the source PDF.

## Acronyms (subset)

| Acronym | Meaning |
|---|---|
| CoSQ | Cost of Software Quality |
| FMEA | Failure Mode and Effects Analysis |
| FTA  | Fault Tree Analysis |
| IV&V | Independent Verification and Validation |
| QFD  | Quality Function Deployment |
| QMS  | Quality Management System |
| SQA  | Software Quality Assurance |
| SQM  | Software Quality Management |
| V&V  | Verification and Validation |

## Introduction `[12-1, 12-2]`

Software quality is overloaded: it refers to (a) desirable characteristics of products, (b) the extent to which a product has them (**software product quality**), and (c) the processes/tools/techniques used to achieve them (**software process quality**).

Modern definitions:

- *"Capability of a software product to satisfy stated and implied needs under specified conditions"*.
- *"The degree to which a software product meets established requirements; however, quality depends upon the degree to which those established requirements accurately represent stakeholder needs, wants, and expectations"*.

Both definitions embrace **conformance to requirements** — and therefore make the quality of the requirements themselves a primary quality concern.

**Software quality requirements** (a.k.a. *the "-ilities"*, *Quality of Service Constraints* in the SR KA) are attributes of or constraints on functional requirements. They specify *how well* the system performs *what* it does.

---

## 1. Software Quality Fundamentals

### 1.0 Core terminology `[12-3]`

- **Error** — human action that produces an incorrect result.
- **Defect (= fault)** — imperfection/deficiency in a work product that does not meet its requirements or specifications; inserted when a developer makes an error.
- **Failure** — termination of the ability of a system to perform a required function (or operation outside specified limits); produced when the software executes a defect.

The software requirements are expected to **define the required software quality attributes**, and they influence the **measurement methods and acceptance criteria** by which quality is assessed.

### 1.2 Value and Cost of Quality `[12-4]`

**Cost of Software Quality (CoSQ)** = implementation cost + **prevention cost** (process improvement, tools, training) + **appraisal cost** (reviews, audits, testing) + **nonconformance / rework cost** (pre- and post-delivery rework, customer impact, public/environmental impact). Goal: optimal CoSQ — minimal total cost for the specified quality level.

### 1.3 Standards, Models, Certifications `[12-4, 12-5]`

Key standards directly relevant when eliciting quality requirements:

- **ISO/IEC/IEEE 12207:2017** — software life-cycle processes.
- **IEEE 730:2014** — SQA plans; adaptation to Agile.
- **IEEE 1228:1994** — Software Safety Plans (safety-related industries).
- **IEEE 1633:2016** — Software Reliability (reliability-critical industries).
- **ISO 9001 / ISO 27001 / ISO 20000** — registrations for quality / security / IT-service management.
- Industry-specific frameworks: **COBIT, PMBOK, BABOK, CMMI, TOGAF**.

Choice of standards drives **compliance requirements** that must end up in the SRS.

### 1.4 Software Dependability and Integrity Levels `[12-5, 12-6]`

**Safety-critical systems** = systems whose failure can harm human life, other living things, physical structures, or the environment. Domain examples: transportation, chemical, nuclear, medical devices.

Three complementary techniques for reducing failure risk that **drive requirements**:

1. **Avoidance**.
2. **Detection and removal**.
3. **Damage limitation**.

They impact functional requirements, performance requirements and development processes. Higher risk → more SQA, more formal inspection of requirements/design/code, more formal V&V, and possibly an **assurance case** (auditable artifact of claims + arguments + evidence).

#### 1.4.1 Dependability `[12-5, 12-6]`

When failures can have severe consequences, **dependability** (aside from raw functionality) is the dominant quality requirement. It regroups: **availability, reliability, maintainability and supportability, safety, security**.

#### 1.4.2 Integrity Levels of Software `[12-6]`

An **integrity level** is a value representing project-unique characteristics (complexity, criticality, risk, safety level, security level, desired performance, reliability) that define the importance of the system/software/hardware to the user.

- Integrity levels may change as the software evolves.
- They are set by agreement among acquirer, supplier, developer and independent assurance authorities.
- In safety-critical industries (avionics, railways, nuclear, medical, …) industry-specific guidance can **require certain V&V techniques per integrity level** (usability analysis, algorithm analysis, **boundary value analysis**, data flow analysis, walk-through review).

---

## 2. Software Quality Management Process (summary)

**SQM** coordinates activities to direct and control the organisation with regard to software quality. The **Quality Management System (QMS)** — per ISO 90003 — defines processes, owners, requirements, measurements, and feedback channels across the life cycle. Activities: **SQA, V&V, reviews and audits, software configuration management (SCM)**. Requires management sponsorship.

---

## 3. Software Quality Assurance Process

### 3.3 Perform Product Assurance `[12-11, 12-12]`

Software engineers are responsible for:

1. **Eliciting quality requirements** that might not be explicit at the outset.
2. Understanding their importance and the difficulty in **defining, measuring, and establishing them for final acceptance**.
3. Defining **quality targets** so they can effectively be measured at acceptance.
4. **Anticipating additional development costs** when safety, security, dependability are important.

The international standard for measurable quality characteristics is **ISO/IEC 25010**. It proposes:

- a **software product quality model**, and
- a **quality-in-use model**,

both made of **characteristics and sub-characteristics**. These characteristics — commonly called **product quality requirements** — are non-functional software requirements.

> **ISO/IEC 25010 product quality characteristics** (the eight "-ilities" most engineers must know): **Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability**.

Engineers must also know that **quality characteristics have conflicting impacts** (e.g., adding encryption to strengthen *security* can degrade *performance*). The standard also defines a **data quality model** for data used by humans and systems.

#### Work-product quality

Beyond the final product, **work products** themselves (system/subsystem specifications, software requirements specifications, software design descriptions, source code, test docs, test reports) must be evaluated via **reviews and inspections** throughout the engineering process.

### 3.4 V&V and Testing `[12-12, 12-13]`

- **Verification** — *building the product correctly* — outputs of a life-cycle phase satisfy the conditions imposed at the start of that phase.
- **Validation** — *building the right product* — the product fulfills its specific intended purpose; determines whether it satisfies specified requirements.

V&V (per **IEEE 1012:2016**) must demonstrate the requirements are **correct, complete, accurate, consistent and testable**. V&V begins early in development or maintenance to prevent late-cycle defects.

Engineers should identify the **product integrity level** and ensure **minimum V&V tasks** are assigned to key product features. **Traceability** among software work products augments V&V quality and is mandatory for impact analysis on requirements changes.

---

## Cross-references back to the Software Requirements KA

- **§1.4 Dependability** ⇄ SR KA §1.7 *Quality of Service Constraints* and Security KA §1.2 *Information Security (CIA)*.
- **§1.4.2 Integrity Levels** ⇄ SR KA §7.2 *Requirements Prioritization* and §7.4 *Stability and Volatility*.
- **§3.3 Quality Requirements** ⇄ SR KA §1.5 / §1.7 *Nonfunctional & QoS* and §3.2 *Economics of QoS (fail & perfection points)*.
- **§3.4 V&V** ⇄ SR KA §5 *Requirements Validation* (reviews, simulation, prototyping) and §7.3 *Requirements Tracing*.
- **ISO/IEC 25010** is the canonical reference for the *non-functional* portion of any SRS section 6 (Quality Attributes) and for §6.x QoS targets defined with fail/perfection points.
