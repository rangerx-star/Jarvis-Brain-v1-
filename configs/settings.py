from dotenv import load_dotenv
import os

load_dotenv()

# API-KEYs
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

# URLs & HEADERs For Models

GEMINI_API_ENDPOINT = ("https://generativelanguage.googleapis.com/v1beta/" "models/gemini-2.5-flash:generateContent" f"?key={GEMINI_API_KEY}")
GEMINI_HEADERS = {"Content-Type": "application/json"}

OLLAMA_ENDPOINT = "http://localhost:11434/api/chat"

OPEN_ROUTER_API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
OPEN_ROUTER_HEADERS = {"Authorization": f"Bearer {OPEN_ROUTER_API_KEY}", "Content-Type": "application/json"}

# URLs & Configs for tools
DUCKDUCKGO_SEARCH_ENDPOINT = "https://html.duckduckgo.com/html/"

LAT = "9.2655337"
LON = "76.7871514"
OPEN_WEATHER_API_ENDPOINT = ("https://api.openweathermap.org/data/2.5/weather?" f"lat={LAT}&lon={LON}" f"&appid={OPEN_WEATHER_API_KEY}")