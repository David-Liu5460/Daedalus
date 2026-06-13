# Daedalus
Implement an agent harness from scratch

# Architecture Design
![alt text](image-1.png)

As shown in the figure above, viewed from bottom to top:
- Main third-party libraries used include:
  - Agentic System is built on the upcoming official release of LangChain + LangGraph 1.0
  - The console interface is based on the two widget libraries Textual and Rich
- The model layer uses Doubao Seed 1.6 by default, and supports both Thinking and non-Thinking modes
- Tool layer includes:
  - File system tool set:
The file system tool implementation partially references Claude Code's implementation
| Tool | Description |
|------|-------------|
| ls | List subdirectories and files in the specified directory, supports Glob fuzzy query, can be used for file listing and fuzzy file name search |
| tree | List all descendant directories and files in the specified directory, supports specifying depth (maximum depth is 3 levels). This tool helps Coding Agent understand the project structure and tech stack |
| grep | Almost identical to the grep command in operating systems, used for code text search through string and Glob matching, very practical for code location |
| glob (deprecated) | Some Coding Agents also implement the glob tool, which has been incorporated into the ls tool in this solution design. |
  - Text editor tool:
The text editor is a single tool that supports 4 subcommands, fully referencing Anthropic's text_editor_20250728 implementation. Both Doubao and other models are very familiar with this abstraction.
| Command | Description |
|---------|-------------|
| view | Inspect file content or list directory content, it can read the entire file or a specific range of lines |
| create | Used to create new files with specified content |
| str_replace | Replace a specific string in a file with a new string. This is used for precise editing |
| insert | Insert text at a specific position in the file |
| undo (deprecated) | Since models cannot yet fully understand the scope of each undo action, Anthropic eventually removed this tool, and it is also removed in this solution. |
  - Command line tool: Used to execute Bash commands, also references Anthropic's bash tool implementation
  - To-do list tool: Used for the Agent to actively create and continuously update the To-do list. This tool itself does not have any practical functions, it is a "Pseudo Tool" just to constantly "inspire" the Agent to carry out the Planning process.
  - MCP tool loader: Used to load MCP tools specified in config.yaml
- Prompt Template: Used to manage and instantiate system prompt templates
- Agent layer: Builds Coding Agent based on the above capabilities
- Finally, in the form of Console UI, assemble the capabilities of Coding Agent to interact with users

## Why do Coding Agents favor Console UI design so much?
You may ask, why do almost all Coding Agents unanimously choose command-line CUI (Console UI) and CLI (Command Line Interface)?
- **Lightweight and low development cost**: Compared with Graphical User Interface (GUI), Console UI does not need to handle complex window management, button rendering, event listening, etc. With simple layout, while maintaining a certain "programmer aesthetic", the development efficiency is much higher.
- **Cross-platform compatibility**: Terminal is almost the "common language" of all development environments. Whether it is Linux, macOS, or Windows, command line can run.
- **Suitable for continuous development and integration workflow**: Can be easily integrated into CI/CD processes.
- **Portability and low resource consumption**: Console UI has very small memory and CPU footprint, very suitable for running on remote servers, containers or embedded devices, and can also be remotely controlled via SSH commands.
- **Progressive enhancement**: You can first implement MVP with Console UI, and then launch IDE plugins, web interfaces, desktop apps, etc.
