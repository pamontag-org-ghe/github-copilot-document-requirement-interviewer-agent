# Chapter 10 — Elicitation Techniques (BABOK v3, selected)

> Source: **BABOK® Guide v3**, Chapter 10 *Techniques* (pp. 217–366).
> This file contains the techniques most relevant to **eliciting requirements through stakeholder interviews and related activities**. For each, the BABOK §10.x.1 *Purpose*, §10.x.2 *Description*, §10.x.3 *Elements*, and §10.x.4 *Usage Considerations (strengths / limitations)* are preserved or summarised. Less interview-relevant techniques (Balanced Scorecard, Business Model Canvas, Financial Analysis, Data Mining, Data Modelling, …) are not included.

## Index

| § | Technique | Used for |
|---|---|---|
| §10.1  | Acceptance and Evaluation Criteria | Defining the conditions a solution must meet to be accepted; ranking alternatives |
| §10.5  | Brainstorming | Generating many ideas from a group in a short time |
| §10.10 | Collaborative Games | Building joint understanding through structured play |
| §10.18 | Document Analysis | Eliciting context and requirements from existing materials |
| §10.21 | Focus Groups | Capturing attitudes / impressions / preferences from a small group |
| §10.23 | Glossary | Establishing common business vocabulary |
| §10.25 | **Interviews** | One-on-one or small-group questioning to elicit information |
| §10.26 | Item Tracking | Capturing & resolving issues, concerns, defects, decisions |
| §10.30 | Non-Functional Requirements Analysis | Categorising and quantifying NFRs (-ilities) |
| §10.31 | Observation | Eliciting by watching activities in their context |
| §10.33 | Prioritization | Establishing relative importance |
| §10.36 | Prototyping | Eliciting / validating needs through an iterative model of the solution |
| §10.37 | Reviews | Evaluating the content of a work product |
| §10.43 | Stakeholder List, Map, or Personas | Identifying and analysing stakeholders |
| §10.45 | Survey or Questionnaire | Structured group elicitation in a short time |
| §10.47 | Use Cases and Scenarios | Describing actor-system interactions to achieve a goal |
| §10.48 | User Stories | Concise stakeholder-value statements |
| §10.50 | Workshops | Facilitated collaborative event with a defined goal |

---

## 10.1 Acceptance and Evaluation Criteria

**Purpose** — define the requirements / outcomes / conditions that must be met for a solution to be considered acceptable (**acceptance criteria**), or the measures used to assess and rank alternative solutions (**evaluation criteria**).

**Description** — measurable and testable criteria let solutions be assessed objectively and consistently. Acceptance criteria are usually pass/fail (one solution being evaluated). Evaluation criteria express continuous or discrete scales to rank multiple solutions on attributes like cost, performance, usability, fit to needs.

**Elements**

- *Value Attributes* — characteristics that determine or substantially influence the value of a solution: ability to provide specific information, ability to perform specific operations, performance & responsiveness, applicability to specific situations / contexts, availability of features, usability, security, scalability, reliability. **Base acceptance and evaluation criteria on value attributes** so they remain valid and relevant.
- *Assessment*
  - **Testability** — acceptance criteria are expressed in a testable form. May require breaking down requirements into atomic form so test cases can verify the solution against the criteria. Typically achieved through **UAT**.
  - **Measures** — evaluation criteria are parameters measurable on a scale (benchmarking, expert judgment); may require designing tools and instructions for the assessment.

**Strengths**

- Agile methodologies often require all requirements to be expressed as testable acceptance criteria.
- Necessary when requirements express contractual obligations.
- Provide objective basis for assessing whether requirements are met.

**Limitations**

- Acceptance criteria expressing contractual obligations are hard to change for legal / political reasons.
- Achieving agreement on evaluation criteria across diverse stakeholders can be challenging.

---

## 10.5 Brainstorming

**Purpose** — foster creative thinking; produce many new ideas in a short time; derive themes for further analysis.

