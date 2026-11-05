# Spot-check: track 3 (300 prompts total)

System prompt for all: "You are a football data analyst. Answer with a single JSON object and nothing else: no prose, no markdown fences."

---
## t3_263  condition=clean
**hidden truth:** `{'plant': None, 'index': None, 'match_id': 3754237}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 53:36 | Team B | P539 (Left Center Midfield) | Carry |  | 55.7,16.9 -> 54.8,16.2 | 0.5
 2 | P2 53:37 | Team B | P539 (Left Center Midfield) | Pass | Ground Pass | 54.8,16.2 -> 56.6,10.7 | 1.0
 3 | P2 53:38 | Team B | P374 (Right Midfield) | Ball Receipt* |  | 56.6,10.7 | 
 4 | P2 53:38 | Team B | P374 (Right Midfield) | Carry |  | 56.6,10.7 -> 61.0,8.3 | 0.1
 5 | P2 53:38 | Team B | P374 (Right Midfield) | Pass | Ground Pass | 61.0,8.3 -> 69.5,13.4 | 0.5
 6 | P2 53:38 | Team B | P030 (Center Defensive Midfield) | Ball Receipt* |  | 69.5,13.4 | 
 7 | P2 53:38 | Team B | P030 (Center Defensive Midfield) | Carry |  | 69.5,13.4 -> 69.5,13.4 | 0.1
 8 | P2 53:39 | Team B | P030 (Center Defensive Midfield) | Pass | Ground Pass | 69.5,13.4 -> 55.5,16.2 | 0.7
 9 | P2 53:39 | Team B | P539 (Left Center Midfield) | Ball Receipt* |  | 55.5,16.2 | 
10 | P2 53:39 | Team B | P539 (Left Center Midfield) | Carry |  | 55.5,16.2 -> 55.5,16.2 | 0.1
11 | P2 53:39 | Team B | P539 (Left Center Midfield) | Pass | Incomplete Low Pass | 55.5,16.2 -> 63.1,15.1 | 0.2
12 | P2 53:39 | Team B | P374 (Right Midfield) | Block |  | 63.1,15.1 | 0.0
13 | P2 53:40 | Team A | P479 (Left Center Midfield) | Pressure |  | 58.8,62.7 | 0.5
14 | P2 53:41 | Team B | P539 (Left Center Midfield) | Pass | Recovery Low Pass | 61.3,15.3 -> 68.6,9.5 | 0.8
15 | P2 53:41 | Team B | P030 (Center Defensive Midfield) | Ball Receipt* |  | 68.6,9.5 | 
16 | P2 53:41 | Team B | P030 (Center Defensive Midfield) | Carry |  | 68.6,9.5 -> 70.5,10.7 | 1.5
17 | P2 53:42 | Team A | P527 (Right Back) | Pressure |  | 49.6,70.6 | 0.7
18 | P2 53:43 | Team B | P030 (Center Defensive Midfield) | Dispossessed |  | 70.5,10.7 | 0.0
19 | P2 53:43 | Team A | P527 (Right Back) | Duel | Tackle | 49.6,69.4 | 0.0
20 | P2 53:44 | Team A | P479 (Left Center Midfield) | Ball Recovery |  | 53.1,69.7 | 0.0
21 | P2 53:44 | Team A | P479 (Left Center Midfield) | Carry |  | 53.1,69.7 -> 59.1,70.6 | 0.9
22 | P2 53:45 | Team A | P479 (Left Center Midfield) | Pass | High Pass | 59.1,70.6 -> 102.4,70.8 | 3.5
23 | P2 53:48 | Team B | P310 (Left Center Back) | Pressure |  | 18.6,11.3 | 0.7
24 | P2 53:48 | Team A | P075 (Left Center Forward) | Ball Receipt* |  | 102.4,70.8 | 
25 | P2 53:48 | Team A | P075 (Left Center Forward) | Carry |  | 102.4,70.8 -> 104.5,71.1 | 0.4
26 | P2 53:49 | Team A | P075 (Left Center Forward) | Dribble |  | 104.5,71.1 | 0.0
27 | P2 53:49 | Team B | P310 (Left Center Back) | Duel | Tackle | 15.6,9.0 | 0.0
28 | P2 53:49 | Team B | P310 (Left Center Back) | Carry |  | 15.6,9.0 -> 6.2,6.9 | 3.0
29 | P2 53:50 | Team A | P075 (Left Center Forward) | Pressure |  | 106.8,78.2 | 1.5
30 | P2 53:52 | Team B | P310 (Left Center Back) | Pass | Low Pass | 6.2,6.9 -> 19.5,3.1 | 1.2
31 | P2 53:53 | Team B | P125 (Left Back) | Ball Receipt* |  | 19.5,3.1 | 
32 | P2 53:53 | Team B | P125 (Left Back) | Carry |  | 19.5,3.1 -> 17.0,2.2 | 0.9
33 | P2 53:54 | Team B | P125 (Left Back) | Pass | Ground Pass | 17.0,2.2 -> 4.8,13.4 | 1.6
34 | P2 53:54 | Team A | P151 (Left Midfield) | Pressure |  | 99.8,76.4 | 0.5
35 | P2 53:55 | Team B | P310 (Left Center Back) | Ball Receipt* |  | 4.8,13.4 | 
36 | P2 53:55 | Team B | P310 (Left Center Back) | Carry |  | 4.8,13.4 -> 5.4,12.1 | 0.9
37 | P2 53:56 | Team A | P075 (Left Center Forward) | Pressure |  | 113.0,69.7 | 0.5
38 | P2 53:56 | Team B | P310 (Left Center Back) | Pass | Low Pass | 5.4,12.1 -> 23.5,21.5 | 1.0
39 | P2 53:57 | Team B | P539 (Left Center Midfield) | Ball Receipt* |  | 23.5,21.5 | 
40 | P2 53:57 | Team B | P539 (Left Center Midfield) | Carry |  | 23.5,21.5 -> 21.2,18.3 | 2.4

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_239  condition=deleted_goal
**hidden truth:** `{'plant': 'deleted_goal', 'index': 12, 'match_id': 3754302}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 90:42 | Team A | P490 (Goalkeeper) | Pass | Incomplete High Pass | 11.4,42.5 -> 61.5,17.4 | 1.6
 2 | P2 90:43 | Team B | P479 (Right Center Midfield) | Pass | Recovery Low Pass | 58.6,62.7 -> 72.2,63.1 | 0.9
 3 | P2 90:44 | Team B | P224 (Left Midfield) | Ball Receipt* |  | 72.2,63.1 | 
 4 | P2 90:44 | Team B | P224 (Left Midfield) | Carry |  | 72.2,63.1 -> 75.6,57.6 | 1.8
 5 | P2 90:44 | Team A | P153 (Right Defensive Midfield) | Pressure |  | 50.0,17.6 | 1.4
 6 | P2 90:46 | Team B | P224 (Left Midfield) | Pass | Low Pass | 75.6,57.6 -> 81.9,56.5 | 0.7
 7 | P2 90:47 | Team B | P151 (Right Center Forward) | Ball Receipt* |  | 81.9,56.5 | 
 8 | P2 90:47 | Team B | P151 (Right Center Forward) | Carry |  | 81.9,56.5 -> 85.5,52.8 | 1.6
 9 | P2 90:48 | Team B | P151 (Right Center Forward) | Pass | Ground Pass | 85.5,52.8 -> 108.7,51.6 | 0.6
