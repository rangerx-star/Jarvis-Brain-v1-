MEMORY = []
MESSAGES = []

def update_memory(content: dict, ollama: bool = False):
  """
  Updates/saves the model/user response
  into a sequeense of conversation list.
  """
  
  if ollama:
      MESSAGES.append(content)
      
  else:
    MEMORY.append(content)
    
def get_memory(ollama: bool = False):
  """
  return last 5 conversation chat history
  """
  if ollama:
    return MESSAGES[-5:]
  else:
    return MEMORY[-5:]
  
