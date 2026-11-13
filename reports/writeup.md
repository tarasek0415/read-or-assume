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
- Open-weight models on track 2 (v2): Nemotron 3 Ultra and Nemotron 3.5 Super, through
  OpenRouter's free tier, thinking off.
- Total spend: $22.19 on OpenRouter (see Cost). The open-weight runs cost nothing.

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

### Track 2 (v2), open-weight models: the name changes facts, not just judgments

Same 96 prompts, run on free open-weight models.

| | Nemotron 3 Ultra | Nemotron 3.5 Super | closed models (above) |
|---|---|---|---|
| accuracy on 8 yes/no questions, "Team K" | 1.00 | 0.89 [0.85, 0.94] | 1.00 |
| flip rate, big-club name | 0.10 [0.06, 0.15] | 0.11 [0.06, 0.15] | 0.00 |
| flip rate, small-club name | 0.00 | 0.16 [0.10, 0.21] | 0.00 |
| predicted-finish error, "Team K" (places) | 3.1 [2.0, 4.2] | 3.0 [2.0, 4.2] | 1.7-2.5 |
| shift in predicted finish, big-club name | **-5.9 [-8.7, -3.3]** | -1.5 [-3.1, 0.2] | -0.5 to -1.3 |
| shift in predicted finish, small-club name | +2.1 [-0.7, 5.0] | +1.1 [-0.5, 2.5] | +0.7 to +2.1 |
| leakage (named the club from "Team K") | 0.05 [0.00, 0.15] | 0.05 [0.00, 0.15] | 0.00-0.10 |
| self-agreement (16 repeats) | 0.94 [0.81, 1.00] | 0.94 [0.81, 1.00] | 0.50-0.81 |

- The closed models never changed a factual answer when only the club name changed. Both
  open models did, on 10-16% of questions whose answer is fixed by the numbers.
- Nemotron 3 Ultra moved a big-club team up about six places, with the season already
  removed. That is the v1 effect size again, now from the name alone.
- Both open models were *more* self-consistent than the closed ones (0.94 vs 0.50-0.81).
  Consistent is not the same as right: they repeat the same name-driven answer.
- Gemma 4 31B was also tried but the free tier was rate-limited upstream for almost every
  call, so it has no usable results.

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
5. The gap between models shows up in the hint, not the facts. With neutral names every
   model answers the factual questions well; with a famous name, the open models start
   changing facts and one moves its predicted finish by six places.

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

## Cost

The whole study ran on a personal budget, so cost shaped the design.

| Model | Calls | Spend | per call |
|---|---|---|---|
| Claude Opus 5.5 | 1,204 | $9.27 | $0.008 |
| Muse Wonder | 742 | $8.39 | $0.011 |
| Gemini 4 Argon | 1,204 | $2.47 | $0.002 |
| Claude Fable 5.1 (sample) | 60 | $1.11 | $0.019 |
| GPT-6 Astra (sample) | 60 | $0.94 | $0.016 |
| Claude Haiku 5.5 (sample) | 60 | $0.01 | <$0.001 |
| Nemotron 3 Ultra, Nemotron 3.5 Super (free tier) | 192 | $0.00 | $0 |
| **Total** | | **$22.19** | |

- A full run of all six closed models on all three tracks would have cost about $65. The
  design spent where the result was decided: two cheap-per-call models on everything, the
  expensive thinking model where it mattered, 20-call samples for the rest.
- Guards in `run.py`: `--estimate` prints the cost before anything runs, every paid batch
  asks y/N, a hard cap ($20) stops a run, and answers are cached so a rerun never pays twice.
- Muse Wonder spent ~10x the tokens per call on thinking, which is why it is partial on
  tracks 1 and 3. Cheaper per token is not cheaper per answer.
- Free open-weight tiers cost nothing but allow ~20 calls a minute and ~1,000 a day, so a
  full open-model run takes days, and one provider (Gemma) was unusable on the free tier.

## Future scope

- **A correct-hint control everywhere.** Track 1 shows a model can "resist" a false label by
  reflex. Every track should pair the false hint with a true one.
- **Less memory, more reading.** A post-cutoff season or a less-covered league (StatsBomb
  also has women's and international competitions) to separate reading from recall.
- **Rerun tracks 1 and 3 without the season,** and run the open models on them as free
  quotas allow.
- **Harder integrity plants** (subtler coordinates, two plants, longer excerpts) so track 3
  separates models again.
- **Full reasoning effort** on a subset, to test whether thinking budget changes how much
  the hint leaks in.
- **Open models on paid providers** (DeepSeek, Gemma) for a fuller open-vs-closed picture.

## Reproduce

See README.md. Each version has its own folder: prompts/v1/ and prompts/v2/, raw answers in
results/v1/ and results/v2/, scores in results/<version>/scores.json, tables and charts in
reports/v1/ and reports/v2/. The version to build and run is set in config.yaml.
