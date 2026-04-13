import pygame
from vector import Vector2
from snake import Snake
from food import Apple

def main():
    pygame.init()
    pygame.mouse.set_visible(False)

    background_color = (20, 46, 16)
    width, height = 480, 480

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height), pygame.SCALED)
    pygame.display.set_caption("Snake")

    block_pixels = 15

    snake = Snake(screen, block_pixels, 3, (width, height))
    apple = Apple(screen, block_pixels)

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
