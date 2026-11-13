"""Send prompts to models through OpenRouter, one stateless call each, and save every answer.

Usage:
  python run.py --track 1 --model anthropic/claude-haiku-5.5 --limit 20   # test batch
  python run.py --track 1 --model all                                       # full run
  python run.py --track 1 --model all --estimate                            # cost only, no calls
Finished calls (a file in results/) are skipped, so a run can be resumed.
"""
import argparse
import json
import random
import sys
import time
from pathlib import Path

import httpx
import yaml
from dotenv import dotenv_values

import prompts

ROOT = Path(__file__).parent
CFG = yaml.safe_load(open(ROOT / "config.yaml"))
BASE_URL = "https://openrouter.ai/api/v1"  # fixed in code on purpose; never read from env
KEY_VAR = "OPENROUTER_API_KEY"
ENV_FILE = ROOT / ".env"
RESULTS = ROOT / "results" / CFG["version"]


def startup() -> str:
    """Load the API key from this project's .env. Never prints a key value."""
    env = dotenv_values(ENV_FILE)  # explicit path; os.environ is not consulted
    key = env.get(KEY_VAR)
    print(f"env file: {ENV_FILE}  base url: {BASE_URL}  key var: {KEY_VAR}  "
          f"key present: {bool(key)}")
    if not key:
        sys.exit(f"put {KEY_VAR}=... in {ENV_FILE}")
    return key


def call(key: str, m: dict, system: str, user: str) -> dict:
    model, effort = m["id"], m.get("reasoning", CFG["reasoning"])  # per-model override in config
    body = {"model": model, "temperature": 0,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "usage": {"include": True}}
    if effort == "off":  # thinking tokens would eat the answer budget and the money
        body |= {"reasoning": {"enabled": False}, "max_tokens": CFG["max_tokens"]}
    else:  # the top models refuse to switch thinking off: a bigger budget, low effort
        body |= {"reasoning": {"effort": effort}, "max_tokens": CFG["max_tokens_with_reasoning"]}
    headers = {"Authorization": f"Bearer {key}"}  # no referer/title/session/user fields
    for attempt in range(6):
        try:
            r = httpx.post(f"{BASE_URL}/chat/completions", json=body, headers=headers, timeout=180)
        except httpx.HTTPError as e:
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            d = r.json()
            if "choices" in d:
                return {"text": d["choices"][0]["message"]["content"], "usage": d.get("usage", {})}
        if r.status_code == 429 and "per-day" in r.text:  # free models: daily cap, waiting won't help
            return {"text": None, "error": "daily_limit", "usage": {}}
        # 429 (free models allow ~20 a minute) gets a longer wait than other errors
        time.sleep(15 * (attempt + 1) if r.status_code == 429 else 2 ** attempt)
    return {"text": None, "error": f"{r.status_code} {r.text[:200]}", "usage": {}}


def balance(key: str) -> float | None:
    """Credits left on the OpenRouter account, or None if the lookup fails."""
    try:
        d = httpx.get(f"{BASE_URL}/credits", headers={"Authorization": f"Bearer {key}"}, timeout=30).json()["data"]
        return d["total_credits"] - d["total_usage"]
    except Exception:
        return None


def estimate(recs: list[dict], model: dict) -> float:
    toks_in = sum(len(r["system"] + r["user"]) / 1.7 for r in recs)  # measured: numbers tokenise badly
    toks_out = len(recs) * (600 if model.get("reasoning") == "minimal" else 60)  # measured per model
    return (toks_in * model["price_in"] + toks_out * model["price_out"]) / 1e6


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", type=int, required=True)
    ap.add_argument("--model", default="all")
    ap.add_argument("--limit", type=int, help="only the first N prompts (after shuffling)")
    ap.add_argument("--estimate", action="store_true", help="print cost estimate and exit")
    ap.add_argument("--version", default=CFG["version"], help="prompt/result folder, e.g. v1 or v2")
    a = ap.parse_args()
    global RESULTS
    RESULTS = ROOT / "results" / a.version

    recs = prompts.load(a.track, a.version)
    rng = random.Random(CFG["seed"])
    rng.shuffle(recs)
    repeats = [dict(r, id=r["id"] + "_rep") for r in rng.sample(recs, round(len(recs) * CFG["repeat_fraction"]))]
    recs = recs + repeats
    if a.limit:
        recs = recs[: a.limit]
    models = [m for m in CFG["models"] if a.model in ("all", m["id"])]

    for m in models:
        todo = [r for r in recs if not _done(_path(a.track, m["id"], r["id"]))]
        est = estimate(todo, m)
        print(f"{m['id']}: {len(todo)} calls to make, estimated ${est:.2f}")
        if a.estimate:
            continue
        if est > CFG["spend"]["hard_cap_usd"]:
            sys.exit("estimate exceeds spend.hard_cap_usd in config.yaml; lower --limit")
        key = startup()
        left = balance(key)
        if left is None:
            sys.exit("could not read the account balance (expired key or no network); not spending blind")
        print(f"credits left: ${left:.2f}")
        if left - est < CFG["spend"]["reserve_usd"]:
            sys.exit("not enough credit for this batch; lower --limit or top up")
        if input(f"send {len(todo)} calls to {m['id']} (~${est:.2f})? [y/N] ").lower() != "y":
            continue
        spent = 0.0
        for i, r in enumerate(todo, 1):
            out = call(key, m, r["system"], r["user"])
            if out.get("error") == "daily_limit":
                sys.exit(f"free-model daily limit reached after {i - 1} calls. Finished answers are saved; rerun tomorrow.")
            out |= {"id": r["id"], "model": m["id"], "track": a.track}
            p = _path(a.track, m["id"], r["id"])
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(out, indent=1))
            spent += out["usage"].get("cost", 0) or 0
            if i % 10 == 0 or i == len(todo):
                left = balance(key)
                print(f"  {i}/{len(todo)}  spent ${spent:.3f}  left ${left if left is None else round(left, 2)}", flush=True)
                if left is not None and left < CFG["spend"]["reserve_usd"]:
                    sys.exit("stopping: credit below reserve. Finished answers are saved; rerun to resume.")


def _done(p: Path) -> bool:
    """A saved answer counts as done only if the call succeeded (errors are retried)."""
    return p.exists() and json.loads(p.read_text()).get("text") is not None


def _path(track, model, pid) -> Path:
    return RESULTS / f"track{track}" / model.replace("/", "_").replace(":", "_") / f"{pid}.json"


if __name__ == "__main__":
    main()
