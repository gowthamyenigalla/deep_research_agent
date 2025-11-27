from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import AIMessage
from .state import AgentState  # relative import if using package form, adjust if needed

# Initialize the DuckDuckGo search tool (no API key required)
ddg_search = DuckDuckGoSearchRun()

def search_node(state: AgentState):
    # Take the most recent user query from the message list
    query = state["messages"][-1].content

    # Perform a live DuckDuckGo search to fetch web results
    results = ddg_search.run(query)

    # Wrap the search output in an AIMessage tagged as a tool result
    tool_message = AIMessage(
        content=str(results),
        additional_kwargs={"tool": "duckduckgo"}
    )

    # Append the tool output to the existing message sequence
    return {"messages": state["messages"] + [tool_message]}
