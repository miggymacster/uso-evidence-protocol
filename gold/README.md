# USO Gold Test Set v0.1

This directory contains the candidate human-classification reference set for USO Evidence Protocol v0.9.5.

## Files

- `uso-gold-test-set-v0.1.json` — participant-facing blind test set
- `uso-gold-answer-key-v0.1.json` — canonical candidate answer key; keep separate from participants

## Design

The set contains 50 cases:

- 40 execution-classification cases
- 10 reporting-integrity cases

The cases target the highest-risk boundaries identified during specification hardening, including MENTIONED vs INCLUDED, INCLUDED vs RECOMMENDED, Represented Need, entity ambiguity, claim validation, adverse treatment, retrieval uncertainty, Determination Coverage, prompt construction, comparison selection, causality, derivative reporting, audit sampling, system scope, and exclusions.

The answer key is a candidate reference, not empirical proof. It must itself be evaluated through independent classification testing.
