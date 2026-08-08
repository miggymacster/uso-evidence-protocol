# USO Reporting Integrity Core v0.2

## Minimum Requirements for Defensible AI Search Reporting

**Author:** A. L. MacFarland  
**Framework:** Universal Search Optimization (USO)  
**Parent Specification:** USO Evidence Protocol v0.9.5  
**Version:** 0.2  
**Status:** Candidate Core Specification  
**License:** CC BY 4.0

---

## 1. Purpose

The USO Reporting Integrity Core defines the minimum requirements for reporting AI-search observations without materially overstating what the underlying evidence establishes.

It is intended for practical use by practitioners, agencies, marketing teams, AI visibility platforms, analysts, researchers, and consultants.

Core Conformance does not imply Full USO Evidence Protocol Conformance.

The governing principle is:

# No conclusion may outrun its evidence.

---

## 2. Core Evidence States

Where applicable, reports SHOULD distinguish:

- MENTIONED;
- CITED;
- INCLUDED;
- RECOMMENDED;
- ADVERSELY_TREATED.

These states MUST NOT be silently treated as equivalent.

**Citation is not recommendation.**  
**Mention is not inclusion.**  
**Inclusion is not recommendation.**  
**Recommendation is not conversion.**

---

# The 12 Core Requirements

## CORE-1: Declare the Scope of Measurement

Every report containing a Derived Metric MUST disclose, where applicable:

- systems tested;
- System Selection Scope;
- materially relevant systems intentionally excluded;
- observation period;
- Prompt Domain;
- geographic or service-area scope;
- language and locale;
- number of prompts;
- number of valid executions;
- execution count per prompt;
- Prompt Class composition;
- Prompt Provenance;
- Prompt Construction Mode;
- Observation State being measured.

A report MUST NOT imply broader system, geographic, market, or prompt coverage than the declared scope supports.

---

## CORE-2: Fix the Test Before Formal Measurement

Before formal measurement begins, the analyst MUST predeclare:

- Prompt Set;
- Prompt Selection Criterion;
- planned execution count per Prompt and system;
- aggregation rule;
- exclusion rules;
- Comparison Selection Criterion where applicable.

Execution counts MUST NOT be increased because a favorable result has not appeared.

Execution counts MUST NOT be reduced because a favorable result appeared early.

Outcome-Dependent Stopping and Outcome-Dependent Continuation are prohibited.

---

## CORE-3: Disclose Prompt Construction and Prevent Favorable Screening

Every formal Prompt MUST disclose its Prompt Provenance.

Prompt construction MUST be identified as:

- ENTITY_INDEPENDENT; or
- ENTITY_INFORMED.

ENTITY_INFORMED Prompts are permitted, but MUST NOT be represented as neutral or representative discovery evidence without separate justification.

Formal Prompts MUST NOT be selected or removed according to previously observed favorable Target Entity performance.

If an exploratory screen preceded the formal Prompt Set, the report MUST disclose the screening population and selection procedure where Target Entity performance was visible.

---

## CORE-4: Pre-Record the Represented Need and Separate Branded from Non-Branded

Where INCLUDED or RECOMMENDED is classified, the Represented Need for the Prompt MUST be recorded before the first valid execution.

The Represented Need MUST NOT be broadened or redefined after viewing the response merely to obtain a preferred classification.

Every formal Prompt MUST be identified at minimum as:

- BRANDED; or
- NON_BRANDED.

Branded and non-branded results MUST remain separately visible.

Strong branded performance MUST NOT be represented as non-branded category discovery performance.

---

## CORE-5: Report the Execution-Level Reality

Where repeated executions are used, the report MUST disclose:

- OBSERVED Executions;
- NOT OBSERVED Executions;
- NOT ESTABLISHED Executions;
- valid Execution count.

If a Prompt-level reduction such as ANY_OBSERVED is shown, its corresponding execution-level result MUST appear at Equal Prominence.

A Prompt-level percentage MUST NOT visually conceal materially lower execution-level occurrence.

---

## CORE-6: Report Determination Coverage

When an Observation State is not determinable for every valid Execution, the report MUST disclose:

**Determination Coverage = (OBSERVED + NOT OBSERVED) / Valid Executions**

Determination Coverage MUST appear at Equal Prominence with the corresponding rate.

When Determination Coverage is below 50%:

- raw counts across all valid Executions MUST be the primary presentation;
- the determinable-execution percentage MUST NOT be the headline metric;
- the percentage MAY appear only as a secondary technical statistic.

The 50% threshold is a reporting-integrity boundary indicating that most observations are indeterminate. It is not a statistical-sufficiency claim.

---

## CORE-7: Report Favorable, Adverse, and Validation Evidence Together

Whenever INCLUDED or RECOMMENDED is reported, ADVERSELY_TREATED MUST also be classified for the same executions and shown at Equal Prominence.

