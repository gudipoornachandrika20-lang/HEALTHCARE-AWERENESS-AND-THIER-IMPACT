import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_FILE = "_Andhra_Pradesh logo.webp"

# Only group / field photographs placed in the `images/` folder
GROUP_PHOTOS = [
    {
        "file": "images/group_survey.jpg",
        "caption": "Group Fieldwork: Health & Hygiene Survey — Chakali Street, Nellore"
    },
    {
        "file": "images/group_hospital.jpg",
        "caption": "Group Visit: Government Hospital & Early Intervention Centre, Nellore"
    },
    {
        "file": "images/group_team.jpg",
        "caption": "CSP Group Team & Coordination Photo"
    }
]

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #2b2d31;
    }
    [data-testid="stSidebar"] * {
        color: #f1f3f5 !important;
    }
    .top-banner {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 12px 18px;
    }
    .main-banner-title {
        font-size: 25px;
        font-weight: 800;
        color: #111827;
        letter-spacing: 0.4px;
        margin: 0;
        line-height: 1.25;
    }
    .main-banner-sub {
        font-size: 13px;
        color: #4b5563;
        margin-top: 4px;
    }
    .status-ok {
        background-color: #edf7ed;
        color: #1e4620;
        border-radius: 6px;
        padding: 10px 14px;
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 16px;
    }
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 16px;
    }
    .kpi-label {
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 6px;
    }
    .kpi-val {
        font-size: 26px;
        font-weight: 700;
        color: #111827;
    }
    .thank-card {
        background: #f8fafc;
        border-left: 5px solid #2b2d31;
        border-radius: 8px;
        padding: 18px 20px;
        margin-top: 16px;
    }
    </style>
""", unsafe_allow_html=True)

day_logs_df = pd.DataFrame({
    "Week": [
        "Week 1", "Week 1", "Week 1", "Week 1", "Week 1", "Week 1",
        "Week 2", "Week 2", "Week 2", "Week 2", "Week 2", "Week 2",
        "Week 3", "Week 3", "Week 3", "Week 3", "Week 3", "Week 3",
        "Week 4", "Week 4", "Week 4", "Week 4", "Week 4", "Week 4",
        "Week 5", "Week 5", "Week 5", "Week 5", "Week 5", "Week 5",
        "Week 6", "Week 6", "Week 6", "Week 6", "Week 6", "Week 6"
    ],
    "Day & Date": [
        "Day 1 (01-06-2026)", "Day 2 (02-06-2026)", "Day 3 (03-06-2026)",
        "Day 4 (04-06-2026)", "Day 5 (05-06-2026)", "Day 6 (06-06-2026)",
        "Day 1 (08-06-2026)", "Day 2 (09-06-2026)", "Day 3 (10-06-2026)",
        "Day 4 (11-06-2026)", "Day 5 (12-06-2026)", "Day 6 (13-06-2026)",
        "Day 1 (15-06-2026)", "Day 2 (16-06-2026)", "Day 3 (17-06-2026)",
        "Day 4 (18-06-2026)", "Day 5 (19-06-2026)", "Day 6 (20-06-2026)",
        "Day 1 (22-06-2026)", "Day 2 (23-06-2026)", "Day 3 (24-06-2026)",
        "Day 4 (25-06-2026)", "Day 5 (26-06-2026)", "Day 6 (27-06-2026)",
        "Day 1 (29-06-2026)", "Day 2 (30-06-2026)", "Day 3 (01-07-2026)",
        "Day 4 (02-07-2026)", "Day 5 (03-07-2026)", "Day 6 (04-07-2026)",
        "Day 1 (06-07-2026)", "Day 2 (07-07-2026)", "Day 3 (08-07-2026)",
        "Day 4 (09-07-2026)", "Day 5 (10-07-2026)", "Day 6 (11-07-2026)"
    ],
    "Activity Summary": [
        "Baseline survey on health care & hygiene awareness",
        "Spoke with residents on check-ups, balanced diet & hygiene",
        "Gathered details on government health schemes & facilities",
        "Session on disease prevention, vaccination & sanitation",
        "House visits & pamphlets on nutrition and safe water",
        "Reviewed week activities & collected community feedback",
        "Studied local dietary habits & food challenges",
        "Talks on healthy food vs. junk food risks",
        "Distributed fruits, nuts & whole-grain healthy snacks",
        "Cooking demo & nutrition label reading workshop",
        "House visits on avoiding junk food & healthy meals",
        "Collected participant feedback & suggestions",
        "Checked plant cover in the locality",
        "Distributed saplings to children",
        "Identified planting spots with children & parents",
        "Explained benefits of trees, clean air & oxygen",
        "Guided children on daily watering responsibility",
        "Collected plantation photos & encouraged more planting",
        "House visits on Swachh Bharat & cleanliness",
        "Identified littered area with dust & plastic waste",
        "Discussed cleanliness & permission with municipal commissioner",
        "Coordinated with municipal workers to clean streets & drains",
        "Campaign on waste segregation & mosquito-borne diseases",
        "Distributed sanitizers & hygiene items",
        "Visited Government Hospital & identified key units",
        "Met hospital staff & obtained awareness permission",
        "Observed child screening & growth monitoring at Early Intervention Centre",
        "Interacted with doctor on early detection & regular check-ups",
        "Ward interaction with mother & infant on nutrition & vaccination",
        "Compiled weekly report & staff feedback",
        "Identified elderly care homes in the locality",
        "Obtained permission from elderly home staff",
        "Distributed nutritious food to elderly residents",
        "Distributed healthy food at another elderly home
