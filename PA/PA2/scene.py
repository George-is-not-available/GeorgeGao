import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load('resources/images/ground/ground.png')
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.left, self.ground_rect.bottom = 0, 650

        self.ground_other = pygame.image.load('resources/images/ground/ground.png')
        self.ground_other_rect = self.ground_other.get_rect()
        self.ground_other_rect.left, self.ground_other_rect.bottom = self.ground_rect.right, 650
        self.displacement = 0

    def update(self):
        self.ground_rect.left -= 10
        self.ground_other_rect.left -= 10
        self.displacement += 10
        if self.ground_rect.right < 0:
            self.ground_rect.left = self.ground_other_rect.right
        if self.ground_other_rect.right < 0:
            self.ground_other_rect.left = self.ground_rect.right

    def draw(self, screen):
        screen.blit(self.ground, self.ground_rect)
        screen.blit(self.ground_other, self.ground_other_rect)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('resources/images/cloud/cloud.png')
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Move the cloud to the left
        self.rect.x -= 1

        # Reset the cloud's position when it goes off the screen
        if self.rect.right < 0:
            self.rect.x = 1280

    def reset_position(self):
        self.rect.left = 1280
        self.rect.bottom = random.randint(50, 300)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score_y = 40
        self.score_x = 1140
        self.score = 0
        self.images = list()
        for i in range(10):
            self.images.append(pygame.image.load(f'resources/images/scoreboard/scoreboard-{i}.png'))
        self.images = tuple(self.images)
        print(self.images)
        self.image_score = pygame.Surface((20 * 5, 21))

    def update(self, time, v):
        self.score = time * v * 0.015
        self.image_score.fill('black')
        self.score = list(str(int(self.score)))
        print(self.score)
        for i in range(5 - len(self.score)):
            self.score.insert(0, '0')
        print(self.score)
        # add image to scoreboard
        for i in range(5):
            self.image_score.blit(self.images[int(self.score[i])], (20 * i, 0))

        self.image_score.set_alpha(255)  # use set_alpha to make surface background transparent

    def draw(self, screen):
        screen.blit(self.image_score, (self.score_x, self.score_y))


class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/moon/moon-2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 1000, 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)


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


