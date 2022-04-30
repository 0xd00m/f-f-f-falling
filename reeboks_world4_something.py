def turn_right():
    for i in range(3): turn_left()

while at_goal() == False:
    while (front_is_clear() == True) or at_goal == False:
        move()
    if wall_on_right() == False or at_goal == True:
        turn_right()
        move()
    else:
        turn_left()