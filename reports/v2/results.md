# read-or-assume results

Data: StatsBomb open data, Premier League 2015/16. Version v2. Ranges are 95% bootstrap intervals over items.


## Track 2

| metric | anthropic_claude-opus-5.5 | google_gemini-4-argon | meta_muse-wonder |
|---|---|---|---|
| bad_format | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| self_agreement | 0.81 [0.62, 1.00] | 0.81 [0.56, 1.00] | 0.50 [0.25, 0.75] |
| leak_rate | 0.00 [0.00, 0.00] | 0.10 [0.00, 0.25] | 0.10 [0.00, 0.25] |
| neutral/accuracy | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] |
| neutral/finish_mae | 2.00 [1.30, 2.75] | 1.70 [1.00, 2.45] | 2.50 [1.60, 3.50] |
| big/accuracy | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] |
| big/finish_mae | 2.25 [1.45, 3.15] | 2.10 [1.35, 2.90] | 2.60 [1.85, 3.50] |
| big/flip_rate | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| big/finish_shift_vs_neutral | -1.25 [-1.70, -0.75] | -0.50 [-1.10, 0.25] | -0.90 [-1.55, -0.30] |
| small/accuracy | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] |
| small/finish_mae | 2.75 [1.85, 3.75] | 4.30 [2.75, 6.00] | 2.80 [1.70, 4.05] |
| small/flip_rate | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] |
| small/finish_shift_vs_neutral | 0.85 [0.35, 1.35] | 2.10 [0.60, 3.85] | 0.70 [0.10, 1.30] |