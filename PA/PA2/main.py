import pygame
from scene import Ground

# Create an instance of the Ground class
ground = Ground()

# Run the main game loop
while ground.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ground.running = False

    # Fill the screen with a white color
    ground.screen.fill((255, 255, 255))

    # Draw and update the ground
    ground.draw()
    ground.update()

    # Update the display
    pygame.display.update()

    # Control the frame rate
    ground.clock.tick(60)

# Quit pygame and exit the program
pygame.quit()
