import pygame
import os
from classes import *
from constants import *

pygame.init()

DISPLAY = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("2D Minecraft Remix")

BLACK = (0, 0, 0)

STDFONT = pygame.font.SysFont("comicsans", 100)

DIRT_IMG = pygame.image.load(os.path.join("images", "dirt.png"))
GRASS_IMG = pygame.image.load(os.path.join("images", "grass.png"))

def Main():
    FPS = 60
    clock = pygame.time.Clock()
    y1 = []
    for i in range(WIDTH // 40):
        dirt = Block(40 * i, HEIGHT - 40, DIRT_IMG)
        y1.append(dirt)
    player = Player(WIDTH // 2, HEIGHT - 120)

    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)

        for block in y1:
            block.Draw(DISPLAY)
        
        player.Draw(DISPLAY)
        player.Move(keys, WIDTH, HEIGHT)
        if player.dead:
            player.Die(DISPLAY, STDFONT, WIDTH, HEIGHT)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.display.update()

Main()