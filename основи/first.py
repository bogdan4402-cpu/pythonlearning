item_price = 9000
my_money = int(input("Товар коштує 9000, скільки грошей у вас є?:"))
if my_money >= item_price:
    print("У вас вистачає грошей")
else:
    print("Грошей замало, потрібно ще " + str(item_price - my_money))