**Description** — focus on a topic or problem and produce many possible solutions. Best in a group (6–8 participants from a range of backgrounds). Encourages new perspectives and free association.

**Elements**

- *Preparation* — define the area of interest concisely; set a time limit (larger groups need more); identify facilitator and participants; set expectations and get buy-in; **establish criteria for evaluating and rating ideas in advance**.
- *Session* — share ideas without discussion / criticism / evaluation; visibly record all ideas; encourage exaggerated ideas and building on others'; don't cap the number of ideas.
- *Wrap-up* — discuss and evaluate ideas using the predetermined criteria; create a condensed list; combine and de-duplicate; rate; distribute final list.

**Strengths** — many ideas in short time; non-judgmental environment enables creative thinking; useful during workshops to reduce tension.

**Limitations** — depends on individual creativity and willingness; organisational / interpersonal politics can limit participation; participants must commit to not debating ideas during generation.

---

## 10.10 Collaborative Games

**Purpose** — encourage participants to collaborate in building a joint understanding of a problem or solution.

**Description** — structured techniques inspired by game play with rules to keep participants focused on a specific objective. Used to share knowledge, identify hidden assumptions, and explore in ways that don't occur during normal interactions. Often benefit from a **neutral facilitator** who enforces rules, keeps the game moving, ensures everyone plays a role. Strong visual or tactile elements (sticky notes, whiteboards, drawings) help overcome inhibitions and stimulate creative thinking.

**Elements**

- *Game Purpose* — develop better understanding of a problem or stimulate creative solutions.
- *Process* — at least three steps:
  1. **Opening** — participants get involved, learn the rules, start generating ideas.
  2. **Exploration** — engage with one another, look for connections, test, experiment.
  3. **Closing** — ideas are assessed; participants identify the most useful.
- *Outcome* — facilitator and participants determine decisions or actions to take.

Examples: **Product Box** (build a retail box for the product → drives interest), **Affinity Map** (group features by similarity → reveal themes), **Fishbowl** (one group speaks, the other documents observations → expose hidden assumptions).

**Strengths** — reveal hidden assumptions or differences of opinion; encourage creative thinking; activate normally reserved participants; can expose unmet business needs.

**Limitations** — may feel silly to reserved participants or in some cultural norms; time-consuming and may be perceived as unproductive if objectives unclear; group participation can give false confidence in conclusions.

---

## 10.18 Document Analysis

**Purpose** — elicit business analysis information (context and requirements) by examining available materials describing the business environment or existing organisational assets.

**Description** — used for background research, to validate findings from interviews / observations, or to study how existing solutions are implemented. **Data Mining** is an approach to document analysis. Materials commonly reviewed: marketing studies, industry guidelines, standards, company memos, org charts, business rules, technical documentation, training docs, problem reports, previous requirements documents, procedure manuals.

Particularly valuable when the SMEs for the existing solution are no longer present.

**Elements**

- *Preparation* — assess relevance, currency, genuineness, credibility; readability; define classes of data and clusters.
- *Document Review and Analysis* — detailed review of each document's content; document analysis chart with topic / type / source / verbatim details / paraphrased critique / follow-up. Identify conflicts, duplicates, gaps.
- *Record Findings* — appropriate level of detail for the intended audience; transform into visual aids (graphs, models, flows, decision tables) when useful.

**Strengths** — pre-existing material as basis; analyst doesn't have to create content; useful as a reference point to detect what has changed; can validate other elicitation results.

**Limitations** — documents may be out of date, unreviewed, unapproved, incorrect; authors may not be available; primarily evaluates current state; large document sets can lead to information overload.

---

## 10.21 Focus Groups

**Purpose** — elicit ideas and opinions about a specific product, service, or opportunity in an interactive group environment.

**Description** — composed of **pre-qualified participants** (typically 6–12). A trained moderator manages preparation, selection, and facilitation. Observers may be present but do not participate. Focus group is **not a group interview** — it is a focused discussion. Output is analysed and reported as themes and perspectives (qualitative research).

