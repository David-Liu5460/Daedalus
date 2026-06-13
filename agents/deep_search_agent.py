from langchain.agents import create_agent
from coder.models.chat_model import doubao_seed
from coder.tools.search_tool import search_tool


deep_search_agent=create_agent(
    model=doubao_seed(),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information."
)

