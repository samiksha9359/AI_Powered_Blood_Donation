import streamlit as st
import os

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Blood Donation Management System",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #FFF8F8;
}

/* Hide Streamlit Default UI */
[data-testid="stSidebarNav"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* Main Container */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}


/* Title */
.title {
    text-align: center;
    color: #C62828;
    font-size: 46px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 10px;
}


/* Subtitle */
.subtitle {
    text-align: center;
    color: #555555;
    font-size: 21px;
    margin-bottom: 8px;
}


/* Quote */
.quote {
    text-align: center;
    color: #D32F2F;
    font-size: 20px;
    font-style: italic;
    margin-bottom: 25px;
}


/* Description */
.description {
    text-align: center;
    color: #666666;
    font-size: 16px;
    max-width: 750px;
    margin: auto;
    line-height: 1.6;
}


/* Get Started Button */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    border: none;
    background: #DC2626;
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}


.stButton > button:hover {
    background: #991B1B;
    transform: scale(1.02);
}


/* Small Footer Text */
.footer-text {
    text-align: center;
    color: #999999;
    font-size: 14px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGO
# =========================================================

logo_path = os.path.join(
    os.path.dirname(__file__),
    "Assets",
    "logo.png"
)


# Center Logo
logo_col1, logo_col2, logo_col3 = st.columns([1, 2, 1])

with logo_col2:
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    else:
        st.markdown(
            "<h1 style='text-align:center;'>🩸</h1>",
            unsafe_allow_html=True
        )


# =========================================================
# TITLE
# =========================================================

st.markdown(
    "<h1 class='title'>Blood Donation Management System</h1>",
    unsafe_allow_html=True
)


# =========================================================
# SUBTITLE
# =========================================================

st.markdown(
    "<p class='subtitle'>AI Powered Blood Donation App</p>",
    unsafe_allow_html=True
)


# =========================================================
# QUOTE
# =========================================================

st.markdown(
    "<p class='quote'>❤️ Donate Blood, Save Lives ❤️</p>",
    unsafe_allow_html=True
)


# =========================================================
# DESCRIPTION
# =========================================================

st.markdown(
    """
    <p class='description'>
    A smart blood donation management system designed to manage
    donors, blood requests, blood stock and donation-related activities
    efficiently.
    </p>
    """,
    unsafe_allow_html=True
)


st.write("")
st.write("")
st.write("")


# =========================================================
# GET STARTED BUTTON
# =========================================================

col1, col2, col3 = st.columns([1.5, 1, 1.5])

with col2:

    if st.button("🚀 Get Started", use_container_width=True):

        st.switch_page("pages/login.py")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    "<p class='footer-text'>Blood Donation Management System • AI Powered</p>",
    unsafe_allow_html=True
)