import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as palm

palm.configure(api_key = "AIzaSyAC4PqD3EnrBUWpDZoMJzi37v04zSQZM6Y")
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
    st.session_state.messages.append({"ROLE" : "ASSISTANT", "CONTENT" : reply})

    with st.chat_message("ASSISTANT"):
        st.write(reply)
