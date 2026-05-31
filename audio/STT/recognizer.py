import os
import time

# filename for getting user input
USER_AUDIO_FILE = "user_command.txt"
text = None

# Jarvis STT(speech-to-text)
def recognize():
  """
  Takes input throught device in-built 
  microphone and place it into text file
  and return the text from the file.
  """
  
  # recognize using termux-api
  print("Listening...")
  time.sleep(1)
  os.system(f"termux-speech-to-text > '{USER_AUDIO_FILE}'")
  time.sleep(2)
  
  # checking and returning text from file
  if os.path.exists(USER_AUDIO_FILE):
    with open(USER_AUDIO_FILE, "r") as recent_file:
      text = recent_file.read()
      
    return text
    
  else:
    print(f"No file named {USER_AUDIO_FILE}")