from style import hide_sidebar
hide_sidebar()
from email_sender import send_approval_email
import streamlit as st
import sqlite3
import os
import pandas as pd

st.set_page_config(
    page_title="All Requests",
    page_icon="📋"
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


st.title("📋 All Blood Requests")


# Database
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Display Requests
df = pd.read_sql_query("""
SELECT *
FROM blood_requests
ORDER BY request_id
""", conn)


if df.empty:

    st.warning("No Requests Found")

else:

    search = st.text_input(
        "🔍 Search Request"
    )

    if search:
        df = df[
            df.astype(str)
            .apply(
                lambda x:x.str.contains(
                    search,
                    case=False
                ).any(),
                axis=1
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    st.divider()

    request_id = st.selectbox(
        "Select Request",
        df["request_id"]
    )


    status = st.selectbox(
        "Update Status",
        [
            "Pending",
            "Approved",
            "Rejected",
            "Completed"
        ]
    )


    if st.button("💾 Update Status"):

        cursor.execute("""
        SELECT blood_group, units, status, email, patient_name 
        FROM blood_requests
        WHERE request_id=?
        """,
        (request_id,))

        data = cursor.fetchone()
        blood_group = data[0]
        units = data[1]
        old_status = data[2]
        email = data[3]
        patient_name = data[4]

        if status=="Approved" and old_status!="Approved":

            blood_group = data[0]
            units = data[1]


            cursor.execute("""
            SELECT units
            FROM blood_stock
            WHERE blood_group=?
            """,
            (blood_group,))

            stock = cursor.fetchone()[0]


            if stock < units:
                st.error("❌ Not Enough Blood Stock")

            else:

                cursor.execute("""
                UPDATE blood_stock
                SET units = units - ?
                WHERE blood_group=?
                """,
                (units,blood_group))


                cursor.execute("""
                UPDATE blood_requests
                SET status=?
                WHERE request_id=?
                """,
                (status,request_id))


                conn.commit()

                email_sent = send_approval_email(
                    email,
                    patient_name,
                    blood_group,
                    units
                )

                if email_sent:
                    st.success("✅ Request Approved Successfully!")
                    st.info("📧 Approval Email Sent Successfully.")
                else:
                    st.success("✅ Request Approved Successfully!")
                    st.warning("⚠ Request approved, but email could not be sent.")

                st.rerun()

        else:

            cursor.execute("""
            UPDATE blood_requests
            SET status=?
            WHERE request_id=?
            """,
            (status,request_id))


            conn.commit()

            st.success("✅ Status Updated")
            st.rerun()



    if st.button("🗑 Delete Request"):

        cursor.execute("""
        DELETE FROM blood_requests
        WHERE request_id=?
        """,
        (request_id,))


        conn.commit()

        st.success("✅ Request Deleted")
        st.rerun()


conn.close()


if st.button("⬅ Back to Home"):
    st.switch_page("pages/admin_home.py")