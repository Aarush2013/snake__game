import pygame
import sys
import random
import time
pygame.init()
screen_width = 1290
screen_height = 737
running=True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")
background_color = ('black')
play_button=pygame.Rect(545,268.5,200,50)
exit_button=pygame.Rect(545,268.5+80,200,50)

def snake_game():
    block_size = 20
    snake = [(100, 100)]

    # snake[0][0]
    # snake[0][1]

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Basics")

    background_color = pygame.Color('black')

    direction = (block_size, 0)

    clock = pygame.time.Clock()

    food = (random.randint(0, screen_width // block_size - 1) * block_size,
            random.randint(0, screen_height // block_size - 1) * block_size)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = (-block_size, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (block_size, 0)
                elif event.key == pygame.K_DOWN:
                    direction = (0, block_size)
                elif event.key == pygame.K_UP:
                    direction = (0, -block_size)

        screen.fill(background_color)

        new_pos = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (new_pos in snake or new_pos[0] < 0 or new_pos[0] >= screen_width or new_pos[1] < 0 or new_pos[
            1] >= screen_height):
            running = False

        # snake[0]=new_pos
        snake.insert(0, new_pos)
        if new_pos == food:
            food = (random.randint(0, screen_width // block_size - 1) * block_size,
                    random.randint(0, screen_height // block_size - 1) * block_size)

        else:
            snake.pop()

        # pygame.draw.rect(screen,'green',(snake[0][0],snake[0][1],block_size,block_size))

        for a in snake:
            pygame.draw.rect(screen, 'green', (a[0], a[1], block_size, block_size))

        pygame.draw.rect(screen, 'red', (food[0], food[1], block_size, block_size))

        pygame.display.flip()
        clock.tick(10)

    return

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                running=False
            if play_button.collidepoint(event.pos):
                print("play button was clicked")
                snake_game()


    screen.fill(background_color)

    pygame.draw.rect(screen,'green',play_button,border_radius=20)
    pygame.draw.rect(screen,'red',exit_button,border_radius=20)
    font=pygame.font.Font(None,36)

    play_text=font.render("Play",True,'black')
    exit_text=font.render("Exit",True,'black')

    screen.blit(play_text,(play_button.x+75,play_button.y+10))
    screen.blit(exit_text, (exit_button.x+75, exit_button.y+10))

    pygame.display.flip()