**Elements**

- *Focus Group Objective* — clear, specific.
- *Focus Group Plan* — purpose; location (in-person / online); logistics; participants and demographics; budget; timelines; outcomes (how results analyzed and communicated).
- *Participants* — willing to share insights and listen; demographics driven by objective; invite extras to offset no-shows.
- *Discussion Guide* — prepared script with questions and topics; structure (general feedback → specifics); includes welcome and intro of objectives.
- *Moderator and Recorder* — moderator keeps the session on track, engages all participants, is unbiased. Recorder takes notes for accuracy. The BA may be moderator or recorder.
- *Conduct the Focus Group* — moderator guides discussion (typically 1–2 hours), follows the script, ensures objectives met, but the discussion should feel free-flowing.
- *After* — transcribe ASAP; analyse agreements and disagreements; identify trends; report summary.

**Strengths** — elicit data from a group in a single session (cheaper than equivalent individual interviews); effective for attitudes, experiences, desires; active discussion stimulates reflection; online focus groups work for distributed participants.

**Limitations** — trust / privacy concerns; what people *say* may differ from how they *behave*; homogeneous groups may miss requirements; needs a skilled moderator; scheduling difficulties; online format limits interaction; one vocal participant can sway results.

---

## 10.23 Glossary

**Purpose** — define key terms relevant to a business domain so all stakeholders share a common understanding.

**Description** — a term goes in the glossary when it is unique to a domain, has multiple definitions, has a non-common meaning, or is at risk of misunderstanding. Created early in the project; assigned an owner; clear, concise, brief definitions; acronyms spelled out; accessible to stakeholders; edit access limited.

**Strengths** — promotes common understanding and consistent communication; enterprise glossary provides a single reference; simplifies maintenance of requirements, rules, and change strategy.

**Limitations** — without an owner it becomes outdated; getting different stakeholders to agree on one definition can be challenging.

---

## 10.25 Interviews

**Purpose** — a systematic approach to elicit business analysis information by talking to interviewees, asking relevant questions, and documenting responses. Also used to **build trust and rapport** between BA and stakeholders.

**Description** — common technique. Direct communication with individuals or small groups. The interviewer directs questions to obtain information.

Two basic types:

- **Structured** — predefined set of questions.
- **Unstructured** — no predetermined format or order; questions vary based on interviewee responses.

In practice the BA combines both — adding, dropping, and varying the order of questions as needed.

Success depends on: domain understanding, interviewer experience, skill in documenting discussions, readiness of interviewee and interviewer, clarity in the interviewee's mind about the interview goal, rapport between interviewer and interviewee.

**Elements**

### .1 Interview Goal

Consider both the overall purpose of a *set* of interviews and the *individual* goal for each interview based on what the interviewee can provide. **Communicate the goal clearly to each interviewee.**

### .2 Potential Interviewees

Identified with the help of the PM, sponsor, and other stakeholders, based on interview goals.

### .3 Interview Questions

Designed for the goal — collecting data, researching the stakeholder's view, developing a proposed solution, building rapport / support.

- **Open-ended questions** elicit dialogue or a series of steps; cannot be answered yes/no. Good for surfacing information the interviewer is unaware of.
- **Closed questions** elicit a single response (yes / no / specific number). Used to clarify or confirm.

Order questions by priority and significance — examples: **general to specific, start to finish, detailed to summary**. Or by interviewee knowledge level / subject.

Customise questions when gathering information unique to the interviewee's perspective. Standardise questions when results will be tallied. Compile in an **interview guide** with timing and follow-up; allow omission of some questions on time pressure.

### .4 Interview Logistics

- Location — adapted to the schedule, availability, and communication mode (in-person, phone, online).
- Whether to record (may require a scribe).
- Whether to send questions in advance — only when the interviewee needs to gather information.
- Confidentiality of results.

### .5 Interview Flow

**Opening**

