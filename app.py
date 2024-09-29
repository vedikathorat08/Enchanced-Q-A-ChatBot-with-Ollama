import streamlit as st
import os
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

engine = "mistral"  # or whatever engine you're using
temperature = 0.7
max_tokens = 150

##Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_Tracing_V2"]="true"
os.environ["LANGCHAIN_Project"]="Q&A ChatBot with OllAMA"

##Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer



##Title of the app
st.title("Enchanced Q&A ChatBot with Ollama")



##Drop down to select various Ollama models
llm=st.sidebar.selectbox("Select an Open AI Model",["llama3.2","mistral"])

##Adjust response parameter
temperature =st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max-Tokens",min_value=50,max_value=300,value=150)

##Main Interface for user Input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")



if user_input:
    print(engine)
    print(f"Engine value: {engine}")
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")