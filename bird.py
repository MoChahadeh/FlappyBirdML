#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

#   Libraries and classes
import pygame
import os
from settings import *


# Bird Class
class Bird(pygame.sprite.Sprite):

    # class constructor
    def __init__(self, *groups, index):
        super().__init__(*groups)   # superclass constructor
        self.index = index  # index of bird in the Birds sprite group
        self.pos = pygame.Vector2(20, 180)  # initalize position of bird as vector X,Y
        self.spd = pygame.Vector2(0,0)  # initial speed of bird
        self.accel = pygame.Vector2(0, 0.5) # default acceleration of bird, 0 on x, 0.5 on y (Gravity)
        self.image = pygame.image.load(os.path.join("images","bird.png"))   # loading bird image
        self.dim = pygame.Vector2(30,24)    # width and height for the bird sprite
        self.sprite = pygame.transform.scale(self.image, (self.dim.x, self.dim.y))  # scaling the sprite image to the desired dimensions
        self.rect = self.sprite.get_rect()  # rectangle (hitbox) of the sprite
        self.dead = False   # death state of bird
        self.jumpingSpeed = -6  # strength of jump, minus is up..

    def draw(self):
        WINDOW.blit(self.sprite, (self.pos.x, self.pos.y))  # Drawing the sprite on the pygame WINDOW
    
    def update(self):   # update method for bird, called each frame through the group's update method..

        if not self.dead:
            self.spd += self.accel  # increasing the speed by the acceleration (Applying gravity in this case..)
            self.pos += self.spd    # increasing the position by the speed

            if self.pos.y <= 0: self.pos.y = 0  # upper constraint for birds, cannot go above the window 
            if self.pos.y > HEIGHT+50: self.dead = True   # lower contraint for birds, cannot go lower than 50px under the screen

            self.sprite = pygame.transform.rotate(pygame.transform.scale(self.image, (self.dim.x, self.dim.y)), -self.spd.y)    # rotating the bird with the Y speed, making that cool flying effect
            self.rect = self.sprite.get_rect()  # refreshing the rect of the sprite
            self.draw()   # drawing method defined above..
    
    def jump(self):
        self.spd.y = self.jumpingSpeed  # adds jumping speed to spd.y

    def checkCollision(self):   #collision checker for bird
        # Checks for collisions with every obstacles
        # collision logic can be better but it works for now..
        for obs in obstacles:
             
            if(self.pos.x + self.dim.x > obs.rect.left and self.pos.x < obs.rect.right) and (self.pos.y < obs.rect.bottom and self.pos.y+self.dim.y > obs.rect.top):
                print("lower col")
                self.dead = True
            if(self.pos.x+ self.dim.x > obs.upperRect.left and self.pos.x < obs.upperRect.right) and (self.pos.y < obs.upperRect.bottom and self.pos.y+self.dim.y > obs.upperRect.top):
                print("upper col")
                self.dead = True