import requests
import os
from dotenv import load_dotenv

# Încarcă variabilele din fișierul .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    result = get_weather_data("Iasi,RO")
    print(result)