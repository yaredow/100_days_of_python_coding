import requests
from pprint import pprint

SHEETY_END_POINT = "https://api.sheety.co/4720ea770e594a9ef987fddb9ccb6e73/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.final_data = {}

    def get_final_data(self):
        response = requests.get(url=SHEETY_END_POINT)
        data = response.json()
        self.final_data = data["prices"]
        return self.final_data

    def update_the_sheet(self):
        for city in self.final_data:
            new_city = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response1 = requests.put(
                url=f"{SHEETY_END_POINT}/{city['id']}",
                json=new_city
            )
            print(response1.text)

