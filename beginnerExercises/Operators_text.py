# Python language basics 1
# Variable syntax
# Variable types: ints, floats, booleans, strings

#Int / position a player occupies on x axis on a game
x_pos = 5

#Float
speed = 2.5

#Boolean
is_game_over = False

#string
character_name = "Joseles"

#This will prin the type of variable "x_pos" is
#In this case, its "int"
# print(type(x_pos))

#if we redifine x_pos next time we print it, it will have a new value
#  x_pos = "fadsfd"

# print(type(x_pos))

# Python language basics 2
# Operations
# Assignment: = not
# Arithmetic: + - * / % // += -= *= /= **
# Conditional: > >= < <= != ==

x_pos = speed    # x_pos = 2.5

#Assignment
is_not_game_over = not is_game_over       #is_not_game_over = true

print(is_not_game_over) #prints true

#Arithmetic
new_x_pos = x_pos + speed  #new_x_pos = 5

full_name = character_name + " Narang" #full_name = Joseles Narang

x_pos = 5

mod_x_pos = 5 % 2 # mod_x_pos = 1 (5 / 2 = 2, with a remainder of 1, % gets the remainder)

floor_div_x_pos = x_pos // 2  #floor_dix_x_pos = 2 (5/2 = 2, the result is whats shown with //

x_pos_squared = x_pos**2  # x_pos_squared = 25

x_pos += 5      # X_pos = 10

#conditionals

5 < 2 = false

5 == 2 = false

is_true = 5 > 2    # is_true = True





