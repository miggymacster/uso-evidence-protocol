# USO Evidence Protocol

This repository contains the public candidate release package for the USO Evidence Protocol.

**Current version:** USO Evidence Protocol v0.9.5  
**Status:** Final Candidate Specification  
**DOI:** https://doi.org/10.5281/zenodo.21852690  
**Tagged release:** https://github.com/miggymacster/uso-evidence-protocol/releases/tag/v0.9.5

## Current public artifacts

- **USO Evidence Protocol v0.9.5** — Final Candidate Specification
- **USO Reporting Integrity Core v0.2** — Practical minimum reporting standard
- **USO Evidence Schema v0.1** — Machine-readable execution evidence
- **USO Test Manifest Schema v0.1** — Machine-readable pre-execution test design
- **USO Test Registry Schema v0.1** — Machine-readable chronological test registry
- **USO Report Schema v0.1** — Machine-readable calculated reporting output
- **USO Gold Test Set v0.1** — 50-case candidate human/reference test set
- **USO Reference Validator v0.1** — Schema plus cross-record conformance validator
- **Initial Conformance Suite** — Known-pass/known-fail implementation tests
- **Independent Validation Protocols** — Classification, implementation, and materiality-review procedures

## Status

The protocol is a **Final Candidate Specification** undergoing independent validation prior to v1.0.

Version 0.9.5 has been publicly released, archived, and assigned the persistent identifier:

**DOI:** https://doi.org/10.5281/zenodo.21852690

The package demonstrates machine-readable implementation, a working synthetic end-to-end example, a reference validator, and an initial conformance suite.

It does **not** yet demonstrate independent reproducibility, independent implementation compatibility, industry adoption, scientific validation, or v1.0 readiness.

It MUST NOT be represented as an established industry standard or scientifically proven methodology.

## Governing principle

**No conclusion may outrun its evidence.**

## Repository structure

```text
/SPECIFICATION.md
/REPORTING-INTEGRITY-CORE.md
/README.md
/CHANGELOG.md
/CITATION.cff
/LICENSE
/PUBLICATION-CHECKLIST.md
/RELEASE-MANIFEST.json
/SHA256SUMS.txt

/schema/
    uso-evidence.schema.json
    uso-test-manifest.schema.json
    uso-test-registry.schema.json
    uso-report.schema.json
    uso-gold-response.schema.json

/examples/
    uso-evidence.example.json
    uso-test-manifest.example.json
    uso-test-registry.example.json
    uso-report.example.json
    /full-conformant-test/
        uso-test-manifest.json
        uso-test-registry.json
        uso-evidence.json
        uso-report.json

/gold/
    README.md
    uso-gold-test-set-v0.1.json
    uso-gold-answer-key-v0.1.json
    uso-participant-response.template.json

/tools/
    README.md
    requirements.txt
    uso_validator.py
    score_gold_results.py

/tests/conformance/
    run_conformance_tests.py
    latest-results.json

/validation/
    VALIDATION-STATUS.md
    independent-classification-protocol.md
    independent-implementation-protocol.md
    independent-materiality-review-protocol.md

/.github/ISSUE_TEMPLATE/
    specification-defect.md
    adversarial-exploit.md
    classification-disagreement.md
    implementation-ambiguity.md
```

## Quick validation

Install the Python dependency:

```bash
pip install -r tools/requirements.txt
```

Run the full synthetic reference bundle:

```bash
python tools/uso_validator.py \
  --manifest examples/full-conformant-test/uso-test-manifest.json \
  --registry examples/full-conformant-test/uso-test-registry.json \
  --evidence examples/full-conformant-test/uso-evidence.json \
  --report examples/full-conformant-test/uso-report.json
```

Run the software conformance suite:

```bash
python tests/conformance/run_conformance_tests.py
```

## External validation still required

- independent human classification study;
- independent implementation;
- independent materiality/adversarial review;
- empirical inter-rater analysis.

See `validation/VALIDATION-STATUS.md`.

## Archival publication

The human-readable normative publication of USO Evidence Protocol v0.9.5 is archived on Zenodo:

**MacFarland, A. L. (2026). _USO Evidence Protocol v0.9.5: Final Candidate Specification for AI Search Observation, Validation, Aggregation, Reporting Integrity, and Evidence Governance._ Zenodo.**

https://doi.org/10.5281/zenodo.21852690

The canonical supporting implementation and validation artifacts remain in this repository and the tagged v0.9.5 GitHub release.

## Candidate answer-key warning

`gold/uso-gold-answer-key-v0.1.json` must not be given to blind-study participants before classification is complete.
