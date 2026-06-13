import os

from dotenv import load_dotenv
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool("search", parse_docstring=True)
def search_tool(query: str):
    """Search the web for the given query.

    Args:

    query: The SEO-optimized query to search for.
    """

    results = tavily_client.search(query, num_results=110)
    return results

if __name__ == "__main__":
    print(search_tool.invoke("What is the capital of France?"))
