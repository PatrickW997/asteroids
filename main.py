# this allows us to run the code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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

    # game groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    # assign asteroid(field) class containers and create asteroid_field
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    asteroid_filed = AsteroidField()

    # assign player class containers and create player
    Player.containers = (updateable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    # assign Shot class containers
    Shot.containers = (updateable, drawable, shots)

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

        # Draw every drawable every frame
        for drawable_object in drawable:
            drawable_object.draw(screen)

        # update player movement
        updateable.update(dt)

        # check for colision
        for asteroid_object in asteroids:
            if player.collides_with(asteroid_object):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid_object.collides_with(shot):
                    shot.kill()
                    asteroid_object.kill()

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
