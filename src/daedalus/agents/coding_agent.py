from langchain.agents import create_agent
from langchain.agents.middleware.todo import TodoListMiddleware
from langchain.agents.middleware import SummarizationMiddleware

from daedalus.models.chat_model import init_chat_model
from daedalus.project import project
from daedalus.tools.edit import text_editor_tool
from daedalus.tools.ls_tool import ls_tool
# from daedalus.tools.read_file_tool import read_file_tool
from daedalus.tools.tree_tool import tree_tool

from daedalus.prompts import apply_prompt_template

coding_agent = create_agent(
    model=init_chat_model(),
    tools=[ls_tool, tree_tool, text_editor_tool],
    # system_prompt=f"""You are a helpful assistant that can help with coding tasks.
    # # Project Information
    # PROJECT_ROOT_DIR={project.root_dir}
    # """,
    system_prompt=apply_prompt_template("coding_agent", PROJECT_ROOT=project.root_dir),
    middleware=[
        TodoListMiddleware(),
        SummarizationMiddleware(
            model=init_chat_model(),
            trigger=("tokens", 4000),
            keep=("messages", 20),
        ),
    ],
)