#from integrations.gemini_llm import call_gemini_model
from integrations.ollama_llm import OllamaModel
#from integrations.open_router_models import OpenRouterModel
from state.runtime.runtime_state_instance import runtime_state
from state.personality.personality_state import AgentPersonalityState
from memory.episodic.episodic import load_episode
import json

model = OllamaModel()
agent_personality = AgentPersonalityState()

with open("./prompts/workers_prompts/conversation_agent_instruction.txt") as ins_file:
  conversation_agent_ins = ins_file.read()
  
def call_conversation_agent(relavent_context = None):
  #if data is not None:
    # Updating state with agent results
    #state.update_state(agent_result=data)
    
  conversation_agent_state = {
    "context": {
      "currently_running": runtime_state.get_state(),
      "relavent_memory": relavent_context
    },
    "personality": agent_personality.load_personality_state()
  }
  
  print(f"\nCONVERSATION STATE: \n{conversation_agent_state}\n")
    
  response = model.call_model(
    conversation_agent_state,
    conversation_agent_ins
  )
    
  if "response" in response:
    #print(f"\nConversation agent response: \n{response} | returned_type: {type(response)}\n")
    return response.get("response")
    #return response
  else:
    return f"\nNo response field inside conversation agent: \n{response}\n"
    
