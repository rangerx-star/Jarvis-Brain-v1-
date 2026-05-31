from configs.settings import OPEN_WEATHER_API_ENDPOINT
import requests
import json
import time

class GetWeatherInfo:
  def __init__(self):
    self.WEATHER_STATE = {
      "weather_description": None,
      "temperature": None,
      "wind_speed": None
    }
    
  def get_live_info(self):
    while True:
      try:
        self.response = requests.get(OPEN_WEATHER_API_ENDPOINT).json()
      
      except Exception as e:
        return f"\nREQUESTS ERROR > error: {e}"
        
      if "weather" in self.response:
        self.WEATHER_STATE["weather_description"] = self.response["weather"][0].get("description")
      else:
        return f"\nNo weather field inside response: \n{self.response}"
      
      if "main" in self.response:
        self.WEATHER_STATE["temperature"] = self.response["main"].get("temp")
      else:
        return f"\nNo main field inside response: \n{self.response}" 
        
      if "wind" in self.response:
        self.WEATHER_STATE["wind_speed"] = self.response["wind"].get("speed")
      else:
        return f"\nNo wind field inside response: \n{self.response}"
        
      
      return self.WEATHER_STATE
      
      # Update timing
      time.sleep(3000)