import time
import os
def save_note(text):    
    try:
        with open("notes.txt", "a") as file:
            file.write(text + "\n")
        return True
    except Exception:
        return False
       

while True:
    note = input("Введи нотатку (або 'стоп' для виходу): ")
    if note.lower() == "стоп":
        break
    
    current_time = time.ctime() # Отримуємо час тут
     # Викликаємо нашу функцію і передаємо їй сформований текст 
if save_note(f"[{current_time}] {note}"):
        print("Записано!")
else:
    print("Помилка у записі файлу")

print("\n--- Твій файл --- ")
try:
    with open("notes.txt", "r") as file:
        print(file.read())
    os.startfile("notes.txt")
except FileNotFoundError:
    print("Упс! Схоже файл  notes.txt кудись зник!")
    
   
        