"""One deliberate change per track. Everything else in the prompt stays real.

track1: the position label shown next to a player profile (none / true / false).
track2: the club name shown next to a team profile (neutral / big club / small club).
track3: one planted impossibility inside 40 consecutive real events (or none).
"""
import random

import pandas as pd

# ---- track 1: position labels -------------------------------------------------
TWO_AWAY = {"defender": "forward", "forward": "defender"}  # midfielders have no group two away


def track1_label(group: str, condition: str) -> str | None:
    if condition == "none":
        return None
    if condition == "true":
        return group
    return TWO_AWAY[group]  # condition == "false"


# ---- track 2: club names -----------------------------------------------------
BIG = ["Manchester City", "Manchester United", "Chelsea", "Arsenal", "Liverpool"]
SMALL = ["AFC Bournemouth", "Watford", "Norwich City", "Aston Villa", "Sunderland"]


def track2_name(team: str, condition: str, rng: random.Random) -> str:
    if condition == "neutral":
        return "Team K"
    pool = [t for t in (BIG if condition == "big" else SMALL) if t != team]
    return rng.choice(pool)


# ---- track 3: planted data errors ------------------------------------------
PLANTS = ["goal_no_shot", "fast_long_pass", "keeper_corner", "wrong_team",
          "time_impossible", "sub_before_entry", "deleted_goal"]
FOOTBALL_SENSE = {"goal_no_shot", "deleted_goal"}  # the rest are checkable by a rule
WINDOW = 40


def track3_excerpt(ev: pd.DataFrame, gks: dict, plant: str | None, rng: random.Random):
    """Return (40-row excerpt, 1-based index of the planted row or None).

    ev: all events of one match, in order. gks: team -> goalkeeper name.
    Windows are chosen so the plant is possible (e.g. a corner exists for keeper_corner).
    """
    ev = ev.reset_index(drop=True)
    anchor = _anchor(ev, plant, rng)
    if anchor is None:
        return None, None
    start = max(0, min(anchor - rng.randint(8, 20), len(ev) - WINDOW - 2))
    ex = ev.iloc[start:start + WINDOW + 2].copy().reset_index(drop=True)  # 2 spare rows
    i = anchor - start
    teams = list(dict.fromkeys(ev.team.dropna()))
    other = {teams[0]: teams[1], teams[1]: teams[0]}

    if plant == "goal_no_shot":  # a keeper concedes a goal nobody shot
        ex.loc[i, ["type", "goalkeeper_type", "team"]] = ["Goal Keeper", "Goal Conceded", other[ex.team[i]]]
        ex.loc[i, ["player", "position"]] = [gks[ex.team[i]], "Goalkeeper"]
        ex.loc[i, ["x", "y"]] = [2.0, 40.0]  # keeper events are logged in the keeper's own frame
        ex.loc[i, ["end_x", "end_y", "duration", "pass_type", "pass_outcome", "pass_height",
                   "pass_length", "shot_outcome", "duel_type"]] = [None] * 9
    elif plant == "fast_long_pass":  # 65 units in half a second
        ex.loc[i, "end_x"] = ex.x[i] + 65 if ex.x[i] < 55 else ex.x[i] - 65
        ex.loc[i, ["duration", "pass_length"]] = [0.5, 65.0]
    elif plant == "keeper_corner":
        ex.loc[i, ["player", "position"]] = [gks[ex.team[i]], "Goalkeeper"]
    elif plant == "wrong_team":  # same player, other team
        ex.loc[i, "team"] = other[ex.team[i]]
    elif plant == "time_impossible":  # minute beyond any half
        ex.loc[i, "minute"] = max(ex.minute[i] + 60, 106 if ex.period[i] == 2 else 0)
    elif plant == "sub_before_entry":  # replacement acts before the substitution event
        sub = ex.index[(ex.type == "Substitution") & (ex.index > i)][0]
        ex.loc[i, "player"] = ex.substitution_replacement[sub]
    elif plant == "deleted_goal":  # drop the goal and the keeper's goal-conceded event
        drop = [i] + [j for j in (i + 1, i + 2) if ex.type[j] == "Goal Keeper"]
        ex = ex.drop(drop).reset_index(drop=True)
    ex = ex.iloc[:WINDOW].reset_index(drop=True)
    return ex, (None if plant is None else i + 1)


def _anchor(ev, plant, rng):
    """Row index the plant is applied to (or the window centre for clean excerpts)."""
    mid = ev.index[(ev.index > 30) & (ev.index < len(ev) - 50)]
    if plant is None or plant == "time_impossible":
        return rng.choice(list(mid))
    if plant == "goal_no_shot":
        ok = [i for i in mid if ev.type[i] in ("Pass", "Carry")
              and not (ev.type[i - 8:i] == "Shot").any()]
    elif plant == "fast_long_pass":
        ok = [i for i in mid if ev.type[i] == "Pass" and pd.isna(ev.pass_outcome[i])
              and pd.isna(ev.pass_type[i])]
    elif plant == "keeper_corner":
        ok = [i for i in mid if ev.pass_type[i] == "Corner"]
    elif plant == "wrong_team":
        ok = [i for i in mid if ev.type[i] == "Pass"
              and (ev.player[i - 10:i + 10] == ev.player[i]).sum() > 1]
    elif plant == "sub_before_entry":
        subs = [j for j in mid if ev.type[j] == "Substitution"]
        ok = [i for j in subs for i in range(j - 15, j - 2)
              if ev.team[i] == ev.team[j] and ev.type[i] in ("Pass", "Carry", "Ball Receipt*")]
    elif plant == "deleted_goal":
        ok = [i for i in mid if ev.shot_outcome[i] == "Goal"]
    return rng.choice(ok) if ok else None
