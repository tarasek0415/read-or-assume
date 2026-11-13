# read-or-assume

Does an LLM read football event data, or assume? One thing in real data is changed on
purpose; code measures whether the answer follows the evidence or the hint.

Data: [StatsBomb open data](https://github.com/statsbomb/open-data), Premier League 2015/16.
Credit StatsBomb; non-commercial licence.

## Tracks
1. **Position labels** – player per-90 profile with no label / true label / false label two
   groups away. Headline: label-follow rate under false labels.
2. **Club names** – identical team profile shown as "Team K", a big club, a small club.
   Headline: flip rate when only the name changes.
3. **Data integrity** – 40 real consecutive events with one planted impossibility or none.
   Headline: detection by plant type and false-alarm rate on clean excerpts.

## Findings
Full write-up: [reports/writeup.md](reports/writeup.md).
- False position labels almost never win (1-2%), but one model contradicted *true* labels
  half the time: not following a wrong hint is not the same as reading the data.
- Club names moved predicted finish 4-6 places until the season was dropped from the
  prompt, then 1-2: most of the effect was memory of the real table.
- Open-weight models changed fixed, factual answers on 10-16% of questions when only the
  club name changed (closed models: 0%), and one moved a big club up ~6 places.
- Planted data errors are found at ceiling; false alarms on clean data separate the models
  (3% / 10% / 22%).
- Total cost $22.19, open-weight runs free. See the Cost and Future scope sections.

## Run
```
cp .env.example .env            # put OPENROUTER_API_KEY in it
uv run python data.py           # download + cache the season (once, ~15 min)
uv run python prompts.py        # build prompts/<version>/track{1,2,3}.jsonl
uv run python run.py --track 1 --model anthropic/claude-haiku-5.5 --limit 20
uv run python score.py && uv run python report.py
```
The runner reads only `.env` next to it, hard-codes the base URL, and asks before every paid batch.
