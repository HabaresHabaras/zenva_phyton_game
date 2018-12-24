# Subclasses and Superclasses


class GameCharacter:     #classes are usually camelcassed, instead of game_caracter

    speed = 5

# the self keyword refers to GameCharacter
    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name        
        self.width = width      
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):    
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

class PlayerCharacter(GameCharacter):

    def __init__(self, name, width, height, x_pos, y_pos):
        super().__init__(name, width, height, x_pos, y_pos)
        
    def move(self, by_y_amount):     # Method overriding
        super().move(0, by_y_amount)

player_character = PlayerCharacter("P_character", 100, 100, 500, 500)
print(player_character.name)        
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)
