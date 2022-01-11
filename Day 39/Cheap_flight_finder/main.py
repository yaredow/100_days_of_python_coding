from data_manager import DataManager
from pprint import pprint

data = DataManager()
sheet_data = data.get_final_data()
city_name = []
for city in sheet_data:
    city_name.append(city["city"])

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data: {sheet_data}")
    data.final_data = sheet_data
    data.update_the_sheet()






