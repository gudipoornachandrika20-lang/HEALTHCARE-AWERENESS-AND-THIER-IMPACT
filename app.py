import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Health Care Awareness & Impact",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_FILE = "_Andhra_Pradesh logo.webp"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #162447;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    .header-title {
        font-size: 26px;
        font-weight: 800;
        color: #1b263b;
        margin: 0;
        letter-spacing: 0.5px;
    }
    .header-subtitle {
        font-size: 14px;
        color: #5c677d;
        margin: 2px 0 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
        else:
            st.markdown("## 🏥")
    st.markdown("<h3 style='text-align: center; margin-bottom: 0;'>AP HEALTH AWARENESS</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 11px; color: #adb5bd !important;'>HEALTHCARE AWARENESS & IMPACT</p>", unsafe_allow_html=True)
    st.divider()
    st.markdown("**MAIN MENU**")
    menu = st.radio(
        "Navigation",
        ["Dashboard", "Awareness Programs", "District Monitoring", "Impact Analysis", "Health Assistant"],
        label_visibility="collapsed"
    )

# --- TOP HEADER ---
top_col1, top_col2 = st.columns([1, 9])
with top_col1:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=85)
    else:
        st.markdown("# 🏥")
with top_col2:
    st.markdown("""
        <div style="padding-top: 8px;">
            <div class="header-title">ANDHRA PRADESH - HEALTH CARE AWARENESS</div>
            <div class="header-subtitle">Community Health Care Awareness Programs and Impact Monitoring System</div>
        </div>
    """, unsafe_allow_html=True)

st.success("Application is running successfully")

# --- DATA ---
data = pd.DataFrame({
    "District": ["Nellore", "Guntur", "Visakhapatnam", "Tirupati", "Kurnool"],
    "Program": ["Maternal Nutrition", "Anemia Prevention", "Child Immunization", "Hygiene & Sanitation", "Diabetes Screening"],
    "Participants": [1250, 1580, 1920, 1400, 1650],
    "Before_Awareness_%": [42, 38, 50, 45, 40],
    "After_Awareness_%": [84, 81, 89, 86, 82],
    "Checkups_Done": [980, 1210, 1700, 1150, 1340]
})

# --- PAGES ---
if menu == "Dashboard":
    st.subheader("📊 Monitoring Dashboard")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Programs", len(data))
    m2.metric("Total Participants", f"{data['Participants'].sum():,}")
    m3.metric("Checkups Completed", f"{data['Checkups_Done'].sum():,}")
    m4.metric("Avg Impact Gain", "+41.4%")

    st.divider()
    st.subheader("📈 Awareness Impact: Before vs After Program")
    fig = px.bar(
        data,
        x="Program",
        y=["Before_Awareness_%", "After_Awareness_%"],
        barmode="group",
        color_discrete_sequence=["#8d99ae", "#162447"]
    )
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Awareness Programs":
    st.subheader("🩺 Active Health Care Awareness Programs")
    st.dataframe(data, use_container_width=True)

elif menu == "District Monitoring":
    st.subheader("📍 District-Wise Reach")
    district = st.selectbox("Select District", data["District"].unique())
    st.table(data[data["District"] == district])

elif menu == "Impact Analysis":
    st.subheader("📉 Program Impact Comparison")
    fig_pie = px.pie(data, names="District", values="Participants", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

elif menu == "Health Assistant":
    st.subheader("💬 Community Health Info")
    st.info("Select a program from the sidebar to view awareness guidelines and district statistics.")
