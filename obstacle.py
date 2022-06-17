import pygame
import os


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
    
    def draw(self):
        pass

    def update(self):
        pass