from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_data = response.text
soup = BeautifulSoup(movie_data, "html.parser")
movie_title = soup.find_all(name="h3", class_="jsx-4245974604")
all_movies_list = [title.getText for title in movie_title]
movie = all_movies_list[::-1]

with open("100-best_movies_of_all_time", mode="w") as file:
    file.write(f"{movie}\n")