from orchestration.supervisor import call_supervisor
from orchestration.router import route_agent
from agents.conversation_agent.agent import call_conversation_agent
from state.runtime.runtime_state_instance import runtime_state
from state.conversation.conversation_window_instance import conversation_window
from memory.episodic.episodic import create_episode

# Coloured logs
from rich.console import Console

import json 

console = Console()

# ------AGENT LOOP--------------------------
def run_agent_loop(user_request):
  """
  Starts the main agent loop.
  """
  
  workflow_complete = False
  step = 0
  MAX_STEPS = 5
  
  agent_results = {
    "result": {}
  }
  
  if user_request:
    """memory.create_memory_entry(
      content=user_request,
      role="user",
      
    )"""
    
    # Load previous_conversations
    runtime_state.refresh_memory_context()
    
    # Updating state with user input
    runtime_state.update_state(user=user_request)
    
    while not workflow_complete and step < MAX_STEPS:
      step += 1
      
      # LOG #1 [steps & state updates]
      #console.print(f"[bold cyan]\nSTEP: {step} | MAX: {MAX_STEPS}[/bold cyan]")
      print(f"\nCURRENT MEMORY: \n{runtime_state.get_state()}\n")
      
      # Supervisor Decision
      decision = call_supervisor(runtime_state.get_state())
      
      # LOG #2 [returned suoervisor decision]
      print(f"\nSUPERVISOR DECISION: \n{decision} | returned_type: {type(decision)}\n")
      
      if not isinstance(decision, dict):
        return f"supervisor returned invaild response: {decision}"
      
      if decision.get("res_type") == "agent_call":
        agent_calls = decision["agent_calls"]
        
        for call in agent_calls:
          agent_name = call["agent"]
          agent_task = call.get("task", {})
          
          # LOG #3 [called agent name]
          #print(f"\nCALLING -> {agent_name}")
          agent_response = route_agent(agent_name, agent_task)
          
          # LOG #4 [agent response]
          #print(f"\nAGENT RESPONSE: \n{agent_response}\n")
          
        if agent_response.get("success"):
            
          if agent_response.get("tool_results"):
            tool_results = agent_response.get("tool_results", {})
            
          if tool_results is None:
            agent_results["result"] = agent_response.get("text")
          
          else:
            agent_results["result"] = (
            tool_results.get("summarized_text") 
            or None
          )
            
          # Updating system state with agent results
          runtime_state.update_state(agent_result=agent_results["result"])
          
          """memory.create_memory_entry(
            role="tool",
            content="AGENT_RESULT",
            metadata={
              "agent": agent_name,
              "task": agent_task,
              "status": "completed",
              "agent_result": agent_results["result"]
            }
          )"""
          
          # LOG #5 [agent result state update]
          #print("Memory update (with agent res)")
          #console.print("\n[red]Skiping next supervisor step...[/red]\n")
          workflow_complete = True # Redirecting to conversation_agent
          
        else:
          # LOG #6
          print("\nSkipping failed agent result memory update...\n")
          
        #print(f"\nMEMORY AFTER AGENT ROUTE: \n{get_memory()}\n")
      
      elif decision.get("res_type") == "complete":
        workflow_complete = True
        
      else:
        return f"\nUnknown supervisor state {decision}"
        
  # creating user entry in memory
  
  final_response = call_conversation_agent()
  
  runtime_state.update_conversation_memory(
    user_message=user_request,
    model_message=final_response
  )
  
  if workflow_complete:
    chat_window = conversation_window.build_model_context(model_name="ollama")
    
    # Trying to create episode
    status = create_episode(user_request, chat_window)
    print("\n"+status)
    
    return final_response
  
  return "\nWorkflow stopped: maximum reasoning steps reached.\n"