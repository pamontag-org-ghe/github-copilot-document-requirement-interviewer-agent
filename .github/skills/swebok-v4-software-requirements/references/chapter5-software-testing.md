# Chapter 5 — Software Testing (requirements-relevant extract)

> Source: **SWEBOK Guide v4.0**, Chapter 05 *Software Testing* (pp. 5-1 → 5-35).
> This file is a cleaned, structure-preserving extract of the testing material that is **directly relevant when eliciting, specifying and validating software requirements**: testing fundamentals, test levels, testing objectives (conformance, compliance, security, privacy, usability, performance, etc.) and the role of acceptance criteria in disambiguating requirements. Process, tools and technique-internal sections (3.x structural & mutation testing, 5–8 test process and tools) are intentionally summarised or omitted.
> Page numbers `[5-x]` refer to chapter pagination in the source PDF.

## Acronyms (subset)

| Acronym | Meaning |
|---|---|
| ATDD | Acceptance Test-Driven Development |
| BDD  | Behavior Driven Development |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| KPI  | Key Performance Indicator |
| MTTR | Mean Time to Recovery |
| OAT  | Orthogonal Array Testing |
| SoS  | System of Systems |
| SUT  | System Under Test |
| TDD  | Test-Driven Development |

## Introduction `[5-1, 5-2]`

Software testing consists of the **dynamic validation that a System Under Test (SUT) provides expected behaviors on a finite set of test cases suitably selected from the usually infinite execution domain**.

Key terms:

- **SUT** — program, product, application, service composition, system, system of systems or ecosystem under test.
- **Test case** — specification of input values, execution/timing conditions, procedure and expected outcomes. A set of test cases is a **test suite**.
- **Dynamic** — testing requires execution. Static techniques complement it (covered in the Quality KA).
- **Finite** — exhaustive testing is infeasible; testing is always a trade-off between resources and coverage.
- **Selected** — selection criteria include risk analysis, **software requirements**, cost reduction, quality attribute satisfaction, prioritisation, fault detection.
- **Expected** — observed outcomes are checked against user needs (**validation**), specifications (**verification**) or implicit expectations. (See Acceptance Criteria-Based Requirements Specification — Software Requirements KA §4.3.)

Testing is **pervasive and holistic**: it accompanies every step of the development life cycle (including shift-left).

---

## 1. Software Testing Fundamentals

### 1.1. Faults vs. Failures `[5-3]`

- **Fault** — cause of malfunction (defect inserted by a human error).
- **Failure** — observed undesired effect in the delivered service.
- Testing reveals failures; the *faults* that cause them are what must be removed. A failure's cause cannot always be unequivocally identified.

### 1.2. Key Issues (selected) `[5-3 → 5-6]`

- **1.2.4 Purpose of Testing** — a test suite can only be generated, executed and evaluated against a specific, stated purpose.
- **1.2.5 Assessment and Certification** — tests must focus on mandatory prescriptions (requirements, laws, standards). Evidence must come from test cases derived from baseline requirements, under configuration control, with repeatable processes.
- **1.2.6 Testing for Quality Assurance / Improvement** — testing measures or assesses the quality characteristics defined in **ISO/IEC 25010** (see Quality KA).
- **1.2.7 The Oracle Problem** — a test is meaningful only if its outcome can be decided. Oracles include **unambiguous requirements specifications**, behavioural models and code annotations. Verdicts are pass / fail / inconclusive.
- **1.2.8 Theoretical & Practical Limitations** — Dijkstra: *"program testing can be used to show the presence of bugs, but never to show their absence"*.
- **1.2.10 Testability** — ease with which a coverage criterion can be satisfied; likelihood that a test suite exposes a failure if the software is faulty. **Both meanings matter when writing requirements.**
- **1.2.12 Scalability** — software's ability to scale on non-functional requirements (load, transactions, data volume) and across distributed/wireless/virtualised/cluster/cloud environments.
- **1.2.15 Offline vs Online Testing** — offline = no external interaction; online = real application environment.

---

## 2. Test Levels

Levels are distinguished by the **target** (object) of the test or by its **objective** (purpose). Both decisions shape what acceptance criteria a requirement must carry.

### 2.1. The Target of the Test `[5-6, 5-7]`

Four stages — **no precedence implied**:

