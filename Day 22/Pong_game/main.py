from turtle import Screen
from paddle import L_paddle
from paddle import R_paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(100)
screen.title("Pong")
r_paddle = R_paddle()
l_paddle = L_paddle()
ball = Ball()



screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.listen()
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_movement()










screen.exitonclick()
