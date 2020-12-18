import pygame
import os
from classes import *
from constants import *

pygame.init()

DISPLAY = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("2D Minecraft Remix")

BLACK = (0, 0, 0)

def Main():
    FPS = 60
    clock = pygame.time.Clock()
    dirt = Block(WIDTH // 2, HEIGHT // 2, pygame.image.load(os.path.join("images", "dirt.png")))
    grass = Block(500, 500, pygame.image.load(os.path.join("images", "grass.png")))
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)
        dirt.Draw(DISPLAY)
        grass.Draw(DISPLAY)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.update()

Main()