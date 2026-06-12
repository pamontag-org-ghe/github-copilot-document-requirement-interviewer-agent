# Interview Question Bank (BABOK v3)

> Reusable question bank for **stakeholder interviews** during software requirements elicitation. Questions are organised in two complementary axes:
>
> - **Part A — by BABOK requirement type** (Business / Stakeholder / Solution-Functional / Solution-NonFunctional / Transition). Use this when you want to cover the four requirement levels exhaustively.
> - **Part B — by BACCM core concept** (Change / Need / Solution / Stakeholder / Value / Context). Use this when you want to check holistic coverage of the analysis.
> - **Part C — opening / closing / disambiguation questions** to use in any session.
>
> Mark each question OPEN (elicit dialogue / new information) or CLOSED (confirm / quantify). Mix intentionally (BABOK §10.25.3 .3).
>
> Source: BABOK® Guide v3, Chapters 2 (Key Concepts), 4 (Elicitation), 10 (Techniques — esp. §10.25 Interviews, §10.30 Non-Functional Requirements, §10.1 Acceptance Criteria, §10.43 Stakeholder analysis).

---

## Part A — by BABOK requirement type (§2.3)

### A.1 Business Requirements (the *why*)

Goals, objectives, outcomes of the change.

- OPEN — *What problem are we trying to solve, in your own words?*
- OPEN — *What opportunity does this change capture?*
- OPEN — *Why now? What changed in the business that triggered this?*
- OPEN — *What does success look like 12 months after we deliver this?*
- OPEN — *What business outcomes do you want to be different — and by how much?*
- CLOSED — *Is this a "must do" (regulatory / strategic) or a "should do"?*
- CLOSED — *Is this an enterprise-wide, business-area, or initiative-specific goal?*
- OPEN — *What happens if we do nothing?*
- OPEN — *How will the business measure that this initiative was worth the investment?*
- CLOSED — *Is there a hard deadline tied to a business event (regulatory, contractual, market window)?*
- OPEN — *Which strategic objectives or OKRs does this map to?*
- CLOSED — *Who is the executive sponsor and who is the budget owner?*

### A.2 Stakeholder Requirements (the *who needs what*)

The needs of stakeholders that must be met for the business requirements to be achieved.

- OPEN — *Who else, besides you, will be impacted by this change — positively or negatively?*
- OPEN — *Whose work changes the most when we deliver this?*
- OPEN — *Who currently does the work this will replace or augment?*
- OPEN — *Walk me through a typical day / week / month for this user.*
- OPEN — *What do they need to be able to do that they can't do today?*
- OPEN — *What do they need to stop doing that they do today?*
- CLOSED — *How many people are in this user class? Where are they located?*
- OPEN — *What is their level of technical proficiency? Do they need training?*
- OPEN — *What is their attitude toward this change — champion, neutral, sceptical, opposed?*
- OPEN — *Who has final say on decisions about their workflow?*
- OPEN — *Who else needs to be in the room when we talk about their needs?*

### A.3 Solution Requirements — Functional (the *what the system does*)

Capabilities the solution must have in terms of behaviour and information.

- OPEN — *Describe end-to-end the activity the system should support.*
- OPEN — *What triggers this activity? What event or input starts it?*
- OPEN — *What inputs does the system receive? From whom or what?*
- OPEN — *What outputs does the system produce? For whom?*
- OPEN — *What are the alternative flows? When does the "happy path" not apply?*
- OPEN — *What are the exception scenarios? What errors must be handled, and how?*
- OPEN — *What are the business rules that govern this activity?*
- CLOSED — *Are there decisions the system must make automatically? Based on what data?*
- OPEN — *What state changes happen in the data? Who can transition them?*
- OPEN — *Who is allowed to do this? Who is not?*
- OPEN — *What audit trail / log do you need to keep, and for how long?*
- CLOSED — *Is there an existing process / system that does this today? Can I observe it?*
- OPEN — *What's the boundary — what is **out of scope** for this activity?*

### A.4 Solution Requirements — Non-Functional (the *how well*) — BABOK §10.30 categories

Choose categories that apply; quantify each.

#### Availability

- CLOSED — *What % availability do you need, over what window (24/7? business hours?)?*
- CLOSED — *What is the maximum tolerable unplanned downtime? Per incident? Per month?*
- CLOSED — *Is scheduled maintenance allowed, and during what windows?*
- OPEN — *What is the business impact per hour of unavailability?*

#### Performance Efficiency

- CLOSED — *What response time is acceptable for action X — average / p95 / p99?*
- CLOSED — *What throughput must the system sustain (RPS, TPS, batch records / hour)?*
- OPEN — *Is performance allowed to degrade under peak load? How gracefully?*
- CLOSED — *What is the expected peak / off-peak ratio?*

