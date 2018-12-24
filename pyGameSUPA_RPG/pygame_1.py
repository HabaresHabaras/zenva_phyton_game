# Pygame development 1
# Start the basic game set up
# Set up the display

# Import pygame as a library
import pygame

pygame.init()

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Crossy RPG"
# Colors in RGB Codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Create the window of specified size in display
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)
# We are going to create a clock that makes the game run at a certain speed

clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False


# GAME LOOP - while loop

while not is_game_over:

# event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        print(event)

    pygame.display.update()
    clock.tick(TICK_RATE)
    
pygame.quit()
quit()
