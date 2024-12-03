import pygame
import time
import random

pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
blue = (50, 153, 213)
green = (0, 255, 0)  # Color for the head
yellow = (255, 255, 0)  # Color for the tail

# Screen dimensions
width = 800
height = 600

# Snake block size
block_size = 20

# Frames per second
FPS = 60

# Initialize the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling the game speed
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)

# Function to draw the snake
def snake(snake_list):
    for index, x in enumerate(snake_list):
        if index == 0:
            pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])  # Head
        elif index == len(snake_list) - 1:
            pygame.draw.rect(screen, yellow, [x[0], x[1], block_size, block_size])  # Tail
        else:
            pygame.draw.rect(screen, red, [x[0], x[1], block_size, block_size])  # Body

# Function to display the score
def display_score(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Initial position of the food
    foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, height - block_size) / block_size) * block_size

    score = 0

    while not game_over:
        while game_close:
            screen.fill(black)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(message, [width / 6, height / 3])
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.circle(screen, blue, [foodx + block_size // 2, foody + block_size // 2], block_size // 2)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        snake(snake_list)
        display_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, height - block_size) / block_size) * block_size
            length_of_snake += 1
            score += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
