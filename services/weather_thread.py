from tools.get_weather import GetWeatherInfo
import threading
import time

weather = GetWeatherInfo()

weather_thread_ = threading.Thread(target=weather.get_live_info, daemon=True)

