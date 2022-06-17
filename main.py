from pip import main
import pygame
from bird import *

WIDTH, HEIGHT = 750, 375
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

pygame.display.set_caption("FlappyBirdML")


def mainLoop():

    running = True
    bird = Bird()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bird.draw(WINDOW)
        pygame.display.update()
        CLOCK.tick(FPS)
    

if __name__ == "__main__":
    mainLoop()