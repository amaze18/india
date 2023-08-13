from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openai
from qa_anupam import chat_gpt
#from hugchat import hugchat
#from hugchat.login import Login
import os
from PIL import Image
import os
SECRET_TOKEN = os.environ["SECRET_TOKEN"] 
openai.api_key = SECRET_TOKEN

# App title
st.set_page_config(page_title="🤗💬 Anupam @ Everywhere Chat Bot")
st.header('🤗💬Anupam @ Everywhere Chat Bot')
st.subsubheader('🤗💬Ask anything about Anupam Purwar')

#
# Hugging Face Credentials
with st.sidebar:
    st.title('🤗💬Anupam @ Everywhere Chat Bot')
    st.success('Developed by [Anupam](https://www.linkedin.com/in/anupamisb/)!!', icon='✅')
    hf_email = 'anupam_purwar2019@pgp.isb.edu'
    hf_pass = 'PASS'
    st.markdown('📖 This app is hosted by [Anupam](https://www.linkedin.com/in/anupamisb/)!')
    st.write("Anupam @ Everywhere Chat Bot")
    image = Image.open('anupam_pic.jpg')
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

    
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Ask anything about Anupam ..."}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
     question0=prompt_input
     question=prompt_input
     ans = chat_gpt(prompt_input)
     # st.write(ans)
     if (ans=='I don\'t know.' or ans=='I don\'t know' or ans== 'I could not find an answer.' or 'I could not find' in ans  or ' I couldn\'t find'  in ans  ):
           question=question0+ " Anupam Purwar"
           ans=answer_question(question)
           if (ans=='I don\'t know.'  or ans=='I don\'t know' or ans== 'I could not find an answer.' or 'I could not find' in ans or ' I couldn\'t find'  in ans  ):
             question=question0+ " Anupam"
             ans=answer_question(question)
             if (ans=='I don\'t know.'  or ans=='I don\'t know'  or ans== 'I could not find an answer.' or 'I could not find' in ans or ' I couldn\'t find'  in ans  ):
               question=question0+ " Anupam Purwar ISB"
               ans=answer_question(question)
     return ans

# User-provided prompt
page_bg_img = '''
<style>
body {
background-image: url("https://csrbox.org/media/Hero-Image.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

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
