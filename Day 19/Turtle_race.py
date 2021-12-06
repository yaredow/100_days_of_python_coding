from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
screen = Screen()
screen.setup(500, 400)
user_input = screen.textinput(title="make your bet", prompt="Which turtle will win? enter color")
tom.shape("turtle")
tom.color("green")
tim.shape("turtle")
tim.color("purple")
tim.goto(x=(-250), y = 0)
tom.setheading(90)
tom.forward(10)
tom.setheading(0)
tom.goto(x=(-250), y=20)
tim.forward(10)
tom.forward(40)




screen.exitonclick()
