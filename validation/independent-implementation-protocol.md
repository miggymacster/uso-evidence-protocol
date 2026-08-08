# Independent Implementation Protocol v0.1

## Objective

Determine whether an implementer who did not build the reference implementation can create a compatible USO v0.9.5 implementation from the public specification and schemas.

## Independence

The implementer MUST NOT use `tools/uso_validator.py` as implementation source code before submitting their first implementation result.

They MAY use:

- `SPECIFICATION.md`
- `REPORTING-INTEGRITY-CORE.md`
- files under `/schema`
- public examples under `/examples`

For a stricter test, withhold `/examples/full-conformant-test` until the first implementation attempt is complete.

## Required Implementation

The independent implementation should be able to:

1. read a Test Manifest;
2. read Test Registry entries;
3. read Execution Evidence;
4. calculate execution-level Observation State counts;
5. calculate Determination Coverage;
6. calculate declared Prompt-level reductions;
7. detect missing expected Executions;
8. detect undeclared Prompts and systems;
9. detect Manifest/Evidence drift;
10. detect invalid exclusions;
11. reconcile report counts;
12. emit machine-readable conformance errors or warnings.

## Test Inputs

Use:

- `examples/full-conformant-test/`
- `tests/conformance/`
- a copy of the Gold Test Set where relevant.

## Required Comparison

After the independent implementation is frozen, compare it against the reference validator.

Record:

- identical pass/fail decisions;
- divergent pass/fail decisions;
- divergent metric calculations;
- divergent interpretation of schema fields;
- cases where one implementation requires manual review.

Any material divergence MUST be investigated rather than averaged away.

## Success Evidence

A credible implementation result requires:

- source code or executable artifact;
- version identifier;
- documented runtime/dependencies;
- results on the conformance suite;
- differences from the reference implementation;
- implementer statement that the first implementation was produced independently.

One independent implementation is the minimum v0.9.5 promotion criterion. Two are preferred.
