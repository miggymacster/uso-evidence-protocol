# USO Evidence Protocol v0.9.5

## Final Candidate Specification for AI Search Observation, Validation, Aggregation, Reporting Integrity, and Evidence Governance

**Author:** A. L. MacFarland  
**Framework:** Universal Search Optimization (USO)  
**Version:** 0.9.5  
**Status:** Final Candidate Specification  
**Specification Owner:** A. L. MacFarland  
**License:** CC BY 4.0  
**Canonical Repository:** Pending public repository  
**Persistent Identifier:** Pending candidate release DOI  
**Review Channel:** Public repository issue tracker upon release  
**Purpose:** Final normative candidate prior to schema implementation, Gold Test Set validation, independent classification testing, and v1.0 consideration.

---

## 1. Purpose

The USO Evidence Protocol specifies a method for recording, classifying, validating, aggregating, comparing, and reporting evidence produced by AI-mediated search and discovery systems.

The protocol exists to prevent observational evidence from being converted into conclusions stronger than the underlying test supports.

It separately governs:

1. system observation;
2. factual validation;
3. uncertainty;
4. scope of measurement;
5. prompt and sample construction;
6. execution design;
7. aggregation;
8. comparison;
9. reporting and presentation;
10. intervention claims;
11. derivative reporting;
12. publication integrity.

The governing principle is:

**No conclusion may outrun its evidence.**

---

## 2. Scope

The protocol may be applied to:

- AI assistants;
- answer engines;
- generative search systems;
- AI-generated search summaries;
- retrieval-augmented systems;
- agentic discovery systems;
- comparable machine-mediated discovery environments.

The protocol applies to individual executions and collections of executions.

It does not independently establish:

- population-level demand;
- market share;
- consumer preference;
- platform-wide behavior;
- traffic;
- conversion;
- revenue;
- causal business impact;
- causal impact of optimization or remediation.

Those conclusions require separate supporting evidence.

---

## 3. Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in BCP 14, RFC 2119, and RFC 8174 when, and only when, they appear in all capitals.

A report, dataset, benchmark, system, or implementation claiming compatibility with this protocol MUST satisfy every applicable MUST and MUST NOT requirement.

---

## 4. Defined Terms

### 4.1 Execution

One completed interaction between a defined Prompt and a defined system environment.

### 4.2 Execution Observation

The evidence record created from one Execution.

### 4.3 Prompt

The query, instruction, conversational input, or other user-supplied input being tested.

### 4.4 Represented Need

The need, problem, decision, comparison, or selection task expressed by the Prompt.

Where INCLUDED or RECOMMENDED will be classified, the Represented Need MUST be recorded before the first valid Execution.

The Represented Need MUST NOT be broadened, narrowed, or redefined after examining the response to obtain a preferred classification.

### 4.5 Prompt Set

The declared collection of Prompts included in a Test.

### 4.6 Prompt Class

A category describing the decision context or construction of a Prompt.

Examples include:

- BRANDED;
- NON_BRANDED;
- INFORMATIONAL;
- PROBLEM_RECOGNITION;
- COMPARISON;
- ALTERNATIVES;
- REPUTATION;
- TRANSACTIONAL;
- PURCHASE_CONSIDERATION;
- OTHER.

### 4.7 Prompt Provenance

The documented origin or evidentiary basis of a Prompt.

### 4.8 Prompt Construction Mode

The relationship between the Prompt's construction and knowledge of the Target Entity.

Allowed values are:

**ENTITY_INDEPENDENT**

The Prompt was constructed without using attributes, differentiators, known strengths, known weaknesses, or prior observed performance of the Target Entity to shape the Prompt.

**ENTITY_INFORMED**

Knowledge of the Target Entity, its differentiators, attributes, services, strengths, weaknesses, positioning, or other characteristics materially informed Prompt construction.

ENTITY_INFORMED does not make a Prompt invalid.

It changes what conclusions may reasonably be drawn from the resulting test.

### 4.9 Prompt Selection Criterion

The declared rule determining which Prompts enter a Prompt Set.

### 4.10 Test

Any organized set of one or more Executions used to examine AI-mediated search behavior.

### 4.11 Exploratory Test

A Test intended to investigate hypotheses, discover topics, examine behavior, or inform future study design without qualifying as Formal Measurement.

### 4.12 Formal Measurement

Any Test whose results:

- appear in a Published Artifact containing a Derived Metric;
- inform a client or business decision;
- support a benchmark;
- support a contractual or performance claim;
- support a public comparative statement;
- support a public claim about the measured entity;
- are represented as evidence of performance, improvement, decline, standing, visibility, recommendation, or comparable outcome.

Formal Measurement is determined by how results are used, not by the analyst's chosen label.

### 4.13 Test Manifest

The pre-execution record defining the Test.

### 4.14 Test Registry

A chronological record of Tests performed by the analyst or organization.

### 4.15 Test Family

Tests addressing materially comparable questions about the same Target Entity, Prompt Domain, system scope, or reporting objective.

A Test Family MUST NOT be defined or fragmented primarily to avoid prior-Test disclosure requirements.

### 4.16 Prompt Domain

The declared subject, category, decision context, product or service scope, or other substantive boundary represented by the Prompt Set.

