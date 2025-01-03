import streamlit as st
import requests
import pandas as pd
import time
from visualizations import plot_race_positions

st.set_page_config(page_title="F1 Race Dashboard", layout="wide")

st.title("🏎️ F1 Race Strategy & Live Tracking")

# Sidebar Controls
st.sidebar.header("Race Settings")
driver = st.sidebar.selectbox("Select Driver:", ["Verstappen", "Hamilton", "Leclerc", "Russell"])
driver_style = st.sidebar.selectbox("Driving Style:", ["Aggressive", "Balanced", "Conservative"])
tyre_type = st.sidebar.selectbox("Tyre Type:", ["Soft", "Medium", "Hard", "Intermediate", "Wet"])
total_laps = st.sidebar.slider("Total Laps:", 10, 70, 50)

# Fetch Strategy Data
if st.sidebar.button("Get Strategy"):
    api_url = f"http://127.0.0.1:8000/strategy?driver={driver}&driver_style={driver_style}&tyre_type={tyre_type}&total_laps={total_laps}"
    response = requests.get(api_url)
    strategy = response.json()
    
    st.subheader("🚀 Recommended Race Strategy")
    st.json(strategy)

# Real-Time Race Tracking
st.subheader("🏁 Live Race Positions")
drivers = ["Verstappen", "Hamilton", "Leclerc"]
positions = {driver: {"x": [], "y": []} for driver in drivers}

chart = st.empty()

for i in range(50):
    for driver in drivers:
        positions[driver]["x"].append(i)
        positions[driver]["y"].append(i * 0.8 if driver == "Verstappen" else i * 0.75)
    
    fig = plot_race_positions(drivers, positions)
    chart.plotly_chart(fig)
    time.sleep(0.5)
