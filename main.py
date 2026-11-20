import pygame
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from shot import Shot
import sys

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(
        f"Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0.0
    chara = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    threat = AsteroidField()
    while True:
        log_state()
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if chara.collides_with(a) == True:
                log_event("player_hit")
                print ("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(a):
                    log_event("asteroid_shot")
                    bullet.kill()
                    a.split()
            else:
                pass
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
if __name__ == "__main__":
    main()