#### Scalability

- CLOSED — *What is the upper bound on users, transactions, data volume?*
- OPEN — *How fast must we be able to scale up / down?*
- CLOSED — *Should scaling be automatic, on-demand, or planned?*

#### Reliability

- CLOSED — *What is the target MTBF / failure rate per unit work?*
- CLOSED — *What is the RTO / RPO if a major failure occurs?*
- OPEN — *Which operations are critical (must never lose data) vs. tolerable to retry?*

#### Maintainability

- OPEN — *Who will maintain this once it's live? With what skill set?*
- CLOSED — *How often do you expect changes to this functionality (weekly, quarterly, yearly)?*
- OPEN — *Are there parts that change much more often than others — should they be isolated?*

#### Portability

- CLOSED — *Where must this run (cloud regions, on-prem, mobile platforms, OS versions)?*
- OPEN — *Could this be re-deployed to another cloud / vendor in the future?*

#### Compatibility / Interoperability

- OPEN — *What other systems must this coexist or interoperate with?*
- CLOSED — *Which versions of those systems must be supported?*
- OPEN — *What data formats and protocols are used at each interface?*

#### Usability

- OPEN — *Who is the primary user? What is their proficiency level?*
- CLOSED — *Is accessibility compliance required (WCAG 2.2 AA, EN 301 549)?*
- OPEN — *How will we measure "easy to use" — success rate? time on task? SUS?*

#### Security

- OPEN — *What data is sensitive? Personal? Financial? Health? Regulated?*
- OPEN — *Which Confidentiality / Integrity / Availability properties matter per data class?*
- OPEN — *Who are the threat actors you're concerned about?*
- OPEN — *What's the authentication / authorisation model — RBAC / ABAC / SSO / MFA?*
- CLOSED — *What audit and logging requirements do you have, with what retention?*
- OPEN — *What encryption (at rest, in transit) is required? Any HSM / KMS constraints?*

#### Certification / Compliance

- CLOSED — *Which standards / regulations / clauses must we comply with? (GDPR, HIPAA, PCI-DSS, ISO 27001, sector-specific)*
- OPEN — *What certification audits are planned, and when?*
- CLOSED — *Are there contractual SLAs that constrain non-functional behaviour?*

#### Localization

- CLOSED — *Which languages, currencies, date / number / address formats?*
- OPEN — *Which jurisdictions impose specific legal requirements?*
- OPEN — *Are there cultural conventions that must be respected?*

#### Service Level Agreements

- OPEN — *Do existing SLAs apply to this solution? What are the targets and penalties?*

#### Extensibility

- OPEN — *What capabilities do you anticipate adding in the next 12–24 months?*
- OPEN — *Which extension points should we design for now?*

### A.5 Transition Requirements (the *how do we get there*)

Capabilities needed to move from current state to future state — **temporary**.

- OPEN — *What data exists today that we need to migrate? In what format? How clean is it?*
- CLOSED — *What is the cutover strategy — big-bang, parallel run, phased rollout, blue-green?*
- OPEN — *How long must the old system stay in operation in parallel? Why?*
- OPEN — *What training do the users need before they can use the new system?*
- OPEN — *What manuals, knowledge base articles, or in-app help must be ready at launch?*
- OPEN — *What temporary integrations are needed during the transition?*
- OPEN — *What is the rollback plan if the cutover fails?*
- CLOSED — *Who will perform the data migration? When? With what window of downtime?*
- OPEN — *What change-management activities are planned (comms, sponsorship, support hotline)?*
- OPEN — *Which transition activities have hard external dependencies (regulators, vendors)?*

---

## Part B — by BACCM core concept (§2.1)

Use this set when you want to do a holistic sweep and detect what the conversation has not yet covered. If a concept has zero or shallow answers, the analysis is incomplete.

### B.1 Change

- *What exactly is changing — process, data, technology, people, organisation?*
- *Is this a brand-new capability, an enhancement, a replacement, a retirement?*
- *Who decided this change should happen? Why now?*
- *How will we know the change has been successful?*
- *What other changes are happening in parallel that could affect this one?*

### B.2 Need

- *What is the underlying problem or opportunity?*
- *Why does this problem matter — what is the cost of not solving it?*
- *Whose need is this — and is it shared by other groups?*
- *Is this a real need, or a solution someone has already chosen?* (apply 5-Whys)
- *Has this need existed for long? Is it growing or stable?*

### B.3 Solution

- *What outcomes must the solution deliver?*
- *What characteristics or qualities must the solution have?*
- *What is **not** the solution (anti-scope)?*
- *Are there constraints on the solution (mandated tech, prohibited tech, budget cap)?*
- *Have alternative solutions been considered? Why discarded?*

### B.4 Stakeholder

