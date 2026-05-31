#from tools.web_search import search
from tools.webscraper import WebScraper

webscraper = WebScraper()

AVAILABLE_TOOLS = {
  "web_scrape": webscraper.perform_webscrape
}