- **2.1.1 Unit Testing** — verifies individual SUT elements (subprograms, components, subsystems) in isolation. Usually performed by the code author.
- **2.1.2 Integration Testing** — verifies interactions between SUT elements; strategies are top-down, bottom-up, sandwich, big bang; covers interoperability, compatibility, configuration and external interfaces to other apps/utilities/hardware/operating environments.
- **2.1.3 System Testing** — tests SUT behaviour as a whole. **Considered appropriate for assessing non-functional system requirements** (security, privacy, speed, accuracy, reliability). (Cross-reference: Functional & Non-Functional Requirements — Software Requirements KA.)
- **2.1.4 Acceptance Testing** — targets the SUT deployment. Main goal: verify that the SUT **satisfies the requirements and the end-users' expectations**. Run by/with end-users. May target usability testing or operational acceptance. **Defining acceptance tests before implementing the corresponding functionality is the key activity of ATDD** (see SR KA §4.3).

### 2.2. Objectives of Testing `[5-7 → 5-10]`

Objectives must be stated **precisely and quantitatively** to support measurement and control. The test objective varies with the test target.

- **2.2.1 Conformance Testing** — SUT conforms to standards, rules, specifications, requirements, design, processes or practices.
- **2.2.2 Compliance Testing** — SUT adheres to a **law or regulation** (forced by an external regulatory body — e.g., GDPR, HIPAA).
- **2.2.3 Installation Testing** — system testing in the operational hardware/environment; verifies installation procedures.
- **2.2.4 Alpha / Beta Testing** — small selected group / larger representative group, before release; often uncontrolled.
- **2.2.5 Regression Testing** — selective re-testing after modification to verify that the SUT still complies with its specified requirements and that no unintended effects were introduced. Fundamental to Agile, DevOps, TDD, Continuous Delivery. May involve functional and non-functional re-testing (reliability, accessibility, usability, maintainability, conversion, migration, compatibility).
- **2.2.6 Prioritization Testing** — schedule test cases to increase rate/likelihood of fault detection, coverage, reliability.
- **2.2.7 Non-Functional Testing** — hundreds of techniques, including:
  - **Performance** — meets specified performance requirements; assesses capacity, response time.
  - **Load** — SUT behaviour under load pressure to discover deadlocks, races, buffer overflows, memory leaks, reliability/stability/robustness violations.
  - **Stress** — push the SUT beyond expected capabilities.
  - **Volume** — internal storage limits, data exchange capacity.
  - **Failover / Recovery** — manage heavy loads or failures and continue operations; recovery from crash or disaster.
  - **Reliability** — observe SUT in operation or exercise via operational-profile statistical models; uses reliability growth models.
  - **Compatibility** — collaborate with different hw/sw facilities and versions.
  - **Scalability** — scale up non-functional requirements (load, transactions, volume).
  - **Elasticity** — rapidly expand/shrink compute/memory/storage (esp. cloud).
  - **Infrastructure** — IT infrastructure components.
  - **Back-to-Back** — same input on two or more program variants; compare outputs.
- **2.2.8 Security Testing** — protection from external attacks; verifies **Confidentiality, Integrity, Availability**; includes misuse/abuse (negative) testing. (See Security KA.)
- **2.2.9 Privacy Testing** — security and privacy of users' personal data; validates privacy / information-sharing policies, decentralised social profile management and data storage solutions. (See Legal Issues — Professional Practice KA.)
- **2.2.10 Interface and API Testing** — components' interfaces exchange data/control correctly; test cases derived from the interface specification; for APIs, simulate end-user app calls (parameters, environment conditions, internal data).
- **2.2.11 Configuration Testing** — verifies the SUT under each supported configuration.
- **2.2.12 Usability / Human-Computer Interaction Testing** — ease of learning to use; covers functions supporting user tasks, user-aiding documentation, and recovery from user errors. (See User-Centered Design — Software Design KA.)

---

## 3. Test Techniques (requirements-relevant subset)

### 3.1.2 Boundary Value Analysis `[5-11]`

Test cases chosen on/near the boundaries of input domain variables (faults concentrate there). **Robustness testing** extends this with values outside the input domain.

### 3.1.4 Combinatorial Test Techniques `[5-11]`

All-combinations, t-wise (incl. **pair-wise / OAT**), each-choice, base-choice — systematically derive test cases that cover specific parameter combinations. Useful when many configuration parameters interact.

