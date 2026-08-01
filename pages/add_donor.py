from style import hide_sidebar
hide_sidebar()
from email_sender import send_email
import streamlit as st
import sqlite3
import os

st.set_page_config(
    page_title="Add Donor",
    page_icon="🩸",
    layout="wide"
)

# Database Connection
db_path = os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

st.title("👤 Add Donor")

# Auto Generate Donor ID
cursor.execute("""
SELECT donor_id
FROM donors
ORDER BY donor_id DESC
LIMIT 1
""")

last = cursor.fetchone()

if last:
    number = int(last[0][1:]) + 1
else:
    number = 1

donor_id = f"D{number:03d}"

st.text_input("🆔 Donor ID", value=donor_id, disabled=True)

# Donor Details
name = st.text_input("👤 Full Name")

age = st.number_input(
    "🎂 Age",
    min_value=18,
    max_value=65,
    value=18,
    step=1
)

st.write("Current Age :", age)

gender = st.selectbox(
    "⚧ Gender",
    ["Male", "Female", "Other"]
)

blood_group = st.selectbox(
    "🩸 Blood Group",
    ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)

phone = st.text_input("📱 Mobile Number")

email = st.text_input("📧 Email")

city = st.text_input("🏙️ City")

address = st.text_area("🏠 Address")

last_donation = st.date_input("🗓️ Last Donation Date")

# Save Button
if st.button("💾 Save Donor", use_container_width=True):

    if name.strip() == "":
        st.error("❌ Please Enter Full Name")

    elif age < 18:
        st.error("❌ Donor age must be at least 18 years.")

    elif len(phone) != 10 or not phone.isdigit():
        st.error("❌ Mobile Number must be exactly 10 digits.")

    elif email.strip() == "":
        st.error("❌ Please Enter Email")

    elif "@" not in email or "." not in email:
        st.error("❌ Please Enter a Valid Email")

    elif city.strip() == "":
        st.error("❌ Please Enter City")

    elif address.strip() == "":
        st.error("❌ Please Enter Address")

    else:

        # Check Duplicate Mobile
        cursor.execute(
            "SELECT * FROM donors WHERE phone=?",
            (phone,)
        )

        if cursor.fetchone():
            st.error("❌ Mobile Number Already Exists")

        else:

            # Check Duplicate Email
            cursor.execute(
                "SELECT * FROM donors WHERE email=?",
                (email,)
            )

            if cursor.fetchone():
                st.error("❌ Email Already Exists")

            else:

                cursor.execute("""
                INSERT INTO donors
                (
                    donor_id,
                    name,
                    age,
                    gender,
                    blood_group,
                    phone,
                    email,
                    city,
                    address,
                    last_donation
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    donor_id,
                    name,
                    age,
                    gender,
                    blood_group,
                    phone,
                    email,
                    city,
                    address,
                    str(last_donation)
                ))

                conn.commit()
                email_sent = send_email(email, name, blood_group)

                if email_sent:
                    st.success("✅ Donor Registered Successfully!")
                    st.info("📧 Confirmation Email Sent Successfully.")
                else:
                    st.success("✅ Donor Registered Successfully!")
                    st.warning("⚠ Registration completed, but email could not be sent.")

# Back Button
if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/admin_home.py")

conn.close()