- describe the purpose, including why the interviewee's time is needed;
- confirm the interviewee's role and address initial concerns;
- explain how the information will be recorded and shared.

**During**

- maintain focus on established goals and predefined questions; adapt based on responses and **non-verbal cues**;
- consider both the interviewee's willingness to participate and to provide the required information;
- consider that several meetings might be required;
- manage concerns immediately or document them for follow-up;
- practice **active listening** to confirm what was said;
- take written notes or record (as appropriate).

**Closing**

- ask for areas overlooked;
- provide contact info for follow-up;
- summarise the session;
- outline the process for how the interview results will be used;
- thank the interviewee.

### .6 Interview Follow-Up

Organise the information and confirm results with the interviewee **as soon as possible** so they can point out missed or wrongly recorded items.

**Strengths**

- encourages participation and establishes rapport;
- simple, direct, applicable in many situations;
- allows full discussion and explanation;
- enables observation of non-verbal behaviour;
- supports follow-up and probing questions to confirm understanding;
- maintains focus through clear objectives;
- allows opinions to be expressed privately that wouldn't be expressed in public.

**Limitations**

- significant time to plan and conduct;
- requires considerable commitment from participants;
- requires training to conduct effective interviews;
- documentation is subject to the interviewer's interpretation;
- risk of unintentionally **leading the interviewee**.

---

## 10.26 Item Tracking

**Purpose** — capture and assign responsibility for issues and stakeholder concerns that pose an impact to the solution.

**Description** — organised approach to address stakeholder concerns. Item types include: **actions, assumptions, constraints, dependencies, defects, enhancements, issues**. When raised, the concern is assessed for viability; if viable, classified by type, tracked through a process to closure, assigned to one or more stakeholders. The record may be shared for transparency.

**Item Record attributes** — *Item Identifier, Summary, Category, Type, Date Identified, Identified By, Impact (time / cost / scope / quality), Priority, Resolution Date, Owner, Resolver, Agreed Strategy (accept / pursue / ignore / mitigate / avoid), Status (open / assigned / resolved / cancelled), Resolution Updates, Escalation Matrix.*

**Strengths** — ensures concerns are captured, tracked, resolved; allows stakeholders to rank importance.

**Limitations** — excessive recording can outweigh benefits; can be time-consuming.

---

## 10.30 Non-Functional Requirements Analysis

**Purpose** — examine the requirements that define **how well** the functional requirements must perform — criteria used to judge operation rather than specific behaviours.

**Description** — NFRs (a.k.a. quality attributes, quality of service requirements) are often associated with system solutions but also apply to process and people aspects. They augment functional requirements, identify constraints, or describe quality attributes. Usually expressed as **declarative statements with a constraining factor** (e.g., "errors must not exceed X per use", "transactions must be at least X% processed after S seconds").

### Common categories of NFRs

| Category | Definition |
|---|---|
| **Availability** | degree to which the solution is operable and accessible when required (often % of time available) |
| **Compatibility** | degree to which the solution operates effectively with other components in its environment |
| **Functionality** | degree to which solution functions meet user needs (suitability, accuracy, interoperability) |
| **Maintainability** | ease with which the solution can be modified to correct faults, improve, or adapt |
| **Performance Efficiency** | degree to which the solution performs with minimum resource consumption (context / period dependent — peak, mid-peak, off-peak) |
| **Portability** | ease with which the solution can be transferred between environments |
| **Reliability** | ability to perform required functions under stated conditions for a specified period (e.g., MTBF) |
| **Scalability** | degree to which the solution can grow to handle increased work |
| **Security** | aspects that protect content or components from accidental or malicious access / use / modification / destruction / disclosure |
| **Usability** | ease of learning to use the solution |
| **Certification** | constraints to meet standards or industry conventions |
| **Compliance** | regulatory, financial, legal constraints |
| **Localization** | local languages, laws, currencies, cultures, spellings |
| **Service Level Agreements** | constraints formally agreed with the provider / user |
| **Extensibility** | ability to incorporate new functionality |

