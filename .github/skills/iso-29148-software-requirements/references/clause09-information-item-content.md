# Clause 9 — Information Item Content (ISO/IEC/IEEE 29148:2018)

> Source: **ISO/IEC/IEEE 29148:2018**, Clause 9 *Information item content* (pp. 57–74).
> This is the **normative content** of each of the four required information items. The project shall produce content in accordance with the project's information-management policies; section order and structure may be selected accordingly.

## 9.2 General content (applicable to all information items)

| Section | Required content |
|---|---|
| **9.2.1 Identification** | (a) **title**; (b) **revision notice**. Revision information may include project name, version number, date of release, approved signature, list of sub-clauses changed in the current version, and list of version numbers and dates of release of all previous versions. |
| **9.2.2 Front matter** | (a) **table of contents**; (b) **list of figures**; (c) **list of tables**. |
| **9.2.3 Definitions** | Definitions for any words or phrases with special meaning beyond normal dictionary definitions. |
| **9.2.4 References** | (a) complete list of all documents referenced elsewhere; (b) title, report number (if applicable), date, publishing organisation per document; (c) sources from which references can be obtained. **Subdivide** into *Compliance* (cited documents containing requirements that apply by citation) and *Guidance* (cited documents containing information but no requirements). |
| **9.2.5 Acronyms and abbreviations** | Spell out / define all acronyms and abbreviations used. |

---

## 9.3 Business Requirements Specification (BRS) content

| Section | Required content |
|---|---|
| **9.3.1 BRS overview** | The project shall produce the BRS content in accordance with project policies. Organisation of the content (order / section structure) may be selected. |
| **9.3.2 Business purpose** | Reason and background — why the organisation is pursuing new business or changing the current business; how the proposed system will contribute to meeting business objectives. |
| **9.3.3 Business scope** | (a) identify the business domain by name; (b) define the range of business activities included — divisions and external entities that relate directly, or functions to be performed; show environmental entities outside scope; (c) describe the scope of the system being developed or changed, including assumptions on which business activities are supported. |
| **9.3.4 Business overview** | Major internal divisions and external entities of the business domain and how they are interrelated. **Diagrammatic description recommended.** |
| **9.3.5 Major stakeholders** | List major stakeholders or classes of stakeholders; describe how they influence the organisation and business or are related to development and operation. |
| **9.3.6 Business environment** | External and internal environmental factors to be considered in understanding the new or existing business and eliciting stakeholder requirements — market trends, laws and regulations, social responsibilities, technology base. |
| **9.3.7 Mission, goals and objectives** | Business results to be obtained through or by the proposed system. |
| **9.3.8 Business model** | Methods by which the business mission is expected to be achieved — products and services, geographies / locales, distribution channels, business alliances and partnerships, finance and revenue model. (Cf. OMG Business Motivation Model.) |
| **9.3.9 Information environment** | Overall strategy for organisation-level decisions on common bases for multiple information systems: (a) information portfolio (long-term strategy); (b) common system infrastructure / architecture decisions as constraints; (c) database configuration plan and constraints on availability and accessibility of organisation-global data. |
| **9.3.10 Business processes** | Procedures of business activities and possible system interfaces within the processes. Decomposition and classification; each business process **uniquely named and numbered**; described as a diagram representing a sequence of activities. |
| **9.3.11 Business operational policies and rules** | Logical propositions applied in conducting the business processes — conditions to start/branch/terminate, criteria for judgement, formulas. Likely to become functional requirements in SyRS/SRS. **Uniquely named and numbered; referenced in the business processes description.** |
| **9.3.12 Business operational constraints** | Conditions imposed on the business processes — performance constraints (e.g., "finished within a day after triggering event") or management requisites (e.g., "every occurrence shall be monitored and recorded"). |
| **9.3.13 Business operational modes** | Methods to conduct business operation in **unsteady states** (extremely busy due to event spikes; manual operation when the proposed system is unavailable). |
| **9.3.14 Business operational quality** | Quality level required for the business operation (e.g., urgency over reliability). Includes high-level objectives for **usability and quality-in-use** (effectiveness, efficiency, satisfaction, freedom from risk). |
| **9.3.15 Business structure** | Structures relevant to the system — organisational, role/responsibility, geographic, resource sharing. |
| **9.3.16 High-level operational concept** | Proposed system in a high-level manner without design details: (a) operational policies and constraints; (b) description of proposed system; (c) modes of system operation; (d) user classes and other personnel; (e) support environment. Detailed content of the System Operational Concept is in Annex A. |
| **9.3.17 High-level operational scenarios** | How users / operators / maintainers will interact with the system in important contexts of use. **Uniquely named and numbered; referenced in business-processes description.** |
| **9.3.18 Other high-level life-cycle concepts** | How the system-of-interest is to be acquired, deployed, supported and retired. |
| **9.3.19 Project constraints** | Constraints to performing the project within cost and schedule. |

