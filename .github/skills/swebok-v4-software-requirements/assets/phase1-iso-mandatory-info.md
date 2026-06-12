# Phase 1 — Mandatory information per SRS section (ISO/IEC/IEEE 29148 + Wiegers template)

> Companion reference used by the `swebok-v4-software-requirements` skill during interview-time elicitation.
> Each row distils — **from the canonical [srs-template.md](../../software-requirements-spec/assets/srs-template.md)** and aligned with **ISO/IEC/IEEE 29148:2018** — the minimum information that must be elicited from the stakeholder to fill that section of the SRS. This is the "what must I get out of the user" view; the `software-requirements-spec` skill owns the "where do I write it" view.
> Cross-reference column points to the SWEBOK chapter / checklist that drives the deeper questions. Checklist IDs (e.g., `SR-001`, `ST-007`, `SQ-006`, `SS-004`) refer to rows in the prioritised checklists under [../references/](../references/).

## Cover & front matter

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| Title block | Project name; document version + status; author full name; organization; ISO date created | — |
| Revision history | At least the initial row (author, date, "Initial draft", version) | — |
| Table of contents | Auto-derived from headings; must include anchors down to level 3 | — |

## 1. Introduction

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 1.1 Document Purpose | Product identity; release/revision; intended readers (dev, PM, QA, ops, marketing, …) | — |
| 1.2 Document Conventions | Typographic conventions; requirement-ID format (e.g., `FR-3.1-01`, `NFR-PERF-02`, `SEC-014`) | SR-027 |
| 1.3 Project Scope | One-paragraph product summary; link to business goals/strategy; high-level feature/function list for *this* release; relation to long-term vision if incremental | SR-026, SR-033 |
| 1.4 References | Hyperlinked list of related docs (style guides, contracts, standards, vision doc, related SRS, regulatory texts) — title/author/version/date/URL each | SR-012, SS-004, SQ-014 |

## 2. Overall Description

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 2.1 Product Perspective | Origin (new / replacement / next version / part of larger system); context diagram or ecosystem map; identification of major interfaces | SR-021, SR-022 |
| 2.2 User Classes & Characteristics | Each user class with: pertinent characteristics, technical proficiency, frequency of use, importance, *favored* flag | SR-006, SR-029 |
| 2.3 Operating Environment | Hardware platform; OS + versions; geographical locations of users/servers/databases; hosting orgs; co-existing software with versions; required infrastructure work | SR-023, SQ-009, SQ-011 |
| 2.4 Design & Implementation Constraints | Corporate / regulatory policies; hardware limits (timing, memory); mandated technologies / databases / tools / languages; interfaces to existing apps; prohibitions | SR-023, SS-004 |
| 2.5 Assumptions & Dependencies | Assumed factors (vs known facts); third-party / commercial components planned; reuse expectations; external dependencies outside project control | SR-022 |

## 3. System Features (per feature `3.x`)

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 3.x (heading) | Feature name in a few words | — |
| 3.x.1 Description | One-paragraph description **+ priority** (High / Medium / Low) | SR-024 |
| 3.x.2 Stimulus/Response Sequences | User action → system response pairs covering the feature's main flows; **alternate flows must be elicited explicitly** | SR-002, ST-002, ST-006 |
| 3.x.3 Functional Requirements | Atomic, testable requirements with stable IDs; **explicit error/exception handling**; acceptance criteria (ATDD/BDD) attached; `TBD` for missing info | SR-001..SR-005, SR-007, SR-010, SR-017, ST-001, ST-002, ST-006 |

## 4. Data Requirements

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 4.1 Logical Data Model | Entities, attributes, relationships, cardinalities (ER-style; Mermaid `erDiagram` preferred) | SQ-020 |
| 4.2 Data Dictionary | Per data element: name, type, length, format, allowed values, default, units; or link to external dictionary | SQ-020 |
| 4.3 Reports | Each generated report: content, sort order, totaling levels, predefined layouts/constraints (defer detailed layout to design) | — |
| 4.4 Acquisition, Integrity, Retention, Disposal | Acquisition flow; integrity techniques (backups, checkpointing, mirroring, accuracy verification); retention/disposal per data class **including temporary/metadata/residual/cached/local-copies/archives/interim-backups** | SS-021, SS-001, SS-020 |