### Measurement of NFRs

NFRs are often vague ("must be easy to learn", "must respond quickly"). To be useful and verifiable, **quantify them**:

- "easy to learn" → "90% of operators must be able to use the new process after no more than six hours of training";
- "respond quickly" → "the system must provide 90% of responses in no more than two seconds".

Other categories are measured by their source: certification by the standard body, compliance / localization by their providers, SLAs state their measures explicitly, enterprise architecture defines environment constraints.

### Context of NFRs

Context (regulators, geographic operations, …) imposes additional NFRs. NFRs **interact** — security may impose performance trade-offs; localisation in one jurisdiction may justify a lower performance target than in another. Context is dynamic; reassess NFRs periodically.

**Strengths** — clearly states constraints on functional requirements; provides measurable expressions; strongly influences user acceptance.

**Limitations** — clarity depends on stakeholder knowledge and expression; perceptions differ ("fast" varies by user); inherent conflicts require negotiation; over-strict requirements add cost; many NFRs are qualitative and subjective.

---

## 10.31 Observation

**Purpose** — elicit information by **viewing and understanding activities in their context**. Used to identify needs and opportunities, understand a business process, set performance standards, evaluate solution performance, support training.

**Description** — observation of activities (job shadowing) examines work firsthand as it is performed. Can be in the natural work environment or a controlled lab.

Two basic approaches:

- **Active / Noticeable** — the observer asks questions as they arise. Despite interruption, the observer can more quickly understand rationale and hidden processes (e.g., decision making). A stronger variant has the observer stimulate actors to perform specific tasks.
- **Passive / Unnoticeable** — observer does not interrupt; concerns raised after the session. Allows observation of the natural flow and measurement of time and quality. Video recording is a common variant.

**Contextual Inquiry** — inspection of the person's work environment to discover the tools and information assets involved.

**Elements**

- *Observation Objectives* — clear and specific: understand activity and its elements (tasks, tools, events, interactions), identify improvement opportunities, establish performance metrics, assess solutions, validate assumptions.
- *Prepare for Observation* — plan the approach; consider skill / experience levels, frequency of activities, existing documentation; schedule.
- *Conduct the Observation Session*
  - **Before** — explain why; reassure that personal performance is not being judged; inform they can stop at any time; recommend sharing reasoning or concerns during or soon after.
  - **During** — attentively watch typical / atypical tasks, tool use, information content; record what is seen, time, quality, anomalies, observer's questions; ask probing questions during or shortly after.
- *Confirm and Present Observation Results* — review notes; follow up with the participant for remaining questions or gaps; collate with related observations; identify similarities, differences, trends; aggregate, summarise, analyse against the session's objectives.

**Strengths** — realistic insight; informally performed tasks and workarounds become visible; productivity can be measured firsthand; recommendations supported by objective evidence.

**Limitations** — disruptive; intrusive to the person being observed; participants may alter their work practices while observed; significant time to plan and conduct; not suitable for knowledge-based activities.

---

## 10.33 Prioritization

**Purpose** — framework for facilitating stakeholder decisions and understanding the relative importance of BA information.

**Description** — prioritization uses value, risk, difficulty of implementation, or other criteria. Four common approaches:

- **Grouping** — classify into predefined categories (high / medium / low).
- **Ranking** — order from most to least important (e.g., product backlog).
- **Time boxing / Budgeting** — based on a fixed allocation of time or money.
- **Negotiation** — establish stakeholder consensus on priorities.

Choose approach based on audience needs and opinions. Revisit when the environment, stakeholders, or BA information changes.

**Strengths** — facilitates consensus, trade-offs, value realization, timeline management.

**Limitations** — stakeholders may avoid difficult choices; the solution team may bias the prioritization by overestimating complexity; metrics may not be available, leading to subjectivity.

---

## 10.36 Prototyping

**Purpose** — elicit and validate stakeholder needs through an iterative process that creates a model of requirements / designs. Also used to optimize UX, evaluate design options, and as a basis for development.