---

## 9.4 Stakeholder Requirements Specification (StRS) content

> Sections 9.4.2 – 9.4.9 are **substantially the same as 9.3.2 – 9.3.9** because the StRS describes the same context from the stakeholders' perspective. The novel sections are highlighted below.

| Section | Required content (differences and new sections) |
|---|---|
| **9.4.10 System processes** | How and in which context the system supports business activities — flowing from the ordered business processes. Each system process **uniquely named and numbered**; described as a sequence-of-activities diagram. |
| **9.4.11 System operational policies and rules** | How business operational policies and rules will likely be addressed in functional requirements in SyRS/SRS. **Uniquely named and numbered; referenced in business-processes description.** |
| **9.4.12 Operational constraints** | System conditions and functional requirements imposed on the system in conducting the business process; may result in a performance requirement in the SyRS. |
| **9.4.13 System operational modes and states** | Operational modes and states to support system operation. |
| **9.4.14 System operational quality** | Quality level required for system operation: **performance, compatibility, reliability, security, maintainability, portability**. (Cf. ISO/IEC 25010.) |
| **9.4.15 User requirements** | Requirements for use that provide the basis for design and evaluation. Include **use-related quality (incl. usability)** with intended outcomes and quality criteria, **user-system interaction** requirements, and any **constraints** that could limit freedom of design. **The context of use shall be specified** as part of the user requirements specification, clearly identifying the conditions under which the requirements apply. Usability requirements include **measurable effectiveness, efficiency and satisfaction criteria** in specific contexts of use. |
| **9.4.16 Operational concept** | (a) operational policies and constraints; (b) description of proposed system; (c) modes of system operation; (d) user classes and other personnel; (e) support environment. Detailed in Annex A. |
| **9.4.17 Operational scenarios** | How users / operators / maintainers will interact with the system in important contexts of use. **Uniquely named and numbered; referenced in the business-processes description.** |
| **9.4.18 Other detailed concepts of proposed system** | Detailed content of the concepts for acquisition, deployment, support and retirement. |
| **9.4.19 Project constraints** | If appropriate, constraints to performing the project within cost and schedule. |

---

## 9.5 System Requirements Specification (SyRS) content

