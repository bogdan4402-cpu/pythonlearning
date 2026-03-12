def analyze_spending(expenses):
    total = sum(expenses)
    if total >= 1000:
        print("Перевищення бюджету!")
    return total

my_expenses = []
while True:
    value = input("Введіть витрату (або 'стоп'): ") 
    if value == "стоп":
        break
    my_expenses.append(int(value))
print("Загальна сума:", analyze_spending(my_expenses))

