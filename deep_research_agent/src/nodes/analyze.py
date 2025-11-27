import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_core.messages import HumanMessage, AIMessage
from ..state import AgentState

# Load your API key from local .env
load_dotenv("deep_research_agent/.env")

# Initialize the OpenAI client (official SDK)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_node(state: AgentState):
    # Pull the last tool output (search results)
    search_output = state["messages"][-1].content

    # Prepare a summarization prompt for the LLM
    prompt = f"""
    Summarize the following web search results into clear, concise key insights:

    {search_output}
    """

    # Invoke GPT-4o-mini to generate a clean summary
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    # Extract text using the correct v1 SDK access pattern
    summary_text = completion.choices[0].message.content

    # Wrap and return the summary as the next assistant message
    summary_msg = AIMessage(content=summary_text)
    return {"messages": state["messages"] + [summary_msg]}
