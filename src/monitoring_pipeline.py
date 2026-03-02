import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

def build_monitoring_snapshots():
    vendors = pd.read_csv(DATA_RAW / "vendors.csv")
    events = pd.read_csv(DATA_RAW / "risk_events.csv")

    daily = (events
             .groupby(["day", "vendor_id", "risk_category"])
             .size()
             .reset_index(name="event_count"))

    daily_total = (daily
                   .groupby(["day", "vendor_id"])["event_count"]
                   .sum()
                   .reset_index())

    df = daily_total.merge(vendors, on="vendor_id", how="left")

    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PROCESSED / "monitoring_snapshots.csv", index=False)
    print("Saved monitoring_snapshots.csv")

if __name__ == "__main__":
    build_monitoring_snapshots()
