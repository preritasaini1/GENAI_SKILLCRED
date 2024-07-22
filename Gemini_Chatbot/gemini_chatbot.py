import streamlit as st    #UI Design
import os
from dotenv import load_dotenv   # Package to get the environment variables loaded into the application 
load_dotenv()     # loading of all the env. variable
import google.generativeai as genai

#genai configuration of API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#intializing the model 
model = genai.GenerativeModel('gemini-pro')

#define a function to generate the response from LLM
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# setting up Streamlit app 
st.set_page_config(
    page_title='gemini-pro_q&a',
    layout="wide",
    page_icon=":computer:",
    initial_sidebar_state="expanded"
)

#setting up header
st.header("MY_GEMINI-PRO_Q&A")
#st.title("MY_GEMINI-PRO_Q&A")

#input
question = st.text_input("Please Ask Your Question Here!")

#submit
if st.button("Submit Here!"):
    response=get_gemini_response(question)
    st.write("**YOU**",question)
    st.write("**GEMINI**",response)