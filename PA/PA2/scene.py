import pygame
import sys


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        self.ground = pygame.image.load('resources/images/ground/ground.png')
        self.ground_rect = self.ground.get_rect()
        self.ground_rect.left, self.ground_rect.bottom = 0, 650

        self.ground2 = pygame.image.load('resources/images/ground/ground.png')
        self.ground2_rect = self.ground2.get_rect()
        self.ground2_rect.left, self.ground2_rect.bottom = self.ground_rect.width, 650

    def draw(self):
        self.screen.blit(self.ground, self.ground_rect)
        self.screen.blit(self.ground2, self.ground2_rect)

    def update(self):
        self.ground_rect.left -= 8
        self.ground2_rect.left -= 8

        if self.ground_rect.right < 0:
            self.ground_rect.left = self.ground2_rect.right

        if self.ground2_rect.right < 0:
            self.ground2_rect.left = self.ground_rect.right

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            self.draw()
            self.update()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/moon/moon.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('resources/images/cloud/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('resources/images/star/star.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EndingIcon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/images/end_icon/end_icon.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


if __name__ == "__main__":
    game = Ground()
    game.run()
