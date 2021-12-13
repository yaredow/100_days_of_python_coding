from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)

    def ball_movement(self):
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(new_x, new_y)

    def refresh(self):
        pass
        



