# Chapter 2 — Business Analysis Key Concepts (BABOK v3)

> Source: **A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide), v3**, Chapter 2 *Business Analysis Key Concepts* (pp. 11–22).
> This file is a cleaned, structure-preserving extract used as the conceptual foundation for the `babok-v3-software-requirements` skill.

## 2.1 The Business Analysis Core Concept Model™ (BACCM™)

BACCM™ is a conceptual framework for business analysis. It is composed of **six equally important core concepts**, each defined by the other five:

| Core Concept | Definition (BABOK v3) |
|---|---|
| **Change** | The act of transformation in response to a need. Improvements are deliberate and controlled through business analysis activities. |
| **Need** | A problem or opportunity to be addressed. Needs can cause changes by motivating stakeholders to act; changes can also cause needs by eroding or enhancing the value of existing solutions. |
| **Solution** | A specific way of satisfying one or more needs in a context. A solution satisfies a need by resolving a problem or enabling the exploitation of an opportunity. |
| **Stakeholder** | A group or individual with a relationship to the change, the need, or the solution. Often defined by **interest, impact, and influence**. |
| **Value** | The worth, importance, or usefulness of something to a stakeholder within a context. Can be tangible or intangible; can also be negative (losses, risks, costs). |
| **Context** | The circumstances that influence, are influenced by, and provide understanding of the change. Includes attitudes, behaviours, beliefs, competitors, culture, demographics, goals, governments, infrastructure, languages, processes, products, technology, etc. |

The BACCM is used to:

- describe the profession and domain of business analysis;
- communicate with common terminology;
- evaluate the relationships among key concepts;
- evaluate quality and completeness of the work by holistically assessing the six concepts;
- evaluate the impact of changes to any concept on the others.

When planning or performing any task, the analyst asks BACCM-driven questions:

- What are the kinds of changes we are doing?
- What are the needs we are trying to satisfy?
- What are the solutions we are creating or changing?
- Who are the stakeholders involved?
- What do stakeholders consider to be of value?
- What contexts are we and the solution in?

> If any core concept changes, re-evaluate all six concepts and their relationships to value delivery.

## 2.2 Key Terms

- **Business Analysis** — "the practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value to stakeholders".
- **Business Analysis Information** — broad, diverse information that BAs analyze, transform and report (elicitation results, requirements, designs, solution options, solution scope, change strategy, …).
- **Design** — a usable representation of a solution; focuses on *how* value might be realized if built.
- **Enterprise** — a system of one or more organizations and the solutions they use to pursue a shared set of goals.
- **Organization** — an autonomous group of people under the management of a single individual or board.
- **Plan** — a proposal for doing or achieving something; describes events, dependencies, sequence, schedule, outcomes, resources, stakeholders.
- **Requirement** — a usable representation of a need; focuses on *what* kind of value could be delivered if the requirement is fulfilled.
- **Risk** — the effect of uncertainty on the value of a change, solution, or enterprise.

## 2.3 Requirements Classification Schema

BABOK v3 categorises requirements as:

- **Business requirements** — statements of goals, objectives, and outcomes describing *why* a change has been initiated. Apply to the whole enterprise, a business area, or a specific initiative.
- **Stakeholder requirements** — describe the needs of stakeholders that must be met to achieve the business requirements. Bridge between business and solution requirements.
- **Solution requirements** — describe the capabilities and qualities of a solution that meet the stakeholder requirements. Two sub-categories:
  - **Functional requirements** — capabilities the solution must have, in terms of behaviour and information it manages.
  - **Non-functional requirements** (a.k.a. **quality of service requirements**) — conditions under which the solution must remain effective, or qualities it must have.
- **Transition requirements** — capabilities the solution must have and conditions it must meet to facilitate transition from current state to future state, but **not needed once the change is complete** (temporary). Examples: data conversion, training, business continuity.

The elicitation interview must cover all four levels — failure to do so is a primary source of late, costly rework.

## 2.4 Stakeholders (generic role list)

Generic stakeholder roles used throughout the BABOK Guide:

| Generic role | Typical actual roles | Why interview them |
|---|---|---|
| **Business analyst** | (the analyst themselves) | Inherent in all BA activities. |
| **Customer** | end customer / buyer | Uses or may use the product or service; may have contractual or moral rights. |
| **Domain Subject Matter Expert (SME)** | end user, manager, process owner, legal staff, consultant | In-depth knowledge of the topic, business need or solution scope. |
| **End User** | participant in a business process; user of the product | Directly interacts with the solution; primary source of usability and functional fit feedback. |
| **Implementation SME** | architect, developer, DBA, info architect, usability analyst, trainer, change consultant | Designs / builds / deploys the solution; ensures feasibility. |
| **Operational Support** | ops analyst, product analyst, help desk, release manager | Day-to-day management and maintenance. |
| **Project Manager** | project / technical / product lead | Balances scope, budget, schedule, resources, quality, risk. |
| **Regulator** | government, regulatory body, auditor | Defines and enforces standards / legislation / corporate governance. |
| **Sponsor** | executive sponsor, project sponsor | Authorises the work, controls budget and scope. |
| **Supplier** | vendor, provider, consultant | External provider of products or services. |
| **Tester** | QA analyst | Verifies the solution meets the requirements; ensures quality and risk are managed. |

> A single individual may fill more than one role; any stakeholder can be a source of requirements, assumptions, or constraints.

## 2.5 Requirements and Designs

Requirements focus on the **need**; designs focus on the **solution**. The distinction is not always crisp — the same techniques are used to elicit, model, and analyze both. A requirement leads to a design; a design may drive the discovery of more requirements.

The cycle is:

1. **Business Requirements** — *Why* do I want it?
2. **Stakeholder Requirements** — *What are the needs?*
3. **Solution Requirements** — *What do I want?*
4. **Transition Requirements** — *What are the conditions?*
5. **Designs** — usable representations of the solution.
6. **Assess Outcomes** — verify value delivery; the cycle continues until requirements are met.

When a stakeholder presents a *solution* rather than a need, the analyst's job is to **continuously ask "why?"** until the underlying business / stakeholder requirement is reached.

| Example requirement | Example design |
|---|---|
| View six months of sales data across multiple organizational units in a single view. | A sketch of a dashboard. |
| Reduce the time required to pick and pack a customer order. | A process model. |
| Record and access a medical patient's history. | Screen mock-up with specific data fields. |
| Develop business strategy, goals, and objectives for a new business. | Business Capability Model. |
| Provide information in English and French. | Prototype with text displayed in English and French. |
