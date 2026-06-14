import os
import streamlit as st
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient
load_dotenv()

# model instantiation
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  
grok_model=ChatGroq(model="qwen/qwen3-32b")


st.title("Search Agent with Groq Model")
@tool
def search(query:str)->str:
    """Web search the query and return the result"""
    TAVILY=os.getenv('TAVILY_API_KEY')
    Client=TavilyClient(TAVILY)
    response=Client.search(
        query=query,
        include_answer="basic",
        search_depth="advanced"
    )    
    return response.get("answer","no answer found")

agent=create_agent(
    model=grok_model,
    tools=[search],
    system_prompt="you are a helpful ai assistant which help in searching the web" 
)

query = st.text_input("enter your query to search from web or to find weather information : ")
if st.button("Search"):
    with st.spinner("Fetching Search Result ..."):
        try:
            response = agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            })
            st.write(response["messages"][-1].content)
        except Exception as e:
            st.error(f"Error: {e}")



