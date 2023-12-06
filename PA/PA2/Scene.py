import pygame
import sys
import time


class Scene:
    class Ground:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True

        # create a ground image
        ground = pygame.image.load('resources/images/ground/ground.png')
        ground_rect = ground.get_rect()
        ground_rect.left, ground_rect.bottom = 0, 650

        # create a second ground image for continuous scrolling
        ground2 = pygame.image.load('resources/images/ground/ground.png')
        ground2_rect = ground2.get_rect()
        ground2_rect.left, ground2_rect.bottom = ground_rect.width, 650

        # game loop
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a white color
            screen.fill('white')

            # put both ground images on the screen
            screen.blit(ground, ground_rect)
            screen.blit(ground2, ground2_rect)

            # move both ground images
            ground_rect.left -= 8
            ground2_rect.left -= 8

            # check if either ground image is completely off the screen, then reset its position
            if ground_rect.right < 0:
                ground_rect.left = ground2_rect.right

            if ground2_rect.right < 0:
                ground2_rect.left = ground_rect.right

            # update the display
            pygame.display.update()

            # limit FPS to 60
            clock.tick(60)

        pygame.quit()
        sys.exit()
        pass

    import threading

    class Scene:
        class Ground:
            def __init__(self):
                # pygame setup
                pygame.init()
                self.screen = pygame.display.set_mode((1280, 720))
                self.clock = pygame.time.Clock()
                self.running = True

                # create a ground image
                self.ground = pygame.image.load('resources/images/ground/ground.png')
                self.ground_rect = self.ground.get_rect()
                self.ground_rect.left, self.ground_rect.bottom = 0, 650

                # create a second ground image for continuous scrolling
                self.ground2 = pygame.image.load('resources/images/ground/ground.png')
                self.ground2_rect = self.ground2.get_rect()
                self.ground2_rect.left, self.ground2_rect.bottom = self.ground_rect.width, 650

            def run(self):
                while self.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False

                    # fill the screen with a white color
                    self.screen.fill('white')

                    # put both ground images on the screen
                    self.screen.blit(self.ground, self.ground_rect)
                    self.screen.blit(self.ground2, self.ground2_rect)

                    # move both ground images
                    self.ground_rect.left -= 8
                    self.ground2_rect.left -= 8

                    # check if either ground image is completely off the screen, then reset its position
                    if self.ground_rect.right < 0:
                        self.ground_rect.left = self.ground2_rect.right

                    if self.ground2_rect.right < 0:
                        self.ground2_rect.left = self.ground_rect.right

                    # update the display
                    pygame.display.update()

                    # limit FPS to 60
                    self.clock.tick(60)

                pygame.quit()
                sys.exit()

        class DayNightCycle:
            def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((800, 600))
                self.clock = pygame.time.Clock()
                self.is_day = True
                self.cycle_duration = 120  # 2 minutes for each cycle
                self.start_time = time.time()

            def _init_(self):
                pygame.init()
                self.screen = pygame.display.set_mode((800, 600))
                self.clock = pygame.time.Clock()
                self.is_blood_moon = True
                self.cycle_duration = 240  # 2 minutes for each cycle
                self.start_time = time.time()

            def run(self):
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    elapsed_time = time.time() - self.start_time

                    if elapsed_time >= self.cycle_duration:
                        self.is_day = not self.is_day
                        self.start_time = time.time()

                    if self.is_day:
                        self.screen.fill('white')  # White color for day
                    elif self.is_blood_moon:
                        self.screen.fill('red')
                    else:
                        self.screen.fill('black')  # Black color for night

                    pygame.display.flip()
                    self.clock.tick(60)

    if __name__ == "__main__":
        scene = Scene()
        ground = scene.Ground()
        day_night_cycle = scene.DayNightCycle()

        # Start both the ground rendering and the day-night cycle in parallel
        pygame_thread = threading.Thread(target=ground.run)
        cycle_thread = threading.Thread(target=day_night_cycle.run)

        pygame_thread.start()
        cycle_thread.start()
        pygame_thread.join()
        cycle_thread.join()

    class Moon:
        pass

    class Cloud:
        pass

    class Star:
        pass

    class Scoreboard:
        pass

    class Endinglcon:
        pass
