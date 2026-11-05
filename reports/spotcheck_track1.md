# Spot-check: track 1 (543 prompts total)

System prompt for all: "You are a football data analyst. Answer with a single JSON object and nothing else: no prose, no markdown fences."

---
## t1_P519_false  condition=false
**hidden truth:** `{'position': 'defender', 'label': 'forward'}`

```
Premier League 2015/16, outfield player, 1147 minutes played. Per 90 minutes:
  shots: 0.16
  box touches: 1.25
  key passes: 0.86
  passes: 65.81
  progressive passes: 15.77
  tackles: 2.35
  interceptions: 3.29
  clearances: 3.45
  aerials: 1.1
  average position: x=63.87, y=10.85 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.17/0.57/0.26

The club's squad list has this player as a forward.

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P401_leak  condition=leak
**hidden truth:** `{'player': 'Michail Antonio', 'team': 'West Ham United'}`

```
Premier League 2015/16, outfield player, 2148 minutes played. Per 90 minutes:
  shots: 2.35
  box touches: 7.84
  key passes: 0.92
  passes: 29.67
  progressive passes: 4.61
  tackles: 2.1
  interceptions: 2.14
  clearances: 2.51
  aerials: 3.02
  average position: x=74.3, y=57.8 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.14/0.38/0.48

Question: who is this player? Answer {"player": "<full name or unknown>", "team": "<club or unknown>"}.
```

---
## t1_P015_none  condition=none
**hidden truth:** `{'position': 'midfielder', 'label': None}`

```
Premier League 2015/16, outfield player, 3263 minutes played. Per 90 minutes:
  shots: 0.77
  box touches: 1.54
  key passes: 1.24
  passes: 48.38
  progressive passes: 12.85
  tackles: 2.92
  interceptions: 1.74
  clearances: 2.76
  aerials: 1.21
  average position: x=59.85, y=42.28 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.18/0.64/0.18

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P311_true  condition=true
**hidden truth:** `{'position': 'forward', 'label': 'forward'}`

```
Premier League 2015/16, outfield player, 1596 minutes played. Per 90 minutes:
  shots: 3.16
  box touches: 10.99
  key passes: 0.68
  passes: 42.34
  progressive passes: 4.34
  tackles: 0.68
  interceptions: 0.45
  clearances: 0.56
  aerials: 1.47
  average position: x=82.89, y=17.89 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.03/0.37/0.59

The club's squad list has this player as a forward.

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P096_true  condition=true
**hidden truth:** `{'position': 'defender', 'label': 'defender'}`

```
Premier League 2015/16, outfield player, 1479 minutes played. Per 90 minutes:
  shots: 1.52
  box touches: 5.66
  key passes: 1.03
  passes: 33.9
  progressive passes: 6.88
  tackles: 2.86
  interceptions: 0.79
  clearances: 1.77
  aerials: 1.95
  average position: x=70.76, y=18.11 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.15/0.44/0.4

The club's squad list has this player as a defender.

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P381_none  condition=none
**hidden truth:** `{'position': 'midfielder', 'label': None}`

```
Premier League 2015/16, outfield player, 2976 minutes played. Per 90 minutes:
  shots: 0.48
  box touches: 0.51
  key passes: 1.06
  passes: 48.35
  progressive passes: 9.86
  tackles: 2.09
  interceptions: 1.27
  clearances: 2.72
  aerials: 2.15
  average position: x=59.18, y=36.24 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.18/0.67/0.15

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P348_false  condition=false
**hidden truth:** `{'position': 'defender', 'label': 'forward'}`

```
Premier League 2015/16, outfield player, 3420 minutes played. Per 90 minutes:
  shots: 0.42
  box touches: 1.68
  key passes: 0.29
  passes: 49.58
  progressive passes: 16.55
  tackles: 1.87
  interceptions: 1.82
  clearances: 8.53
  aerials: 3.42
  average position: x=44.18, y=25.65 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.43/0.54/0.03

The club's squad list has this player as a forward.

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P113_none  condition=none
**hidden truth:** `{'position': 'defender', 'label': None}`

```
Premier League 2015/16, outfield player, 1913 minutes played. Per 90 minutes:
  shots: 0.56
  box touches: 2.45
  key passes: 0.05
  passes: 50.53
  progressive passes: 14.58
  tackles: 2.12
  interceptions: 2.12
  clearances: 6.4
  aerials: 3.25
  average position: x=43.8, y=47.5 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.4/0.57/0.03

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P359_true  condition=true
**hidden truth:** `{'position': 'defender', 'label': 'defender'}`

```
Premier League 2015/16, outfield player, 2240 minutes played. Per 90 minutes:
  shots: 0.6
  box touches: 2.89
  key passes: 0.56
  passes: 51.2
  progressive passes: 8.56
  tackles: 2.69
  interceptions: 1.09
  clearances: 1.97
  aerials: 2.21
  average position: x=65.46, y=66.57 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.17/0.51/0.32

The club's squad list has this player as a defender.

Question: judging from the data, which position group does this player play? Answer {"position": "defender" | "midfielder" | "forward"}.
```

---
## t1_P187_leak  condition=leak
**hidden truth:** `{'player': 'Jonjo Shelvey', 'team': 'Swansea City'}`

```
Premier League 2015/16, outfield player, 2378 minutes played. Per 90 minutes:
  shots: 2.16
  box touches: 1.4
  key passes: 1.63
  passes: 60.29
  progressive passes: 14.61
  tackles: 1.48
  interceptions: 1.44
  clearances: 0.91
  aerials: 1.02
  average position: x=60.91, y=39.85 (pitch 120x80, attacking left to right)
  share of on-ball actions in defensive/middle/attacking third: 0.14/0.68/0.18

Question: who is this player? Answer {"player": "<full name or unknown>", "team": "<club or unknown>"}.
```
