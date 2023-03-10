# Since we'll use the PyGame game engine, import the library
import pygame

# Before you can do much with pygame, you will need to initialize it
pygame.init()

# Let's create a game with a display size of 288 x 512 pixels
SCREENWIDTH = 288
SCREENHEIGHT = 512
# and create a list that contains the width and height
z = [SCREENWIDTH, SCREENHEIGHT]

# Create a tuple that represents the color white
white = (255, 255, 255)

global SCREEN

# Create a PyGame window and set a variable that points to it
SCREEN = pygame.display

# Set the caption for the game to be FlapPyBird Basic
SCREEN.set_caption('FlapPyBird Basic')
# Set the size of the window
surface = SCREEN.set_mode(z)

# Choose the image to display (but don't display it)
image = pygame.image.load('background-day.png')

window = True

# Show the window until the player dismisses it
while window:
    # Check to see if the player dismissed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The player has dismissed the window
            window = False

    # Display white on screen but not image, yet
    surface.fill(white)

    # Now, we layer the image onto the window - it's called blitting
    surface.blit(image, (0, 0))
    # Show the current window
    SCREEN.update()

pygame.quit()