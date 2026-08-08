# Changelog

## USO Evidence Protocol v0.9.5

Status: Final Candidate Specification.

Key changes from v0.9.4:

- Added Scope of Measurement.
- Added System Selection Scope.
- Added Prompt Construction Mode: ENTITY_INDEPENDENT / ENTITY_INFORMED.
- Made Represented Need pre-recording mandatory where INCLUDED or RECOMMENDED is classified.
- Restored auditor-independence guidance.
- Added post-ledger, non-predictable audit-sampling integrity.
- Restored full exclusion-record requirements and outcome-filter prohibition.
- Restored validation warnings for unvalidated Decision-Material Claims.
- Added Authorized Derivative Artifact integrity.
- Added Test Family anti-fragmentation rule.
- Added Majority-Indeterminate Presentation Rule for Determination Coverage below 50%.
- Restored Full-Conformance Checklist as Annex A.
- Established normative freeze candidate.

## USO Reporting Integrity Core v0.2

- Reconciled the Core with USO Evidence Protocol v0.9.5.
- Added Scope of Measurement and System Selection Scope.
- Added Prompt Provenance and Prompt Construction Mode.
- Added mandatory pre-recorded Represented Need.
- Added Majority-Indeterminate Presentation Rule.
- Strengthened validation and exclusion disclosure.
- Added Comparison Universe integrity.
- Added derivative-artifact qualifier inheritance.
- Added Core-to-Protocol mapping.

## USO Evidence Schema v0.1

- Initial machine-readable execution-evidence schema.
- Validated against JSON Schema Draft 2020-12.
- Includes Observation States, Prompt evidence, system context, classification, claim validation, citations, entity resolution, and exclusion integrity.


## USO Test Manifest Schema v0.1

- Initial machine-readable pre-execution Test Manifest schema.
- Encodes Scope of Measurement, Prompt construction, Represented Need, system selection, execution design, classification, validation, exclusion, aggregation, and comparison controls.
- Rejects Formal Measurement manifests that permit outcome-dependent stopping.
- Requires Represented Need where INCLUDED or RECOMMENDED will be classified.
- Requires ADVERSELY_TREATED in the classification plan when INCLUDED or RECOMMENDED is evaluated.

## USO Test Registry Schema v0.1

- Initial machine-readable chronological Test Registry schema.
- Supports exploratory and formal Tests and required dispositions.
- Preserves Test Family, target entity, registration/start/completion timestamps, artifact references, prior-test disclosure status, and invalid/superseded/abandoned dispositions.
- Requires public registry access metadata when public Full Conformance is claimed.


## USO Report Schema v0.1

- Added machine-readable output for calculated Observation State metrics.
- Encodes execution-level counts, Determination Coverage, Prompt-level reduction output, scope, validation, adverse treatment, exclusions, comparison status, causal status, and derivative requirements.
- Separates claim-level validation outcomes from execution-level `NO_CLAIM_EVALUATED` status to avoid mixed denominators.

## USO Gold Test Set v0.1

- Added 50 candidate reference cases.
- Includes 40 execution-classification cases and 10 reporting-integrity cases.
- Keeps the candidate answer key separate from participant materials.
- Added participant response schema and response template.

## USO Reference Validator v0.1

- Added JSON Schema validation plus cross-record reconciliation.
- Checks Manifest/Evidence drift, undeclared Prompts and systems, valid execution counts, context parity, report metric reconciliation, Determination Coverage, adverse reporting, validation warnings, exclusion counts, and registry accessibility.
- Added initial known-pass/known-fail conformance suite.

## Independent Validation Kit v0.1

- Added independent classification protocol.
- Added independent implementation protocol.
- Added independent materiality/adversarial review protocol.
- Added explicit validation-status boundary.