### 4.17 System Selection Scope

The declared basis for determining which AI systems are eligible for inclusion in the Test.

### 4.18 Scope of Measurement

The complete declared boundary of what the Test measures.

It includes, where applicable:

- Prompt Domain;
- Prompt Construction Mode;
- Prompt Provenance;
- Prompt Classes;
- geographic scope;
- service area;
- language;
- locale;
- System Selection Scope;
- systems tested;
- systems intentionally excluded;
- execution period.

### 4.19 Published Artifact

Any report, dashboard, document, presentation, webpage, export, social publication, research paper, case study, or other artifact communicating results to an intended audience.

### 4.20 Authorized Derivative Artifact

A Published Artifact created, commissioned, approved, distributed, or materially controlled by the same person or organization claiming USO conformance and containing a metric, conclusion, visualization, or claim derived from a USO-governed Test.

### 4.21 Same-Artifact Disclosure

Information presented within the same Published Artifact as the metric or claim it qualifies.

### 4.22 Equal Prominence

A required qualifier has Equal Prominence when a reasonable reader encountering the primary metric or claim would encounter the qualifier as part of the same act of reading.

Required qualifiers MUST:

- appear in the same visual or textual presentation area;
- remain visible without expansion, hover, secondary navigation, or another link;
- use legible typography;
- use materially comparable contrast;
- not be visually subordinated as fine print;
- not be materially reduced in size relative to the qualified metric;
- not be placed behind collapsed interface elements.

Co-location alone does not establish Equal Prominence.

### 4.23 Accessible Evidence

Evidence is Accessible when delivered to the intended audience with the Published Artifact through:

- the artifact itself;
- an attached evidence appendix;
- an explicitly linked companion evidence artifact.

Access MUST NOT require additional payment, discretionary analyst approval, or a separate request.

### 4.24 Target Entity

The entity being evaluated.

### 4.25 Comparison Set

The declared entities directly compared with the Target Entity.

### 4.26 Comparison Universe

The broader identifiable population from which the Comparison Set is selected.

### 4.27 Decision Set

Entities presented by the system as legitimate candidates relevant to the Represented Need.

### 4.28 Source of Record

An authoritative source designated as controlling for a specific factual claim where such a source exists.

### 4.29 Decision-Material Claim

A factual claim capable of materially influencing inclusion, exclusion, recommendation, adverse treatment, comparison, qualification, or purchase suitability.

### 4.30 Derived Metric

Any score, percentage, rate, aggregate, index, or summary calculated from Execution Observations.

### 4.31 Determination Coverage

The proportion of valid Executions for which an Observation State could be classified as OBSERVED or NOT OBSERVED.

**Determination Coverage = (OBSERVED + NOT OBSERVED) / Valid Executions**

### 4.32 Outcome-Dependent Stopping

Changing execution count according to whether a desired or undesired state has occurred.

### 4.33 Outcome-Informed Prompt Selection

Selecting or excluding Prompts for Formal Measurement based on previously observed Target Entity performance.

### 4.34 Outcome-Informed Comparison Selection

Selecting, excluding, narrowing, or defining Comparison Entities or a Comparison Universe according to previously observed AI-search performance.

---

## 5. Evidence Architecture

### 5.1 Observation States

The protocol defines:

- RETRIEVED;
- MENTIONED;
- CITED;
- INCLUDED;
- RECOMMENDED;
- ADVERSELY_TREATED.

Each MUST use one value:

- OBSERVED;
- NOT OBSERVED;
- NOT ESTABLISHED.

OBSERVED means sufficient evidence establishes that the state occurred.

NOT OBSERVED means the relevant output could be evaluated and the state did not occur.

NOT ESTABLISHED means available evidence is insufficient to determine whether the state occurred.

NOT ESTABLISHED MUST NOT be converted into NOT OBSERVED.

NOT OBSERVED MUST NOT be converted into NOT ESTABLISHED when the state is reasonably determinable.

### 5.2 Claim Validation States

Allowed values are:

- VERIFIED;
- INACCURATE;
- MATERIALLY_MISLEADING;
- UNVERIFIED;
- NO_CLAIM_EVALUATED.

Validation applies to identified claims, not automatically to entire responses.

NO_CLAIM_EVALUATED MAY be used only when no Decision-Material Claim within the relevant scope requires evaluation.

---

## 6. Fundamental Evidence Rule

Every reported conclusion MUST remain within the evidentiary boundary of the observation that produced it.

Citation establishes citation.

Mention establishes mention.

Inclusion establishes inclusion.

Recommendation establishes recommendation within the recorded Execution.

None independently establishes market prevalence, audience demand, consumer preference, traffic, conversion, revenue, source causality, or intervention causality.

---

## 7. Scope of Measurement Declaration

Every Formal Measurement MUST declare a Scope of Measurement before the first valid Execution.

The Scope MUST identify, where applicable:

- Prompt Domain;
- geographic scope;
- service or market scope;
- language;
- locale;
- Prompt Construction Mode;
- Prompt Provenance;
- Prompt Class composition;
- System Selection Scope;
- systems selected;
- known material systems intentionally excluded;
- execution period.

The Scope of Measurement MUST appear at Equal Prominence with the first primary Derived Metric in the Published Artifact.

