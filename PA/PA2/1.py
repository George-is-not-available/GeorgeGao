# Initialize Pygame
pygame.init()
# Set up the screen
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dinosaur Game")
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

#  Main game loop
while ground.running:
    screen.fill('black')
    ground.draw_background(screen)
    # 检查音乐是否已经播放完
    if not pygame.mixer.music.get_busy() and music_played:
        # 切换到下一首音乐
        current_music_index = (current_music_index + 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_music_index])
        pygame.mixer.music.play()
        music_played = True  # 设置变量以指示音乐已经播放




        ###############################
        import pygame
        import random
        from scene import Ground, Cloud, Scoreboard, Moon, Star
        from dinosaur import Dinosaur
        from obstacle import Cactus, Pterosaurs

        moon = Moon()
        clouds = [Cloud(random.randint(0, 1280), random.randint(50, 200), ground.ground_speed) for _ in range(3)]
        stars = [Star(random.randint(0, 1280), random.randint(50, 400), ground.ground_speed) for _ in range(5)]
        font = pygame.font.Font(None, 75)
        pygame.init()
        screen = pygame.display.set_mode((1280, 820))
        clock = pygame.time.Clock()
        ground = Ground()
        cloud = Cloud(1000, 300)
        cloud_1 = Cloud(2000, 350)
        cloud_2 = Cloud(1500, 400)
        dinosaur = Dinosaur()
        cactus = Cactus()
        cacti = pygame.sprite.Group()
        cactus_timer = 0
        s = Scoreboard()
        time = 0
        pterosaur = Pterosaurs(1243, 600)
        pterosaurs = pygame.sprite.Group()
        pterosaur_timer = 0
        pygame.display.set_caption('slave out of the dungeon')
        pygame.mixer.init()
        pygame.mixer.music.load('resources/audios/kun_man.mp3')
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    dinosaur.jump()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and dinosaur.status == 'run':
                        dinosaur.duck()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN and dinosaur.status == 'duck':
                        dinosaur.run()
                if cactus_timer == 80:
                    cacti.add(Cactus())
                    cactus_timer = 0
            cactus_timer += 1
            for cactus in cacti:
                if pygame.sprite.collide_mask(dinosaur, cactus):
                    dinosaur.die()
                    running = False
            if pterosaur_timer == 209:
                pterosaurs.add(Pterosaurs(1280, random.randint(100, 650)))
                pterosaur_timer = 0
            for pterosaur in pterosaurs:
                if pygame.sprite.collide_mask(dinosaur, pterosaur):
                    dinosaur.die_2()
                    running = False
            pterosaur_timer += 1
            time += 1
            screen.fill('white')
            cloud.update()
            cloud.draw(screen)
            cloud_1.update()
            cloud_1.draw(screen)
            cloud_2.update()
            cloud_2.draw(screen)
            cacti.update()
            ground.update()
            ground.draw(screen)
            dinosaur.update()
            dinosaur.draw(screen)
            cacti.draw(screen)
            pterosaurs.update()
            pterosaurs.draw(screen)
            s.update(time, 15)
            s.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            screen.fill('black')
            text = font.render('Do it Again', True, 'pink')
            text_rect = text.get_rect()
            text_rect.left, text_rect.bottom = 540, 420
            screen.blit(text, text_rect)

        for star in stars:
            star.update()
            star.draw(screen)

    pygame.display.flip()
    while not running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
        pygame.quit()

    ##################

