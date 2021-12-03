from turtle import *
import random

tim = Turtle() 
tim.shape("turtle")

color_list = ["dim gray", "navy", "dark green", "brown", "blue violet", "orange", "dark slate gray", "black", "yellow", "red"]

def color_choice():
    random.choice(color_list)
    tim.color(random.choice(color_list))

def draw_polygon(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)
        

for num_side in range(3, 11):
    tim.pensize(5)
    draw_polygon(num_side)
    color_choice()

screen = Screen()
screen.exitonclick()