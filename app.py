import streamlit as st
from menu_editor import show_menu_management
from chat_agent import chat_agent

#st.set_page_config(page_title="🍽 ChatFood AI", layout="centered")

st.set_page_config(page_title="ChatFood AI", page_icon="🍽️", layout="wide")

# Sidebar login
with st.sidebar:
    st.title("🔑 Admin Panel Login")
    if "is_admin" not in st.session_state:
        st.session_state.is_admin = False

    if not st.session_state.is_admin:
        password_input = st.text_input("Enter Admin Password", type="password")
        if st.button("Login"):
            if password_input == st.secrets["admin_password"]:
                st.session_state.is_admin = True
                st.success("✅ Logged in as admin.")
                st.rerun()
            else:
                st.error("❌ Incorrect password.")
    else:
        st.success("Logged in as admin.")
        if st.button("Logout"):
            st.session_state.is_admin = False
            st.rerun()

# Layout: chatbot on left, admin menu on right (if logged in)
col1, col2 = st.columns([2, 1])
with col1:
    chat_agent()
with col2:
    if st.session_state.is_admin:
        show_menu_management()