import os
from dotenv import load_dotenv # this is simply to be able to load the environment, but you still need to us os!

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langchain_core.tools import tool # tool decorator which is how we pass tools to LLMs!

load_dotenv()


tool = [TavilySearch]

###

def main():
    print()


if __name__ == "__main__":
    main()
