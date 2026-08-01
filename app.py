import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Blood Donation Management System",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Main Background */
.stApp{
    background:#f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#b91c1c;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Title */
h1{
    text-align:center;
    color:#b91c1c;
    font-weight:bold;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    border:none;
    padding:12px;
    background:#dc2626;
    color:white;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    background:#991b1b;
    transform:scale(1.02);
}

/* Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea{
    border-radius:10px;
    border:1px solid #d1d5db;
}

/* Select Box */
.stSelectbox{
    border-radius:10px;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)
# Custom CSS
st.markdown("""
<style>
.stApp{
    background-color:#FFF8F8;
}

.title{
    text-align:center;
    color:#C62828;
    font-size:48px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#555555;
    font-size:22px;
}

.quote{
    text-align:center;
    color:#D32F2F;
    font-size:20px;
    font-style:italic;
}
</style>
""", unsafe_allow_html=True)

# Logo
st.markdown("<h1 style='text-align:center;'>🩸</h1>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>Blood Donation Management System</h1>", unsafe_allow_html=True)

# Quote
st.markdown("<p class='quote'>❤️ Donate Blood, Save Lives ❤️</p>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p class='subtitle'>AI Powered Blood Donation App</p>", unsafe_allow_html=True)

st.write("")
st.write("")

# Get Started Button
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🚀 Get Started", use_container_width=True):
        st.switch_page("pages/login.py")