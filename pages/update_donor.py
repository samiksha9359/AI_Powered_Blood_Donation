import streamlit as st
import sqlite3
import os

st.set_page_config(
    page_title="Update Donor",
    page_icon="✏️",
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
st.title("✏️ Update Donor")

# Database path
db_path = os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

donor_id = st.text_input("🆔 Enter Donor ID")

if st.button("🔍 Search Donor"):

    cursor.execute(
        "SELECT * FROM donors WHERE donor_id=?",
        (donor_id,)
    )

    donor = cursor.fetchone()

    if donor:
        st.session_state.donor = donor
        st.success("Donor Found ✅")

    else:
        st.error("Donor Not Found ❌")


if "donor" in st.session_state:

    donor = st.session_state.donor

    name = st.text_input("👤 Name", donor[1])
    age = st.number_input("🎂 Age", value=donor[2])

    gender = st.selectbox(
        "⚧ Gender",
        ["Male", "Female", "Other"],
        index=["Male","Female","Other"].index(donor[3])
    )

    blood_group = st.selectbox(
        "🩸 Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        index=["A+","A-","B+","B-","AB+","AB-","O+","O-"].index(donor[4])
    )

    phone = st.text_input("📱 Mobile", donor[5])
    email = st.text_input("📧 Email", donor[6])
    city = st.text_input("🏙️ City", donor[7])
    address = st.text_area("🏠 Address", donor[8])


    if st.button("💾 Update", use_container_width=True):

        cursor.execute("""
        UPDATE donors SET
        name=?,
        age=?,
        gender=?,
        blood_group=?,
        phone=?,
        email=?,
        city=?,
        address=?
        WHERE donor_id=?
        """,
        (
            name, age, gender, blood_group,
            phone, email, city, address,
            donor_id
        ))

        conn.commit()

        st.success("Donor Updated Successfully! 🎉")


if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/admin_home.py")

conn.close()