import time
with open("notes.txt", "a") as file:
 note = input("Введи свою замітку: ")
 current_time = time.ctime()
 file.write(f"[{current_time}] {note}\n")