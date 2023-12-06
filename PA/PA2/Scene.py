import pygame
import sys
import time


class Scene:
    class Time:
        if time == 1000:
            T = 'black'
        else:
            T = 'white'

    class Ground:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True

        # create a ground image
        ground = pygame.image.load('resources/images/ground/ground.png')
        ground_rect = ground.get_rect()
        ground_rect.left, ground_rect.bottom = 0, 650

        # create a second ground image for continuous scrolling
        ground2 = pygame.image.load('resources/images/ground/ground.png')
        ground2_rect = ground2.get_rect()
        ground2_rect.left, ground2_rect.bottom = ground_rect.width, 650

        # game loop
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a white color
            screen.fill((255, 255, 255))

            # put both ground images on the screen
            screen.blit(ground, ground_rect)
            screen.blit(ground2, ground2_rect)

            # move both ground images
            ground_rect.left -= 8
            ground2_rect.left -= 8

            # check if either ground image is completely off the screen, then reset its position
            if ground_rect.right < 0:
                ground_rect.left = ground2_rect.right

            if ground2_rect.right < 0:
                ground2_rect.left = ground_rect.right

            # update the display
            pygame.display.update()

            # limit FPS to 60
            clock.tick(60)

        pygame.quit()
        sys.exit()
        pass

    class Moon:
        pass

    class Cloud:
        pass

    class Star:
        pass

    class Scoreboard:
        pass

    class Endinglcon:
        pass
