# Python language basics 5
# while loops
# for in loops


is_game_over = False
p_x_pos = 6
e_x_pos = 3
end_x_pos = 10


while not is_game_over:   #this will loop infinetly until the condition below checks as false
    # do something
    print(p_x_pos)   #this will show the progress of player till the goal
    print(e_x_pos)   #this will show the progress of enemy till the goal
    if p_x_pos == e_x_pos:
        print("you lose")    
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        print("You win")
        is_game_over = True
    else:    #update player and enemy position
        p_x_pos += 2
        e_x_pos += 1

    # the continue operator makes you loop again faster
    # the break operator makes your loop to stop

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

for movement in movements: # movement is going to equal each of the numbers on the movement array
    # moving one index to the right each time it loops
    x_pos += movement # this will be added to x_pos, and at the end, the total numbers added will be printed
print(x_pos) 
