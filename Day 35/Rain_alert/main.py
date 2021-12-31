import requests
from twilio.rest import Client
import os

account_sid = "ACe8a33132e138ffa600f277406243884f"
auth_token = "ca05860ffa1d1b08f289947ed981391d"
api_key = os.environ.get("OWN_API_KEY")
parameters = {
    "lat": 25.299030,
    "lon": 91.583321,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
will_rain = False
for hourly_data in weather_slice:
    new_data = hourly_data["weather"][0]["id"]
    if int(new_data) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain. don't forget to bring umbrella",
        from_='+13236010511',
        to='+251928315616'
    )
    print(message.status)
