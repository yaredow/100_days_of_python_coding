import requests
import datetime as dt


USER_NAME = "yared"
TOKEN = "hdjeuekskslie"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPHID}"
user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=pixela_endpoint, json=user_param)

graph_param = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

# response1 = requests.post(url=graph_endpoint, json=graph_param, headers=headers)

today = dt.datetime(year=2021, month=12, day=31)
year = today.strftime("%Y")
day = today.strftime("%d")
month = today.strftime("%m")
date = f"{year}{month}{day}"
post_pixel_param = {
    "date": date,
    "quantity": "10",
}
post_header = {
    "X-USER-TOKEN": TOKEN
}
response2 = requests.post(url=post_endpoint, json=post_pixel_param, headers=post_header)
response2.raise_for_status()
print(response2.text)