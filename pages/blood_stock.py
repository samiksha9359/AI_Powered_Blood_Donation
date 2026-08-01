import streamlit as st
import sqlite3
import os
import pandas as pd


st.set_page_config(
    page_title="Blood Stock",
    page_icon="🩸",
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

.card h3{
    color:#111827;
}

.card p{
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)



st.title("🩸 Blood Stock Management")



# ---------- Database ----------

db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)


conn = sqlite3.connect(db_path)



# ---------- Fetch Stock ----------

data = pd.read_sql_query(
"""
SELECT blood_group, units
FROM blood_stock
ORDER BY blood_group
""",
conn
)



# ---------- Display Cards ----------

st.subheader("📦 Available Blood Stock")


if data.empty:

    st.warning("No Blood Stock Available")

else:

    cols = st.columns(4)

    for index,row in data.iterrows():

        with cols[index % 4]:

            if row["units"] <= 5:
                status = "🔴 Low Stock"

            elif row["units"] <= 10:
                status = "🟡 Medium"

            else:
                status = "🟢 Available"


            st.markdown(
            f"""
            <div class="card">

            <h2>🩸 {row['blood_group']}</h2>

            <h3>{row['units']} Units</h3>

            <p>{status}</p>

            </div>
            """,
            unsafe_allow_html=True
            )



st.divider()



# ---------- Low Stock Alert ----------

st.subheader("🚨 Stock Alert")


low_stock = data[data["units"] <= 5]


if low_stock.empty:

    st.success("✅ All blood groups have sufficient stock.")

else:

    for _,row in low_stock.iterrows():

        st.error(
            f"🔴 {row['blood_group']} has only {row['units']} units left"
        )



conn.close()



st.divider()


if st.button("⬅ Back to Home"):

    st.switch_page("pages/admin_home.py")