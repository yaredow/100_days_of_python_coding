import requests
import datetime as dt
import os

GENDER = "Male"
WEIGHT_KG = 62
HEIGHT_CM = 168
AGE = 24
APP_ID = "f591d690"
API_KEY = "49875408ab30683f9454b67b1a3a4b39"
TOKEN = os.getenv("SHEETY_TOKEN")
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHITTY_END_POINT = "https://api.sheety.co/4720ea770e594a9ef987fddb9ccb6e73/myWorkout/workouts"
USER_INPUT = input("Tell me which exercise you did? ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
 "query": USER_INPUT,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(url=END_POINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
print(data)
day = dt.datetime.now()
today = day.strftime("%d/%m/%Y")
time = day.strftime("%H:%M:%S")

bearer_header = {
    "Authorization": "Bearer h1234772727jwjwuwwwrrty",
    "Content-Type": "application/json",
}
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": (exercise["user_input"] + "ing").title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response1 = requests.post(url=SHITTY_END_POINT, json=sheet_inputs, headers=bearer_header)
