from style import hide_sidebar
hide_sidebar()
import streamlit as st
import sqlite3
import os
import pandas as pd

st.set_page_config(
    page_title="AI Prediction",
    page_icon="🤖"
)

# Theme
st.markdown("""
<style>

.stApp{
    background:#f5f7fb;
}

h1{
    text-align:center;
    color:#b91c1c;
}

label, div[data-testid="stWidgetLabel"] p{
    color:#111827 !important;
    font-weight:600;
}

.stButton>button{
    width:100%;
    background:#dc2626;
    color:white !important;
    border-radius:10px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


st.title("🤖 AI Blood Stock Prediction")


# Database
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)

conn = sqlite3.connect(db_path)


# Get Stock Data
stock_data = pd.read_sql_query(
"""
SELECT blood_group, units
FROM blood_stock
""",
conn
)

conn.close()


if stock_data.empty:

    st.warning("No Blood Stock Available")

else:

    st.subheader("🩸 Current Blood Availability")

    st.dataframe(
        stock_data,
        use_container_width=True,
        hide_index=True
    )


    st.divider()

    st.subheader("🔮 AI Prediction Result")


    for _, row in stock_data.iterrows():

        group = row["blood_group"]
        units = row["units"]


        if units <= 5:

            st.error(
                f"🔴 {group}: Low Stock - Arrange Donation Camp"
            )

        elif units <= 10:

            st.warning(
                f"🟡 {group}: Medium Stock - Monitor Availability"
            )

        else:

            st.success(
                f"🟢 {group}: Stock Available"
            )


st.divider()


if st.button("⬅ Back to Home"):
    st.switch_page("pages/admin_home.py")