**Description** — provides an early model of the final result. Used to identify missing or improperly specified requirements and unsubstantiated assumptions by demonstrating what the product looks like and how it acts in the early stages of design.

Two common approaches:

- **Throw-away** — simple tools (paper, whiteboard, software) to uncover and clarify requirements. Not maintained as a deliverable. Inexpensive way to uncover requirements that go beyond the interface — processes, data, business rules.
- **Evolutionary / Functional** — extended into a functioning solution as requirements emerge. Usually requires specialised tools.

**Prototyping Examples** — *Proof of Principle / Proof of Concept* (validate design), *Form Study Prototype* (size, look, feel without functionality), *Usability Prototype* (test user interaction), *Visual Prototype* (visual aspects only), *Functional Prototype* (software functionality + appearance + workflow).

**Prototyping Methods** — *Storyboarding*, *Paper Prototyping*, *Workflow Modelling*, *Simulation*.

**Strengths** — visual representation of future state; early stakeholder input and feedback; throw-away / paper prototypes invite criticism because they look unfinished; narrow-deep vertical prototype for technical feasibility / PoC.

**Limitations** — for complex systems, prototyping can bog down in "how" instead of "what"; may require assumptions about underlying technology; very elaborate prototypes may set unrealistic stakeholder expectations; risk that developers feel bound to match the prototype's UI exactly even when better approaches exist.

---

## 10.37 Reviews

**Purpose** — evaluate the content of a work product.

**Description** — reviews vary along three dimensions: **Objectives, Techniques, Participants**. They focus on the work product (not on the skills or actions of the participants). May be a package, single deliverable, portion of a deliverable, or work in process.

**Elements**

- *Objectives* — remove defects, ensure conformance to specifications / standards, ensure completeness and correctness, establish consensus on approach, answer a question / resolve an issue, educate reviewers, measure quality.
- *Techniques*
  - **Inspection** — formal: overview + individual review + log defects + team consolidation + follow-up.
  - **Formal Walkthrough (Team Review)** — formal: individual review + team consolidation.
  - **Single Issue Review (Technical Review)** — formal: focused on one issue / standard.
  - **Informal Walkthrough** — BA runs through the draft work product and solicits feedback.
  - **Desk Check** — informal: reviewer not involved in creation provides verbal / written feedback.
  - **Pass Around** — informal: multiple reviewers provide feedback in sequence.
  - **Ad hoc** — informal: BA seeks informal review or assistance from a peer.
- *Participants* — Author, Reviewer, Facilitator (neutral), Scribe.

**Strengths** — early defect identification; engages all parties in a quality outcome.

**Limitations** — depends on reviewer skill and effort; formal reviews can be time-consuming.

---

## 10.43 Stakeholder List, Map, or Personas

**Purpose** — analyse stakeholders and their characteristics. Ensures the BA identifies all sources of requirements and understands stakeholders well enough to make the best choices for engagement, collaboration, and communication.

**Description** — identify stakeholders affected or sharing a common need, analyse their characteristics.

Common characteristics: level of authority within the domain of change and within the organisation, attitudes toward the change, attitudes toward the BA work and role, level of decision-making authority.

**Elements**

### .1 Stakeholder Lists

Techniques: Brainstorming, Interviews. Goal: a thorough list (central to stakeholder analysis and to elicitation / collaboration / communication planning). Categorise and structure as analysis proceeds.

### .2 Stakeholder Map

- **Stakeholder Matrix** — level of stakeholder influence × level of stakeholder interest.
  - **High Influence / High Impact** → key players; engage regularly.
  - **High Influence / Low Impact** → keep informed; reduce anxiety.
  - **Low Influence / High Impact** → supporters / goodwill ambassadors; engage for input.
  - **Low Influence / Low Impact** → general communications.
