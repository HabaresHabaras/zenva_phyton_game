# Python language basics 7
# Classes and objects
# Class fields, methods and constructors
# Object instatiation

class GameCharacter:     #classes are usually camelcassed, instead of game_caracter

    speed = 5

# the self keyword refers to GameCharacter
    def __init__(self, name, width, height, x_pos, y_pos):      #this is a constructor
        self.name = name        #All of these are fields
        self.width = width          #this is a field too
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):     #this is a method
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

        # because we are working inside of GameCharacter (self) we don't need to
        # use the global keyword, cuz all the variables exist withing (self) and they are accessed within (self)

character_0 = GameCharacter("char_0", 50, 100, 100, 100)
print(character_0.name)    #this will print self.name, in this care cuz we declared that
                           #character_0 = GameCharacter(and all the parameters here) name will be the first paramenter
                           # char_0
character_0.name = "char_1"    #we can change the characters name like this
print(character_0.name)     #now it will print char_1

character_0.move(50, 100)     # here we pass the parameters to the method move
                              # it says add 50 to the x_pos, and 100, to the y_pos
print(character_0.x_pos)     
print(character_0.y_pos)
