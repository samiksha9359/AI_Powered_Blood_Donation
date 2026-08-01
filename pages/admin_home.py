import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Blood Donation System",
    page_icon="🩸",
    layout="wide"
)

# ---------------- CSS ----------------
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
.main-title{
    text-align:center;
    font-size:35px;
    font-weight:bold;
    color:#b91c1c;
    margin-top:20px;
}

.sub-title{
    text-align:center;
    font-size:18px;
    color:#374151;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.card h2{
    color:#b91c1c;
}

.footer{
    text-align:center;
    color:#b91c1c;
    font-weight:bold;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
"""
<div class="main-title">
🩸 AI Powered Blood Donation System
</div>

<div class="sub-title">
🤖 Smart Blood Bank Management | Saving Lives Through Technology
</div>

""",
unsafe_allow_html=True
)


# ---------------- STATS ----------------

col1,col2,col3,col4 = st.columns(4)


with col1:
    st.markdown("""
    <div class="card">
    <h2>👥</h2>
    <h2>Donors</h2>
    <p>Manage Donors</p>
    </div>
    """,unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="card">
    <h2>🩸</h2>
    <h2>Stock</h2>
    <p>Blood Availability</p>
    </div>
    """,unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="card">
    <h2>🏥</h2>
    <h2>Requests</h2>
    <p>Patient Needs</p>
    </div>
    """,unsafe_allow_html=True)


with col4:
    st.markdown("""
    <div class="card">
    <h2>🤖</h2>
    <h2>AI</h2>
    <p>Smart Prediction</p>
    </div>
    """,unsafe_allow_html=True)



st.divider()



# ---------------- NAVIGATION ----------------

st.subheader("🚀 Quick Access")


buttons = [

("👤 Add Donor","pages/add_donor.py"),
("🔍 Search Donor","pages/search_donor.py"),

("📋 View All Donors","pages/view_donors.py"),
("✏️ Update Donor","pages/update_donor.py"),

("🗑 Delete Donor","pages/delete_donor.py"),
("🩸 Donate Blood","pages/donate_blood.py"),

("🏥 Hospital Request","pages/hospital_request.py"),
("📋 All Requests","pages/all_requests.py"),

("📊 Dashboard","pages/dashboard.py"),
("🤖 AI Prediction","pages/ai_prediction.py"),

("📍 Nearest Donor","pages/nearest_donor.py"),
("📊 Blood stock","pages/blood_stock.py"),

("🚪 Logout","app.py")

]


for i in range(0,len(buttons),2):

    col1,col2 = st.columns(2)

    with col1:
        name,path = buttons[i]

        if st.button(name,use_container_width=True):
            st.switch_page(path)


    with col2:
        if i+1 < len(buttons):

            name,path = buttons[i+1]

            if st.button(name,use_container_width=True):
                st.switch_page(path)



st.divider()


st.markdown(
"""
<div class="footer">

❤️ Every Drop Counts • Every Donor Matters ❤️

<br><br>

© 2026 AI Powered Blood Donation Management System

</div>
""",
unsafe_allow_html=True
)