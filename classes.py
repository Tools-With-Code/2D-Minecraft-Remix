import pygame

pygame.init()

class Block:
    BLOCK_WIDTH_HEIGHT = 37
    def __init__(self, x, y, blockImg):
        self.x = x
        self.y = y
        self.blockImg = pygame.transform.scale(blockImg, (self.BLOCK_WIDTH_HEIGHT, self.BLOCK_WIDTH_HEIGHT))

    def _GetCenter(self, x, y, surface):
        return (x - surface.get_width() // 2, y - surface.get_width() // 2)

    def Draw(self, display):
        display.blit(self.blockImg, self._GetCenter(self.x, self.y, self.blockImg))