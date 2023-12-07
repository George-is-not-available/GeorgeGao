import pygame

from scene import Ground
from dinosaur import Dinosaur

# main.py
pygame.init()
screen = pygame.display.set_mode((1300, 740))
clock = pygame.time.Clock()
# create dinosaur
dinosaur = Dinosaur()


# Create an instance of the Ground class
ground = Ground()

# Run the main game loop
while ground.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ground.running = False

    # main.py
    # set action on key press event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ground.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        dinosaur.jump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ground.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        dinosaur.crouch()
    else:
        dinosaur.stand_up_()

    # Fill the screen with a white color
    ground.screen.fill('white')

    # Draw and update the ground
    ground.draw()
    ground.update()
    # draw dinosaur
    dinosaur.update()
    dinosaur.draw(screen)
    # Update the display
    pygame.display.update()

    # Control the frame rate
    ground.clock.tick(60)

# Quit pygame and exit the program
pygame.quit()
