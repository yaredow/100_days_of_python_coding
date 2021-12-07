from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
all_turtle = []

starting_position  = [(0, 0), (-20, 0), (-40, 0)]

snakes = []
for position  in starting_position:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    snakes.append(snake)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    for num_snake in range(len(snakes)-1, 0, -1):
        new_x = snakes[num_snake - 1].xcor()
        new_y = snakes[num_snake - 1].ycor()
        snakes[num_snake].goto(new_x, new_y)
    snakes[0].forward(20)
    snakes[0].right(90)









screen.exitonclick()