| Section | Required content |
|---|---|
| **9.5.1 SyRS overview** | Project shall produce content per project policies; organisation may be selected. |
| **9.5.2 System purpose** | Reason(s) for which the system is being developed or modified. |
| **9.5.3 System scope** | (a) identify the system to be produced by name; (b) refer to and state the results of the earlier needs analysis — brief clear expression of user's problem(s); explain what the system will and will not do to satisfy those needs; (c) describe the application of the system, with top-level benefits, objectives and goals as precisely as possible. |
| **9.5.4.1 System context** | Major elements of the system, including human elements and how they interact. Includes diagrams and narrative; defines **all significant interfaces crossing the system's boundaries**. |
| **9.5.4.2 System functions** | Major system capabilities, conditions and constraints. |
| **9.5.4.3 User characteristics** | Each type of user/operator/maintainer (by function, location, type of device); number in each group; nature of use; characteristics and capabilities. (Consistent with the SRS where appropriate.) |
| **9.5.5 Functional requirements** | Functional requirements applicable to system operation. |
| **9.5.6 Usability requirements** | Usability and quality-in-use requirements with **measurable effectiveness, efficiency, satisfaction criteria and avoidance of harm** in specific contexts of use. |
| **9.5.7 Performance requirements** | Critical performance conditions and associated capabilities: (a) **dynamic actions or changes** (rates, velocities, movements, noise levels); (b) **quantitative criteria** for endurance under stipulated environmental / other conditions, including **minimum total life expectancy** and required operational session duration / planned utilisation rate; (c) performance requirements for operational phases and modes. |
| **9.5.8 System interface requirements** | Requirements for interfaces among system elements (including human element) and with external entities (including other systems). Define interdependencies / constraints (protocols, special devices, standards, fixed formats). Each interface may represent bidirectional flow. **Graphic representation can be used for clarity.** |
| **9.5.9.1 Human system integration requirements** | Reference applicable documents; specify special / unique requirements (constraints on allocation of functions to personnel, communications, personnel/equipment interactions). Define requirements for any areas / stations / equipment needing concentrated human-engineering attention (sensitivity of operation, criticality of task). (Cf. ISO 9241-220.) |
| **9.5.9.2 Maintainability requirements** | **Quantitative** maintainability in the planned maintenance / support environment: (a) **time** (mean / max downtime, reaction time, turnaround time, MTTR, mean time between maintenance actions); (b) **rate** (staff-hours per action, operational ready rate, maintenance time per operating hour, frequency of PM); (c) **complexity** (number of people, skill levels, variety of support equipment, R&R of components); (d) **maintenance action indices** (maintenance cost per operating hour, staff hours per overhaul); (e) **accessibility** to components within systems and to parts within components. |
| **9.5.9.3 Reliability requirements** | System reliability in **quantitative terms**, including the conditions under which the requirements are to be met. May include the reliability **apportionment model** to support allocation of reliability values to system functions. |
| **9.5.9.4 Other quality requirements** | How the system will implement other quality requirements such as **compatibility and portability**. |
| **9.5.10 System modes and states** | If the system can exist in various operational modes / states, define these (with diagrams). Define modes-and-states requirements. |
| **9.5.11.1 Physical requirements** | Constraints on **weight, volume, dimension**; construction characteristics of where the system will be installed; requirements for materials; nameplates and system markings; interchangeability of equipment; workmanship. |
| **9.5.11.2 Adaptability requirements** | Requirements for growth, expansion, capability and contraction (e.g., extra card slots for future network bandwidth). |
| **9.5.12 Environmental conditions** | Environmental conditions encountered by the system: **natural** (wind, rain, temperature, humidity, flora, fauna, fungus, mould, sand, salt spray, dust, radiation, chemical, airborne contaminants, immersion); **induced** (motion, shock, noise, electromagnetic, thermal); **electromagnetic signal environment**; **self-induced**; **threat**; **cooperative**. Also legal/regulatory, political, economic, social, business environments. |
| **9.5.13 System security requirements** | Security related to the facility that houses the system and operational security. Examples: security and privacy requirements (access limitations, log-on procedures, passwords); data protection and recovery methods; factors that protect the system from accidental or malicious **access, use, modification, destruction or disclosure**. In safety-critical embedded systems: distributed log / history of data sets, assignment of functions to different single systems, restriction of communications between areas. |
| **9.5.14 Information management requirements** | Management of information the system receives, generates or exports: types and amounts of information; proprietary or other protections; backup and archiving. |
| **9.5.15 Policy and regulation requirements** | Derive requirements from organisational policies, business practices and **external regulations**. Examples: multilingual support, labour policies, protection of personnel information. Health and safety criteria, including equipment characteristics, methods of operation and environmental influences (toxic systems, electromagnetic radiation). |
| **9.5.16 System life cycle sustainment requirements** | Quality activities (review and measurement collection and analysis) to help realise a quality system. Provision of facilities for operational and depot-level support, spares, sourcing and supply, provisioning, technical documentation and data, support-personnel training, initial cadre training, initial contractor-logistics support. |
| **9.5.17 Packaging, handling, shipping and transportation requirements** | Imposed on the system to make certain it can be packaged, handled, shipped, transported and stored within its intended operational context. |
| **9.5.18 Verification** | The **verification approaches and methods** planned to qualify the system or system element. **Information elements for verification are recommended to be given in a parallel manner with the information elements in 9.5.5 to 9.5.17.** |
| **9.5.19 Assumptions and dependencies** | Assumptions and dependencies applicable to the system requirements to be taken into account in the allocation and derivation of lower-level system requirements. |

---

## 9.6 Software Requirements Specification (SRS) content

