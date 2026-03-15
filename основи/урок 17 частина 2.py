import time
import os

if not os.path.exists("notes.txt"):
    with open("notes.txt", "w") as file:
        file.write("Це автоматично створений файл.\n")
    print("Файл не знайдено тому я його створив")


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
    
    current_time = time.ctime() 
    if save_note(f"[{current_time}] {note}"):
     print("Записано!")
    else:
     print("Помилка у записі файлу")


try:
    print("\n--- Твій файл --- ")
    with open("notes.txt", "r") as file:
     os.startfile("notes.txt")
except FileNotFoundError:
    print("Упс! Схоже файл  notes.txt кудись зник!")
    
   
        