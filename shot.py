import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen:pygame.surface):
        pygame.draw.circle(screen,
                           color = "white",
                           center = self.position,
                           radius = self.radius,
                           width = 0)

    def update(self, dt: float):
        self.position +=(self.velocity * dt)