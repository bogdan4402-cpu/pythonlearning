def add_task(name):
    tasks.append(name) # Додаємо елемент у список
    print(f"Завдання '{name}' додано!")

def show_tasks():
    print("\n---  Список справ ---")
    for i, task in enumerate(tasks, 1): # Виводимо нумерацію 
        print(f"{i} {task}")

tasks=[]

while True:
    print("\n1. Додати завдання\n2. Показати список\n3. Вихід")
    choice = input("Обери дію:")
    
    if choice == '1':
        t_name = input("Що потрібно зробити?: ")
        add_task(t_name)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("Бувай!")
        break
    else:
        print("Невірний вибір, спробуй ще раз")
