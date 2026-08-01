import streamlit as st

def hide_sidebar():
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)