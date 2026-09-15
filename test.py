from flask import Flask, request, jsonify, send_from_directory
import requests
import json
import os
import time
import threading
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

api_key = os.getenv("API_KEY")
SAVE_FOLDER = "Weather-Log"

os.makedirs(SAVE_FOLDER, exist_ok=True)

def clear_saved_folder():
    while True:
        now = datetime.now()

        # Find the next :00 or :30 mark
        if now.minute < 30:
            next_run = now.replace(minute=30, second=0, microsecond=0)
        else:
            next_run = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

        sleep_seconds = max(0.0, (next_run - now).total_seconds())
        print(f"Next clear at {next_run.strftime('%H:%M')}, sleeping {int(sleep_seconds)}s")
        time.sleep(sleep_seconds)

        for filename in os.listdir(SAVE_FOLDER):
            file_path = os.path.join(SAVE_FOLDER, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Cleared saved_cities folder at", datetime.now().strftime("%H:%M:%S"))

@app.route("/")
def index():
    return send_from_directory(".", "main.html")

@app.route("/weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data["city"]

    filename = os.path.join(SAVE_FOLDER, city + ".json")

    # If a saved file already exists for this city, read from it
    if os.path.exists(filename):
        with open(filename, "r") as file:
            weather = json.load(file)
        print("Loaded from saved file:", filename)
        return jsonify(weather)

    # Otherwise, fetch fresh from the API
    url = "https://api.weatherapi.com/v1/current.json"
    params = {"q": city, "key": api_key}

    response = requests.get(url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        weather = {
            "city": weather_data["location"]["name"],
            "temperature": weather_data["current"]["temp_c"],
            "weather": weather_data["current"]["condition"]["text"],
            "time": weather_data["current"]["last_updated"]
        }

        with open(filename, "w") as file:
            json.dump(weather, file, indent=4)

        print("Saved new file:", filename)
        return jsonify(weather)
    else:
        return jsonify({"error": "City not found"}), 400

@app.route("/saved", methods=["GET"])
def list_saved():
    files = [f.replace(".json", "") for f in os.listdir(SAVE_FOLDER) if f.endswith(".json")]
    return jsonify(files)

# NEW: read one saved city's data
@app.route("/saved/<city>", methods=["GET"])
def get_saved(city):
    filename = os.path.join(SAVE_FOLDER, city + ".json")
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "No saved data for this city"}), 404
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)