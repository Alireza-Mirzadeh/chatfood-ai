import streamlit as st
from menu_editor import show_menu_management
from chat_agent import chat_agent

st.set_page_config(page_title="🍽 ChatFood AI", layout="centered")

tab1, tab2 = st.tabs(["🤖 Chat with Agent", "📋 Menu Management"])

with tab1:
    chat_agent()
with tab2:
    show_menu_management()