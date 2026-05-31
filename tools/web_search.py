import wikipedia

def search(query: str) -> str:
  summarized_result = wikipedia.summary(
      query,
      sentences=2
    )
    
  if not summarized_result:
    return "No result from wikipedia."
    
  return summarized_result