| Section | Required content |
|---|---|
| **9.6.1 SRS overview** | Project shall produce content per project policies; organisation may be selected. |
| **9.6.2 Purpose** | Delineate the purpose of the software being specified. |
| **9.6.3 Scope** | (a) identify the software product(s) to be produced by name (e.g., Host DBMS, Report Generator); (b) explain what the software product(s) will do; (c) describe the application of the software, with benefits, objectives and goals; (d) be **consistent with similar statements in higher-level specifications** (e.g., a SyRS) if they exist. |
| **9.6.4 Product perspective** | System's relationship to other related products. If the product is an element of a larger system, relate higher-level requirements to the product functionality; identify the interfaces. Consider a **block diagram** of the larger system, interconnections and external interfaces. Describe operation within constraints across: (a) system interfaces; (b) user interfaces; (c) hardware interfaces; (d) software interfaces; (e) communications interfaces; (f) memory; (g) operations; (h) site adaptation; (i) interfaces with services. |
| **9.6.4.1 System interfaces** | List each system interface; identify the software functionality to accomplish the system requirement and the interface description to match the system. |
| **9.6.4.2 User interfaces** | Logical characteristics of each interface between the software and its users. A **style guide** can provide consistent rules for organisation, coding and interaction. |
| **9.6.4.3 Hardware interfaces** | Logical characteristics of each interface between the software and the hardware elements — configuration characteristics (number of ports, instruction sets, …); devices supported; how they are supported; protocols. |
| **9.6.4.4 Software interfaces** | Use of other required software products (e.g., DBMS, OS, mathematical package) and interfaces with other application systems. For each required software product: (a) name; (b) mnemonic; (c) specification number; (d) version number; (e) source. For each interface: (a) discussion of the purpose of the interfacing software relative to this software product; (b) definition of the interface in terms of **message content and format** (or a reference to the document defining it). |
| **9.6.4.5 Communications interfaces** | Interfaces to communications (e.g., local network protocols). |
| **9.6.4.6 Memory constraints** | Applicable characteristics and limits on primary and secondary memory. |
| **9.6.4.7 Operations** | Normal and special operations required by the user: (a) various modes of operations in the user organisation (e.g., user-initiated); (b) periods of interactive vs unattended operations; (c) data-processing support functions; (d) backup and recovery operations. |
| **9.6.4.8 Site adaptation requirements** | (a) requirements for any data or initialisation sequences specific to a given site, mission or operational mode (grid values, safety limits, …); (b) specification of the site- or mission-related features that should be modified to adapt the software to a particular installation. |
| **9.6.4.9 Interfaces with services** | Interactions with services (e.g., SaaS or cloud services). |
| **9.6.5 Product functions** | Summary of the **major functions** the software will perform (e.g., for accounting: customer account maintenance, customer statement, invoice preparation). Can be derived from a higher-level specification (if one exists). **Use cases, user stories and scenarios** are also used. Functions should be organised so the list is understandable to the acquirer or a first-time reader. Textual or graphical methods can show different functions and their relationships (not a design; logical relationships only). |
| **9.6.6 User characteristics** | General characteristics of the intended groups of users that may influence usability — **educational level, experience, disabilities, technical expertise**. Should not state specific requirements but rather state the reasons why specific requirements (in §9.6.9) are later specified. Consistent with the SyRS where appropriate. |
| **9.6.7 Limitations** | Items that will limit the supplier's options: (a) regulatory requirements and policies; (b) hardware limitations (signal timing); (c) interfaces to other applications; (d) parallel operation; (e) audit functions; (f) control functions; (g) higher-order language requirements; (h) signal handshake protocols (XON-XOFF, ACK-NACK); (i) quality requirements (e.g., reliability); (j) criticality of the application; (k) safety and security considerations; (l) physical/mental considerations; (m) limitations sourced from other systems, including real-time requirements through interfaces. |
| **9.6.8 Assumptions and dependencies** | Factors that affect the requirements stated in the SRS — not design constraints, but any changes to these factors can affect the requirements. *Example: an assumption that a specific OS will be available on the designated hardware.* |
| **9.6.9 Apportioning of requirements** | Apportion requirements to software elements. For requirements implemented over multiple elements or initially unallocated, state so. **Use a cross-reference table by function and software element**. Identify requirements that may be delayed until future versions (blocks / increments). |
| **9.6.10 Specified requirements** | Software system requirements to a level of detail sufficient for software design, development and verification. Requirements shall: (a) be stated in conformance with all the characteristics described in **§5.2** of the standard; (b) be **cross-referenced to earlier versions or related documents**; (c) be **uniquely identifiable**; (d) **describe every input (stimulus) into the system, every output (response) from the system, and all functions performed in response to an input or in support of an output**. |
| **9.6.11 External interfaces** | All inputs into and outputs from the software system. Complements (does not repeat) §9.6.4.1–§9.6.4.5. Each interface includes: (a) name of item; (b) description of purpose; (c) source of input or destination of output; (d) **valid range, accuracy and/or tolerance**; (e) **units of measure**; (f) **timing**; (g) relationships to other inputs/outputs; (h) **data formats**; (i) **command formats**; (j) data items or information included in the input and output. |
| **9.6.12 Functions** | Fundamental actions in accepting / processing inputs and processing / generating outputs: (a) **validity checks on the inputs**; (b) **exact sequence of operations**; (c) **responses to abnormal situations** (overflow; communication facilities; hardware faults and failures; **error handling and recovery**); (d) effect of parameters; (e) relationship of outputs to inputs (input/output sequences; formulas for input-to-output conversion). May partition into sub-functions / sub-processes — does **not** imply software design partitioning. |
| **9.6.13 Usability requirements** | Usability and quality-in-use requirements with **measurable** effectiveness, efficiency, satisfaction criteria, and avoidance of harm in specific contexts of use. |
| **9.6.14 Performance requirements** | Static and dynamic numerical requirements. **Static** may include: (a) number of terminals supported; (b) number of simultaneous users; (c) amount and type of information handled. Sometimes called *Capacity*. **Dynamic** may include numbers of transactions / tasks / amount of data within certain time periods for both normal and peak workload. **Stated in measurable terms** (e.g., *"95% of the transactions shall be processed in less than 1 s"* — not *"An operator shall not have to wait for the transaction to complete"*). |
| **9.6.15 Logical database requirements** | Logical requirements for information placed into a database: (a) types of information used by various functions; (b) frequency of use; (c) accessing capabilities; (d) data entities and their relationships; (e) **integrity constraints**; (f) security; (g) **data retention requirements**. |
| **9.6.16 Design constraints** | Constraints on system design imposed by external standards, regulatory requirements or project limitations. |
| **9.6.17 Standards compliance** | Requirements derived from existing standards or regulations: (a) report format; (b) data naming; (c) accounting procedures; (d) audit tracing. *Example: an audit trace requirement that all changes to a payroll database shall be recorded in a trace file with before and after values.* |
| **9.6.18 Software system attributes** | The "-ilities" — partial list: (a) **Reliability**; (b) **Availability** (checkpoint, recovery, restart); (c) **Security** — protect from accidental / malicious access, use, modification, destruction or disclosure: cryptographic techniques; specific log / history data sets; assignment of functions to different modules; restriction of communications between areas; **check data integrity for critical variables**; **assure data privacy**; (d) **Maintainability** — modularity, interfaces, complexity limitation; (e) **Portability** — % host-dependent code; portable language; particular compiler / language subset; particular OS. |
| **9.6.19 Verification** | The verification approaches and methods planned to qualify the software. **Information items for verification are recommended to be given in a parallel manner with the information items in 9.6.10 to 9.6.18.** |
| **9.6.20 Supporting information** | Additional supporting information to be considered: (a) sample input/output formats, descriptions of cost analysis studies, results of user surveys; (b) supporting / background information; (c) description of the problems to be solved; (d) special packaging instructions for the code and the media (security, export, initial loading). The SRS should **explicitly state** whether or not this information is to be considered part of the requirements. |

---

## Annex A — System Operational Concept (OpsCon) overview

The OpsCon document describes **what the system will do (not how) and why (rationale)**. User-oriented document describing system characteristics from the user's viewpoint. Used to communicate overall quantitative and qualitative system characteristics to acquirer, user, supplier and other organisational elements.

> The OpsCon can be a separate document or combined with the SyRS. Each version should contain a title and a revision notice that uniquely identifies the document; a table of contents, list of figures and list of tables should be included.
