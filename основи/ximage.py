import os
import random
import pygame
from moviepy import VideoFileClip

# Папка з медіа
folder = "/home/bogdan/Картинки/X"
extensions_img = (".jpg", ".jpeg", ".png")
extensions_vid = (".mp4", ".mkv", ".avi")

files = [f for f in os.listdir(folder) if f.lower().endswith(extensions_img + extensions_vid)]
random.shuffle(files)

# Початкові налаштування
WIN_W, WIN_H = 800, 600
pygame.init()
# Використовуємо тільки DOUBLEBUF (HWSURFACE іноді заважає на нових ядрах Linux)
screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Media Viewer")

index = 0
zoom_level = 1.0
is_fullscreen = False

def show_image(path, zoom):
    curr_w, curr_h = screen.get_size()
    screen.fill((0, 0, 0))
    
    try:
        # Використовуємо .convert() для прискорення
        img = pygame.image.load(path).convert()
        img_w, img_h = img.get_size()

        base_ratio = min(curr_w / img_w, curr_h / img_h)
        new_size = (int(img_w * base_ratio * zoom), int(img_h * base_ratio * zoom))
        
        # smoothscale дає найкращу картинку
        img = pygame.transform.smoothscale(img, new_size)
        
        x = (curr_w - new_size[0]) // 2
        y = (curr_h - new_size[1]) // 2
        
        screen.blit(img, (x, y))
        pygame.display.flip()
    except Exception as e:
        print(f"Помилка: {e}")

def apply_display_mode():
    global screen
    # Перемикаємо режим
    if is_fullscreen:
        # Режим (0,0) з FULLSCREEN — це "рідна" роздільна здатність монітора
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    else:
        screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.RESIZABLE | pygame.DOUBLEBUF)
    
    # --- МЕТОД ГРУБОЇ СИЛИ ДЛЯ LINUX ---
    # Малюємо 3 порожні кадри, щоб виштовхнути "сміття" з пам'яті відеокарти
    for _ in range(3):
        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.delay(30) # Коротка пауза, щоб ОС встигла "зрозуміти" зміни
        pygame.event.pump()

running = True
redraw = True

while running:
    if not files: break
    path = os.path.join(folder, files[index])

    if redraw:
        if files[index].lower().endswith(extensions_img):
            show_image(path, zoom_level)
        else:
            # MoviePy preview
            clip = VideoFileClip(path)
            clip.preview()
            apply_display_mode() # Повертаємо вікно після відео
        redraw = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.VIDEORESIZE and not is_fullscreen:
            redraw = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: # Колесо вгору
                zoom_level += 0.1
                redraw = True
            elif event.button == 5: # Колесо вниз
                zoom_level = max(0.1, zoom_level - 0.1)
                redraw = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(files)
                zoom_level = 1.0
                redraw = True
            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(files)
                zoom_level = 1.0
                redraw = True
            elif event.key == pygame.K_f:
                is_fullscreen = not is_fullscreen
                apply_display_mode()
                redraw = True
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()