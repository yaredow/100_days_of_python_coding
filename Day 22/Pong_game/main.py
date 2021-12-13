from turtle import Screen
from paddle import L_paddle
from paddle import R_paddle
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()



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

    # detect collusion with upper and lower ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collusion with both paddles and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # detect if the boll is beyond the right paddle
    if ball.xcor() > 380:
        ball.reset_ball()

    # detect if the boll is beyond the left paddle
    if ball.xcor() < -380:
        ball.reset_ball()










screen.exitonclick()
