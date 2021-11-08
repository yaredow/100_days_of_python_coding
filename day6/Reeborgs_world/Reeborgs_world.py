def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

# or using while loop instead

number_of_hurdle = 6
while number_of_hurdle > 0:
    jump()
    number_of_hurdle -= 1
    print(number_of_hurdle)
    