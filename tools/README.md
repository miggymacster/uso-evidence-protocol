# USO Reference Tools

## Reference validator

```bash
python uso_validator.py   --manifest ../examples/full-conformant-test/uso-test-manifest.json   --registry ../examples/full-conformant-test/uso-test-registry.json   --evidence ../examples/full-conformant-test/uso-evidence.json   --report ../examples/full-conformant-test/uso-report.json
```

The validator performs JSON Schema validation plus cross-record reconciliation.

It is a candidate reference implementation, not an independent implementation.

## Gold Test scoring

`score_gold_results.py` compares completed participant response files with the candidate key and reports pairwise raw agreement between raters.

Raw agreement should remain visible even if later studies add a chance-corrected coefficient.