Decision-Material Claims associated with INCLUDED, RECOMMENDED, or ADVERSELY_TREATED results MUST be identified where applicable.

Where authoritative evidence is reasonably available, the report MUST disclose the Claim Validation distribution:

- VERIFIED;
- INACCURATE;
- MATERIALLY_MISLEADING;
- UNVERIFIED;
- NO_CLAIM_EVALUATED where properly applicable.

If one or more Decision-Material Claims remain UNVERIFIED, the report MUST state:

**UNVERIFIED DECISION-MATERIAL CLAIMS PRESENT**

If no Decision-Material Claims were validated, it MUST state:

**DECISION-MATERIAL CLAIMS NOT VALIDATED**

---

## CORE-8: Preserve Execution and Exclusion Integrity

All valid executions defined by the formal test MUST be retained.

Executions MUST NOT be removed because they are unfavorable, contradictory, unexpected, or commercially inconvenient.

Every excluded Execution MUST retain:

- Execution identifier;
- exclusion reason;
- applicable exclusion rule;
- whether that rule existed before execution;
- generated response where available;
- recoverable Observation States where determinable.

A technical exclusion rule MUST NOT operate as an outcome filter.

The report MUST disclose excluded execution count, exclusion rate, and reason distribution.

Where excluded outputs remain interpretable, recoverable Observation State distribution MUST also be disclosed.

---

## CORE-9: Define the Comparison Universe Before Comparing

Comparative reporting MUST disclose:

- Comparison Universe;
- Comparison Selection Criterion;
- total qualifying entities identified where reasonably knowable;
- entities tested;
- qualifying entities excluded;
- reasons for exclusion.

Comparison Entities MUST NOT be selected according to previously observed weak AI-search performance.

If an external source cannot reasonably define the universe, the report MUST disclose:

**ANALYST-DEFINED COMPARISON UNIVERSE**

A win against a tested subset MUST NOT be represented as market or category leadership.

---

## CORE-10: Keep Systems, Competitors, and Time Periods Like-for-Like

Comparisons across systems, competitors, reporting periods, baselines, or pre/post-remediation periods MUST use materially comparable controllable conditions.

Relevant differences include:

- Prompt Set;
- Prompt Classes;
- execution counts;
- systems or models;
- authentication;
- personalization;
- memory;
- geography;
- locale;
- Classification Method;
- aggregation rule.

Where material differences exist:

**NON-EQUIVALENT TEST CONDITIONS**

MUST appear at Equal Prominence.

Selected systems MUST NOT be represented as universal AI behavior.

---

## CORE-11: Do Not Imply Causality Without Evidence

Before-and-after observation does not establish intervention causality.

This rule applies to the entire artifact, including:

- title;
- subtitle;
- filename;
- executive summary;
- chart title;
- captions;
- annotations;
- case-study name;
- surrounding narrative;
- conclusion.

Temporal association MAY be reported.

Causal attribution requires separate supporting evidence.

---

## CORE-12: Preserve Meaning in Presentation and Derivative Artifacts

Interpretation-critical qualifiers MUST have Equal Prominence with the metric they qualify.

They MUST NOT exist only in:

- fine print;
- footnotes;
- appendices;
- methodology links;
- tooltips;
- collapsed interface elements;
- separate documents available only on request.

Co-location alone does not establish Equal Prominence.

A required qualifier MUST not be materially smaller, lower contrast, or visually subordinated to the metric it qualifies.

If the same person or organization creates, authorizes, commissions, or distributes a derivative slide, dashboard, social graphic, executive summary, case study, or sales artifact using a USO-governed metric, interpretation-critical qualifiers MUST travel with the metric.

A derivative artifact that strips those qualifiers MUST NOT:

- claim USO conformance;
- imply that the derivative claim is USO-conformant;
- display a USO conformance designation;
- cite USO as validating the decontextualized metric.

---

## 3. Minimum Reporting Block

A USO Core-conformant report SHOULD provide a summary substantially equivalent to:

### Scope of Measurement

**Prompt Domain:** Local service provider selection  
**Geographic scope:** Greenville, South Carolina, United States  
**Language / locale:** English / en-US  
**Systems tested:** ChatGPT, Gemini, Perplexity  
**Material system exclusions:** Claude, with reason disclosed  
**Prompt construction:** ENTITY_INDEPENDENT  
**Prompt provenance:** Search-query data and observed customer language  
**Prompts:** 20  
**Prompt composition:** 15 NON_BRANDED / 5 BRANDED  
**Executions:** 3 per Prompt per system  
**Valid Executions:** 180

### Recommendation Evidence

**Prompt-level:** 12/20 Prompts, 60%  
**Reduction rule:** ANY_OBSERVED  
**Execution-level:** 27/180 Executions, 15%  
**NOT ESTABLISHED:** 4/180  
**Determination Coverage:** 176/180, 97.8%

