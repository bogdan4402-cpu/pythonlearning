def calculate_result(grades):
    if not grades:
        return "Список оцінок порожній"
    
    average = sum(grades) / len(grades)
    if average >= 75:
        return f"\033[92m Середній бал: {average}: Клас готовий до іспиту! \033[0m"
    else: 
        return f"\033[91m Середній бал: {average}: Клас не готовий, потрібно більше практики! \033[0m"

user_grades = []
while True:
    entry = input("Введіть оцінку учня (або 'стоп' для завершення: ") # Додали input
    if entry.lower() == "стоп":
        break
    user_grades.append(int(entry)) # Додаємо число в список 

print(calculate_result(user_grades))
