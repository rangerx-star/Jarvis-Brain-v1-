import requests
import json
from configs.settings import OPEN_ROUTER_API_ENDPOINT
from configs.settings import OPEN_ROUTER_HEADERS

class OpenRouterModel:
  def __init__(self, model_name):
    self.MODEL_NAME = model_name
    
  def call_model(self, chat_history: dict, system_ins: str):
    self.chat_history = chat_history
    
    self.chat_history.append({
      "role": "system",
      "content": system_ins
    })
    
    self.payload = {
      "model": self.MODEL_NAME,
      "messages": chat_history
    }
    
    try:
      self.response = requests.post(
        OPEN_ROUTER_API_ENDPOINT,
        headers=OPEN_ROUTER_HEADERS,
        json=self.payload,
        timeout=64
      )
      
      if self.response.status_code != 200:
        print(f"\nHTTP ERROR (model side) > status: {self.response.status_code} | returned: {self.response}")
        
    except Exception as e:
      print(f"\nREQUESTS ERROR (model side) > returned: {self.response} | error: {str(e)}")
      
    data = self.response.json()
    
    """ choices -> first element -> message -> content """
    
    if "choices" in data:
      choices_field = data.get("choices", {})
      
      # Checking if it has more than one item and message or not.
      if len(choices_field) > 0 and "message" in choices_field[0]:
        message_field = choices_field[0].get("message", {})
        
        if "content" in message_field:
          try:
            #json.loads(message_field["content"])
            return message_field["content"]
          except Exception as e:
            return f"\nInvaild structure inside model response: \n{data}\nERROR MSG: \n{e}\n"
      
        else:
          return f"\nNo content field inside message field: \n{data}\n"
      else:
        return f"\nNo message field inside list choices: \n{data}\n"
    else:
      return f"\nNo choices field inside model response: \n{data}\n"