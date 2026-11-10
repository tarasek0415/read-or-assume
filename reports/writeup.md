# read-or-assume: do LLMs read football data or assume?

v1 results, 5 November 2026; v2 track 2 rerun, 10 November 2026. Data: StatsBomb open data, Premier League 2015/16 (380 matches,
1.3M events). Credit StatsBomb; used under their non-commercial licence.

## Question

When a model is given football event data plus a hint, does the answer follow the data or
the hint? We change exactly one thing in real data and measure which way the answer moves.
All grading is code against known truth. No model judges anything.

## Method

- **Track 1, position labels.** 150 outfield players with 900+ minutes, anonymised. Per-90
  profile (shots, box touches, key passes, passes, progressive passes, tackles,
  interceptions, clearances, aerials, average position, share of actions per third).
  Conditions: no label, true label, false label two groups away (defender shown as forward
  or the reverse; wing-backs and attacking midfielders excluded). Truth is the StatsBomb
  lineup position folded to defender/midfielder/forward.
- **Track 2, club names.** All 20 teams. Season per-90 profile with league averages.
  Same numbers shown as "Team K", as a big club, and as a small club. Eight yes/no questions
  answerable from the numbers, plus a predicted league finish.
- **Track 3, data integrity.** 300 excerpts of 40 consecutive real events, 40% clean. One
  plant or none: phantom goal, 65-yard pass in half a second, keeper taking a corner, wrong
  team credited, impossible minute, substitute acting before entry, deleted goal.
- One stateless call per prompt, temperature 0, low reasoning effort (the top models refuse
  to run with thinking off). JSON-only answers; refusals and bad format count as wrong.
  20% of prompts sent twice for self-agreement. 95% bootstrap ranges over items.
- Models: Claude Opus 5.5 and Gemini 4 Argon on everything; Muse Wonder on track 2, 450 of
  the 652 track 1 calls and 100 of the 360 track 3 calls (thinking tokens made it ~10x the
  price per call). Claude Fable 5.1, GPT-6 Astra and Claude Haiku 5.5: 20-call samples only.
- Total spend: about $21 on OpenRouter for v1, $1.42 for the v2 track 2 rerun.

## Results

### Track 1: nobody follows a false label, but one model fights the true one

| | Opus 5.5 | Gemini 4 | Muse Wonder (partial) |
|---|---|---|---|
| accuracy, no label | 0.85 [0.80, 0.91] | 0.87 [0.82, 0.92] | 0.88 [0.82, 0.93] |
| accuracy, true label | 0.88 [0.83, 0.93] | 0.88 [0.83, 0.93] | **0.50 [0.42, 0.58]** |
| accuracy, false label | 0.77 [0.69, 0.85] | 0.91 [0.85, 0.97] | 0.81 [0.72, 0.89] |
| label-follow rate, false label | 0.01 [0.00, 0.03] | 0.02 [0.00, 0.05] | 0.01 [0.00, 0.04] |
| self-agreement (repeat prompts) | 0.86 [0.80, 0.93] | 0.89 [0.84, 0.95] | - |
| leakage (named the player) | 0.19 [0.13, 0.25] | 0.13 [0.08, 0.18] | 0.19 [0.12, 0.25] |

- A false label almost never wins: 1-2% follow rate for all three models. On this task the
  models read the numbers.
- **Muse Wonder reacts against labels rather than ignoring them.** Told the true label
  "defender", it answered "midfielder" 28 times out of 48, although with no label it gets
  defenders right 94% of the time. Its low false-label follow rate is therefore not evidence
  of reading; the true-label control is what separates "reads the data" from "contradicts
  the hint". Opus and Gemini are unchanged by a true label.
- The common no-label error is one group up: defenders called midfielders, midfielders
  called forwards. Full-backs and attacking midfielders sit between groups.
- Self-agreement is only 86-89% at temperature 0, because low reasoning effort still
  introduces run-to-run variation. Any single-run difference under ~10 points is noise.
- Leakage: 13-19% of anonymised player profiles were named correctly (Kane, Özil, Kanté,
  Payet and other distinctive players). Profiles are not fully anonymous to models that know
  the season. For track 1 this is a limit, not a flaw in the headline, since a known player
  makes a false label *easier* to reject.

### Track 2 (v1): facts are read correctly, judgments move with the club name

v1 prompts named the season ("Premier League 2015/16"). The v2 rerun below shows most of
this effect was the models recalling that season, so read this table with that section.

| | Opus 5.5 | Gemini 4 | Muse Wonder |
|---|---|---|---|
| accuracy on 8 yes/no questions, any condition | 1.00 | 1.00 | 1.00 |
| flip rate when only the name changes | 0.00 | 0.00 | 0.00 |
| predicted-finish error, "Team K" (places) | 2.3 [1.4, 3.2] | 1.1 [0.5, 1.9] | 1.8 [1.0, 2.9] |
| shift in predicted finish, big-club name | -2.5 [-5.4, 0.9] | +2.1 [0.9, 3.4] | -4.8 [-8.0, -1.3] |
| shift in predicted finish, small-club name | +6.1 [3.5, 9.0] | +3.6 [1.4, 5.9] | +4.5 [1.7, 7.4] |
| leakage (named the club from "Team K") | 0.65 [0.40, 0.85] | 0.75 [0.55, 0.95] | 0.55 [0.35, 0.75] |

- Every model answered all 160 above/below-average questions correctly in every condition,
  so the name never flipped a factual answer. Reading numbers against a stated average is
  solved.
