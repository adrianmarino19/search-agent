import os
from dotenv import load_dotenv # this is simply to be able to load the environment, but you still need to us os!

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langchain_core.tools import tool # tool decorator which is how we pass tools to LLMs!

load_dotenv()

tools = [TavilySearch()]
llm = ChatOpenAI(model='gpt-4')
react_prompt = hub.pull('hwchase17/react') #pulling template from the langchain hub.

# We need this method in order to create an agent ;)
agent = create_react_agent(
    llm,
    tools,
    react_prompt)

executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chain = executor

###

def main():
    result = chain.invoke(input={
        'input': 'search for 3 job postings for an ai engineer using langchain in Madrid, Spain on linkedin and list their details'
    })

    print(result)

if __name__ == "__main__":
    main()


### What exactly is the AgentExecutor under the black box?