A report MUST NOT imply broader coverage than its Scope of Measurement supports.

---

## 8. System Selection Scope

A Formal Measurement involving one or more AI systems MUST declare the criteria used to select those systems.

The Published Artifact MUST disclose:

- eligible-system criteria;
- systems tested;
- materially relevant systems intentionally excluded where known;
- reason for material exclusions;
- material access limitations.

The protocol does not require identification of every AI system in existence.

It requires transparency about the system scope against which the report's claims are made.

Results from selected systems MUST NOT be described as universal AI behavior.

---

## 9. Test Registry Requirement

Every Test, including Exploratory and Formal Tests, MUST enter the Test Registry before its first valid Execution.

The Test Registry MUST preserve:

- Test identifier;
- Target Entity;
- Test Family;
- Test type;
- creation date;
- start date;
- completion date;
- disposition.

A Test MUST NOT disappear because its results are unfavorable.

The Test Registry MUST be available to an auditor evaluating Full Conformance.

For publicly claimed Full Conformance, the existence and disposition of Tests required by the prior-Test disclosure rules MUST be Accessible to the report audience.

---

## 10. Test Manifest Requirement

Every Test MUST have a Test Manifest.

For Formal Measurement, it MUST be completed before the first valid Execution.

It MUST identify:

- Test identifier;
- Test Family;
- Test type;
- Target Entity;
- Scope of Measurement;
- tested systems;
- exact Prompt Set;
- Represented Need for every Prompt where INCLUDED or RECOMMENDED will be classified;
- Prompt Classes;
- Prompt Provenance;
- Prompt Construction Mode;
- Prompt Selection Criterion;
- planned execution count;
- Comparison Set where applicable;
- Comparison Universe where applicable;
- Comparison Selection Criterion;
- execution context;
- Classification Method;
- Observation States;
- validation scope;
- exclusion rules;
- aggregation rules;
- reporting purpose.

Material post-start changes MUST produce a new Manifest version.

Prior Manifest versions MUST remain retained.

---

## 11. Represented Need Record

For every Prompt where INCLUDED or RECOMMENDED is classified, the Represented Need MUST be recorded before the first valid Execution.

The record MUST remain unchanged for that Test unless a Manifest amendment is created before affected replacement or future Executions.

The Represented Need MUST be included in the Accessible evidence appendix or equivalent evidence record.

An evaluator MUST NOT retrospectively broaden the need merely because redefinition permits a preferred INCLUDED classification.

---

## 12. Exploratory Testing

Exploratory Testing MAY use adaptive methods.

Exploratory results MUST be labeled EXPLORATORY.

Exploratory results MUST NOT be represented as Formal Measurement.

Exploratory testing MAY inform hypotheses, topic coverage, terminology, feasibility, and future test design.

It MUST NOT function as an undisclosed performance screen for favorable Prompt or Comparison Entity selection.

---

## 13. Prompt Construction Disclosure

Prompt construction MUST be classified as ENTITY_INDEPENDENT or ENTITY_INFORMED.

For ENTITY_INFORMED Prompt Sets, the Published Artifact MUST disclose:

- that Target Entity knowledge informed Prompt construction;
- the general attributes or evidence classes used;
- whether known differentiators were incorporated;
- whether competitor attributes informed construction.

ENTITY_INFORMED results MAY be reported.

They MUST NOT be presented as equivalent to entity-independent discovery evidence without separate justification.

---

## 14. Outcome-Informed Prompt Selection

Formal Prompts MUST NOT be selected or removed according to previously observed Target Entity performance.

A prior exploratory screen MAY identify duplicates, malformed Prompts, irrelevant Prompts, or Prompts outside the declared Prompt Domain.

It MUST NOT identify Formal Measurement Prompts according to favorable outcomes.

---

## 15. Prompt Selection Criterion

Formal Measurement MUST predeclare a Prompt Selection Criterion.

The criterion MUST explain why Prompts belong in the Test independently of favorable Target Entity performance.

---

## 16. Fixed Execution Rule

Formal Measurement MUST declare planned valid execution counts before testing.

Outcome-Dependent Stopping and Outcome-Dependent Continuation are prohibited.

Technical replacements for invalid Executions MAY occur but MUST NOT increase the planned valid execution total.

---

## 17. Execution Count Parity

Formal comparisons MUST use equivalent planned execution counts for equivalent Prompt-system combinations.

Material deviations MUST be disclosed at Equal Prominence.

---

## 18. Execution Completeness

Every valid Manifest Execution MUST be retained.

Valid Executions MUST NOT be excluded because they are unfavorable, contradictory, unexpected, or commercially inconvenient.

---

## 19. Exclusion Record

Every excluded Execution MUST retain:

- Execution identifier;
- exclusion reason;
- applicable exclusion rule;
- whether that exclusion rule existed before execution;
- generated response where available;
- recoverable Observation State values where determinable.

An exclusion rule created after an Execution MUST NOT retroactively justify excluding that Execution from a Formal Measurement.

---

## 20. Excluded-Execution Integrity

Excluded Executions MUST remain in an Excluded Execution Ledger.

A technical exclusion rule MUST NOT function as an outcome filter.

The Published Artifact MUST disclose:

