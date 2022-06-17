from psutil import WINDOWS
import pygame
import os


class Bird(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.pos = pygame.Vector2(250, 180)
        self.spd = pygame.Vector2(0,0)
        self.accel = pygame.Vector2(0, 0.5)
        self.image = pygame.image.load(os.path.join("images","bird.png"))
        self.dim = pygame.Vector2(35,28)
        self.sprite = pygame.transform.scale(self.image, (self.dim.x, self.dim.y))
    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.sprite, (self.pos.x, self.pos.y))
    def update(self, WINDOW):

        self.spd += self.accel
        self.pos += self.spd

        self.draw(WINDOW)
    def jump(self):
        self.spd.y = -10