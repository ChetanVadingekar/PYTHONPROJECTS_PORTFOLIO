import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    
    if data["cod"] == "404":
        print("City not found.")
        return None

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

#  API key from OpenWeatherMap
api_key = 'a51f53c954ec568a3645ab5541de3503'

# Specify the city for which you want to get the weather information
city_name = "Kolhapur"

get_weather(api_key, city_name)
