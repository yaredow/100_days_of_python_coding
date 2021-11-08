def turn_right():
    turn_left()
    turn_left()
    turn_left()
def num_jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()        
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        num_jump()
    