### Decision Context

**ADVERSELY_TREATED:** 8/180 Executions

**Claim Validation**
- VERIFIED: 22
- INACCURATE: 2
- MATERIALLY_MISLEADING: 1
- UNVERIFIED: 4

### Comparison Status

**Comparison Universe:** 8 qualifying providers  
**Entities tested:** 5 of 8  
**Qualifying exclusions:** disclosed with reasons  
**Comparison conditions:** Equivalent

### Interpretation

> Recommendation was observed within the declared Test environment. These results describe the tested Prompts, systems, executions, geography, locale, and observation period. They do not independently establish total market visibility, audience demand, consumer preference, or business impact.

---

## 4. Prohibited Reporting Practices

A report claiming USO Reporting Integrity Core Conformance MUST NOT:

- convert tested Prompts into market share;
- represent analyst-created or ENTITY_INFORMED Prompts as audience demand without independent evidence;
- represent partial system coverage as universal AI behavior;
- generalize single-locale or narrow-geography evidence beyond its scope;
- hide execution-level results behind Prompt-level percentages;
- hide low Determination Coverage;
- combine branded and non-branded results without showing both components;
- suppress valid unfavorable Executions;
- use technical exclusions as outcome filters;
- select formal Prompts according to favorable observed outcomes;
- select weak competitors according to prior observed performance;
- present Recommendation without Adverse Treatment results;
- treat inaccurate recommendations as equivalent to accurate recommendations;
- imply category leadership from a limited Comparison Set;
- present materially non-equivalent Tests as like-for-like;
- imply intervention causality from temporal sequence or presentation framing;
- hide interpretation-critical qualifiers in fine print;
- strip required qualifiers from controlled derivative artifacts while retaining a USO conformance implication.

---

## 5. Conformance Claim

A report satisfying every applicable Core requirement MAY state:

> **USO Reporting Integrity Core v0.2: Conformant**

A report that does not satisfy every applicable requirement MUST NOT make that statement.

If selected controls are used without full Core Conformance, the artifact MAY state:

> **Uses selected controls from USO Reporting Integrity Core v0.2. Not fully conformant.**

The term:

**USO Certified**

MUST NOT be used under this candidate specification.

---

## 6. Relationship to the Full USO Evidence Protocol

The USO Reporting Integrity Core governs the minimum reporting controls necessary for defensible communication of AI-search evidence.

The full USO Evidence Protocol v0.9.5 additionally governs:

- Test Manifests;
- Test Registries;
- Execution Observation records;
- detailed system context;
- automated classifier controls;
- audit-sampling integrity;
- retrieval evidence;
- source conflict handling;
- evidence preservation;
- implementation conformance;
- adversarial review;
- governance.

Core Conformance does not imply Full Protocol Conformance.

Full Protocol Conformance includes all applicable Core reporting requirements.

---

## 7. Core-to-Protocol Mapping

| Core Requirement | Primary v0.9.5 Clauses |
|---|---|
| CORE-1 Scope of Measurement | §§7, 8, 21, 22, 49 |
| CORE-2 Fixed Test Design | §§10, 15, 16, 17 |
| CORE-3 Prompt Construction | §§12, 13, 14, 21 |
| CORE-4 Represented Need / Prompt Class | §§11, 22, 30 |
| CORE-5 Execution-Level Reality | §§41, 42, 43, 44 |
| CORE-6 Determination Coverage | §45 |
| CORE-7 Adverse / Validation | §§34, 37, 38 |
| CORE-8 Exclusions | §§18, 19, 20 |
| CORE-9 Comparison Universe | §§52, 53, 54 |
| CORE-10 Comparability / Systems | §§8, 24, 51, 55, 57 |
| CORE-11 Causality | §§58, 59, 62 |
| CORE-12 Presentation / Derivatives | §§4.22, 49, 50 |

---

## 8. Core Design Principle

The Core is intentionally compact.

Its purpose is not to prescribe every detail of AI-search research.

Its purpose is to prevent a bounded Test from being communicated as a stronger conclusion than the evidence supports.

A Core-conformant report should allow a reasonable reader to determine:

**What was tested?**

**How was the Prompt Set constructed?**

**Which systems, geography, and locale were covered?**

**What happened across the actual Executions?**

**How much of the Test was determinable?**

**Were favorable and unfavorable states both shown?**

**Were the Decision-Material Claims accurate?**

**How were exclusions handled?**

**How were competitors selected?**

**Were comparisons genuinely comparable?**

**Is the artifact describing observation or implying causation?**

**Did the meaning survive when the metric was reused elsewhere?**

If those questions cannot be answered from the report itself, the reporting standard has not done its job.

# No conclusion may outrun its evidence.
