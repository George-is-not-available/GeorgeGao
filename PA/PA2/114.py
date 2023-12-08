import pygame
import sys
import random


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.color_reversed = False  # 添加颜色反转标志
        self.start_time = pygame.time.get_ticks()  # 记录游戏开始的时间

        self.ground = pygame.image.load('resources/images/ground/ground.png')
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.left, self.ground_rect.bottom = 0, 650

        self.ground2 = pygame.image.load('resources/images/ground/ground.png')
        self.ground2_rect = self.ground2.get_rect()
        self.ground2_rect.left, self.ground2_rect.bottom = self.ground_rect.width, 650

        self.ground_speed = 8  # 地面速度


class Moon(pygame.sprite.Sprite):
    class Moon(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.running = None
            self.image = pygame.image.load('resources/images/moon/moon-1.png')
            self.rect = self.image.get_rect()
            self.rect.center = (100, 100)

        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def switch_to_sun(self):
            self.image = pygame.image.load('resources/images/sun/sun-1.png')


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_speed):
        super().__init__()
        self.image = pygame.image.load('resources/images/cloud/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = ground_speed  # 与地面同步的速度

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_speed):
        super().__init__()
        self.image = pygame.image.load('resources/images/star/star-2.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = ground_speed  # 与地面同步的速度

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)


class EndingIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/ending/game-over.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)


if __name__ == "__main__":
    game = Ground()
    moon = Moon()
    clouds = [Cloud(random.randint(0, 1280), random.randint(50, 200), game.ground_speed) for _ in range(3)]
    stars = [Star(random.randint(0, 1280), random.randint(50, 400), game.ground_speed) for _ in range(5)]
    game.run()
