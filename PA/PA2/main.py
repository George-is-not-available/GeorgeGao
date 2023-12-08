import pygame
import sys
import random
from dinosaur import Dinosaur
from obstacle import Cactus
from scene import Ground, Moon, Cloud, Star, Scoreboard, EndingIcon

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Game")

    # Create instances of the classes
    ground = Ground()
    dinosaur = Dinosaur()
    moon = Moon()
    clouds = [Cloud(random.randint(0, 1280), random.randint(50, 200), ground.ground_speed) for _ in range(3)]
    stars = [Star(random.randint(0, 1280), random.randint(50, 400), ground.ground_speed) for _ in range(5)]
    scoreboard = Scoreboard()
    ending_icon = EndingIcon()

    # Create a sprite group for cacti
    cacti = pygame.sprite.Group()

    # Main game loop
    while ground.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ground.running = False

        # Handle key events for the dinosaur (jump, crouch, etc.)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dinosaur.jump()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            dinosaur.crouch()
        else:
            dinosaur.stand_up_()

        # Add new cacti to the group
        if random.randint(0, 100) < 5:
            cacti.add(Cactus(ground.ground_rect.right))

        # Update and draw cacti
        cacti.update()

        # Fill the screen with a white color
        screen.fill((255, 255, 255))

        # Draw and update the ground
        ground.update()
        ground.draw(screen)

        # Draw other elements
        moon.draw(screen)
        for cloud in clouds:
            cloud.draw(screen)
        for star in stars:
            star.draw(screen)

        # Draw dinosaur
        dinosaur.update()
        dinosaur.draw(screen)

        # Update and draw scoreboard
        scoreboard.get_score(ground)  # Get the score from the ground
        scoreboard.update()
        scoreboard.draw(screen)

        # Draw ending icon if the game is over
        if not ground.running:
            ending_icon.draw(screen)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        ground.clock.tick(60)

    # Quit pygame and exit the program
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
