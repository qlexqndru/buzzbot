import streamlit as st
import time
from langchain_handler import LangchainHandler

st.set_page_config(page_title="Chat with BuzzBot")

# Inject custom CSS to center sidebar content vertically
st.markdown(
    """
    <style>
    /* Center the sidebar content vertically */
    [data-testid="stSidebar"] > div:first-child {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize handler and session state
if "handler" not in st.session_state:
    st.session_state.handler = LangchainHandler()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.sidebar:
    st.title("🤖 BuzzBot")
    use_web_search = st.toggle("Web Search")

# Handle user input
if prompt := st.chat_input("Message"):
    # Add user message to chat
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and stream response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()
        full_response = ""

        # Stream the response
        for chunk in st.session_state.handler.process_input(
            prompt, user_id="1", use_web_search=use_web_search
        ):
            if chunk.content:
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")

        # Final response without cursor
        response_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
