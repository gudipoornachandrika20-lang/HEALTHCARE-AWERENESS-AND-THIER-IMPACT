import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Health Care Awareness Programs and Their Impact",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_FILE = "_Andhra_Pradesh logo.webp"

# Group / Field photos placed in repository root or an `images/` folder
GROUP_PHOTOS = [
    {
        "file": "images/week1_survey.jpg",
        "caption": "Week 1: Community & Hygiene Survey — Chakali Street, Nellore"
    },
    {
        "file": "images/week5_hospital.jpg",
        "caption": "Week 5: Awareness Visit — Government General Hospital & DEIC, Nellore"
    },
    {
        "file": "images/team_group.jpg",
        "caption": "CSP Team & Faculty / Coordination Group Photo"
    }
]

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
    }
    .header-subtitle {
        font-size: 14px;
        color: #5c677d;
        margin: 4px 0 0 0;
    }
    .thank-you-box {
        background-color: #eef4ff;
        border-left: 6px solid #162447;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, use_container_width=True)
    st.markdown("### HEALTH CARE AWARENESS")
    st.caption("Programs and Their Impact | CSP Mini Project")
    st.divider()
    section = st.radio(
        "Navigate Sections",
        [
            "Home & Abstract",
            "Day & Weekly Logs",
            "Architecture & Modules",
            "Present Generation Graph",
            "Group Photos",
            "Conclusion & Thank You"
        ],
        label_visibility="collapsed"
    )

# --- TOP HEADER ---
col_logo, col_title = st.columns([1, 9])
with col_logo:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=80)
with col_title:
    st.markdown("""
        <div class="header-title">HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT</div>
        <div class="header-subtitle">Community Service Project (CSP) — Chakali Street Sachivalayam 44/2, Govt. Hospital & DEIC, Nellore</div>
    """, unsafe_allow_html=True)

st.divider()

# --- DATA ---
weekly_logs_df = pd.DataFrame({
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"],
    "Period": [
        "01-06-2026 to 06-06-2026",
        "08-06-2026 to 13-06-2026",
        "15-06-2026 to 20-06-2026",
        "22-06-2026 to 27-06-2026",
        "29-06-2026 to 04-07-2026",
        "06-07-2026 to 11-07-2026"
    ],
    "Key Activity": [
        "Baseline health & hygiene survey, handwashing, safe water & health schemes awareness",
        "Nutrition & healthy diet vs. junk food awareness, healthy snacks & workshop",
        "Tree plantation drive with children & parents for clean air and green surroundings",
        "Swachh Bharat cleanliness drive, waste segregation, drain cleaning & sanitizers",
        "Govt. Hospital & DEIC visit: child screening, growth monitoring, maternal & anemia care",
        "Elderly care homes: nutritious food distribution, mental well-being & check-up guidance"
    ],
    "Awareness_Before_%": [40, 38, 45, 36, 42, 44],
    "Awareness_After_%": [82, 80, 85, 79, 86, 84]
})

generation_df = pd.DataFrame({
    "Age Group": [
        "Present Generation (Youth & Students)",
        "Young Adults & Parents",
        "Middle-Aged Adults",
        "Senior Citizens (Elderly)"
    ],
    "Preventive_Health_Awareness_%": [76, 68, 61, 54],
    "Healthy_Lifestyle_Adoption_%": [72, 64, 58, 52],
    "Junk_Food_Risk_Exposure_%": [69, 55, 42, 30]
})

