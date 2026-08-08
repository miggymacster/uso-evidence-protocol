# Changelog

## Post-release publication metadata

Date: 2026-08-08

The following publication and repository actions were completed after the USO Evidence Protocol v0.9.5 candidate package was released. These actions update the live repository and publication record. They do not modify the frozen normative v0.9.5 tagged release.

- Published the canonical public repository at https://github.com/miggymacster/uso-evidence-protocol.
- Published the tagged `v0.9.5` GitHub release.
- Archived the human-readable Final Candidate Specification on Zenodo.
- Assigned persistent DOI: https://doi.org/10.5281/zenodo.21852690.
- Added the DOI and canonical repository information to live repository metadata.
- Updated `README.md` to reflect completed public release and archival publication.
- Updated `CITATION.cff` with current citation metadata and DOI.
- Updated the live `SPECIFICATION.md` metadata with the canonical repository, persistent identifier, and public issue-review channel.
- Updated `validation/VALIDATION-STATUS.md` to distinguish completed publication milestones from pending independent validation.
- Updated `PUBLICATION-CHECKLIST.md` to record completion of the public-release and archival-publication phase.

Independent human classification, independent implementation, independent materiality/adversarial review, empirical inter-rater analysis, and v1.0 promotion evaluation remain pending.

No normative requirement in the frozen `v0.9.5` tagged release was changed by these post-release publication and metadata updates.

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