- excluded execution count;
- exclusion rate;
- reason distribution.

Where excluded outputs remain interpretable, their recoverable Observation State distribution MUST also be disclosed.

Material outcome skew among excluded Executions MUST be disclosed.

---

## 21. Prompt Provenance

Prompt Provenance MUST be recorded.

Permitted categories include:

- observed customer language;
- search-query data;
- sales interaction;
- support interaction;
- keyword research;
- analyst constructed;
- synthetically generated;
- research dataset;
- other documented source.

Synthetic or analyst-created Prompts MUST NOT automatically be represented as evidence of audience frequency or demand.

---

## 22. Prompt-Class Boundary

Every Formal Measurement Prompt MUST be classified at minimum as BRANDED or NON_BRANDED.

Those results MUST remain independently reportable.

Branded performance MUST NOT establish non-branded category performance.

---

## 23. Execution Context

Execution records MUST preserve, where known:

- system;
- model or variant;
- UI or API;
- authentication;
- personalization;
- memory;
- geography;
- locale;
- language;
- conversation position;
- relevant prior context;
- timestamp.

---

## 24. Context Parity

Formal comparisons MUST use materially equivalent controllable conditions.

Where material parity cannot be achieved:

**NON-EQUIVALENT TEST CONDITIONS**

MUST appear at Equal Prominence.

---

## 25. Classification Method

Every Test MUST declare HUMAN, AUTOMATED, or HYBRID.

Automated classification contributing to a Published Artifact MUST preserve classifier identity, model/version, classification instructions, ruleset, outputs, and confidence information where available.

---

## 26. Automated Classification Audit

Automated classifications materially contributing to published results MUST undergo human audit.

The audit MUST:

- cover at least 10% of automated classifications;
- include at least 20 records where 20 or more exist;
- include all records where fewer than 20 exist;
- use a documented random or stratified procedure.

The person performing the audit SHOULD NOT be solely responsible for configuring or tuning the automated classifier.

Where practical, the auditor SHOULD be independent of classifier configuration.

---

## 27. Audit Sampling Integrity

The classification ledger MUST be closed against modification before the audit sample is selected.

Audit-sample selection MUST be non-predictable at the time the classified records are created.

Where pseudorandom selection is used:

- the seed MUST be generated or committed only after ledger closure;
- the seed MUST be retained in the audit record;
- the selection method MUST be reproducible from the closed ledger and seed.

Records MUST NOT be regenerated, modified, reordered for selection manipulation, or selectively removed after ledger closure.

The Published Artifact MUST disclose audit sample size, selection method, and disagreement rate.

Material systematic disagreement MUST be resolved before publication.

If unresolved:

**CLASSIFICATION RELIABILITY NOT ESTABLISHED**

MUST appear at Equal Prominence with the affected metric.

---

## 28. RETRIEVED

RETRIEVED refers to evidence that a source or information item entered a system's pre-response retrieval or candidate-source process.

Visible citation alone does not establish RETRIEVED.

Where sufficient evidence is unavailable:

**RETRIEVED = NOT ESTABLISHED**

---

## 29. MENTIONED

MENTIONED = OBSERVED when the Target Entity is explicitly identifiable in the response.

Mention does not establish Inclusion or Recommendation.

---

## 30. INCLUDED

INCLUDED = OBSERVED when the Target Entity is presented as a legitimate candidate capable of satisfying the pre-recorded Represented Need.

An evaluator MUST NOT redefine the Represented Need after seeing the response.

If decision relevance cannot be established:

**INCLUDED = NOT ESTABLISHED**

---

## 31. CITED

CITED = OBSERVED when the system visibly attributes information to an identifiable source.

Citation does not establish retrieval, mention, inclusion, recommendation, factual support, or causal influence.

---

## 32. RECOMMENDED

RECOMMENDED = OBSERVED when the response explicitly favors selecting the Target Entity for the Represented Need or a stated condition.

List order alone does not establish Recommendation.

Positive description alone does not establish Recommendation.

Recommendation scope SHOULD be classified as UNCONDITIONAL, CONDITIONAL, or COMPARATIVE.

---

## 33. ADVERSELY_TREATED

ADVERSELY_TREATED = OBSERVED when the response negatively characterizes the Target Entity in a decision-relevant way or steers the user away from selecting it.

---

## 34. Mandatory Adverse-State Reporting

Whenever INCLUDED or RECOMMENDED is reported, ADVERSELY_TREATED MUST also be classified.

Its counts MUST appear at Equal Prominence with the corresponding positive metric.

---

## 35. Observation-State Independence

Observation States MUST be independently classified.

One state MUST NOT automatically establish another.

---

## 36. Entity Ambiguity and Classification Symmetry

Entity-resolution criteria MUST apply symmetrically to Target and Comparison Entities.

NOT ESTABLISHED MUST NOT be used where the state is reasonably determinable merely to manipulate a denominator.

---

## 37. Claim Validation

Decision-Material Claims associated with INCLUDED, RECOMMENDED, or ADVERSELY_TREATED results MUST be identified.

Where authoritative evidence is reasonably available, they MUST be classified as VERIFIED, INACCURATE, MATERIALLY_MISLEADING, or UNVERIFIED.

