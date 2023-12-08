import pygame
from obstacle import ObstacleManager


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = (
            pygame.image.load('resources/images/dinosaur/dinosaur-run-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-run-2.png')
        )
        self.crouch_images = (
            pygame.image.load('resources/images/dinosaur/dinosaur-duck-1.png'),
            pygame.image.load('resources/images/dinosaur/dinosaur-duck-2.png')
        )
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = 30, 637
        self.frame = 0
        self.jump_time = 2
        self.status = 'run'
        self.is_crouching = False
        self.jump_height = [29, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 17, 14, 10,
                            5, 1, -1, -5, -10, -14, -17,
                            -18, -19,
                            -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -29]

        self.mask = pygame.mask.from_surface(self.image)

    def stand_up(self):
        self.is_crouching = False

    def switch_image(self):
        if self.frame % 10 == 0:
            if not self.is_crouching:
                self.image = self.images[1] if self.image == self.images[0] else self.images[0]
            else:
                self.image = self.crouch_images[self.frame % len(self.crouch_images)]
        self.frame += 1

    def jump(self):
        if self.status != 'jump':
            self.status = 'jump'
            pygame.mixer.Sound('resources/audios/jump.mp3').play()
            self.image = pygame.image.load('resources/images/dinosaur/dinosaur-jump.png')
            self.jump_time = 0  # Reset jump time when initiating a jump

    def crouch(self):
        self.is_crouching = True

    def stand_up_(self):
        self.is_crouching = False

    def die(self):
        self.status = 'die'
        self.image = pygame.image.load('resources/images/dinosaur/dinosaur-die.png')
        self.rect.y += 10  # Adjust the position after death for better visual
        self.mask = pygame.mask.from_surface(self.image)

    def switch_image_die(self):
        if self.status == 'die':
            self.rect.y += 5  # Move the dinosaur downward for a falling effect
            if self.rect.y > 720:  # Check if the dinosaur is below the screen
                self.rect.y = 720  # Keep it at the bottom of the screen
                self.status = 'dead'  # Change status to 'dead' after falling off the screen

    def update(self, obstacles):
        self.switch_image()
        if self.status == 'jump':
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.status = 'run'
                self.jump_time = 0
                self.rect.bottom = min(self.rect.bottom, 640)

        self.switch_image_die()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Test")

    dinosaur = Dinosaur()

    clock = pygame.time.Clock()
    running = True

    obstacle_manager = ObstacleManager()  # Assuming you have an ObstacleManager class

    def die(self):
        self.state = "die"
        self.refresh_time = 0
        self.image_id = 0
        self.image_current_list.clear()
        self.image_current_list.extend(self.image_die_list)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dinosaur.die()

        screen.fill((255, 255, 255))

        obstacle_manager.update()
        obstacle_manager.draw(screen)

        dinosaur.update(obstacle_manager.cacti)
        dinosaur.draw(screen)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
