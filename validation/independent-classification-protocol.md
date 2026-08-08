# Independent Classification Validation Protocol v0.1

## Objective

Test whether independent evaluators can apply USO Evidence Protocol v0.9.5 consistently without coaching from the specification author.

This is an empirical reproducibility exercise. It is not a popularity survey and it does not establish industry adoption.

## Participants

Use at least 3 independent evaluators. Five is preferred.

Participants SHOULD:

- have sufficient experience to understand AI-generated search or answer outputs;
- have had no authorship role in USO v0.9.5;
- not receive the Gold Test answer key before completing classification;
- not receive prior adversarial-review findings before classification.

Record participant background only at a coarse professional level. Do not collect unnecessary personal information.

## Materials Given to Participants

Provide only:

1. `SPECIFICATION.md`
2. `REPORTING-INTEGRITY-CORE.md`
3. `gold/uso-gold-test-set-v0.1.json`
4. `gold/uso-participant-response.template.json`
5. `schema/uso-gold-response.schema.json`

Do NOT provide:

- `gold/uso-gold-answer-key-v0.1.json`
- prior adversarial reviews;
- the author's classification rationale;
- another participant's answers.

## Procedure

1. Assign an anonymous participant identifier.
2. Give the participant the materials above.
3. Permit normal reading of the public specification, but no author coaching on individual cases.
4. Require one completed response for all 50 cases.
5. Record the completion timestamp.
6. Lock the response file after submission.
7. Only after all participants finish, compare results with each other and with the candidate answer key.

## Primary Measurements

Report separately:

- exact raw agreement for each Observation State;
- exact raw agreement for recommendation scope;
- exact raw agreement for adverse subtype;
- exact raw agreement for Claim Validation;
- exact raw agreement for reporting-integrity judgments;
- disagreement counts by Gold Test case;
- disagreement counts by conceptual boundary.

Do not collapse all dimensions immediately into one universal score.

Where a chance-corrected agreement coefficient is used, identify the coefficient and its assumptions. Raw agreement MUST remain visible.

## Boundary Analysis

At minimum, separately inspect disagreement on:

- MENTIONED vs INCLUDED;
- INCLUDED vs RECOMMENDED;
- Represented Need;
- ADVERSELY_TREATED;
- entity ambiguity;
- NOT ESTABLISHED;
- Claim Validation;
- conditional Recommendation;
- reporting-integrity cases.

## Candidate-Key Review

The answer key is itself a candidate artifact.

If multiple independent participants disagree with the candidate key on the same case, the case MUST be reviewed for:

- defective wording;
- insufficient evidence;
- an ambiguous protocol definition;
- an incorrect candidate answer.

Do not automatically treat participant disagreement as participant error.

## Change Control

If validation reveals a material specification defect, record:

- affected case;
- participant disagreement;
- affected clause;
- proposed disposition.

Normative prose remains frozen unless the defect meets v0.9.5 §72's correction criteria.

## Output

Publish or retain:

- anonymized participant response files;
- aggregate agreement results;
- case-level disagreement table;
- any specification defects discovered;
- final disposition of disputed Gold Test cases.

The study MUST NOT be described as successful independent validation until independent participants have actually completed it.
