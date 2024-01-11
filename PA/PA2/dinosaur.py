import pygame
import random

screen = pygame.display.set_mode((1280, 720))


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = (
            pygame.image.load('resources/images/dinosaur/dinosaur-run-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-run-2.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-duck-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-duck-2.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-die-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-die-2.png')
        )
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 30, 650
        self.frame = 6  # 控制小恐龙的图片切换速度
        self.status = 'run'
        self.y = 0
        self.jump_height = [37,36,35,34,33,32,31, 30, 28, 25, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, -1, -2, -4, -6, -8, -10,
                            -12,
                            -14, -16, -18, -20, -22, -25, -28, -30, -31, -32, -33,-34,-35,-36,-37]
        self.jump_time = 0
        self.mask = pygame.mask.from_surface(self.image)

    def switch_image(self):
        if self.frame % 10 == 0:
            if self.status == 'run':
                if self.image == self.images[0]:
                    self.image = self.images[1]
                else:
                    self.image = self.images[0]
            elif self.status == 'duck':
                if self.image == self.images[2]:
                    self.image = self.images[3]
                else:
                    self.image = self.images[2]
            elif self.status == 'die':
                self.image = self.images[random.randint(4, 5)]
        self.frame += 1

    def update(self):
        self.switch_image()
        if self.status == 'jump':
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.status = 'run'
                self.jump_time = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def jump(self):
        self.status = 'jump'
        pygame.mixer.Sound('resources/audios/jump.mp3').play()
        self.image = pygame.image.load('resources/images/dinosaur/dinosaur-jump.png')

    def run(self):
        self.status = 'run'

    def duck(self):
        self.status = 'duck'
        pygame.mixer.Sound('resources/audios/die.mp3').play()

    def die(self):
        self.status = 'die'
        self.image = (pygame.image.load('resources/images/dinosaur/dinosaur-die-1.png'))
        pygame.mixer.Sound('resources/audios/die.mp3').play()

    def die_2(self):
        self.status = 'die'
        pygame.image.load('resources/images/dinosaur/dinosaur-die-2.png')
        pygame.mixer.Sound('resources/audios/die.mp3').play()
