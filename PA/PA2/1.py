import pygame

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
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
        self.jump_time = 0
        self.status = 'run'
        self.is_crouching = False
        self.jump_height = [34, 34, 34, 34, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 17, 14, 10,
                            5, 1, -1, -5, -10, -14, -17,
                            -18, -19,
                            -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -34, -34,
                            -34. - 34]
    def stand_up(self):
        self.is_crouching = False

    def switch_image(self):
        if self.frame % 10 == 0:
            if not self.is_crouching:
                if self.image == self.images[0]:
                    self.image = self.images[1]
                else:
                    self.image = self.images[0]
            else:
                # Alternate between the two crouch images
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
        # Use crouch image when the character is crouching
        self.image = self.crouch_images[0]

    def stand_up_(self):
        self.is_crouching = False
        # Return to the running image when standing up
        self.image = self.images[0]

    def update(self):
        self.switch_image()
        if self.status == 'jump':
            self.rect.bottom -= self.jump_height[self.jump_time]
            self.jump_time += 1
            if self.jump_time == len(self.jump_height):
                self.status = 'run'
                self.jump_time = 0
                # Ensure that the dinosaur is within the screen bounds after jumping
                self.rect.bottom = min(self.rect.bottom, 640)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
