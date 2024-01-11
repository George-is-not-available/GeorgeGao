import pygame
import random
import sys

from scene import Ground, Cloud, Star, Moon, Scoreboard
from dinosaur import Dinosaur
from obstacle import Cactus, Pterosaurs


# 定义一些全局变量
ctrl_pressed = False
skill_duration = 4000  # 技能持续时间（毫秒）
skill_start_time = 0 # 技能开始时间


def generate_image():

    image_path = 'resources/retouch_2023121221225532.png'
    image = pygame.image.load(image_path)
    return image


ctrl_pressed = False  # 用于跟踪 CTRL 键是否被按下
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
Moon = Moon()
time = 0
pterosaur = Pterosaurs(145, 600)
pterosaurs = pygame.sprite.Group()
pterosaur_timer = 0
pygame.display.set_caption('Fuck you~')

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

running = True
while running:

    cloud.update()
    cloud_1.update()
    cloud_2.update()

    if not pygame.mixer.music.get_busy() and music_played:
        # 切换到下一首音乐
        current_music_index = (current_music_index + 1) % len(music_files)
        pygame.mixer.music.load(music_files[current_music_index])
        pygame.mixer.music.play()
        music_played = True  # 设置变量以指示音乐已经播放

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            ctrl_pressed = True
        else:
            ctrl_pressed = False
    current_time = pygame.time.get_ticks()

    if cactus_timer == 70:
        cacti.add(Cactus()) or pterosaurs.add(Pterosaurs(1280, random.randint(110, 650)))
        cactus_timer = 0
    cactus_timer += 1
    for cactus in cacti:
        if pygame.sprite.collide_mask(dinosaur, cactus):
            dinosaur.die()
            running = False
    for pterosaur in pterosaurs:
        if pygame.sprite.collide_mask(dinosaur, pterosaur):
            dinosaur.die_2()
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinosaur.jump()
            elif event.key == pygame.K_DOWN and dinosaur.status == 'run':
                dinosaur.duck()
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and dinosaur.status == 'duck':
                dinosaur.run()
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                ctrl_pressed = False

    if ctrl_pressed:
        # 激活技能 - 让所有鸟和仙人掌向上平移直到看不见，然后删除它们
        if current_time - skill_start_time < skill_duration:
            # 在恐龙的位置生成一张图片
            generated_image = generate_image()
            # 绘制生成的图片在恐龙的位置
            screen.blit(generated_image, (dinosaur.rect.x, dinosaur.rect.y))
            for entity in pterosaurs.sprites() + cacti.sprites():
                while entity.rect.bottom > 0:
                    entity.rect.y -= 10  # 调整平移速度
                    screen.fill('black')
                    # 重新绘制所有实体
                    Moon.draw(screen)
                    cloud.update()
                    cloud.draw(screen)
                    cloud_1.update()
                    cloud_1.draw(screen)
                    cloud_2.update()
                    cloud_2.draw(screen)
                    ground.update()
                    ground.draw(screen)
                    cacti.update()
                    dinosaur.update()
                    cacti.draw(screen)
                    pterosaurs.update()
                    pterosaurs.draw(screen)
                    s.update(time, 13)
                    s.draw(screen)
                    pygame.display.flip()
                    clock.tick(60)

        else:
            # 技能时间到，重置标志和时间
            ctrl_pressed = False
            skill_start_time = 0

    pterosaur_timer += 1
    time += 1

    screen.fill('black')
    Moon.update()
    Moon.draw(screen)
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
    s.update(time,30)
    s.draw(screen)
    pygame.display.flip()
    clock.tick(60)
screen.fill('black')
text = font.render('Ops!', True, 'yellow')
text_rect = text.get_rect()
text_rect.left, text_rect.bottom = 540, 420
screen.blit(text, text_rect)

pygame.display.flip()
while not running:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dinosaur.jump()
            elif event.key == pygame.K_DOWN and dinosaur.status == 'run':
                dinosaur.duck()
            elif event.key == pygame.K_r and not running:
                # Restart the game if 'R' is pressed
                running = True
                cloud.reset_position()
                cloud_1.reset_position()
                cloud_2.reset_position()
                cacti.empty()
                pterosaurs.empty()
                dinosaur.reset()
                s.update(0, 10)
                time = 0
pygame.quit()
