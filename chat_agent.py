import streamlit as st
from graph_agent import chat_with_memory

# --- Page config ---
st.set_page_config(
    page_title="ChatFood AI",
    page_icon="🍽️",
    layout="wide"
)

def chat_agent():
    # Sidebar
    with st.sidebar:
        st.markdown("### 🍽️ ChatFood AI")
        st.markdown("Ask about menu items, prices, availability, or ingredients.")
        st.divider()
        st.caption("💡 Tip: You can ask things like *'What pizzas do you have?'* or *'Show vegan options'*.")

    st.title("💬 Chat with ChatFood AI")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    chat_container = st.container()
    with chat_container:
    # Display previous messages
        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    
    # Always scroll to the bottom automatically
    chat_container.scroll_to_bottom = True

    # User input
    user_input = st.chat_input("Ask about the menu or food...")
    if user_input:
        # Save and display user message
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking... 🍳"):
                response = chat_with_memory(user_input)
                st.markdown(response)

        # Save assistant message
        st.session_state["messages"].append({"role": "assistant", "content": response})

        st.rerun()



if __name__ == "__main__":
    chat_agent()


