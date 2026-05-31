from orchestration.agent_loop import run_agent_loop
from services.weather_thread import weather_thread_

# Starting threads
weather_thread_.start()

while True:
  user = input("Ask to Jarvis: ")
  
  if user.lower() == "q":
    break
  
  response = run_agent_loop(user)
  print(response)