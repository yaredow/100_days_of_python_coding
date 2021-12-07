from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Class Module"""
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)


    def move(self):
        for num_snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[num_snake - 1].xcor()
            new_y = self.snakes[num_snake - 1].ycor()
            self.snakes[num_snake].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

