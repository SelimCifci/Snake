import pygame
import random
from vector import Vector2

class Apple:
    def __init__(self, screen, block_size):
        self.block_size = block_size
        self.screen = screen
        self.margin = block_size / 10
        self.size = self.block_size - self.margin * 2

        self.position = Vector2(0, 0)

        self.spawn()

    def spawn(self):
        self.position.x = random.randint(
            0, self.screen.get_width() // self.block_size - 1
        )
        self.position.y = random.randint(
            0, self.screen.get_height() // self.block_size - 1
        )

    def draw(self):
        rect = pygame.Rect(
            self.position.x * self.block_size + self.margin,
            self.position.y * self.block_size + self.margin,
            self.size,
            self.size,
        )
        pygame.draw.rect(self.screen, (135, 157, 98), rect)
