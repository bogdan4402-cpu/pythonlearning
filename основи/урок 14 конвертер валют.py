
def to_uah(dollars):
     return dollars * 42
results = []
while True:
    entry = (input("Скільки грошей у вас в доларах? Введіть 'стоп' якщо хочете отримати результат "))
    if entry.lower() == "стоп":
        break
    else:
     amount_in_uah = to_uah(float(entry))
    results.append(amount_in_uah)
print("Ось ваш результат:", sum(results))
        