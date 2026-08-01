from style import hide_sidebar
hide_sidebar()
import streamlit as st
import sqlite3
import os

st.set_page_config(
    page_title="Search Donor",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background:#f5f7fb;
}

/* Title */
h1{
    text-align:center;
    color:#b91c1c;
    font-weight:bold;
}

/* All Labels */
label, 
div[data-testid="stWidgetLabel"] p{
    color:#111827 !important;
    font-weight:600;
}

/* Input Box */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

/* Select Box */
div[data-baseweb="select"]{
    background:white !important;
}

div[data-baseweb="select"] *{
    color:black !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:45px;
    border-radius:10px;
    background:#dc2626;
    color:white !important;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#991b1b;
}

</style>
""", unsafe_allow_html=True)
# Database path
db_path = os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

st.title("🔍 Search Donor")

donor_id = st.text_input("🆔 Enter Donor ID (Example: D001)")


if st.button("🔎 Search", use_container_width=True):

    cursor.execute(
        "SELECT * FROM donors WHERE donor_id=?",
        (donor_id,)
    )

    donor = cursor.fetchone()

    if donor:
        st.success("Donor Found ✅")

        st.write("### 🩸 Donor Information")

        st.write("🆔 Donor ID:", donor[0])
        st.write("👤 Name:", donor[1])
        st.write("🎂 Age:", donor[2])
        st.write("⚧ Gender:", donor[3])
        st.write("🩸 Blood Group:", donor[4])
        st.write("📱 Phone:", donor[5])
        st.write("📧 Email:", donor[6])
        st.write("🏙️ City:", donor[7])
        st.write("🏠 Address:", donor[8])

    else:
        st.error("Donor Not Found ❌")


conn.close()


if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/admin_home.py")