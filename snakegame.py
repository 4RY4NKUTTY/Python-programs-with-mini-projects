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
block_size = 10

# Speed of the snake
speed = 30

# Initialize the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling the speed of the game
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)

def snake(block_size, snake_list):
    for index, x in enumerate(snake_list):
        if index == 0:
            # Draw the head
            pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])
        elif index == len(snake_list) - 1:
            # Draw the tail
            pygame.draw.rect(screen, yellow, [x[0], x[1], block_size, block_size])
        else:
            # Draw the rest of the body
            pygame.draw.rect(screen, red, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def display_score(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

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
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
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
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.circle(screen, blue, [int(foodx + block_size / 2), int(foody + block_size / 2)], int(block_size / 2))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(block_size, snake_list)
        display_score(score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1
            score += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()
