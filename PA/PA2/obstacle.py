import pygame
import random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, ground_speed):
        super().__init__()
        self.images = [
            pygame.image.load('resources/images/cactus/cactus-1.png'),
            pygame.image.load('resources/images/cactus/cactus-2.png'),
            pygame.image.load('resources/images/cactus/cactus-3.png'),
            pygame.image.load('resources/images/cactus/cactus-4.png'),
            pygame.image.load('resources/images/cactus/cactus-5.png'),
            pygame.image.load('resources/images/cactus/cactus-6.png')
        ]
        self.image = random.choice(self.images)  # 随机选择仙人掌图像
        self.rect = self.image.get_rect()
        self.rect.right, self.rect.bottom = 1280, 637
        self.speed = ground_speed  # 障碍物速度

    def update(self):
        self.rect.left -= self.speed
        # 重新定位仙人掌，使其循环出现在屏幕右侧
        if self.rect.right <= 0:
            self.rect.left = 1280
            self.image = random.choice(self.images)
            self.rect.bottom = 637

class ObstacleManager:
    def __init__(self):
        self.cacti = pygame.sprite.Group()

    def add_cactus(self, ground_speed):
        cactus = Cactus(ground_speed)
        self.cacti.add (cactus)

    def update(self):
        self.cacti.update()

    def draw(self, screen):
        self.cacti.draw(screen)
