# Python language basics 3
# Collections
# Tuples, arrays/lists, dictionaries


# pos_x = 5
# print(type(pos_x))
# is_true = (pos_x) > 3
# print(is_true)


#Tubles / can store variables and elements, but they cant be changed, moved or added
#Arrays / can be changed, and store variables and elements
#Dictionaries / store values by keys, not an index(0, 1, 2, 3 ...)

size = (100, 200)    #on size we can store height and width, as just one tuble
print(size)

width = size[0]
height = size[1]

#by using index, you can select one part of size, and define it as width
print(width)

#tubles cant be changed, but can be reassigned on a new tuble, like this:

new_size = size + (300, 400, 500, 600,  )

#we can also delete a new tuble with del, as: del new_size
print(new_size)
 
print(len(new_size)) # 6
print(max(new_size)) # 600
print(min(new_size)) # 100

does_contain = 100 in size  #does_contain = True

print(does_contain)

contains_too = 150 in new_size #contains_too = false

print(contains_too)

movement = [5, -2, -3, 4, -1]
first_movement = movement[0]   #first_movement = 5
movement[0] = 7  #Now movement[0] = 7, but first_movement stays at 5, cuz it was defined before this
movement.append(-5) #movement = [7, -2, -3, 4, -1, -5]
movement.remove(-3) #movement = [7, -2, 4, -1, -5]


#dictionary
starting_positions = {"p_0": 50,"p_1": 100,"p_2": 150}
#to access an element from a dictionary, you have to call the key
starting_positions["p_0"]  #50

#this will log the keys in the dictionary
print(starting_positions.keys())