10 | P2 90:49 | Team B | P075 (Left Center Forward) | Ball Receipt* |  | 108.7,51.6 | 
11 | P2 90:49 | Team B | P075 (Left Center Forward) | Carry |  | 108.7,51.6 -> 107.3,45.8 | 1.6
12 | P2 92:08 | Team A | P008 (Center Forward) | Pass | Kick Off Ground Pass | 60.0,40.0 -> 31.1,26.4 | 1.5
13 | P2 92:09 | Team A | P462 (Left Center Back) | Ball Receipt* |  | 31.1,26.4 | 
14 | P2 92:10 | Team A | P462 (Left Center Back) | Pass | High Pass | 30.0,27.5 -> 71.6,40.4 | 0.7
15 | P2 92:11 | Team A | P008 (Center Forward) | Ball Receipt* |  | 71.6,40.4 | 
16 | P2 92:11 | Team A | P008 (Center Forward) | Pass | High Pass | 71.6,40.4 -> 56.9,33.0 | 1.5
17 | P2 92:12 | Team A | P153 (Right Defensive Midfield) | Ball Receipt* |  | 56.9,33.0 | 
18 | P2 92:12 | Team B | P151 (Right Center Forward) | Duel | Aerial Lost | 63.2,47.1 | 0.0
19 | P2 92:12 | Team A | P153 (Right Defensive Midfield) | Pass | High Pass | 56.9,33.0 -> 56.6,39.0 | 2.3
20 | P2 92:15 | Team A | P416 (Left Defensive Midfield) | Ball Receipt* |  | 56.6,39.0 | 
21 | P2 92:15 | Team B | P151 (Right Center Forward) | Duel | Aerial Lost | 63.5,41.1 | 0.0
22 | P2 92:15 | Team A | P416 (Left Defensive Midfield) | Pass | Low Pass | 56.6,39.0 -> 61.5,30.3 | 0.8
23 | P2 92:15 | Team A | P382 (Left Midfield) | Ball Receipt* |  | 61.5,30.3 | 
24 | P2 92:15 | Team A | P382 (Left Midfield) | Carry |  | 61.5,30.3 -> 61.5,30.3 | 0.0
25 | P2 92:15 | Team A | P382 (Left Midfield) | Pass | High Pass | 61.5,30.3 -> 68.6,30.3 | 1.0
26 | P2 92:16 | Team A | P006 (Right Midfield) | Ball Receipt* |  | 68.6,30.3 | 
27 | P2 92:16 | Team A | P006 (Right Midfield) | Carry |  | 68.6,30.3 -> 68.1,30.3 | 0.7
28 | P2 92:17 | Team B | P517 (Left Center Midfield) | Pressure |  | 52.0,47.7 | 0.7
29 | P2 92:17 | Team A | P006 (Right Midfield) | Pass | Ground Pass | 68.1,30.3 -> 69.7,29.4 | 0.5
30 | P2 92:18 | Team A | P008 (Center Forward) | Ball Receipt* |  | 69.7,29.4 | 
31 | P2 92:18 | Team A | P008 (Center Forward) | Carry |  | 69.7,29.4 -> 71.6,25.7 | 1.9
32 | P2 92:18 | Team B | P345 (Right Center Back) | Block |  | 49.2,52.8 | 0.0
33 | P2 92:19 | Team A | P008 (Center Forward) | Dispossessed |  | 71.6,25.7 | 0.0
34 | P2 92:19 | Team B | P345 (Right Center Back) | Duel | Tackle | 48.5,54.4 | 0.0
35 | P2 92:21 | Team B | P517 (Left Center Midfield) | Ball Recovery |  | 50.4,51.6 | 0.0
36 | P2 92:21 | Team B | P517 (Left Center Midfield) | Carry |  | 50.4,51.6 -> 58.6,61.5 | 2.4
37 | P2 92:23 | Team B | P517 (Left Center Midfield) | Pass | Ground Pass | 58.6,61.5 -> 65.5,77.9 | 1.4
38 | P2 92:24 | Team B | P151 (Right Center Forward) | Ball Receipt* |  | 65.5,77.9 | 
39 | P2 92:24 | Team B | P151 (Right Center Forward) | Carry |  | 65.5,77.9 -> 77.3,54.9 | 8.5
40 | P2 92:29 | Team A | P416 (Left Defensive Midfield) | Pressure |  | 38.2,16.3 | 3.5

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_034  condition=fast_long_pass
**hidden truth:** `{'plant': 'fast_long_pass', 'index': 19, 'match_id': 3753992}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 52:39 | Team A | P268 (Right Wing) | Ball Receipt* |  | 88.2,65.4 | 
 2 | P2 52:39 | Team A | P268 (Right Wing) | Carry |  | 88.2,65.4 -> 87.4,59.3 | 2.7
 3 | P2 52:42 | Team A | P268 (Right Wing) | Pass | Ground Pass | 87.4,59.3 -> 78.3,38.7 | 1.2
 4 | P2 52:43 | Team A | P188 (Left Defensive Midfield) | Ball Receipt* |  | 78.3,38.7 | 
 5 | P2 52:43 | Team A | P188 (Left Defensive Midfield) | Carry |  | 78.3,38.7 -> 78.3,38.7 | 1.3
 6 | P2 52:44 | Team A | P188 (Left Defensive Midfield) | Pass | Ground Pass | 78.3,38.7 -> 91.5,33.0 | 0.7
 7 | P2 52:45 | Team B | P006 (Right Wing) | Pressure |  | 31.0,50.1 | 0.3
 8 | P2 52:45 | Team A | P330 (Left Wing) | Ball Receipt* |  | 91.5,33.0 | 
 9 | P2 52:45 | Team A | P330 (Left Wing) | Carry |  | 91.5,33.0 -> 90.9,32.4 | 0.1
10 | P2 52:45 | Team A | P330 (Left Wing) | Pass | Ground Pass | 90.9,32.4 -> 85.8,42.1 | 0.7
11 | P2 52:46 | Team A | P268 (Right Wing) | Ball Receipt* |  | 85.8,42.1 | 
12 | P2 52:46 | Team A | P268 (Right Wing) | Carry |  | 85.8,42.1 -> 84.5,41.9 | 0.9
13 | P2 52:47 | Team A | P268 (Right Wing) | Pass | Ground Pass | 84.5,41.9 -> 83.4,23.8 | 1.3
14 | P2 52:48 | Team A | P188 (Left Defensive Midfield) | Ball Receipt* |  | 83.4,23.8 | 
15 | P2 52:48 | Team A | P188 (Left Defensive Midfield) | Carry |  | 83.4,23.8 -> 83.4,23.8 | 1.1
16 | P2 52:49 | Team A | P188 (Left Defensive Midfield) | Pass | Ground Pass | 83.4,23.8 -> 96.0,5.7 | 1.3
17 | P2 52:50 | Team A | P212 (Left Back) | Ball Receipt* |  | 96.0,5.7 | 
18 | P2 52:50 | Team A | P212 (Left Back) | Carry |  | 96.0,5.7 -> 96.0,5.5 | 2.3
19 | P2 52:53 | Team A | P212 (Left Back) | Pass | Ground Pass | 96.0,5.5 -> 31.0,13.9 | 0.5
20 | P2 52:54 | Team A | P188 (Left Defensive Midfield) | Ball Receipt* |  | 107.8,13.9 | 
21 | P2 52:54 | Team A | P188 (Left Defensive Midfield) | Carry |  | 107.8,13.9 -> 109.8,12.0 | 0.9
22 | P2 52:55 | Team A | P188 (Left Defensive Midfield) | Pass | High Pass | 109.8,12.0 -> 111.2,76.1 | 5.4
23 | P2 53:00 | Team A | P037 (Right Back) | Ball Receipt* |  | 111.2,76.1 | 
24 | P2 53:00 | Team A | P037 (Right Back) | Carry |  | 111.2,76.1 -> 111.2,76.1 | 1.4
25 | P2 53:02 | Team A | P037 (Right Back) | Pass | Ground Pass | 111.2,76.1 -> 108.2,69.0 | 1.0
26 | P2 53:02 | Team B | P544 (Left Wing) | Pressure |  | 11.1,14.3 | 1.8
27 | P2 53:03 | Team A | P017 (Center Attacking Midfield) | Ball Receipt* |  | 108.2,69.0 | 
28 | P2 53:03 | Team A | P017 (Center Attacking Midfield) | Carry |  | 108.2,69.0 -> 109.0,68.8 | 1.2
29 | P2 53:04 | Team A | P017 (Center Attacking Midfield) | Pass | Ground Pass | 109.0,68.8 -> 112.9,76.1 | 1.3
30 | P2 53:05 | Team A | P037 (Right Back) | Ball Receipt* |  | 112.9,76.1 | 
31 | P2 53:05 | Team A | P037 (Right Back) | Carry |  | 112.9,76.1 -> 112.9,76.1 | 0.1
32 | P2 53:05 | Team A | P037 (Right Back) | Pass | Ground Pass | 112.9,76.1 -> 93.9,68.6 | 1.4
33 | P2 53:07 | Team A | P031 (Right Defensive Midfield) | Ball Receipt* |  | 93.9,68.6 | 
34 | P2 53:07 | Team A | P031 (Right Defensive Midfield) | Carry |  | 93.9,68.6 -> 93.9,68.6 | 1.0
35 | P2 53:08 | Team A | P031 (Right Defensive Midfield) | Pass | Ground Pass | 93.9,68.6 -> 88.9,50.5 | 1.2
36 | P2 53:09 | Team A | P268 (Right Wing) | Ball Receipt* |  | 88.9,50.5 | 
37 | P2 53:09 | Team A | P268 (Right Wing) | Carry |  | 88.9,50.5 -> 88.9,50.5 | 0.6
38 | P2 53:09 | Team A | P268 (Right Wing) | Pass | Ground Pass | 88.9,50.5 -> 98.8,54.4 | 0.8
39 | P2 53:10 | Team A | P017 (Center Attacking Midfield) | Ball Receipt* |  | 98.8,54.4 | 
40 | P2 53:10 | Team A | P017 (Center Attacking Midfield) | Carry |  | 98.8,54.4 -> 98.8,54.4 | 0.1

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_115  condition=goal_no_shot
**hidden truth:** `{'plant': 'goal_no_shot', 'index': 12, 'match_id': 3754009}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P1 09:32 | Team A | P528 (Right Back) | Miscontrol |  | 37.6,75.9 | 0.0
 2 | P1 09:33 | Team B | P180 (Left Center Forward) | Ball Recovery |  | 88.6,14.6 | 0.0
 3 | P1 09:33 | Team B | P180 (Left Center Forward) | Carry |  | 88.6,14.6 -> 89.6,16.5 | 1.0
 4 | P1 09:34 | Team A | P113 (Right Center Back) | Pressure |  | 28.8,63.8 | 0.6
 5 | P1 09:34 | Team B | P180 (Left Center Forward) | Dribble |  | 89.6,16.5 | 0.0
 6 | P1 09:34 | Team A | P113 (Right Center Back) | Duel | Tackle | 30.5,63.6 | 0.0
 7 | P1 09:35 | Team B | P180 (Left Center Forward) | Pressure |  | 82.3,16.2 | 1.8
 8 | P1 09:36 | Team A | P266 (Left Defensive Midfield) | Ball Recovery |  | 41.2,66.5 | 0.0
 9 | P1 09:36 | Team A | P266 (Left Defensive Midfield) | Carry |  | 41.2,66.5 -> 43.8,68.1 | 1.1
