


import streamlit as st
import requests as rq
import time

st.set_page_config(page_title="GAJALA CHATGPT", page_icon="🤖")
st.title("💬 GAJALA CHATGPT")

# Initialize conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Options")
    if st.button("Clear Chat"):
        st.session_state.conversation = []
    st.markdown("Made by **GAJALA PARWEEN**")

# Chat Input
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.conversation.append({"role": "user", "data": prompt})

    with st.spinner("AI is thinking... 🤔"):
        response = rq.post(
            url="https://gajala.app.n8n.cloud/webhook/b17afb30-f7c1-419d-aa62-f50c75a77b97",
            json={"prompt": prompt}
        )

        if response.status_code == 200:
            ai_text = response.json()["output"]

            # Typing animation effect
            temp = ""
            message_placeholder = st.empty()
            for char in ai_text:
                temp += char
                message_placeholder.markdown(temp)
                time.sleep(0.01)

            st.session_state.conversation.append({"role": "ai", "data": ai_text})

# Display chat history
for chat in st.session_state.conversation:
    with st.chat_message(chat["role"]):
        st.write(chat["data"])
