#!/usr/bin/env python3
"""Validate a full resume self-audit and summarize human-assigned scores.

Standard library only. No resume parsing, keyword scoring, network access,
candidate ranking, or factual verification is performed here.
"""

import argparse
import json
import re
import sys
from pathlib import Path


VERSION = "1.0"
RUBRIC = Path(__file__).resolve().parents[1] / "references" / "rubric.md"
EXPECTED_COUNTS = {"KW": 7, "PS": 14, "JM": 20, "SP": 15, "BQ": 9,
                   "PR": 14, "SK": 7, "ED": 8, "RS": 6}
TEXT_FIELDS = ("evidence", "location", "rationale", "fix")


def load_catalog():
    """Read the rubric itself as the sole source of check wording."""
    categories = {}
    checks = {}
    current = None
    for line in RUBRIC.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^## ([A-Z]{2}) — (.+)$", line)
        if heading:
            current, title = heading.groups()
            if current in categories:
                raise ValueError(f"Duplicate rubric category: {current}")
            categories[current] = title
        row = re.match(r"^\| ([A-Z]{2}\d{2}) \| (.+?) \| (.+?) \|$", line)
        if row:
            check_id, description, applicability = row.groups()
            if current is None or check_id[:2] != current:
                raise ValueError(f"Rubric category mismatch: {check_id}")
            if check_id in checks:
                raise ValueError(f"Duplicate rubric ID: {check_id}")
            checks[check_id] = {"category": current, "check": description,
                                "applicability": applicability}
    if list(categories) != list(EXPECTED_COUNTS):
        raise ValueError("Rubric categories/order do not match version 1.0")
    for category, expected in EXPECTED_COUNTS.items():
        actual = [i for i in checks if i.startswith(category)]
        wanted = [f"{category}{n:02d}" for n in range(1, expected + 1)]
        if actual != wanted:
            raise ValueError(f"Rubric IDs/count do not match: {category}")
    return categories, checks


def make_template(checks):
    return {
        "rubric_version": VERSION,
        "metadata": {"mode": "unassessed", "note": "Replace every observation; this is not an evaluation."},
        "checks": [
            {"id": check_id, "check": item["check"], "score": "U",
             "evidence": "Not yet assessed.", "location": "not inspected",
             "rationale": "Assessment has not been performed.",
             "fix": "Inspect the applicable input and record an evidence-grounded judgment."}
            for check_id, item in checks.items()
        ],
    }


def validate_audit(audit, catalog):
    if not isinstance(audit, dict):
        raise ValueError("Audit must be a JSON object")
    if audit.get("rubric_version") != VERSION:
        raise ValueError(f"rubric_version must be {VERSION!r}")
    rows = audit.get("checks")
    if not isinstance(rows, list):
        raise ValueError("checks must be a list")
    found = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"checks[{index}] must be an object")
        check_id = row.get("id")
        if not isinstance(check_id, str) or check_id not in catalog:
            raise ValueError(f"Unknown check ID at row {index}: {check_id!r}")
        if check_id in found:
            raise ValueError(f"Duplicate check ID: {check_id}")
        score = row.get("score")
        numeric = type(score) is int and score in (0, 1, 2)
        state = isinstance(score, str) and score in ("NA", "U")
        if not numeric and not state:
            raise ValueError(f"{check_id}: score must be integer 0/1/2 or string NA/U")
        for field in TEXT_FIELDS:
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"{check_id}: {field} must be a nonempty string")
        found[check_id] = row
    missing = sorted(set(catalog) - set(found))
    if missing:
        raise ValueError("Missing check IDs: " + ", ".join(missing))
    return found


def summarize(audit, categories, catalog, overall=False):
    rows = validate_audit(audit, catalog)
    result = {
        "rubric_version": VERSION,
        "interpretation": "Descriptive document-evidence audit; not an employer ATS score or hiring prediction.",
        "categories": [],
        "totals": {"checks": len(catalog), "scored": 0, "NA": 0, "U": 0},
    }
    unrounded = []
    for category, name in categories.items():
        group = [rows[i] for i in catalog if catalog[i]["category"] == category]
        scores = [r["score"] for r in group if type(r["score"]) is int]
        na = sum(r["score"] == "NA" for r in group)
        unknown = sum(r["score"] == "U" for r in group)
        points, possible = sum(scores), 2 * len(scores)
        quality = 100 * points / possible if possible else None
        assessable = len(scores) + unknown
        coverage = 100 * len(scores) / assessable if assessable else None
        result["categories"].append({
            "id": category, "name": name, "points": points,
            "possible": possible, "observed_quality_percent": round(quality, 1) if quality is not None else None,
            "scored": len(scores), "NA": na, "U": unknown,
            "assessment_coverage_percent": round(coverage, 1) if coverage is not None else None,
            "partial": bool(unknown),
        })
        result["totals"]["scored"] += len(scores)
        result["totals"]["NA"] += na
        result["totals"]["U"] += unknown
        if quality is not None:
            unrounded.append(quality)
    total_applicable = result["totals"]["scored"] + result["totals"]["U"]
    result["totals"]["assessment_coverage_percent"] = (
        round(100 * result["totals"]["scored"] / total_applicable, 1)
        if total_applicable else None
    )
    if overall:
        if result["totals"]["U"]:
            raise ValueError("Overall score unavailable: U checks remain; report category results and coverage")
        if not unrounded:
            raise ValueError("Overall score unavailable: no scored categories")
        result["overall"] = {
            "editorial_quality_percent": round(sum(unrounded) / len(unrounded), 1),
            "categories_included": len(unrounded),
            "method": "Equal category mean; wholly NA domains excluded; unvalidated editorial convention.",
        }
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", nargs="?", type=Path, help="Full audit JSON file")
    parser.add_argument("--template", action="store_true", help="Print a complete, unassessed JSON template")
    parser.add_argument("--overall", action="store_true", help="Compute an explicitly requested editorial mean; requires no U")
    args = parser.parse_args(argv)
    if args.template and (args.audit or args.overall):
        parser.error("--template cannot be combined with an audit or --overall")
    if not args.template and not args.audit:
        parser.error("Supply an audit path or --template")
    try:
        categories, catalog = load_catalog()
        if args.template:
            result = make_template(catalog)
        else:
            audit = json.loads(args.audit.read_text(encoding="utf-8"))
            result = summarize(audit, categories, catalog, args.overall)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Audit error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
