from configs.settings import GEMINI_API_ENDPOINT, GEMINI_HEADERS
import json
import requests

# GEMINI LLM CALL
def call_gemini_model(conversation_history, system_ins):
  """
  This function inputs chat history and
  calls a gemini model to get LLM respond.
  """
  
  if conversation_history:
    # Preparing json payload for model
    payload = {
      "system_instruction": {
        "parts": [{"text": system_ins}]
      },
      "contents": conversation_history,
      "generationConfig": {
        "maxOutputTokens": 8192
      }
    }
    
    # Post request to model url
    raw_response = requests.post(
        GEMINI_API_ENDPOINT,
        headers=GEMINI_HEADERS,
        json=payload
      ).json()
      
    if "candidates" in raw_response:
      candidtaes_field = raw_response["candidates"]
      
      if len(candidtaes_field) > 0 and "content" in candidtaes_field[0]:
        content_field = candidtaes_field[0]["content"]
        parts_field = content_field.get("parts", [])
        
        if not parts_field:
          return f"No parts field inside model response: \n{raw_response}\n"
          
        full_text = ""
        for parts in parts_field:
          full_text += parts.get("text", "")
          
        full_text = full_text.strip()
        try:
          return json.loads(full_text)
        except Exception as e:
          return f"INVAILD RESPONSE: \n{raw_response}\nERROR MSG: \n{e}\n"
          
      else:
        return f"No content field inside model response: \n{raw_response}\n"
    else:
      return f"No candidates field inside model response: \n{raw_response}\n"