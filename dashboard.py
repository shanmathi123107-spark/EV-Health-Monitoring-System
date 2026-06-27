import os
from datetime import datetime
import streamlit as st
import pandas as pd
import random
from streamlit_autorefresh import st_autorefresh
st.set_page_config(page_title="EV Health Monitor", layout="wide")
st.sidebar.title("⚙️ Dashboard Menu")

st.sidebar.info("""
Project:
EV Health Monitoring System

Developer:
Shanmathi K

Version:
1.0
""")
count = st_autorefresh(interval=3000, key="refresh")
st.write("Refresh count:", count)
st.image("logo.png", width=120)
st.title("🚗 EV Health Monitoring System")
st.caption("Real-Time Electric Vehicle Monitoring Dashboard")

# Simulated EV Data
voltage = round(random.uniform(42, 54), 2)
current = round(random.uniform(0, 20), 2)
temperature = round(random.uniform(25, 50), 2)
battery = round((voltage / 54) * 100, 1)
if temperature < 40:
    battery_health = "Healthy ✅"
elif temperature < 45:
    battery_health = "Moderate ⚠️"
else:
    battery_health = "Critical 🔴"

new_data = pd.DataFrame({
    "Time": [datetime.now()],
    "Battery": [battery],
    "Voltage": [voltage],
    "Current": [current],
    "Temperature": [temperature]
})
st.subheader("🚗 EV Status")

if battery > 70:
    st.success("EV Status: Excellent")
elif battery > 40:
    st.info("EV Status: Normal")
else:
    st.warning("EV Status: Charging Recommended")
csv_file = "ev_data.csv"

if os.path.exists(csv_file):
    new_data.to_csv(csv_file, mode="a", header=False, index=False)
else:
    new_data.to_csv(csv_file, index=False)

# Metrics Row
col1, col2, col3, col4 = st.columns(4)

col1.metric("🔋 Battery", f"{battery}%")
col2.metric("⚡ Voltage", f"{voltage} V")
col3.metric("🔌 Current", f"{current} A")
col4.metric("🌡️ Temperature", f"{temperature} °C")
st.subheader("🔋 Battery Health Status")
st.write(battery_health)
# Alerts
if temperature > 45:
    st.error("⚠️ High Temperature Warning!")

if battery < 20:
    st.warning("🔋 Low Battery Warning!")

# Graph Data
data = pd.DataFrame({
    "Battery %": [random.uniform(60, 100) for _ in range(20)],
    "Voltage": [random.uniform(42, 54) for _ in range(20)],
    "Temperature": [random.uniform(25, 50) for _ in range(20)]
})

st.subheader("📈 EV Performance Trends")
st.line_chart(data)
st.subheader("📁 Logged EV Data")

history = pd.read_csv("ev_data.csv")

st.subheader("📊 Historical EV Trends")

history = pd.read_csv("ev_data.csv")

st.line_chart(
    history.tail(50).set_index("Time")[["Battery", "Voltage", "Temperature"]]
)