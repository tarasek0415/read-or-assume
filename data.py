"""Load StatsBomb open data for one season and cache it locally.

Data: StatsBomb open data (https://github.com/statsbomb/open-data), used under
its non-commercial licence. Credit: StatsBomb.
"""
import warnings
from pathlib import Path

import pandas as pd
from statsbombpy import sb

warnings.filterwarnings("ignore")  # statsbombpy warns about missing credentials

CACHE = Path(__file__).parent / "cache"
COMPETITION_ID, SEASON_ID = 2, 27  # Premier League 2015/16, 380 matches
PITCH_X, PITCH_Y = 120, 80  # StatsBomb pitch units


def matches() -> pd.DataFrame:
    f = CACHE / "matches.parquet"
    if not f.exists():
        m = sb.matches(competition_id=COMPETITION_ID, season_id=SEASON_ID)
        m = m[["match_id", "match_date", "match_week", "home_team", "away_team",
               "home_score", "away_score"]].sort_values("match_id")
        m.to_parquet(f)
    return pd.read_parquet(f)


def events() -> pd.DataFrame:
    """All events of the season, one row per event, sorted by match and index."""
    f = CACHE / "events.parquet"
    if not f.exists():
        frames = []
        for i, mid in enumerate(matches().match_id, 1):
            e = sb.events(match_id=mid)
            frames.append(_flatten(e))
            if i % 20 == 0:
                print(f"downloaded {i} matches", flush=True)
        pd.concat(frames, ignore_index=True).to_parquet(f)
    return pd.read_parquet(f)


def lineups() -> pd.DataFrame:
    """One row per (match, player): team, minutes played, main position."""
    f = CACHE / "lineups.parquet"
    if not f.exists():
        rows = []
        for mid in matches().match_id:
            for team, df in sb.lineups(match_id=mid).items():
                for _, p in df.iterrows():
                    mins, by_pos = 0, {}
                    for st in p.positions:
                        start = _clock(st["from"], st["from_period"])
                        end = _clock(st["to"], st["to_period"]) if st["to"] else 95
                        mins += end - start
                        by_pos[st["position"]] = by_pos.get(st["position"], 0) + end - start
                    if mins > 0:
                        pos = max(by_pos, key=by_pos.get)
                        rows.append(dict(match_id=mid, team=team, player=p.player_name,
                                         player_id=p.player_id, minutes=mins, position=pos))
        pd.DataFrame(rows).to_parquet(f)
    return pd.read_parquet(f)


def _clock(hhmm: str, period: int) -> float:
    """Lineup clock '47:30' -> minutes as a float (period is informational)."""
    m, s = hhmm.split(":")
    return int(m) + int(s) / 60


def _flatten(e: pd.DataFrame) -> pd.DataFrame:
    """Keep the columns the tracks need; split location lists into x/y."""
    keep = ["match_id", "index", "period", "timestamp", "minute", "second", "possession",
            "possession_team", "team", "player", "player_id", "position", "type", "duration",
            "location", "pass_end_location", "carry_end_location", "pass_length", "pass_type",
            "pass_outcome", "pass_shot_assist", "pass_goal_assist", "pass_cross", "pass_height",
            "shot_outcome", "shot_statsbomb_xg", "duel_type", "duel_outcome", "foul_committed_type",
            "aerial_won", "under_pressure", "substitution_replacement", "substitution_outcome",
            "goalkeeper_type", "goalkeeper_outcome", "clearance_aerial_won", "play_pattern"]
    e = e.reindex(columns=keep)
    xy = e.location.apply(lambda v: v if isinstance(v, list) else [None, None])
    e["x"], e["y"] = [v[0] for v in xy], [v[1] for v in xy]
    end = e.pass_end_location.where(e.pass_end_location.notna(), e.carry_end_location)
    end = end.apply(lambda v: v if isinstance(v, list) else [None, None])
    e["end_x"], e["end_y"] = [v[0] for v in end], [v[1] for v in end]
    return e.drop(columns=["location", "pass_end_location", "carry_end_location"]).sort_values("index")


if __name__ == "__main__":
    print(len(matches()), "matches")
    print(len(lineups()), "lineup rows")
    print(len(events()), "events")
