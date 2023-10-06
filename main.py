import pygame
import random

background_color = (20,46,16)
(width, height) = (480, 480)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

block_size_pixels = 30

direction = [1,0]

class Snake:
    def __init__(self, start_blocks, block_size):
        self.block_size = block_size

        self.blocks = []
        self.head_rect = None
        self.grow = False

        for nmb in range(start_blocks):
            self.blocks.append((0, nmb*self.block_size))

    def move(self):
        new_head = (direction[0]*self.block_size + self.blocks[0][0], direction[1]*self.block_size + self.blocks[0][1])

        self.blocks.insert(0, new_head)
        if not self.grow:
            self.blocks.pop(-1)
        else:
            self.grow = False

        self.head_rect = pygame.Rect(new_head[0], new_head[1], 30, 30)

    def draw(self):
        for snake_part in self.blocks:
            rect = pygame.Rect(snake_part[0]+3, snake_part[1]+3, 24, 24)
            pygame.draw.rect(screen, (85, 107, 48), rect, 0)

class Apple:
    def __init__(self, block_size):
        self.block_size = block_size

        self.rect = None

    def spawn(self):
        margin = self.block_size/10

        position = round(random.random()*self.block_size/2)*self.block_size
        self.rect = pygame.Rect(position+margin, position+margin, self.block_size-margin*2, self.block_size-margin*2)

    def draw(self):
        pygame.draw.rect(screen, (85, 107, 48), self.rect)

snake = Snake(3, block_size_pixels)
apple = Apple(block_size_pixels)

def logic():
    if snake.head_rect.colliderect(apple.rect):
        snake.grow = True
        apple.spawn()

    for block in snake.blocks:
        rect = pygame.Rect(block[0]+1, block[1]+1, block[0]+block_size_pixels-1, block[1]+block_size_pixels-1)
        if snake.head_rect.colliderect(rect):
            print("Collided")

def draw():
    snake.draw()
    apple.draw()

def main():
    apple.spawn()

    old_direction = direction.copy()

    snake.move()

    running = True
    while running:
        screen.fill(background_color)

        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if old_direction[0] != 1:
                        direction[0] = -1
                        direction[1] = 0
                if event.key == pygame.K_RIGHT:
                    if old_direction[0] != -1:
                        direction[0] = 1
                        direction[1] = 0
                if event.key == pygame.K_DOWN:
                    if old_direction[1] != -1:
                        direction[0] = 0
                        direction[1] = 1
                if event.key == pygame.K_UP:
                    if old_direction[1] != 1:
                        direction[0] = 0
                        direction[1] = -1

        logic()
        draw()

        old_direction = direction.copy()

        pygame.display.set_icon(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
