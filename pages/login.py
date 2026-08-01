from style import hide_sidebar
hide_sidebar()
import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🩸",
    layout="wide"
)

st.title("🩸 Blood Donation Management System")
st.subheader("Login to continue ❤️")

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    role = st.selectbox(
        "Select Role",
        ["Admin", "Hospital"]
    )

    username = st.text_input(
        "👤 Username"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )


    if st.button("🚀 Login", use_container_width=True):

        if role == "Admin":

            if username == "Admin" and password == "blood1234":

                st.session_state["role"] = "Admin"

                st.switch_page(
                    "pages/admin_home.py"
                )

            else:
                st.error("Invalid Admin Login")


        elif role == "Hospital":

            if username == "Hospital" and password == "hospital123":

                st.session_state["role"] = "Hospital"

                st.switch_page(
                    "pages/hospital_home.py"
                )

            else:
                st.error("Invalid Hospital Login")