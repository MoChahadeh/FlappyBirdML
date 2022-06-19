import pygame

#   Window size
WIDTH, HEIGHT = 750, 375
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FlappyBirdML")

#   Frame per second
FPS = 60
CLOCK = pygame.time.Clock()

#   initalizing Text Engine
pygame.font.init()
writer = pygame.font.SysFont("Roboto", 20)

#   Pygame Groups for obstacles and birds
obstacles = pygame.sprite.Group()
birds = pygame.sprite.Group()

#   Settings for gameplay, population, speed, and number of current generation
obsSpeed = 2
genNumber = 1
genPopulation = 10


#   State variables that get reset at the start every generation
nets: list[NeuralNet] = []
fitness:list[int] = []
dead = [False] * genPopulation