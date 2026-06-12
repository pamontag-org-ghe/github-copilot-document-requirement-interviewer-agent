# Clauses 7 & 8 — Information Items and Outlines (ISO/IEC/IEEE 29148:2018)

> Source: **ISO/IEC/IEEE 29148:2018**, Clause 7 *Information items* (p. 50) and Clause 8 *Guidelines for information items* (pp. 51–57).
> This file lists the **four normative information items** that a conforming project must produce, and the **example outlines** for each. For the detailed normative content of each section, see [clause09-information-item-content.md](clause09-information-item-content.md).

## 7 Information items *(normative)*

The project **shall produce** the following information items as part of the requirements engineering processes:

| Acronym | Information item | When |
|---|---|---|
| **BRS** | Business Requirements Specification | Always |
| **StRS** | Stakeholder Requirements Specification | Always |
| **SyRS** | System Requirements Specification | Always |
| **SRS** | Software Requirements Specification | If adhering to **ISO/IEC/IEEE 12207** |

The Software Requirements Specification can also be identified as the *System/Software Requirements Specification*.

The information items **shall contain the content as defined in Clause 9** of the standard.

### Important practical notes (Clause 7 NOTES)

- **Multiple specification information items** for each of the four document types **can be produced** in the project (e.g., one SyRS per system element).
- The four specification items **can contain similar information** that could be considered as different views for the same product. The standard presents typical contents separately **for ease of use**.
- The **BRS and StRS** can have different titles in different domains and can be contained in other information items, as long as the functionality of these specifications can be clearly referenced.
- The management of information items **shall be performed by applying the Information Management process** of ISO/IEC/IEEE 15288 and ISO/IEC/IEEE 12207.
- **Information items do not require physical documentation** so long as required content is easily available and logically organised. *Example: Model-Driven Development (MDD) approaches maintain almost all system information in a modelling tool — contextually stored in the modelling tool's repository, viewable in the model or extractable as reports / tables.*

---

## 8 Guidelines for information items

### 8.1 Requirements information item outlines

Clause 8 provides **recommended structure** in the form of an **example outline** for each of the four information items.

The specific requirements clause of each information item **should be organised** such that a consensus of stakeholders agrees that the organisation method aids understanding of the requirements. **There is no one optimal organisation for all projects.**

### 8.2 Business Requirements Specification (BRS)

#### 8.2.1 Purpose

The **BRS** describes:

- the **organisation's motivation** for why the system is being developed or changed;
- the **processes and policies / rules** under which the system is used;
- the **top-level requirements from the stakeholder perspective**, including the needs of users / operators / maintainers as derived from the context of use, in a specific, precise, unambiguous manner.

In a business environment, the BRS describes how the organisation pursues new business or changes the current business to fit a new business environment, and how to utilise the system as a means to contribute to the business.

It should describe (at the organisation level): organisational environment, goals and objectives, business model, information environment. And (at the business operation level): business operation model, business operation modes, business operational quality, organisational formation, and concept of the proposed system.

> **It is very important that business management actively participates or leads the development of the BRS.** The information elements should be specified by the business; business management should be responsible for the content of the specification.

Typical types of requirements in the BRS: **organisational requirements and business requirements**.

NOTE — The BRS is often **identified with the StRS** in many industries; users of this document **can combine the StRS with the BRS** according to the users' environment.

#### 8.2.2 BRS example outline

Detailed content per section is in [clause09-information-item-content.md](clause09-information-item-content.md) §9.3.

```
1. Business purpose
2. Business scope
3. Business overview
4. Major stakeholders
5. Business environment
6. Mission, goals and objectives
7. Business model
8. Information environment
9. Business processes
10. Business operational policies and rules
11. Business operational constraints
12. Business operational modes
13. Business operational quality
14. Business structure
15. High-level operational concept
16. High-level operational scenarios
17. Other high-level life-cycle concepts
18. Project constraints
```

### 8.3 Stakeholder Requirements Specification (StRS)

#### 8.3.1 Purpose

Same overall intent as the BRS but from the **stakeholders' perspective**: in the context described in the BRS, the StRS describes how the organisation will utilise the system as a means to contribute to the business. The information elements should be specified by the stakeholders; the stakeholders should be responsible for the content.

Typical types in the StRS: **organisational, business, and user requirements**.

NOTE — The StRS is often **identified with the BRS** in many industries; combination is allowed.

#### 8.3.2 StRS example outline

Detailed content per section is in [clause09-information-item-content.md](clause09-information-item-content.md) §9.4.

