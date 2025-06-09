import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

WeatherAPI = os.getenv("WeatherAPI")

print("API Key loaded:", bool(WeatherAPI)) 
def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

# Example usage
API_KEY = WeatherAPI
city = "London"
weather_info = get_weather(city, API_KEY)
print(weather_info)
