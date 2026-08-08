#!/usr/bin/env python3
from __future__ import annotations
import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
FULL = ROOT / "examples" / "full-conformant-test"
SCHEMAS = ROOT / "schema"

spec = importlib.util.spec_from_file_location("uso_validator", TOOLS / "uso_validator.py")
uv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(uv)

schemas = {
    "manifest": uv.load_json(SCHEMAS / "uso-test-manifest.schema.json"),
    "registry": uv.load_json(SCHEMAS / "uso-test-registry.schema.json"),
    "evidence": uv.load_json(SCHEMAS / "uso-evidence.schema.json"),
    "report": uv.load_json(SCHEMAS / "uso-report.schema.json"),
}

base = {
    "manifest": uv.load_json(FULL / "uso-test-manifest.json"),
    "registry": uv.load_json(FULL / "uso-test-registry.json"),
    "evidence": uv.load_json(FULL / "uso-evidence.json"),
    "report": uv.load_json(FULL / "uso-report.json"),
}

tests = []

def add(name, expected, mutate):
    bundle = copy.deepcopy(base)
    mutate(bundle)
    tests.append((name, expected, bundle))

add("valid_reference_bundle", "PASS", lambda b: None)

add("wrong_report_execution_count", "FAIL",
    lambda b: b["report"]["observation_metrics"][0]["execution_level"].__setitem__("observed", 3))

add("represented_need_drift", "FAIL",
    lambda b: b["evidence"]["evidence_records"][0]["prompt"].__setitem__("represented_need", "A different need"))

add("undeclared_system", "FAIL",
    lambda b: b["evidence"]["evidence_records"][0]["system_context"].__setitem__("system_name", "Undeclared System"))

def extra_exec(b):
    r = copy.deepcopy(b["evidence"]["evidence_records"][0])
    r["execution_id"] = "EXEC-004"
    r["executed_at"] = "2026-08-08T12:40:00Z"
    b["evidence"]["evidence_records"].append(r)
    b["report"]["scope_of_measurement"]["valid_execution_count"] = 4
    b["report"]["exclusions_summary"]["total_attempted_executions"] = 4
add("extra_valid_execution_beyond_manifest", "FAIL", extra_exec)

def missing_adverse(b):
    b["report"]["observation_metrics"] = [
        m for m in b["report"]["observation_metrics"]
        if m["observation_state"] != "ADVERSELY_TREATED"
    ]
    b["report"]["adverse_treatment_summary"] = None
add("recommendation_without_adverse_metric", "FAIL", missing_adverse)

def wrong_period(b):
    b["report"]["scope_of_measurement"]["observation_period_start"] = "2026-08-08T12:00:00Z"
add("wrong_observation_period", "FAIL", wrong_period)

def retroactive_exclusion(b):
    r = b["evidence"]["evidence_records"][0]
    r["exclusion"] = {
        "excluded": True,
        "reason": "Post-hoc low quality",
        "rule_id": "EX-NEW",
        "rule_preexisted_execution": False,
        "technical_failure": False
    }
add("retroactive_exclusion_rule", "FAIL", retroactive_exclusion)

def registry_inaccessible(b):
    b["registry"]["public_registry_access"]["accessible"] = False
    b["registry"]["public_registry_access"]["location"] = None
add("full_conformance_registry_inaccessible", "FAIL", registry_inaccessible)

def prompt_class_drift(b):
    b["evidence"]["evidence_records"][0]["prompt"]["prompt_class"] = ["BRANDED", "PURCHASE_CONSIDERATION"]
add("prompt_class_drift", "FAIL", prompt_class_drift)

def metric_rate_wrong(b):
    b["report"]["observation_metrics"][1]["execution_level"]["rate_among_determinable"] = 0.9
add("incorrect_execution_rate", "FAIL", metric_rate_wrong)

def unverified_without_warning(b):
    claim = {
        "claim_id": "C-UNV",
        "claim_text": "Unverified material claim",
        "decision_material": True,
        "validation_state": "UNVERIFIED",
        "source_of_record": None,
        "validation_notes": "No authoritative confirmation.",
        "conflicting_sources": []
    }
    b["evidence"]["evidence_records"][1]["claim_validation"] = {
        "status": "CLAIMS_EVALUATED", "claims": [claim], "notes": None
    }
    b["report"]["validation_summary"] = {
        "decision_material_claims_total": 2,
        "claim_outcomes": {
            "verified": 1, "inaccurate": 0, "materially_misleading": 0, "unverified": 1
        },
        "executions_no_claim_evaluated": 1,
        "warning_labels": []
    }
add("unverified_claim_without_warning", "FAIL", unverified_without_warning)

failures = []
rows = []
for name, expected, bundle in tests:
    result = uv.validate_bundle(
        bundle["manifest"], bundle["registry"], bundle["evidence"], bundle["report"], schemas
    ).as_dict()
    actual = result["status"]
    ok = actual == expected
    rows.append({
        "name": name,
        "expected": expected,
        "actual": actual,
        "ok": ok,
        "error_count": result["errors"],
        "warning_count": result["warnings"],
        "codes": [x["code"] for x in result["issues"]],
    })
    if not ok:
        failures.append(name)

print(json.dumps({"tests": rows, "failed_expectations": failures}, indent=2))
raise SystemExit(1 if failures else 0)
