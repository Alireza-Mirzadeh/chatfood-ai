import streamlit as st
from agent import create_agent

def chat_agent():

    st.subheader("Chat with ChatFood AI")
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask about the menu or food...")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("assistant"):
            agent = create_agent()
            response = agent.invoke(user_input)
            response_text = response.get('output', str(response))
            st.markdown(response_text)
            st.session_state["messages"].append({"role": "assistant", "content": response_text})