```
1. Stakeholder purpose
2. Stakeholder scope
3. Overview
4. Stakeholders
5. Business environment
6. Mission, goals and objectives
7. Business model
8. Information environment
9. System processes
10. System operational policies and rules
11. Operational constraints
12. System operational modes and states
13. System operational quality
14. User requirements
15. Operational concept
16. Operational scenarios
17. Other detailed concepts of proposed system
18. Project constraints
```

### 8.4 System Requirements Specification (SyRS)

#### 8.4.1 Purpose

The **SyRS** identifies the **technical requirements for the selected system-of-interest** and the **usability for the envisaged human-system interaction**. Defines high-level system requirements from the **domain perspective**, with background information about overall objectives, target environment, and constraints / assumptions / non-functional requirements. May include conceptual models illustrating system context, usage scenarios, principal domain entities, data, information and workflows.

Purpose: **describe what the system should do**, in terms of the system's interactions / interfaces with its external environment. The SyRS should **completely describe all inputs, outputs and required relationships between inputs and outputs**.

The SyRS bridges acquirer and technical community — its representation must be **understandable by both**. The standard distinguishes between the structured collection of information and the way it is presented; **all presentations** (paper, models, prototypes, …) **shall be traceable to a common source of system requirements information**.

> Generally, **process requirements** (how to develop / construct the system) should be contained in **contract documentation** such as a Statement of Work, **not** in a requirements specification. If included in a specification, they should be clearly identified as process requirements.

The SyRS outline can be used (with tailoring) for **subordinate specifications for system elements, even those that include software**.

#### 8.4.2 SyRS example outline

Detailed content per section is in [clause09-information-item-content.md](clause09-information-item-content.md) §9.5.

```
1. System purpose
2. System scope
3. System overview
   3.1 System context
   3.2 System functions
   3.3 User characteristics
4. Functional requirements
5. Usability requirements
6. Performance requirements
7. System interface requirements
8. System operations
   8.1 Human system integration requirements
   8.2 Maintainability requirements
   8.3 Reliability requirements
   8.4 Other quality requirements
9. System modes and states
10. Physical characteristics
    10.1 Physical requirements
    10.2 Adaptability requirements
11. Environmental conditions
12. System security requirements
13. Information management requirements
14. Policy and regulation requirements
15. System life cycle sustainment requirements
16. Packaging, handling, shipping and transportation requirements
17. Verification
18. Assumptions and dependencies
```

### 8.5 Software Requirements Specification (SRS)

#### 8.5.1 Purpose

The **SRS** is a specification for a **particular software product, program, or set of programs** that performs certain functions in a specific environment. May be written by representatives of the supplier, the acquirer, or both.

When the software is **part of a larger system**, the higher-level system specification states the interfaces and the external performance / functionality requirements; the SRS **should agree with and expand upon** those system requirements.

The SRS indicates the **precedence and criticality** of requirements. It defines all required capabilities of the specified software, the conditions and constraints under which the software has to perform, and the **intended verification approaches**.

#### 8.5.2 SRS example outline

Detailed content per section is in [clause09-information-item-content.md](clause09-information-item-content.md) §9.6.

```
1. Purpose
2. Scope
3. Product perspective
   3.1 System interfaces
   3.2 User interfaces
   3.3 Hardware interfaces
   3.4 Software interfaces
   3.5 Communications interfaces
   3.6 Memory constraints
   3.7 Operations
   3.8 Site adaptation requirements
   3.9 Interfaces with services
4. Product functions
5. User characteristics
6. Limitations
7. Assumptions and dependencies
8. Apportioning of requirements
9. Specified requirements
   9.1 External interfaces
   9.2 Functions
   9.3 Usability requirements
   9.4 Performance requirements
   9.5 Logical database requirements
   9.6 Design constraints
   9.7 Standards compliance
   9.8 Software system attributes
       (Reliability, Availability, Security, Maintainability, Portability)
   9.9 Verification
   9.10 Supporting information
```

#### Common organisational approaches for SRS specific requirements

The "specified requirements" clause can be organised by:

- **System mode** — e.g., training / normal / degraded / emergency.
- **User class** — e.g., passengers / maintenance / firefighters for an elevator system.
- **Objects** — real-world entities (patients, sensors, rooms, …) with attributes and functions/methods/services.
- **Feature** — externally desired service requiring a sequence of inputs; typically described as stimulus-response pairs.
- **Stimulus** — by stimuli (loss of power, wind shear, …).
- **Response** — by all functions supporting the generation of a response.
- **Functional hierarchy** — hierarchy organised by common inputs / outputs / internal data access.

> Notations align with the organisation: state machines / state charts for mode-organised; OO analysis for object-organised; stimulus-response sequences for feature-organised; data-flow diagrams + data dictionaries for hierarchy-organised.
