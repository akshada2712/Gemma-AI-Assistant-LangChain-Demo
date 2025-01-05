# # to run this app 
# # cd Ollama_basics
# # streamlit run app.py

# import os 
# from dotenv import load_dotenv 
# from langchain_ollama import OllamaLLM
# import streamlit as st 
# import json

# from langchain_community.llms import Ollama
# from langchain_core.prompts import ChatPromptTemplate 
# from langchain_core.output_parsers import StrOutputParser


# load_dotenv()

# ## langsmith tracking 

# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
# os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")
 

# ## designing prompt template 


# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant. Please respond to the user's question **clearly in plain text**."),
#         ("user", "Question: {question}")
#     ]
# )


# ## streamlit framework 

# st.title("Langchain Demo with Gemma2b ")

# input_txt = st.text_input("What is running in your mind? ")


# ## Ollama LLama2 model: 

# llm = OllamaLLM(model="gemma:2b", format='json')

# chain = prompt | llm

# if input_txt:
#     try:
#         # Invoke the chain and get the JSON response
#         response = chain.invoke({"question": input_txt})
#         response = json.loads(response)
#         st.write(response)
#     except Exception as e:
#         # Catch and display any errors
#         st.error(f"An error occurred: {e}")


import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


