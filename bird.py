import pygame
import os


class Bird(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.pos = pygame.Vector2(250, 180)
        self.speed = pygame.Vector2(0,0)
        self.gravity = pygame.Vector2(0, 1)
        self.image = pygame.image.load(os.path.join("images","bird.png"))
    
    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.image, (self.pos.x, self.pos.y))
