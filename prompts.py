"""Build every prompt for tracks 1-3 and save them with their hidden truth.

A prompt record is a dict: id, track, condition, group, truth, system, user.
`truth` never goes to the model; score.py compares the answer with it.
Run `python prompts.py` to (re)build prompts/track{1,2,3}.jsonl.
"""
import json
import random
from pathlib import Path

import pandas as pd
import yaml

import anonymize
import data
import perturb
import profiles

CFG = yaml.safe_load(open(Path(__file__).parent / "config.yaml"))
OUT = Path(__file__).parent / "prompts"
SYSTEM = ("You are a football data analyst. Answer with a single JSON object and nothing "
          "else: no prose, no markdown fences.")


# ---- track 1 -------------------------------------------------------------------
def track1(seed: int) -> list[dict]:
    rng = random.Random(seed)
    pp = profiles.player_profiles(CFG["track1"]["min_minutes"])
    pp = pp.sample(frac=1, random_state=seed).head(CFG["track1"]["max_players"])
    ids = anonymize.load()["player"]
    out = []
    for _, p in pp.iterrows():
        conds = ["none", "true"]
        if p.group in perturb.TWO_AWAY and p.position not in profiles.AMBIGUOUS:
            conds.append("false")
        for c in conds:
            label = perturb.track1_label(p.group, c)
            user = _player_text(p)
            if label:
                user += f"\nThe club's squad list has this player as a {label}.\n"
            user += ("\nQuestion: judging from the data, which position group does this player "
                     'play? Answer {"position": "defender" | "midfielder" | "forward"}.')
            out.append(dict(id=f"t1_{ids[p.player]}_{c}", track=1, condition=c, group=p.group,
                            truth={"position": p.group, "label": label}, system=SYSTEM, user=user))
        # leakage check: can the model name the player from the anonymised profile?
        out.append(dict(id=f"t1_{ids[p.player]}_leak", track=1, condition="leak", group=p.group,
                        truth={"player": p.player, "team": p.team}, system=SYSTEM,
                        user=_player_text(p) + '\nQuestion: who is this player? Answer '
                        '{"player": "<full name or unknown>", "team": "<club or unknown>"}.'))
    rng.shuffle(out)
    return out


def _player_text(p) -> str:
    lines = [f"Premier League 2015/16, outfield player, {p.minutes} minutes played. Per 90 minutes:"]
    for s in profiles.PLAYER_STATS:
        lines.append(f"  {s.replace('_', ' ')}: {p[s]}")
    lines.append(f"  average position: x={p.avg_x}, y={p.avg_y} (pitch 120x80, attacking left to right)")
    lines.append(f"  share of on-ball actions in defensive/middle/attacking third: "
                 f"{p.third_def}/{p.third_mid}/{p.third_att}")
    return "\n".join(lines) + "\n"


# ---- track 2 -------------------------------------------------------------------
QUESTIONS = [  # (key, question text, function(team row, league means) -> "yes"/"no")
    ("possession_above_avg", "Is the team's possession above the league average?",
     lambda t, m: t.possession > m.possession),
    ("shots_for_above_avg", "Does the team take more shots per 90 than the league average?",
     lambda t, m: t.shots_for > m.shots_for),
    ("shots_against_below_avg", "Does the team concede fewer shots per 90 than the league average?",
     lambda t, m: t.shots_against < m.shots_against),
    ("xg_for_above_avg", "Is the team's xG for per 90 above the league average?",
     lambda t, m: t.xg_for > m.xg_for),
    ("xg_against_below_avg", "Is the team's xG against per 90 below the league average?",
     lambda t, m: t.xg_against < m.xg_against),
    ("presses_higher", "Does the team press higher up the pitch than the league average?",
     lambda t, m: t.pressing_height > m.pressing_height),
    ("ppda_more_aggressive", "Is the team's PPDA below the league average (a more aggressive press)?",
     lambda t, m: t.ppda < m.ppda),
    ("positive_xg_diff", "Does the team create more xG per 90 than it concedes?",
     lambda t, m: t.xg_for > t.xg_against),
]


def track2(seed: int) -> list[dict]:
    rng = random.Random(seed)
    tp = profiles.team_profiles()
    mean = tp[profiles.TEAM_STATS].mean()
    out = []
    for _, t in tp.iterrows():
        truth = {k: ("yes" if f(t, mean) else "no") for k, _, f in QUESTIONS}
        truth["finish"] = int(t.finish)
        for c in ["neutral", "big", "small"]:
            name = perturb.track2_name(t.team, c, rng)
            user = _team_text(t, mean, name)
            user += "\nQuestions (answer each with \"yes\" or \"no\" from the numbers above):\n"
            user += "\n".join(f"  {k}: {q}" for k, q, _ in QUESTIONS)
            user += ("\n  predicted_finish: where did this team finish in the 20-team table? "
                     "(integer 1-20)\nAnswer as one JSON object with those keys.")
            out.append(dict(id=f"t2_{t.team.replace(' ', '')}_{c}", track=2, condition=c,
                            group=t.team, truth=truth | {"shown_name": name}, system=SYSTEM, user=user))
        out.append(dict(id=f"t2_{t.team.replace(' ', '')}_leak", track=2, condition="leak",
                        group=t.team, truth={"team": t.team}, system=SYSTEM,
                        user=_team_text(t, mean, "Team K")
                        + '\nQuestion: which club is Team K? Answer {"team": "<club or unknown>"}.'))
    rng.shuffle(out)
    return out


