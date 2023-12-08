# moon.py
import pygame
import random


class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/moon/moon-2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 1000, 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# cloud.py
import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('resources/images/cloud/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 0:
            self.rect.left = 1280


# star.py
import pygame


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('resources/images/star/star-2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 0:
            self.rect.left = 1280


# scoreboard.py
import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def update(self):
        pass

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))


# endingicon.py
import pygame


class EndingIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/ending/game-over.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, ground_speed):
        super().__init__()
        self.images = [
            pygame.image.load('resources/images/cactus/cactus-2.png'),
            pygame.image.load('resources/images/cactus/cactus-3.png'),
            pygame.image.load('resources/images/cactus/cactus-4.png'),
            pygame.image.load('resources/images/cactus/cactus-5.png'),
            pygame.image.load('resources/images/cactus/cactus-6.png')
        ]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = x, 650
        self.speed = ground_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 0:
            self.rect.left = 1280
            self.image = random.choice(self.images)

    def check_collision(self, dinosaur):
        if self.rect.colliderect(dinosaur.rect):
            return True
        return False


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Initialize ground
        self.ground = pygame.image.load('resources/images/ground/ground.png')
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.left, self.ground_rect.bottom = 0, 650

        self.ground2 = pygame.image.load('resources/images/ground/ground.png')
        self.ground2_rect = self.ground2.get_rect()
        self.ground2_rect.left, self.ground2_rect.bottom = self.ground_rect.width, 650

        self.ground_speed = 8
        self.displacement = 0

    def draw(self, screen):
        screen.blit(self.ground, self.ground_rect)
        screen.blit(self.ground2, self.ground2_rect)

    def update(self):
        self.displacement += self.ground_speed
        if self.displacement >= self.ground_rect.width:
            self.displacement = 0

        self.ground_rect.left = 0 - self.displacement
        self.ground2_rect.left = self.ground_rect.width - self.displacement
