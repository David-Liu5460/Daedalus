from langchain.agents import create_agent

from daedalus.models.chat_model import init_chat_model
from daedalus.project import project
from daedalus.tools.ls_tool import ls_tool

coding_agent = create_agent(
    model=init_chat_model(),
    tools=[ls_tool],
    system_prompt=f"""You are a helpful assistant that can help with coding tasks.
    # Project Information
    PROJECT_ROOT_DIR={project.root_dir}
    """,
)