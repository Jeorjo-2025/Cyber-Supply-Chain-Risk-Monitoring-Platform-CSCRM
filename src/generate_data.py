import numpy as np
import pandas as pd
from faker import Faker
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"

fake = Faker()

def load_config():
    with open(ROOT / "src" / "config.yaml", "r") as f:
        return yaml.safe_load(f)

def generate_vendors(cfg):
    n = cfg["vendors"]["n_vendors"]
    tier1_ratio = cfg["vendors"]["tier1_ratio"]
    industries = cfg["vendors"]["industries"]

    vendor_ids = [f"V{str(i).zfill(4)}" for i in range(1, n + 1)]
    tiers = np.where(np.random.rand(n) < tier1_ratio, "Tier 1", "Tier 2/3")
    criticality_score = np.where(tiers == "Tier 1",
                                 np.random.randint(80, 101, n),
                                 np.random.randint(30, 81, n))

    df = pd.DataFrame({
        "vendor_id": vendor_ids,
        "vendor_name": [fake.company() for _ in range(n)],
        "industry": np.random.choice(industries, size=n),
        "tier": tiers,
        "criticality_score": criticality_score,
        "country": [fake.country() for _ in range(n)]
    })
    return df

def generate_risk_events(cfg, vendors_df):
    n_days = cfg["monitoring"]["n_days"]
    base_prob = cfg["monitoring"]["base_event_prob"]
    tier1_mult = cfg["monitoring"]["tier1_multiplier"]
    categories = cfg["risk_categories"]

    records = []
    for _, row in vendors_df.iterrows():
        vendor_id = row["vendor_id"]
        tier = row["tier"]
        prob = base_prob * (tier1_mult if tier == "Tier 1" else 1.0)

        for day in range(n_days):
            if np.random.rand() < prob:
                category = np.random.choice(categories, p=[0.3, 0.25, 0.3, 0.15])
                severity = np.random.choice(["Low", "Medium", "High", "Critical"],
                                            p=[0.4, 0.3, 0.2, 0.1])
                records.append({
                    "vendor_id": vendor_id,
                    "day": day,
                    "risk_category": category,
                    "severity": severity
                })

    return pd.DataFrame(records)

def main():
    cfg = load_config()
    DATA_RAW.mkdir(parents=True, exist_ok=True)

    vendors_df = generate_vendors(cfg)
    vendors_df.to_csv(DATA_RAW / "vendors.csv", index=False)

    risk_events_df = generate_risk_events(cfg, vendors_df)
    risk_events_df.to_csv(DATA_RAW / "risk_events.csv", index=False)

    print("Generated vendors.csv and risk_events.csv")

if __name__ == "__main__":
    main()
