# this allows us to run the code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle events (makes close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with black
        screen.fill("black")

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
