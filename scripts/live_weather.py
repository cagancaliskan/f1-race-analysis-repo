import requests
import os

# Load API Key from environment variable (Set it before running)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
CITY = "Monza"

def get_weather():
    """Fetches real-time weather data for the F1 track location."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch weather data"}
    
    data = response.json()
    
    weather_info = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_condition": data["weather"][0]["main"]
    }

    return weather_info

if __name__ == "__main__":
    print(get_weather())  # Test function
