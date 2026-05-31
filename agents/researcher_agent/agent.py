from integrations.gemini_llm import call_gemini_model
#from state.short_term_memory import update_memory, get_memory
from agents.researcher_agent.tool_selector import select_tool
#from integrations.ollama_llm import OllamaModel

#model = OllamaModel()

# Getting researcher system instruction
with open("prompts/workers_prompts/researcher_instruction(tools).txt", "r") as ins_file:
  researcher_ins = ins_file.read()
  
agent_task_logs = {}


def call_researcher(task):
  """
  Calls gemini llm as researcher using 
  researcher system instructions for making
  precise answers to supervisor.
  """
  
  try:
    
    if not task:
      return {
        "success": False,
        "error": "No task provided."
      }
    
    """memory.create_memory_entry(
      content=f"Researcher Agent task: {task}",
      role="user"
    )"""
    
    agent_task_logs = {
      "role": "user",
      "parts": [{"text": f"TASK FOR RESEARCHER: {task}"}]
    }
    
    # calling gemini llm with memory
    response = call_gemini_model(
       agent_task_logs,
       researcher_ins
    )
      
    #print(f"\nRAW RESEARCHER RESPONSE: \n{response}")
    
    if isinstance(response, str):
      return {
        "success": False,
        "error": "Model returned str."
      }
      
    if not isinstance(response, dict):
      return {
        "success": False,
        "error": "Model returned invaild res type."
      }
    
    if response.get("tool_calls"):
      tool_calls = response["tool_calls"]
      print("\nTOOL NEEDED...")
      
      for call in tool_calls:
        tool_name = call["tool"]
        tool_args = call.get("args", {})
        print(f"\nTOOL: {tool_name} | PARAMS: {tool_args}")
        tool_result = select_tool(tool_name, tool_args)
        #print("\nTOOL RESULT GATHERED\n")
        
      if tool_result is None:
        return {
          "success": False,
          "error": "Tool result is None."
        }
          
      else:
        return {
          "success": True,
          "tool_results": tool_result
        }
        
    else:
      if response.get("final_answer"):
        #print("\nCASUAL RESPONSE...")
        text = response["final_answer"]
        return {
          "success": True,
          "text": text
        }
        
  except Exception as e:
    return {
      "success": False,
      "error": str(e)
    }