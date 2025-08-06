# this allows us to run the code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *



def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Initialize pygame
    pygame.init()

    # Create Game clock
    clock = pygame.time.Clock()

    # dt variable set to 0
    dt = 0

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)


    # game groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)


    # Game loop
    while True:
        # Handle events (makes close button work)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Calculate delta time
        dt = clock.tick(60)/1000

        # Fill screen with black
        screen.fill("black")

        # Draw Player every frame
        drawable.draw(screen)

        # update player movement
        updateable.update(dt)

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
