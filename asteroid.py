import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.surface):
        pygame.draw.circle(screen,
                           color = "white",
                           center = self.position,
                           radius = self.radius,
                           width = LINE_WIDTH)

    def update(self, dt: float):
        self.position +=(self.velocity * dt)

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            split_asteriod_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            split_asteriod_1.velocity = (self.velocity.rotate(angle) * 1.2)
            split_asteriod_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            split_asteriod_2.velocity = (self.velocity.rotate(-angle) * 1.2)