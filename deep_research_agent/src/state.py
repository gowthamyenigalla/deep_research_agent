from typing import List, TypedDict
from langchain_core.messages import BaseMessage

# LangGraph state structure used across the graph.
# The assignment requires a `messages` field in state where:
# - user queries (role=user) are stored
# - tool outputs (role=tool) are stored
# - assistant messages (role=assistant) are stored (including final report)
# Keeping the state minimal makes the graph easy to follow and validate.
class AgentState(TypedDict):
    messages: List[BaseMessage]
