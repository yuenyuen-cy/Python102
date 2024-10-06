import requests
import os
from twilio.rest import Client

## Codes and personal details redacted due to sensitivity of information

MY_LAT = 1.3840
MY_LONG = 103.7470

API_KEY = os.environ.get("OWM_API_KEY")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

FROM_PHONE = "+123456789"
TO_PHONE = "+123456789"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_ids = []
for item in weather_data["list"]:
    for weather in item["weather"]:
        weather_ids.append(weather["id"])

umbrella_needed = False

for id in weather_ids:
    if id < 700:
        umbrella_needed = True

if umbrella_needed:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Bring an ☂️.",
        from_=FROM_PHONE,
        to=TO_PHONE,
    )

    print(message.status)