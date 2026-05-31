from tools.get_weather import GetWeatherInfo
from state.conversation.conversation_window_instance import conversation_window

weather = GetWeatherInfo()

# Getting live weather data
weather_state = weather.get_live_info()

class RuntimeState:
  def __init__(self, model: str = None):
    self.model_name = model
    self.RUNTIME_STATE = {
      "previous_conversations": [], 
      "current_input": None,
      "agent_results": None,
      "environment": weather_state
    }
    
  def update_state(self, agent_result: any = None, user: any = None):
     """ 
     Updates only specific fields
     return: None
     """
     
     # Updating specific fields
     if user is not None:
       self.RUNTIME_STATE["current_input"] = user
     
     if agent_result is not None:
       self.RUNTIME_STATE["agent_results"] = None
       self.RUNTIME_STATE["agent_results"] = agent_result
       
  def refresh_memory_context(self):
    """Now load the universal lang
    memory into model understandable
    schema to previous_conversations field
    in system_state.
    """
    
    self.RUNTIME_STATE["previous_conversations"] = conversation_window.build_model_context(
      model_name = self.model_name
    )
    
  def update_conversation_memory(self, user_message = None, model_message = None):
    """
    Only create the memory entry
    into SHARED_MEMORY using universal
    schema.
    """
    
    if user_message is not None:
      conversation_window.create_entry(
        role="user",
        content=user_message
      )
      
    if model_message is not None:
      conversation_window.create_entry(
        role="model",
        content=model_message
      )
      
    # load memory into model view
    #self.refresh_memory_context()
  
  def get_state(self):
    """
    Get the full system state.
    return: dict
    """
    
    return self.RUNTIME_STATE