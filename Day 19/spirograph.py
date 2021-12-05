from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

def left():
    timy.backward(10)

def right():
    current_heading = timy.heading()
    timy.setheading(current_heading + 10)
    timy.backward(10)

def move_forward():
    timy.forward(10)

def move_backward():
    timy.backward(10)

def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()


screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(clear, "c")
screen.listen()    
screen.exitonclick()