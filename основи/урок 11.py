def get_final_price(price, discount):
    if discount > price:
        return "Помилка: Знижка більше за ціну"
    return price - discount

user_p = int(input("Яка ціна продукту?: "))
user_d = int(input("Яка знижка на продукт?: "))
print("Ваша ціна зі знижкою буде: ", get_final_price(user_p, user_d))




    