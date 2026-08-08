# Independent Materiality and Adversarial Review Protocol v0.1

## Objective

Attempt to construct a result that is simultaneously:

1. materially misleading to a reasonable reader;
2. commercially advantageous to the reporting party;
3. mathematically or factually presented as valid;
4. technically conformant with all applicable USO v0.9.5 mandatory requirements.

If such an artifact exists, the enabling requirement is a candidate-specification defect unless explicitly accepted as residual risk.

## Reviewer Independence

The reviewer SHOULD:

- have no authorship role in v0.9.5;
- not receive prior adversarial-review reports before completing the first pass;
- not be coached toward known exploit classes;
- disclose material conflicts of interest.

## Materials

Provide:

- `SPECIFICATION.md`
- `REPORTING-INTEGRITY-CORE.md`
- `/schema`
- `/examples`
- `tools/uso_validator.py`

Do not provide prior exploit reports in the first pass.

## Attack Surfaces

The reviewer is free to attack any surface, including:

- Prompt construction;
- Prompt selection;
- system selection;
- Comparison Universe;
- execution counts;
- exclusions;
- NOT ESTABLISHED;
- Determination Coverage;
- automated classification;
- audit sampling;
- Claim Validation;
- aggregation;
- Equal Prominence;
- causal framing;
- derivative artifacts;
- Test Family construction;
- Test Registry disclosure;
- partial implementation claims.

This list is not exhaustive.

## Required Finding Format

For each proposed exploit record:

- exploit identifier;
- commercial or interpretive goal;
- exact steps;
- clauses relied upon;
- why the artifact remains technically conformant;
- why the result is materially misleading;
- minimal corrective change, if any.

## Adjudication

Do not patch an exploit merely because it is imaginative.

First determine whether it already violates an existing MUST or MUST NOT.

Classify findings as:

- VALID MATERIAL DEFECT;
- VALID NON-MATERIAL DEFECT;
- ALREADY NON-CONFORMING;
- IMPLEMENTATION DEFECT;
- DOCUMENTATION AMBIGUITY;
- NOT REPRODUCIBLE.

The Specification Owner MUST NOT be the sole final adjudicator of materiality for v1.0 promotion.
