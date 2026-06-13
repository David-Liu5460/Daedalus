# Daedalus
 从0到1实现一个agent harness

# 架构设计 
![alt text](image-1.png)

如上图所示，从下往上看：
- 使用到的主要第三方库包括：
  - Agentic System 基于最近即将发布的 LangChain + LangGraph 1.0 正式版
  - 控制台界面则是基于 Textual 和 Rich 这两个控件库
- 模型层默认采用豆包 Seed 1.6，同时支持 Thinking 和无 Thinking 模式
- 工具层包括：
  - 文件系统工具集：
文件系统工具部分参考了 Claude Code 的实现
工具
说明
ls
列出指定目录下的子目录和文件，支持 Glob 模糊查询，可用于文件列举和文件名模糊查找
tree
列出指定目录下的所有子孙目录和文件，支持指定深度（最大深度为 3 层），该工具有助于 Coding Agent 了解项目的结构和技术栈
grep
和操作系统的 grep 命令几乎一样，用于通过字符串和 Glob 匹配进行代码文本的查找，在代码定位中非常实用
glob（deprecated）
一些 Coding Agent 还实现了 glob 工具，在本文的方案设计中被并入了 ls 工具。
  - 文本编辑器工具：
文本编辑器是一个单一工具，但支持了 4 个子命令，完全参考了 Anthropic 的 text_editor_20250728 实现，无论是豆包还是其他模型对此抽象都非常熟悉
命令
说明
view
检查文件内容或列出目录内容，它可以读取整个文件或特定行范围
create
用于创建具有指定内容的新文件
str_replace
用新字符串替换文件中的特定字符串。这用于进行精确编辑
insert
在文件的特定位置插入文本
undo（reprecated）
由于模型尚不能完全理解 undo 每次撤销的动作范围，因此 Anthropic 最终移除了该工具，在本文的方案中，也同样移除了该工具。
  - 命令行工具：用于执行 Bash 命令，同样参考了 Anthropic 的 bash 工具实现
  - To-do 列表工具：用于让 Agent 主动创建和不断更新 To-do 列表，这个工具本身不具备任何实际功能，是一个“Pseudo Tool”，仅仅是为了不断“启发”Agent 去进行 Planning 过程。
  - MCP 工具加载器：用于加载 config.yaml 中指定的 MCP 工具
- Prompt Template 用于管理、实例化系统提示词的模板
- Agent 层基于以上能力，构建了 Coding Agent
- 最后以 Console UI 的形式，组装 Coding Agent 的能力，与用户进行交互
为何 Coding Agent 如此青睐 Console UI 设计？
你可能不禁要问，为何几乎所有的 Coding Agent 都清一色的选择了命令行 CUI（Console UI） 、CLI（Command Line Interface）呢？
- 轻量与低开发成本：对比图形化界面（GUI），Console UI 不需要处理复杂的窗口管理、按钮渲染、事件监听等，简单布局一下，保持一定的“程序员审美”的同时，开发效率高很多。
- 跨平台兼容性：终端几乎是所有开发环境的“公共语言”。无论是 Linux、macOS，还是 Windows，都能跑命令行。
- 适合持续开发集成工作流：可以被轻松的集成到 CI/CD 流程。
- 可移植性与低资源占用：Console UI 占用内存和 CPU 极小，非常适合在远程服务器、容器或嵌入式设备上运行，还可以通过 SSH 命令远程控制。
- 渐进式增强：可以先用 Console UI 实现 MVP，然后再推出 IDE 插件、Web 界面、桌面 App 等。