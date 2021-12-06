import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_input = screen.textinput(title="make your bet", prompt="Which turtle will win? enter color")
color = ["red", "blue", "yellow", "purple", "green", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtle = []

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=(-230), y=y_positions[turtles])
    new_turtle.color(color[turtles])
    all_turtle.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_input:
                print("You have won. {} win the game".format(winner_color))
            else:
                print("You have lost. {} is the winner".format(winner_color))

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()