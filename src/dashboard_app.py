import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
DATA_PROCESSED = ROOT / "data" / "processed"

@st.cache_data
def load_data():
    vendors = pd.read_csv(DATA_PROCESSED / "vendor_risk_scores.csv")
    snapshots = pd.read_csv(DATA_PROCESSED / "monitoring_snapshots.csv")
    return vendors, snapshots

def main():
    st.set_page_config(page_title="Cyber Supply Chain Risk Monitor", layout="wide")
    st.title("Cyber Supply Chain Risk Monitoring Dashboard")

    vendors, snapshots = load_data()

    st.sidebar.header("Filters")
    tier_filter = st.sidebar.multiselect("Vendor Tier", options=vendors["tier"].unique().tolist(),
                                         default=vendors["tier"].unique().tolist())
    band_filter = st.sidebar.multiselect("Risk Band", options=vendors["risk_band"].unique().tolist(),
                                         default=vendors["risk_band"].unique().tolist())
    industry_filter = st.sidebar.multiselect("Industry", options=vendors["industry"].unique().tolist(),
                                             default=vendors["industry"].unique().tolist())

    filtered = vendors[
        vendors["tier"].isin(tier_filter) &
        vendors["risk_band"].isin(band_filter) &
        vendors["industry"].isin(industry_filter)
    ]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Vendors Monitored", len(filtered))
    with col2:
        st.metric("Tier 1 Vendors", (filtered["tier"] == "Tier 1").sum())
    with col3:
        st.metric("Critical Risk Vendors", (filtered["risk_band"] == "Critical").sum())
    with col4:
        st.metric("High Risk Vendors", (filtered["risk_band"] == "High").sum())

    col_a, col_b = st.columns(2)
    with col_a:
        fig_band = px.histogram(filtered, x="risk_band", color="tier",
                                title="Risk Band Distribution by Tier", barmode="group")
        st.plotly_chart(fig_band, use_container_width=True)

    with col_b:
        fig_industry = px.box(filtered, x="industry", y="composite_risk_score_norm",
                              color="tier", title="Risk Score by Industry")
        st.plotly_chart(fig_industry, use_container_width=True)

    st.subheader("Vendor Risk Table")
    st.dataframe(filtered[["vendor_id", "vendor_name", "tier", "industry",
                           "criticality_score", "composite_risk_score_norm", "risk_band"]]
                 .sort_values("composite_risk_score_norm", ascending=False),
                 use_container_width=True, height=400)

    st.subheader("Monitoring Trend – Events Over Time")
    snapshots["tier"] = snapshots["tier"].fillna("Unknown")
    trend = (snapshots
             .groupby(["day", "tier"])["event_count"]
             .sum()
             .reset_index())

    fig_trend = px.line(trend, x="day", y="event_count", color="tier",
                        title="Daily Risk Events by Tier")
    st.plotly_chart(fig_trend, use_container_width=True)

    st.subheader("Vendor Drill-down")
    vendor_choice = st.selectbox("Select Vendor", options=filtered["vendor_id"].tolist())
    v_meta = filtered[filtered["vendor_id"] == vendor_choice].iloc[0]

    st.write(f"**Vendor:** {v_meta['vendor_name']} ({v_meta['vendor_id']})")
    st.write(f"**Tier:** {v_meta['tier']} | **Industry:** {v_meta['industry']} | "
             f"**Risk Band:** {v_meta['risk_band']} | **Score:** {v_meta['composite_risk_score_norm']}")

    v_snap = snapshots[snapshots["vendor_id"] == vendor_choice]
    if not v_snap.empty:
        fig_v = px.bar(v_snap, x="day", y="event_count",
                       title="Daily Risk Events for Selected Vendor")
        st.plotly_chart(fig_v, use_container_width=True)
    else:
        st.info("No events recorded for this vendor.")

if __name__ == "__main__":
    main()
