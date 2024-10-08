import requests
from datetime import datetime

### Create user account ###

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "12345678"
USERNAME = "username"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

### Create a graph ###

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora" #blue
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

### Add a pixel ###

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime(year=2024, month=10, day=7)
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometer did you run today? ")
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)

### Update pixel data ###

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=new_pixel_data, headers=headers)
# print(response.text)

### Delete pixel data ###

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)

