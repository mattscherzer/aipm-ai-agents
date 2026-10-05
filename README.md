# Building AI Agents in Python

A hands-on introduction to building AI agents in Python. The notebooks start by building an agent from scratch with the raw Groq API, then move up to LangChain's high-level `create_agent(...)` runtime, down to explicit LangGraph control flow, and on to workflow patterns and two ways to connect external tools. All examples run against a Groq-hosted model.

## Learning Objectives

By the end of this repository, you should be able to:

- Build a minimal agent loop from scratch with the raw Groq API, and explain why language models are stateless.
- Test an agent by asserting on its answers and tool-call order, and grade open-ended answers with a second model acting as a judge.
- Build tool-using agents with LangChain's high-level `create_agent(...)` runtime.
- Inspect agent message traces (`HumanMessage`, `AIMessage`, `ToolMessage`) and add short-term memory with checkpointers.
- Rebuild the same agent loop explicitly with the LangGraph Graph API using state, reducers, routing, and checkpoints.
- Apply workflow patterns: structured (typed) output, step-by-step streaming, and interrupt-driven human review.
- Integrate external capabilities through MCP servers and through plain `@tool` HTTP wrappers, and compare the two approaches.

## Learning Path

Notebooks 1 to 4 are the **core path**: work through them in order. They cover the agent loop three ways (by hand, then with LangChain, then with LangGraph) plus the SQL exercise. Notebooks 3 and 4 deliberately revisit the same loop from notebook 1, so skim the loop itself and focus on what each framework adds.

Notebooks 5 to 7 are **optional extensions**. They build on the core path and can be taken later, in any order. Cover them if you have time once the core notebooks are done.

### Core notebooks

| File / Folder                                                       | Description                                                                                                                                                                    |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [**1 - Agents from Scratch**](1_agents_from_scratch.ipynb)     | Build the agent loop by hand with the raw Groq API: stateless calls, manual memory, and tool calling.                                                                          |
| [**2 - Exercise: SQL Agent**](2_exercise_sql_agent.ipynb)      | Exercise: build a SQL agent over NYC taxi data in DuckDB, then test it (assertions, tool-call order, an LLM judge, cost tracking). Downloads about 64 MB of data on first run. |
| [**3 - LangChain Agents**](3_langchain_agents.ipynb)           | High-level LangChain runtime:`create_agent(...)`, `@tool`, message traces, and checkpoint-backed memory.                                                                   |
| [**4 - LangGraph Graph API**](4_langgraph_graph_api.ipynb)     | The same agent loop rebuilt with the LangGraph Graph API: explicit state, reducers, routing, and checkpoints.                                                                  |

### Optional extensions

> [!NOTE]
> These are not part of the expected core path. Notebooks 5 to 7 build on the core notebooks and can be taken later, in any order.

| File / Folder | Description |
| --- | --- |
| [**5 - Workflow Patterns**](5_workflow_patterns.ipynb)         | Three ways to control an agent: return typed structured output, stream its steps as they happen, and pause for a human to approve an action before it continues. |
| [**6 - MCP Integration**](6_mcp_integration.ipynb)             | Connect an agent to a local MCP (Model Context Protocol) server over streamable HTTP, and use the tools, resources, and prompts it exposes. |
| [**7 - External Tool Calling**](7_external_tool_calling.ipynb) | Wrap external HTTP APIs as `@tool` functions with their own error handling, combine them with a Python REPL and a Wikipedia search, and contrast this approach with MCP. |

### Additional Folders and Files

| File / Folder                                            | Description                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [**Solutions**](solutions/)                         | Worked solution for the notebook 2 exercise.                                   |
| [**MCP Support Server**](support/mcp_ops_server.py) | Small FastMCP server used by notebook 6; the notebook starts it automatically. |
| [**.env.example**](.env.example)                    | Template for the`GROQ_API_KEY` environment variable.                         |
| [**pyproject.toml**](pyproject.toml)                | Project configuration and dependencies.                                        |
| [**uv.lock**](uv.lock)                              | Pinned dependency lock file.                                                   |

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a **placeholder**. Replace it, including the `< >` brackets, with your own value. For example, `cd <repo-name>` becomes `cd ds-ai-agent`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only **one person** should complete this step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings → Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like `git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in `.venv/`.

```bash
cd <repo-name>
uv sync
```

---

### 5. Add your Groq API Key

The notebooks read a Groq API key from a local `.env` file. Copy the template, then fill in your key:

```bash
cp .env.example .env
```

Edit `.env` and set the value:

```text
GROQ_API_KEY=<your-groq-api-key>
```

You can create a free key from the [Groq Console](https://console.groq.com/playground).

> [!CAUTION]
> `.env` holds a secret and must never be committed. Only `.env.example`, with placeholder values, belongs in the repository.

---

### 6. Open the Notebooks

> [!NOTE]
> Open VS Code from the project root so it automatically detects the environment created by `uv sync`.

Launch VS Code in the project root folder:

```bash
code .
```

Then open a notebook and select the Python environment created by `uv sync` as the kernel.

> [!NOTE]
> Notebook 6 starts the local MCP server for you as a background process, so there is no separate server to run.

## References & Further Reading

- [**LangChain Agents**](https://docs.langchain.com/oss/python/langchain/agents): How the high-level `create_agent(...)` runtime works.
- [**LangChain Structured Output**](https://docs.langchain.com/oss/python/langchain/structured-output): Returning typed, validated data from an agent.
- [**LangGraph Overview**](https://docs.langchain.com/oss/python/langgraph/overview): The orchestration framework agents are built on.
- [**LangGraph Quickstart**](https://docs.langchain.com/oss/python/langgraph/quickstart): Building an agent with the Graph API and the Functional API.
- [**Thinking in LangGraph**](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph): Decomposing a workflow into state, nodes, and edges.
- [**LangGraph Interrupts**](https://docs.langchain.com/oss/python/langgraph/interrupts): Pausing a graph for human-in-the-loop review.
- [**LangChain MCP**](https://docs.langchain.com/oss/python/langchain/mcp): Connecting agents to Model Context Protocol servers.
- [**MCP Python SDK**](https://py.sdk.modelcontextprotocol.io/): Building MCP servers and clients in Python.
- [**Groq Console**](https://console.groq.com/playground): Create a free API key and try the model used here.
