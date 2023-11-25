# Author Guson Ulysse
# Date : 11/25/2023
import requests
from datetime import datetime
import os

# Pixela account token and username
MYTOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = "chillsu"

# Base endpoint URL for Pixela
pixela_endpoint = "https://pixe.la/v1/users"

# Configuration for creating a new Pixela user
user_params = {
    "token": MYTOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment to make a POST request to create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Endpoint URL for creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",                     # ID for the graph
    "name": "Coding Graph",             # Name of the graph
    "unit": "Hours",                    # Unit of measurement
    "type": "int",                      # Data type (integer)
    "color": "kuro"                     # Color of the graph
}

# Headers for authentication
headers = {
    "X-USER-TOKEN": MYTOKEN
}

# Uncomment to make a POST request to create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Endpoint URL for adding data to the graph
data_to_graph_endpoint = f"{graph_endpoint}/graph1"

# Getting the current date
today_date = datetime.now()

# Configuration for adding a pixel to the graph
pixels_config = {
    "date": today_date.strftime("%Y%m%d"),              # Current date in 'YYYYMMDD' format
    "quantity": input("How many hours did you put in how raising your skills today?"),
}

# Making a POST request to add data to the graph
response = requests.post(url=data_to_graph_endpoint, json=pixels_config, headers=headers)
print(response.text)
