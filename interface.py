import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as palm

palm.configure(api_key = os.getenv("api_key"))
model_id="models/chat-bison-001"

if "messages" not in st.session_state:
    st.session_state.messages = []
    intro = "Hi! How are doing buddy? How can I help you?"
    
    st.session_state.messages.append({"ROLE" : "ASSISTANT", "CONTENT" : intro})
    
    
for message in st.session_state.messages:
    with st.chat_message(message.get('ROLE')):
        st.write(message.get("CONTENT"))

prompt = st.chat_input("Ask Anything")
    
if prompt:
    st.session_state.messages.append({"ROLE" : "USER", "CONTENT" : prompt})

    with st.chat_message("USER"):
        st.write(prompt)
    
    response = palm.chat(messages=prompt)  
    reply = response.last
    if reply != None:
        st.session_state.messages.append({"ROLE" : "ASSISTANT", "CONTENT" : reply})

    with st.chat_message("ASSISTANT"):
        if reply != None:
            st.write(reply)
        else:
            st.write("I couldn't understand")
