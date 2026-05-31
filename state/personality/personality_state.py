import json
import os

class AgentPersonalityState:
  def __init__(self, file_path="personality_data.json"):
    self.file_path = file_path
    self.data = self.load_personality_state()
    
  def load_personality_state(self):
    try:
      if os.path.exists(self.file_path):
        with open(self.file_path, "r") as file:
          return json.load(file)
      else:
        return {
          "user_name": "Aagal",
          "preferences": {
            "communication_style": "simple, sightly humorus",
            "tone": "friendly, helpful, assisting in tasks"
          }
        }
    
    except Exception as e:
      return f"\nError occured (UserPersonality side): \n{e}\n"
      
  def save_state(self):
    try:
      with open(self.file_path, "w") as file:
        json.dump(self.data, file, indent=2)
        
    except Exception as e:
      return f"\nError occured when saving (AgentPersonalityState side): \n{e}\n"
      
