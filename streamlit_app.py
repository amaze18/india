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

from PIL import Image


import os
SECRET_TOKEN = os.environ["SECRET_TOKEN"] 
openai.api_key = SECRET_TOKEN



# App title
st.set_page_config(page_title="🤗💬 I-Venture @ ISB AI-Chat Bot")
st.write("I-Venture @ ISB Chat Bot")
image = Image.open('isbdlabs.jpg')
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
#
# Hugging Face Credentials
with st.sidebar:
    st.title('🤗💬I-Venture @ ISB Chat Bot')
    st.success('Access to this Gen-AI Powered Chatbot is provided by Anupam [website](https://github.com/amaze18)!!', icon='✅')
    hf_email = 'anupam_purwar2019@pgp.isb.edu'
    hf_pass = 'PASS'
    st.markdown('📖 This app is hosted by I-Venture @ ISB [website](https://i-venture.org/)!')
    
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Ask anything about I-Venture @ ISB ..."}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
     question0=prompt_input
     question=prompt_input
     ans = answer_question(prompt_input)
     # st.write(ans)
     if (ans=='I don\'t know.' or ans=='I don\'t know' or ans== 'I could not find an answer.' ):
           question=question0+ " ISB DLabs"
           ans=answer_question(question)
           if (ans=='I don\'t know.'  or ans=='I don\'t know' or ans== 'I could not find an answer.'):
             question=question0+ " ISB"
             ans=answer_question(question)
             if (ans=='I don\'t know.'  or ans=='I don\'t know'  or ans== 'I could not find an answer.' ):
               question=question0+ " I-Venture @ ISB"
               ans=answer_question(question)
     return ans

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt,hf_email,hf_pass) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
