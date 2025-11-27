from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

# Import node functions and shared state definition
from .state import AgentState
from .nodes.search import search_node
from .nodes.analyze import analyze_node
from .nodes.report import report_node

def build_graph():
    # Create the workflow using LangGraph
    workflow = StateGraph(AgentState)

    # Register nodes for each stage of the pipeline
    workflow.add_node("search", search_node)
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("report", report_node)

    # Define the execution flow: search → analyze → report → END
    workflow.set_entry_point("search")
    workflow.add_edge("search", "analyze")
    workflow.add_edge("analyze", "report")
    workflow.add_edge("report", END)

    # Compile the workflow into an executable graph
    return workflow.compile()

def main():
    # Build the graph
    app = build_graph()

    # Example query — reviewers can modify this
    initial_state = {
        "messages": [
            HumanMessage(content="Latest advancements in Retrieval-Augmented Generation (RAG)?")
        ]
    }

    # Run the workflow
    result = app.invoke(initial_state)

    # Print the final report from the last message
    print("\n===== FINAL REPORT =====\n")
    print(result["messages"][-1].content)

# Allow running this file directly
if __name__ == "__main__":
    main()
