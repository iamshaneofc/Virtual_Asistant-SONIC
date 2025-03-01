import requests
from voice import speak  # Import the speak function from utils

def get_weather(city):
    """Fetches weather details for the given city using OpenWeather API."""
    API_KEY = "77992d17d1fbb947f42271f4206df5ce"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url).json()
        
        if response["cod"] != 200:
            speak("Sorry, I couldn't get the weather details.")
            return
        
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]

        weather_info = (f"The weather in {city} is currently {desc} with a temperature of {temp}°C. "
                        f"Humidity is at {humidity}%, and wind speed is {wind_speed} meters per second.")
        
        print(weather_info)
        speak(weather_info)

    except Exception as e:
        print(f"Error fetching weather: {e}")
        speak("I encountered an issue while fetching the weather.")

