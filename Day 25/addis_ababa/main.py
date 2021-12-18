import pandas as pd
import turtle

screen = turtle.Screen()
image = "addis_ababa.gif"
screen.addshape(image)
turtle.shape(image)

num_guess = []
while len(num_guess) < 10:
    user_guess = str(screen.textinput(title="{}/10 correctly guessed".format(len(num_guess)),
                                      prompt="How many other sub-city can you guess?")).title()
    cities = pd.read_csv("Sheger_cities.csv")
    list_of_cities = cities.City.to_list()

    if user_guess in list_of_cities:
        num_guess.append(user_guess)
        sheger = turtle.Turtle()
        sheger.hideturtle()
        sheger.penup()
        city_row = cities[cities.City == user_guess]
        sheger.goto(int(city_row.x), int(city_row.y))
        sheger.write(user_guess, font=("Courier", 10, "normal"))

    if user_guess == "Exit":
        correct_guess = [sub_city for sub_city in list_of_cities if user_guess not in list_of_cities]
        break

df = pd.DataFrame(correct_guess)
df.to_csv("Sub_cities_for_study.csv")

screen.exitonclick()
