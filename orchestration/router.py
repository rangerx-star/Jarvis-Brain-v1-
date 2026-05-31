from orchestration.registry import AGENTS

def route_agent(agent_name, agent_task):
  """
  Route tasks to agent using their names
  """
  
  if agent_name in AGENTS and agent_task:
    try:
      agent_response = AGENTS[agent_name](agent_task)
      
      if agent_response:
        print("\nAgent response gathered...")
        return agent_response
      else:
        print("\nNothing inside agent response...")
      
      #clean_agent_res = normalize_agent_response(agent_response, agent_name, agent_task)
      #print(f"\n{agent_response}")
      
      """if clean_agent_res:
        return clean_agent_res
      else:
        print("\nNothing inside agent response.")"""
      
    except Exception as e:
      return {
        "success": False,
        "error": str(e),
        "agent_name": agent_name,
        "agent_task": agent_task,
        "message": "Agent execution failed due to internal error."
      }

"""def normalize_agent_response(raw_response, agent_name, agent_task):
  if isinstance(raw_response, dict):
    
    if "No message field inside model response" in str(raw_response):
      error_details = raw_response.get("error", str(raw_response))
      
      return {
        "success": False,
        "error": error_details,
        "agent_name": agent_name,
        "agent_task": agent_task,
        "message": "Tool execution failed. Please try again or use general knowledge."
      }
      
    if raw_response.get("tool_calls") or raw_response.get("final_answer"):
      message = (
        raw_response.get("final_answer")
        or raw_response.get("tool_calls")
        or "No usable response"
      )
      
      return {
        "success": True,
        "message": message
      }
      
  else:
    return {
        "success": False,
        "error": "Unknown response format",
        "agent": agent_name,
        "task": agent_task,
        "message": str(raw_response)[:500]
    }
    
"""