#from state.conversation.conversation_window_instance import conversation_window
from agents.reflection_agent.agent import extract_events
from pathlib import Path
from datetime import datetime
import json
import os

# CONSTANTS
BASE_DIR = Path(__file__).resolve().parent
EPISODES_DIR = BASE_DIR / "episodes"
EPISODES_DIR.mkdir(exist_ok=True)

# Creating date-based new file
today_date = datetime.now().strftime("%Y-%m-%d")
filename = f"{today_date}.json"
path = EPISODES_DIR / filename

def load_all_episodes():
  pass

def load_episode():
    if not os.path.exists(path):
      with open(path, "w") as ep_file:
        json.dump([], ep_file, indent=4)
        
      return []
      
    else:
      try:
        with open(path, "r") as ep_file:
          return json.load(ep_file)
          
      except Exception as e:
        return f"\nError occured (episode loader side): \n{e}\n"
    
def generate_episode_id():
  episodes = load_episode()
  
  if not episodes:
    return "ep-001"
    
  last_episode = episodes[-1:]
  last_id = last_episode[0].get("id")
  
  last_id_num = int(last_id.split("-")[1])
  
  return f"ep-{last_id_num + 1:03d}"

def save_episode(episode_state):
  episodes = load_episode()
  
  episodes.append(episode_state)
  
  with open(path, "w") as ep_file:
    json.dump(episodes, ep_file, indent=4)

def create_episode(current_input: str, user_chat_window: dict):
  if len(user_chat_window) > 3:
    reflection = extract_events(
      user=current_input,
      conversation_history=user_chat_window
    )
    
    # episode Parsing
    episode = reflection.get("ep")
    conversation_summary = reflection.get("sum")
    
    episode_state = {
      "id": generate_episode_id(),
      "time": datetime.now().astimezone().isoformat(),
      "summary": conversation_summary,
      "episode": episode
    }
    
    
    save_episode(episode_state)
    
    return f"\nepisodic memory status: episode file '{filename}' saved with id '{episode_state['id']}'"
    
  else:
    return "\nepisodic memory status: No episode created."