party_guest = []
print("Скільки гостей буде? Напишіть їх імена сюди: ")


while True:
    item = input("Гість: ")
    if item == "Досить":
        break

    if item == "Адмін":
     print("Привіт, Бос! Вас немає у списку, ви поза чергою")
     continue

    party_guest.append(item)

print("\nВаш готовий список:")
for i in range(len(party_guest)):
    print(str(i + 1) + ". " + party_guest[i])



