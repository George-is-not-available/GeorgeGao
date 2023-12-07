# pygame setup
import threading
import pygame
import sys
import time


class Ground:
    class Ground:
        def __init__(self):
            # pygame setup
            pygame.init()
            self.screen = pygame.display.set_mode((1280, 720))
            self.clock = pygame.time.Clock()
            self.running = True

            # create a ground image
            self.ground = pygame.image.load('resources/images/ground/ground.png')
            self.ground_rect = self.ground.get_rect()
            self.ground_rect.left, self.ground_rect.bottom = 0, 650

            # create a second ground image for continuous scrolling
            self.ground2 = pygame.image.load('resources/images/ground/ground.png')
            self.ground2_rect = self.ground2.get_rect()
            self.ground2_rect.left, self.ground2_rect.bottom = self.ground_rect.width, 650

        def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                # fill the screen with a white color
                self.screen.fill('white')

                # put both ground images on the screen
                self.screen.blit(self.ground, self.ground_rect)
                self.screen.blit(self.ground2, self.ground2_rect)

                # move both ground images
                self.ground_rect.left -= 8
                self.ground2_rect.left -= 8

                # check if either ground image is completely off the screen, then reset its position
                if self.ground_rect.right < 0:
                    self.ground_rect.left = self.ground2_rect.right

                if self.ground2_rect.right < 0:
                    self.ground2_rect.left = self.ground_rect.right

                # update the display
                pygame.display.update()

                # limit FPS to 60
                self.clock.tick(60)

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
