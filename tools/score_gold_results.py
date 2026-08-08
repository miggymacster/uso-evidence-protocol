#!/usr/bin/env python3
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

STATES = ["RETRIEVED","MENTIONED","CITED","INCLUDED","RECOMMENDED","ADVERSELY_TREATED"]

def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

def by_case(response_file):
    return {r["case_id"]: r for r in response_file["responses"]}

def pct(n,d):
    return None if d == 0 else n/d

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--answer-key", required=True)
    ap.add_argument("responses", nargs="+")
    args = ap.parse_args()

    key = load(args.answer_key)["answers"]
    raters = [(Path(p).stem, by_case(load(p))) for p in args.responses]

    output = {
        "rater_count": len(raters),
        "accuracy_vs_candidate_key": {},
        "pairwise_raw_agreement": {},
        "case_disagreement_counts": {}
    }

    for rname, rr in raters:
        state_correct = Counter()
        state_total = Counter()
        report_correct = report_total = 0
        for cid, ans in key.items():
            if cid not in rr:
                continue
            resp = rr[cid]
            if "expected_observation_states" in ans:
                for s in STATES:
                    state_total[s] += 1
                    if resp["observation_states"][s] == ans["expected_observation_states"][s]:
                        state_correct[s] += 1
            else:
                report_total += 1
                if resp["core_conformant"] == ans["core_conformant"]:
                    report_correct += 1
        output["accuracy_vs_candidate_key"][rname] = {
            "observation_states": {s: pct(state_correct[s], state_total[s]) for s in STATES},
            "reporting_integrity": pct(report_correct, report_total)
        }

    for (n1,r1),(n2,r2) in itertools.combinations(raters,2):
        agree = Counter(); total = Counter()
        for cid in sorted(set(r1) & set(r2)):
            if "observation_states" in r1[cid] and "observation_states" in r2[cid]:
                for s in STATES:
                    total[s] += 1
                    if r1[cid]["observation_states"][s] == r2[cid]["observation_states"][s]:
                        agree[s] += 1
            elif "core_conformant" in r1[cid] and "core_conformant" in r2[cid]:
                total["REPORTING"] += 1
                if r1[cid]["core_conformant"] == r2[cid]["core_conformant"]:
                    agree["REPORTING"] += 1
        output["pairwise_raw_agreement"][f"{n1}__{n2}"] = {
            k: pct(agree[k], total[k]) for k in total
        }

    for cid in key:
        values = []
        for _, rr in raters:
            if cid in rr:
                if "observation_states" in rr[cid]:
                    values.append(tuple(rr[cid]["observation_states"][s] for s in STATES))
                else:
                    values.append(rr[cid]["core_conformant"])
        output["case_disagreement_counts"][cid] = max(0, len(set(values)) - 1)

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
