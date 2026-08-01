from style import hide_sidebar
hide_sidebar()
import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(
    page_title="View All Donors",
    page_icon="📋",
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
st.title("📋 View All Donors")

# Database Path
db_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "blood_donation.db")
)

# Connect Database
conn = sqlite3.connect(db_path)

try:
    # Read Donor Data
    df = pd.read_sql_query(
        "SELECT * FROM donors",
        conn
    )

    conn.close()

    # Display Data
    if df.empty:
        st.warning("⚠️ No Donors Found!")
    else:
        st.success(f"Total Donors: {len(df)}")
        st.dataframe(
            df,
            use_container_width=True
        )

        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Donor List (CSV)",
            data=csv,
            file_name="donors.csv",
            mime="text/csv",
            use_container_width=True
        )

except Exception as e:
    conn.close()
    st.error("Database Error:")
    st.write(e)


# Back Button
if st.button("⬅ Back to Home", use_container_width=True):
    st.switch_page("pages/admin_home.py")