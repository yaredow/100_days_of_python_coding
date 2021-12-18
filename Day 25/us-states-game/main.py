import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = []
while len(guessed_state) < 50:
    user_guess = str(screen.textinput(title="{}/50 correct guess".format(len(guessed_state)),
                                      prompt="What other state name do you know?")).title()
    data = pd.read_csv("50_states.csv")
    list_of_state = data["state"].to_list()
    if user_guess in list_of_state:
        guessed_state.append(user_guess)
        f = turtle.Turtle()
        f.hideturtle()
        f.penup()
        state_data = data[data.state == user_guess]
        f.goto(int(state_data.x), int(state_data.y))
        f.write(user_guess)

    if user_guess == "Exit":
        missed = [state for state in list_of_state if state not in guessed_state]
        break

missed_data = pd.DataFrame(missed)
missed_data.to_csv("states_to_learn.csv")

screen.exitonclick()