- **Onion Diagram** — concentric rings: Solution Delivery (innermost), Affected Organizational Unit, Organization / Enterprise, Affected External Stakeholders (outermost). Shows how involved each stakeholder is with the solution.

### .3 Responsibility (RACI) Matrix

For each task / activity, label each stakeholder as:

- **Responsible (R)** — performs the work;
- **Accountable (A)** — ultimately accountable for successful completion; **one** stakeholder;
- **Consulted (C)** — asked to provide an opinion or information; two-way communication;
- **Informed (I)** — kept up to date and notified of outcome; one-way communication.

### .4 Personas

Fictional archetype that exemplifies how a typical user interacts with a product. Built from research (interviews + surveys/questionnaires). Written in narrative form, focused on the goals of the group. Makes the user feel real to designers and builders.

**Strengths** — identifies the specific people who must be engaged; supports planning of collaboration / communication / facilitation; useful to track changes in impacted groups over time.

**Limitations** — analysts working with the same teams may neglect stakeholder analysis; assessing influence and interest can feel politically risky.

---

## 10.45 Survey or Questionnaire

**Purpose** — elicit BA information from a group of people in a structured way and a short period — about customers, products, work practices, attitudes.

**Description** — set of questions whose responses are collected and analysed. Submitted in writing, in person, by phone, or via a survey tool.

Two question types:

- **Close-ended** — predefined responses (yes/no, multiple-choice, rank-order, level of agreement). Easier to analyse and quantify.
- **Open-ended** — free-form. Useful when the issues are known but the range of responses is not. More detail and wider range, but harder to analyse.

Questions must be **neutral** and not structured / sequenced to condition the respondent.

**Elements**

### .1 Prepare

- Define the objective.
- Define the target survey group.
- Choose the appropriate type (mix of close- and open-ended).
- Select the sample group (statistical sampling may be required for large populations).
- Select distribution and collection methods.
- Set target response level and timeline.
- Decide whether to support with individual interviews (pre- or post-).
- Write the survey questions (aligned to objectives).
- Test the survey for usability.

### .2 Distribute

Communicate the objectives, how results will be used, and any confidentiality / anonymity arrangements. Choose distribution method based on urgency, security, geographic distribution.

### .3 Document the Results

Collate, summarise, evaluate, identify emerging themes, formulate categories, break down into measurable increments.

**Strengths** — quick and inexpensive; reaches larger audiences than interviews; little time required from respondents; effective when stakeholders are geographically dispersed; closed-ended produces quantitative data; open-ended yields insights.

**Limitations** — needs statistical-sampling skills; response rates may be too low; open-ended questions require more analysis; ambiguous questions may be unanswered or wrong; may require follow-up questions / iterations.

---

## 10.47 Use Cases and Scenarios

**Purpose** — describe how a person or system interacts with the solution to achieve a goal.

**Description** — use cases describe interactions between primary actor, solution, and any secondary actors. Usually triggered by the primary actor. A use case describes possible outcomes — primary / alternative / exception flows. Written from the **actor's point of view**; avoids describing internal workings.

Use case **diagrams** show actors, use cases, and their relationships (associations, *<<include>>*, *<<extend>>*). Some methods distinguish **business use cases** and **system use cases**.

A **scenario** describes just one way an actor accomplishes a particular goal — one of the flows of a use case.

**Use Case Description elements**

- *Name* — unique; verb + noun.
- *Goal* — successful outcome from the primary actor's perspective.
- *Actors* — primary (starts the use case) and secondary; some methods recommend against using systems / events as actors.
- *Preconditions* — facts that must be true before the use case can begin; not tested, act as constraints.
- *Trigger* — event that initiates the flow (most commonly an action by the primary actor; may be temporal).
- *Flow of Events* — basic / primary / main success flow; alternative flows; exception flows.
- *Post-conditions / Guarantees* — facts true when the use case completes; success guarantee (post-conditions for success) and minimal guarantee (always true, even when goal not achieved — e.g., security or data integrity).

**Strengths** — clarify scope; understandable narrative flow; ensure business value is articulated; articulate functional behaviour.

