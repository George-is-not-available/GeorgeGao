# scene.py
import pygame
import random

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.color_reversed = False
        self.start_time = pygame.time.get_ticks()

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

class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        self.speed = ground_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left -= self.speed
        if self.rect.right < 0:
            self.rect.left = 1280
            self.rect.top = random.randint(50, 200)

class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_speed):
        super().__init__()
        self.image = pygame.image.load('resources/images/star/star-2.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = ground_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.images = [
            pygame.image.load('resources/images/scoreboard/scoreboard-0.png'),
            # Add other images here
        ]
        self.image_score = pygame.Surface((20 * 5, 21))

    def get_score(self, ground):
        # Get score from ground
        self.score = ground.displacement // 100  # Adjust this based on your scoring mechanism

        # Play a sound every time the score reaches a multiple of 100
        if self.score and not self.score % 100:
            pygame.mixer.Sound('resources/audios/score.mp3').play()

    def update(self):
        # Update the scoreboard image
        self.image_score.fill((255, 255, 255))

        # Add image to scoreboard
        for i in range(5):
            self.image_score.blit(self.images[0], (20 * i, 0))  # Fix the index to 0

        self.image_score.set_alpha(255)

    def draw(self, screen):
        # Draw the scoreboard on the screen
        screen.blit(self.image_score, (10, 10))

class EndingIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/ending/game-over.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, ground_speed):
        super().__init__()
        self.images = [
            pygame.image.load('resources/images/cactus/cactus-1.png'),
            # Add other cactus images here
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
