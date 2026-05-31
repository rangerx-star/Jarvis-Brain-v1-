class ConversationWindow:
  def __init__(self):
    self.SHARED_MEMORY = []
    
  def create_entry(self, content: dict = None, role: str = None, metadata: dict = None):
    if role is not None and content is not None and metadata is not None:
      self.SHARED_MEMORY.append({
        "role": role,
        "message": content,
        "others": metadata
      })
    
    else:
      self.SHARED_MEMORY.append({
        "role": role,
        "message": content
      })
    
  def build_model_context(self, limit: int = 0, model_name: str = None):
    self.TRANSCRIPTED_MEMORY = []
    
    if model_name is not None:
      
      if model_name == "gemini":
        for memory in self.SHARED_MEMORY:
          self.TRANSCRIPTED_MEMORY.append({
            "role": memory["role"],
            "parts": [{"text": memory["message"]}]
          })
          
      elif model_name == "ollama":
        for memory in self.SHARED_MEMORY:
          if "others" in memory:
            self.TRANSCRIPTED_MEMORY.append({
              "role": memory["role"],
              "content": memory["message"],
              "metadata": memory["others"]
            })
          
          else:
            self.TRANSCRIPTED_MEMORY.append({
              "role": memory["role"],
              "content": memory["message"]
            })
          
      else:
        raise ValueError(
          f"\nNo model context translater for {model_name}"
        )
        
      return self.TRANSCRIPTED_MEMORY[-limit:]