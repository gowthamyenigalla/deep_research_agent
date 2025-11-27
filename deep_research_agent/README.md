# Deep Research Agent (LangGraph + OpenAI)

This repository implements a simple deep research agent using LangGraph, the official OpenAI Python client, and a DuckDuckGo-based search tool. The objective is to build a minimal, reproducible pipeline that accepts a user query, gathers relevant context from the web, summarizes the information, and generates a structured research report.

The project intentionally keeps the design focused and readable while meeting all the requirements specified in the assignment.

---

## Project Overview

The agent operates through three main stages:

1. Search – Uses DuckDuckGoSearchRun to gather relevant web information.
2. Analyze – Summarizes the retrieved content using GPT-4o-mini (via the OpenAI Python SDK).
3. Report – Produces a structured and readable research report based on the summary.

These steps are orchestrated using LangGraph in a linear workflow:

search → analyze → report → END

The agent maintains a minimal state dictionary containing a single field:

messages: List[BaseMessage]

This stores all user messages, tool responses, intermediate summaries, and the final report.

---

## Folder Structure

```

deep_research_agent/
src/
state.py
graph.py
nodes/
search.py
analyze.py
report.py
requirements.txt
.env.example
README.md

```

Each file has a clear responsibility to keep the project maintainable and easy to follow.

---

## Setup Instructions

### 1. Clone the Repository

```

git clone <your-repo-url>
cd deep_research_agent

```

### 2. Create a `.env` File

```

cp .env.example .env

```

Then add your OpenAI key:

```

OPENAI_API_KEY=your-openai-key

```

### 3. Install Dependencies

```

pip install -r requirements.txt

```

This installs LangGraph, LangChain core utilities, the OpenAI SDK, dotenv, and the DuckDuckGo search tool.

---

## Running the Agent

Once dependencies are installed and the `.env` file is configured, you can run the full research pipeline:

```

python src/graph.py

```

This triggers the entire workflow. After execution completes, the final report will be printed in the terminal.

---

## How the Agent Works

### LangGraph Workflow

The workflow is constructed using StateGraph. Nodes represent individual steps and the graph passes the shared state between them.

### State Definition

The state is defined in `state.py` and contains:

```

class AgentState(TypedDict):
messages: List[BaseMessage]

```

This keeps the design intentionally minimal and easy to inspect.

### Search Node

The search step (`search.py`) uses DuckDuckGoSearchRun. No API key is required, which reduces reviewer friction and simplifies setup.

### Analyze Node

The analysis step (`analyze.py`) summarizes the search results using the official OpenAI Python SDK. This avoids compatibility issues introduced by deprecated LangChain wrappers.

### Report Node

The report generation step (`report.py`) produces a structured report following a consistent layout. This makes the output easy to read and evaluate.

---

## Design Decisions and Ideas for Improvement

### Why DuckDuckGo?

It avoids requiring another API key, making the project easy for reviewers to run immediately. The output is sufficient for a research prototype.

### Why use the official OpenAI SDK instead of LangChain wrappers?

LangChain has introduced several breaking changes in its LLM wrappers. The official SDK is stable, well-documented, and avoids dependency issues.

### Why keep the state minimal?

A simple messages list keeps the workflow easy to audit and debug while satisfying the assignment requirements.

### Potential Improvements

- Add retry logic and error handling around external calls.
- Add caching to avoid repeated search queries.
- Make the number of searches or models configurable.
- Add citation extraction to improve reference accuracy.
- Split long search results into chunks for higher-quality summarization.
- Introduce multiple search passes for deeper research.

These improvements could extend the usefulness and robustness of the current architecture.

---

## Notes for Reviewers

- All `.py` files contain fully executable code.
- `.env.example` is included for reference; `.env` should be created locally.
- The project can be run with a single command after installation.
- The solution avoids deprecated APIs and follows current OpenAI + LangGraph best practices.