10 | P1 09:37 | Team B | P180 (Left Center Forward) | Foul Committed |  | 76.3,12.0 | 0.0
11 | P1 09:37 | Team A | P266 (Left Defensive Midfield) | Foul Won |  | 43.8,68.1 | 0.0
12 | P1 09:37 | Team B | P281 (Goalkeeper) | Goal Keeper | Goal Conceded | 2.0,40.0 | 
13 | P1 09:37 | Team A | P266 (Left Defensive Midfield) | Pass | Ground Pass | 45.6,70.9 -> 56.8,65.0 | 1.0
14 | P1 09:38 | Team A | P243 (Center Attacking Midfield) | Ball Receipt* |  | 56.8,65.0 | 
15 | P1 09:38 | Team A | P243 (Center Attacking Midfield) | Carry |  | 56.8,65.0 -> 67.6,62.2 | 1.9
16 | P1 09:40 | Team A | P243 (Center Attacking Midfield) | Pass | Ground Pass | 67.6,62.2 -> 92.4,72.9 | 2.0
17 | P1 09:42 | Team A | P072 (Right Wing) | Ball Receipt* |  | 92.4,72.9 | 
18 | P1 09:42 | Team A | P072 (Right Wing) | Carry |  | 92.4,72.9 -> 107.3,74.2 | 5.5
19 | P1 09:43 | Team B | P270 (Left Back) | Pressure |  | 25.3,11.5 | 3.5
20 | P1 09:48 | Team A | P072 (Right Wing) | Pass | Ground Pass | 107.3,74.2 -> 98.8,69.0 | 1.4
21 | P1 09:49 | Team A | P528 (Right Back) | Ball Receipt* |  | 98.8,69.0 | 
22 | P1 09:49 | Team A | P528 (Right Back) | Pass | Ground Pass | 98.8,68.8 -> 101.5,76.8 | 0.8
23 | P1 09:50 | Team A | P072 (Right Wing) | Ball Receipt* |  | 101.5,76.8 | 
24 | P1 09:50 | Team A | P072 (Right Wing) | Carry |  | 101.5,76.8 -> 101.5,76.8 | 0.9
25 | P1 09:51 | Team A | P072 (Right Wing) | Pass | Ground Pass | 101.5,76.8 -> 88.4,67.1 | 1.3
26 | P1 09:52 | Team A | P243 (Center Attacking Midfield) | Ball Receipt* |  | 88.4,67.1 | 
27 | P1 09:52 | Team A | P243 (Center Attacking Midfield) | Carry |  | 88.4,67.1 -> 80.7,69.1 | 3.7
28 | P1 09:56 | Team A | P243 (Center Attacking Midfield) | Pass | Incomplete Ground Pass | 80.7,69.1 -> 84.4,66.9 | 0.2
29 | P1 09:56 | Team A | P173 (Right Defensive Midfield) | Ball Receipt* |  | 95.6,61.2 | 
30 | P1 09:56 | Team B | P146 (Left Defensive Midfield) | Block |  | 35.7,13.2 | 0.0
31 | P1 09:57 | Team A | P243 (Center Attacking Midfield) | Ball Recovery |  | 82.0,63.6 | 0.0
32 | P1 09:57 | Team A | P243 (Center Attacking Midfield) | Carry |  | 82.0,63.6 -> 83.0,61.9 | 0.6
33 | P1 09:58 | Team B | P146 (Left Defensive Midfield) | Pressure |  | 35.2,15.6 | 0.4
34 | P1 09:58 | Team A | P243 (Center Attacking Midfield) | Pass | High Pass | 83.0,61.9 -> 88.0,60.1 | 1.4
35 | P1 10:00 | Team A | P173 (Right Defensive Midfield) | Ball Receipt* |  | 88.0,60.1 | 
36 | P1 10:00 | Team B | P350 (Left Midfield) | Duel | Aerial Lost | 32.1,19.8 | 0.0
37 | P1 10:00 | Team A | P173 (Right Defensive Midfield) | Pass | Low Pass | 88.0,60.3 -> 92.9,73.1 | 1.6
38 | P1 10:01 | Team A | P072 (Right Wing) | Ball Receipt* |  | 92.9,73.1 | 
39 | P1 10:01 | Team A | P072 (Right Wing) | Carry |  | 92.9,73.1 -> 89.2,74.9 | 2.7
40 | P1 10:02 | Team B | P350 (Left Midfield) | Pressure |  | 27.6,11.0 | 1.3

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_250  condition=keeper_corner
**hidden truth:** `{'plant': 'keeper_corner', 'index': 18, 'match_id': 3754165}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 49:49 | Team A | P065 (Left Center Back) | Ball Receipt* |  | 35.4,8.3 | 
 2 | P2 49:49 | Team A | P065 (Left Center Back) | Carry |  | 35.4,8.3 -> 35.4,8.3 | 0.2
 3 | P2 49:49 | Team A | P065 (Left Center Back) | Pass | Incomplete Ground Pass | 35.4,8.3 -> 62.6,18.5 | 1.3
 4 | P2 49:50 | Team A | P229 (Left Midfield) | Ball Receipt* |  | 62.8,19.9 | 
 5 | P2 49:50 | Team B | P358 (Right Back) | Pass | Interception Low Pass | 57.5,61.6 -> 70.6,68.5 | 1.9
 6 | P2 49:52 | Team B | P517 (Right Center Midfield) | Ball Receipt* |  | 70.6,68.5 | 
 7 | P2 49:52 | Team B | P517 (Right Center Midfield) | Carry |  | 70.6,68.5 -> 70.6,68.5 | 0.0
 8 | P2 49:52 | Team B | P517 (Right Center Midfield) | Pass | Ground Pass | 70.6,68.5 -> 65.4,58.7 | 1.3
 9 | P2 49:53 | Team A | P065 (Left Center Back) | Pressure |  | 50.6,20.1 | 0.5
10 | P2 49:54 | Team B | P151 (Right Midfield) | Ball Receipt* |  | 65.4,58.7 | 
11 | P2 49:54 | Team B | P151 (Right Midfield) | Pass | High Pass | 66.0,58.3 -> 101.8,58.7 | 2.6
12 | P2 49:56 | Team B | P358 (Right Back) | Ball Receipt* |  | 101.8,58.7 | 
13 | P2 49:56 | Team B | P358 (Right Back) | Carry |  | 101.8,58.7 -> 110.6,58.7 | 1.4
14 | P2 49:57 | Team A | P038 (Center Defensive Midfield) | Pressure |  | 14.1,24.1 | 0.7
15 | P2 49:58 | Team B | P358 (Right Back) | Pass | Incomplete Ground Pass | 110.6,58.7 -> 110.4,56.2 | 0.1
16 | P2 49:58 | Team B | P036 (Right Center Forward) | Ball Receipt* |  | 112.4,47.7 | 
17 | P2 49:58 | Team A | P038 (Center Defensive Midfield) | Block |  | 9.7,23.9 | 0.0
18 | P2 50:36 | Team B | P368 (Goalkeeper) | Pass | Corner High Pass | 120.0,0.1 -> 115.1,39.6 | 1.3
19 | P2 50:37 | Team B | P316 (Left Center Forward) | Ball Receipt* |  | 115.1,39.6 | 
20 | P2 50:37 | Team A | P061 (Left Center Midfield) | Duel | Aerial Lost | 6.5,44.3 | 0.0
21 | P2 50:37 | Team B | P316 (Left Center Forward) | Shot | Off T xG 0.12 | 113.6,35.8 | 0.8
22 | P2 50:38 | Team A | P364 (Goalkeeper) | Goal Keeper | Shot Faced | 0.8,40.8 | 0.0
23 | P2 50:54 | Team A | P364 (Goalkeeper) | Pass | Goal Kick Ground Pass | 6.0,44.0 -> 16.4,68.2 | 0.7
24 | P2 50:55 | Team A | P414 (Right Center Back) | Ball Receipt* |  | 16.4,68.2 | 
25 | P2 50:55 | Team A | P414 (Right Center Back) | Pass | Ground Pass | 16.4,68.2 -> 2.7,52.0 | 2.9
26 | P2 50:58 | Team A | P364 (Goalkeeper) | Ball Receipt* |  | 2.7,52.0 | 
27 | P2 50:58 | Team A | P364 (Goalkeeper) | Pass | Ground Pass | 2.7,52.0 -> 15.6,21.0 | 2.8
28 | P2 51:01 | Team A | P065 (Left Center Back) | Ball Receipt* |  | 15.6,21.0 | 
29 | P2 51:01 | Team A | P065 (Left Center Back) | Carry |  | 15.6,21.0 -> 52.0,11.2 | 7.5
30 | P2 51:09 | Team A | P065 (Left Center Back) | Pass | Incomplete High Pass | 52.0,11.2 -> 84.3,3.9 | 2.3
31 | P2 51:11 | Team A | P229 (Left Midfield) | Ball Receipt* |  | 89.3,3.9 | 
32 | P2 51:11 | Team B | P358 (Right Back) | Interception |  | 35.8,76.2 | 0.0
33 | P2 51:11 | Team B | P358 (Right Back) | Carry |  | 35.8,76.2 -> 42.9,76.9 | 2.7
34 | P2 51:11 | Team A | P229 (Left Midfield) | Pressure |  | 85.3,6.0 | 2.4
35 | P2 51:14 | Team B | P358 (Right Back) | Pass | Incomplete Low Pass | 42.9,76.9 -> 56.4,76.8 | 1.0
36 | P2 51:14 | Team B | P036 (Right Center Forward) | Pressure |  | 56.4,76.8 | 0.4
37 | P2 51:15 | Team A | P065 (Left Center Back) | Interception |  | 63.7,3.3 | 0.0
38 | P2 51:32 | Team B | P358 (Right Back) | Pass | Throw-in High Pass | 56.4,80.0 -> 77.9,73.9 | 2.3
39 | P2 51:33 | Team B | P316 (Left Center Forward) | Ball Receipt* |  | 77.9,73.9 | 
40 | P2 51:33 | Team A | P065 (Left Center Back) | Duel | Aerial Lost | 42.2,6.2 | 0.0

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_227  condition=sub_before_entry
**hidden truth:** `{'plant': 'sub_before_entry', 'index': 16, 'match_id': 3754115}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 62:43 | Team B | P168 (Right Back) | Pass | Ground Pass | 57.6,68.3 -> 43.0,51.4 | 3.5
 2 | P2 62:46 | Team B | P493 (Right Center Back) | Ball Receipt* |  | 43.0,51.4 | 
 3 | P2 62:46 | Team B | P493 (Right Center Back) | Pass | Ground Pass | 43.0,51.4 -> 45.8,29.9 | 2.6
 4 | P2 62:49 | Team B | P183 (Left Center Back) | Ball Receipt* |  | 45.8,29.9 | 
 5 | P2 62:49 | Team B | P183 (Left Center Back) | Carry |  | 45.8,29.9 -> 50.7,25.3 | 1.4
 6 | P2 62:50 | Team B | P183 (Left Center Back) | Pass | Ground Pass | 50.7,25.3 -> 57.6,41.9 | 0.9
 7 | P2 62:51 | Team B | P343 (Left Center Midfield) | Ball Receipt* |  | 57.6,41.9 | 
 8 | P2 62:51 | Team B | P343 (Left Center Midfield) | Pass | Ground Pass | 57.6,41.9 -> 49.6,26.1 | 1.6
 9 | P2 62:53 | Team B | P183 (Left Center Back) | Ball Receipt* |  | 49.6,26.1 | 
