"""Grade saved answers with code only. No model judges anything.

Run `python score.py` to write results/scores.json (every metric, with 95% bootstrap
ranges) which report.py turns into tables and charts.
"""
import json
import random
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import numpy as np

import prompts

RESULTS = Path(__file__).parent / "results"


def parse(text: str | None) -> dict | None:
    """JSON object from the answer, or None for refusals / bad format."""
    if not text:
        return None
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    try:
        d = json.loads(text)
        return d if isinstance(d, dict) else None
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, flags=re.S)
        try:
            return json.loads(m.group()) if m else None
        except json.JSONDecodeError:
            return None


def ci(vals: list, seed=0) -> dict:
    """Mean with a 95% bootstrap interval; n is the number of items."""
    if not vals:
        return {"mean": None, "lo": None, "hi": None, "n": 0}
    rng = np.random.default_rng(seed)
    v = np.array(vals, dtype=float)
    boots = [rng.choice(v, len(v)).mean() for _ in range(1000)]
    return {"mean": round(v.mean(), 3), "lo": round(np.percentile(boots, 2.5), 3),
            "hi": round(np.percentile(boots, 97.5), 3), "n": len(v)}


def load_answers(track: int) -> dict:
    """{model: {prompt_id: parsed answer or None}} plus format counts."""
    out = {}
    for mdir in sorted((RESULTS / f"track{track}").glob("*")):
        ans = {}
        for f in mdir.glob("*.json"):
            d = json.loads(f.read_text())
            ans[d["id"]] = parse(d.get("text"))
        out[mdir.name] = ans
    return out


def common(track, ans, recs):
    """Metrics shared by all tracks: bad-format rate, self-agreement, leakage."""
    bad = [a is None for pid, a in ans.items()]
    reps = [(pid[:-4], pid) for pid in ans if pid.endswith("_rep") and pid[:-4] in ans]
    agree = [json.dumps(ans[o], sort_keys=True) == json.dumps(ans[r], sort_keys=True) for o, r in reps]
    leak = []
    for r in recs:
        if r["condition"] == "leak" and r["id"] in ans:
            a = ans[r["id"]] or {}
            key = "player" if track == 1 else "team"
            said = str(a.get(key, "")).lower()
            leak.append(_name_match(said, r["truth"][key]))
    return {"bad_format": ci(bad), "self_agreement": ci(agree), "leak_rate": ci(leak)}


def _name_match(said: str, real: str) -> bool:
    """True if any surname token (not the first name) of the real name appears in the answer."""
    norm = lambda s: unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
    toks = [t for t in re.split(r"\W+", norm(real)) if len(t) > 3][1:] or [norm(real).split()[-1]]
    return any(t in norm(said) for t in toks)


def track1(ans, recs):
    m = {}
    for cond in ["none", "true", "false"]:
        for grp in ["all", "defender", "midfielder", "forward"]:
            acc, follow = [], []
            for r in recs:
                if r["condition"] != cond or r["id"] not in ans or grp not in ("all", r["group"]):
                    continue
                a = (ans[r["id"]] or {}).get("position")
                acc.append(a == r["truth"]["position"])
                if r["truth"]["label"]:
                    follow.append(a == r["truth"]["label"])
            m[f"{cond}/{grp}/accuracy"] = ci(acc)
            if cond != "none":
                m[f"{cond}/{grp}/label_follow"] = ci(follow)
                m[f"{cond}/{grp}/override"] = ci([not f for f in follow])
    return m


def track2(ans, recs):
    m, by = {}, defaultdict(dict)
    qs = [k for k, _, _ in prompts.QUESTIONS]
    for r in recs:
        if r["condition"] != "leak" and r["id"] in ans:
            by[r["group"]][r["condition"]] = (ans[r["id"]] or {}, r["truth"])
    for cond in ["neutral", "big", "small"]:
        have = [by[team][cond] for team in by if cond in by[team]]  # (answer, truth) pairs
        m[f"{cond}/accuracy"] = ci([str(a.get(q, "")).lower() == t[q] for a, t in have for q in qs])
        m[f"{cond}/finish_mae"] = ci([abs(float(a["predicted_finish"]) - t["finish"])
                                      for a, t in have if _num(a.get("predicted_finish"))])
        if cond != "neutral":
            flips, toward_yes, shift = [], [], []
            for team in by:
                if cond not in by[team] or "neutral" not in by[team]:
                    continue
                a, n = by[team][cond][0], by[team]["neutral"][0]
                for q in qs:
                    f = str(a.get(q, "")).lower() != str(n.get(q, "")).lower()
                    flips.append(f)
                    if f:
                        toward_yes.append(str(a.get(q, "")).lower() == "yes")
                if _num(a.get("predicted_finish")) and _num(n.get("predicted_finish")):
                    shift.append(float(a["predicted_finish"]) - float(n["predicted_finish"]))
            m[f"{cond}/flip_rate"] = ci(flips)
            m[f"{cond}/flips_toward_yes"] = ci(toward_yes)  # >0.5 = named club looks better
            m[f"{cond}/finish_shift_vs_neutral"] = ci(shift)  # negative = predicted higher finish
    return m


def _num(v):
    try:
        float(v)
        return True
    except (TypeError, ValueError):
        return False


def track3(ans, recs):
    import perturb
    m, det, loc, typ, fa = {}, defaultdict(list), defaultdict(list), defaultdict(list), []
    for r in recs:
        if r["id"] not in ans:
            continue
        a = ans[r["id"]] or {}
        said = str(a.get("corrupt", "")).lower() == "yes"
        plant, idx = r["truth"]["plant"], r["truth"]["index"]
        if plant is None:
            fa.append(said)
            continue
        det[plant].append(said)
        kind = "football_sense" if plant in perturb.FOOTBALL_SENSE else "code_checkable"
        det[kind].append(said)
        if said:
            loc[plant].append(_num(a.get("index")) and abs(float(a["index"]) - idx) <= 1)
            typ[plant].append(a.get("type") == plant)
            loc[kind].append(loc[plant][-1])
    m["clean/false_alarm"] = ci(fa)
    for k in list(perturb.PLANTS) + ["code_checkable", "football_sense"]:
        m[f"{k}/detected"] = ci(det[k])
        m[f"{k}/localized_within_1"] = ci(loc[k])
        if k in perturb.PLANTS:
            m[f"{k}/type_correct"] = ci(typ[k])
    m["any_plant/detected"] = ci([x for p in perturb.PLANTS for x in det[p]])
    return m


def main():
    scores = {}
    for t, fn in [(1, track1), (2, track2), (3, track3)]:
        if not (RESULTS / f"track{t}").exists():
            continue
        recs = prompts.load(t)
        for model, ans in load_answers(t).items():
            scores[f"track{t}/{model}"] = common(t, ans, recs) | fn(ans, recs)
    (RESULTS / "scores.json").write_text(json.dumps(scores, indent=1))
    for k, v in scores.items():
        print(k)
        for name, c in v.items():
            if c["n"]:
                print(f"  {name:40s} {c['mean']:.3f}  [{c['lo']:.3f}, {c['hi']:.3f}]  n={c['n']}")


if __name__ == "__main__":
    main()
