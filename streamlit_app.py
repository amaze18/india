from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
from qa import answer_question
#from hugchat import hugchat
#from hugchat.login import Login


import os
SECRET_TOKEN = os.environ["SECRET_TOKEN"] #{{ secrets.SECRET_KEY }} 
#st.write("secret_token::",SECRET_TOKEN) 
openai.api_key = SECRET_TOKEN



# App title
st.set_page_config(page_title="🤗💬 ISB Dlabs Chat Bot")
st.write("ISB Dlabs Chat Bot")
# Hugging Face Credentials
with st.sidebar:
    st.title('🤗💬 ISB Dlabs Chat Bot')
    #if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
    st.success('HuggingFace Login credentials already provided!', icon='✅')
    hf_email = 'anupam_purwar2019@pgp.isb.edu'
    hf_pass = 'PASS'
   
    st.markdown('📖 This app is hosted by i-venture @ ISB [website](https://i-venture.org/)!')
    
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    #sign = Login(email, passwd)
    #cookies = sign.login()
    # Create ChatBot                        
    #chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return answer_question(prompt_input)

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
