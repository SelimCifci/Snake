import pygame
import random

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Snake:
    def __init__(self, start_blocks, block_size, screen):
        self.block_size = block_size
        self.screen = screen
        self.margin = block_size / 10
        self.size = self.block_size - self.margin*2

        self.blocks = []
        self.grow = False
        self.direction = Vector2(1,0)
        self.old_direction = Vector2(1,0)
        self.position = Vector2(1,0)

        for i in range(start_blocks):
            self.blocks.append(Vector2(0, i))

    def move(self):
        self.position = Vector2(self.blocks[0].x + self.direction.x, self.blocks[0].y + self.direction.y)

        self.blocks.insert(0, self.position)
        if not self.grow:
            self.blocks.pop(-1)
        else:
            self.grow = False

    def draw(self):
        for block in self.blocks:
            rect = pygame.Rect(block.x*self.block_size+self.margin, block.y*self.block_size+self.margin, self.size, self.size)
            pygame.draw.rect(self.screen, (85, 107, 48), rect, 0)

class Apple:
    def __init__(self, block_size, screen):
        self.block_size = block_size
        self.screen = screen
        self.margin = block_size / 10
        self.size = self.block_size - self.margin*2

        self.position = Vector2(0,0)

        self.spawn()

    def spawn(self):
        self.position.x = random.randint(0, self.screen.get_width() // self.block_size - 1)
        self.position.y = random.randint(0, self.screen.get_height() // self.block_size - 1)

    def draw(self):
        rect = pygame.Rect(self.position.x*self.block_size+self.margin, self.position.y*self.block_size+self.margin, self.size, self.size)
        pygame.draw.rect(self.screen, (135, 157, 98), rect)

def main():
    background_color = (20,46,16)
    width, height = 480, 480

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake')

    block_pixels = 30

    snake = Snake(3, block_pixels, screen)
    apple = Apple(block_pixels, screen)

    running = True
    while running:
        screen.fill(background_color)

        clock.tick(4)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            if snake.old_direction.x != 1:
                                snake.direction.x = -1
                                snake.direction.y = 0
                        case pygame.K_RIGHT:
                            if snake.old_direction.x != -1:
                                snake.direction.x = 1
                                snake.direction.y = 0
                        case pygame.K_DOWN:
                            if snake.old_direction.y != -1:
                                snake.direction.x = 0
                                snake.direction.y = 1
                        case pygame.K_UP:
                            if snake.old_direction.y != 1:
                                snake.direction.x = 0
                                snake.direction.y = -1

        snake.move()

        if snake.position.__eq__(apple.position):
            snake.grow = True
            apple.spawn()

        for block in snake.blocks[1:-1]:
            if snake.blocks[0].__eq__(block):
                running = False

        snake.draw()
        apple.draw()

        snake.old_direction = Vector2(snake.direction.x, snake.direction.y)

        pygame.display.flip()

if __name__ == "__main__":
    main()
