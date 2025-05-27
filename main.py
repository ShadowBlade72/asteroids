import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPSClock
    clock = pygame.time.Clock()
    dt = 0 #delta time

#Player Variables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill("black") # Fill the screen with black
        player.draw(screen)
        pygame.display.flip() # Update the screen

        dt = clock.tick(60) / 1000 # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()