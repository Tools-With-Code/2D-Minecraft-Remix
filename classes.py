import pygame
import math

pygame.init()

class Block:
    BLOCK_WIDTH_HEIGHT = 40
    def __init__(self, x, y, blockImg):
        self.x = x
        self.y = y
        self.blockImg = pygame.transform.scale(blockImg, (self.BLOCK_WIDTH_HEIGHT, self.BLOCK_WIDTH_HEIGHT))

    def Draw(self, display):
        display.blit(self.blockImg, (self.x, self.y))

class Player:
    VEL = 5
    JUMP_HEIGHT = math.sqrt(40)
    NGTV_JUMP_HEIGHT = 0 - JUMP_HEIGHT
    def __init__(self, x, y):
        self.jump = False
        self.x = x
        self.y = y
        self.color = (255, 255, 255)

    def Draw(self, display):
        pygame.draw.rect(display, self.color, (self.x, self.y, 40, 80))

    def Move(self, keys):
        if not self.jump:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.x -= self.VEL
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.x += self.VEL
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.JUMP_HEIGHT >= self.NGTV_JUMP_HEIGHT:
                neg = 1
                if self.JUMP_HEIGHT < 0:
                    neg = -1
                self.y -= (self.JUMP_HEIGHT ** 2) * neg
                self.JUMP_HEIGHT -= 1
            else:
                self.jump = False
                self.JUMP_HEIGHT = math.sqrt(40)