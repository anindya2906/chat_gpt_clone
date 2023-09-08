import time
import streamlit as st
from backend import get_ai_response

ROLES = {"USER": {"ROLE": "User", "AVATAR": "🧑‍💻"}, "AI": {"ROLE": "Assistant", "AVATAR": "🤖"}}

def show_chat_message(message):
    with st.chat_message(name=message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])

def show_chat_message_with_streaming(message):
    with st.chat_message(name=message["role"], avatar=message["avatar"]):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in message['content']:
            full_response += chunk
            time.sleep(0.01)
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    show_chat_message(message=message)

if prompt := st.chat_input():
    user_message = {"role": ROLES['USER']['ROLE'], "avatar": ROLES['USER']['AVATAR'], "content": prompt}
    st.session_state.messages.append(user_message)
    show_chat_message(user_message)

    ai_response = get_ai_response(user_message['content'])
    ai_message = {"role": ROLES['AI']['ROLE'], "avatar": ROLES['AI']['AVATAR'], "content": ai_response}
    st.session_state.messages.append(ai_message)
    show_chat_message_with_streaming(message=ai_message)
