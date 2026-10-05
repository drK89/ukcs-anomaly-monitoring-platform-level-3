from pathlib import Path
import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="UKCS Anomaly Monitoring", layout="wide")
st.title("UKCS Multi-Field Anomaly Monitoring")
st.caption("Portfolio screening for engineering review — not an operational alarm system")

scores = pd.read_csv(ROOT / "outputs/tables/portfolio_anomaly_scores.csv", parse_dates=["report_month"])
cases = pd.read_csv(ROOT / "outputs/tables/review_cases.csv", parse_dates=["report_month"])
clusters = pd.read_csv(ROOT / "outputs/tables/portfolio_clusters.csv", parse_dates=["report_month"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Scored field-months", len(scores))
col2.metric("Critical cases", int(cases.severity.eq("critical").sum()))
col3.metric("High cases", int(cases.severity.eq("high").sum()))
col4.metric("Cross-field clusters", int(clusters.portfolio_cluster_flag.sum()))

selected_fields = st.multiselect("Fields", sorted(scores.field_name.unique()), default=sorted(scores.field_name.unique()))
selected_severity = st.multiselect("Severity", ["critical", "high", "review"], default=["critical", "high"])

filtered_scores = scores.loc[scores.field_name.isin(selected_fields)]
filtered_cases = cases.loc[cases.field_name.isin(selected_fields) & cases.severity.isin(selected_severity)]

st.subheader("Risk score by field")
chart = filtered_scores.pivot(index="report_month", columns="field_name", values="risk_score_0_100")
st.line_chart(chart)

st.subheader("Prioritised review cases")
st.dataframe(filtered_cases[["case_id", "field_name", "report_month", "severity", "risk_score_0_100", "top_driver_1", "top_driver_2", "top_driver_3"]], use_container_width=True, hide_index=True)

st.subheader("Cross-field clusters")
st.dataframe(clusters.loc[clusters.portfolio_cluster_flag], use_container_width=True, hide_index=True)

st.subheader("Generated portfolio visuals")
st.image(str(ROOT / "outputs/charts/01_portfolio_risk_heatmap.png"), caption="Risk heatmap")

