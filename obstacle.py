import pygame
import os


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        self.pos = pygame.Vector2(250, 200)
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, 40, 100)
    
    def draw(self, WINDOW: pygame.Surface):
        pygame.draw.rect(WINDOW, (255,255,255), self.rect)
        pass

    def update(self):
        pass