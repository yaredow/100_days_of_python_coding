from bs4 import BeautifulSoup
import requests
user_input = input("what year you would like to travel to in YYY-MM-DD? ")
Url = f"https://www.billboard.com/charts/hot-100/{user_input}/"
response = requests.get(Url)
billboard_data = response.text
soup = BeautifulSoup(billboard_data, "html.parser")
print(soup.prettify())