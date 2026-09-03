import requests
import json

# API_KEY = "9b2e0c9c52246a49ceefb5cdb81b9e6b"

# url = "https://api.openweathermap.org/data/2.5/weather"

API_KEY = "427ba6220967431ca99114314260109"

url = "https://api.weatherapi.com/v1/current.json"

params = {
    "q": "Heerenveen",
    "key": API_KEY,
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    weather = {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "weather": data["current"]["condition"]["text"],
        "time": data["current"]["last_updated"]
    }

    with open("weather.json", "w") as file:
        json.dump(weather, file, indent=4)

    print("Weather saved to weather.json")
else:
    print("Error:", data)