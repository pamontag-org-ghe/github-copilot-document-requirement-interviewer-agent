# Chapter 13 — Software Security

> Source: **SWEBOK Guide v4.0**, Chapter 13 *Software Security* (pp. 13-1 → 13-8).
> This file is a cleaned, structure-preserving transcription of the chapter for use as a knowledge-base reference when eliciting, specifying and validating **security requirements**. The chapter is small in SWEBOK v4 and is preserved in full.
> Page numbers `[13-x]` refer to chapter pagination in the source PDF.

## Acronyms

| Acronym | Meaning |
|---|---|
| CAPEC | Common Attack Pattern Enumeration and Classification |
| CC    | Common Criteria |
| CIA   | Confidentiality, Integrity, Availability |
| CVE   | Common Vulnerabilities and Exposures |
| CVSS  | Common Vulnerability Scoring System |
| CWE   | Common Weakness Enumeration |
| ISMS  | Information Security Management System |
| SDLC  | Secure Development Life Cycle |
| SSE-CMM | Systems Security Engineering — Capability Maturity Model |

## Introduction `[13-1]`

Security is now a primary concern in software development because of misuse and malicious activity. Beyond correctness and reliability, software developers must address the **security** of what they build. **Secure software development** builds security in by following established rules and practices. **Secure software maintenance** ensures no security problems are introduced during maintenance and that identified vulnerabilities (errors attackers can exploit) are handled across the life cycle. Vulnerabilities can also originate from **third-party components** (libraries, COTS, OS).

---

## 1. Software Security Fundamentals `[13-1, 13-2]`

It is **much better to design security into software than to patch it in afterwards**. Security must be considered at every life-cycle stage: requirements, design, construction, testing, and maintenance.

### 1.1 Software Security `[13-1]`

Security is a **product quality characteristic** (ISO/IEC 25010 — see Quality KA): the degree to which a product or system protects information and data so that persons or other products/systems have data access appropriate to their types and levels of authorisation.

### 1.2 Information Security `[13-1]`

Information security preserves **Confidentiality, Integrity, Availability** (CIA), and may also involve **authenticity, accountability, non-repudiation, reliability** (ISO/IEC 27000):

- **Confidentiality** — information is not disclosed to unauthorised individuals/entities/processes.
- **Integrity** — accuracy and completeness.
- **Availability** — accessible and usable on demand by an authorised entity.

Software engineers must **define the security properties** of their software and **maintain them throughout the life cycle**.

### 1.3 Cybersecurity `[13-2]`

Cybersecurity safeguards people, society, organisations and nations from cyber risks at a *tolerable* level. Threats to mitigate:

- Social engineering
- Hacking
- Proliferation of malware
- Spyware
- Other potentially unwanted software

---

## 2. Security Management and Organization `[13-2, 13-3]`

Security governance and management are most effective when systematic — *woven into the culture and fabric of organisational behaviours and actions*. Project managers must elevate software security from a stand-alone technical concern to an **enterprise issue**.

### 2.1 Capability Maturity Model `[13-2]`

**SSE-CMM** (Systems Security Engineering — Capability Maturity Model) measures the process capability of an organisation performing risk assessments.

### 2.2 Information Security Management System (ISMS) `[13-2, 13-3]`

**ISO/IEC 27001:2022** specifies requirements for establishing, implementing, maintaining and continually improving an ISMS. An ISMS:

- documents risks and the measures to address them;
- protects the organisation's data and prevents breaches;
- continually conducts risk assessments to identify risks/vulnerabilities and deploy protective measures.

An ISMS can **raise new or changed software security requirements**. Additional sources: laws, regulations, contractual compliance obligations.

### 2.3 Agile Practice for Software Security `[13-3]`

Agile teams must adopt security practices and take responsibility for their systems' security. Security professionals must accept change, work faster and iteratively, and think about risk incrementally. Keys to success: involvement of security team and developers, enablement, automation, agility.

---

## 3. Software Security Engineering and Processes

### 3.1 Security Engineering and Secure Development Life Cycle (SDLC) `[13-3]`

Software is only as secure as its development process. **SDLC** uses a classical spiral model that views security holistically across the life cycle so security is **inherent in design and development, not an afterthought**. SDLC reduces software maintenance costs and increases reliability against security faults.

**DevSecOps** extends SDLC with culture, automation and platform design to keep the software life cycle as agile and responsible as Agile development and CI.

### 3.2 Common Criteria (ISO/IEC 15408:2022) `[13-3]`

**Common Criteria (CC)** for Information Technology Security Evaluation establishes confidence in the security functionality of IT products and the assurance measures applied to them. Useful for developing, evaluating and procuring IT products with security functionality. CC categorises protection failures as **confidentiality, integrity and availability**.

---

## 4. Security Engineering for Software Systems

### 4.1 Security Requirements `[13-3, 13-4]`

Security requirements engineering includes **elicitation, specification, and prioritization**. It considers:

- **threats**, illustrated by **misuse and abuse cases**;
- **threat actors**;
- **security risk assessments**;
- selection and application of specification methods;
- prioritization methods;
- inspections and revisions.

