import pygame
import sys
import random
from dinosaur import Dinosaur
from obstacle import ObstacleManager
from scene import Ground, Moon, Cloud, Star, Scoreboard, EndingIcon

pygame.init()

obstacle_manager = ObstacleManager()

def main():
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dinosaur Game")

    ground = Ground()
    moon = Moon()
    clouds = [Cloud(random.randint(0, 1280), random.randint(50, 200), ground.ground_speed) for _ in range(3)]
    stars = [Star(random.randint(0, 1280), random.randint(50, 400), ground.ground_speed) for _ in range(5)]
    scoreboard = Scoreboard()
    ending_icon = EndingIcon()
    dinosaur = Dinosaur()

    clock = pygame.time.Clock()
    running = True
    # 音乐文件路径列表
    music_files = [
        'resources/jvke - this is what autumn feels like.flac',
        'resources/Mustard _ Roddy Ricch - BallinExplicit.flac',
        'resources/Anuo_ - Faded异域 (0_8X).ogg',  # 替换为下一首音乐文件的路径
        # 添加更多音乐文件路径
    ]

    # 初始化音乐索引
    current_music_index = 0

    # 播放第一首音乐
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()
    # 变量以指示音乐是否已经播放
    music_played = True

    # Create a sprite group for cacti
    cacti = pygame.sprite.Group()

    while running:
        #  Main game loop
        # 检查音乐是否已经播放完
        if not pygame.mixer.music.get_busy() and music_played:
            # 切换到下一首音乐
            current_music_index = (current_music_index + 1) % len(music_files)
            pygame.mixer.music.load(music_files[current_music_index])
            pygame.mixer.music.play()
            music_played = True  # 设置变量以指示音乐已经播放
        screen.fill('black')  # Change background color to black for night

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dinosaur.jump()

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            dinosaur.crouch()
        else:
            dinosaur.stand_up_()

        obstacle_manager.add_cactus(ground.ground_speed)
        obstacle_manager.update()
        obstacle_manager.draw(screen)

        ground.update()
        ground.draw(screen)

        moon.update()
        moon.draw(screen)

        for cloud in clouds:
            cloud.update()
            cloud.draw(screen)

        for star in stars:
            star.update()
            star.draw(screen)

        dinosaur.update()
        dinosaur.draw(screen)
        scoreboard.update()
        scoreboard.draw(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
