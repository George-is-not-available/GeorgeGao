# main.py

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# create a ground image
ground = pygame.image.load('resources/images/ground/ground.png')
rect = ground.get_rect()
rect.left, rect.bottom = 0, 650

# game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # put ground on screen
    screen.blit(ground, rect)

    # move ground
    rect.left -= 8

    if rect.right < 0:
        rect.left = 4

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(100)

pygame.quit()
