import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FPSClock
    clock = pygame.time.Clock()
    dt = 0 #delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # Fill the screen with black
        pygame.display.flip() # Update the screen

        dt = clock.tick(60) / 1000 # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    main()