### 3.1.5 Decision Tables `[5-11]`

Logical relationships between conditions (inputs) and actions (outputs). Test cases derived by considering every possible combination of conditions. Related: **cause-effect graphing**. Strongly aligned with shift-left development for documenting test results.

### 3.1.7 State Transition Testing `[5-12]`

Represent the SUT as a finite-state machine; cover states and transitions at a specific coverage level. Useful when requirements describe modal behaviour.

### 3.1.8 Scenario-Based Testing `[5-12]`

A model is an abstract (formal) representation of the SUT or its software requirements. Scenario-based testing **validates requirements, checks their consistency, and generates test cases focused on the SUT's behavioural aspects**. Workflows graphically represent activity sequences (typical *and* alternate workflows must be tested). Business process testing is a scenario-based variant focused on workflow roles.

### 3.1.9 Random Testing & Fuzz Testing `[5-12]`

Test cases drawn at random from the (known) input domain. **Fuzz testing** — random selection of invalid/unexpected inputs and data — is extensively used in cybersecurity to find hackable bugs, coding errors and security loopholes. (See §2.2.8.)

### 3.1.11 Forcing Exception `[5-12]`

Test cases conceived to exercise predefined exceptions/errors (data, operation, overflow, protection, underflow). Focus on negative test scenarios.

### 3.5 Usage-Based Techniques `[5-15]`

Rely on a **usage model or operational profile**. The testing environment must represent the actual operational environment; execution must reproduce real usage. Applied mostly at acceptance.

- **3.5.1 Operational Profile** — estimate reliability of the SUT (or part of it) from observed test results; requires deriving real operational profiles.
- **3.5.2 User Observation Heuristics** — usability inspection: cognitive walkthroughs, claims analysis, field observations, thinking aloud, questionnaires, interviews.

### 3.6 Techniques Based on the Nature of the Application `[5-15, 5-16]`

Different test derivation/execution techniques apply depending on the nature of the software: object-oriented, component-based, web-based, concurrent, protocol-based, communication, real-time, **safety-critical**, service-oriented, open-source, embedded, cloud-based, blockchain-based, big-data, **AI/ML/DL-based**, mobile apps, **security & privacy-preserving** software. Standards such as **ISO/IEC/IEEE 29119** support specifying test cases, automating execution and maintaining suites.

---

## 4. Test-Related Measures (selected) `[5-16, 5-17]`

- **Coverage** measures vary 0–100 % (excluding infeasible tests). Examples: % of branches in the program flow graph, **% of functional requirements exercised among those listed in the specifications document**.
- **KPIs** for evaluating the SUT: deployment frequency, lead time, MTTR, change failure rate (shift-left).
- **Fault density** — faults found / SUT size. Variants: fault depth, fault multiplicity.
- **Reliability growth models** — failure-count and time-between-failure families.
- **Mutation score** — killed mutants / generated mutants; estimates test-suite effectiveness.

---

## 6. Software Testing in the Development Processes and Application Domains (summary)

- Testing is integrated across the development process; in shift-left (Agile/DevOps) it is continuous and automated.
- Application domains imposing additional, mandatory requirements-related testing: **avionics (DO-178C), railway (EN 50128), medical (HIPAA, HL7, FHIR, DICOM, IEC 62304), automotive (ISO 26262), data protection (GDPR)**. These laws/standards directly create **compliance requirements** (see §2.2.2).

---

## Cross-references back to the Software Requirements KA

- **§2.1.4 Acceptance Testing** ⇄ SR KA §4.3 *Acceptance Criteria-Based Requirements Specification* (ATDD/BDD).
- **§2.1.3 System Testing** ⇄ SR KA §1.4–1.5 *Functional / Non-Functional Requirements*.
- **§2.2.2 Compliance Testing** ⇄ SR KA §2.1 *Requirements Sources* (regulators) and §3.1 *external consistency* with regulations.
- **§3.1.8 Scenario-Based Testing** ⇄ SR KA §4.2 *Structured Natural Language* (use cases, scenarios).
- **§1.2.7 Oracle** ⇄ SR KA §3.1 *unambiguous and testable*.
- **§2.2.8 Security Testing** ⇄ SR KA §1.7 *QoS Constraints — safety & security* and Security KA §4.1 *Security Requirements*.
