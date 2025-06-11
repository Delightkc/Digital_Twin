# app.py
import streamlit as st
import pandas as pd

st.title("🌡️ Smart Room Digital Twin Dashboard")

df = pd.read_csv("room_data.csv")
st.line_chart(df[['temperature', 'humidity']])
st.dataframe(df)
