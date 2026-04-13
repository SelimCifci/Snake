import pygame
from vector import Vector2

class Snake:
    def __init__(self, screen: pygame.Surface, pixels: int, start_blocks: int, scr_size: tuple[int, int]):
        self.screen = screen
        self.pixels = pixels

        self.margin = self.pixels / 10
        self.field_size = (scr_size[0] / self.pixels, scr_size[1] / self.pixels)
        self.block_pixels = self.pixels - self.margin*2

        self.direction = Vector2(1, 0)
        self.old_direction = Vector2(1, 0)
        self.position = Vector2(1, 0)
        self.grow = False

        self.blocks = []
        for i in range(start_blocks):
            self.blocks.append(Vector2(0, i))

    def move(self):
        self.position = Vector2(
            (self.blocks[0].x + self.direction.x) % self.field_size[0],
            (self.blocks[0].y + self.direction.y) % self.field_size[1]
        )

        self.blocks.insert(0, self.position)
        if not self.grow:
            self.blocks.pop(-1)
        else:
            self.grow = False

    def draw(self):
        for block in self.blocks:
            rect = pygame.Rect(
                block.x * self.pixels + self.margin,
                block.y * self.pixels + self.margin,
                self.block_pixels,
                self.block_pixels,
            )
            pygame.draw.rect(self.screen, (85, 107, 48), rect, 0)