NO_CLAIM_EVALUATED MAY be used only when no Decision-Material Claim in the relevant scope requires evaluation.

---

## 38. Validation Outcome Distribution

Published decision metrics MUST show the associated Claim Validation distribution at Equal Prominence.

If one or more Decision-Material Claims remain UNVERIFIED:

**UNVERIFIED DECISION-MATERIAL CLAIMS PRESENT**

MUST appear with the result.

If no Decision-Material Claims were validated:

**DECISION-MATERIAL CLAIMS NOT VALIDATED**

MUST appear at Equal Prominence.

A statement that validation was performed is insufficient without its outcome distribution.

---

## 39. Conflicting Sources

Credible source conflicts MUST be disclosed.

An analyst MUST NOT silently select whichever source favors the desired outcome.

Where no controlling Source of Record can be established, UNVERIFIED may be appropriate.

---

## 40. List-Order Ambiguity

List position does not independently establish recommendation, preference, rank, or expected selection.

---

## 41. Repeated Executions

For every Observation State, repeated testing MUST retain valid Executions, OBSERVED, NOT OBSERVED, and NOT ESTABLISHED.

Repeated Executions measure repeated system behavior, not additional audience demand.

---

## 42. Prompt-Level Reduction

Permitted scalar reduction rules include ANY_OBSERVED, MAJORITY_OBSERVED, and ALL_OBSERVED.

The rule MUST be declared before Formal Measurement begins.

---

## 43. ANY_OBSERVED Restriction

ANY_OBSERVED MAY be used only with fixed execution counts, no Outcome-Dependent Stopping, and no Outcome-Dependent Continuation.

The corresponding execution-level result MUST appear at Equal Prominence.

---

## 44. Execution-Level Observation Rate

An execution-level rate MAY be calculated as:

**OBSERVED / Determinable Executions**

where:

**Determinable Executions = OBSERVED + NOT OBSERVED**

The Published Artifact MUST separately show OBSERVED, NOT OBSERVED, NOT ESTABLISHED, Valid Executions, and Determination Coverage.

---

## 45. Determination Coverage

Every Observation State rate derived from fewer than all valid Executions MUST report Determination Coverage.

Determination Coverage MUST appear at Equal Prominence with the rate.

### 45.1 Majority-Indeterminate Presentation Rule

When Determination Coverage is below 50%, the majority of valid Executions are indeterminate.

Under that condition:

- raw counts across all valid Executions MUST be the primary presentation;
- the determinable-execution percentage MUST NOT be used as the headline metric;
- the percentage MAY appear only as a secondary technical statistic.

The 50% threshold is a reporting-integrity boundary indicating that most observations are indeterminate.

It is not a claim of statistical sufficiency or scientific validity.

---

## 46. Prompt-Set Aggregation

A Prompt Set defines a Test environment.

It does not automatically represent the market.

Every Prompt Set metric MUST disclose Prompt count, Execution count, Prompt Class distribution, aggregation rule, Observation State, exclusions, and Determination Coverage where applicable.

**The denominator is the test, not the market.**

---

## 47. Percentage Reporting

Every percentage MUST directly accompany its raw numerator and denominator.

Percentages MUST NOT imply population precision, audience prevalence, or market prevalence without independent sampling evidence.

---

## 48. Composite Metric Restriction

Observation States MUST NOT be collapsed into a primary scalar that obscures their individual behavior.

A secondary composite MUST disclose components, formula, weights, and weighting rationale.

It MUST be labeled:

**COMPOSITE TEST INDEX**

---

## 49. Reporting Conformance

A Published Artifact presenting a Derived Metric MUST include:

- declared conformance level;
- Scope of Measurement;
- Prompt Domain;
- Prompt Provenance;
- Prompt Construction Mode;
- Prompt Selection Criterion;
- System Selection Scope;
- systems tested;
- relevant systems intentionally excluded;
- Observation State;
- raw numerator;
- raw denominator;
- aggregation rule;
- valid Execution count;
- NOT ESTABLISHED count;
- Determination Coverage where applicable;
- Prompt Class composition;
- observation period;
- per-system values;
- Classification Method;
- classifier audit results where applicable;
- Validation distribution where applicable;
- ADVERSELY_TREATED results where applicable;
- Observation States not classified;
- material context differences;
- material Manifest amendments;
- exclusion information;
- required prior-Test disclosures.

Interpretation-critical qualifiers MUST satisfy Equal Prominence.

---

## 50. Derivative Artifact Integrity

A person or organization claiming Full Conformance MUST NOT knowingly create, authorize, commission, or distribute an Authorized Derivative Artifact that strips away interpretation-critical qualifiers from a Derived Metric.

When an Authorized Derivative Artifact reproduces or summarizes a USO-governed metric, it MUST carry the qualifiers necessary to preserve the metric's evidentiary meaning.

If an Authorized Derivative Artifact omits required qualifiers, it MUST NOT:

- claim USO conformance;
- state or imply that the derivative claim is USO-conformant;
- display a USO conformance designation;
- cite USO as validating the derivative representation.

Independent third-party republication outside the control of the conformance claimant does not retroactively invalidate the underlying conformant Test.

---

## 51. Cross-System Aggregation

Per-system observations MUST remain visible.

