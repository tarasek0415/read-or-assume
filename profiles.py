"""Per-90 summaries for players (track 1) and teams (track 2).

Every number here is computed from StatsBomb events with plain pandas; the
definitions are in the docstrings so a reader can check them.
"""
import pandas as pd

import data

GROUP = {  # StatsBomb lineup position -> position group
    "Goalkeeper": "goalkeeper",
    "Right Back": "defender", "Left Back": "defender", "Center Back": "defender",
    "Right Center Back": "defender", "Left Center Back": "defender",
    "Right Wing Back": "defender", "Left Wing Back": "defender",
    "Center Defensive Midfield": "midfielder", "Right Defensive Midfield": "midfielder",
    "Left Defensive Midfield": "midfielder", "Center Midfield": "midfielder",
    "Right Center Midfield": "midfielder", "Left Center Midfield": "midfielder",
    "Right Midfield": "midfielder", "Left Midfield": "midfielder",
    "Center Attacking Midfield": "midfielder", "Right Attacking Midfield": "midfielder",
    "Left Attacking Midfield": "midfielder",
    "Right Wing": "forward", "Left Wing": "forward", "Center Forward": "forward",
    "Right Center Forward": "forward", "Left Center Forward": "forward",
    "Secondary Striker": "forward",
}
# Positions whose stats sit between two groups; excluded from the false-label condition.
AMBIGUOUS = {"Right Wing Back", "Left Wing Back", "Center Attacking Midfield",
             "Right Attacking Midfield", "Left Attacking Midfield"}

PLAYER_STATS = ["shots", "box_touches", "key_passes", "passes", "progressive_passes",
                "tackles", "interceptions", "clearances", "aerials"]


def player_profiles(min_minutes: int = 900) -> pd.DataFrame:
    """One row per outfield player with >= min_minutes. Counts are per 90 minutes.

    box_touches: any on-ball event in the opposition box (x>=102, 18<=y<=62).
    key_passes: passes flagged shot_assist or goal_assist.
    progressive_passes: completed passes that move the ball >= 10 units toward goal.
    aerials: aerial duels won (aerial_won flag) plus aerial duels lost.
    thirds: share of the player's on-ball events in the defensive/middle/attacking third.
    """
    e = data.events()
    lu = data.lineups()
    mins = lu.groupby("player").minutes.sum()
    pos = lu.groupby(["player", "position"]).minutes.sum().reset_index()
    pos = pos.sort_values("minutes").groupby("player").last()  # position with most minutes
    team = lu.groupby("player").team.agg(lambda s: s.mode()[0])

    e = e[e.player.notna()].copy()
    completed = e.pass_outcome.isna()
    rows = []
    for name, g in e.groupby("player"):
        m = mins.get(name, 0)
        if m < min_minutes or GROUP.get(pos.loc[name, "position"]) in (None, "goalkeeper"):
            continue
        p = g[g.type == "Pass"]
        on_ball = g[g.type.isin(["Pass", "Carry", "Shot", "Dribble", "Ball Receipt*"])]
        k = 90 / m
        rows.append({
            "player": name, "team": team[name], "minutes": round(m),
            "position": pos.loc[name, "position"], "group": GROUP[pos.loc[name, "position"]],
            "shots": k * (g.type == "Shot").sum(),
            "box_touches": k * ((on_ball.x >= 102) & on_ball.y.between(18, 62)).sum(),
            "key_passes": k * (p.pass_shot_assist.fillna(False) | p.pass_goal_assist.fillna(False)).sum(),
            "passes": k * len(p),
            "progressive_passes": k * (completed.loc[p.index] & ((p.end_x - p.x) >= 10)).sum(),
            "tackles": k * (g.duel_type == "Tackle").sum(),
            "interceptions": k * (g.type == "Interception").sum(),
            "clearances": k * (g.type == "Clearance").sum(),
            "aerials": k * (g.aerial_won.fillna(False).astype(bool).sum()
                            + g.clearance_aerial_won.fillna(False).astype(bool).sum()
                            + (g.duel_type == "Aerial Lost").sum()),
            "avg_x": on_ball.x.mean(), "avg_y": on_ball.y.mean(),
            "third_def": (on_ball.x < 40).mean(), "third_mid": on_ball.x.between(40, 80).mean(),
            "third_att": (on_ball.x > 80).mean(),
        })
    return pd.DataFrame(rows).round(2)


TEAM_STATS = ["possession", "shots_for", "shots_against", "xg_for", "xg_against",
              "pressing_height", "ppda", "crosses"]


def team_profiles() -> pd.DataFrame:
    """One row per team, per 90 minutes over the whole season.

    possession: share of the team's passes among all passes in its matches.
    pressing_height: mean x of the team's Pressure events (higher = presses further up).
    ppda: opponent passes in the opponent's own 60% of the pitch divided by the team's
          tackles, interceptions and fouls in that same zone (lower = more aggressive press).
    crosses: passes flagged as crosses.
    """
    e = data.events()
    m = data.matches()
    rows = []
    for t in sorted(set(m.home_team)):
        ids = m[(m.home_team == t) | (m.away_team == t)].match_id
        g = e[e.match_id.isin(ids)]
        own, opp = g[g.team == t], g[g.team != t]
        n = len(ids)
        opp_passes = ((opp.type == "Pass") & (opp.x < 72)).sum()  # opponent's own 60%
        own_def = (own.duel_type.eq("Tackle") | own.type.isin(["Interception", "Foul Committed"])) & (own.x > 48)
        rows.append({
            "team": t, "matches": n,
            "possession": 100 * (own.type == "Pass").sum() / (g.type == "Pass").sum(),
            "shots_for": (own.type == "Shot").sum() / n, "shots_against": (opp.type == "Shot").sum() / n,
            "xg_for": own.shot_statsbomb_xg.sum() / n, "xg_against": opp.shot_statsbomb_xg.sum() / n,
            "pressing_height": own[own.type == "Pressure"].x.mean(),
            "ppda": opp_passes / max(own_def.sum(), 1),
            "crosses": own.pass_cross.fillna(False).astype(bool).sum() / n,
        })
    df = pd.DataFrame(rows).round(2)
    pts = _points(m)
    df["finish"] = df.team.map(pts.rank(ascending=False, method="first").astype(int))
    return df


def _points(m: pd.DataFrame) -> pd.Series:
    pts = {}
    for _, r in m.iterrows():
        h, a = r.home_team, r.away_team
        hs, as_ = r.home_score, r.away_score
        pts[h] = pts.get(h, 0) + (3 if hs > as_ else 1 if hs == as_ else 0)
        pts[a] = pts.get(a, 0) + (3 if as_ > hs else 1 if hs == as_ else 0)
    s = pd.Series(pts)
    # break ties on goal difference, then alphabetically (stable)
    return s + 1e-3 * _goal_diff(m)


def _goal_diff(m):
    gd = {}
    for _, r in m.iterrows():
        gd[r.home_team] = gd.get(r.home_team, 0) + r.home_score - r.away_score
        gd[r.away_team] = gd.get(r.away_team, 0) + r.away_score - r.home_score
    return pd.Series(gd)
