import time
import os
while True:
    note = input("Введи нотатку (Або 'стоп' для виходу: ")
    if note.lower() == "стоп":
        break
    current_time = time.ctime()
    
    with open("notes.txt", "a") as file:
        file.write(f"[{current_time}] {note}\n")
    
    print("Записано!")
os.startfile("notes.txt")
   
        