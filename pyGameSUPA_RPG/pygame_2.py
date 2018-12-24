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


# This loads the image from the folder it is in and transforms it by increasing its size
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))




# We are going to create a clock that makes the game run at a certain speed
# Typical rate of 60 = 60 FPS

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
# THESE COMMANDS CAN BE USED TO DRAW CIRCLES AND RECTANGLES ON THE SCREEN
# GIVING THE (LOCATION, COLOR, [X_POSITION, Y_POSITION, HEIGHT, WIDTH])
    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

    game_screen.blit(player_image, (350, 350))  
    pygame.display.update()
    clock.tick(TICK_RATE)
    
pygame.quit()
quit()
