#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

#   libraries and classes
import pygame
from random import randint
from settings import *

# Obstacle class
class Obstacle(pygame.sprite.Sprite):

    # class constructor
    def __init__(self, *groups, initX) -> None:
        super().__init__(*groups)   # superclass constructor

        self.pos = pygame.Vector2(initX, randint(int(HEIGHT/4), HEIGHT-100))     # inital position of obstacle with random y for lower rectangle
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, 40, HEIGHT-self.pos.y+100)    # lower rectangle with height spanning from pos.y to bottom of screen
        self.upperRect = pygame.rect.Rect(self.pos.x, 0, 40, self.pos.y-randint(minOpening,minOpening*2))    # upper rectange set at y=0 and spanning down to lower rect.y - a random number between 60 and 120 pixels..
        self.openingPos = pygame.Vector2(self.pos.x, (self.rect.top+self.upperRect.bottom)/2)   # getting the middle point of the opening of the obstacle, this is fed into the nerual net
        self.color = (70,255,100)   # color of obstacle, light green
        self.dead = False   # death state of obstacle
    
    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)     # drawing the lower rect
        pygame.draw.rect(WINDOW, self.color, self.upperRect)    # drawinght the upper rect

    def update(self):

        if not self.dead:   # checks if sprite is dead, might seem redundant because I'm using .kill() but guards from any errors if I change the way I update them..
            
            self.pos.x -= obsSpeed     # changing the position with the speed
            self.rect.x= self.pos.x # changing the lower rect position
            self.upperRect.x = self.pos.x   # changing the upper rect position
            self.openingPos.x = self.pos.x  # changing the opening position
            self.draw()   # drawing method define above

            if(self.pos.x < -40):   # if obstacle passes the left of the screen..
                self.dead = True    # sets dead variable to true, disabling the update method...
                obstacles.add(Obstacle(initX = obstacles.sprites()[len(obstacles.sprites())-1].pos.x + 170))
                self.kill()     # remove the obstacle from every sprite group it's in..