**Limitations** — flexibility may embed information better captured elsewhere (UI interactions, NFRs, business rules); decisions and business rules should be linked, not embedded; may capture unnecessary detail; do not relate to solution design — significant mapping effort in development.

---

## 10.48 User Stories

**Purpose** — small, concise statement of functionality or quality needed to deliver value to a specific stakeholder.

**Description** — captures the needs of a specific stakeholder; enables short, simple documentation of features. A sentence or two — who has the need, the goal they want to accomplish, additional information critical to understanding the scope. **Invites further conversation** with stakeholders.

User stories are used to: capture needs and prioritise; estimate and plan; generate user acceptance tests; measure value delivery; trace related requirements; perform additional analysis; manage and report project work.

**Elements**

- *Title (optional)* — active-verb goal phrase.
- *Statement of Value* — no mandatory structure. Most popular: **"As a `<who>`, I need to `<what>`, so that `<why>`"**. Another common format: *"Given … When … Then"*.
- *Conversation* — explores and understands the feature and its value; supplements the story with further modelling as it is delivered.
- *Acceptance Criteria* — define the boundaries; help the team understand what the solution must provide. May be supplemented with other analysis models (see Acceptance and Evaluation Criteria, §10.1).

**Strengths** — easily understandable; supports varied elicitation techniques; focuses on value; collaboration enhances shared understanding of the domain; tied to small, implementable, testable slices.

**Limitations** — intended for short-term capture and prioritisation, **not** for long-term knowledge retention or detailed analysis; team can lose sight of the big picture if stories aren't traced or supplemented with higher-level visual artifacts; may not meet governance or baseline documentation needs.

---

## 10.50 Workshops

**Purpose** — bring stakeholders together to collaborate on achieving a predefined goal.

**Description** — focused event attended by key stakeholders and SMEs for a concentrated period. Used for planning, analysis, design, scoping, requirements elicitation, modelling, idea generation, consensus, review of requirements / designs.

Workshops generally include: representative group of stakeholders, a defined goal, interactive and collaborative work, a defined work product, a facilitator.

Promotes trust, mutual understanding, strong communication; produces deliverables that structure future work.

**Elements**

### .1 Prepare for the Workshop

- define purpose and desired outcomes;
- identify key stakeholders to participate;
- identify facilitator and scribe;
- create the agenda;
- determine how outputs will be captured;
- schedule the session and invite participants;
- arrange room logistics and equipment;
- send the agenda and other materials in advance;
- if appropriate, conduct **pre-workshop interviews** with participants.

### .2 Workshop Roles

- **Sponsor** — frequently not a participant but accountable for the outcome.
- **Facilitator** — sets professional and objective tone; introduces goals / agenda; enforces structure and ground rules; keeps activities focused; facilitates decision-making and conflict resolution; ensures all participants have a chance to be heard.
- **Scribe** — documents decisions in the format determined prior to the workshop; tracks deferred items and issues.
- **Timekeeper** — keeps track of time on each agenda item.
- **Participants** — key stakeholders and SMEs; provide input, listen to other views, discuss without bias.

### .3 Conduct the Workshop

Begin with statement of purpose and outcomes. Optionally an ice-breaker. Agree ground rules:

- respect the opinions of others;
- everyone is expected to contribute;
- off-topic discussion limited to a specific time;
- discuss the issues, not the people;
- agreement on how decisions are made.

Throughout, the facilitator validates activities against the workshop's purpose and outcomes.

### .4 Post Workshop Wrap-up

Follow up on action items; complete documentation; distribute to attendees and other stakeholders who need to be informed.

**Strengths** — agreement in a short period; collaboration / decision-making / mutual understanding; lower cost than equivalent multiple interviews; immediate feedback.

**Limitations** — scheduling difficulty; depends on facilitator expertise and participant knowledge; too many participants slows the workshop; too few may overlook stakeholder needs or yield non-representative decisions.
