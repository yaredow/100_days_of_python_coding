import requests

FLIGHT_SEARCH_END_POINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "_F0Awr2BLPBjdtlI_b6gLb2cJDJBW8y0"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{FLIGHT_SEARCH_END_POINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        print(response.text)
        data = response.json()
        results = data["locations"]
        code = results[0]["code"]
        return code
