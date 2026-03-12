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
    else: 
        try:
            results.append(float(entry))
        except ValueError: # Якщо замість введеного числа будуть букви програма не вилетить а напише уведіть число
               print("Будь ласка уведіть вірне число")
if len(results) > 0:
    print("\033[91mВи не ввели жодних данних!")
else:
    print("Ви пройшли:", ((analyze_steps(results))))


    
    