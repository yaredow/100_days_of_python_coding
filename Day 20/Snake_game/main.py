from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")


snake = Snake()
snake.create_snake()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()