import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPSClock
    clock = pygame.time.Clock()
    dt = 0 # delta time

# Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # All player objects after this change!
    Asteroid.containers = (asteroids, updatable, drawable) # All asteroid objects after this change!
    AsteroidField.containers = (updatable)
    asteroid_object = AsteroidField()

# Player Variables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black") # Fill the screen with black
        for item in drawable:
            item.draw(screen)
        pygame.display.flip() # Update the screen

        dt = clock.tick(60) / 1000 # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()