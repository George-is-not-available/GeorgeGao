# dinosaur.py

import pygame


class Dinosaur:
    def __init__(self):
        self.images = (
            pygame.image.load('resources/images/dinosaur/dinosaur-run-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-run-2.png')
        )
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 0, 640
        self.frame = 0

    def switch_image(self):
        if self.frame % 10 == 0:
            if self.image == self.images[0]:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
        self.frame += 1

    def update(self):
        self.switch_image()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
