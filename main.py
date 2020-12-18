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
    block = Block(WIDTH // 2, HEIGHT // 2, )
    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)
        block.Draw(DISPLAY)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.update()

Main()