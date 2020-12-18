import pygame
from ..constants import *

pygame.init()

def Main():
    while True:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        pygame.display.update()
        DISPLAY = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption("2D Minecraft Remix")