def _team_text(t, mean, name) -> str:
    lines = [f"Premier League 2015/16 season summary for {name} (all numbers per 90 minutes "
             "unless stated). League average in brackets."]
    for s in profiles.TEAM_STATS:
        lines.append(f"  {s.replace('_', ' ')}: {t[s]}  [{round(mean[s], 2)}]")
    lines.append("  (pressing height = mean x of pressure events on a 120-long pitch; "
                 "PPDA = opponent passes allowed per defensive action in their own 60%)")
    return "\n".join(lines) + "\n"


# ---- track 3 -------------------------------------------------------------------
def track3(seed: int) -> list[dict]:
    rng = random.Random(seed)
    ev, lu = data.events(), data.lineups()
    ids = anonymize.load()
    n, clean = CFG["track3"]["n_excerpts"], CFG["track3"]["clean_share"]
    plan = [None] * round(n * clean)
    plan += [perturb.PLANTS[i % len(perturb.PLANTS)] for i in range(n - len(plan))]
    rng.shuffle(plan)
    match_ids = list(ev.match_id.unique())
    out = []
    for k, plant in enumerate(plan):
        while True:
            mid = rng.choice(match_ids)
            m = ev[ev.match_id == mid]
            gks = lu[(lu.match_id == mid) & (lu.position == "Goalkeeper")].groupby("team").player.first().to_dict()
            ex, idx = perturb.track3_excerpt(m, gks, plant, rng)
            if ex is not None:
                break
        teams = list(dict.fromkeys(m.team.dropna()))
        tmap = {teams[0]: "Team A", teams[1]: "Team B"}
        lines = [_event_line(i + 1, r, tmap, ids["player"]) for i, r in ex.iterrows()]
        user = ("40 consecutive events from one Premier League 2015/16 match (StatsBomb format). "
                "Columns: idx | period minute:second | team | player (position) | type | detail | "
                "start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s\n\n"
                + "\n".join(lines)
                + "\n\nAt most one event has been corrupted so that it is impossible or inconsistent "
                  "with the others. Possible corruption types: " + ", ".join(perturb.PLANTS) + ".\n"
                  'Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.')
        out.append(dict(id=f"t3_{k:03d}", track=3, condition=plant or "clean", group=plant or "clean",
                        truth={"plant": plant, "index": idx, "match_id": int(mid)}, system=SYSTEM, user=user))
    return out


def _event_line(i, r, tmap, pids) -> str:
    def f(v):
        return "" if pd.isna(v) else (f"{v:.1f}" if isinstance(v, float) else str(v))
    detail = " ".join(f(r[c]) for c in ["pass_type", "pass_outcome", "shot_outcome", "duel_type",
                                        "goalkeeper_type", "pass_height"] if not pd.isna(r[c]))
    if r.type == "Substitution":
        detail = f"off, on: {pids.get(r.substitution_replacement, '?')}"
    if r.type == "Shot" and not pd.isna(r.shot_statsbomb_xg):
        detail += f" xG {r.shot_statsbomb_xg:.2f}"
    team = tmap.get(r.team, "")
    player = f"{pids.get(r.player, '')} ({r.position})" if not pd.isna(r.player) else ""
    end = f" -> {f(r.end_x)},{f(r.end_y)}" if not pd.isna(r.end_x) else ""
    return (f"{i:2d} | P{r.period} {int(r.minute):02d}:{int(r.second):02d} | {team} | {player} | "
            f"{r.type} | {detail.strip()} | {f(r.x)},{f(r.y)}{end} | {f(r.duration)}")


def build_all():
    seed = CFG["seed"]
    lu = data.lineups()
    anonymize.build(lu.player.tolist(), lu.team.tolist(), seed)
    OUT.mkdir(exist_ok=True)
    for n, fn in [(1, track1), (2, track2), (3, track3)]:
        recs = fn(seed)
        with open(OUT / f"track{n}.jsonl", "w") as f:
            for r in recs:
                f.write(json.dumps(r) + "\n")
        print(f"track {n}: {len(recs)} prompts")


def load(track: int) -> list[dict]:
    return [json.loads(l) for l in open(OUT / f"track{track}.jsonl")]


if __name__ == "__main__":
    build_all()
