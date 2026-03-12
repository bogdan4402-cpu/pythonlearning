basket = []
for i in range(3):
    item = input("Що додати в список?: ")
    basket.append(item)
print("\nВаш список покупок:")
for i in range(3):
    print("Покупка №" + str(i + 1) + ": " + basket[i])

    #Як написати список з добавлянням своїх продуктів але не більше 3х