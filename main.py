#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh


#   Libraries and Classes
import pygame
import numpy as np
from copy import deepcopy
from neuralnet import NeuralNet
from bird import *
from obstacle import *
from settings import *

#   initializing the state variables for the first Generation
for i in range(genPopulation):
    nets.append(NeuralNet(2, 5, 1))
    fitness.append(0)
    birds.add(Bird(index = i))
    obstacles.add(Obstacle(initX = WIDTH + (150*i)))

#   drawing text on the screen
def drawLabels():
    genText = writer.render("Generation "+str(genNumber), True, (255,255,255))  #   Generation Number Label
    aliveText = writer.render("Alive: " + str(sum(map(lambda x : x ==False, dead))), True, (255,255,255))   #   number of birds alive Label
    bestFitness = writer.render("Best Fitness: " + str(max(fitness)), True, (255,255,255))  #   Fitness of best performing Model

    #   Drawing the labels on the screen
    WINDOW.blit(bestFitness, (10,50))
    WINDOW.blit(aliveText, (10,30))
    WINDOW.blit(genText, (10,10))


# game loop
def mainLoop():
    global dead

    running = True
    while running:
        WINDOW.fill((100,130,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #   Quitting Event
                running = False
            if event.type == pygame.KEYDOWN:    # Keydown Events
                if event.key == pygame.K_SPACE: #   Space key event ends the current generation and moves on to the next
                    dead = [True] * genPopulation   #   sets the state of all birds to DEAD

        for currentBird in birds.sprites():     #   Loop for each bird
            if not currentBird.dead:    #   checks if bird is dead or not

                #   Inputs of the neural network; distance from the first obstacle on x and on y
                inputs = [obstacles.sprites()[0].openingPos.x - currentBird.pos.x, obstacles.sprites()[0].openingPos.y - currentBird.pos.y]
                
                #   feeding the neural net the input and getting its decision
                decision = nets[currentBird.index].forward([inputs])

                #   one node decision between 0 and 1, if above 0.5 then we jump otherwise no
                if(decision > 0.5): currentBird.jump()

                #   checking for collisions for current Bird, see Bird Class
                currentBird.checkCollision()

                #   adds one point of fitness in each frame the bird plays
                fitness[currentBird.index] += 1
            else:

                #   sets the bird's state in state list "dead" to True, yes it does at each iteration but not that big of deal..
                dead[currentBird.index] = True

        #   checks if all the birds are dead
        if(all(d == True for d in dead)): 
            #   prints all the fitnesses in the console
            print(fitness)
            #   resets state variable and clones and mutates the best performing neural nets
            restartAndMutate()
            

        obstacles.update()  #   calls the update method for all obstacles in group
        birds.update()    #   calls the update method for all birds in group, the death checking is done inside the bird's update method..
        drawLabels()    #   calling the label drawing method
        pygame.display.update()     #refreshed the screen with the new states
        CLOCK.tick(FPS)     #   sets the frame rate of the game


def restartAndMutate():
    global genNumber
    genNumber += 1  #   incrementing Generation Number
    maximums = np.flip(np.argsort(fitness)) #   sorts the indices of the fitnesses highest to lowest, which are the same indices for the corresponding neural nets
    fitness.clear() # resets the fitness list
    dead.clear()    # resets the dead list

    #   resetting the sprite groups:
    for obs in obstacles: obs.kill()
    for bird in birds: bird.kill()

    #   re-assigns new values to the state variables
    for i in range(genPopulation):
        fitness.append(0)
        birds.add(Bird(index = i))
        dead.append(False)
        obstacles.add(Obstacle(initX = WIDTH + (150*i)))
        # Copies one of the three best performing neurons and appends it the list of neurons
        nets[i] = deepcopy(nets[maximums[i%3]])
        # Mutates the newly assigned neural net by a random rate between -15% and +15%
        nets[i].mutate(0.15)


    
#   Starts the mainloop() but only if the main.py file is directly executed..
if __name__ == "__main__":
    mainLoop()