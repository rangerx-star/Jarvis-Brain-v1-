from bs4 import BeautifulSoup
import requests
from configs.settings import DUCKDUCKGO_SEARCH_ENDPOINT
from agents.summarizer_agent.agent import summarize
import os

# AI Web Web Scraping
class WebScraper:
  def __init__(self):
    # GLOBAL VARIABLEs
    self.HTTP_REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    self.extracted_search_links = []
    self.KNOWLEDGE_BASE_PATH = "agents/summarizer_agent/knowledge_base.txt"
    
  def fetch_search_urls(self, search_query: str):
    """Function for fetching webpage urls 
    from duckduckgo and returning the top links."""
    
    self.extracted_search_links = []
    
    try:
      # Getting search results including vid, img, text, links...
      self.search_response = requests.post(
        DUCKDUCKGO_SEARCH_ENDPOINT,
        headers=self.HTTP_REQUEST_HEADERS,
        data={"q": search_query},
        timeout=5
      )
      
      if self.search_response.status_code != 200:
        return f"HTTP ERROR > Status code: {self.search_response.status_code}"
        
    
    except Exception as e:
      return f"REQUEST ERROR: \n{str(e)}"
    
    # Converting raw search result page into html for easy scraping.
    self.parsed_search_html = BeautifulSoup(
      self.search_response.text,
      "html.parser"
    ) 
    
    # Taking every anchor tag in search html page for links.
    for a in self.parsed_search_html.select(".result__a"):
      self.extracted_search_links.append(a.get("href", ""))
      
    # Returning only top links/urls.
    return self.extracted_search_links[:3] # only 3 links
    
  def scrape_page(self, urls: str):
    """ 
    Function for scraping only needed
    text info about the query from the 
    above searched urls.
    """
    
    for url in urls:
      # Getting raw webpage from the url.
      self.webpage_response = requests.get(
        url,
        headers=self.HTTP_REQUEST_HEADERS,
        timeout=5
      )
      
      if self.webpage_response.status_code != 200:
        return f"HTTP ERROR > Status code: {self.webpage_response.status_code}"
      
      # Converting raw webpage content into html for scraping.
      self.parsed_webpage_html = BeautifulSoup(
        self.webpage_response.text,
        "html.parser"
      )
      
      # Removing unwanted tags
      for removable_tags in self.parsed_webpage_html(["script", "style"]):
        removable_tags.decompose()
      
      # Taking every paragraph tag from html page
      self.paragraph_elements = self.parsed_webpage_html.find_all("p")
      self.extracted_page_text = ""
      
      # For every top paragraphs, taking all text info only.
      for paragraph_element in self.paragraph_elements[:3]:
        self.extracted_page_chuck = paragraph_element.get_text() + " "
        self.extracted_page_text += self.extracted_page_chuck
      
      # making cleaned and only limited text
      self.cleaned_page_text = " ".join(self.extracted_page_text.split())[:1000]
        
      # Writing text into text file
      with open("agents/summarizer_agent/knowledge_base.txt", "w") as knowledge_base_file:
        knowledge_base_file.write(self.cleaned_page_text)
        
    return "Scraping Done, Uploaded into knowledge base."
        
  def summarize_text_content(self, user):
    """
    For summarizing knowledge_base/scraped text
    """
    
    if os.path.exists(self.KNOWLEDGE_BASE_PATH):
      with open(self.KNOWLEDGE_BASE_PATH) as knowledge_base:
        self.contents = knowledge_base.read()
        
    else:
      return "No Knowledge base file found."
      
    if not self.contents:
      return "Nothing inside contents (summarization side)"
      
    return summarize(self.contents, user)
    
  def perform_webscrape(self, user_search_query: any):
    """
    Main wrapper function combining 
    every functions creating a workflow.
    """
    
    page_urls = self.fetch_search_urls(user_search_query)
    scraping_status = self.scrape_page(page_urls)
    summarized_text = self.summarize_text_content(user_search_query)
    
    if scraping_status:
      return summarized_text