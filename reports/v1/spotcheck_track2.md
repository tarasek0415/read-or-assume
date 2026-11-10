# Spot-check: track 2 (80 prompts total)

System prompt for all: "You are a football data analyst. Answer with a single JSON object and nothing else: no prose, no markdown fences."

---
## t2_Chelsea_big  condition=big
**hidden truth:** `{'possession_above_avg': 'yes', 'shots_for_above_avg': 'yes', 'shots_against_below_avg': 'yes', 'xg_for_above_avg': 'yes', 'xg_against_below_avg': 'yes', 'presses_higher': 'yes', 'ppda_more_aggressive': 'yes', 'positive_xg_diff': 'yes', 'finish': 10, 'shown_name': 'Liverpool'}`

```
Premier League 2015/16 season summary for Liverpool (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 55.65  [49.84]
  shots for: 14.08  [13.04]
  shots against: 12.97  [13.04]
  xg for: 1.41  [1.28]
  xg against: 1.26  [1.28]
  pressing height: 53.63  [53.31]
  ppda: 13.81  [15.56]
  crosses: 12.08  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_Southampton_leak  condition=leak
**hidden truth:** `{'team': 'Southampton'}`

```
Premier League 2015/16 season summary for Team K (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 49.31  [49.84]
  shots for: 13.87  [13.04]
  shots against: 12.39  [13.04]
  xg for: 1.43  [1.28]
  xg against: 1.05  [1.28]
  pressing height: 54.3  [53.31]
  ppda: 14.64  [15.56]
  crosses: 15.95  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Question: which club is Team K? Answer {"team": "<club or unknown>"}.
```

---
## t2_ManchesterUnited_neutral  condition=neutral
**hidden truth:** `{'possession_above_avg': 'yes', 'shots_for_above_avg': 'no', 'shots_against_below_avg': 'yes', 'xg_for_above_avg': 'no', 'xg_against_below_avg': 'yes', 'presses_higher': 'yes', 'ppda_more_aggressive': 'yes', 'positive_xg_diff': 'yes', 'finish': 5, 'shown_name': 'Team K'}`

```
Premier League 2015/16 season summary for Team K (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 58.3  [49.84]
  shots for: 11.34  [13.04]
  shots against: 10.92  [13.04]
  xg for: 1.11  [1.28]
  xg against: 1.01  [1.28]
  pressing height: 55.26  [53.31]
  ppda: 12.21  [15.56]
  crosses: 13.71  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_Watford_small  condition=small
**hidden truth:** `{'possession_above_avg': 'no', 'shots_for_above_avg': 'no', 'shots_against_below_avg': 'no', 'xg_for_above_avg': 'no', 'xg_against_below_avg': 'no', 'presses_higher': 'no', 'ppda_more_aggressive': 'no', 'positive_xg_diff': 'no', 'finish': 13, 'shown_name': 'Aston Villa'}`

```
Premier League 2015/16 season summary for Aston Villa (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 45.05  [49.84]
  shots for: 11.84  [13.04]
  shots against: 13.5  [13.04]
  xg for: 1.16  [1.28]
  xg against: 1.41  [1.28]
  pressing height: 53.02  [53.31]
  ppda: 16.08  [15.56]
  crosses: 10.45  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_SwanseaCity_leak  condition=leak
**hidden truth:** `{'team': 'Swansea City'}`

```
Premier League 2015/16 season summary for Team K (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 52.22  [49.84]
  shots for: 11.79  [13.04]
  shots against: 13.84  [13.04]
  xg for: 1.11  [1.28]
  xg against: 1.34  [1.28]
  pressing height: 54.74  [53.31]
  ppda: 15.69  [15.56]
  crosses: 11.63  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Question: which club is Team K? Answer {"team": "<club or unknown>"}.
```

---
## t2_Sunderland_big  condition=big
**hidden truth:** `{'possession_above_avg': 'no', 'shots_for_above_avg': 'no', 'shots_against_below_avg': 'no', 'xg_for_above_avg': 'no', 'xg_against_below_avg': 'no', 'presses_higher': 'no', 'ppda_more_aggressive': 'no', 'positive_xg_diff': 'no', 'finish': 17, 'shown_name': 'Liverpool'}`

```
Premier League 2015/16 season summary for Liverpool (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 41.29  [49.84]
  shots for: 11.87  [13.04]
  shots against: 15.37  [13.04]
  xg for: 1.12  [1.28]
  xg against: 1.61  [1.28]
  pressing height: 51.09  [53.31]
  ppda: 17.59  [15.56]
  crosses: 8.66  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_LeicesterCity_small  condition=small
**hidden truth:** `{'possession_above_avg': 'no', 'shots_for_above_avg': 'yes', 'shots_against_below_avg': 'no', 'xg_for_above_avg': 'yes', 'xg_against_below_avg': 'yes', 'presses_higher': 'no', 'ppda_more_aggressive': 'no', 'positive_xg_diff': 'yes', 'finish': 1, 'shown_name': 'Watford'}`

```
Premier League 2015/16 season summary for Watford (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 42.45  [49.84]
  shots for: 13.82  [13.04]
  shots against: 13.61  [13.04]
  xg for: 1.74  [1.28]
  xg against: 1.21  [1.28]
  pressing height: 52.9  [53.31]
  ppda: 16.35  [15.56]
  crosses: 13.58  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_Southampton_big  condition=big
**hidden truth:** `{'possession_above_avg': 'no', 'shots_for_above_avg': 'yes', 'shots_against_below_avg': 'yes', 'xg_for_above_avg': 'yes', 'xg_against_below_avg': 'yes', 'presses_higher': 'yes', 'ppda_more_aggressive': 'yes', 'positive_xg_diff': 'yes', 'finish': 6, 'shown_name': 'Chelsea'}`

```
Premier League 2015/16 season summary for Chelsea (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 49.31  [49.84]
  shots for: 13.87  [13.04]
  shots against: 12.39  [13.04]
  xg for: 1.43  [1.28]
  xg against: 1.05  [1.28]
  pressing height: 54.3  [53.31]
  ppda: 14.64  [15.56]
  crosses: 15.95  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_ManchesterUnited_big  condition=big
**hidden truth:** `{'possession_above_avg': 'yes', 'shots_for_above_avg': 'no', 'shots_against_below_avg': 'yes', 'xg_for_above_avg': 'no', 'xg_against_below_avg': 'yes', 'presses_higher': 'yes', 'ppda_more_aggressive': 'yes', 'positive_xg_diff': 'yes', 'finish': 5, 'shown_name': 'Liverpool'}`

```
Premier League 2015/16 season summary for Liverpool (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 58.3  [49.84]
  shots for: 11.34  [13.04]
  shots against: 10.92  [13.04]
  xg for: 1.11  [1.28]
  xg against: 1.01  [1.28]
  pressing height: 55.26  [53.31]
  ppda: 12.21  [15.56]
  crosses: 13.71  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```

---
## t2_Arsenal_big  condition=big
**hidden truth:** `{'possession_above_avg': 'yes', 'shots_for_above_avg': 'yes', 'shots_against_below_avg': 'yes', 'xg_for_above_avg': 'yes', 'xg_against_below_avg': 'yes', 'presses_higher': 'yes', 'ppda_more_aggressive': 'yes', 'positive_xg_diff': 'yes', 'finish': 2, 'shown_name': 'Manchester City'}`

```
Premier League 2015/16 season summary for Manchester City (all numbers per 90 minutes unless stated). League average in brackets.
  possession: 57.57  [49.84]
  shots for: 15.34  [13.04]
  shots against: 12.0  [13.04]
  xg for: 1.71  [1.28]
  xg against: 0.88  [1.28]
  pressing height: 54.68  [53.31]
  ppda: 14.64  [15.56]
  crosses: 12.53  [12.56]
  (pressing height = mean x of pressure events on a 120-long pitch; PPDA = opponent passes allowed per defensive action in their own 60%)

Questions (answer each with "yes" or "no" from the numbers above):
  possession_above_avg: Is the team's possession above the league average?
  shots_for_above_avg: Does the team take more shots per 90 than the league average?
  shots_against_below_avg: Does the team concede fewer shots per 90 than the league average?
  xg_for_above_avg: Is the team's xG for per 90 above the league average?
  xg_against_below_avg: Is the team's xG against per 90 below the league average?
  presses_higher: Does the team press higher up the pitch than the league average?
  ppda_more_aggressive: Is the team's PPDA below the league average (a more aggressive press)?
  positive_xg_diff: Does the team create more xG per 90 than it concedes?
  predicted_finish: where did this team finish in the 20-team table? (integer 1-20)
Answer as one JSON object with those keys.
```
