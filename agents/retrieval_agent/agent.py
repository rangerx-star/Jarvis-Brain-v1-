from integrations.gemini_llm import call_gemini_model
from memory.episodic.episodic import load_episode

with open("prompts/workers_prompts/retrieval_agent_instruction.txt") as ins_file:
  retrieval_agent_instruction = ins_file.read()
  
def retrieve_relavent_context(current_user_input, memory: any = None):
  if memory is not None:
    temporal_agent_context = f"""
    CURRENT USER INPUT: {current_user_input}
    
    CONTEXT TO LOOK FOR RELAVENT INFORMATION:
    {memory}
    """
    
    temporal_agent_state = {
      "role": "user",
      "parts": [{"text": temporal_agent_context}]
    }
  
    response = call_gemini_model(
      temporal_agent_state,
      retrieval_agent_instruction
    )
    
    return response