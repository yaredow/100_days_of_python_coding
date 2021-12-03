from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.pensize(10)
screen.colormode(255)

direction = [0, 90, 180, 270]

def color_choice():
    r= random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for _ in range(300):
    tim.pencolor(color_choice())
    tim.forward(25)
    tim.setheading(random.choice(direction))


screen.exitonclick()


