"""Jev (TypeSafe System One) client: typed routing signals for the Beal research loop.

Jev is NEVER a proof oracle. Every answer is stored tagged HYPOTHESIS_ONLY and may
only route attention; status changes to PROVED/REFUTED/VERIFIED require a derivation,
a counterexample, an exact computation, or a proof assistant.

Stdlib only (urllib). Key is read from $TYPESAFE_API_KEY or .env.local; never logged.
"""
from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"
REPO = Path(__file__).resolve().parent.parent
EVIDENCE_DIR = REPO / "research" / "pool" / "evidence"


class JevUnavailable(RuntimeError):
    """Service unreachable or refusing: caller must degrade to pure AI reasoning."""


def _api_key() -> str:
    key = os.environ.get("TYPESAFE_API_KEY")
    if key:
        return key.strip()
    envfile = REPO / ".env.local"
    if envfile.exists():
        for line in envfile.read_text().splitlines():
            line = line.strip()
            if line.startswith("TYPESAFE_API_KEY="):
                return line.split("=", 1)[1].strip().strip("'\"")
    raise JevUnavailable("TYPESAFE_API_KEY not set (env or .env.local)")


# ---------------------------------------------------------------- question types

def noul(instructions: str, true: str, false: str) -> dict[str, Any]:
    return {"type": "noul", "instructions": instructions,
            "criteria": {"true": true, "false": false}}


def choice(instructions: str, criteria: dict[str, str]) -> dict[str, Any]:
    return {"type": "choice", "instructions": instructions, "criteria": criteria}


def score(instructions: str, criteria: list[str]) -> dict[str, Any]:
    return {"type": "score", "instructions": instructions, "criteria": criteria}


# ---------------------------------------------------------------- transport

def ask(state: Any, questions: dict[str, dict[str, Any]], *,
        timeout: float = 90.0, tries: int = 5) -> dict[str, Any]:
    """One request, one state. Returns {"answers": ..., "usage": ...}."""
    body = json.dumps({"model": MODEL, "state": state, "questions": questions}).encode()
    headers = {"Authorization": f"Bearer {_api_key()}", "Content-Type": "application/json"}
    delay = 1.0
    for attempt in range(tries):
        req = urllib.request.Request(ENDPOINT, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 529) and attempt < tries - 1:
                time.sleep(delay + random.random() * 0.5)
                delay *= 2
                continue
            detail = e.read().decode()[:400]
            raise JevUnavailable(f"HTTP {e.code} from Jev: {detail}") from None
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < tries - 1:
                time.sleep(delay + random.random() * 0.5)
                delay *= 2
                continue
            raise JevUnavailable(f"Jev unreachable: {e}") from None
    raise JevUnavailable("Jev retries exhausted")


def ask_many(states: list[Any], questions: dict[str, dict[str, Any]], *,
             concurrency: int = 12) -> list[dict[str, Any]]:
    """Same questions over many states, concurrently. Failures come back as {'error': ...}."""
    def one(s: Any) -> dict[str, Any]:
        try:
            return ask(s, questions)
        except JevUnavailable as e:
            return {"error": str(e)}
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        return list(pool.map(one, states))


# ---------------------------------------------------------------- persistence

def persist(candidate_id: str, state: Any, questions: dict[str, Any],
            response: dict[str, Any]) -> Path:
    """Store raw request + answers so the exploration tree can be reconstructed."""
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    path = EVIDENCE_DIR / f"{candidate_id}_{int(time.time())}.json"
    path.write_text(json.dumps({
        "state": "HYPOTHESIS_ONLY",
        "candidate_id": candidate_id,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "model": MODEL,
        "request_state": state,
        "questions": questions,
        "response": response,
    }, indent=2))
    return path
