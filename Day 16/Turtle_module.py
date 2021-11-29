# from turtle import * 

# my_turtle =Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("red", "yellow")
# my_turtle.forward(100)
# my_screen = Screen()
# print(my_turtle)
# print(my_screen)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokeman name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)