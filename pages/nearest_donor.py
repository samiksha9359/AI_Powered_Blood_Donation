import streamlit as st
import sqlite3
import os
import pandas as pd

st.set_page_config(
    page_title="Nearest Donor Finder",
    page_icon="📍",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background:#f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#b91c1c;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Title */
h1{
    text-align:center;
    color:#b91c1c;
    font-weight:bold;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    border:none;
    padding:12px;
    background:#dc2626;
    color:white;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#991b1b;
    transform:scale(1.02);
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea{
    border-radius:10px;
    border:1px solid #d1d5db;
}

/* Select Box */
.stSelectbox{
    border-radius:10px;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)
st.title("📍 Nearest Donor Finder")

db_path = os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")
conn = sqlite3.connect(db_path)

blood_group = st.selectbox(
    "🩸 Select Blood Group",
    ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
)

city = st.text_input("🏙️ Enter City")

if st.button("🔍 Find Donors", use_container_width=True):

    query = """
    SELECT
    donor_id,
    name,
    blood_group,
    phone,
    email,
    city,
    last_donation
    FROM donors
    WHERE blood_group=?
    AND LOWER(city)=LOWER(?)
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(blood_group, city.strip())
    )

    if df.empty:
        st.error("❌ No Donor Found")
    else:
        st.success(f"✅ {len(df)} Donor(s) Found")
        st.dataframe(df, use_container_width=True)

conn.close()

if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/admin_home.py")