Cross-system aggregates MUST disclose systems included, formula, weights, and weighting basis.

Equal weighting is analyst-selected.

It MUST NOT be represented as natural market weighting.

---

## 52. Comparison Universe Integrity

Formal comparisons MUST define the Comparison Universe and Comparison Selection Criterion before testing.

Where an independent external source can reasonably define the universe, that source SHOULD be used.

Otherwise:

**ANALYST-DEFINED COMPARISON UNIVERSE**

MUST be disclosed.

The artifact MUST show universe definition, source or basis, total qualifying entities identified, entities tested, qualifying entities excluded, and reasons for exclusion.

---

## 53. Outcome-Informed Comparison Selection

A Formal Comparison Universe or Comparison Set MUST NOT be selected, narrowed, geographically bounded, categorically bounded, or otherwise defined according to previously observed AI-search performance.

Prior performance MAY generate a separate research hypothesis.

It MUST NOT determine Formal Comparison membership.

---

## 54. Comparison Claims

Leadership claims MUST remain bounded to the tested Comparison Set.

Preferred:

> Highest recommendation rate among the five predeclared tested entities.

Unsupported without broader evidence:

> Leading provider in AI search.

---

## 55. Comparative Fairness

Formal comparisons MUST apply materially equivalent Prompts, Prompt Classes, execution counts, systems, context, classification rules, and validation rules.

---

## 56. Prior-Test Disclosure

Published Derived Metrics MUST disclose materially comparable Tests in the same Test Family conducted by the same analyst or organization within the preceding 180 days.

This includes relevant Exploratory Tests.

The Test Family MUST NOT be artificially fragmented to avoid this requirement.

---

## 57. Baseline and Longitudinal Comparison

Baseline comparisons MUST disclose material differences in systems, models, Prompt Sets, Prompt Classes, execution counts, context, Classification Method, and aggregation.

Material differences require:

**NON-EQUIVALENT TEST CONDITIONS**

at Equal Prominence.

---

## 58. Intervention-Causality Boundary

Temporal sequence does not establish intervention causality.

This rule applies to the Published Artifact as a whole, including title, subtitle, executive summary, filename, chart title, captions, annotations, callouts, case-study name, conclusion, and surrounding narrative.

A report MUST NOT produce a materially causal interpretation through framing while avoiding explicit causal verbs.

---

## 59. Change Metrics

Changes between periods MAY be reported when underlying conditions are disclosed.

Materially non-equivalent Tests MUST NOT be represented as like-for-like improvement.

---

## 60. Negative Evidence

Failure to observe a state in a bounded Test does not establish universal absence.

---

## 61. Temporal Boundary

Every Execution Observation is time-bound to system, context, and observation period.

It does not guarantee persistence.

---

## 62. Business Outcome Boundary

AI-search evidence and business-outcome evidence are separate evidence classes.

Causal relationships MUST NOT be asserted without sufficient causal evidence.

---

## 63. Prohibited Inferences

A conforming analysis MUST NOT infer without independent supporting evidence:

- audience demand from analyst-created Prompts;
- representative market behavior from ENTITY_INFORMED Prompt construction;
- market share from Prompt Set visibility;
- category visibility from branded Prompts alone;
- representative Prompt performance from outcome-informed selection;
- universal AI behavior from partial System Selection Scope;
- broad geographic performance from a narrower geographic Test;
- cross-locale behavior from single-locale testing;
- comparative leadership from outcome-informed Comparison selection;
- consumer preference from Recommendation frequency;
- traffic from Citation frequency;
- conversion from Mentions;
- revenue from Inclusion;
- source causality from Citation;
- Retrieval from Citation;
- Recommendation from list order;
- platform-wide behavior from limited Executions;
- demand from repeated Executions;
- absence where NOT ESTABLISHED is required;
- NOT ESTABLISHED where a state is reasonably determinable merely to manipulate a denominator;
- market weighting from arbitrary system weighting;
- category leadership from a selected Comparison Set;
- intervention causality from temporal sequence;
- intervention causality through presentation framing;
- like-for-like improvement from materially non-equivalent Tests.

---

## 64. Formal Measurement Integrity Declaration

Every Full-Conformance Formal Measurement report MUST contain a statement equivalent to:

> This report includes all valid executions defined by the declared Test Manifest. Execution counts and aggregation rules were established before formal testing and were not changed based on observed outcomes. Formal Prompts and Comparison Entities were not selected according to favorable prior performance. Prompt construction, system scope, material exclusions, exploratory precursor Tests, Manifest amendments, validation results, Determination Coverage, and non-equivalent conditions are disclosed within this artifact where applicable. Authorized derivative reporting produced by the conformance claimant must preserve interpretation-critical qualifiers.

If this statement is not true, Full Conformance MUST NOT be claimed.

---

## 65. Conformance Levels

### 65.1 FULL CONFORMANCE

All applicable mandatory requirements are satisfied.

### 65.2 PARTIAL IMPLEMENTATION

One or more mandatory requirements are not satisfied.

The unmet requirements MUST be identified.

A Partial Implementation MUST NOT use layout, branding, wording, or proximity to imply Full Conformance.

### 65.3 EXPLORATORY USE

The protocol is used investigatively without satisfying Formal Measurement requirements.

