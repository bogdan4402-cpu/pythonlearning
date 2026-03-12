import random
import time
words = "Звісно","Так","50 на 50","Всяке може бути","Звичайно так!","Я в тебе вірю" 
colors = ["\033[92m", "\033[91m", "\033[94m", "\033[95m"]
while True:
    user_query = input("Запитай мене про щось: ")
    c = random.choice(colors)
    time.sleep(1)
    print(f"{c}{random.choice(words)}\033[0m")
    user_query.lower() == 'стоп'
    break
    