import os
import random

folder = "/home/bogdan/Картинки/X"

extensions = (".jpg", ".jpeg", ".png", ".mp4", ".mkv", ".avi")

files = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]

random.shuffle(files)

for file in files:
    path = os.path.join(folder, file)

    print("Открывается:", file)

    os.system(f'xdg-open "{path}"')

    input("Нажми Enter для следующего...")