# ==========================================================
# 🚀 COSMIC MISSION CONTROL – FINAL POLISHED VERSION
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Cosmic Mission Control", layout="wide")

# ==========================================================
# 🌌 ADVANCED ANIMATED BACKGROUND
# ==========================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #000000, #0f2027, #1b2735, #090a0f);
    background-size: 400% 400%;
    animation: gradient 20s ease infinite;
    color: white;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: url('https://www.transparenttextures.com/patterns/stardust.png');
    animation: stars 200s linear infinite;
    opacity: 0.3;
    z-index: -1;
}
@keyframes stars {
    from {background-position: 0 0;}
    to {background-position: -10000px 5000px;}
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 COSMIC MISSION CONTROL SYSTEM")
st.markdown("Design missions. Analyze performance. Explore space.")

# ==========================================================
# 📂 SAFE DATA LOADING
# ==========================================================

@st.cache_data
def load_data():
    df = pd.read_csv("mission_data.csv")
    df.columns = df.columns.str.strip()
    df["Launch_Date"] = pd.to_datetime(df["Launch_Date"], errors="coerce")
    return df

df = load_data()

# ==========================================================
# 📊 KPI DASHBOARD
# ==========================================================

st.header("📊 Mission Overview")

col1, col2, col3, col4 = st.columns(4)

success_rate = round((df["Mission_Success"] == "Success").mean() * 100, 2)

col1.metric("Total Missions", len(df))
col2.metric("Success Rate (%)", success_rate)
col3.metric("Avg Budget (M$)", round(df["Estimated_Budget_Million"].mean(), 2))
col4.metric("Avg Scientific Yield", round(df["Scientific_Yield_Score"].mean(), 2))

# ==========================================================
# 🎛 FILTERS
# ==========================================================

st.sidebar.header("🔎 Filter Missions")

agency = st.sidebar.multiselect("Agency", df["Agency"].unique(), df["Agency"].unique())
destination = st.sidebar.multiselect("Destination", df["Destination"].unique(), df["Destination"].unique())

filtered_df = df[(df["Agency"].isin(agency)) & (df["Destination"].isin(destination))]

# ==========================================================
# 📈 VISUAL ANALYTICS
# ==========================================================

st.header("📈 Analytics Dashboard")

fig1 = px.bar(filtered_df, x="Agency", y="Estimated_Budget_Million", color="Agency",
              title="Budget by Agency")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(filtered_df, x="Estimated_Budget_Million", y="Scientific_Yield_Score",
                  size="Payload_kg", color="Agency",
                  hover_data=["Destination"],
                  title="Budget vs Scientific Yield")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(filtered_df.sort_values("Launch_Date"),
               x="Launch_Date", y="Estimated_Budget_Million",
               title="Budget Trend Over Time")
st.plotly_chart(fig3, use_container_width=True)

# ==========================================================
# 🚀 SIMULATION SECTION
# ==========================================================

st.header("🚀 Mission Simulation")

planet_gravity = {
    "Moon":1.62,"Mars":3.71,"Venus":8.87,"Jupiter":24.79,
    "Saturn":10.44,"Mercury":3.7,"Neptune":11.15,
    "Europa":1.31,"Titan":1.35,"Pluto":0.62
}

planet = st.selectbox("Select Planet", list(planet_gravity.keys()))
gravity = planet_gravity[planet]

thrust = st.slider("Thrust (N)", 5_000_000, 20_000_000, 10_000_000)
payload = st.slider("Payload (kg)", 10000, 80000, 30000)
fuel = st.slider("Fuel Mass (kg)", 100000, 500000, 300000)

if st.button("🚀 Launch Simulation"):

    st.success("Initiating Launch Sequence...")
    time.sleep(1)

    mass = 200000 + payload + fuel
    velocity = 0
    altitude = 0
    dt = 0.1

    results = []

    for t in range(300):
        acceleration = (thrust - mass*gravity) / mass
        velocity += acceleration * dt
        altitude += velocity * dt
        fuel -= 800
        mass -= 800
        if fuel <= 0:
            thrust = 0
        results.append([t, altitude, velocity])

    sim_df = pd.DataFrame(results, columns=["Time","Altitude","Velocity"])

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter3d(
        x=sim_df["Time"],
        y=sim_df["Velocity"],
        z=sim_df["Altitude"],
        mode='lines'
    ))

    fig_sim.update_layout(template="plotly_dark",
                          scene=dict(
                              xaxis_title="Time",
                              yaxis_title="Velocity",
                              zaxis_title="Altitude"
                          ))

    st.plotly_chart(fig_sim, use_container_width=True)

    if sim_df["Altitude"].iloc[-1] > 100000:
        st.success("🌍 Mission Successful!")
    else:
        st.error("❌ Mission Failed. Adjust thrust or fuel.")