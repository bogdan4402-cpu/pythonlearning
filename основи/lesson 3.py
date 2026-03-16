sprava = []


task1 = input("Яку справу №1 ви хочете додати?: ")
sprava.append(task1)
task2 = input("Яку справу №2 ви хочете додати?: ")
sprava.append(task2)
task3 = input("Яку справу №3 ви хочете додати?: ")
sprava.append(task3)
for i in range(3):
    print("Справа №" + str(i + 1) + ": " + sprava[i])

    
    


