import pygame
import os


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, *groups, initX) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(initX, 200)
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, 40, 375-200)
        self.dead = False
    
    def draw(self, WINDOW: pygame.Surface):
        pygame.draw.rect(WINDOW, (70,255,100), self.rect)

    def update(self, WINDOW, speed):

        if not self.dead:
            self.pos.x -= speed
            self.rect.x, self.rect.y = self.pos.x,self.pos.y
            self.draw(WINDOW)

            if(self.pos.x < -50):
                self.dead = True
                self.kill()