- The judgment question moved. With identical numbers, a small-club name pushed the
  predicted finish 4-6 places lower for every model. The big-club result was mixed. Both
  turned out to be mostly memory: given "Chelsea" and "2015/16", all three models answered
  10th, Chelsea's real finish that season, for numbers that say top three.
- Leakage is high: 55-75% of teams were named from "Team K" profiles. The models know
  this season. The flip rate is still a fair test (the numbers are identical across
  conditions), but "neutral" is not blind, and the finish predictions in the neutral
  condition are partly memory (error of 1-2 places).

### Track 2 (v2): without the season, the name effect shrinks to 1-2 places

The v2 prompts say "Premier League" with no season. Everything else is word-for-word the
same as v1, so the two runs compare directly.

| | Opus 5.5 | Gemini 4 | Muse Wonder |
|---|---|---|---|
| accuracy on 8 yes/no questions, any condition | 1.00 | 1.00 | 1.00 |
| flip rate when only the name changes | 0.00 | 0.00 | 0.00 |
| predicted-finish error, "Team K" (places) | 2.0 [1.3, 2.8] | 1.7 [1.0, 2.5] | 2.5 [1.6, 3.5] |
| shift in predicted finish, big-club name | -1.3 [-1.7, -0.8] | -0.5 [-1.1, 0.3] | -0.9 [-1.6, -0.3] |
| shift in predicted finish, small-club name | +0.9 [0.4, 1.4] | +2.1 [0.6, 3.9] | +0.7 [0.1, 1.3] |
| leakage (named the club from "Team K") | 0.00 | 0.10 [0.00, 0.25] | 0.10 [0.00, 0.25] |
| self-agreement (16 repeats) | 0.81 [0.62, 1.00] | 0.81 [0.56, 1.00] | 0.50 [0.25, 0.75] |

- Removing one line of context cut the small-club penalty from 4-6 places to 1-2, and team
  leakage from 55-75% to 0-10%. Most of the v1 effect was recall of the 2015/16 table.
- What remains is small but consistent: a small-club name costs about a place, a big-club
  name gains about a place, for all three models. Gemini's big-club range and Muse's
  self-agreement (50% on 16 repeats) make those two the weakest parts of the result.
- Liverpool's season (8th in reality) as an example. v1: "Team K" 3rd, "Chelsea" 10th from
  all three models. v2: "Team K" 3rd-4th, "Chelsea" 3rd from all three.
- The benchmark caught its own confound: stating the season let the models answer from
  memory, and the counterfactual design showed how much.

### Track 3: planted errors are a solved problem for the top models

| | Opus 5.5 | Gemini 4 | Muse Wonder (100) |
|---|---|---|---|
| detection, any plant | 1.00 | 0.99 [0.98, 1.00] | 0.97 [0.92, 1.00] |
| localised within 1 event, rule-checkable plants | 1.00 | 1.00 | 1.00 |
| localised, football-sense plants | 0.96 [0.90, 1.00] | 1.00 | 0.93 [0.79, 1.00] |
| false alarm on clean excerpts | 0.10 [0.05, 0.16] | 0.03 [0.01, 0.07] | 0.22 [0.11, 0.35] |
| bad format / no answer | 0.00 | 0.00 | 0.30 [0.21, 0.39] |
| self-agreement | 0.93 [0.87, 0.98] | 0.95 [0.90, 1.00] | - |

- Detection and localisation are at ceiling. The only plant that caused any trouble was the
  deleted goal, where the evidence is a mid-half kick-off from the centre spot: Opus and
  Muse missed its position a few times.
- The discriminating number is the false-alarm rate on clean data: Gemini 3%, Opus 10%,
  Muse 22%. Muse also ran out of its thinking budget on 30% of excerpts.
- Haiku 5.5 (sample of 20) shows the failure mode for a cheaper model: with thinking off it
  flagged every excerpt including all clean ones; with thinking on it found plants exactly
  but never concluded an excerpt was clean before running out of tokens.

## What this says

1. On explicit facts, current top models read the data. False labels and club names do not
   change factual answers.
2. On judgments, the hint leaks in a little. Without the season, a club name moves a
   predicted finish by about one place. With the season, memory of the real table moved
   it by four to six. Context that invites recall is a bigger risk than the name itself.
3. "Didn't follow the wrong hint" is not the same as "read the data". Muse's true-label
   result shows a model can resist hints by reflex. A control with a *correct* hint is
   needed to tell the two apart.
4. Anonymisation of a famous season is leaky, and stating the season makes it much worse.
   Team leakage fell from 55-75% to 0-10% when the season was dropped from the prompt.

## Limits

- One season of one league, and one that the models have seen. A less-covered league or a
  post-cutoff season would test reading with less memory available.
- Track 3 is saturated for top models; harder plants (subtler coordinates, two plants,
  longer excerpts) are needed to see differences.
- Muse Wonder is partial on tracks 1 and 3 and has no self-agreement estimate there.
- v1 tracks 1 and 3 still name the season. Track 1 has not been rerun without it.
- In v1 track 3 every plant sat between rows 9 and 21 of 40. v2 code spreads plants over
  all 40 rows, but track 3 has not been rerun yet because of cost.
- Low reasoning effort was forced by cost. Results may differ with full reasoning.
- Position truth is the lineup position, which is itself a label; a false 9 or inverted
  full-back is scored by the team sheet, not by how they played.
- Fable, Astra and Haiku numbers are 20-call samples and are not comparable.

## Reproduce

See README.md. Each version has its own folder: prompts/v1/ and prompts/v2/, raw answers in
results/v1/ and results/v2/, scores in results/<version>/scores.json, tables and charts in
reports/v1/ and reports/v2/. The version to build and run is set in config.yaml.
