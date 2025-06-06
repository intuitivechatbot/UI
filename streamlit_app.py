import streamlit as st
import requests

st.set_page_config(page_title="Intuitive Soul Chatbot", page_icon="")

st.title("Intuitive Soul Chatbot")
st.markdown("Ask about anything that you want to talk about")

# Initialize session state for chat and role
if "messages" not in st.session_state:
    st.session_state.messages = []
if "role" not in st.session_state:
    st.session_state.role = "You are the CEO of Intuitive Soul"


# Chat interface
user_input = st.chat_input("Ask your question")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prepare request
    payload = {
        "input": user_input,
        "role": st.session_state.role
    }

    try:
        response = requests.post("https://intuitive-soul-f229c1e78695.herokuapp.com/ask", json=payload)
        if response.status_code == 200:
            answer = response.json()["answer"]
        else:
            answer = f"⚠️ Error {response.status_code}: {response.text}"
    except Exception as e:
        answer = f"❌ Request failed: {str(e)}"

    # Add assistant message to chat
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])