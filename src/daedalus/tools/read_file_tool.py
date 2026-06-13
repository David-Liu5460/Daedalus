from pathlib import Path
from typing import Optional

from langchain.tools import ToolRuntime, tool

MAX_LINES = 2000


@tool("read_file", parse_docstring=True)
def read_file_tool(
    runtime: ToolRuntime,
    path: str,
    offset: Optional[int] = None,
    limit: Optional[int] = None,
) -> str:
    """Reads the contents of a file and returns it with line numbers.

    Args:
        path: The absolute path to the file to read. Relative paths are **not** allowed.
        offset: The 1-based line number to start reading from. Defaults to the first line.
        limit: The maximum number of lines to read. Defaults to reading up to 2000 lines.
    """
    _path = Path(path)
    if not _path.is_absolute():
        return f"Error: the path {path} is not an absolute path. Please provide an absolute path."
    if not _path.exists():
        return f"Error: the path {path} does not exist. Please provide a valid path."
    if not _path.is_file():
        return f"Error: the path {path} is not a file. Please provide a valid file path."

    try:
        with _path.open("r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except PermissionError:
        return f"Error: permission denied to access the path {path}."

    if not lines:
        return f"The file {path} is empty."

    start = (offset - 1) if offset and offset > 0 else 0
    if start >= len(lines):
        return f"Error: offset {offset} is beyond the end of the file ({len(lines)} lines)."

    count = limit if limit and limit > 0 else MAX_LINES
    end = min(start + count, len(lines))
    selected = lines[start:end]

    width = len(str(end))
    numbered = [
        f"{str(start + i + 1).rjust(width)}\t{line.rstrip(chr(10))}"
        for i, line in enumerate(selected)
    ]

    result = (
        f"Here's the content of {path} (lines {start + 1}-{end} of {len(lines)}):\n"
        "```\n" + "\n".join(numbered) + "\n```"
    )
    return result


if __name__ == "__main__":
    print(
        read_file_tool.func(
            runtime=None,
            path=str(Path(__file__).resolve()),
            limit=20,
        )
    )
