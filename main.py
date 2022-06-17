#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import pygame
import numpy as np
from copy import deepcopy
from neuralnet import NeuralNet
from bird import *
from obstacle import *

WIDTH, HEIGHT = 750, 375
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FlappyBirdML")

FPS = 60
CLOCK = pygame.time.Clock()

pygame.font.init()
writer = pygame.font.SysFont("Roboto", 20)

obstacles = pygame.sprite.Group()
birds = pygame.sprite.Group()

obsSpeed = 2
genNumber = 1
genPopulation = 10
nets: list[NeuralNet] = []
fitness:list[int] = []
dead = [False] * genPopulation

for i in range(genPopulation):
    nets.append(NeuralNet(2, 5, 1))
    fitness.append(0)
    birds.add(Bird(index = i))


def drawLabels():
    genText = writer.render("Generation "+str(genNumber), True, (255,255,255))
    aliveText = writer.render("Alive: " + str(sum(map(lambda x : x ==False, dead))), True, (255,255,255))
    bestFitness = writer.render("Best Fitness: " + str(max(fitness)), True, (255,255,255))

    WINDOW.blit(bestFitness, (10,50))
    WINDOW.blit(aliveText, (10,30))
    WINDOW.blit(genText, (10,10))

def mainLoop():
    global dead
    numOfObs = 0
    running = True
    while running:
        WINDOW.fill((100,130,200))
        obstacles.add(Obstacle(initX = 750 + (150*len(obstacles.sprites()))))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dead = [True] * genPopulation

        for currentBird in birds.sprites():
            if not currentBird.dead:
                inputs = [obstacles.sprites()[0].openingPos.x - currentBird.pos.x, obstacles.sprites()[0].openingPos.y - currentBird.pos.y]
                decision = nets[currentBird.index].forward([inputs])

                if(decision > 0.5): currentBird.jump()

                currentBird.checkCollision(obstacles)
                fitness[currentBird.index] += 1
            else:
                dead[currentBird.index] = True

        if(all(d == True for d in dead)): 
            print(fitness)
            restartAndMutate()
            

        obstacles.update(WINDOW, obsSpeed)
        birds.update(WINDOW)
        drawLabels()
        pygame.display.update()
        CLOCK.tick(FPS)


def restartAndMutate():
    global genNumber
    genNumber += 1
    maximums = np.flip(np.argsort(fitness))
    fitness.clear()
    dead.clear()
    for obs in obstacles: obs.kill()
    for bird in birds: bird.kill()
    for i in range(genPopulation):
        fitness.append(0)
        birds.add(Bird(index = i))
        dead.append(False)
        nets[i] = deepcopy(nets[maximums[i%3]])
        nets[i].mutate(0.15)


    

if __name__ == "__main__":
    mainLoop()