10 | P2 62:53 | Team B | P183 (Left Center Back) | Carry |  | 49.6,26.1 -> 49.6,26.1 | 0.6
11 | P2 62:53 | Team B | P183 (Left Center Back) | Pass | Ground Pass | 49.6,26.1 -> 42.4,51.6 | 1.6
12 | P2 62:55 | Team B | P493 (Right Center Back) | Ball Receipt* |  | 42.4,51.6 | 
13 | P2 62:55 | Team B | P493 (Right Center Back) | Carry |  | 42.4,51.6 -> 41.8,51.6 | 2.6
14 | P2 62:57 | Team B | P493 (Right Center Back) | Pass | Ground Pass | 41.8,51.6 -> 41.3,16.7 | 2.0
15 | P2 62:59 | Team B | P183 (Left Center Back) | Ball Receipt* |  | 41.3,16.7 | 
16 | P2 62:59 | Team B | P379 (Left Center Back) | Carry |  | 41.3,16.7 -> 49.9,9.2 | 3.1
17 | P2 63:02 | Team A | P024 (Center Attacking Midfield) | Pressure |  | 71.4,66.3 | 0.9
18 | P2 63:03 | Team B | P183 (Left Center Back) | Pass | Incomplete High Pass | 49.9,9.2 -> 92.0,9.2 | 2.1
19 | P2 63:05 | Team B | P103 (Left Wing) | Ball Receipt* |  | 90.5,13.8 | 
20 | P2 63:05 | Team A | P307 (Right Back) | Ball Recovery |  | 28.1,70.9 | 0.0
21 | P2 63:37 | Team B | P264 (Left Back) | Substitution | off, on: P379 | , | 0.0
22 | P2 63:51 | Team B | P379 (Left Back) | Pass | Throw-in Incomplete Low Pass | 104.9,0.1 -> 106.0,10.4 | 0.9
23 | P2 63:52 | Team B | P245 (Right Wing) | Ball Receipt* |  | 104.3,15.0 | 
24 | P2 63:52 | Team A | P427 (Left Defensive Midfield) | Interception |  | 14.1,69.7 | 0.0
25 | P2 63:52 | Team A | P427 (Left Defensive Midfield) | Carry |  | 14.1,69.7 -> 14.4,68.0 | 0.9
26 | P2 63:53 | Team A | P427 (Left Defensive Midfield) | Pass | High Pass | 14.4,68.0 -> 20.1,51.4 | 2.9
27 | P2 63:56 | Team A | P081 (Right Center Back) | Ball Receipt* |  | 20.1,51.4 | 
28 | P2 63:56 | Team A | P081 (Right Center Back) | Pass | Incomplete Low Pass | 20.1,51.4 -> 35.9,54.0 | 1.0
29 | P2 63:57 | Team A | P024 (Center Attacking Midfield) | Ball Receipt* |  | 32.4,50.5 | 
30 | P2 63:57 | Team B | P343 (Left Center Midfield) | Pass | Recovery Ground Pass | 84.2,26.1 -> 85.9,33.3 | 0.6
31 | P2 63:57 | Team B | P232 (Right Center Midfield) | Ball Receipt* |  | 85.9,33.3 | 
32 | P2 63:57 | Team B | P232 (Right Center Midfield) | Carry |  | 85.9,33.3 -> 85.9,33.3 | 0.2
33 | P2 63:58 | Team B | P232 (Right Center Midfield) | Pass | Ground Pass | 85.9,33.3 -> 75.1,51.6 | 1.6
34 | P2 63:59 | Team B | P168 (Right Back) | Ball Receipt* |  | 75.1,51.6 | 
35 | P2 63:59 | Team B | P168 (Right Back) | Carry |  | 75.1,51.6 -> 75.1,51.6 | 0.6
36 | P2 64:00 | Team B | P168 (Right Back) | Pass | Incomplete High Pass | 75.1,51.6 -> 110.3,23.6 | 3.1
37 | P2 64:03 | Team B | P238 (Center Attacking Midfield) | Ball Receipt* |  | 104.9,21.9 | 
38 | P2 64:03 | Team A | P307 (Right Back) | Ball Recovery |  | 9.8,56.5 | 0.0
39 | P2 64:03 | Team A | P307 (Right Back) | Carry |  | 9.8,56.5 -> 3.8,74.3 | 1.9
40 | P2 64:04 | Team B | P238 (Center Attacking Midfield) | Pressure |  | 112.9,12.7 | 1.2

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_236  condition=time_impossible
**hidden truth:** `{'plant': 'time_impossible', 'index': 16, 'match_id': 3754252}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 83:30 | Team B | P177 (Right Wing) | Ball Recovery |  | 110.0,68.1 | 0.0
 2 | P2 83:30 | Team B | P177 (Right Wing) | Carry |  | 110.0,68.1 -> 111.4,68.9 | 3.0
 3 | P2 83:33 | Team B | P177 (Right Wing) | Pass | Incomplete Low Pass | 111.4,68.9 -> 110.0,65.8 | 0.1
 4 | P2 83:33 | Team A | P396 (Left Back) | Block |  | 10.1,14.3 | 0.0
 5 | P2 83:38 | Team B | P177 (Right Wing) | Pass | Throw-in Low Pass | 110.1,80.0 -> 97.5,61.7 | 1.9
 6 | P2 83:40 | Team B | P080 (Right Back) | Ball Receipt* |  | 97.5,61.7 | 
 7 | P2 83:40 | Team B | P080 (Right Back) | Carry |  | 97.5,61.7 -> 97.3,61.7 | 0.1
 8 | P2 83:40 | Team B | P080 (Right Back) | Pass | Out Low Pass | 97.3,61.7 -> 120.0,68.5 | 4.2
 9 | P2 83:44 | Team B | P157 (Left Wing) | Ball Receipt* |  | 116.2,68.1 | 
10 | P2 84:11 | Team A | P506 (Goalkeeper) | Pass | Goal Kick Incomplete High Pass | 7.0,44.1 -> 69.2,44.6 | 3.5
11 | P2 84:15 | Team B | P093 (Right Center Back) | Ball Recovery |  | 50.9,35.5 | 0.0
12 | P2 84:15 | Team B | P093 (Right Center Back) | Carry |  | 50.9,35.5 -> 55.1,21.1 | 2.6
13 | P2 84:17 | Team B | P093 (Right Center Back) | Pass | Ground Pass | 55.1,21.1 -> 57.8,11.7 | 0.8
14 | P2 84:18 | Team A | P322 (Right Wing) | Pressure |  | 65.1,70.1 | 0.7
15 | P2 84:18 | Team B | P185 (Center Forward) | Ball Receipt* |  | 57.8,11.7 | 
16 | P2 144:18 | Team B | P185 (Center Forward) | Carry |  | 57.8,11.7 -> 57.8,13.5 | 0.5
17 | P2 84:19 | Team B | P185 (Center Forward) | Miscontrol |  | 57.8,13.5 | 0.0
18 | P2 84:19 | Team A | P322 (Right Wing) | Ball Recovery |  | 59.7,65.1 | 0.0
19 | P2 84:19 | Team A | P322 (Right Wing) | Carry |  | 59.7,65.1 -> 55.8,62.1 | 1.3
20 | P2 84:20 | Team A | P322 (Right Wing) | Pass | Ground Pass | 55.8,62.1 -> 65.9,58.2 | 0.6
21 | P2 84:21 | Team A | P303 (Center Attacking Midfield) | Ball Receipt* |  | 65.9,58.2 | 
22 | P2 84:21 | Team A | P303 (Center Attacking Midfield) | Carry |  | 65.9,58.2 -> 64.7,55.4 | 1.5
23 | P2 84:22 | Team B | P185 (Center Forward) | Pressure |  | 53.6,22.0 | 0.3
24 | P2 84:22 | Team A | P303 (Center Attacking Midfield) | Pass | Incomplete Ground Pass | 64.7,55.4 -> 65.9,59.3 | 0.2
25 | P2 84:22 | Team A | P215 (Right Back) | Ball Receipt* |  | 66.5,72.4 | 
26 | P2 84:22 | Team B | P185 (Center Forward) | Block |  | 54.2,20.8 | 0.0
27 | P2 84:23 | Team A | P447 (Left Wing) | Ball Recovery |  | 76.9,44.1 | 0.0
28 | P2 84:23 | Team A | P447 (Left Wing) | Carry |  | 76.9,44.1 -> 78.3,44.3 | 2.1
29 | P2 84:25 | Team A | P447 (Left Wing) | Pass | Low Pass | 78.3,44.3 -> 97.0,62.1 | 1.1
30 | P2 84:26 | Team B | P137 (Left Back) | Pressure |  | 23.1,16.6 | 0.6
31 | P2 84:27 | Team A | P112 (Center Forward) | Ball Receipt* |  | 97.0,62.1 | 
32 | P2 84:27 | Team A | P112 (Center Forward) | Carry |  | 97.0,62.1 -> 99.0,63.5 | 1.7
33 | P2 84:28 | Team B | P137 (Left Back) | Dribbled Past |  | 21.1,16.6 | 0.0
34 | P2 84:28 | Team A | P112 (Center Forward) | Dribble |  | 99.0,63.5 | 0.0
35 | P2 84:28 | Team A | P112 (Center Forward) | Carry |  | 99.0,63.5 -> 100.4,69.1 | 2.6
36 | P2 84:29 | Team B | P137 (Left Back) | Pressure |  | 22.5,13.8 | 1.9
37 | P2 84:31 | Team A | P112 (Center Forward) | Pass | Ground Pass | 100.4,69.1 -> 96.2,74.5 | 1.1
38 | P2 84:32 | Team A | P215 (Right Back) | Ball Receipt* |  | 96.2,74.5 | 
39 | P2 84:32 | Team A | P215 (Right Back) | Carry |  | 96.2,74.5 -> 95.3,73.7 | 0.4
40 | P2 84:32 | Team B | P177 (Right Wing) | Pressure |  | 24.8,7.0 | 0.6

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_019  condition=wrong_team
**hidden truth:** `{'plant': 'wrong_team', 'index': 20, 'match_id': 3754071}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P1 30:22 | Team B | P204 (Center Attacking Midfield) | Carry |  | 76.0,13.0 -> 76.6,15.7 | 0.0
 2 | P1 30:22 | Team B | P204 (Center Attacking Midfield) | Miscontrol |  | 76.6,15.7 | 0.0
 3 | P1 30:23 | Team B | P204 (Center Attacking Midfield) | Pressure |  | 70.8,16.1 | 1.7
 4 | P1 30:24 | Team A | P526 (Right Center Midfield) | Ball Recovery |  | 50.8,61.6 | 0.0
 5 | P1 30:24 | Team A | P526 (Right Center Midfield) | Carry |  | 50.8,61.6 -> 54.5,61.0 | 0.7
 6 | P1 30:25 | Team B | P204 (Center Attacking Midfield) | Foul Committed |  | 65.6,19.1 | 0.0
 7 | P1 30:25 | Team A | P526 (Right Center Midfield) | Foul Won |  | 54.5,61.0 | 0.0
 8 | P1 30:25 | Team A | P526 (Right Center Midfield) | Carry |  | 54.5,61.0 -> 55.6,59.8 | 0.1
 9 | P1 30:25 | Team A | P526 (Right Center Midfield) | Pass | High Pass | 55.6,59.8 -> 69.9,69.6 | 1.8
