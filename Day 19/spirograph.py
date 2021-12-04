from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

def move_forward():
    timy.forward(10)

def move_backward():
    timy.backward(10)

def go_up():
    timy.left(10)
    timy.forward(10)

def go_down():
    timy.left(-10)
    timy.forward(10)



screen.onkey( move_forward, "d")
screen.onkey(move_backward, "a")
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.listen()    
screen.exitonclick()