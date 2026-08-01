import streamlit as st
import sqlite3
import os
from datetime import date


st.set_page_config(
    page_title="Donate Blood",
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

</style>
""", unsafe_allow_html=True)



st.title("🩸 Donate Blood")


# ---------- Database ----------
db_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "blood_donation.db"
)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()



# ---------- Donors ----------

cursor.execute("""
SELECT donor_id, name, blood_group
FROM donors
ORDER BY donor_id
""")


donors = cursor.fetchall()



if not donors:

    st.warning("⚠️ No Donors Available")

else:

    donor = st.selectbox(
        "👤 Select Donor",
        donors,
        format_func=lambda x: f"{x[0]} - {x[1]}"
    )


    units = st.number_input(
        "🩸 Blood Units Donated",
        min_value=1,
        max_value=5,
        value=1
    )


    st.markdown(
    f"""
    <div class="card">
    🩸 Blood Group : <b>{donor[2]}</b>
    </div>
    """,
    unsafe_allow_html=True
    )


    st.write("")


    if st.button("🩸 Donate Blood"):


        # Check Stock

        cursor.execute("""
        SELECT units FROM blood_stock
        WHERE blood_group=?
        """,
        (donor[2],))


        stock = cursor.fetchone()



        # Update or Insert Stock

        if stock:

            cursor.execute("""
            UPDATE blood_stock
            SET units = units + ?
            WHERE blood_group=?
            """,
            (units, donor[2]))

        else:

            cursor.execute("""
            INSERT INTO blood_stock
            (blood_group, units)
            VALUES (?,?)
            """,
            (donor[2], units))



        # Update Donation Date

        cursor.execute("""
        UPDATE donors
        SET last_donation=?
        WHERE donor_id=?
        """,
        (
            str(date.today()),
            donor[0]
        ))



        conn.commit()


        st.success(
            f"✅ {units}unit(s) of {donor[2]} blood added successfully!"
        )
conn.close()
st.divider()
if st.button("⬅ Back to Home"):
    st.switch_page("pages/admin_home.py")