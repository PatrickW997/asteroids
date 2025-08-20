import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)

    def update(self, dt):
        super().update(dt) # calls the parent's update method
        self.position += self.velocity * dt # then adds the Asteroid-specific logic

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # creating two new asteroids on the destroyed ones position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # setting their direction and speed
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
        return asteroid1, asteroid2
