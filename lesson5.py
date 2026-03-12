basket = []
print("Введіть товари (Напишіть 'стоп'), щоб завершити):")

while True:
    item = input("Продукт:  ")
    if item == "стоп":
        break # гальмо яке зупиняє цикл
    basket.append(item)

print("\nВаш готовий список:")
for i in range(len(basket)):
    print(str(i + 1) + ".  " + basket[i])
    
    # len(basket) автоматично дізнається довжину списку [3]
