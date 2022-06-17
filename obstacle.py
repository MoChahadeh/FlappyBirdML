import pygame
from random import randint
import os


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, *groups, initX) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(initX, randint(180, 250))
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, 40, 375-self.pos.y)
        self.upperRect = pygame.rect.Rect(self.pos.x, 0, 40, self.pos.y-randint(80,160))
        self.openingPos = pygame.Vector2(self.pos.x, (self.rect.top+self.upperRect.bottom)/2)
        self.color = (70,255,100)
        self.dead = False
    
    def draw(self, WINDOW: pygame.Surface):
        pygame.draw.rect(WINDOW, self.color, self.rect)
        pygame.draw.rect(WINDOW, self.color, self.upperRect)

    def update(self, WINDOW, speed):

        if not self.dead:
            self.pos.x -= speed
            self.rect.x= self.pos.x
            self.upperRect.x = self.pos.x
            self.openingPos.x = self.pos.x
            self.draw(WINDOW)

            if(self.pos.x < -30):
                self.dead = True
                self.kill()