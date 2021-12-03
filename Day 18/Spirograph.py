from turtle import Turtle, Screen
import random
timy = Turtle()
screen = Screen()
screen.colormode(255)
timy.speed("fastest")


def color_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_spirograph(size_of_the_gap):
    for _ in range(int(360 / size_of_the_gap)):
        timy.pencolor(color_choice())
        timy.circle(100)
        current_heading = timy.heading()
        timy.setheading(current_heading + size_of_the_gap)
draw_spirograph(5)






screen.exitonclick()


