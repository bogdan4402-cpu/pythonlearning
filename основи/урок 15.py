def analyze_steps(steps):
 average = sum(steps) / len(steps) # Середня сума рахується
 if average > 10000:
     return f"Середній результат: {average:.2f} кроків. \033[92mГарний темп!\033[0m" # Повертаємо зелений текст
 else:
     return f"Середній результат: {average:.2f} кроків. \033[91mБільше рухайтесь!\033[0m" # Повертаємо червоний текст 
results = []
while True:
    entry = (input("Скільки шагів ви пройшли за день? напишіть 'стоп' для підрахунку: "))
    if entry.lower() == "стоп":
        break
    try:
        if float(entry) > 0:
            results.append(float(entry))
        else:
            print("\033[91mВведіть число більше нуля!\033[0m")
    except ValueError:
        print("Будь-ласка увведіть вірне число")
if results:
    print("Ви пройшли:", ((analyze_steps(results))))
else:
    print("Даних для підрахунку немає")


    