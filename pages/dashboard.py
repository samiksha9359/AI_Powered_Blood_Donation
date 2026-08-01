from style import hide_sidebar
hide_sidebar()
import streamlit as st
import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
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


st.title("📊 Blood Donation Dashboard")


# ---------- Database ----------
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# ---------- Data ----------

cursor.execute("SELECT COUNT(*) FROM donors")
total_donors = cursor.fetchone()[0]


cursor.execute("SELECT COUNT(*) FROM blood_requests")
total_requests = cursor.fetchone()[0]


cursor.execute(
    "SELECT COUNT(*) FROM blood_requests WHERE status='Pending'"
)
pending = cursor.fetchone()[0]


cursor.execute(
    "SELECT COUNT(*) FROM blood_requests WHERE status='Approved'"
)
approved = cursor.fetchone()[0]

cursor.execute("SELECT SUM(units) FROM blood_stock")
stock = cursor.fetchone()[0]

if stock is None:
    stock = 0


blood_data = pd.read_sql_query(
"""
SELECT blood_group, COUNT(*) AS total
FROM donors
GROUP BY blood_group
""",
conn
)


stock_data = pd.read_sql_query(
"""
SELECT blood_group, units
FROM blood_stock
WHERE units <= 5
""",
conn
)


conn.close()


# ---------- Cards ----------

# Top 3 Cards
# First Row
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👥 Total Donors", total_donors)

with c2:
    st.metric("🩸 Blood Stock", stock)

with c3:
    st.metric("📋 Total Requests", total_requests)


# Second Row
st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🕒 Pending Requests", pending)

with c2:
    st.metric("✅ Approved Requests", approved)

st.divider()


# ---------- Low Stock ----------

st.subheader("🚨 Low Stock Alert")


if stock_data.empty:
    st.success("✅ All blood groups have enough stock.")

else:
    for _,row in stock_data.iterrows():
        st.error(
            f"🔴 {row['blood_group']} : {row['units']} Units Left"
        )


st.divider()


# ---------- Chart ----------

st.subheader("🥧 Blood Group Distribution")


if not blood_data.empty:

    fig,ax = plt.subplots(figsize=(5,5))

    ax.pie(
        blood_data["total"],
        labels=blood_data["blood_group"],
        autopct="%1.1f%%"
    )

    ax.axis("equal")

    st.pyplot(fig)

else:
    st.info("No donor data available.")



st.divider()


# ---------- AI Insight ----------

st.subheader("🤖 AI Insight")


if stock < 10:
    st.warning(
        "⚠️ Blood stock is low. Arrange donation camp."
    )
else:
    st.success(
        "✅ Blood availability is stable."
    )



# ---------- Back Button ----------

if st.button("⬅ Back to Home"):
    st.switch_page("pages/admin_home.py")