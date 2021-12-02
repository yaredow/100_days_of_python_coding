from turtle import *
tim = Turtle() 
tim.shape("turtle")
tim.color("red", "green")

def draw_polygon(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)
for num_side in range(3, 11):
    draw_polygon(num_side)

screen = Screen()
screen.exitwhenclick()