# --- SECTIONS ---
if section == "Home & Abstract":
    st.subheader("📌 Topic & Abstract")
    st.markdown("**Topic Name:** Health Care Awareness Programs and Their Impact")

    st.markdown("#### Abstract")
    st.write(
        "Health care awareness programs play a vital role in improving community well-being by educating "
        "residents on personal hygiene, sanitation, safe drinking water, balanced nutrition, and disease "
        "prevention. Field interactions in Chakali Street, Nellore, along with visits to the Government "
        "Hospital and District Early Intervention Centre (DEIC), highlighted the importance of timely "
        "medical consultation, regular health check-ups, and healthy daily habits."
    )
    st.write(
        "The mini project also emphasizes early identification and care for developmental and health "
        "conditions—including cleft lip/palate, clubfoot, cerebral palsy, spina bifida, hearing/vision "
        "impairments, Retinopathy of Prematurity (ROP) screening, anemia, and childhood conditions—alongside "
        "a simple health education website to share preventive guidance with families."
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("CSP Duration", "6 Weeks")
    m2.metric("Field Locations", "3 Centers (Nellore)")
    m3.metric("Core Modules", "5 Modules")

elif section == "Day & Weekly Logs":
    st.subheader("🗓️ Day-Wise & Weekly Activity Summary")
    st.dataframe(weekly_logs_df, use_container_width=True)

    selected_week = st.selectbox("Select a Week to View Day-by-Day Highlights", weekly_logs_df["Week"])
    row = weekly_logs_df[weekly_logs_df["Week"] == selected_week].iloc[0]
    st.info(f"**{row['Week']} ({row['Period']}):** {row['Key Activity']}")

elif section == "Architecture & Modules":
    st.subheader("🧩 System Architecture & Modules")
    st.code(
        """
        [Community & Hospital Fieldwork (Nellore)]
                         │
                         ▼
        [Health Care Awareness & Impact Platform]
         ├── 1. Home
         ├── 2. Types of Health (Physical, Mental, Social, Spiritual, Intellectual)
         ├── 3. Types of Health Problems & Hygiene (Oral, Personal, Nutrition, Early Screening)
         ├── 4. Activities Done (6-Week Field & Hospital Initiatives)
         └── 5. Contact Us
        """,
        language="text"
    )

    st.markdown("#### Open a Module Title Below")
    t1, t2, t3, t4, t5 = st.tabs([
        "Home",
        "Types of Health",
        "Types of Health Problems",
        "Activities Done",
        "Contact Us"
    ])
    with t1:
        st.write("Overview of health care awareness, preventive care, and community impact in Nellore.")
    with t2:
        st.write("Covers Physical, Mental, Social, Spiritual, and Intellectual health along with personal, environmental, and domestic hygiene.")
    with t3:
        st.write("Highlights balanced diet, sleep habits, early screening, birth defects/disabilities awareness, ROP screening, and timely medical care.")
    with t4:
        st.write("Summarizes Week 1 to Week 6 activities across Chakali Street, Swachh Bharat drives, Government Hospital, DEIC, and elderly homes.")
    with t5:
        st.write("Community Service Project — Sree Venkateswara College of Engineering (SVCN), Nellore.")

elif section == "Present Generation Graph":
    st.subheader("📊 Present Generation & Age-Group Health Awareness")
    fig_gen = px.bar(
        generation_df,
        x="Age Group",
        y=["Preventive_Health_Awareness_%", "Healthy_Lifestyle_Adoption_%", "Junk_Food_Risk_Exposure_%"],
        barmode="group",
        title="How the Present Generation Compares Across Health Indicators (%)"
    )
    st.plotly_chart(fig_gen, use_container_width=True)

    st.caption(
        "Observation: The present generation has stronger digital and general awareness, yet faces higher "
        "exposure to packaged/junk food and irregular routines—making practical nutrition and preventive habits essential."
    )

elif section == "Group Photos":
    st.subheader("📸 Group & Field Activity Photographs")
    cols = st.columns(3)
    for idx, item in enumerate(GROUP_PHOTOS):
        with cols[idx % 3]:
            if os.path.exists(item["file"]):
                st.image(item["file"], caption=item["caption"], use_container_width=True)
            else:
                st.warning(f"Add photo at `{item['file']}`")
                st.caption(item["caption"])

elif section == "Conclusion & Thank You":
    st.subheader("✅ Conclusion")
    st.write(
        "Consistent health care awareness, clean surroundings, balanced nutrition, and early medical "
        "check-ups help prevent illness and build healthier communities. Combining field outreach with "
        "accessible digital health resources supports lasting positive impact."
    )
    st.markdown("""
        <div class="thank-you-box">
            <h3>🙏 Thank You</h3>
            <p>Thank you to our faculty guide, department, community members of Chakali Street, Government Hospital & DEIC staff, and everyone who supported this Health Care Awareness project.</p>
        </div>
    """, unsafe_allow_html=True)
