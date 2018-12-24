# Python language basics 6
# Functions
# Implementing, calling, parameters, return values

x_pos = 0     # global variable
y_pos = 2
e_x_pos = 4
def move():   # brackets are for parameters
    global x_pos   # if you don't write global, x_pos can't be referenced inside of the function
                   # instead it will just create a new x_pos variable that only exists inside move()
    x_pos += 2 # local variable

move()   # we execute the function
print(x_pos)
    


def moveMore(amount):
    global y_pos
    y_pos += amount

moveMore(3)    # need to pass a value for amount
print(y_pos)

    
def checkForCollision():
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False
did_collide = checkForCollision()
print(did_collide)
