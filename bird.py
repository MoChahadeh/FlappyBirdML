#   June 17th, 2022, 4:14AM Friday
#   Mohamad Chahadeh, ©2022
#   https://MoChahadeh.github.io/
#   https://twitter.com/MoChahadeh

import pygame
import os
from obstacle import Obstacle


class Bird(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.pos = pygame.Vector2(250, 180)
        self.spd = pygame.Vector2(0,0)
        self.accel = pygame.Vector2(0, 0.5)
        self.image = pygame.image.load(os.path.join("images","bird.png"))
        self.dim = pygame.Vector2(30,24)
        self.sprite = pygame.transform.scale(self.image, (self.dim.x, self.dim.y))
        self.rect = self.sprite.get_rect()
        self.dead = False
        self.jumpingSpeed = -6
        self.i = 0

    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.sprite, (self.pos.x, self.pos.y))
    
    def update(self, WINDOW):
        self.spd += self.accel
        self.pos += self.spd
        self.sprite = pygame.transform.rotate(pygame.transform.scale(self.image, (self.dim.x, self.dim.y)), -self.spd.y)
        self.rect = self.sprite.get_rect()

        self.draw(WINDOW)
    
    def jump(self):
        self.spd.y = self.jumpingSpeed

    def checkCollision(self, obstacles: pygame.sprite.Group):
        

        for obs in obstacles:
            if (self.pos.x + self.dim.x <= obs.rect.right) and (self.pos.x + self.dim.x >= obs.rect.left) and (self.pos.y + self.dim.y >= obs.rect.top) and (self.pos.y + self.dim.y <= obs.rect.bottom):
                self.dead = True
            elif (self.pos.x + self.dim.x <= obs.upperRect.right) and (self.pos.x + self.dim.x >= obs.upperRect.left) and (self.pos.y >= obs.upperRect.top) and (self.pos.y <= obs.upperRect.bottom):
                self.dead = True        
