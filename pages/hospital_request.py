import streamlit as st
import sqlite3
import os
from datetime import date

st.set_page_config(
    page_title="Hospital Request",
    page_icon="🏥"
)

# ---------- CSS ----------
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

st.title("🏥 Hospital Blood Request")

# ---------- Database ----------

db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ---------- Request ID ----------

cursor.execute("""
SELECT request_id
FROM blood_requests
ORDER BY request_id DESC
LIMIT 1
""")

last = cursor.fetchone()

if last:
    num = int(last[0][1:]) + 1
else:
    num = 1

request_id = f"R{num:03d}"

st.write("🆔 Request ID:", request_id)

# ---------- Form ----------

hospital_name = st.text_input("🏥 Hospital Name")

patient_name = st.text_input("👤 Patient Name")

blood_group = st.selectbox(
    "🩸 Blood Group",
    ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
)

units = st.number_input(
    "🩸 Required Units",
    min_value=1,
    max_value=10,
    value=1
)

phone = st.text_input("📱 Mobile Number")

email = st.text_input("📧 Hospital Email")

city = st.text_input("🏙️ City")

request_date = st.date_input(
    "📅 Date",
    value=date.today()
)

# ---------- Submit ----------

if st.button("📩 Submit Request"):

    if hospital_name.strip() == "":
        st.error("Enter Hospital Name")

    elif patient_name.strip() == "":
        st.error("Enter Patient Name")

    elif len(phone) != 10 or not phone.isdigit():
        st.error("Enter Valid Mobile Number")

    elif email.strip() == "":
        st.error("Enter Hospital Email")

    elif "@" not in email or "." not in email:
        st.error("Enter Valid Email Address")

    elif city.strip() == "":
        st.error("Enter City")

    else:

        cursor.execute("""
        INSERT INTO blood_requests
        (
        request_id,
        request_type,
        hospital_name,
        patient_name,
        blood_group,
        units,
        phone,
        email,
        city,
        request_date,
        status
        )
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            request_id,
            "Hospital",
            hospital_name,
            patient_name,
            blood_group,
            units,
            phone,
            email,
            city,
            str(request_date),
            "Pending"
        ))

        conn.commit()

        st.success("✅ Hospital Request Submitted Successfully!")

conn.close()

st.divider()

if st.button("⬅️ Back"):
    role = st.session_state.get("role")

    if role == "Admin":
        st.switch_page("pages/admin_home.py")

    elif role == "Hospital":
        st.switch_page("pages/hospital_home.py")

    else:
        st.error("Role not found")