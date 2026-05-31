from state.conversation.conversation_window_instance import conversation_window
from agents.reflection_agent.agent import extract_events
import json

conversation_window.create_entry(
  role="user",
  content="Hello, its raining outside and feeling msyterious..."
)

conversation_window.create_entry(
  role="user",
  content="Heyy, its evening now, i am looking for some special type of coffee."
)

conversation_window.create_entry(
  role="user",
  content="Jarvis, i am planning to integrate a dynamic hologram model and overlay generation using AI in my Jarvis Vision Glass."
)

conversation_window.create_entry(
  role="user",
  content="hmmm... Jarvis... yesterday i found a msyterious pitch black entity like a thing in my backyard at sunset."
)

res = extract_events(user="Hey Jarvis, good morning today.", conversation_history=conversation_window.build_model_context(model_name="ollama"))

print(json.dumps(res, indent=4))