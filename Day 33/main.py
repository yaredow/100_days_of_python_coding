import requests
from datetime import *

My_lat = 9.003168
My_lng = 38.742802
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# iss_position = (latitude, longitude)

parameters = {
    "lat": My_lat,
    "lng": My_lng,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)
# fetching current time
time_now = datetime.now()
print(time_now.hour)
