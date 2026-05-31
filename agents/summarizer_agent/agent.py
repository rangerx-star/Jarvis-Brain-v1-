from integrations.ollama_llm import OllamaModel
#from state.short_term_memory import update_memory, get_memory
#from integrations.gemini_llm import call_gemini_model
import json

model = OllamaModel()

agent_task_logs = {}
  
def summarize(data: str, user_request: any):
  with open("prompts/workers_prompts/summarizer_agent_instruction.txt", "r") as ins_file:
    summarizer_ins = ins_file.read()
  
  # Setting summarizer data & user_input
  summarization_template = f"""
  summarize This:
  
  summarization needed data:
  {data}
  
  user: {user_request}
  """
  
  # Updating temporal agent_task_logs with summarization_template
  agent_task_logs = {
    "role": "user",
    "content": "Task for summarizer.",
    "metadata": {
      "data": summarization_template
    }
  }
  
  response = model.call_model(
    agent_task_logs,
    summarizer_ins
  )
    
  return response
  