The term **USO Certified** MUST NOT be used under this candidate specification.

---

## 66. Adversarial Review Requirement

Before v1.0, successful material exploits MUST be treated as candidate-specification defects.

Reviewers SHOULD attempt to construct outputs that are simultaneously materially misleading, commercially advantageous, mathematically correct, and technically conforming.

A proposed exploit SHOULD NOT produce a new rule if it already violates an existing mandatory requirement.

---

## 67. Materiality Adjudication

The Specification Owner MUST NOT be the sole adjudicator of exploit materiality for v1.0 promotion.

At least one independent reviewer with no authorship role MUST participate.

---

## 68. Classification Reliability Testing

Before v1.0, independent evaluators SHOULD classify the same reference evidence.

Agreement and disagreement SHOULD be measured.

Particular attention SHOULD be given to MENTIONED versus INCLUDED, INCLUDED versus RECOMMENDED, Represented Need interpretation, conditional Recommendation, ADVERSELY_TREATED, entity ambiguity, and MATERIALLY_MISLEADING.

---

## 69. Gold Test Set

The reference set SHOULD include cases covering citation without mention, mention without inclusion, weak mention versus genuine inclusion, Represented Need ambiguity, inclusion without recommendation, conditional recommendation, adverse treatment, inaccurate recommendation, materially misleading recommendation, unsupported citation, unknown retrieval, entity ambiguity, list-order ambiguity, high NOT ESTABLISHED rates, low Determination Coverage, outcome-dependent stopping, outcome-informed Prompt selection, ENTITY_INFORMED Prompt construction, outcome-informed Comparison selection, System Selection Scope overclaiming, geographic-scope overclaiming, Test Registry suppression, context asymmetry, intervention-causality framing, classifier disagreement, audit-sampling manipulation, exclusion manipulation, and derivative-artifact qualifier stripping.

---

## 70. Independent Implementation Testing

Before v1.0, at least two independent implementations SHOULD process the same reference evidence.

Material output differences SHOULD be investigated.

---

## 71. Reporting Integrity Core

A compact USO Reporting Integrity Core MUST be maintained separately from the Full Evidence Protocol before v1.0.

The Core is intended to make the most important reporting controls practically adoptable without reproducing the full implementation specification.

Core Conformance MUST NOT be represented as Full Protocol Conformance.

---

## 72. Normative Freeze

v0.9.5 establishes the normative freeze candidate.

Following this version, additional normative prose SHOULD be limited to demonstrated material defects, internal contradictions, requirements discovered during schema implementation, and requirements discovered during independent empirical testing.

New hypothetical edge cases SHOULD ordinarily be addressed first through Gold Test Set cases, schema validation, conformance tests, reference implementation, and independent classification testing.

---

## 73. Open Work Before v1.0

Remaining work includes:

- machine-readable Evidence Schema;
- Test Manifest Schema;
- Test Registry Schema;
- finalized Reporting Integrity Core;
- Gold Test Set;
- reference validator;
- reference implementation;
- independent classification testing;
- independent implementation testing;
- empirical inter-rater agreement analysis;
- uncertainty-reporting guidance;
- governance beyond candidate ownership.

These are validation and implementation requirements, not invitations for continued speculative prose expansion.

---

## 74. Promotion Criteria for v1.0

Promotion requires, at minimum:

1. disposition of known material adversarial exploits;
2. machine-readable Evidence Schema;
3. machine-readable Test Manifest Schema;
4. machine-readable Test Registry Schema;
5. finalized Reporting Integrity Core;
6. Gold Test Set;
7. independent classification testing;
8. independent implementation testing;
9. documented aggregation behavior;
10. documented reporting-conformance behavior;
11. independent materiality review;
12. no known unresolved exploit permitting a materially misleading report to claim Full Conformance.

---

## 75. Terminology and Provenance

The phrase **Universal Search Optimization** has historical uses predating this specification.

This protocol does not claim authorship of the historical phrase.

**USO Evidence Protocol** refers specifically to the evidence architecture, Observation State taxonomy, Claim Validation rules, uncertainty handling, Scope of Measurement controls, Prompt-construction controls, execution controls, Determination Coverage requirements, aggregation rules, presentation-integrity controls, comparative-fairness rules, derivative-reporting requirements, causal boundaries, conformance requirements, and governance model defined in this specification family.

---

## 76. Candidate Status

USO Evidence Protocol v0.9.5 is the **Final Candidate Specification** prior to implementation and empirical validation.

It is intended for schema implementation, Gold Test Set construction, independent classification testing, independent implementation, adversarial conformance testing, and methodological review.

It MUST NOT be represented as an established industry standard or scientifically proven methodology.

---

# Annex A: Full-Conformance Checklist

A Formal Measurement claiming Full Conformance MUST satisfy every applicable item below.

## Test Definition

1. Test entered into Test Registry before first valid Execution.
2. Pre-execution Test Manifest exists.
3. Test Family identified.
4. Scope of Measurement declared.
5. Prompt Domain declared.
6. Geographic scope declared where applicable.
7. Language and locale declared.
8. System Selection Scope declared.
9. Systems tested disclosed.
10. Material system exclusions disclosed.

## Prompt Integrity

