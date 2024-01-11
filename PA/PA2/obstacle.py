import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = (
            pygame.image.load('resources/images/cactus/cactus-1.png'),
            pygame.image.load('resources/images/cactus/cactus-2.png'),
            pygame.image.load('resources/images/cactus/cactus-3.png'),
            pygame.image.load('resources/images/cactus/cactus-4.png'),
            pygame.image.load('resources/images/cactus/cactus-5.png'),
            pygame.image.load('resources/images/cactus/cactus-6.png')
        )
        self.image = self.images[random.randint(0, 5)]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 1280, 650
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.left -= 10
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pterosaurs(pygame.sprite.Sprite):
    def __init__(self, left_co, bottom_co):
        super().__init__()
        self.images = (
            pygame.image.load('resources/images/pterodactyl/pterodactyl-1.png'),
            pygame.image.load('resources/images/pterodactyl/pterodactyl-2.png')

        )
        self.left_co = left_co
        self.bottom_co = bottom_co
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 1350, 300
        self.frame = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.bottom = self.left_co, self.bottom_co

    def switch_image(self):
        if self.frame % 10 == 0:
            if self.image == self.images[0]:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
        self.frame += 1

    def update(self):
        self.switch_image()
        self.rect.left -= 13
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)