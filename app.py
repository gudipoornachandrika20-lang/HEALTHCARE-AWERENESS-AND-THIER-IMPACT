import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT",
    layout="wide",
    initial_sidebar_state="expanded"
)

LOGO_FILE = "_Andhra_Pradesh logo.webp"
STRUCTURE_PLAN_IMG = "images/structure_plan.jpg"
THANK_YOU_IMG = "images/thank_you.jpg"

SINGLE_MEMBERS = [
    {
        "file": "images/member1_vindhya.jpg",
        "name": "G. Vindhya",
        "roll": "24JNA05234"
    },
    {
        "file": "images/member2_chandrika.jpg",
        "name": "G. Poorna Chandrika Reddy",
        "roll": "24JNA05267"
    },
    {
        "file": "images/member3_kousalya.jpg",
        "name": "G. Kousalya",
        "roll": "24JNA05251"
    },
    {
        "file": "images/member4_harshavardhini.jpg",
        "name": "G. Harshavardhini",
        "roll": "24JNA05271"
    }
]

GROUP_PHOTOS = [
    {
        "file": "images/group1.jpg",
        "line": "Interacting with local residents in Chakali Street, Nellore on personal hygiene and preventive healthcare."
    },
    {
        "file": "images/group2.jpg",
        "line": "Discussing child growth monitoring and early detection services with the doctor at Early Intervention Centre, Nellore."
    },
    {
        "file": "images/group3.jpg",
        "line": "Sharing maternal health, vaccination, and infant nutrition awareness in the ward at Government Hospital, Nellore."
    },
    {
        "file": "images/group4.jpg",
        "line": "Guiding mothers on childhood health check-ups, immunization schedules, and balanced nutrition."
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
    .member-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        margin-top: 8px;
    }
    .member-name {
        font-size: 16px;
        font-weight: 700;
        color: #111827;
    }
    .member-roll {
        font-size: 14px;
        color: #374151;
        margin-top: 2px;
    }
    .group-line {
        font-size: 14px;
        color: #1f2937;
        background: #f9fafb;
        border-left: 4px solid #2b2d31;
        padding: 8px 12px;
        margin-top: 6px;
        border-radius: 4px;
    }
    .thank-you-text {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 72px;
        font-weight: 700;
        font-style: italic;
        color: #111827;
        text-align: center;
        padding: 60px 20px;
        line-height: 1.1;
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
        "Baseline survey on health care and hygiene awareness",
        "Interacted with residents on regular check-ups, balanced diet and hygiene",
        "Collected information on government health schemes and medical facilities",
        "Session on disease prevention, vaccination and sanitation practices",
        "Household visits and pamphlets on nutrition and safe drinking water",
        "Reviewed weekly activities and collected community feedback",
        "Visited local communities to study dietary habits and food challenges",
        "Educational talks on healthy food versus junk food risks",
        "Distributed nutritious items including fruits, nuts and whole-grain snacks",
        "Cooking demonstrations and nutrition label reading workshop",
        "House visits spreading awareness on balanced diet and avoiding junk food",
        "Collected feedback from participants on the nutrition program",
        "Inspected locality to assess greenery and plant cover",
        "Distributed saplings to children in the locality",
        "Selected suitable planting places together with children and parents",
        "Explained benefits of trees in purifying air and releasing oxygen",
        "Guided children on daily watering and plant care",
        "Gathered plantation photos and encouraged planting more trees",
        "Visited houses to spread awareness on Swachh Bharat and cleanliness",
        "Identified area affected by dust and plastic waste",
        "Met municipal commissioner to request support for clean-up drive",
        "Coordinated with municipal workers to clean roads and drains",
        "Awareness campaign on waste segregation and mosquito-borne diseases",
        "Distributed sanitizers and hygiene materials to children and residents",
        "Visited Government Hospital and identified child and maternal health units",
        "Met hospital staff to obtain permission for awareness session",
        "Observed child screening and growth monitoring at Early Intervention Centre",
        "Interacted with doctor on early detection and regular check-ups",
        "Visited ward and spoke with mothers on nutrition, vaccination and anemia",
        "Prepared weekly report and collected staff feedback",
        "Identified homes for elderly people in the locality",
        "Visited elderly home to obtain permission for food distribution",
        "Distributed nutritious food to elderly residents",
        "Distributed healthy food at a second home for elderly residents",
        "Spent time with senior citizens and held session on healthy living",
        "Prepared final weekly report noting needs of elderly homes"
    ]
})

present_gen_df = pd.DataFrame({
    "Age Group": [
        "Present Generation (Youth & Students)",
        "Young Adults & Parents",
        "Middle-Aged Adults",
        "Senior Citizens"
    ],
    "Health_Awareness_%": [76, 68, 61, 54],
    "Healthy_Routine_%": [72, 64, 58, 52],
    "Junk_Food_Habit_%": [69, 55, 42, 30]
})

# --- SIDEBAR ---
with st.sidebar:
    c_l, c_r = st.columns([1, 3])
    with c_l:
        if os.path.exists(LOGO_FILE):
            st.image(LOGO_FILE, use_container_width=True)
    with c_r:
        st.markdown("### HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT")
        st.caption("CSP MINI PROJECT")

    st.markdown("---")
    st.caption("MAIN MENU")
    menu = st.radio(
        "Main Menu",
        [
            "Project Structure & Overview",
            "Day-Wise Logs",
            "Abstract",
            "Diagram & Modules",
            "Conclusion",
            "Graphs",
            "Team Members (Single Photos)",
            "Group Photos",
            "Thank You"
        ],
        label_visibility="collapsed"
    )

