from integrations.ollama_llm import OllamaModel
from datetime import datetime

model = OllamaModel()

agent_task_logs = {}

with open("./prompts/workers_prompts/reflection_agent_instruction.txt", "r") as ins_file:
  reflection_agent_instruction = ins_file.read()
  
def extract_events(user, conversation_history):
  agent_task_logs = {
    "role": "user",
    "content": conversation_history,
    "metadata": {
      "user_current_input": user,
      "date_and_time": datetime.now().astimezone().isoformat()
    }
  }
  
  response = model.call_model(
    agent_task_logs,
    reflection_agent_instruction
  )
  
  if isinstance(response, dict):
    return response
 
  else:
    return f"\nReflection agent returned not dict: \n{response}\n"
  