10 | P1 30:27 | Team A | P393 (Right Wing) | Ball Receipt* |  | 69.9,69.6 | 
11 | P1 30:27 | Team A | P393 (Right Wing) | Carry |  | 69.9,69.6 -> 69.1,69.6 | 1.2
12 | P1 30:28 | Team A | P393 (Right Wing) | Pass | Ground Pass | 69.1,69.6 -> 62.0,70.8 | 0.8
13 | P1 30:29 | Team A | P526 (Right Center Midfield) | Ball Receipt* |  | 62.0,70.8 | 
14 | P1 30:29 | Team A | P526 (Right Center Midfield) | Carry |  | 62.0,70.8 -> 62.6,73.6 | 0.7
15 | P1 30:29 | Team A | P526 (Right Center Midfield) | Pass | Ground Pass | 62.6,73.6 -> 71.8,78.1 | 1.1
16 | P1 30:30 | Team A | P393 (Right Wing) | Ball Receipt* |  | 71.8,78.1 | 
17 | P1 30:30 | Team A | P393 (Right Wing) | Carry |  | 71.8,78.1 -> 97.1,60.1 | 5.4
18 | P1 30:36 | Team A | P393 (Right Wing) | Pass | High Pass | 97.1,60.1 -> 109.0,26.2 | 1.8
19 | P1 30:38 | Team A | P155 (Left Center Midfield) | Ball Receipt* |  | 109.0,26.2 | 
20 | P1 30:38 | Team B | P155 (Left Center Midfield) | Pass | Incomplete High Pass | 107.8,26.0 -> 105.0,37.0 | 1.1
21 | P1 30:39 | Team A | P012 (Left Wing) | Ball Receipt* |  | 104.2,36.0 | 
22 | P1 30:39 | Team B | P477 (Right Center Back) | Pass | Interception High Pass | 15.1,43.1 -> 18.7,68.8 | 1.3
23 | P1 30:40 | Team B | P374 (Right Wing) | Ball Receipt* |  | 18.7,68.8 | 
24 | P1 30:40 | Team B | P374 (Right Wing) | Carry |  | 18.7,68.8 -> 19.6,66.6 | 1.9
25 | P1 30:41 | Team A | P012 (Left Wing) | Pressure |  | 101.7,25.6 | 0.6
26 | P1 30:42 | Team B | P374 (Right Wing) | Pass | Ground Pass | 19.6,66.6 -> 43.1,55.4 | 1.3
27 | P1 30:43 | Team B | P011 (Left Wing) | Ball Receipt* |  | 43.1,55.4 | 
28 | P1 30:43 | Team B | P011 (Left Wing) | Carry |  | 43.1,55.4 -> 86.4,72.8 | 7.8
29 | P1 30:46 | Team A | P126 (Left Back) | Pressure |  | 52.0,19.5 | 3.1
30 | P1 30:50 | Team A | P526 (Right Center Midfield) | Pressure |  | 34.6,7.9 | 0.7
31 | P1 30:51 | Team B | P011 (Left Wing) | Dribble |  | 86.4,72.8 | 0.0
32 | P1 30:51 | Team A | P526 (Right Center Midfield) | Duel | Tackle | 33.7,7.3 | 0.0
33 | P1 31:07 | Team B | P228 (Right Back) | Pass | Throw-in Low Pass | 86.2,80.0 -> 81.2,70.9 | 0.8
34 | P1 31:07 | Team B | P011 (Left Wing) | Ball Receipt* |  | 81.2,70.9 | 
35 | P1 31:07 | Team B | P011 (Left Wing) | Pass | Ground Pass | 81.2,70.9 -> 81.6,76.1 | 0.9
36 | P1 31:08 | Team B | P228 (Right Back) | Ball Receipt* |  | 81.6,76.1 | 
37 | P1 31:08 | Team B | P228 (Right Back) | Carry |  | 81.6,76.1 -> 82.5,75.9 | 0.7
38 | P1 31:08 | Team A | P012 (Left Wing) | Pressure |  | 36.7,7.9 | 0.6
39 | P1 31:09 | Team B | P228 (Right Back) | Pass | Incomplete Ground Pass | 82.5,75.9 -> 78.5,74.7 | 0.1
40 | P1 31:09 | Team B | P011 (Left Wing) | Ball Receipt* |  | 76.8,70.9 | 

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_295  condition=wrong_team
**hidden truth:** `{'plant': 'wrong_team', 'index': 16, 'match_id': 3754189}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 67:05 | Team B | P167 (Right Wing Back) | Ball Receipt* |  | 98.6,73.7 | 
 2 | P2 67:05 | Team B | P167 (Right Wing Back) | Carry |  | 98.6,73.7 -> 93.0,69.8 | 2.9
 3 | P2 67:08 | Team B | P167 (Right Wing Back) | Pass | Ground Pass | 93.0,69.8 -> 97.3,54.1 | 1.0
 4 | P2 67:09 | Team B | P008 (Right Center Forward) | Ball Receipt* |  | 97.3,54.1 | 
 5 | P2 67:09 | Team B | P008 (Right Center Forward) | Carry |  | 97.3,54.1 -> 91.1,50.3 | 3.0
 6 | P2 67:10 | Team A | P329 (Left Defensive Midfield) | Pressure |  | 23.0,25.7 | 1.2
 7 | P2 67:12 | Team B | P008 (Right Center Forward) | Pass | Incomplete Ground Pass | 91.1,50.3 -> 111.4,48.9 | 2.6
 8 | P2 67:14 | Team B | P341 (Right Center Back) | Ball Receipt* |  | 106.5,48.6 | 
 9 | P2 67:14 | Team A | P511 (Goalkeeper) | Ball Recovery |  | 8.7,31.2 | 0.0
10 | P2 67:14 | Team A | P511 (Goalkeeper) | Carry |  | 8.7,31.2 -> 14.7,37.3 | 4.7
11 | P2 67:19 | Team A | P511 (Goalkeeper) | Pass | Unknown High Pass | 14.7,37.3 -> 63.4,26.7 | 2.4
12 | P2 67:22 | Team B | P415 (Center Back) | Foul Committed |  | 56.1,53.4 | 0.0
13 | P2 67:22 | Team A | P156 (Center Forward) | Foul Won |  | 64.0,26.7 | 0.0
14 | P2 67:37 | Team A | P329 (Left Defensive Midfield) | Pass | Free Kick Incomplete High Pass | 63.7,25.3 -> 97.8,57.0 | 4.7
15 | P2 67:42 | Team B | P349 (Left Center Back) | Ball Recovery |  | 22.3,23.1 | 0.0
16 | P2 67:47 | Team A | P349 (Left Center Back) | Pass | Ground Pass | 28.5,21.8 -> 41.9,23.7 | 1.0
17 | P2 67:48 | Team B | P416 (Right Defensive Midfield) | Ball Receipt* |  | 41.9,23.7 | 
18 | P2 67:48 | Team B | P416 (Right Defensive Midfield) | Pass | Incomplete Low Pass | 42.7,22.1 -> 29.3,38.2 | 2.1
19 | P2 67:50 | Team B | P317 (Left Defensive Midfield) | Ball Receipt* |  | 28.8,33.8 | 
20 | P2 67:50 | Team A | P156 (Center Forward) | Ball Recovery |  | 90.8,41.9 | 0.0
21 | P2 67:50 | Team A | P156 (Center Forward) | Carry |  | 90.8,41.9 -> 97.7,48.4 | 1.2
22 | P2 67:51 | Team A | P156 (Center Forward) | Shot | Blocked xG 0.04 | 97.7,48.4 | 0.2
23 | P2 67:51 | Team B | P415 (Center Back) | Block |  | 19.7,31.9 | 0.0
24 | P2 67:51 | Team B | P087 (Goalkeeper) | Goal Keeper | Shot Faced | 4.0,38.2 | 0.0
25 | P2 68:14 | Team A | P164 (Right Back) | Pass | Throw-in High Pass | 111.2,80.0 -> 106.9,72.1 | 1.0
26 | P2 68:15 | Team A | P478 (Right Wing) | Ball Receipt* |  | 106.9,72.1 | 
27 | P2 68:15 | Team A | P478 (Right Wing) | Carry |  | 106.9,72.1 -> 106.1,70.8 | 0.0
28 | P2 68:15 | Team A | P478 (Right Wing) | Pass | Ground Pass | 106.1,70.8 -> 109.8,75.1 | 1.1
29 | P2 68:16 | Team A | P164 (Right Back) | Ball Receipt* |  | 109.8,75.1 | 
30 | P2 68:16 | Team A | P164 (Right Back) | Carry |  | 109.8,75.1 -> 109.7,75.3 | 0.3
31 | P2 68:17 | Team A | P164 (Right Back) | Pass | Ground Pass | 109.7,75.3 -> 99.1,76.3 | 1.0
32 | P2 68:17 | Team A | P478 (Right Wing) | Ball Receipt* |  | 99.1,76.3 | 
33 | P2 68:17 | Team A | P478 (Right Wing) | Carry |  | 99.1,76.3 -> 99.1,76.3 | 0.8
34 | P2 68:18 | Team A | P478 (Right Wing) | Pass | Ground Pass | 99.1,76.3 -> 84.4,74.9 | 1.7
35 | P2 68:20 | Team A | P249 (Right Defensive Midfield) | Ball Receipt* |  | 84.4,74.9 | 
36 | P2 68:20 | Team A | P249 (Right Defensive Midfield) | Carry |  | 84.4,74.9 -> 80.2,72.1 | 2.2
37 | P2 68:21 | Team B | P317 (Left Defensive Midfield) | Pressure |  | 34.3,8.0 | 1.1
38 | P2 68:22 | Team A | P249 (Right Defensive Midfield) | Dispossessed |  | 80.2,72.1 | 0.0
39 | P2 68:22 | Team B | P317 (Left Defensive Midfield) | Duel | Tackle | 39.9,8.0 | 0.0
40 | P2 68:24 | Team B | P317 (Left Defensive Midfield) | Pressure |  | 42.7,9.3 | 0.7

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```

