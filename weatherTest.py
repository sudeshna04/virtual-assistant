import requests
import os
import pyttsx3
import requests
import speech_recognition as sr
import eel
import time

import platform
import subprocess
def speak(text1):
    text1=str(text1)
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)  
    # eel.DisplayMessage(text1)  
    engine.say(text1)
    # eel.receiverText(text1)
    engine.runAndWait() 
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
# API_KEY = WeatherAPI
# city = "Jamshedpur"
# weather_info = get_weather(city, API_KEY)
# print(weather_info)
# speak(f"The weather in {weather_info['city']} is {weather_info['description']} with a temperature of {weather_info['temperature']} degrees Celsius, humidity at {weather_info['humidity']} percent, and wind speed of {weather_info['wind_speed']} meters per second.")