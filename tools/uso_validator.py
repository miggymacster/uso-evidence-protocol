#!/usr/bin/env python3
"""
USO Reference Validator v0.1

Validates:
- uso-test-manifest.schema.json
- uso-test-registry.schema.json
- uso-evidence.schema.json
- uso-report.schema.json

and performs cross-record conformance checks that JSON Schema alone cannot express.

Target:
- USO Evidence Protocol v0.9.5
- USO Reporting Integrity Core v0.2
"""

from __future__ import annotations
import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import jsonschema
from jsonschema.validators import validator_for


def parse_dt(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def close(a, b, tol=1e-9):
    if a is None or b is None:
        return a is b
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


class Result:
    def __init__(self):
        self.issues = []

    def add(self, severity, code, message):
        self.issues.append({
            "severity": severity,
            "code": code,
            "message": message,
        })

    @property
    def failed(self):
        return any(i["severity"] == "ERROR" for i in self.issues)

    def as_dict(self):
        counts = Counter(i["severity"] for i in self.issues)
        return {
            "status": "FAIL" if self.failed else "PASS",
            "errors": counts.get("ERROR", 0),
            "warnings": counts.get("WARNING", 0),
            "issues": self.issues,
        }


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def schema_validate(instance, schema, label, result):
    try:
        cls = validator_for(schema)
        cls.check_schema(schema)
        cls(schema, format_checker=jsonschema.FormatChecker()).validate(instance)
    except jsonschema.ValidationError as e:
        result.add("ERROR", f"SCHEMA_{label.upper()}", f"{label}: {e.message}")
    except jsonschema.SchemaError as e:
        result.add("ERROR", f"SCHEMA_DEF_{label.upper()}", f"{label} schema invalid: {e.message}")


def state_counts(records, state_name):
    c = Counter()
    for r in records:
        value = r.get("observation_states", {}).get(state_name)
        if value is not None:
            c[value] += 1
    return {
        "OBSERVED": c.get("OBSERVED", 0),
        "NOT_OBSERVED": c.get("NOT_OBSERVED", 0),
        "NOT_ESTABLISHED": c.get("NOT_ESTABLISHED", 0),
    }


def prompt_level_any(records, state_name):
    by_prompt = defaultdict(list)
    for r in records:
        by_prompt[r["prompt"]["prompt_id"]].append(
            r.get("observation_states", {}).get(state_name)
        )
    observed_prompts = sum(
        any(v == "OBSERVED" for v in vals) for vals in by_prompt.values()
    )
    return observed_prompts, len(by_prompt)


def expected_prompt_class_counts(manifest):
    branded = 0
    nonbranded = 0
    for p in manifest["prompt_set"]:
        classes = set(p["prompt_class"])
        if "BRANDED" in classes:
            branded += 1
        if "NON_BRANDED" in classes:
            nonbranded += 1
    return branded, nonbranded


def validate_bundle(manifest, registry, evidence, report, schemas):
    result = Result()

    # Schema validation first.
    schema_validate(manifest, schemas["manifest"], "manifest", result)
    schema_validate(registry, schemas["registry"], "registry", result)
    schema_validate(evidence, schemas["evidence"], "evidence", result)
    schema_validate(report, schemas["report"], "report", result)
    if result.failed:
        return result

    # Identity/version alignment.
    for label, obj in [("manifest", manifest), ("registry", registry), ("evidence", evidence), ("report", report)]:
        if obj.get("protocol_version") != "0.9.5":
            result.add("ERROR", "PROTOCOL_VERSION", f"{label} does not target protocol 0.9.5.")

    ids = {
        "manifest": manifest["test_id"],
        "evidence": evidence["test_id"],
        "report": report["test_id"],
    }
    if len(set(ids.values())) != 1:
        result.add("ERROR", "TEST_ID_MISMATCH", f"Test IDs do not align: {ids}")

    fam = {
        "manifest": manifest["test_family_id"],
        "evidence": evidence.get("test_family_id"),
        "report": report["test_family_id"],
    }
    if len(set(fam.values())) != 1:
        result.add("ERROR", "TEST_FAMILY_MISMATCH", f"Test Family IDs do not align: {fam}")

    reg_entries = [t for t in registry["tests"] if t["test_id"] == manifest["test_id"]]
    if len(reg_entries) != 1:
        result.add("ERROR", "REGISTRY_ENTRY", "Registry must contain exactly one entry for the Test ID.")
        reg_entry = None
    else:
        reg_entry = reg_entries[0]

    # Chronology.
    first_allowed = parse_dt(manifest["first_valid_execution_must_not_precede"]) if manifest.get("first_valid_execution_must_not_precede") else None
    if reg_entry:
        if parse_dt(reg_entry["registered_at"]) > parse_dt(reg_entry["start_date"]):
            result.add("ERROR", "REGISTRATION_AFTER_START", "Registry registration occurs after the Test start date.")
        if parse_dt(manifest["created_at"]) > parse_dt(reg_entry["start_date"]):
            result.add("ERROR", "MANIFEST_AFTER_START", "Manifest was created after the Test start date.")

    records = evidence["evidence_records"]
    exec_ids = [r["execution_id"] for r in records]
    if len(exec_ids) != len(set(exec_ids)):
        result.add("ERROR", "DUPLICATE_EXECUTION_ID", "Execution IDs must be unique.")

    manifest_prompts = {p["prompt_id"]: p for p in manifest["prompt_set"]}
    manifest_systems = {s["system_name"]: s for s in manifest["systems"]}
    exclusion_rules = {x["rule_id"] for x in manifest["exclusion_rules"]}

    # Record-level reconciliation.
    for r in records:
        eid = r["execution_id"]
        pid = r["prompt"]["prompt_id"]
        sysname = r["system_context"]["system_name"]

        if pid not in manifest_prompts:
            result.add("ERROR", "UNDECLARED_PROMPT", f"{eid}: prompt {pid} not in Manifest.")
            continue
        mp = manifest_prompts[pid]

        if sysname not in manifest_systems:
            result.add("ERROR", "UNDECLARED_SYSTEM", f"{eid}: system {sysname} not in Manifest.")
            continue
        ms = manifest_systems[sysname]

        checks = [
            ("prompt_text", r["prompt"].get("prompt_text"), mp.get("prompt_text")),
            ("represented_need", r["prompt"].get("represented_need"), mp.get("represented_need")),
            ("prompt_provenance", r["prompt"].get("prompt_provenance"), mp.get("prompt_provenance")),
            ("prompt_construction_mode", r["prompt"].get("prompt_construction_mode"), mp.get("prompt_construction_mode")),
        ]
        for field, actual, expected in checks:
            if actual != expected:
                result.add("ERROR", "PROMPT_MANIFEST_DRIFT", f"{eid}: {field} differs from Manifest.")

        if set(r["prompt"]["prompt_class"]) != set(mp["prompt_class"]):
            result.add("ERROR", "PROMPT_CLASS_DRIFT", f"{eid}: Prompt Class differs from Manifest.")

        # Context parity against declared values when the Manifest value is known.
        context_map = [
            ("model_or_variant", "model_or_variant"),
            ("interface", "interface"),
            ("authentication_state", "authentication_state"),
            ("personalization_state", "personalization_state"),
            ("memory_state", "memory_state"),
            ("geography", "geography"),
            ("locale", "locale"),
            ("language", "language"),
        ]
        for ef, mf in context_map:
            declared = ms.get(mf)
            actual = r["system_context"].get(ef)
            if declared is not None and actual != declared:
                result.add("ERROR", "CONTEXT_DRIFT", f"{eid}: {ef}={actual!r}, Manifest={declared!r}.")

        dt = parse_dt(r["executed_at"])
        if first_allowed and dt < first_allowed:
            result.add("ERROR", "EXECUTION_BEFORE_ALLOWED", f"{eid}: execution predates Manifest's permitted start.")

        ex = r["exclusion"]
        if ex["excluded"]:
            if ex["rule_id"] not in exclusion_rules:
                result.add("ERROR", "UNDECLARED_EXCLUSION_RULE", f"{eid}: exclusion rule not predeclared in Manifest.")
            if not ex["rule_preexisted_execution"]:
                result.add("ERROR", "RETROACTIVE_EXCLUSION", f"{eid}: exclusion rule did not pre-exist execution.")

    valid_records = [r for r in records if not r["exclusion"]["excluded"]]
    excluded_records = [r for r in records if r["exclusion"]["excluded"]]

    # Exact valid execution count per prompt/system.
    planned = manifest["planned_execution_design"]["valid_executions_per_prompt_per_system"]
    valid_by_combo = Counter((r["prompt"]["prompt_id"], r["system_context"]["system_name"]) for r in valid_records)
    for pid in manifest_prompts:
        for sysname in manifest_systems:
            actual = valid_by_combo.get((pid, sysname), 0)
            if actual != planned:
                result.add(
                    "ERROR", "EXECUTION_COUNT_MISMATCH",
                    f"{pid}/{sysname}: {actual} valid executions, Manifest requires {planned}."
                )

    # Scope/report alignment.
    rs = report["scope_of_measurement"]
    ms = manifest["scope_of_measurement"]
    scope_pairs = [
        ("prompt_domain", rs.get("prompt_domain"), ms.get("prompt_domain")),
        ("geographic_scope", rs.get("geographic_scope"), ms.get("geographic_scope")),
        ("service_or_market_scope", rs.get("service_or_market_scope"), ms.get("service_or_market_scope")),
        ("language", rs.get("language"), ms.get("language")),
        ("locale", rs.get("locale"), ms.get("locale")),
        ("system_selection_scope", rs.get("system_selection_scope"), ms.get("system_selection_scope")),
        ("prompt_selection_criterion", rs.get("prompt_selection_criterion"), manifest.get("prompt_selection_criterion")),
    ]
    for field, actual, expected in scope_pairs:
        if actual != expected:
            result.add("ERROR", "REPORT_SCOPE_DRIFT", f"Report {field} does not match Manifest.")

    if set(rs["systems_tested"]) != set(manifest_systems):
        result.add("ERROR", "REPORT_SYSTEM_SCOPE", "Report systems_tested does not match Manifest.")

    expected_prov = set(p["prompt_provenance"] for p in manifest["prompt_set"])
    if set(rs["prompt_provenance"]) != expected_prov:
        result.add("ERROR", "REPORT_PROVENANCE", "Report Prompt Provenance does not match Manifest.")

    expected_modes = set(p["prompt_construction_mode"] for p in manifest["prompt_set"])
    if set(rs["prompt_construction_modes"]) != expected_modes:
        result.add("ERROR", "REPORT_CONSTRUCTION_MODE", "Report Prompt Construction Mode does not match Manifest.")

    branded, nonbranded = expected_prompt_class_counts(manifest)
    if rs["prompt_class_counts"]["branded"] != branded or rs["prompt_class_counts"]["non_branded"] != nonbranded:
        result.add("ERROR", "REPORT_PROMPT_CLASS_COUNTS", "Report branded/non-branded counts do not reconcile.")

    if rs["valid_execution_count"] != len(valid_records):
        result.add("ERROR", "REPORT_VALID_EXECUTIONS", "Report valid_execution_count does not reconcile.")

    if valid_records:
        min_dt = min(parse_dt(r["executed_at"]) for r in valid_records)
        max_dt = max(parse_dt(r["executed_at"]) for r in valid_records)
        if rs.get("observation_period_start") and parse_dt(rs["observation_period_start"]) != min_dt:
            result.add("ERROR", "REPORT_PERIOD_START", "Report observation_period_start does not equal first valid execution.")
        if rs.get("observation_period_end") and parse_dt(rs["observation_period_end"]) != max_dt:
            result.add("ERROR", "REPORT_PERIOD_END", "Report observation_period_end does not equal last valid execution.")

    # Report metric reconciliation.
    metric_by_state = defaultdict(list)
    for metric in report["observation_metrics"]:
        metric_by_state[metric["observation_state"]].append(metric)
        ss = metric["system_scope"]
        if ss["scope_type"] == "SINGLE_SYSTEM":
            sysname = ss["system_name"]
            selected = [r for r in valid_records if r["system_context"]["system_name"] == sysname]
            if sysname not in manifest_systems:
                result.add("ERROR", "REPORT_UNDECLARED_SYSTEM", f"Metric uses undeclared system {sysname}.")
                continue
        else:
            selected = list(valid_records)
            result.add(
                "WARNING", "CROSS_SYSTEM_FORMULA_MANUAL_CHECK",
                f"{metric['observation_state']}: raw cross-system counts checked; weighted formula requires manual review."
            )

        state_key = metric["observation_state"].lower()
        counts = state_counts(selected, state_key)
        exec_level = metric["execution_level"]
        observed = counts["OBSERVED"]
        not_observed = counts["NOT_OBSERVED"]
        not_established = counts["NOT_ESTABLISHED"]
        determinable = observed + not_observed
        valid = len(selected)
        coverage = determinable / valid if valid else 0
        rate = observed / determinable if determinable else None

        expected = {
            "observed": observed,
            "not_observed": not_observed,
            "not_established": not_established,
            "valid_executions": valid,
            "determinable_executions": determinable,
        }
        for field, val in expected.items():
            if exec_level[field] != val:
                result.add("ERROR", "METRIC_COUNT_MISMATCH", f"{metric['observation_state']}: {field} does not reconcile.")

        if not close(exec_level["determination_coverage"], coverage):
            result.add("ERROR", "DETERMINATION_COVERAGE", f"{metric['observation_state']}: determination coverage incorrect.")
        if not close(exec_level["rate_among_determinable"], rate):
            result.add("ERROR", "EXECUTION_RATE", f"{metric['observation_state']}: rate among determinable executions incorrect.")

        if coverage < 0.5 and metric["primary_presentation"] != "RAW_COUNTS":
            result.add("ERROR", "MAJORITY_INDETERMINATE_PRESENTATION", f"{metric['observation_state']}: coverage below 50% requires RAW_COUNTS primary presentation.")

        pl = metric.get("prompt_level")
        if pl:
            if pl["reduction_rule"] == "ANY_OBSERVED":
                op, tp = prompt_level_any(selected, state_key)
                if pl["observed_prompts"] != op or pl["total_prompts"] != tp:
                    result.add("ERROR", "PROMPT_LEVEL_COUNT", f"{metric['observation_state']}: ANY_OBSERVED prompt counts incorrect.")
                expected_rate = op / tp if tp else 0
                if not close(pl["rate"], expected_rate):
                    result.add("ERROR", "PROMPT_LEVEL_RATE", f"{metric['observation_state']}: prompt-level rate incorrect.")
            else:
                result.add(
                    "WARNING", "PROMPT_REDUCTION_MANUAL_CHECK",
                    f"{metric['observation_state']}: {pl['reduction_rule']} requires manual verification in validator v0.1."
                )

    # Mandatory adverse treatment if inclusion/recommendation is reported.
    if ("INCLUDED" in metric_by_state or "RECOMMENDED" in metric_by_state) and "ADVERSELY_TREATED" not in metric_by_state:
        result.add("ERROR", "ADVERSE_METRIC_MISSING", "Report includes INCLUDED/RECOMMENDED without ADVERSELY_TREATED metric.")

    if "INCLUDED" in metric_by_state or "RECOMMENDED" in metric_by_state:
        if report.get("adverse_treatment_summary") is None:
            result.add("ERROR", "ADVERSE_SUMMARY_MISSING", "Adverse treatment summary is required.")
        else:
            c = state_counts(valid_records, "adversely_treated")
            a = report["adverse_treatment_summary"]
            if (a["observed"], a["not_observed"], a["not_established"]) != (
                c["OBSERVED"], c["NOT_OBSERVED"], c["NOT_ESTABLISHED"]
            ):
                result.add("ERROR", "ADVERSE_SUMMARY_MISMATCH", "Adverse treatment summary does not reconcile.")

    # Claim validation reconciliation.
    claim_counter = Counter()
    no_eval_execs = 0
    decision_material_total = 0
    for r in valid_records:
        cv = r["claim_validation"]
        if cv["status"] == "NO_CLAIM_EVALUATED":
            no_eval_execs += 1
        else:
            for claim in cv["claims"]:
                if claim["decision_material"]:
                    decision_material_total += 1
                    claim_counter[claim["validation_state"]] += 1

    vs = report.get("validation_summary")
    if vs:
        if vs["decision_material_claims_total"] != decision_material_total:
            result.add("ERROR", "VALIDATION_TOTAL", "decision_material_claims_total does not reconcile.")
        mapping = {
            "verified": "VERIFIED",
            "inaccurate": "INACCURATE",
            "materially_misleading": "MATERIALLY_MISLEADING",
            "unverified": "UNVERIFIED",
        }
        for field, state in mapping.items():
            if vs["claim_outcomes"][field] != claim_counter.get(state, 0):
                result.add("ERROR", "VALIDATION_DISTRIBUTION", f"{field} claim count does not reconcile.")
        if vs["executions_no_claim_evaluated"] != no_eval_execs:
            result.add("ERROR", "NO_CLAIM_EVALUATED_COUNT", "Executions with NO_CLAIM_EVALUATED do not reconcile.")

        warnings = set(vs.get("warning_labels", []))
        if claim_counter.get("UNVERIFIED", 0) > 0 and "UNVERIFIED DECISION-MATERIAL CLAIMS PRESENT" not in warnings:
            result.add("ERROR", "UNVERIFIED_WARNING_MISSING", "Required UNVERIFIED warning label missing.")
        if decision_material_total == 0 and no_eval_execs > 0 and "DECISION-MATERIAL CLAIMS NOT VALIDATED" not in warnings:
            result.add(
                "WARNING", "NO_VALIDATION_WARNING_REVIEW",
                "No Decision-Material Claims were validated. Confirm whether DECISION-MATERIAL CLAIMS NOT VALIDATED is required for the published decision metric."
            )

    # Exclusion reconciliation.
    es = report["exclusions_summary"]
    total_attempted = len(records)
    excluded = len(excluded_records)
    exclusion_rate = excluded / total_attempted if total_attempted else 0
    if es["excluded_executions"] != excluded:
        result.add("ERROR", "EXCLUSION_COUNT", "Report excluded execution count does not reconcile.")
    if es["total_attempted_executions"] != total_attempted:
        result.add("ERROR", "ATTEMPTED_COUNT", "Report total attempted executions does not reconcile.")
    if not close(es["exclusion_rate"], exclusion_rate):
        result.add("ERROR", "EXCLUSION_RATE", "Report exclusion rate does not reconcile.")

    # Registry/report public conformance.
    if report["conformance_level"] == "FULL_CONFORMANCE":
        if registry.get("public_full_conformance_claimed") is not True:
            result.add("ERROR", "REGISTRY_PUBLIC_CONFORMANCE_FLAG", "Full-conformance report requires registry public_full_conformance_claimed=true for this public example.")
        access = registry.get("public_registry_access") or {}
        if access.get("accessible") is not True:
            result.add("ERROR", "REGISTRY_ACCESS", "Public Full Conformance requires accessible registry information.")

    # Known implementation limitations.
    if manifest.get("comparison_plan") is not None:
        result.add(
            "WARNING", "COMPARISON_UNIVERSE_MANUAL_REVIEW",
            "Validator v0.1 checks comparison schema but does not independently verify external universe completeness."
        )

    if manifest["classification_plan"]["mode"] in ("AUTOMATED", "HYBRID"):
        result.add(
            "WARNING", "AUDIT_SEED_MANUAL_REVIEW",
            "Audit sample seed timing/ledger-closure evidence requires an audit record not yet represented by a dedicated schema."
        )

    return result


def main():
    p = argparse.ArgumentParser(description="Validate a USO v0.9.5 test bundle.")
    p.add_argument("--manifest", required=True)
    p.add_argument("--registry", required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--schema-dir", default=None)
    p.add_argument("--json", action="store_true", help="Emit JSON result.")
    args = p.parse_args()

    script_dir = Path(__file__).resolve().parent
    schema_dir = Path(args.schema_dir) if args.schema_dir else script_dir.parent / "schema"

    schemas = {
        "manifest": load_json(schema_dir / "uso-test-manifest.schema.json"),
        "registry": load_json(schema_dir / "uso-test-registry.schema.json"),
        "evidence": load_json(schema_dir / "uso-evidence.schema.json"),
        "report": load_json(schema_dir / "uso-report.schema.json"),
    }

    result = validate_bundle(
        load_json(args.manifest),
        load_json(args.registry),
        load_json(args.evidence),
        load_json(args.report),
        schemas,
    )

    payload = result.as_dict()
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"USO validation: {payload['status']}")
        for issue in payload["issues"]:
            print(f"{issue['severity']}: {issue['code']}: {issue['message']}")
        print(f"Errors: {payload['errors']}  Warnings: {payload['warnings']}")

    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
