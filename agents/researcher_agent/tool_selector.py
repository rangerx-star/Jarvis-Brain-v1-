from agents.researcher_agent.tool_config import AVAILABLE_TOOLS

def select_tool(tool_name: str, tool_args: str) -> str:
  if tool_name in AVAILABLE_TOOLS:
    tool = AVAILABLE_TOOLS[tool_name]
    return tool(tool_args)
    
  else:
    return "No tool found."