"""Research pool store for the Beal exploration loop.

    python3 code/pool.py list [STATUS]
    python3 code/pool.py add   '<json object with at least id, claim, method, status>'
    python3 code/pool.py set   ID field=value [field=value ...]     (value parsed as JSON, else string)
    python3 code/pool.py show  ID

Candidates are never deleted: a refuted route keeps its failure_reason and extracted
lemmas so the loop does not rediscover the same obstruction.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

POOL = Path(__file__).resolve().parent.parent / "research" / "pool" / "candidates.json"
TERMINAL = {"REFUTED", "DUPLICATE"}
STATUSES = {"ACTIVE", "PROMISING", "PARTIAL_RESULT", "BLOCKED", "REFUTED", "DUPLICATE",
            "VERIFICATION_REQUIRED", "SUBMISSION_READY"}
TEMPLATE = {"parents": [], "inspirations": [], "evidence": [], "obligations": [],
            "evaluations": {}, "failure_reason": None, "novelty_note": None, "extracted": []}


def load() -> dict:
    return json.loads(POOL.read_text())


def save(db: dict) -> None:
    POOL.write_text(json.dumps(db, indent=2) + "\n")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd, args = sys.argv[1], sys.argv[2:]
    db = load()
    cands = db["candidates"]
    index = {c["id"]: c for c in cands}

    if cmd == "list":
        want = args[0].upper() if args else None
        for c in cands:
            if want and c.get("status") != want:
                continue
            print(f"{c['id']:<8} {c.get('status',''):<22} {c['claim'][:90]}")
        return 0

    if cmd == "show":
        print(json.dumps(index[args[0]], indent=2))
        return 0

    if cmd == "add":
        obj = json.loads(args[0])
        for k in ("id", "claim", "method", "status"):
            if k not in obj:
                raise SystemExit(f"missing required field: {k}")
        if obj["id"] in index:
            raise SystemExit(f"id already used: {obj['id']}")
        if obj["status"] not in STATUSES:
            raise SystemExit(f"bad status: {obj['status']}")
        cands.append({**TEMPLATE, **obj})
        save(db)
        print(f"added {obj['id']}")
        return 0

    if cmd == "set":
        cid, rest = args[0], args[1:]
        c = index[cid]
        for pair in rest:
            k, v = pair.split("=", 1)
            try:
                val = json.loads(v)
            except json.JSONDecodeError:
                val = v
            if k == "status":
                if val not in STATUSES:
                    raise SystemExit(f"bad status: {val}")
                if val in TERMINAL and not (c.get("failure_reason") or rest_has(rest, "failure_reason")):
                    raise SystemExit(f"{val} requires failure_reason to be set in the same call")
            c[k] = val
        save(db)
        print(json.dumps(c, indent=2))
        return 0

    print(__doc__)
    return 1


def rest_has(rest: list[str], key: str) -> bool:
    return any(p.startswith(key + "=") for p in rest)


if __name__ == "__main__":
    raise SystemExit(main())
