import streamlit as st
import sqlite3
import os

st.set_page_config(
    page_title="Search Donor",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Search Donor")

# Database path
db_path = os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")

donor_id = st.text_input("🆔 Enter Donor ID (Example: D001)")


if st.button("🔎 Search", use_container_width=True):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

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
        st.write("📱 Mobile:", donor[5])
        st.write("📧 Email:", donor[6])
        st.write("🏙️ City:", donor[7])
        st.write("🏠 Address:", donor[8])

    else:
        st.error("Donor Not Found ❌")

    conn.close()


if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/home.py")