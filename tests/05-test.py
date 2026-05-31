from state.runtime.runtime_state_instance import runtime_state
from agents.conversation_agent.agent import call_conversation_agent
from state.conversation.conversation_window_instance import conversation_window
from memory.episodic.episodic import load_episode, create_episode
from agents.retrieval_agent.agent import retrieve_relavent_context

while True:
  runtime_state.refresh_memory_context()
  
  user = input("Ask Agent > ")
  
  retrived_context = retrieve_relavent_context(user, load_episode())
  
  runtime_state.update_state(user=user)
  res = call_conversation_agent(retrived_context)



  print(f"\nAgent response: {res}")
  
  runtime_state.update_conversation_memory(user_message=user, model_message=res)
  
  user_chat_window = conversation_window.build_model_context(model_name="ollama")
  create_episode(user, user_chat_window)
  
  