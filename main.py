# MAIN ENTRY POINT JARVIS BRAIN

from orchestration.agent_loop import run_agent_loop
from audio.STT.recognizer import recognize
from audio.TTS.synthesizer import synthesize
import time


# exit sequences
possible_exit_sequences = ["bye", "exit", "quit"]

def start_jarvis_brain():
  """
  Jarvis brain starting function with
  combined recognition and synthesizer.
  """
  
  while True:
    user_command = recognize()
    
    if user_command in possible_exit_sequences:
      print("\nJARVIS TERMINATED...")
      break
    
    response = run_agent_loop(user_command)
    print(response)
    time.sleep(.5)
    synthesize(response)
    
if __name__ == "__main__":
  start_jarvis_brain()
      