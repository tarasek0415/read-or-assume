"""Turn results/scores.json into markdown tables and a few charts in reports/."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

ROOT = Path(__file__).parent
VERSION = yaml.safe_load(open(ROOT / "config.yaml"))["version"]
OUT = ROOT / "reports" / VERSION
HEADLINES = {  # track -> metrics worth a chart (name, label)
    1: [("false/all/label_follow", "Label-follow rate under false label"),
        ("none/all/accuracy", "Accuracy with no label")],
    2: [("big/flip_rate", "Flip rate: big-club name vs neutral"),
        ("big/finish_shift_vs_neutral", "Predicted finish shift, big-club name (neg = higher)"),
        ("small/finish_shift_vs_neutral", "Predicted finish shift, small-club name (pos = lower)")],
    3: [("any_plant/detected", "Detection rate (planted excerpts)"),
        ("clean/false_alarm", "False-alarm rate (clean excerpts)"),
        ("code_checkable/detected", "Detected: code-checkable plants"),
        ("football_sense/detected", "Detected: football-sense plants")],
}


def main():
    global VERSION, OUT
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=VERSION, help="result folder, e.g. v1 or v2")
    VERSION = ap.parse_args().version
    OUT = ROOT / "reports" / VERSION
    scores = json.loads((ROOT / "results" / VERSION / "scores.json").read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    md = ["# read-or-assume results\n", f"Data: StatsBomb open data, Premier League 2015/16. Version {VERSION}. "
          "Ranges are 95% bootstrap intervals over items.\n"]
    for t in (1, 2, 3):
        rows = {k.split("/", 1)[1]: v for k, v in scores.items() if k.startswith(f"track{t}/")}
        if not rows:
            continue
        md.append(f"\n## Track {t}\n")
        metrics = [m for m in next(iter(rows.values())) if any(r[m]["n"] for r in rows.values())]
        md.append("| metric | " + " | ".join(rows) + " |")
        md.append("|---|" + "---|" * len(rows))
        for m in metrics:
            cells = [f"{r[m]['mean']:.2f} [{r[m]['lo']:.2f}, {r[m]['hi']:.2f}]" if r[m]["n"] else "-"
                     for r in rows.values()]
            md.append(f"| {m} | " + " | ".join(cells) + " |")
        _chart(t, rows)
    (OUT / "results.md").write_text("\n".join(md))
    print("wrote", OUT / "results.md")


def _chart(t, rows):
    items = [(m, lbl) for m, lbl in HEADLINES[t] if any(r[m]["n"] for r in rows.values())]
    if not items:
        return
    fig, axes = plt.subplots(1, len(items), figsize=(4 * len(items), 3.5), squeeze=False)
    for ax, (m, lbl) in zip(axes[0], items):
        names = list(rows)
        means = [rows[n][m]["mean"] or 0 for n in names]
        err = [[(rows[n][m]["mean"] or 0) - (rows[n][m]["lo"] or 0) for n in names],
               [(rows[n][m]["hi"] or 0) - (rows[n][m]["mean"] or 0) for n in names]]
        ax.bar(range(len(names)), means, yerr=err, capsize=3, color="#4c72b0")
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels([n.split("_", 1)[-1] for n in names], rotation=30, ha="right", fontsize=8)
        if "shift" in m or "mae" in m:
            ax.axhline(0, color="black", linewidth=0.8)
        else:
            ax.set_ylim(0, 1)
        ax.set_title(lbl, fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / f"track{t}.png", dpi=150)


if __name__ == "__main__":
    main()