## 5. External Interface Requirements

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 5.1 User Interfaces | Logical characteristics per interface; sample screens; GUI standards / style guide; layout constraints; standard buttons; keyboard shortcuts; error-message standards | SQ-008 |
| 5.2 Software Interfaces | Each named external software (name + version); message formats and contents; data mappings and translations; required services; nonfunctional constraints (latency, security) | ST-011, SQ-009 |
| 5.3 Hardware Interfaces | Device types; data/control interactions; communication protocols; I/O formats; valid value ranges; timing | ST-013 |
| 5.4 Communications Interfaces | Email / web / network protocols; message formatting; **encryption**; data transfer rates; handshaking; synchronisation; constraints (e.g., attachments allowed?) | SS-007, SS-013 |

## 6. Quality Attributes (ISO/IEC 25010 lens)

| Section | Minimum info to elicit | Cross-reference |
|---|---|---|
| 6.1 Usability | Ease of use / learning; memorability; error avoidance/handling/recovery; efficiency; **accessibility (WCAG/EN 301 549)**; ergonomics; trade-offs (ease of use vs ease of learning); UI design standards | SQ-008, ST-019 |
| 6.2 Performance | Per critical operation: response time / throughput / capacity with units, percentile, load conditions, **fail point + perfection point + target** | SR-010, SR-011, SQ-006, ST-007 |
| 6.3 Security | CIA per data class; authn / authz model; auditing; cryptography; vulnerability management; misuse cases; reference to business rules & regulations | SS-001..SS-016, SQ-004 |
| 6.4 Safety | Hazards (loss, damage, harm); safeguards and prevention actions; safety certifications / regulations | SQ-016, SQ-001 |
| 6.5 Others as relevant | Add one subsection per: availability, reliability, maintainability, portability, scalability, interoperability, modifiability, robustness, verifiability — each **specific, quantitative, verifiable**; **declare relative priorities** | SQ-002, SQ-007, SQ-009, SQ-010, SQ-011 |

## 7. Internationalisation & Localisation

| Minimum info to elicit | Cross-reference |
|---|---|
| Currencies; date/number/address/phone formats; languages incl. regional variants; symbols; character sets; given/family name order; time zones; international regulations; cultural/political issues; paper sizes; weights/measures; electrical voltages/plugs | — |

## 8. Other Requirements

| Minimum info to elicit | Cross-reference |
|---|---|
| Legal / regulatory / financial compliance; standards; install / config / startup / shutdown; **logging, monitoring, audit trail** (esp. security events) | SS-004, SS-012, SQ-014 |

## 9. Glossary

| Minimum info to elicit | Cross-reference |
|---|---|
| Every domain term and acronym used in the SRS, spelled out with a definition; align with enterprise glossary if any | SR-030 |

## 10. Analysis Models

| Minimum info to elicit | Cross-reference |
|---|---|
| Data flow diagrams; feature trees; state-transition diagrams; ER diagrams; sequence/activity diagrams — Mermaid preferred or external links | ST-025 |

---

## Cross-cutting elicitation rules (do not skip)

These do not map to a single SRS section but must be enforced across the whole document:

| Rule | Source |
|---|---|
| Each requirement has a stable ID, rationale, source, priority, acceptance criteria, dependencies, conflicts, stability/volatility, change history | SR-019, SR-024, SR-025, SR-027 |
| Backward & forward traceability is maintained (req → source, req → design / test / user manual) | SR-015, SQ-013 |
| Requirements are under configuration management with a documented change-control process | SR-008, SR-019 |
| Functional vs nonfunctional separation respected; Perfect Technology Filter applied | SR-009 |
| Conflict resolution is documented; no unilateral engineer decisions | SR-014 |
| Scope is matched to cost / schedule / staffing (functional size or story points) | SR-016 |
| Reviews from multiple perspectives (business, RA, downstream engineers) are scheduled | SR-013 |
| Stakeholder vocabulary used; acronyms in glossary; no jargon mismatch | SR-030 |
| Multiple elicitation techniques applied (interviews + workshops + observation + documents + …) | SR-020 |
