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