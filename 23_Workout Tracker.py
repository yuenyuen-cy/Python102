import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_AUTH = os.environ["BEARER_AUTH"]
WEIGHT = 55
HEIGHT = 154
AGE = 29

if not APP_ID or not API_KEY or not BEARER_AUTH:
    print("Error: One or more environment variables are not set.")
else:
    print("All environment variables are set.")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("What exercise did you do today? ")

parameters = {
    "query": exercise_input,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
              }

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = exercise_response.json()

sheet_endpoint = os.environ["sheet_endpoint"]

today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
time_now = today.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories":  exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorisation": f"Bearer {BEARER_AUTH}"
    }

    sheet_response = requests.post(url = sheet_endpoint, json= sheet_input, headers = bearer_headers)

    print(sheet_response.text)