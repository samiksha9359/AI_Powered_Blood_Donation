import streamlit as st

st.set_page_config(
    page_title="Hospital Home",
    page_icon="🏥"
)

# Access Control
if st.session_state.get("role") != "Hospital":
    st.error("Access Denied")
    st.stop()

st.title("🏥 Hospital Panel")

st.write("Welcome Hospital")

st.divider()

# Blood Request
if st.button("🩸 Hospital Blood Request", use_container_width=True):
    st.switch_page("pages/hospital_request.py")

st.divider()

# Logout
if st.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.switch_page("app.py")