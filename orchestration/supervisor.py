#from integrations.gemini_llm import call_gemini_model
from integrations.ollama_llm import OllamaModel
#from integrations.open_router_models import OpenRouterModel
import json

model = OllamaModel()

# Getting supervisor instructions
with open("prompts/supervisor_instruction.txt", "r") as ins_file:
  supervisor_ins = ins_file.read()
  
# Supervisor call function
def call_supervisor(state):
  """
  calls gemini llm using supervisor role
  and pass current conversation history
  to get a orchestration decision.
  """
  
  decision = model.call_model(
    state,
    supervisor_ins
  )
    
  """if decision:
     memory.create_memory_entry(
      content=decision,
      role="model",
      metadata={
        "type": "supervisor decision"
      }
     )"""
     
  return decision