---
## t3_299  condition=time_impossible
**hidden truth:** `{'plant': 'time_impossible', 'index': 17, 'match_id': 3754226}`

```
40 consecutive events from one Premier League 2015/16 match (StatsBomb format). Columns: idx | period minute:second | team | player (position) | type | detail | start x,y -> end x,y (pitch 120x80, each team attacks left to right) | duration s

 1 | P2 62:14 | Team B | P216 (Left Wing) | Ball Receipt* |  | 58.2,3.6 | 
 2 | P2 62:14 | Team B | P216 (Left Wing) | Carry |  | 58.2,3.6 -> 57.8,3.8 | 1.4
 3 | P2 62:16 | Team A | P228 (Right Back) | Foul Committed |  | 62.3,76.3 | 0.0
 4 | P2 62:16 | Team B | P216 (Left Wing) | Foul Won |  | 57.8,3.8 | 0.0
 5 | P2 62:33 | Team A | P374 (Left Center Midfield) | Substitution | off, on: P204 | , | 0.0
 6 | P2 62:52 | Team B | P387 (Left Back) | Pass | Free Kick Ground Pass | 62.5,2.9 -> 61.4,11.3 | 1.0
 7 | P2 62:53 | Team B | P123 (Right Defensive Midfield) | Ball Receipt* |  | 61.4,11.3 | 
 8 | P2 62:53 | Team B | P123 (Right Defensive Midfield) | Pass | Ground Pass | 61.4,11.3 -> 63.2,3.8 | 1.0
 9 | P2 62:54 | Team B | P387 (Left Back) | Ball Receipt* |  | 63.2,3.8 | 
10 | P2 62:54 | Team B | P387 (Left Back) | Pass | Ground Pass | 63.2,3.6 -> 37.9,15.8 | 2.5
11 | P2 62:57 | Team B | P107 (Left Center Back) | Ball Receipt* |  | 37.9,15.8 | 
12 | P2 62:57 | Team B | P107 (Left Center Back) | Pass | Ground Pass | 37.9,15.8 -> 37.3,50.2 | 2.8
13 | P2 63:00 | Team B | P337 (Right Center Back) | Ball Receipt* |  | 37.3,50.2 | 
14 | P2 63:00 | Team B | P337 (Right Center Back) | Carry |  | 37.3,50.2 -> 35.4,49.3 | 2.1
15 | P2 63:02 | Team B | P337 (Right Center Back) | Pass | Ground Pass | 35.4,49.3 -> 12.0,42.1 | 3.2
16 | P2 63:05 | Team B | P165 (Goalkeeper) | Ball Receipt* |  | 12.0,42.1 | 
17 | P2 123:05 | Team B | P165 (Goalkeeper) | Carry |  | 12.0,42.1 -> 12.7,47.2 | 5.1
18 | P2 63:10 | Team B | P165 (Goalkeeper) | Pass | High Pass | 12.7,47.2 -> 71.1,70.3 | 3.2
19 | P2 63:13 | Team B | P134 (Center Forward) | Ball Receipt* |  | 71.1,70.3 | 
20 | P2 63:13 | Team B | P134 (Center Forward) | Pass | Incomplete High Pass | 71.1,70.3 -> 80.3,55.1 | 1.5
21 | P2 63:15 | Team B | P251 (Left Defensive Midfield) | Ball Receipt* |  | 75.1,55.8 | 
22 | P2 63:15 | Team A | P015 (Center Defensive Midfield) | Pass | Recovery Low Pass | 39.8,25.0 -> 55.7,14.9 | 1.1
23 | P2 63:16 | Team A | P011 (Left Wing) | Ball Receipt* |  | 55.7,14.9 | 
24 | P2 63:16 | Team A | P011 (Left Wing) | Carry |  | 55.7,14.9 -> 49.7,17.7 | 2.7
25 | P2 63:16 | Team B | P407 (Right Wing) | Pressure |  | 67.9,64.5 | 1.0
26 | P2 63:18 | Team B | P134 (Center Forward) | Pressure |  | 70.4,65.0 | 0.8
27 | P2 63:19 | Team A | P011 (Left Wing) | Pass | Ground Pass | 49.7,17.7 -> 37.0,36.1 | 1.6
28 | P2 63:20 | Team A | P312 (Right Center Back) | Ball Receipt* |  | 37.0,36.1 | 
29 | P2 63:20 | Team A | P312 (Right Center Back) | Carry |  | 37.0,36.1 -> 38.8,43.4 | 1.5
30 | P2 63:22 | Team A | P312 (Right Center Back) | Pass | Ground Pass | 38.8,43.4 -> 63.1,73.1 | 1.9
31 | P2 63:24 | Team A | P228 (Right Back) | Ball Receipt* |  | 63.1,73.1 | 
32 | P2 63:24 | Team A | P228 (Right Back) | Carry |  | 63.1,73.1 -> 87.1,75.7 | 2.2
33 | P2 63:26 | Team A | P228 (Right Back) | Pass | Ground Pass | 87.1,75.7 -> 89.2,56.2 | 0.9
34 | P2 63:27 | Team A | P082 (Right Wing) | Ball Receipt* |  | 89.2,56.2 | 
35 | P2 63:27 | Team A | P082 (Right Wing) | Carry |  | 89.2,56.2 -> 89.7,55.6 | 0.1
36 | P2 63:27 | Team A | P082 (Right Wing) | Miscontrol |  | 89.7,55.6 | 0.0
37 | P2 63:28 | Team A | P204 (Left Center Midfield) | Ball Recovery |  | 92.2,54.1 | 0.0
38 | P2 63:29 | Team B | P123 (Right Defensive Midfield) | Ball Recovery |  | 29.8,25.8 | 0.0
39 | P2 63:29 | Team B | P123 (Right Defensive Midfield) | Carry |  | 29.8,25.8 -> 30.2,23.5 | 1.2
40 | P2 63:29 | Team A | P082 (Right Wing) | Pressure |  | 91.8,55.1 | 0.7

At most one event has been corrupted so that it is impossible or inconsistent with the others. Possible corruption types: goal_no_shot, fast_long_pass, keeper_corner, wrong_team, time_impossible, sub_before_entry, deleted_goal.
Answer {"corrupt": "yes" | "no", "index": <idx or null>, "type": "<type or null>"}.
```
