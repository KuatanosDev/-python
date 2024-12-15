import random

print("Выберите уровень сложности:")
print("1. Легкий")
print("2. Средний")
print("3. Сложный")
print("4. Безумие")
a = int(input())

if a == 1:  # Легкий
    print("Вы выбрали легкий уровень, Угадайте число от 1 до 10")
    b = random.randint(1, 10)
    while True:
        c = int(input("Введите число: "))
        if c > b:
            print("Меньше")
        elif c < b:
            print("Больше")
        else:
            print("Вы угадали число!")
            break

elif a == 2:  # Средний
    print("Вы выбрали средний уровень, Угадайте число от 1 до 100")
    b = random.randint(1, 100)
    while True:
        c = int(input("Введите число: "))
        if c > b:
            print("Меньше")
        elif c < b:
            print("Больше")
        else:
            print("Вы угадали число!")
            break

elif a == 3:  # Сложный
    print("Вы выбрали сложный уровень, Угадайте число от 1 до 1000")
    b = random.randint(1, 1000)
    while True:
        c = int(input("Введите число: "))
        if c > b:
            print("Меньше")
        elif c < b:
            print("Больше")
        else:
            print("Вы угадали число!")
            break

elif a == 4:  # Безумие
    print("Вы выбрали безумие уровень, Угадайте число от 1 до 1000000")
    b = random.randint(1, 1000000)
    while True:
        c = int(input("Введите число: "))
        if c > b:
            print("Меньше")
        elif c < b:
            print("Больше")
        else:
            print("Вы угадали число!")
            break

else:
    print("Неверный выбор уровня сложности!")
