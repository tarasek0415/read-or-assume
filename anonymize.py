"""Map real names to stable IDs so prompts never carry a name.

The mapping is derived from a seed, so it is identical on every run. It is
kept in cache/ids.json only for the leakage check and the final report; it is
never put into a prompt.
"""
import json
import random
from pathlib import Path

IDS = Path(__file__).parent / "cache" / "ids.json"


def build(players: list[str], teams: list[str], seed: int) -> dict:
    rng = random.Random(seed)
    p, t = sorted(set(players)), sorted(set(teams))
    rng.shuffle(p), rng.shuffle(t)
    ids = {"player": {name: f"P{i:03d}" for i, name in enumerate(p, 1)},
           "team": {name: f"T{i:02d}" for i, name in enumerate(t, 1)}}
    IDS.write_text(json.dumps(ids, indent=1))
    return ids


def load() -> dict:
    return json.loads(IDS.read_text())


def real_name(kind: str, anon_id: str) -> str:
    return {v: k for k, v in load()[kind].items()}[anon_id]