11. Exact Prompt Set retained.
12. Prompt Provenance recorded.
13. Prompt Construction Mode recorded.
14. Prompt Selection Criterion predeclared.
15. Outcome-Informed Prompt Selection prohibited.
16. Branded and non-branded Prompts classified separately.
17. Represented Need recorded before execution where INCLUDED or RECOMMENDED is evaluated.

## Execution Integrity

18. Planned execution counts predeclared.
19. Outcome-Dependent Stopping prohibited.
20. Outcome-Dependent Continuation prohibited.
21. All valid Executions retained.
22. Exclusion rules predeclared.
23. Excluded Execution records contain required fields.
24. Technical exclusions do not operate as outcome filters.
25. Excluded-execution distribution disclosed where recoverable.
26. Material execution context retained.

## Classification Integrity

27. Classification Method disclosed.
28. Automated classifier instructions retained.
29. Automated classifications audited where applicable.
30. Audit ledger closed before sample selection.
31. Audit selection is non-predictable at record-creation time.
32. Sampling method and seed retained where applicable.
33. Auditor independence recommendation addressed.
34. Disagreement rate disclosed.
35. Unresolved material disagreement labeled.

## Observation Integrity

36. OBSERVED, NOT OBSERVED, and NOT ESTABLISHED used consistently.
37. Observation States classified independently.
38. Entity-resolution criteria applied symmetrically.
39. INCLUDED classification uses the pre-recorded Represented Need.
40. ADVERSELY_TREATED classified where INCLUDED or RECOMMENDED is reported.

## Validation Integrity

41. Decision-Material Claims identified.
42. NO_CLAIM_EVALUATED used only when appropriate.
43. Claim Validation distribution disclosed.
44. Lack of validation explicitly disclosed.
45. UNVERIFIED Decision-Material Claims explicitly disclosed.
46. Credible source conflicts disclosed.

## Aggregation Integrity

47. Aggregation rule predeclared.
48. Prompt-level reduction rule disclosed.
49. Execution-level result retained.
50. ANY_OBSERVED accompanied by execution-level result.
51. Raw numerator and denominator disclosed.
52. NOT ESTABLISHED count disclosed.
53. Determination Coverage disclosed where applicable.
54. Majority-Indeterminate Presentation Rule followed.
55. Composite metrics remain secondary and fully decomposed.

## Comparison Integrity

56. Comparison Universe defined where applicable.
57. Comparison Selection Criterion declared.
58. Outcome-Informed Comparison Selection prohibited.
59. Total qualifying Comparison Entities disclosed where reasonably identifiable.
60. Excluded qualifying entities disclosed.
61. Comparison conditions materially equivalent or labeled non-equivalent.
62. Leadership claims bounded to the tested set.

## Reporting Integrity

63. Conformance level declared.
64. Prompt Provenance appears in the Published Artifact.
65. Prompt Construction Mode appears in the Published Artifact.
66. Prompt Selection Criterion appears in the Published Artifact.
67. Scope of Measurement appears with the first primary metric.
68. Required qualifiers satisfy Equal Prominence.
69. Per-system results remain visible.
70. Relevant adverse-treatment result remains visible.
71. Validation warnings remain visible.
72. Materially comparable prior Tests disclosed.
73. Causal framing restrictions apply to the entire artifact.
74. Partial Implementation does not imply Full Conformance.

## Derivative Integrity

75. Authorized Derivative Artifacts preserve interpretation-critical qualifiers.
76. Stripped derivative claims do not claim or imply USO conformance.
77. USO methodology is not cited as validating a materially decontextualized derivative metric.

## Evidence Access

78. Underlying evidence remains Accessible.
79. Required Test Registry information is available for conformance review.
80. Sufficient evidence is retained for independent audit.

Failure of any applicable mandatory item means:

**FULL CONFORMANCE MUST NOT BE CLAIMED.**

---

## Governing Principles

**Retrieval is not citation.**

**Citation is not mention.**

**Mention is not inclusion.**

**Inclusion is not recommendation.**

**Recommendation is not conversion.**

**Adverse treatment is not factual inaccuracy.**

**Observation is not causation.**

**Temporal sequence is not intervention causality.**

**Causal wording is not the only way to imply causality.**

**Not observed is not not established.**

**A high rate with low Determination Coverage is not broad evidence.**

**Repeated execution is not additional demand.**

**A branded Prompt is not category discovery.**

**An entity-informed Prompt is not neutral discovery evidence.**

**A Prompt Set is not the market.**

**A favorable subset is not a representative sample.**

**A selected Comparison Set is not the Comparison Universe.**

**A selected System Set is not all AI systems.**

**Single-locale evidence is not universal geographic evidence.**

**Retention is not disclosure.**

**Co-location is not Equal Prominence.**

**Classification performed is not validation established.**

**An aggregate is not its underlying evidence.**

**A composite is not a natural measure merely because it has a number.**

**Unequal conditions do not produce a like-for-like comparison.**

**A conformant source report does not make a misleading derivative artifact conformant.**

And above all:

# No conclusion may outrun its evidence.

The purpose of the protocol is not to prevent measurement.

It is to make unsupported measurement harder to construct, harder to conceal, easier to reproduce, easier to audit, and incompatible with a claim of Full Conformance.
