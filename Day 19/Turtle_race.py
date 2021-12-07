import random
from turtle import Turtle,  Screen

is_race_on = False
screen = Screen()
screen.colormode(255)
screen.screensize(canvwidth=600, canvheight=600)
color = ["yellow", "black", "red", "blue", "orange", "purple"]
user_input = screen.textinput(title="Make your bet", prompt="Make a guess. Insert the color of your turtle")
all_turtle = []
y_directions = [-70, -40, -10, 20, 50, 80]
for turtles in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-290, y=y_directions[turtles])
    all_turtle.append(new_turtle)
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 280:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_input == winner_color:
                print("You have won. The {} turtle is the winner!".format(winner_color))
            else:
                print("You have lost. The {} turtle is the winner!".format(winner_color))

        running_distance = random.randint(0, 10)
        turtle.forward(running_distance)

screen.exitonclick()
