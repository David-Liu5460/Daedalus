from langchain.agents import create_agent

from models.chat_model import init_chat_model
from tools.search_tool import search_tool


deep_search_agent=create_agent(
    model=init_chat_model(),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information."
)