# --- TOP HEADER ---
b1, b2 = st.columns([1, 9])
with b1:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, width=82)
with b2:
    st.markdown("""
        <div class="top-banner">
            <div class="main-banner-title">HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT</div>
            <div class="main-banner-sub">Community Service Project — Chakali Street Sachivalayam 44/2, Government Hospital & Early Intervention Centre, Nellore</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="status-ok">Application is running successfully</div>', unsafe_allow_html=True)

# --- SECTIONS ---
if menu == "Project Structure & Overview":
    st.subheader("Project Structure Plan")
    if os.path.exists(STRUCTURE_PLAN_IMG):
        st.image(STRUCTURE_PLAN_IMG, caption="Project Flow: Topic Name, Day Logs, Abstract, Diagram, Modules, Conclusion & Graph", width=520)
    else:
        st.warning("Upload the project plan photo at `images/structure_plan.jpg`")

elif menu == "Day-Wise Logs":
    st.subheader("Day-Wise Activity Logs (Weeks 1 to 6)")
    selected_week = st.selectbox(
        "Select Week",
        ["All Weeks", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]
    )
    if selected_week == "All Weeks":
        st.dataframe(day_logs_df, use_container_width=True)
    else:
        st.dataframe(day_logs_df[day_logs_df["Week"] == selected_week], use_container_width=True)

elif menu == "Abstract":
    st.subheader("Abstract")
    st.write(
        "Health care awareness programs play an important role in improving community well-being by educating "
        "people on personal hygiene, sanitation, safe drinking water, balanced nutrition, and disease prevention. "
        "Field interactions in Chakali Street, Nellore, along with visits to the Government Hospital and Early "
        "Intervention Centre, highlighted the importance of timely medical advice, regular check-ups, and healthy "
        "daily routines."
    )
    st.write(
        "The project also focuses on early identification and support for physical and developmental conditions—such "
        "as cleft lip and cleft palate, clubfoot, cerebral palsy, spina bifida, hearing and visual impairments, "
        "Retinopathy of Prematurity (ROP) screening, anemia, and childhood health—supported by a simple health "
        "awareness website for sharing preventive guidance."
    )

elif menu == "Diagram & Modules":
    st.subheader("System Diagram & Modules")
    st.code(
        """
        [Fieldwork: Chakali Street, Govt. Hospital & Early Intervention Centre, Nellore]
                                         |
                                         v
                [HEALTH CARE AWARENESS PROGRAMS AND THEIR IMPACT]
                 |-- Home
                 |-- Types of Health (Physical, Mental, Social, Spiritual, Intellectual)
                 |-- Types of Health Problems & Hygiene
                 |-- Activities Done (6-Week Programs)
                 |-- Contact Us
        """,
        language="text"
    )

    st.markdown("#### Open Module Titles")
    t1, t2, t3, t4, t5 = st.tabs([
        "Home",
        "Types of Health",
        "Types of Health Problems",
        "Activities Done",
        "Contact Us"
    ])
    with t1:
        st.write("Overview of health care awareness, hygiene, and community impact in Nellore.")
    with t2:
        st.write("Physical, Mental, Social, Spiritual, and Intellectual health along with personal, environmental, and domestic hygiene.")
    with t3:
        st.write("Balanced nutrition, sleep habits, early screening, birth defects and disabilities awareness, ROP screening, and timely care.")
    with t4:
        st.write("Six-week activities covering baseline survey, nutrition, tree plantation, Swachh Bharat, hospital and early intervention visits, and elderly care.")
    with t5:
        st.write("Community Service Project — Sree Venkateswara College of Engineering, Nellore.")

elif menu == "Conclusion":
    st.subheader("Conclusion")
    st.write(
        "Health care awareness, clean surroundings, balanced nutrition, and timely medical check-ups help "
        "prevent illness and improve overall community health. Combining direct field outreach with simple "
        "digital awareness pages encourages families and children to adopt lasting healthy habits."
    )

elif menu == "Graphs":
    st.subheader("Present Generation Health & Lifestyle Graph")
    fig_gen = px.bar(
        present_gen_df,
        x="Age Group",
        y=["Health_Awareness_%", "Healthy_Routine_%", "Junk_Food_Habit_%"],
        barmode="group",
        title="How the Present Generation Compares Across Health & Lifestyle Indicators (%)"
    )
    st.plotly_chart(fig_gen, use_container_width=True)
    st.caption(
        "The present generation demonstrates higher health information access, while facing higher junk-food "
        "and sedentary routine exposure—highlighting the need for consistent nutrition and preventive habits."
    )

elif menu == "Team Members (Single Photos)":
    st.subheader("Team Members")
    cols = st.columns(4)
    for idx, member in enumerate(SINGLE_MEMBERS):
        with cols[idx]:
            if os.path.exists(member["file"]):
                st.image(member["file"], use_container_width=True)
            else:
                st.warning(f"Upload `{member['file']}`")
            st.markdown(f"""
                <div class="member-card">
                    <div class="member-name">{member['name']}</div>
                    <div class="member-roll">Roll No: {member['roll']}</div>
                </div>
            """, unsafe_allow_html=True)

elif menu == "Group Photos":
    st.subheader("Group Photographs")
    cols = st.columns(2)
    for idx, item in enumerate(GROUP_PHOTOS):
        with cols[idx % 2]:
            if os.path.exists(item["file"]):
                st.image(item["file"], use_container_width=True)
            else:
                st.warning(f"Upload `{item['file']}`")
            st.markdown(f'<div class="group-line">{item["line"]}</div>', unsafe_allow_html=True)

elif menu == "Thank You":
    if os.path.exists(THANK_YOU_IMG):
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image(THANK_YOU_IMG, use_container_width=True)
    else:
        st.markdown('<div class="thank-you-text">Thank you!</div>', unsafe_allow_html=True)
