import requests
from datetime import datetime as dt
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "**********"
TOKEN = "**********"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creating a Graph using this api
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph001"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding Habit Graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN":  TOKEN
}

# Post the pixel into your graph
today = dt.now()

POST_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many duration you are coding today? "),
}

# Update the graph pixel by following code
UPDATE_ENDPOINT = f"{POST_PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}"
update_param = {
    "quantity": "59"
}
response = requests.put(url=UPDATE_ENDPOINT, json=update_param, headers=headers)
print(response.text)
