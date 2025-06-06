import requests

def get_weather(city_name):
    api_key = "2f4c30e33ee845dd83975703212212"  # Replace with your real API key
    base_url = "https://api.weatherapi.com/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found.")
        return

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"Weather in {city_name}:\n"
          f"Temperature: {temp}°C\n"
          f"Condition: {description}\n"
          f"Humidity: {humidity}%\n"
          f"Wind Speed: {wind} m/s")

# Example use
get_weather("Jamshedpur")

# # | Weather API        | Accuracy | Free Tier | Ease of Use | Best For                        |
# # |--------------------|----------|-----------|-------------|---------------------------------|
# # | **OpenWeatherMap** | ✅ Good  | ✅ Yes     | ✅ Easy      | Beginners, general weather info |
# # | **WeatherAPI**     | ✅ Good  | ✅ Yes     | ✅ Easy      | Forecasts, clean JSON data      |
# # | **Tomorrow.io**    | ✅ Great | ✅ Yes     | ⚠️ Medium    | Hyper-local data, advanced use  |
# # | **AccuWeather**    | ✅ Great | ⚠️ Limited | ⚠️ Complex   | Professional apps, alerts       |
# # | **Weatherstack**   | ✅ Okay  | ✅ Yes     | ✅ Easy      | Simple current weather only     |