- *Who is affected by, influences, or has interest in this change?*
- *Who has decision authority on this?*
- *Who can block or delay this?*
- *Who is the most likely champion? The most likely detractor?*
- *Whose needs have we **not** considered yet?*

### B.5 Value

- *What value will this deliver, to whom, and how is it measured?*
- *Is the value tangible (revenue / cost) or intangible (reputation / morale)?*
- *Can value be negative for any stakeholder group (losses, risks, costs)? How will we mitigate?*
- *How will we know we delivered the value — what indicator do we track post-release?*

### B.6 Context

- *What is the organisational, technical, market, regulatory context of this change?*
- *What in the context is stable, what is volatile?*
- *What assumptions about the context might be wrong?*
- *What context-driven constraints apply (geography, jurisdiction, calendar, season)?*
- *Are there competitors, vendors, partners whose actions could affect this?*

---

## Part C — Session questions (any technique)

### C.1 Opening

- *Thank you for joining. Before we start, let me confirm the goal of this session: …*
- *Is there anything you'd like to add to or change about the agenda?*
- *How would you like the outcome of this session to be used — informally, or as a baseline I'll share with the steering committee?*
- *Are you comfortable with me taking notes / recording for accuracy?*

### C.2 Mid-session — probing and confirming

- *Tell me more about that — what does that look like in practice?*
- *Can you walk me through a recent example, step by step?*
- *Who else does this affect?*
- *What would happen if we didn't do this?*
- *On a scale of 1 (nice-to-have) to 5 (must-have), how would you rate this?*
- *Is that always true, or are there exceptions?*
- *Let me re-state what I heard — please correct me: "…"*
- *I notice you hesitated when I asked X — what's behind that?*

### C.3 Closing

- *What have we missed today that you wish I'd asked?*
- *Who else should I be talking to about this?*
- *Are there documents, recordings, or examples you can share for follow-up?*
- *What's the best way to come back to you with follow-up questions?*
- *Here's a quick summary of what we agreed — does that match your understanding?*
- *I'll share the notes within 48 hours; please confirm or correct.*
- *What's the next step you'd like to see from me?*

### C.4 Disambiguation (apply whenever a vague word appears)

| When the stakeholder says… | Ask… |
|---|---|
| "fast", "quick", "responsive" | *Compared to what? Measured how? At what load and at which percentile?* |
| "user-friendly", "easy", "intuitive" | *Easy for whom doing what task in how much time? How will we measure (success rate, time on task, SUS)?* |
| "secure" | *Against which threat actor? Protecting which asset? In terms of Confidentiality, Integrity or Availability? What control do you have in mind?* |
| "scalable" | *Scaling along which axis (RPS, MAU, data GB), to what upper bound? What should happen beyond it?* |
| "reliable", "stable" | *Availability % over what window? RTO/RPO? MTBF target?* |
| "always available" | *Including planned maintenance? Allowed downtime per month?* |
| "robust" | *To which inputs? Under which failure modes? With what recovery?* |
| "compliant" | *With which standard / regulation / clause exactly? How is conformance demonstrated?* |
| "real-time" | *Within how many milliseconds? At which percentile?* |
| "minimal", "trivial", "negligible" | *Concretely how much — measured how?* |
| "the user wants X" (where X is a solution) | *Why X? What need would X satisfy? (5-Whys)* |
| "everyone agrees", "the team is aligned" | *Who has formally accepted this — and are there stakeholders whose objections we haven't heard?* |
| "we'll figure it out later" | *What is the latest we can defer this decision? Who must be in the room when we do?* |
| "it's obvious" | *Obvious to whom? Will a new joiner understand it from the spec alone?* |
| "always", "never" | *Are there exceptions? Under what conditions?* |
| "the existing system does it" | *Show me how. Is the existing behaviour the requirement, or do we want to keep / change / drop it?* |

---

## Part D — Conflict, ambiguity, gap probes

When the BA suspects the elicitation is incomplete or contradictory:

- *I have two different statements about this from different sources — let's reconcile.*
- *Who can break the tie if the two groups disagree?*
- *If I had to write this as a Given/When/Then scenario right now, what would the Then be?*
- *Imagine we ship this in 6 months exactly as we have it specified. What surprises me most about it?*
- *What is the riskiest assumption we're making here?*
- *What would make you reject this at User Acceptance Testing?*

---

## Suggested coverage matrix (use after the session)

Tick each cell to confirm the session covered it. Empty rows / columns highlight gaps for the next round.

| | Change | Need | Solution | Stakeholder | Value | Context |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Business requirements        | | | | | | |
| Stakeholder requirements     | | | | | | |
| Solution req. – Functional   | | | | | | |
| Solution req. – Non-Functional| | | | | | |
| Transition requirements      | | | | | | |