Selection of life-cycle model may impact the order of activities. Software product revisions imply **revisiting security requirements**. **Traceability of security requirements throughout the development process is important**. Security teams may include specialists in security requirements. Many methods and tools exist.

### 4.2 Security Design `[13-4]`

Concerns **prevention** of unauthorised disclosure, creation, change, deletion or denial of access to information and other resources — and **tolerance** of attacks by limiting damage, continuing service, speeding repair and recovery, and **failing and recovering securely**.

**Access control** is fundamental; most controls build on **cryptographic algorithms and cryptographic material** (keys, distribution, management).

To meet security requirements, developers conduct **threat modeling** — illustrating how a system is being attacked to specify a mitigation design. Factors include frameworks and access modes (overall enforcement strategy) and the individual policy-enforcement mechanisms.

### 4.3 Security Patterns `[13-4]`

A **security pattern** describes a recurring security problem in a specific context and presents a proven generic solution.

### 4.4 Construction for Security `[13-4, 13-5]`

Coding of security into software can follow recommended rules:

- Structure the process so that **all sections requiring extra privileges are modules**; modules small, doing only privileged tasks.
- **Validate all assumptions**; if not possible, document them for installers and maintainers.
- Ensure the program does not share in-memory objects with any other program.
- **Check every function's error status**; do not recover unless neither the cause nor the effects affect security; otherwise restore state and terminate.

#### CERT Top 10 software security practices `[13-5]`

1. **Validate input.**
2. **Heed compiler warnings.**
3. **Architect and design for security policies.**
4. **Keep it simple.**
5. **Default deny.**
6. **Adhere to the principle of least privilege.**
7. **Sanitize data sent to other software.**
8. **Practice defense in depth.**
9. **Use effective quality assurance techniques.**
10. **Adopt a software construction security standard.**

### 4.5 Security Testing `[13-5]`

Security testing ensures the implementation meets the security requirements and contains none of the known vulnerabilities. Two approaches:

1. **Static analysis** — source code or compiled binaries. Detects language/implementation-specific vulnerabilities, optimisation-hidden flaws, vulnerabilities inside compiled third-party components. Automation possible; expert configuration and verification required.
2. **Dynamic testing** — **vulnerability assessment** or **penetration testing** (a.k.a. ethical hacking) to detect vulnerabilities in runtime behaviour; tools include web application scanners and fuzzers. Must be conducted **within legal boundaries and with proper authorization**.

### 4.6 Vulnerability Management `[13-5]`

Sound coding practices reduce defects. Common security defects are categorised in shared databases:

- **CVE** — Common Vulnerabilities and Exposures.
- **CWE** — Common Weakness Enumeration.
- **CAPEC** — Common Attack Pattern Enumeration and Classification.
- **CVSS** — expresses characteristics and severity of vulnerabilities.

**Security maintenance** mitigates vulnerabilities in the system *and in third-party components it uses*. Often comes with a **vulnerability disclosure process** allowing identification reports.

---

## 5. Software Security Tools

### 5.1 Security Vulnerability Checking Tools `[13-5, 13-6]`

**Source code analyzers** detect injection flaws, buffer overflows, insecure library use — finding vulnerabilities identifiable through code patterns and logical flaws. **Binary analysis tools** examine compiled code (incl. third-party libraries) for vulnerabilities not apparent in source or arising during compilation. They cannot find all vulnerabilities (e.g., those in hard-to-produce states or unusual circumstances).

### 5.2 Penetration Testing Tools `[13-6]`

Evaluate a system's security in its operational environment by performing controlled attacks. Techniques include **fuzzing** — submitting malformed/malicious/random data to entry points to detect faults. Provide insights into how a real attacker could exploit the system.

---

## 6. Domain-Specific Software Security `[13-6]`

### 6.1 Security for Container and Cloud

Cloud infrastructure is cheap and easy to provision — leading to **forgotten assets** that become security incidents. Physical asset protection is generally outsourced to the provider; logical security gains relative importance.

### 6.2 Security for IoT Software

IoT systems are interconnected with back-end systems sharing classic business-IT vulnerabilities. Attackers exploiting browser vulnerabilities can also gain access to weakly protected industrial IoT. Required: **hardening of endpoints, secured device-to-device communication, device and information credibility, comprehensive risk and threat analysis**.

### 6.3 Security for Machine Learning-Based Applications

ML presents specific vulnerabilities. Two attack classes:

- **Model poisoning** — attacks the training data.
- **Evasion** — attacks inputs to trained models.

---

## Cross-references back to the Software Requirements KA

- **§4.1 Security Requirements** ⇄ SR KA §1.7 *QoS Constraints — Safety & Security* and §2.1 *Stakeholder Sources* (regulators, ISMS).
- **§4.5 Security Testing** ⇄ Testing KA §2.2.8 (Security) and §2.2.9 (Privacy).
- **§1.2 CIA** ⇄ ISO/IEC 25010 *Security* characteristic (Quality KA §3.3).
- **§4.6 Vulnerability Management** ⇄ Maintenance KA + CVE/CWE/CAPEC/CVSS as inputs to security requirements.
- **§4.1 Misuse/Abuse Cases** ⇄ SR KA §3.1 *complete: boundary, exception, security* and §4.4 *Behavioral Models*.
