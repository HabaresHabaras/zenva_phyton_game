# Python language basics 4
# Control flow
# If statements

# p_0_x =Player 0 x position
# e_0_x_pos=Enemy 0 x position

is_game_over = False
p_0_x_pos = 0
e_0_x_pos = 3
e_1_x_pos = 5


#if player 0 x pos = enemy x pos, which is 3, then print "game over" and set is_game_over to true
p_0_x_pos += 6

if p_0_x_pos == e_0_x_pos: # if this statement is = False skip code below, else, run it
    is_game_over = True
    print(is_game_over)
    print("game over")
elif p_0_x_pos == e_1_x_pos:  # elif is short for else if. 
    is_game_over = True
else:      #carried out if all the above tests fail
    e_0_x_pos += 1
    e_1_x_pos += 1
    print("increased up")

# indentation is what tells the computer which actions get executed with which condition
# and / or operators to make the code above more efficient

if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:   #If the first condition or the second one are true, the code is ran
    # if we use and, instead of or, above, then both conditions have to be true for the code to run
    is_game_over = True
    print(is_game_over)
    print("game over")  
else:      #carried out if all the above tests fail
    e_0_x_pos += 1
    e_1_x_pos += 1
    print("increased up")

