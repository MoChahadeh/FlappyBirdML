#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import pygame
from bird import *
from obstacle import *

WIDTH, HEIGHT = 750, 375
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FlappyBirdML")

FPS = 60
CLOCK = pygame.time.Clock()

pygame.font.init()
writer = pygame.font.SysFont("Roboto", 20)

bird = Bird()
obstacle = Obstacle()

obsSpeed = 2

genNumber = 1


def drawLabels():
    genText = writer.render("Generation "+str(genNumber), True, (255,255,255))
    WINDOW.blit(genText, (10,10))
    pass

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

        obstacle.update(WINDOW, obsSpeed)
        bird.update(WINDOW)
        drawLabels()
        bird.checkCollision([obstacle])
        pygame.display.update()
        CLOCK.tick(FPS)
    

if __name__ == "__main__":
    mainLoop()