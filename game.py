import pygame
import time
import random

pygame.init()

# Set up display
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (169, 169, 169)

# Game variables
block_size = 20
delay = 0.1
score = 0
high_score = 0

# Font
font = pygame.font.SysFont("Courier", 24)

# Snake
snake = [(300, 300)]
direction = "STOP"

# Food
food = (random.randint(0, (width - block_size) // block_size) * block_size,
        random.randint(0, (height - block_size) // block_size) * block_size)

# Functions
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(win, white, (*segment, block_size, block_size))

def draw_food(food):
    pygame.draw.rect(win, red, (*food, block_size, block_size))

def move_snake(snake, direction):
    x, y = snake[0]
    if direction == "UP":
        y -= block_size
    elif direction == "DOWN":
        y += block_size
    elif direction == "LEFT":
        x -= block_size
    elif direction == "RIGHT":
        x += block_size
    new_head = (x, y)
    snake.insert(0, new_head)
    return snake

def check_collision(snake):
    x, y = snake[0]
    if x < 0 or x >= width or y < 0 or y >= height:
        return True
    if snake[0] in snake[1:]:
        return True
    return False

def display_score(score, high_score):
    text = font.render(f"Score: {score}  High Score: {high_score}", True, white)
    win.blit(text, [0, 0])

# Main game loop
running = True
while running:
    win.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_s and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_a and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_d and direction != "LEFT":
                direction = "RIGHT"

    if direction != "STOP":
        snake = move_snake(snake, direction)
        if check_collision(snake):
            time.sleep(1)
            snake = [(300, 300)]
            direction = "STOP"
            score = 0
            delay = 0.1

    if len(snake) > 0 and snake[0] == food:
        food = (random.randint(0, (width - block_size) // block_size) * block_size,
                random.randint(0, (height - block_size) // block_size) * block_size)
        score += 10
        if score > high_score:
            high_score = score
        delay -= 0.001
    elif len(snake) > 0:
        snake.pop()

    draw_snake(snake)
    draw_food(food)
    display_score(score, high_score)
    pygame.display.update()
    time.sleep(delay)

pygame.quit()
