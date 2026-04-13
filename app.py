import streamlit as st
import pandas as pd

st.title("🔥 LLM Evaluation Platform Dashboard")

df = pd.read_csv("results.csv")

st.write("### Full Results")
st.dataframe(df)

# ---------------------------
# METRICS
# ---------------------------
st.write("### Summary")

accuracy = df["score"].mean()
avg_latency = df["latency"].mean()

st.metric("Accuracy", round(accuracy, 2))
st.metric("Avg Latency (seconds)", round(avg_latency, 2))

# ---------------------------
# MODEL COMPARISON
# ---------------------------
st.write("### Model Comparison")

model_stats = df.groupby("model").mean(numeric_only=True)
st.dataframe(model_stats)