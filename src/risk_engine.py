import pandas as pd
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

def load_config():
    with open(ROOT / "src" / "config.yaml", "r") as f:
        return yaml.safe_load(f)

def severity_to_score(sev):
    mapping = {"Low": 1, "Medium": 3, "High": 6, "Critical": 10}
    return mapping.get(sev, 0)

def compute_vendor_risk(cfg):
    vendors = pd.read_csv(DATA_RAW / "vendors.csv")
    events = pd.read_csv(DATA_RAW / "risk_events.csv")

    events["severity_score"] = events["severity"].apply(severity_to_score)

    weights = cfg["scoring"]["weights"]

    pivot = (events
             .groupby(["vendor_id", "risk_category"])["severity_score"]
             .sum()
             .unstack(fill_value=0))

    for cat in weights.keys():
        if cat not in pivot.columns:
            pivot[cat] = 0

    for cat, w in weights.items():
        pivot[f"{cat}_weighted"] = pivot[cat] * w

    pivot["composite_risk_score"] = pivot[[c for c in pivot.columns if c.endswith("_weighted")]].sum(axis=1)

    pivot = pivot.reset_index()
    df = vendors.merge(pivot, on="vendor_id", how="left").fillna(0)

    max_score = df["composite_risk_score"].max() or 1
    df["composite_risk_score_norm"] = (df["composite_risk_score"] / max_score * 100).round(1)

    def band(x):
        if x >= 75: return "Critical"
        if x >= 50: return "High"
        if x >= 25: return "Medium"
        return "Low"

    df["risk_band"] = df["composite_risk_score_norm"].apply(band)

    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PROCESSED / "vendor_risk_scores.csv", index=False)
    print("Saved vendor_risk_scores.csv")

if __name__ == "__main__":
    cfg = load_config()
    compute_vendor_risk(cfg)
