from memory.episodic.episodic import create_episode
from state.conversation.conversation_window_instance import conversation_window


conversation_window.create_entry(
  role="user",
  content="Heyy"
)
conversation_window.create_entry(
  role="user",
  content="I yesterday started building an agentic system called Jarvis Brain."
)
conversation_window.create_entry(
  role="user",
  content="I am planning to scale it with a vision system."
)
conversation_window.create_entry(
  role="user",
  content="hey jarvis, i am currently very much stressed because, i don't have the right tools to build what i am imagining."
)



print(create_episode("", conversation_window.build_model_context(model_name="ollama")))