from pip import main
import pygame
from bird import *

WIDTH, HEIGHT = 750, 375
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

pygame.display.set_caption("FlappyBirdML")

bird = Bird()


def mainLoop():

    running = True
    while running:
        WINDOW.fill((100,130,200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update(WINDOW)
        pygame.display.update()
        CLOCK.tick(FPS)
    

if __name__ == "__main__":
    mainLoop()